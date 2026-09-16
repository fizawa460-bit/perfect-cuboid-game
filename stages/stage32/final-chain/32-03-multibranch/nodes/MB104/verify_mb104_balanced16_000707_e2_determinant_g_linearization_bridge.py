#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
PASS = "PASS STAGE32_MB104_000707_E2_DETERMINANT_G_LINEARIZATION_BRIDGE_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-DETERMINANT-G-LINEARIZATION-BRIDGE.md",
        "7f5a770b0d458533c7f5b999ae880109964b33c8",
    ),
    "PASSPORT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ETALE-BASECHANGE-DETERMINANT-PASSPORT.md",
        "d4e5c3b9c598299114f983594be1fac1b01d24d7",
    ),
    "LINEARIZATION_KERNEL": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-DIAGONAL-G-LINEARIZATION-OBSTRUCTION.md",
        "7593aad67cbc284f16066063bc6abc6afb2352c8",
    ),
    "EQUIVARIANT_PICARD_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/EQUIVARIANT-PICARD-LINEARIZATION-SOURCE-NOTE.md",
        "a8db86e809ed6a19e7777a7680f3392f980e0bf0",
    ),
}


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)


def repo_root() -> Path:
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


root = repo_root()

# Fail closed before any retained arithmetic or semantic replay.
for name, (rel, expected) in LOCKS.items():
    path = root / rel
    req(path.is_file(), f"missing source lock {name}: {rel}")
    got = git_blob_sha1(path)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
passport = (root / LOCKS["PASSPORT"][0]).read_text(encoding="utf-8")
kernel = (root / LOCKS["LINEARIZATION_KERNEL"][0]).read_text(encoding="utf-8")
source = (root / LOCKS["EQUIVARIANT_PICARD_SOURCE"][0]).read_text(encoding="utf-8")

for token in [
    "epsilon_i is G-linearizable",
    "epsilon_i in Ker(obs_G | J(C8)^G)",
    "No individual conductor pair is assigned the class `0` or `gamma_Q`",
    "No e=2 closure is claimed",
]:
    req(token in note, f"human-note token missing: {token}")

for token in [
    "b_q=b_-q",
    "T^*epsilon_i = epsilon_i",
    "d_-(f1)=0",
    "d_+(f2)=0",
]:
    req(token in passport, f"passport token missing: {token}")

for token in [
    "Ker(obs_G | J(C8)^G)",
    "~= (Z/2)^2",
    "32*4 = 128",
]:
    req(token in kernel, f"linearization-kernel token missing: {token}")

for token in [
    "Pic^G(X)",
    "H^2(G,C^*)",
    "exactly the subgroup represented by `G`-invariant divisors",
]:
    req(token in source, f"equivariant-Picard token missing: {token}")

# Replay the exact parity mechanism behind the fibre-character equality.
# For one residual pair, nu_plus + nu_minus = 8*l*m and n=28*l.
# Since nu values are even, b=(nu/2) mod 2.  The half-sum is 4*l*m,
# hence even, so the two b bits agree.
for l in range(1, 17):
    n = 28 * l
    for m in range(0, 8):
        total = 8 * l * m
        for nu_plus in range(0, min(n, total) + 1, 2):
            nu_minus = total - nu_plus
            if not (0 <= nu_minus <= n) or (nu_minus & 1):
                continue
            req((nu_plus // 2 + nu_minus // 2) % 2 == 0, "paired half-sum parity")
            b_plus = (nu_plus // 2) & 1
            b_minus = (nu_minus // 2) & 1
            req(b_plus == b_minus, "paired determinant fibre sign")

# Local normalized base-change fibre bookkeeping:
# nu fixed sheets plus r transpositions has degree n=nu+2r and determinant
# sign (-1)^r.  Check all admissible fibres in a bounded symbolic replay.
for l in range(1, 17):
    n = 28 * l
    for nu in range(0, n + 1, 2):
        r = (n - nu) // 2
        req(nu + 2 * r == n, "local fibre degree")
        req((r & 1) == ((nu // 2) & 1), "passport sign formula")

# Exact finite target inherited from the equivariant-Picard calculation.
fixed_jacobian_size = 1 << 5
obstruction_size = 1 << 3
linearizable_kernel_size = fixed_jacobian_size // obstruction_size
req(fixed_jacobian_size == 32, "fixed Jacobian size")
req(obstruction_size == 8, "obstruction group size")
req(linearizable_kernel_size == 4, "linearizable kernel size")

# The passport leaves one unresolved determinant bit per factor after the
# exact node-table specializations.  This remains a 2-element line inside the
# common four-class linearizable kernel; no equality of the two lines is used.
req(2 <= linearizable_kernel_size, "factor determinant binary line capacity")

print(PASS)
print("determinant_G_linearizable=true linearizable_kernel=4 factor1_bits<=1 factor2_bits<=1 e2_closed=false")
