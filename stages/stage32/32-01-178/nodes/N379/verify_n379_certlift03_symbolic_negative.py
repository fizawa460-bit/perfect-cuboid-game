#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
N379 = HERE / "STATE.json"
N378 = HERE.parent / "N378/STATE.json"

N379_BLOB = "2aba2e66e11b428ec3650eaa486152472a4681a4"
N379_CANON = "60cc37e8098cba454fe63bbfd3c909802dc623bc67d675b004ba36e3a9fc016f"
N378_BLOB = "5ddd2379750d291a3b77d630479335ff02a159c3"
N378_CANON = "6312c0d2a49b2407c6fb431c5a845010a1eea38c268c6cfe7400685d73a17bca"

CERTLIFT_HEAD = "d42062c498d42550e85143d72abf53854676b93d"
CERTLIFT_STATE_REL = Path("stages/stage32/cut-cert-lift/STATE.json")
CERTLIFT_STATE_BLOB = "65eb0d6346eb1b4c94cc4a333f3371a82a2de2dc"
FEATURE_REL = Path("stages/stage32/cert-lift/CERTLIFT-02-FEATURE-DISCRIMINATOR-RECEIPT.json")
FEATURE_BLOB = "58d2c41e646d8a168441bdd46e9694a5380667ac"
FEATURE_CANON = "241a922dfd37fbd47b297654ea29aeac7e32bc9d73fad1165f0592d9f5d14188"
G3_RECEIPT_REL = Path("stages/stage32/cert-lift/CERTLIFT-03-G3-EXACT-CANDIDATE-RECEIPT.json")
G3_RECEIPT_BLOB = "39bdd6eb2aca1bef8f03e3d2096ad17746514c93"
G3_RECEIPT_CANON = "6cb776745bbb7da2fe2c2ef457b3f75f8f8246b89156b6ef60493c5c45238576"
G3_ROW_REL = Path("stages/stage32/cert-lift/g3_row_certificate.py")
G3_ROW_BLOB = "e9bd3f8dbf85f974bca3e20ea3ff244db39a5647"
G3_PARITY_REL = Path("stages/stage32/cert-lift/g3_fibre_parity_lemma.py")
G3_PARITY_BLOB = "74a17fb7f784b42f1deb7358ab9f09743523e9d4"
PRODUCER_WORKFLOW_REL = Path(".github/workflows/stage32-claim-frontier-integrity.yml")
PRODUCER_WORKFLOW_BLOB = "43e8a68761187d4364d953389b48a7b7f80fb760"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected_blob: str, expected_canon: str | None = None) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
        req(canonical(obj) == expected_canon, f"canonical replay drift: {path}")
    return obj


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def run_json(cmd: list[str], *, cwd: Path, env: dict[str, str]) -> tuple[int, dict | None, str, str]:
    p = subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True)
    obj = None
    if p.stdout.strip():
        try:
            obj = json.loads(p.stdout)
        except json.JSONDecodeError:
            lines = [line for line in p.stdout.splitlines() if line.strip()]
            if lines:
                try:
                    obj = json.loads(lines[-1])
                except json.JSONDecodeError:
                    pass
    return p.returncode, obj, p.stdout, p.stderr


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certlift-root", type=Path, required=True)
    ap.add_argument("--ex5-source-root", type=Path, required=True)
    args = ap.parse_args()

    n378 = checked(N378, N378_BLOB, N378_CANON)
    n379 = checked(N379, N379_BLOB, N379_CANON)

    certroot = args.certlift_root.resolve()
    ex5root = args.ex5_source_root.resolve()
    req(exact_head(certroot) == CERTLIFT_HEAD, "CERT-LIFT exact head drift")

    producer = checked(certroot / CERTLIFT_STATE_REL, CERTLIFT_STATE_BLOB)
    feature = checked(certroot / FEATURE_REL, FEATURE_BLOB, FEATURE_CANON)
    g3 = checked(certroot / G3_RECEIPT_REL, G3_RECEIPT_BLOB, G3_RECEIPT_CANON)
    req(blob(certroot / G3_ROW_REL) == G3_ROW_BLOB, "g3 row certificate blob drift")
    req(blob(certroot / G3_PARITY_REL) == G3_PARITY_BLOB, "g3 fibre parity lemma blob drift")
    req(blob(certroot / PRODUCER_WORKFLOW_REL) == PRODUCER_WORKFLOW_BLOB, "producer workflow blob drift")

    req(n378["status"] == "WAITING_CERTLIFT02_EXECUTION_AND_V22_ADAPTER_NO_CREDIT", "N378 parent status drift")
    req(n379["parent"]["n378_state_blob_sha1"] == N378_BLOB, "N379 parent blob drift")
    req(n379["parent"]["n378_state_canonical_sha256"] == N378_CANON, "N379 parent canonical drift")
    req(n379["status"] == "CERTLIFT03_EXACT_G3_FINITE_PASS_SYMBOLIC_PARITY_FAIL_NO_CREDIT", "N379 status drift")

    req(producer["schema"] == "STAGE32_CUT_CERT_LIFT_STATE_V1", "producer schema drift")
    req(producer["status"] == "ACTIVE", "producer status drift")
    req(producer["active_node"] == "CERTLIFT-02_INVARIANT_COMPRESSION_AND_COUNTEREXAMPLE_SPLIT", "producer retained active-node drift")
    req(producer["credit"]["main_pruning"] is False and producer["credit"]["full178"] is False, "producer credit firewall drift")

    best = feature["result"]["best_single"]
    req(best["predicate"] == "g3==3", "feature best-single drift")
    req(best["selected_mod2_obstructed"] == 1677, "g3 current-MAIN obstructed count drift")
    req(best["selected_projection_survivors"] == 0, "g3 unexpectedly intersects the 275 projection survivors")
    req(feature["scope"]["projection_survivors"] == 275, "CERTLIFT-02 survivor count drift")

    req(g3["status"] == "PASS_G3_EQ_3_FULL_COMPRESSED_E8_MOD2_OBSTRUCTION", "g3 exact finite candidate drift")
    req(g3["result"]["targeted_blocks"] == 1852 and g3["result"]["mod2_obstructed_blocks"] == 1852, "g3 1852/1852 exact count drift")
    req(g3["result"]["projection_survivors"] == 0, "g3 full-e8 finite candidate gained survivors")
    req(g3["interpretation"]["symbolic_row_certificate_still_required"] is True, "finite/symbolic firewall drift")
    req(g3["credit"]["main_pruning"] is False, "g3 receipt prematurely grants MAIN credit")

    env = os.environ.copy()
    env["PYTHONPATH"] = str(ex5root / "stages/stage32-ex5/cut-handoff")

    rc, row, out, err = run_json(
        [sys.executable, str(certroot / G3_ROW_REL), "--self-check"],
        cwd=certroot,
        env=env,
    )
    req(rc == 0 and row is not None, f"g3 row-certificate replay failed: {out} {err}")
    req(row["status"] == "PASS_G3_PRE_GF2_FIBRE_EMPTY", "g3 row replay status drift")
    req(row["targeted_blocks"] == 1852 and row["fibre_empty_blocks"] == 1852, "g3 fibre-empty count drift")
    req(row["post_fibre_configurations"] == 0, "g3 post-fibre configurations unexpectedly nonzero")

    rc, parity, out, err = run_json(
        [sys.executable, str(certroot / G3_PARITY_REL)],
        cwd=certroot,
        env=env,
    )
    req(rc == 0 and parity is not None, f"g3 parity negative replay failed to serialize: {out} {err}")
    req(parity["status"] == "NO_SYMBOLIC_G3_PARITY_CONTRADICTION", "failed symbolic route unexpectedly promoted")
    req(parity["derivation"]["constraint_rank_representation_found"] is False, "g3 functional unexpectedly entered parity span")
    req(parity["derivation"]["d8_g3_equals_3_contradiction"] is False, "parity-only d8 contradiction unexpectedly established")
    req(parity["credit"]["certlift_symbolic_lemma_candidate"] is False, "failed parity route grants candidate credit")

    obs = n379["exact_observations"]
    req(obs["g3_feature_discriminator"]["selected_projection_survivors"] == 0, "N379 residual accounting drift")
    req(obs["g3_row_certificate_replay"]["post_fibre_projected_configurations"] == 0, "N379 row-certificate observation drift")
    req(obs["symbolic_fibre_parity_replay"]["self_check_pass"] is False, "N379 failed-CI boundary drift")
    req(obs["symbolic_fibre_parity_replay"]["g3_functional_in_fibre_parity_span"] is False, "N379 parity-span observation drift")

    req(n379["n101_contract"]["remains_stopped"] is True, "N101 unexpectedly reopened")
    req(n379["authority_boundary"]["v20_to_v22_exact_adapter_still_required_for_main_consumption"] is True, "V20/V22 adapter firewall drift")
    req(all(value is False for value in n379["credit"].values()), "N379 credit firewall drift")
    req(all(value is False for value in n379["anti_loop"].values()), "N379 anti-loop/heavy firewall drift")

    print(json.dumps({
        "verdict": "PASS_N379_CERTLIFT03_SYMBOLIC_FIBRE_PARITY_NEGATIVE_BOUNDARY",
        "producer_pr": 1803,
        "producer_exact_head": CERTLIFT_HEAD,
        "g3_full_e8_targeted": 1852,
        "g3_full_e8_fibre_empty": 1852,
        "current_main_g3_already_obstructed": 1677,
        "current_main_projection_survivors_touched_by_g3": 0,
        "symbolic_parity_status": parity["status"],
        "g3_functional_in_fibre_parity_span": False,
        "n101_reopened_credit": False,
        "main_pruning_credit": False,
        "full178_complete": False,
        "merge_authorized": False,
        "next_gate": n379["next_gate"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
