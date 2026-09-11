#!/usr/bin/env python3
import hashlib
import json
import math
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

EH = "stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json"
EI = "stages/stage36/36-09EI/bounded-rho-no4-no3-screen-preflight.json"
DW_SOURCE = "stages/stage36/36-09DW/phi-selmer-five-place-local-image-source-lock.md"
EC_SOURCE = "stages/stage36/36-09EC/factor-proselmer-mw-closure-source-lock.md"
SOURCE = "stages/stage36/36-09EJ/bounded-rho-sel2-exact-computation-source-lock.md"
CERT = "stages/stage36/36-09EJ/bounded-rho-sel2-exact-computation-preflight.json"


def blob(rel):
    return subprocess.check_output(["git", "hash-object", str(ROOT / rel)], text=True).strip()


def load(rel):
    return json.loads((ROOT / rel).read_text())


expected = {
    EH: "d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37",
    EI: "979a2d58384d751a98c74555abf9581d95b30d37",
    DW_SOURCE: "08c91eed30774fa5c44509bb61f1c3b1386f2266",
    EC_SOURCE: "c3bc3947747ad72a7708cbdce5b109a9286be6d3",
    SOURCE: "3edce400c120880e1116ed68cef8a727887f49c0",
    CERT: "7ff288962132cae21f30a3c7b05ee1e5b5680c91",
}
for path, sha in expected.items():
    assert blob(path) == sha, (path, blob(path), sha)


eh = load(EH)
ei = load(EI)
cert = load(CERT)
dw_text = (ROOT / DW_SOURCE).read_text()
ec_text = (ROOT / EC_SOURCE).read_text()

assert eh["route_result"]["next_leaf"] == "36-09EI_RHO_CRITERION_FIXED_P_SEARCH_PREFLIGHT"
assert eh["rank_and_torsion_criterion"]["sel2_dimension_condition"] == 2
assert eh["fixed_p_consequence"]["retained_physical_receiver_sector_empty_under_conditions"] is True
assert ei["exact_scan_result"]["all_rows_pass_no4"] is True
assert ei["exact_scan_result"]["all_rows_pass_no3"] is True
assert ei["scan_domain"]["ordered_parameter_count"] == 62
assert "F2-dimension `2` for odd residue characteristic" in dw_text
assert "F2-dimension `3` over `Q_2`" in dw_text
assert "dim Sel_2(E_rho/Q)=2" in ec_text


# ---------- F2 linear algebra ----------
def rref(vs):
    if not vs:
        return ()
    rows = [list(map(int, v)) for v in vs if any(v)]
    if not rows:
        return ()
    n = len(vs[0])
    rr = 0
    for j in range(n):
        q = next((i for i in range(rr, len(rows)) if rows[i][j]), None)
        if q is None:
            continue
        rows[rr], rows[q] = rows[q], rows[rr]
        for i in range(len(rows)):
            if i != rr and rows[i][j]:
                rows[i] = [x ^ y for x, y in zip(rows[i], rows[rr])]
        rr += 1
        if rr == len(rows):
            break
    return tuple(tuple(x) for x in rows[:rr])


def rank(vs):
    return len(rref(vs))


def nullspace(rows, n):
    a = [list(map(int, r)) for r in rows if any(r)]
    piv = []
    rr = 0
    for j in range(n):
        q = next((i for i in range(rr, len(a)) if a[i][j]), None)
        if q is None:
            continue
        a[rr], a[q] = a[q], a[rr]
        for i in range(len(a)):
            if i != rr and a[i][j]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rr])]
        piv.append(j)
        rr += 1
        if rr == len(a):
            break
    free = [j for j in range(n) if j not in piv]
    out = []
    for f in free:
        x = [0] * n
        x[f] = 1
        for i, p in reversed(list(enumerate(piv))):
            s = 0
            for j in free:
                s ^= a[i][j] & x[j]
            x[p] = s
        out.append(tuple(x))
    return out


# ---------- arithmetic / squareclasses ----------
def vpi(n, p):
    if n == 0:
        return 10**9
    n = abs(n)
    z = 0
    while n % p == 0:
        z += 1
        n //= p
    return z


