#!/usr/bin/env python3
"""Exact rational divisor lifts, 2-adic squareclasses, and first 31-adic log digits."""

import json
from pathlib import Path

from flint import fmpq, fmpq_poly, fmpz_poly, nmod_mat, nmod_poly

import row373_local_arithmetic as local
from row371_log_arithmetic import GENUS, N, P, P2, Jacobian, coeffs


def binary_rank(rows):
    pivots = {}
    for value in rows:
        while value:
            j = value.bit_length()-1
            if j not in pivots:
                pivots[j] = value
                break
            value ^= pivots[j]
    return len(pivots)


def rational_divisors(root, f, a, b):
    x = fmpz_poly([0,1])
    fq = fmpq_poly(f)
    aq = fmpq_poly(a)
    classes = [
        ("H", b, (-aq)%fmpq_poly(b), 104),
        ("D+", x-1, fmpq_poly([2**35]), 2),
        ("D-", x+1, fmpq_poly([2**35]), 2),
    ]
    extras = json.loads((root/"mw_divisors.json").read_text())
    for entry in extras:
        u = fmpz_poly(entry["u"])
        v = fmpq_poly([fmpq(c) for c in entry["v"]])
        classes.append((entry["name"], u, v, entry["m"]))
    assert [d[0] for d in classes] == [
        "H","D+","D-","D5a","D5b","D7","D14","D15a","D15b",
    ]
    assert [d[1].degree() for d in classes] == [52,1,1,3,3,6,24,24,24]
    for _,u,v,_ in classes:
        uq = fmpq_poly(u)
        assert u.leading_coefficient() == 1
        assert v.degree() < u.degree() <= GENUS
        assert not (fq-v*v)%uq
        assert u.gcd(u.derivative()).degree() == 0
        assert uq.gcd(v).degree() == 0
    by_name = {name:(u,v) for name,u,v,_ in classes}
    components = [by_name[k] for k in ("D-","D5a","D14","D15b")]
    product = fmpz_poly([1])
    for u,v in components:
        assert product.gcd(u).degree() == 0
        product *= u
        assert v == (-aq)%fmpq_poly(u)
    assert product == b
    # These components sum to H by the CRT identity on the second polynomial.
    return classes[:-1]


def unit_kummer(root, f, g, classes):
    x = fmpz_poly([0,1])
    thetas = local.local_roots(f(x-1))
    assert [theta.ring.degree for theta in thetas] == [7,28]
    assert -int(g(1)) == 2**35
    masks = [int(t,16) for t in json.loads(
        (root/"row373_kummer2_membership.json").read_text()
    )["parity_equations"]]
    assert len(masks) == binary_rank(masks) == 54
    rows = []
    for name,u,_,m in classes:
        sign = (-1)**u.degree()
        assert m >= 0 and m % 2 == 0
        assert sign*int(f.resultant(u)) == 2**(35*m)
        shifted = u(x-1)
        codes = []
        for theta in thetas:
            ring = theta.ring
            normalized = sign*local.evaluate(ring.scaled_polynomial(shifted,m),theta)
            assert normalized.valuation() == 0
            # Both t^m and pi^m are squares, so no t/p uniformizer choice enters.
            codes.append(ring.coordinate(normalized))
        code = local.combine(codes)
        assert all((code & mask).bit_count()%2 == 0 for mask in masks)
        rows.append(code)
    assert binary_rank(rows) == 8
    r = (1<<21)|(1<<106)
    assert all((r&mask).bit_count()%2 == 0 for mask in masks)
    assert binary_rank(rows+[r]) == 9
    return rows,r


def sign_on_interval(poly, left, right):
    mid = (left+right)/2
    value = fmpq_poly(poly)(mid)
    radius = max(fmpq(1), abs(left), abs(right))
    derivative_bound = sum(
        abs(int(c))*i*radius**(i-1) for i,c in enumerate(poly) if i
    )
    assert abs(value) > (right-left)*derivative_bound/2
    return 1 if value > 0 else -1


def real_signature_rank(root, f, a, b):
    witness = json.loads((root/"real_sign_witnesses.json").read_text())
    F = fmpq_poly(f)
    intervals = []
    for left,right in witness["root_intervals"]:
        lo,hi = fmpq(left),fmpq(right)
        v = F(lo)
        assert lo < hi and v*F(hi) < 0
        for _ in range(768):
            mid = (lo+hi)/2
            side = F(mid)*v
            assert side
            if side > 0:
                lo = mid
            else:
                hi = mid
        intervals.append((lo,hi))
    assert len(intervals) == 7
    t_sign = [sign_on_interval(-a-b,l,h)*sign_on_interval(b,l,h) for l,h in intervals]
    x = fmpz_poly([0,1])
    thetas = local.local_roots(f(x-1))
    signatures = []
    for entry in witness["units"]:
        poly = fmpz_poly(entry["polynomial"])
        m,sign = entry["m"],entry["sign"]
        assert m >= 0 and sign in (-1,1)
        assert int(f.resultant(poly)) == sign*2**(35*m)
        shifted = poly(x-1)
        for theta in thetas:
            normalized = local.evaluate(theta.ring.scaled_polynomial(shifted,m),theta)
            assert normalized.valuation() == 0
        values = [
            sign*sign_on_interval(poly,l,h)*t**(m%2)
            for (l,h),t in zip(intervals,t_sign)
        ]
        bits = sum((s < 0)<<i for i,s in enumerate(values))
        assert bits.bit_count()%2 == 0 and bits == int(entry["real_sign_bits"],16)
        signatures.append(bits)
    assert len(signatures) == binary_rank(signatures) == 6
    assert binary_rank(signatures+[127]) == 7
    return [hex(s) for s in signatures]


