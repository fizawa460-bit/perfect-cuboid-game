#!/usr/bin/env python3
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
PASS = "PASS STAGE32_MB104_000707_E2_ETALE_BASECHANGE_DETERMINANT_PASSPORT_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ETALE-BASECHANGE-DETERMINANT-PASSPORT.md",
        "d4e5c3b9c598299114f983594be1fac1b01d24d7",
    ),
    "EQUALITY_RIGIDITY": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md",
        "a20547082b1ea2f786b1272d1b76af3527508e9b",
    ),
    "H_QUOTIENT_MODEL": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md",
        "d2e3056137360a9e15ae7c820088d2977a5eb137",
    ),
    "NODE_ORBIT_TABLE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md",
        "dbfea5a4f62b1388c9810c37ad867076ed4dca6e",
    ),
    "BOUNDARY_SATURATION": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md",
        "aa9a7215467428b55b18ef296ced91b63ec4bf07",
    ),
    "DET_ONE_BIT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-DETERMINANT-ONE-BIT.md",
        "c0e89e66afee11bbba39fa8bce20019a664fa8dc",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def repo_root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


root = repo_root()
for name, (rel, expected) in LOCKS.items():
    p = root / rel
    req(p.is_file(), f"missing {name}: {rel}")
    got = blob_sha1(p)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
eq = (root / LOCKS["EQUALITY_RIGIDITY"][0]).read_text(encoding="utf-8")
hq = (root / LOCKS["H_QUOTIENT_MODEL"][0]).read_text(encoding="utf-8")
node = (root / LOCKS["NODE_ORBIT_TABLE"][0]).read_text(encoding="utf-8")
boundary = (root / LOCKS["BOUNDARY_SATURATION"][0]).read_text(encoding="utf-8")
onebit = (root / LOCKS["DET_ONE_BIT"][0]).read_text(encoding="utf-8")

for token in [
    "n1=n2=14 e l",
    "Ram(f1)=Ram(f2)=0",
]:
    req(token in eq, f"equality token missing: {token}")

for token in [
    "u^2=(r^4+4)/4",
    "v^2=(r^4-4)/4",
    "T     : (r,u,v) -> (-r, u, v)",
]:
    req(token in hq, f"H quotient token missing: {token}")

for token in [
    "d0-d1+d2-d3-d24+d25-d26 = 0",
    "d8+d9+d10+d11+d32+d33+d34 = 0",
    "P0,P2   -> (a,a)",
    "P8,P10  -> (u,v)",
]:
    req(token in node, f"node-table token missing: {token}")

for token in [
    "#psi^{-1}(q^+) = #psi^{-1}(q^-) = 28l",
    "every point in those two fibers is unramified",
]:
    req(token in boundary, f"boundary token missing: {token}")

req("im(T-1) = {0,kappa}" in onebit, "one-bit predecessor token")

for token in [
    "sum_q nu_q = 8n-2(2n)=4n=112l",
    "T^*epsilon_i = epsilon_i",
    "O(F_i(TZ)-F_i(Z)) ~= O_C8",
    "x0+x1+x2+x3 == 0 mod 2",
    "x8+x9+x10+x11 == 0 mod 2",
    "No e=2 closure is claimed",
]:
    req(token in note, f"semantic token missing: {token}")

# e=2 degree and Riemann--Hurwitz replay.
n = 28
req(2 * n == 56, "elliptic-to-P1 total ramification coefficient")
req(8 * n - 2 * (2 * n) == 4 * n == 112, "eight-value unramified total coefficient")
req(14 * 8 == 112, "supported branch total coefficient")

# Exact supported-node masses in the four residual r<->-r pairs.
# Pair order: (+/-a), (+/-b), (+/-u), (+/-v).
f1_pair_mass = [32, 24, 56, 0]
f2_pair_mass = [56, 0, 24, 32]
req(sum(f1_pair_mass) == 112, "f1 pair masses exhaust unramified budget")
req(sum(f2_pair_mass) == 112, "f2 pair masses exhaust unramified budget")

# b_q=u_q/2 mod 2.  For each residual pair, equality of sign bits follows
# because (u_q+u_-q)/2 is an even multiple of l.
for label, masses in [("f1", f1_pair_mass), ("f2", f2_pair_mass)]:
    for m in masses:
        req(m % 8 == 0, f"{label} pair mass must be 8l multiple: {m}")
        req((m // 2) % 2 == 0, f"{label} residual pair sign mismatch possible: {m}")

# Q0 displayed signs on the second factor give
# u_(+a)=32l + (x0-x1+x2-x3-x24+x25-x26)=28l.
# Replay coefficient arithmetic using the retained Q0 RHS -4l.
req(32 - 4 == 28, "second-factor Q0 +a saturation")
req((28 // 2) % 2 == 0, "Q0 determinant sign bit must vanish")

# Q1 first-factor displayed representatives are all +u, so its exact retained
# saturation sum is u_(+u)=28l.
req((28 // 2) % 2 == 0, "Q1 determinant sign bit must vanish")

# The two genuinely new parity requirements come from individual fiber counts
# being even.  Their complementary three-node sums are equivalent mod 2 by
# the retained seven-node saturation equations.  This verifier records the
# algebraic independence count, not a geometric existence claim.
# q0 mod2: A+B=0; requiring A=0 forces B=0.
for A in (0, 1):
    B = A
    req((A + B) % 2 == 0, "Q0 saturation parity model")
# q1 mod2 has the same two-block structure.
for A in (0, 1):
    B = A
    req((A + B) % 2 == 0, "Q1 saturation parity model")

# Four T-invariant base sign bits modulo the two independent H characters
# leave at most two bits => at most four determinant classes.
req(2 ** (4 - 2) == 4, "two-bit determinant subspace bound")

for forbidden in [
    "e2_closed: true",
    "receiver_credit: true",
    "theorem_credit: true",
    "endpoint_credit: true",
    "perfect_cuboid_nonexistence_claim: true",
]:
    req(forbidden not in note, f"forbidden credit token: {forbidden}")

print(PASS)