def is_qp_square_int(n, p):
    if n == 0:
        return True
    z = vpi(n, p)
    if z & 1:
        return False
    u = (n // (p ** z))
    if p == 2:
        return u % 8 == 1
    u %= p
    return pow(u, (p - 1) // 2, p) == 1


def sc_int(n, p):
    assert n != 0
    z = vpi(n, p)
    u = n // (p ** z)
    if p == 2:
        um = u % 8
        nm = {1: (0, 0), 3: (1, 1), 5: (0, 1), 7: (1, 0)}[um]
        return (z & 1,) + nm
    um = u % p
    return (z & 1, 0 if pow(um, (p - 1) // 2, p) == 1 else 1)


def sc_real(n):
    assert n != 0
    return (1 if n < 0 else 0,)


def prime_factors(n):
    n = abs(n)
    out = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        out.append(n)
    return out


def curve_roots(a, b):
    N = a * a - b * b
    M = a * a + b * b
    d = a * b
    return 4 * N * d, -4 * N * d, -M * M


def finite_support(e1, e2, e3):
    ps = {2}
    for z in (e1 - e2, e1 - e3, e2 - e3):
        ps.update(prime_factors(z))
    return sorted(ps)


def torsion_kummers(e1, e2, e3, place):
    pairs = [
        ((e1 - e2) * (e1 - e3), e1 - e2),
        (e2 - e1, (e2 - e1) * (e2 - e3)),
    ]
    out = []
    for a, b in pairs:
        if place == "infinity":
            out.append(sc_real(a) + sc_real(b))
        else:
            out.append(sc_int(a, place) + sc_int(b, place))
    return out


def local_span(e1, e2, e3, p, bound):
    out = list(torsion_kummers(e1, e2, e3, p))
    for x in range(-bound, bound + 1):
        if x in (e1, e2, e3):
            continue
        rhs = (x - e1) * (x - e2) * (x - e3)
        if is_qp_square_int(rhs, p):
            out.append(sc_int(x - e1, p) + sc_int(x - e2, p))
    return rref(out)


def real_span(e1, e2, e3):
    return rref(torsion_kummers(e1, e2, e3, "infinity"))


def global_generator_local_bits(g, place):
    if place == "infinity":
        return sc_real(g)
    return sc_int(g, place)


def sel2_row(a, b):
    e1, e2, e3 = curve_roots(a, b)
    N = a * a - b * b
    M = a * a + b * b
    d = a * b
    assert e1 - e2 == 8 * N * d
    assert e1 - e3 == (N + 2 * d) ** 2
    assert e2 - e3 == (N - 2 * d) ** 2

    S = finite_support(e1, e2, e3)
    gens = [-1] + S
    m = len(gens)
    ambient = 2 * m
    constraints = []

    places = ["infinity"] + S
    for place in places:
        if place == "infinity":
            W = real_span(e1, e2, e3)
            dloc = 1
            target = 1
        else:
            W = local_span(e1, e2, e3, place, 50)
            dloc = 3 if place == 2 else 2
            target = 3 if place == 2 else 2
        assert rank(W) == target, (a, b, place, W, target)

        orth = nullspace(W, 2 * dloc)
        locgens = [global_generator_local_bits(g, place) for g in gens]
        for z in orth:
            z1 = z[:dloc]
            z2 = z[dloc:]
            row = [0] * ambient
            for j, lg in enumerate(locgens):
                row[j] = sum(x * y for x, y in zip(z1, lg)) & 1
                row[m + j] = sum(x * y for x, y in zip(z2, lg)) & 1
            constraints.append(tuple(row))

    cr = rank(constraints)
    dim = ambient - cr
    return S, ambient, cr, dim


# ---------- exact 62-row replay ----------
pairs = []
for a in range(1, 11):
    for b in range(1, 11):
        if a != b and math.gcd(a, b) == 1:
            pairs.append((a, b))
assert len(pairs) == 62

# Certify the deterministic local witness bound and the claimed maximum minimum bound.
minimum_bound_records = []
for a, b in pairs:
    e1, e2, e3 = curve_roots(a, b)
    for p in finite_support(e1, e2, e3):
        target = 3 if p == 2 else 2
        hit = None
        for bound in range(0, 51):
            if rank(local_span(e1, e2, e3, p, bound)) == target:
                hit = bound
                break
        assert hit is not None, (a, b, p)
        minimum_bound_records.append((hit, a, b, p))
max_hit = max(x[0] for x in minimum_bound_records)
max_cases = sorted((a, b, p) for hit, a, b, p in minimum_bound_records if hit == max_hit)
assert max_hit == 47
assert max_cases == [(6, 7, 97), (7, 6, 97)]

rows = []
dims = Counter()
dim2_rows = []
for a, b in pairs:
    S, ambient, cr, dim = sel2_row(a, b)
    dims[dim] += 1
    if dim == 2:
        dim2_rows.append([a, b])
    rows.append((a, b, ";".join(map(str, S)), ambient, cr, dim))

assert dims == Counter({4: 30, 2: 14, 3: 14, 5: 4}), dims
expected_dim2_rows = [[1,2],[1,3],[1,5],[2,1],[2,3],[2,7],[2,9],[3,1],[3,2],[5,1],[5,9],[7,2],[9,2],[9,5]]
assert dim2_rows == expected_dim2_rows

csv = "".join(f"{a},{b},{S},{ambient},{cr},{dim}\n" for a, b, S, ambient, cr, dim in rows)
digest = hashlib.sha256(csv.encode()).hexdigest()
assert digest == "1a1ef2d5c15d74062f6af417f88b70ec358012afceb8c18aa9d4b55c7133eeea"

res = cert["exact_result"]
assert res["sel2_dimension_distribution"] == {"2":14,"3":14,"4":30,"5":4}
assert res["sel2_dimension_2_rows"] == expected_dim2_rows
assert res["p2_and_reciprocal_reproduce_fixed_rho_sel2_dim2"] is True
assert sel2_row(2,1)[3] == 2
assert sel2_row(1,2)[3] == 2

assert cert["global_sel2_intersection"]["row_digest_sha256"] == digest
assert cert["local_kummer_exactness"]["all_required_local_images_saturated"] is True
assert cert["local_kummer_exactness"]["largest_minimum_witness_abs_x"] == 47

new_params = ["1/5","5","2/3","3/2","2/7","7/2","2/9","9/2","5/9","9/5"]
cc = cert["criterion_consumption"]
assert cc["EI_no4_pass_all_62"] is True
assert cc["EI_no3_pass_all_62"] is True
assert cc["EH_complete_criterion_satisfied_on_all_14_dim2_rows"] is True
assert cc["new_excluded_parameters_outside_EG_orbit"] == new_params
assert cc["new_excluded_parameter_count"] == 10
assert cc["expanded_fixed_parameter_registry_count"] == 14
assert cc["new_parameter_outside_EG_orbit_excluded"] is True
assert cc["each_new_fixed_parameter_receiver_sector_empty"] is True

for key, value in cert["scope_firewalls"].items():
    assert value is False, (key, value)

print("36-09EJ verified: exact full-2 local Kummer intersections give Sel2 dimensions 2:14,3:14,4:30,5:4 on the 62-row AX box; EI+EH then exclude ten new fixed-p sectors outside the prior C3_2 orbit. No finite-ledger/full-receiver/endpoint credit.")
