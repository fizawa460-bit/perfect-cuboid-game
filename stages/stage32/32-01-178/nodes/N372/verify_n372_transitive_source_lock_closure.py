#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPLAY = HERE / "verify_n372_current_v15_witness_replay.py"

CUT196_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
REPLAY_BLOB = "4368be620af7f8ee903c9a278f6b3157646d9fd8"
SYMPY_VERSION = "1.14.0"

# Complete local-file closure that is executed or read by the CUT196 E8 adapter
# path used by the retained N372 replay.  These checks happen before importing
# or executing any of those bytes.
CUT196_TRANSITIVE_LOCKS = {
    "stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py": "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f",
    "stages/stage32-ex5/breadth-cycle-2/bc2_18_n354_survivor_exceptional_mod8_decomposition.py": "1e2ed93cae3c5b446c8d90c1ae2250be83289c79",
    "stages/stage32-ex5/breadth-cycle-2/bc2-17-n354-authority-picard64-retarget-v2-evidence.json": "28c4b762c7f96a4898c62751062648cad066578c",
    "stages/stage32/residual-32-01-production/compressed_terminal_family.py": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    "stages/stage33/33-07/picard_base_rows_retained.py": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    "stages/stage32/32-01-178/nodes/N220/STATE-AUDITED.json": "f5f0e902062c9fafc9f03fe8a203d744cf58281e",
    "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-RESULT.json": "0f30517cc5007ea435f4183201fc6cad699dd635",
    "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-HOSTILE-AUDIT-PASS.json": "033294f56fb86d81b7aa43758a51a39747ccc082",
}

# The N357 module is imported by the replay for prefix_survives/n357_accepts.
# Those functions have no local runtime imports; locking this module freezes
# the exact executed helper bytes.
N357_TRANSITIVE_LOCKS = {
    "stages/stage32/verify_n357_v13_current_authority_composition.py": "fdca9ad629983d8c31c7e6355540af3545910120",
}


def req(v: bool, msg: str) -> None:
    if not v:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def verify_lock_set(root: Path, locks: dict[str, str], label: str) -> None:
    for rel, expected in locks.items():
        path = root / rel
        req(path.is_file(), f"missing {label} source: {rel}")
        actual = blob(path)
        req(actual == expected, f"{label} source-lock drift {rel}: {actual} != {expected}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    args = ap.parse_args()
    cut_root = args.cut196_root.resolve()
    comp_root = args.n357_composition_root.resolve()

    req(not any(k == "z3" or k.startswith("z3.") for k in sys.modules), "z3 imported before closure preflight")
    req(exact_head(cut_root) == CUT196_HEAD, "CUT196 exact head drift")
    req(exact_head(comp_root) == N357_HEAD, "N357 exact head drift")
    req(blob(REPLAY) == REPLAY_BLOB, "N372 retained replay verifier blob drift")
    req(importlib.metadata.version("sympy") == SYMPY_VERSION, "sympy version drift")

    verify_lock_set(cut_root, CUT196_TRANSITIVE_LOCKS, "CUT196")
    verify_lock_set(comp_root, N357_TRANSITIVE_LOCKS, "N357")

    proc = subprocess.run(
        [
            sys.executable,
            str(REPLAY),
            "--cut196-root", str(cut_root),
            "--n357-composition-root", str(comp_root),
        ],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise RuntimeError("N372 retained replay failed after transitive source-lock preflight")
    print(proc.stdout, end="")
    req("PASS_N372_CURRENT_V15_WITNESS_SOLVER_INDEPENDENT_REPLAY" in proc.stdout, "N372 replay PASS missing")
    req('"z3_imported": false' in proc.stdout, "N372 replay z3 firewall missing")
    req(not any(k == "z3" or k.startswith("z3.") for k in sys.modules), "closure verifier imported z3")

    lock_manifest = {"cut196": CUT196_TRANSITIVE_LOCKS, "n357": N357_TRANSITIVE_LOCKS}
    manifest_sha256 = hashlib.sha256(
        json.dumps(lock_manifest, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    print(json.dumps({
        "verdict": "PASS_N372_TRANSITIVE_SOURCE_LOCK_CLOSURE",
        "cut196_exact_head": CUT196_HEAD,
        "n357_exact_head": N357_HEAD,
        "local_dependency_blob_locks": len(CUT196_TRANSITIVE_LOCKS) + len(N357_TRANSITIVE_LOCKS),
        "lock_manifest_sha256": manifest_sha256,
        "sympy_version": SYMPY_VERSION,
        "replay_blob_sha1": REPLAY_BLOB,
        "z3_imported": False,
        "main_pruning_credit": False,
        "full178_complete": False,
        "stage32_closed": False,
        "merge_authorized": False,
        "next_gate": "stage32-01-178-audit",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