def mod_p2(poly):
    digits = [int(c.numerator)*pow(int(c.denominator),-1,P2)%P2 for c in poly]
    return nmod_poly(digits,P2)


def first_logs(root, f, classes):
    J = Jacobian(list(map(int,f)))
    assert J.f0.gcd(J.f0.derivative()) == 1 and N % P == 13
    residues = []
    for _,u,v,_ in classes:
        D = nmod_poly(coeffs(u),P2),mod_p2(v)
        J.validate(D)
        assert J.finite_mul(D,N)[0] == 1
        residues.append(D)
    discs = J.quadratic_lifts()
    assert len(discs) == 226
    runs = []
    trace_rows = []
    for seed,target in [(375,0),(376,4)]:
        shifts = J.make_shifts(discs,seed)
        digits = []
        terminals = []
        for D in residues:
            shifted, stats = J.shifted_mul(D,N,shifts,target)
            digit = J.first_log_digit(shifts[target],shifted)
            digits.append([a*pow(N,-1,P)%P for a in digit])
            terminals.append({
                "terminal":list(map(coeffs,shifted)),
                "chart":stats,
            })
        trace_rows.append(digits)
        runs.append({
            "seed":seed,"target":target,"initial":list(map(coeffs,shifts[target])),
            "classes":terminals,
        })
    assert trace_rows[0] == trace_rows[1]
    rows = trace_rows[0]
    assert rows[:3] == json.loads((root/"row371_parent_digits.json").read_text())
    e = [[int(i==j) for j in range(GENUS)] for i in range(2)]
    matrix = nmod_mat([r[:10] for r in rows+e],P)
    assert matrix.det() == 6 and nmod_mat(rows,P).rank() == 8
    inv = matrix.inv()
    dual = [[int(inv[j,i]) for j in range(10)] for i in (8,9)]
    for i,form in enumerate(dual):
        values = [sum(u*v for u,v in zip(r,form))%P for r in rows+e]
        assert values == [int(j==8+i) for j in range(10)]
    return rows,dual,runs,J.finite_crosschecks


def main():
    root = Path(__file__).resolve().parent
    data = json.loads((root/"curve_C29.json").read_text())
    f,a,b = (fmpz_poly(data[k]) for k in ("F_ascending","A_star_ascending","B_star_ascending"))
    x = fmpz_poly([0,1])
    assert f == a*a+x*b*b and f.degree() == 105
    g = a(-x*x)+x*b(-x*x)
    assert g.degree() == 105 and g.leading_coefficient() == 1
    assert g(x)*g(-x) == f(-x*x)

    classes = rational_divisors(root,f,a,b)
    units,r = unit_kummer(root,f,g,classes)
    signatures = real_signature_rank(root,f,a,b)
    rows,dual,runs,crosschecks = first_logs(root,f,classes)
    result = {
        "names":[d[0] for d in classes],
        "redundant_divisor_relation":"D15b = H - D- - D5a - D14",
        "unit_squareclasses_at_2":[hex(u) for u in units],
        "unit_squareclass_rank":8,"unramified_diagonal":hex(r),
        "rank_after_adding_unramified_diagonal":9,
        "norm_one_unit_real_signatures":signatures,
        "full_unit_signature_rank":7,
        "log31_div31_digits":rows,"rank_known_logs":8,
        "rank_logs_plus_source_jets":10,"determinant_columns_0_to_9_mod31":6,
        "dual_forms_supported_on_columns_0_to_9":dual,
        "finite_cantor_crosschecks":crosschecks,
        "log31_trace_runs":runs,
    }
    (root/"row375_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print("exact divisor congruences over Q, eight classes and the CRT identity for D15b")
    print("2-adic unit squareclasses rank 8; rank 9 with unramified diagonal")
    print("unramified diagonal satisfies all 54 local Kummer equations")
    print("real unit signature rank 7; narrow and ordinary class groups agree")
    print("two independent 31^2 chart runs agree in all 52 coordinates")
    print("finite Cantor arithmetic crosschecks",crosschecks)
    print("rank of eight logarithms 8; rank with two jets 10; determinant 6 mod 31")
    print("dual forms on columns 0..9",dual)


if __name__ == "__main__":
    main()
