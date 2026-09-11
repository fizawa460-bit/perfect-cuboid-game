#!/usr/bin/env python3
import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(rel):
    return json.loads((ROOT / rel).read_text())


def blob(rel):
    return subprocess.check_output(["git", "hash-object", str(ROOT / rel)], text=True).strip()

# Minimal exact polynomial arithmetic in h. Coefficients are integers and
# tuples are ascending in h.
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(out)


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def scale(a, k):
    return trim([k * x for x in a])

ONE = (1,)
H = (0, 1)
H2 = mul(H, H)
R2 = add(H2, (4,))
R4 = mul(R2, R2)

O_PATH = "stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json"
DZ_PATH = "stages/stage36/36-09DZ/mw-phi-quotient-source-lock.md"
EE_SOURCE_PATH = "stages/stage36/36-09EE/q2-rho-torsion-retained-open-exclusion-source-lock.md"
EG_PATH = "stages/stage36/36-09EG/fixed-p2-parameter-orbit-impact-preflight.json"
SOURCE_PATH = "stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-source-lock.md"
CERT_PATH = "stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json"

expected = {
    O_PATH: "6a2678ebedba40e13277100441361039ee47ca28",
    DZ_PATH: "4ff753f9933f56cd33accaac264ddc7e936d2364",
    EE_SOURCE_PATH: "0cc6e97c62fbb0782f19e30d87b19509d8144a8c",
    EG_PATH: "5a2977d3eafe9ea1d4751dc386e6a7b3aad01dc3",
    SOURCE_PATH: "71415af89ff48b0efce0f10429e5a2d4c4947634",
    CERT_PATH: "d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37",
}
for path, sha in expected.items():
    assert blob(path) == sha, (path, blob(path), sha)

O = load(O_PATH)
EG = load(EG_PATH)
cert = load(CERT_PATH)
dz_text = (ROOT / DZ_PATH).read_text()
ee_text = (ROOT / EE_SOURCE_PATH).read_text()

assert O["three_genus1_quotients"]["E_sigma_tau"]["map"] == ["S=t-1/t", "v=y/t^2"]
assert O["three_genus1_quotients"]["E_sigma_tau"]["model"] == "v^2=(S^2+r^2)*(S^2+4*r^2/h^2)"
assert O["notation_separation"]["physical_base_quantities"]["h"] == "p-1/p"
assert O["notation_separation"]["physical_base_quantities"]["r"] == "p+1/p"
assert O["notation_separation"]["physical_base_quantities"]["relations"][0] == "r^2-h^2=4"
assert "Z/2Z x Z/2nZ" in dz_text
assert "E_rho(Q)(2)=E_rho[2](Q)" in ee_text
assert EG["route_result"]["next_leaf"] == "36-09EH_RHO_QUOTIENT_PARAMETER_FAMILY_EXTENSION_PREFLIGHT"

# Generic root model: (X-4h)(X+4h)(X+r^2)
# gives X^3+r^2 X^2-16h^2 X-16h^2 r^2.
a2 = R2
a4 = scale(H2, -16)
a6 = scale(mul(H2, R2), -16)
assert cert["rank_and_torsion_criterion"]["expanded_model"] == "Y^2=X^3+r^2*X^2-16*h^2*X-16*h^2*r^2"

# Halving differences, replayed as polynomial identities in h.
e1 = scale(H, 4)
e2 = scale(H, -4)
e3 = neg(R2)
assert sub(e1, e2) == scale(H, 8)
assert sub(e1, e3) == mul(add(H, (2,)), add(H, (2,)))
assert sub(e2, e1) == scale(H, -8)
assert sub(e2, e3) == mul(sub(H, (2,)), sub(H, (2,)))
assert sub(e3, e1) == neg(mul(add(H, (2,)), add(H, (2,))))
assert sub(e3, e2) == neg(mul(sub(H, (2,)), sub(H, (2,))))

# h=+/-2 would require p satisfying p^2 ∓2p -1=0, discriminant 8,
# which is not a rational square.
assert 8 > 0
assert int(8 ** 0.5) ** 2 != 8

# Standard a1=a3=0 division-polynomial formula:
# psi3 = 3X^4 + b2 X^3 + 3b4 X^2 + 3b6 X + b8,
# b2=4a2, b4=2a4, b6=4a6, b8=4a2a6-a4^2.
b2 = scale(a2, 4)
b4 = scale(a4, 2)
b6 = scale(a6, 4)
b8 = sub(scale(mul(a2, a6), 4), mul(a4, a4))
assert b2 == scale(R2, 4)
assert b4 == scale(H2, -32)
assert b6 == scale(mul(H2, R2), -64)
assert b8 == scale(add(mul(H2, R4), scale(mul(H2, H2), 4)), -64)
psi3_x_coeffs = [b8, scale(b6, 3), scale(b4, 3), b2, (3,)]
assert psi3_x_coeffs[1] == scale(mul(H2, R2), -192)
assert psi3_x_coeffs[2] == scale(H2, -96)
assert cert["rank_and_torsion_criterion"]["psi3"] == "3X^4+4r^2*X^3-96h^2*X^2-192h^2*r^2*X-64h^2*(r^4+4h^2)"

# p=2 compatibility with the audited EE root model.
p = Fraction(2, 1)
h = p - 1 / p
r = p + 1 / p
assert h == Fraction(3, 2)
assert r == Fraction(5, 2)
roots = [4*h, -4*h, -(r*r)]
assert roots == [Fraction(6), Fraction(-6), Fraction(-25, 4)]
assert [100*x for x in roots] == [Fraction(600), Fraction(-600), Fraction(-625)]
assert "(x0-600)(x0+600)(x0+625)" in ee_text

# Exact logical credit ceiling.
assert cert["rational_4torsion_test"]["order4_iff"] == "8h in Q^2 or -8h in Q^2"
assert cert["rank_and_torsion_criterion"]["sel2_dimension_condition"] == 2
assert cert["rank_and_torsion_criterion"]["sel2_dimension_2_forces_rank_zero"] is True
assert cert["rank_and_torsion_criterion"]["psi3_no_rational_root_sufficient_for_no_rational_3torsion"] is True
assert cert["fixed_p_consequence"]["U_ret_C3_p_Q_empty_under_conditions"] is True
assert cert["fixed_p_consequence"]["retained_physical_receiver_sector_empty_under_conditions"] is True
assert cert["operational_reduction"]["new_parameter_outside_EG_orbit_excluded_by_this_leaf"] is False
for key, value in cert["scope_firewalls"].items():
    assert value is False, (key, value)

print("36-09EH verified: generic rho quotient is full-2-torsion with roots +/-4h,-r^2; Sel2-dim2 + no4 (+/-8h nonsquare) + no3 is a sufficient fixed-p retained-receiver exclusion criterion. No new parameter or receiver/endpoint credit.")
