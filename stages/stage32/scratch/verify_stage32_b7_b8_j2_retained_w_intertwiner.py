#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = HERE / "b7-b8-j2-retained-w-intertwiner-20260908.json"
DIAG = HERE / "diagnose_stage32_b7_b8_j2_retained_w_intertwiner.py"
RETAINED = ROOT / "stages/stage32/residual-32-01-production/post1505-o210-q602-marked-w-line-gauge-orbit.json"
EXPECTED_RETAINED_BLOB = "2b790882222656f65ed7ea4bdc2336553890b6a1"
EXPECTED_RETAINED_CANONICAL = "7ad84e3c0a567119933ee0941b3b125ebcdb80651973033e13dbf12b553bfc92"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def require(cond: bool, message: str) -> None:
    if not cond:
        raise SystemExit(message)


def main() -> None:
    artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    retained = json.loads(RETAINED.read_text(encoding="utf-8"))
    diag = json.loads(subprocess.check_output([sys.executable, str(DIAG)], text=True))

    require(git_blob_sha1(RETAINED) == EXPECTED_RETAINED_BLOB, "retained marked-W asset blob moved")
    require(retained["canonical_sha256_without_this_field"] == EXPECTED_RETAINED_CANONICAL, "retained marked-W canonical moved")
    require(artifact["source_locks"]["retained_marked_w_orbit"]["blob_sha1"] == EXPECTED_RETAINED_BLOB, "artifact retained blob lock moved")
    require(artifact["source_locks"]["retained_marked_w_orbit"]["canonical_sha256"] == EXPECTED_RETAINED_CANONICAL, "artifact retained canonical lock moved")

    require(diag["invertible_F2_intertwiner_count"] == 2, "intertwiner count moved")
    require(diag["forced_pair_line_map"] == {"Z1": "L1", "Z2": "L2", "Z3": "L3"}, "forced pair-line map moved")
    require(diag["forced_delta_0inf_line_if_ordered_generator_pair_is_source_bound"] == "L3", "conditional delta_0inf line moved")
    require(diag["forced_q602_residue_if_ordered_generator_pair_is_source_bound"] == 235, "conditional residue moved")
    require(not diag["absolute_identification_promoted_now"], "diagnostic promoted conditional result")

    finite = artifact["finite_intertwiner_enumeration"]
    require(finite["invertible_solution_count"] == diag["invertible_F2_intertwiner_count"], "artifact/diagnostic count mismatch")
    require(finite["solutions"] == diag["intertwiners"], "artifact/diagnostic intertwiners mismatch")
    require(finite["forced_pair_line_map_under_ordered_generator_binding"] == diag["forced_pair_line_map"], "artifact/diagnostic forced map mismatch")

    decision = artifact["decision"]
    require(decision["if_ordered_pair_is_source_bound"] == "delta_0inf=Z3 maps to L3 and hence Q602 residue 235", "conditional decision moved")
    require(not decision["absolute_delta0inf_retained_W_line_identified_now"], "absolute line promoted without source binding")
    require(decision["uniform_EX1_residue_count_now"] == 3, "survivor count changed")
    require(not decision["authority_changed"], "scratch changed authority")
    require(not decision["claim_dag_changed"], "scratch changed claim DAG")
    require(not decision["Q602_excluded"], "scratch excluded Q602")
    require(not decision["O210_excluded"], "scratch excluded O210")

    print("PASS_STAGE32_SCRATCH_B7_B8_J2_RETAINED_W_INTERTWINER")


if __name__ == "__main__":
    main()
