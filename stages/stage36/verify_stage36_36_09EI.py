#!/usr/bin/env python3
import hashlib
import json
import math
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def blob(rel):
    return subprocess.check_output(["git", "hash-object", str(ROOT / rel)], text=True).strip()


def load(rel):
    return json.loads((ROOT / rel).read_text())


def is_square_int(n):
    if n < 0:
        return False
    r = math.isqrt(n)
    return r*r == n


def psi3_coeffs(a, b):
    N = a*a - b*b
    M = a*a + b*b
    d = a*b
    # ascending coefficients
    return [
        -64*N*N*d*d*(M**4 + 4*N*N*d*d),
        -192*N*N*d*d*M*M,
        -96*N*N*d*d,
        4*M*M,
        3,
    ]


def has_root_mod(coeffs, q):
    for x in range(q):
        y = 0
        for c in reversed(coeffs):
            y = (y*x + c) % q
        if y == 0:
            return True
    return False

EH = "stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json"
AX = "stages/stage36/36-09AX/bounded-fixed-p-tunnell-sieve-scan-preflight.json"
SOURCE = "stages/stage36/36-09EI/bounded-rho-no4-no3-screen-source-lock.md"
CERT = "stages/stage36/36-09EI/bounded-rho-no4-no3-screen-preflight.json"

expected = {
    EH: "d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37",
    AX: "e72142f2ec8a2ab0dec4a6602874e1c2edc87c60",
    SOURCE: "379f625e1eb6bad29f37fc2596c1a69913b36112",
    CERT: "979a2d58384d751a98c74555abf9581d95b30d37",
}
for path, sha in expected.items():
    assert blob(path) == sha, (path, blob(path), sha)

eh = load(EH)
ax = load(AX)
cert = load(CERT)

assert eh["route_result"]["next_leaf"] == "36-09EI_RHO_CRITERION_FIXED_P_SEARCH_PREFLIGHT"
assert eh["rational_4torsion_test"]["order4_iff"] == "8h in Q^2 or -8h in Q^2"
assert ax["scan_domain"]["a_range"] == "1..10"
assert ax["scan_domain"]["b_range"] == "1..10"
assert ax["scan_domain"]["ordered_p_count"] == 62
assert cert["scan_domain"]["ordered_parameter_count"] == 62

primes = cert["psi3_screen"]["witness_primes"]
assert primes == [5,7,11,13,17,19,23,29,31,37,41,43,47]

rows = []
for a in range(1, 11):
    for b in range(1, 11):
        if a == b or math.gcd(a,b) != 1:
            continue
        N = a*a - b*b
        d = a*b
        plus = is_square_int(8*N*d)
        minus = is_square_int(-8*N*d)
        assert not plus and not minus, (a,b,8*N*d)
        coeffs = psi3_coeffs(a,b)
        q = next((q for q in primes if not has_root_mod(coeffs,q)), None)
        assert q is not None, (a,b)
        rows.append((a,b,plus,minus,q))

assert len(rows) == 62
counts = Counter(q for _,_,_,_,q in rows)
assert counts == Counter({5:20, 11:36, 29:6}), counts
csv = "".join(f"{a},{b},{int(plus)},{int(minus)},{q}\n" for a,b,plus,minus,q in rows)
digest = hashlib.sha256(csv.encode()).hexdigest()
assert digest == "76ccf3835d0834c9f994822530719fc53e8915c1b06376c26f3f345ea7ac7973"

res = cert["exact_scan_result"]
assert res["no4_pass_count"] == 62
assert res["no3_pass_count"] == 62
assert res["all_rows_pass_no4"] is True
assert res["all_rows_pass_no3"] is True
assert res["first_witness_prime_counts"] == {"5":20,"11":36,"29":6}
assert res["row_digest_sha256"] == digest

impact = cert["criterion_impact"]
assert impact["sole_unresolved_EH_condition_on_bounded_sample"] == "dim_F2 Sel^2(E_rho,p/Q)=2"
assert impact["Sel2_computed_by_this_leaf"] is False
assert impact["new_parameter_outside_EG_orbit_excluded"] is False
for key, val in cert["scope_firewalls"].items():
    assert val is False, (key,val)

print("36-09EI verified: all 62 AX bounded parameters pass exact no4/no3 screens; Sel2 dimension is the sole unresolved EH condition on this sample. No new fixed-p/receiver/endpoint credit.")
