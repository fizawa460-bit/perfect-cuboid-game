#!/usr/bin/env python3
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(rel):
    return json.loads((ROOT / rel).read_text())


def blob(rel):
    return subprocess.check_output(["git", "hash-object", str(ROOT / rel)], text=True).strip()


def c_of(p):
    return (p + 1) / (p - 1)


def coeffs(p):
    c = c_of(p)
    return sorted([p*p, 1/(p*p), c*c, 1/(c*c)])

O_PATH = "stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json"
AW_PATH = "stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json"
EF_PATH = "stages/stage36/36-09EF/fixed-p2-physical-receiver-adapter-preflight.json"
RECEIPT_PATH = "stages/stage36/36-09EF/hostile-audit-pass-consumption.json"
SOURCE_PATH = "stages/stage36/36-09EG/p2-parameter-orbit-impact-source-lock.md"
CERT_PATH = "stages/stage36/36-09EG/fixed-p2-parameter-orbit-impact-preflight.json"

expected = {
    O_PATH: "6a2678ebedba40e13277100441361039ee47ca28",
    AW_PATH: "c1970a020803275ba87b249229e319367fa8f811",
    EF_PATH: "7ba7dd6df5d118868e0344d9d568c62c4058efdd",
    RECEIPT_PATH: "5c6a73434c179fc3e1d11c301d1045a5f23bce2a",
    SOURCE_PATH: "8f1b7fdee751acd673e8d565bfd697db548efa30",
    CERT_PATH: "5a2977d3eafe9ea1d4751dc386e6a7b3aad01dc3",
}
for path, sha in expected.items():
    assert blob(path) == sha, (path, blob(path), sha)

O = load(O_PATH)
AW = load(AW_PATH)
EF = load(EF_PATH)
receipt = load(RECEIPT_PATH)
cert = load(CERT_PATH)

assert O["top_genus3_exact_factorization"]["normalized_model"] == "C3_p: y^2=(t^2+p^2)*(t^2+p^(-2))*(t^2+c^2)*(t^2+c^(-2))"
assert O["notation_separation"]["physical_base_quantities"]["c"] == "(p+1)/(p-1)"
assert O["notation_separation"]["physical_exclusions"] == ["p=0", "p=1", "p=-1", "t=0", "t=1", "t=-1", "t=infinity"]
assert "primitive p=a/b" in AW["fixed_p_outer_enumerator"]["input"]

assert EF["physical_receiver_consequence"]["fixed_p2_retained_receiver_sector_empty"] is True
assert EF["physical_receiver_consequence"]["fixed_p_parameter_exclusion_obtained"] is True
assert EF["physical_receiver_consequence"]["excluded_parameter"] == "p=2"
assert EF["rational_point_consequence"]["U_ret_C3_2_Q_empty"] is True
assert receipt["audit_pr"] == 1741
assert receipt["audited_exact_head"] == "5ea451cdf0efdd87f57fc87d5ada881ac637a183"
assert receipt["hostile_audit_review_id"] == 5150902901
assert receipt["hostile_audit_result"] == "PASS"
assert receipt["consumption_result"]["36_09EF_pass_consumed"] is True
assert receipt["consumption_result"]["36_09EG_entry_allowed"] is True

seed = Fraction(2, 1)
seed_coeffs = coeffs(seed)
assert seed_coeffs == [Fraction(1,9), Fraction(1,4), Fraction(4,1), Fraction(9,1)]

orbit = [Fraction(1,3), Fraction(1,2), Fraction(2,1), Fraction(3,1)]
expected_c = {
    Fraction(1,3): Fraction(-2,1),
    Fraction(1,2): Fraction(-3,1),
    Fraction(2,1): Fraction(3,1),
    Fraction(3,1): Fraction(2,1),
}
for q in orbit:
    assert q > 0 and q != 1
    assert c_of(q) == expected_c[q]
    assert coeffs(q) == seed_coeffs

# Completeness of the positive literal-equation orbit: q^2 is one of the four
# coefficient values, and positive q therefore has exactly these four values.
positive_roots = sorted({Fraction(1,3), Fraction(1,2), Fraction(2,1), Fraction(3,1)})
assert positive_roots == orbit
for q in positive_roots:
    assert q*q in set(seed_coeffs)

assert cert["literal_curve_orbit"]["positive_parameters"] == ["1/3", "1/2", "2", "3"]
assert cert["literal_curve_orbit"]["all_four_parameters_physically_allowed"] is True
assert cert["literal_curve_orbit"]["normalized_curves_literally_equal_over_Q"] is True
assert cert["literal_curve_orbit"]["change_of_variable_used"] is False
assert cert["literal_curve_orbit"]["quadratic_twist_used"] is False
assert cert["literal_curve_orbit"]["scalar_extension_used"] is False
assert cert["literal_curve_orbit"]["literal_positive_orbit_complete"] is True

impact = cert["receiver_impact"]
assert impact["excluded_positive_parameter_values"] == ["1/3", "1/2", "2", "3"]
assert impact["excluded_positive_parameter_count"] == 4
assert impact["each_fixed_parameter_receiver_sector_empty"] is True
assert impact["fixed_parameter_exclusion_registry_expanded"] is True
assert impact["candidate_parameter_set_shrunk"] is False
assert impact["receiver_emptiness_proved"] is False
assert impact["R29_CAMP2_closed"] is False

fw = cert["scope_firewalls"]
for key in [
    "all_positive_rational_p_excluded",
    "candidate_parameter_set_shrunk",
    "receiver_emptiness_proved",
    "R29_CAMP2_closed",
    "Q11_CAMPEDELLI_closed",
    "endpoint_closed",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False

print("36-09EG verified: audited p=2 exclusion propagates by literal C3 equality exactly to positive p={1/3,1/2,2,3}; no finite-candidate/full-receiver/endpoint credit.")
