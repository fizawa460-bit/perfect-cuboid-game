#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

CONTRACT = HERE / "TRANSPORT_SUPPORT_RELAXATION_CLOSURE_CONTRACT.md"
RESEARCH = HERE / "verify_n359_transport_support_relaxation_closure.py"
RESULT = HERE / "RESULT.json"
STATE = HERE / "STATE.json"
HANDOFF = HERE / "AUDIT-HANDOFF.json"

LOCKS = {
    "contract": (CONTRACT, "1366eb2d950b1d7d714452aeff821393ece2830e"),
    "research_verifier": (RESEARCH, "995207ae5ef70fa8ffdcb54ecd9b6dbecedf1f10"),
    "result": (RESULT, "0fdf087fd87506908e29da86b6de712820c13877"),
    "state": (STATE, "8ff1045cd495e6f5a69b42079ecced1338aa84fc"),
    "audit_handoff": (HANDOFF, "3ccbdbc481fd4d84c825470d3e8a812d6195258d"),
    "n356_contract": (ROOT / "stages/stage32/32-01-178/nodes/N356/OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CAP_CONTRACT.md", "d2353cab9c175a680067c7ad4c24759b6dd15df3"),
    "n357_engine": (ROOT / "stages/stage32/32-01-178/nodes/N357-engine/verify_n357_transport_support_capacity.py", "479c783cb42d0952cc310708106787147b499240"),
    "n358_contract": (ROOT / "stages/stage32/32-01-178/nodes/N358/JOINT_TRANSPORT_SUPPORT_SATURATION_CONTRACT.md", "a9a6836dc201feefd37bebb2f6c0ef42e8faaee4"),
    "n358_result": (ROOT / "stages/stage32/32-01-178/nodes/N358/RESULT.json", "e42c2b6cc6128c4666372b0c3f3c172afc006d7f"),
    "n358_audit_receipt": (ROOT / "stages/stage32/32-01-178/nodes/N358/HOSTILE-AUDIT-PASS.json", "7b36e0159987ef65485d36fa2d672c8ee3a1ff33"),
    "n358_consumed_state": (ROOT / "stages/stage32/32-01-178/nodes/N358/STATE.json", "6091b0da0acc3fb4b3b2143327f7d57f5323668e"),
    "full178_manifest": (ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json", "0a46b34e278688240656b4977e9cb7f589e90e06"),
    "claim_frontier_workflow": (ROOT / ".github/workflows/stage32-claim-frontier-integrity.yml", "ae336bb7eb0e1e36eb219f0a211984dc14b9ca3a"),
}

EXPECTED_RESULT_CANONICAL = "349c52bf40ca931c94cffbf37e34757f4069a4343f9c165a3f8f14424bd74c6e"
EXPECTED_STATE_CANONICAL = "3e5b0edf27d998228024df01e5397aefbd56349985d1e6abdb3933ec72f9dab8"
EXPECTED_HANDOFF_CANONICAL = "110e59c0e41b05fe60137ab06d262f235c4030ea143f1fac90500aa29e133ced"
EXPECTED_N358_REVIEW = 5184322011
EXPECTED_STRATA = 17_128
EXPECTED_TERMINALS = 47_589_703_313_957_134_966_240


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"self canonical regression: {path}")
    actual = canonical(obj)
    if actual != expected:
        raise ValueError(f"recomputed canonical regression: {path}: {actual}")
    return obj


