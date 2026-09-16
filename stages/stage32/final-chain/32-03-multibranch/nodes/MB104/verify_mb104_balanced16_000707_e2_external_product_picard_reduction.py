#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
PASS = "PASS STAGE32_MB104_000707_E2_EXTERNAL_PRODUCT_PICARD_REDUCTION_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXTERNAL-PRODUCT-PICARD-REDUCTION.md",
        "dc2def9e4d0148aa3146a034a2ce0ef331206a29",
    ),
    "ROSATI_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ROSATI-ZERO-CORRESPONDENCE-CERTIFICATE.json",
        "9f40705d9018b9e9df73ca9b06d9a79a160562d3",
    ),
    "PRODUCT_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PRODUCT-CORRESPONDENCE-LINEARIZATION.md",
        "2c2db567db6a3c33762b2ff3d7f39f885a95b974",
    ),
    "TORSION4_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-TORSION-EXPONENT-FOUR.md",
        "1f7e9ddd426c6df61c1aff30fb7ef42d12ea3a3b",
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
for name, (rel, expected) in LOCKS.items():
    p = root / rel
    req(p.is_file(), f"missing lock {name}: {rel}")
    got = git_blob_sha1(p)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
product_note = (root / LOCKS["PRODUCT_NOTE"][0]).read_text(encoding="utf-8")
torsion_note = (root / LOCKS["TORSION4_NOTE"][0]).read_text(encoding="utf-8")
rosati = json.loads((root / LOCKS["ROSATI_CERT"][0]).read_text(encoding="utf-8"))

req(rosati.get("active_leaf") == ACTIVE, "Rosati active leaf")
req(rosati.get("scope", {}).get("case") == "e=2", "Rosati e2 scope")
req(rosati.get("deduction", {}).get("Phi_Z") == "0", "Rosati Phi_Z zero")
req(rosati.get("retained_input", {}).get("projection_degree_each") == "28*l", "Rosati projection degree")
req(rosati.get("credit_firewall", {}).get("e2_closed") is False, "Rosati e2 firewall")

for token in [
    "Zbar ~ Tdiag(Zbar)",
    "Phi_Z in End(J(C8))^G",
    "f_1,f_2 are the two degree-`28l` etale projections",
]:
    req(token in product_note, f"product token missing: {token}")

for token in [
    "H=<s1,s2> ~= (Z/2)^2",
    "each of `s1,s2` has exactly eight fixed points",
    "`h` is fixed-point-free",
]:
    req(token in torsion_note, f"torsion/H token missing: {token}")

for token in [
    "O_P(Zbar) ~= p_1^* A tensor p_2^* B",
    "A,B in Pic^(28l)(C8)^G",
    "J(C8)^G subset J(C8)^H subset J(C8)[4]",
    "|J(C8)[4]|=4^(2g)=4^10",
    "No e=2 closure is claimed",
]:
    req(token in note, f"semantic token missing: {token}")

# Riemann--Hurwitz for H of order four: 8 = 4(2g_H-2)+16.
g_c = 5
ram = 16
lhs = 2 * g_c - 2
numerator = lhs - ram
req(numerator % 4 == 0, "H quotient RH divisibility")
qterm = numerator // 4
req(qterm == -2, "H quotient 2g-2")
g_h = (qterm + 2) // 2
req(g_h == 0, "C8/H genus")

# Reference degree formulas for l=2k and l=2k+1.
for k in range(0, 8):
    l_even = 2 * k
    if l_even > 0:
        req(8 * (7 * l_even // 2) == 28 * l_even, f"even reference degree l={l_even}")
    l_odd = 2 * k + 1
    exp = (7 * l_odd - 1) // 2
    req(4 + 8 * exp == 28 * l_odd, f"odd reference degree l={l_odd}")

# Genus five 4-torsion cardinality and ordered-pair crude bound.
req(4 ** (2 * g_c) == 4 ** 10, "J[4] cardinality")
req((4 ** 10) ** 2 == 4 ** 20, "ordered pair bound")

for forbidden in [
    "e2_closed: true",
    "receiver_credit: true",
    "theorem_credit: true",
    "endpoint_credit: true",
    "perfect_cuboid_nonexistence_claim: true",
]:
    req(forbidden not in note, f"forbidden credit token: {forbidden}")

print(PASS)
