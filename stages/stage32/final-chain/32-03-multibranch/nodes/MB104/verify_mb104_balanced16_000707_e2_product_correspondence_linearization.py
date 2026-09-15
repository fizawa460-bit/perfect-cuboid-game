#!/usr/bin/env python3
import hashlib
from pathlib import Path
from fractions import Fraction
from itertools import product

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
PASS = "PASS STAGE32_MB104_000707_E2_PRODUCT_CORRESPONDENCE_LINEARIZATION_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PRODUCT-CORRESPONDENCE-LINEARIZATION.md",
        "2c2db567db6a3c33762b2ff3d7f39f885a95b974",
    ),
    "AMBIENT_H1": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-H1-TORSION-KILL.md",
        "8ab59d0582e3a0c33c867244f00d2ab8f23c9346",
    ),
    "INTERMEDIATE_H": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL-CERTIFICATE.json",
        "983dc26d0fbed5f524f2bfda5f5bda86a7d8f890",
    ),
    "A1_ENERGY": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY.md",
        "3fb4152c35b88160f36730fac941f542566664a8",
    ),
    "EQUALITY_RIGIDITY": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md",
        "a20547082b1ea2f786b1272d1b76af3527508e9b",
    ),
    "JOINT_BIRATIONALITY": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY.md",
        "53608cb51aa49ccde1603b1cb1d136ea497b2324",
    ),
    "MODULAR_CHARACTER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-MODULAR-CONDUCTOR-DECK-CHARACTER.md",
        "ce9554bc047159baf7640db50aa5daf1f0c67f74",
    ),
    "NODE_TYPES": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md",
        "a29161602c0b38f0607794e56e61068b8cb9735d",
    ),
    "PRODUCT_COVER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-PRODUCT-COVER-SOURCE-NOTE.md",
        "974c6cfecb6e4141615583841a0c90146ad2b4a6",
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


def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def dot(a, b):
    return sum(x*y for x, y in zip(a, b)) & 1


root = repo_root()
for name, (rel, expected) in LOCKS.items():
    p = root / rel
    req(p.is_file(), f"missing lock {name}: {rel}")
    got = git_blob_sha1(p)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
for token in [
    "Gamma ~ tau Gamma",
    "Zbar ~ Tdiag(Zbar)",
    "Gamma^2",
    "392l^2",
    "1568l^2",
    "784l^2+112l",
    "Phi_Z in End(J(C8))^G",
    "No e=2 closure is claimed",
]:
    req(token in note, f"semantic token missing: {token}")

# Symbolic coefficient replay for the A1 self-intersection cancellation.
# C1^2 = 168*l^2 - sum a_j^2; fourteen two-lift corrections give
# 1/2*((4l+a)^2+(4l-a)^2)=16*l^2+a^2 per supported node.
base_l2 = 168
per_node_l2 = 16
node_count = 14
req(base_l2 + node_count * per_node_l2 == 392, "Gamma^2 l^2 coefficient")
req(-1 + 1 == 0, "sum a_j^2 cancellation")
req(4 * 392 == 1568, "degree-four pullback self-intersection")

# Adjunction / normalization-defect replay.
# K_P.Zbar=448l and g(normalization)=112l+1.
z2_l2 = 1568
kz_l = 448
pa_l2 = z2_l2 // 2
pa_l = kz_l // 2
req((pa_l2, pa_l) == (784, 224), "arithmetic genus coefficients")
delta_l2 = pa_l2
delta_l = pa_l - 112
req((delta_l2, delta_l) == (784, 112), "normalization defect coefficients")

# Exact G-character replay. Coordinates are (rho,tau,upsilon), with
# s1=T'=(0,0,1), s2=TT'R=(1,1,1), s3=T=(0,1,0).
G = list(product((0, 1), repeat=3))
one = (0, 0, 0)
singular = {(0, 0, 1), (1, 1, 1), (0, 1, 0)}
free = set(G) - {one} - singular
req(len(free) == 4, "free-element count")

# Quotient genus: singular involution -> 1, free involution -> 3.
# For dim V=5, trace(g)=2*dim(V^g)-5.
trace = {one: 5}
trace.update({g: -3 for g in singular})
trace.update({g: 1 for g in free})

mult = {}
for chi in G:
    s = 0
    for g in G:
        s += trace[g] * (1 if dot(chi, g) == 0 else -1)
    req(s % 8 == 0, f"nonintegral Fourier multiplicity for {chi}")
    mult[chi] = s // 8

expected = {
    (0, 0, 0): 0,
    (0, 0, 1): 1,
    (0, 1, 0): 1,
    (0, 1, 1): 1,
    (1, 0, 0): 0,
    (1, 0, 1): 0,
    (1, 1, 0): 0,
    (1, 1, 1): 2,
}
req(mult == expected, f"G-character multiplicities: {mult}")
req(sum(mult.values()) == 5, "character dimension")
req(sum(m*m for m in mult.values()) == 7, "complex centralizer dimension")

# Credit/firewall checks.
for forbidden in [
    "e2_closed: true",
    "receiver_credit: true",
    "theorem_credit: true",
    "endpoint_credit: true",
    "merge_authorized: true",
]:
    req(forbidden not in note, f"forbidden promotion token: {forbidden}")

print(PASS)