def require_false(mapping: dict, keys: tuple[str, ...], label: str) -> None:
    for key in keys:
        if mapping.get(key) is not False:
            raise ValueError(f"{label} firewall regression: {key}")


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"{name} source-lock regression: {actual} != {expected}")

    result = load_canonical(RESULT, EXPECTED_RESULT_CANONICAL)
    state = load_canonical(STATE, EXPECTED_STATE_CANONICAL)
    handoff = load_canonical(HANDOFF, EXPECTED_HANDOFF_CANONICAL)

    if result.get("status") != "AUDIT_CANDIDATE_ROUTE_EXHAUSTION_NO_NEW_PRUNING_CREDIT":
        raise ValueError("N359 RESULT status regression")
    authority = result.get("authority_input", {})
    if authority.get("hostile_audit_review_id") != EXPECTED_N358_REVIEW or authority.get("n358_main_pruning_credit") is not True:
        raise ValueError("N359 N358 authority regression")
    claim = result.get("claim", {})
    if claim.get("additional_rejected_exceptional_prefixes") != 0 or claim.get("additional_rejected_terminals") != 0:
        raise ValueError("N359 zero-pruning result regression")
    if claim.get("candidate_remaining_strata") != EXPECTED_STRATA or claim.get("candidate_remaining_terminals") != EXPECTED_TERMINALS:
        raise ValueError("N359 retained frontier regression")
    if claim.get("transport_support_relaxation_route_exhausted_if_audited") is not True:
        raise ValueError("N359 route-exhaustion candidate regression")

    semantics = result.get("semantics", {})
    if semantics.get("n358_main_pruning_credit") is not True or semantics.get("route_exhaustion_requires_external_hostile_audit") is not True:
        raise ValueError("N359 authority/audit firewall regression")
    require_false(semantics, (
        "n359_main_pruning_credit", "full178_complete", "n350_producer_registered",
        "production_complete", "n104_release", "receiver_credit", "theorem_credit",
        "endpoint_credit", "stage32_closed", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim", "heavy_compute_authorized", "merge_authorized",
    ), "N359 RESULT")

    if state.get("status") != "AUDIT_REQUIRED_ROUTE_EXHAUSTION_NO_NEW_PRUNING_CREDIT":
        raise ValueError("N359 STATE status regression")
    cand = state.get("candidate", {})
    if cand.get("result_canonical_sha256") != EXPECTED_RESULT_CANONICAL or cand.get("additional_rejected_terminals") != 0:
        raise ValueError("N359 STATE candidate regression")
    credit = state.get("credit", {})
    if credit.get("n358_main_pruning_credit") is not True:
        raise ValueError("N359 STATE lost N358 credit")
    require_false(credit, (
        "n359_main_pruning_credit", "transport_support_relaxation_route_exhausted",
        "full178_complete", "n350_producer_registered", "production_complete",
        "n104_release", "receiver_credit", "theorem_credit", "endpoint_credit",
        "stage32_closed", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
        "heavy_compute_authorized", "merge_authorized",
    ), "N359 STATE")

    if handoff.get("status") != "READY_FOR_INDEPENDENT_HOSTILE_AUDIT_NO_NEW_MAIN_PRUNING_CREDIT":
        raise ValueError("N359 AUDIT-HANDOFF status regression")
    hc = handoff.get("candidate", {})
    if hc.get("additional_rejected_terminals") != 0 or hc.get("candidate_remaining_terminals") != EXPECTED_TERMINALS:
        raise ValueError("N359 AUDIT-HANDOFF candidate regression")
    hlocks = handoff.get("source_locks", {})
    for key in ("contract", "research_verifier", "result", "state", "n356_contract", "n357_engine",
                "n358_contract", "n358_result", "n358_audit_receipt", "n358_consumed_state",
                "full178_manifest", "claim_frontier_workflow"):
        if hlocks.get(key, {}).get("blob_sha1") != LOCKS[key][1]:
            raise ValueError(f"N359 handoff source-lock regression: {key}")
    if handoff.get("audit_verifier_path") != "stages/stage32/32-01-178/nodes/N359/verify_n359_audit_source_locks.py":
        raise ValueError("N359 audit verifier path regression")

    proc = subprocess.run(
        [sys.executable, str(RESEARCH)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        raise ValueError(f"N359 research verifier failed:\n{proc.stdout}")
    marker = "PASS_N359_OPTIMISTIC_TRANSPORT_SUPPORT_RELAXATION_CLOSURE_AUDIT_CANDIDATE"
    if marker not in proc.stdout:
        raise ValueError("N359 research verifier PASS marker missing")
    payload = json.loads(proc.stdout.strip().splitlines()[-1])
    if payload.get("additional_rejected_terminals") != 0:
        raise ValueError("N359 replay unexpectedly prunes")
    if payload.get("n358_is_exact_joint_projection_of_n356_n357_relaxation") is not True:
        raise ValueError("N359 exact-projection replay regression")

    print(json.dumps({
        "verdict": "PASS_N359_FROZEN_AUDIT_BOUNDARY_ROUTE_EXHAUSTION_IDENTITY",
        "result_canonical_sha256": EXPECTED_RESULT_CANONICAL,
        "state_canonical_sha256": EXPECTED_STATE_CANONICAL,
        "handoff_canonical_sha256": EXPECTED_HANDOFF_CANONICAL,
        "source_remaining_strata": EXPECTED_STRATA,
        "source_remaining_terminals": EXPECTED_TERMINALS,
        "additional_rejected_terminals": 0,
        "candidate_remaining_terminals": EXPECTED_TERMINALS,
        "n359_main_pruning_credit": False,
        "route_exhaustion_audit_required": True,
        "retained_artifact_identity_fail_closed": True,
        "research_replay": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
