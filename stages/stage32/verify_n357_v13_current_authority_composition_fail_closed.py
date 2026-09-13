#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURRENT_REPLAY = ROOT / "stages/stage32/verify_n357_v13_current_authority_composition.py"
CURRENT_RECEIPT = ROOT / "stages/stage32/management/N357-V13-CURRENT-AUTHORITY-COMPOSITION.json"
CURRENT_STATE = ROOT / "stages/stage32/MAIN-STATE.json"

AUDITED_HEAD = "0d787839b7e0dad4a42108c61d16e7849c50862f"
AUDITED_REVIEW = 5183069892
EXPECTED = {
    "result": (
        "stages/stage32/32-01-178/nodes/N357/RESULT.json",
        "50014d453266ad79101910a943d14388bd3ef6ec",
    ),
    "engine": (
        "stages/stage32/32-01-178/nodes/N357-engine/verify_n357_transport_support_capacity.py",
        "479c783cb42d0952cc310708106787147b499240",
    ),
    "audit_state": (
        "stages/stage32/32-01-178/nodes/N357/AUDIT-STATE.json",
        "9fdca61ce325023bc050016d3a81787e225b0962",
    ),
    "audit_handoff": (
        "stages/stage32/32-01-178/nodes/N357/AUDIT-HANDOFF.json",
        "253c5fb4ed5cced2c033cbfa0ffe4b9eb3c107bf",
    ),
    "audit_source_lock_verifier": (
        "stages/stage32/32-01-178/nodes/N357/verify_n357_audit_source_locks.py",
        "9ce7477652b234e3424236bd2e61232fb38510d2",
    ),
}
EXPECTED_RESULT_CANONICAL = "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"
EXPECTED_INCREMENT = 17797986705435299826016
EXPECTED_SOURCE = 65396964990500233636214
EXPECTED_OLD_RESIDUAL = 47598978285064933810198
EXPECTED_CURRENT_V13 = 65396964990500233609659
EXPECTED_CURRENT_RESIDUAL = 47598978285064933783643


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(f"FAIL: {message}")


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(isinstance(obj, dict), f"expected JSON object: {path}")
    return obj


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("s32_audited_n357_engine", path)
    req(spec is not None and spec.loader is not None, "cannot load audited N357 engine")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-n357-root", type=Path, required=True)
    args = ap.parse_args()
    audited = args.audited_n357_root.resolve()
    req(audited.is_dir(), "audited N357 checkout missing")

    head = subprocess.check_output(
        ["git", "-C", str(audited), "rev-parse", "HEAD"], text=True
    ).strip()
    req(head == AUDITED_HEAD, f"audited N357 checkout head drift: {head}")

    paths: dict[str, Path] = {}
    for name, (rel, expected_blob) in EXPECTED.items():
        path = audited / rel
        req(path.is_file(), f"audited N357 file missing: {rel}")
        actual = git_blob(path)
        req(actual == expected_blob, f"audited N357 {name} blob drift: {actual}")
        paths[name] = path

    result = load(paths["result"])
    req(result.get("canonical_sha256_without_this_field") == EXPECTED_RESULT_CANONICAL,
        "audited N357 RESULT stored canonical drift")
    req(canonical(result) == EXPECTED_RESULT_CANONICAL,
        "audited N357 RESULT canonical drift")
    agg = result["aggregate"]
    req(int(agg["source_terminals_replayed"]) == EXPECTED_SOURCE,
        "audited N357 source population drift")
    req(int(agg["candidate_incremental_rejected_terminals"]) == EXPECTED_INCREMENT,
        "audited N357 increment drift")
    req(int(agg["candidate_remaining_terminals"]) == EXPECTED_OLD_RESIDUAL,
        "audited N357 original residual drift")
    req(result["semantics"]["main_pruning_credit"] is False,
        "audited N357 RESULT self-promoted MAIN credit")

    audit_state = load(paths["audit_state"])
    req(audit_state["source_locks"]["result"]["blob_sha1"] == EXPECTED["result"][1],
        "audited N357 audit-state RESULT lock drift")
    req(audit_state["direct_runtime_dependency_locks"]["n357_engine"]["blob_sha1"] == EXPECTED["engine"][1],
        "audited N357 audit-state engine lock drift")
    req(audit_state["source_locks"]["audit_source_lock_verifier"]["blob_sha1"] == EXPECTED["audit_source_lock_verifier"][1],
        "audited N357 audit-state verifier lock drift")
    req(audit_state["credit"]["n357_main_pruning_credit"] is False,
        "audited N357 audit-state self-promoted MAIN credit")

    handoff = load(paths["audit_handoff"])
    req(handoff["frozen_source_locks"]["result"]["blob_sha1"] == EXPECTED["result"][1],
        "audited N357 handoff RESULT lock drift")
    req(handoff["direct_runtime_dependency_locks"]["n357_engine"]["blob_sha1"] == EXPECTED["engine"][1],
        "audited N357 handoff engine lock drift")
    req(handoff["frozen_source_locks"]["audit_source_lock_verifier"]["blob_sha1"] == EXPECTED["audit_source_lock_verifier"][1],
        "audited N357 handoff verifier lock drift")
    req(handoff["firewalls"]["n357_main_pruning_credit"] is False,
        "audited N357 handoff self-promoted MAIN credit")

    # Re-run the exact verifier that was itself part of the hostile-audited N357
    # boundary. It executes against the separate exact-head checkout, so every
    # transitive source lock is checked on the bytes that review 5183069892 audited.
    proc = subprocess.run(
        [sys.executable, str(paths["audit_source_lock_verifier"])],
        cwd=audited,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise SystemExit("FAIL: audited N357 transitive source-lock verifier failed")
    print(proc.stdout, end="")

    # Load the byte-exact audited predicate implementation as an executable
    # identity check, rather than trusting a copied formula string.
    engine = load_module(paths["engine"])
    req(engine.support_suffix_capacity(100, 50, 50, 0) == 20,
        "audited N357 engine witness predicate drift")

    receipt = load(CURRENT_RECEIPT)
    aud = receipt["audited_n357_candidate"]
    req(aud["hostile_audit_status"] == "PASS", "current receipt lost N357 PASS status")
    req(aud["hostile_audit_review_id"] == AUDITED_REVIEW, "current receipt review drift")
    req(aud["audited_exact_head"] == AUDITED_HEAD, "current receipt audited-head drift")
    req(aud["result_blob_sha1"] == EXPECTED["result"][1], "current receipt RESULT blob drift")
    req(aud["engine_blob_sha1"] == EXPECTED["engine"][1], "current receipt engine blob drift")
    req(aud["result_canonical_sha256"] == EXPECTED_RESULT_CANONICAL,
        "current receipt RESULT canonical drift")
    req(aud["main_pruning_credit"] is False, "current receipt self-promoted N357")

    state = load(CURRENT_STATE)
    auth = state["authority_sync"]
    req(auth["n357_candidate_hostile_audit_review_id"] == AUDITED_REVIEW,
        "MAIN state N357 review drift")
    req(auth["n357_candidate_hostile_audit_exact_head"] == AUDITED_HEAD,
        "MAIN state N357 audited-head drift")
    req(auth["n357_candidate_result_blob_sha1"] == EXPECTED["result"][1],
        "MAIN state N357 RESULT blob drift")
    req(auth["n357_main_pruning_credit_consumed"] is False,
        "MAIN state prematurely consumed N357")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == EXPECTED_CURRENT_V13,
        "current V13 authority drift")
    req(EXPECTED_CURRENT_V13 - EXPECTED_INCREMENT == EXPECTED_CURRENT_RESIDUAL,
        "current V13 N357 composition arithmetic drift")

    # The retained inner replay still owns the CUT191/CUT194 exact overlap logic.
    # Execute it only after the audited N357 object boundary above is proven.
    inner = subprocess.run([sys.executable, str(CURRENT_REPLAY)], cwd=ROOT)
    req(inner.returncode == 0, "current-V13 N357 overlap/composition replay failed")

    print(json.dumps({
        "verdict": "PASS_N357_CURRENT_V13_COMPOSITION_FAIL_CLOSED_ON_AUDITED_OBJECTS",
        "audited_exact_head": AUDITED_HEAD,
        "audited_review": AUDITED_REVIEW,
        "audited_result_blob": EXPECTED["result"][1],
        "audited_engine_blob": EXPECTED["engine"][1],
        "audited_source_lock_verifier_blob": EXPECTED["audit_source_lock_verifier"][1],
        "n357_incremental_rejected_terminals_if_later_consumed": EXPECTED_INCREMENT,
        "candidate_remaining_terminals_if_later_consumed": EXPECTED_CURRENT_RESIDUAL,
        "n357_main_pruning_credit": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
