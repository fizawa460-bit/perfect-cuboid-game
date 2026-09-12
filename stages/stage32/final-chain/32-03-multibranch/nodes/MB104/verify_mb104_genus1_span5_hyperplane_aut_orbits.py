#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]

LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB103/CERTIFICATE.json": "9cb1e8acc268491a84f0c0e27f4fd39f6cb39d8b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-FINITE-REDUCTION-CERTIFICATE.json": "b6035b2e525a08ab0fc028e1e1f81519548e1a5b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GLOBAL-EFFECTIVITY-P5-CONIC-CERTIFICATE.json": "7bef88be7a8a81bbcf022ef9fea4834c2dc2da39",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md": "cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-AUT-ORBIT-CLASSIFICATION.md": "c3bcc580b5bd43b7805c7227c7420445f14c4b8c",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-AUT-ORBIT-CERTIFICATE.json": "3bc4453affce96e87a60864c99f745bb4c28c794",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_genus1_span5_hyperplane_aut_orbits.cpp": "0c5b460b76b69e41e6009be2e92b7c051f003c22",
}

CPP = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_genus1_span5_hyperplane_aut_orbits.cpp"


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()


def main() -> int:
    for rel, expected in LOCKS.items():
        got = git_blob(ROOT / rel)
        if got != expected:
            raise SystemExit(f"source-lock mismatch: {rel}: {got} != {expected}")

    with tempfile.TemporaryDirectory(prefix="mb104-span5-aut-") as td:
        exe = Path(td) / "verify_span5_aut"
        subprocess.run(["g++", "-O3", "-std=c++17", str(CPP), "-o", str(exe)], cwd=ROOT, check=True)
        subprocess.run([str(exe)], cwd=ROOT, check=True)

    print("PASS source-locks-and-span5-aut-orbit-replay")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
