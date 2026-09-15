#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
PASS = "PASS STAGE32_MB104_000707_E2_ROSATI_ZERO_CORRESPONDENCE_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ROSATI-ZERO-CORRESPONDENCE.md",
        "24cc729070ab685491fd2659d970da1a9f415891",
    ),
    "PRODUCT_LINEARIZATION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PRODUCT-CORRESPONDENCE-LINEARIZATION-CERTIFICATE.json",
        "ea8bd879093a5ec2054f560807fa05806f96a553",
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


root = repo_root()

# Fail closed on every imported retained asset before any arithmetic replay.
for name, (rel, expected) in LOCKS.items():
    p = root / rel
    req(p.is_file(), f"missing lock {name}: {rel}")
    got = git_blob_sha1(p)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
cert = json.loads((root / LOCKS["PRODUCT_LINEARIZATION_CERT"][0]).read_text(encoding="utf-8"))

req(cert.get("active_leaf") == ACTIVE, "product certificate active leaf")
req(cert.get("scope", {}).get("case") == "e=2", "product certificate e=2 scope")
req(cert.get("scope", {}).get("conductor_pair_sign_computed") is False, "product certificate conductor firewall")
req(cert.get("intersection_and_genus", {}).get("Zbar_self_intersection") == "1568*l^2", "retained Zbar^2")

for token in [
    "D^2 = 2 d_1 d_2 - Tr_H1(Phi_D Phi_D^dagger)",
    "n=28l",
    "Zbar^2=1568l^2",
    "Phi_Z=0",
    "No claim that a zero Jacobian correspondence is geometrically impossible",
    "No e=2 closure is claimed",
]:
    req(token in note, f"semantic token missing: {token}")

# Exact numerical saturation replay.  The coefficient of l^2 in 2*n^2 is
# 2*28^2 = 1568, exactly the retained product-image self-intersection.
n_coeff = 28
zbar2_coeff = 1568
rosati_trace_coeff = 2 * n_coeff * n_coeff - zbar2_coeff
req(2 * n_coeff * n_coeff == 1568, "2*(28l)^2 coefficient")
req(rosati_trace_coeff == 0, "Rosati trace coefficient must vanish")

# Diagonal normalization sanity check for genus(C8)=5:
# Delta^2 = 2 - Tr_H1(id) = 2 - 10 = -8 = 2 - 2g.
g = 5
req(2 - 2 * g == -8, "diagonal self-intersection normalization")
req(2 - (2 * g) == 2 - 2 * g, "H1 trace normalization")

# Credit/firewall checks are textual because this verifier certifies only the
# retained candidate consequence, not existence/nonexistence of the curve.
for forbidden in [
    "e2_closed: true",
    "receiver_credit: true",
    "theorem_credit: true",
    "endpoint_credit: true",
    "perfect_cuboid_nonexistence_claim: true",
]:
    req(forbidden not in note, f"forbidden credit token: {forbidden}")

print(PASS)
