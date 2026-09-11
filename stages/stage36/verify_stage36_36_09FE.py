#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09FE/rho-forced-crt-factor-shape-realization-preflight.json"
FD = ROOT / "stages/stage36/36-09FD/rho-fixed-quartic-frobenius-seed-crt-preflight.json"
FA = ROOT / "stages/stage36/36-09FA/rho-residual-core-partial-legendre-chart-preflight.json"
FB = ROOT / "stages/stage36/36-09FB/rho-one-bit-splitting-realization-preflight.json"
SOURCE = ROOT / "stages/stage36/36-09FE/rho-forced-crt-factor-shape-realization-source-lock.md"

EXPECTED = {
    FD: "0a397081cc689a85120328764d7a633da2542eff",
    FA: "499ac146f0d453a7a7abee565e4dcfb4aec982ed",
    FB: "a48aa0032a4cf7789702458df2c537f2d1cf2e16",
    SOURCE: "bf002a79950da8e9c0387df638ff05a519bdd9fe",
    CERT: "56a30188f0e09e6a54ad5b395ac8aea3f4274b0b",
}


def blob_sha(path):
    return subprocess.check_output(["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True).strip()


def is_prime(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic for n < 2^64.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factor_dict_to_pair(d):
    vals = []
    for k, e in d.items():
        vals.extend([int(k)] * int(e))
    return sorted(vals)


def check_row(row):
    K, U0, M = 729, 17627, 34440
    j, u = row["j"], row["u"]
    branch = row["branch"]
    pfs = row["P_over_7_factors"]
    qfs = row["Qabs_over_41_factors"]
    assert u == U0 + M * j
    assert branch in (6, 9) and j % 17 == branch
    expected_u_residue = 224267 if branch == 6 else 327587
    assert u % 585480 == expected_u_residue
    f, e = 2 * u + K, 4 * u + K
    P = 8 * u * u - K * K
    Qabs = 8 * u * u + 8 * K * u + K * K
    assert len(pfs) == len(qfs) == 2
    assert P == 7 * pfs[0] * pfs[1]
    assert Qabs == 41 * qfs[0] * qfs[1]
    assert 17 in pfs
    all_primes = [u, f, e, 7, 41] + pfs + qfs
    assert max(all_primes) < 2**64
    assert all(is_prime(x) for x in all_primes)
    assert len(set(all_primes)) == len(all_primes)
    assert all(p % 8 == 1 for p in pfs)
    assert all(q % 8 == 7 for q in qfs)
    assert sorted(p % 3 for p in pfs) == [1, 2]
    assert u % 8 == 3 and f % 8 == 7 and e % 8 == 5


for path, sha in EXPECTED.items():
    assert blob_sha(path) == sha, (path, blob_sha(path), sha)

c = json.loads(CERT.read_text())
fd = json.loads(FD.read_text())
fa = json.loads(FA.read_text())
fb = json.loads(FB.read_text())

assert c["schema"] == "STAGE36_36_09FE_RHO_FORCED_CRT_FACTOR_SHAPE_REALIZATION_PREFLIGHT_V1"
assert c["status"] == "PROVISIONAL_EXACT_BOTH_SEED17_BRANCHES_FACTOR_SHAPE_REALIZED_PENDING_CI"
assert c["entry_authority"]["v294_exact_head"] == "cec3ff043efe72025ec6f9ee232c9f0bd6a7b1d1"
assert c["entry_authority"]["v294_exact_head_ci"] == "34424593468/102707016628"
assert c["entry_authority"]["36_09FE_entry_allowed"] is True
assert c["entry_authority"]["fixed_parameter_exclusion_registry_count"] == 224

s17 = c["seed17_forcing"]
assert s17["p0"] == 17 and s17["j_residues_mod17"] == [6, 9]
assert s17["forced_P1_factor"] == 17 and s17["FD_forces_B_minus_on_factor_shape"] is True
assert fd["seed_17"]["p0"] == 17
assert fd["seed_17"]["j_roots_mod_p0"] == [6, 9]
assert fd["seed_17"]["u_progressions"] == s17["u_progressions"]
# Recheck that 17 is a good fixed-quartic seed: F=(Y^2-7)(Y^2-12) mod 17,
# with both 7 and 12 nonsquares.
qr = {x*x % 17 for x in range(1, 17)}
assert 7 not in qr and 12 not in qr
for y in range(17):
    lhs = (y**4 - 2*y*y - 1) % 17
    rhs = ((y*y - 7) * (y*y - 12)) % 17
    assert lhs == rhs

promoted = c["promoted_authority_realizations"]
assert len(promoted) == 4
for row in promoted:
    check_row(row)

# Bind the two branch-9 witnesses to exact FA authority.
fa_by_j = {r["j"]: r for r in fa["arithmetic_realizations"]}
for row in [r for r in promoted if r["source"] == "FA"]:
    old = fa_by_j[row["j"]]
    assert old["u"] == row["u"]
    assert factor_dict_to_pair(old["factorization"]["s"]) == sorted(row["P_over_7_factors"])
    assert factor_dict_to_pair(old["factorization"]["t"]) == sorted(row["Qabs_over_41_factors"])
    assert old["support_rank"] == 22 and old["EH_no4_no3"] is True

# Bind the two branch-6 witnesses to exact FB authority.
fb_by_j = {r["j"]: r for r in fb["arithmetic_realizations"]}
for row in [r for r in promoted if r["source"] == "FB"]:
    old = fb_by_j[row["j"]]
    assert old["u"] == row["u"]
    assert factor_dict_to_pair(old["factorization"]["s"]) == sorted(row["P_over_7_factors"])
    assert factor_dict_to_pair(old["factorization"]["t"]) == sorted(row["Qabs_over_41_factors"])
    assert old["B"] == -1

th = c["finite_compatibility_theorem"]
assert th["branch6_exact_factor_shape_realization_count_from_promoted_authority"] == 2
assert th["branch9_exact_factor_shape_realization_count_from_promoted_authority"] == 2
assert th["both_seed17_branches_nonempty_in_exact_FB_factor_shape"] is True
assert th["local_or_congruence_incompatibility_of_a_whole_seed17_branch_excluded"] is True
assert th["unbounded_realization_proved"] is False and th["infinitely_many_realizations_proved"] is False
assert sum(r["branch"] == 6 for r in promoted) == 2
assert sum(r["branch"] == 9 for r in promoted) == 2

# Extra rows are exact arithmetic diagnostics only; they do not receive registry credit.
diag = c["additional_exact_diagnostics"]
assert len(diag) == 2
for row in diag:
    check_row(row)
    assert row["registry_promotion_claimed"] is False
assert {r["branch"] for r in diag} == {6, 9}

ri = c["registry_impact"]
assert ri["previous_count"] == ri["provisional_count"] == 224
assert ri["new_orbits_promoted"] == ri["new_parameters_promoted"] == 0
assert ri["diagnostic_disjointness_against_full_registry_claimed"] is False

scope = c["scope_firewalls"]
for key in (
    "positive_density_proved", "simultaneous_primality_infinitude_proved",
    "semiprime_factorization_infinitude_proved", "sieve_theorem_proved",
    "FB_B_minus_necessary_proved", "candidate_parameter_set_shrunk",
    "receiver_emptiness_proved", "R29_CAMP2_closed", "Q11_CAMPEDELLI_closed",
    "endpoint_closed", "perfect_cuboid_nonexistence_claim"
):
    assert scope[key] is False

assert c["route_result"]["next_leaf"] == "36-09FF_RHO_FORCED_CRT_FACTOR_SHAPE_UNBOUNDED_CONTROL_PREFLIGHT"
assert c["route_result"]["next_leaf_entry_allowed"] is False
print("36-09FE verified: both seed-17 forced CRT branches have exact promoted FB factor-shape realizations; two extra rows replay exactly; registry remains 224 and unbounded/receiver/endpoint credit stays closed.")
