#!/usr/bin/env python3
from __future__ import annotations
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB101/CERTIFICATE.json": "282fc94d8d5feb0221cf6bf096ed4b0030883563",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-LOW-SUPPORT-FINITENESS-CERTIFICATE.json": "248adcc01021ba087cb24e06e6492e837aca22ae",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-SPAN-DEGREE-CERTIFICATE.json": "dd174696c7391981d4d9a95e631b5df22d08500a",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GLOBAL-EFFECTIVITY-P5-CONIC-CERTIFICATE.json": "7bef88be7a8a81bbcf022ef9fea4834c2dc2da39",
}
CPP = Path(__file__).with_name("verify_mb104_genus1_span5_hyperplane_finite_reduction.cpp")
CPP_SHA = "e4bb3c37661d6e8c80d75af987c277bc16959859"

def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()

def main() -> int:
    for rel, expected in LOCKS.items():
        got = git_blob(ROOT / rel)
        if got != expected:
            raise SystemExit(f"source-lock mismatch: {rel}: {got} != {expected}")
    got_cpp = git_blob(CPP)
    if got_cpp != CPP_SHA:
        raise SystemExit(f"verifier source-lock mismatch: {got_cpp} != {CPP_SHA}")
    with tempfile.TemporaryDirectory(prefix="mb104-span5-") as td:
        exe = Path(td) / "verify_span5"
        subprocess.run(["g++", "-O3", "-std=c++17", str(CPP), "-o", str(exe)], cwd=ROOT, check=True)
        subprocess.run([str(exe)], cwd=ROOT, check=True)
    print("PASS source-locks-and-exhaustive-replay")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
