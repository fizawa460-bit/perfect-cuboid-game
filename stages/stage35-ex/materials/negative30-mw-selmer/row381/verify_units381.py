#!/usr/bin/env python3
"""Check a basis for the norm-one unit squareclasses and its local intersections."""
from collections import defaultdict
from functools import cache
from math import prod
from pathlib import Path
import json

from flint import arb, arb_poly, ctx, fmpq, fmpz_poly, nmod_poly

HERE = Path(__file__).resolve().parent
from verify_row380 import CURVE, G, X, local, w_roots, prime_factors, hensel_valuation
from linear import BinarySpan, dependencies

local.PRECISION = 18
local.MODULUS = 2**(local.PRECISION//3)
roots = w_roots()
masks = [int(x,16) for x in json.loads((HERE/"row373_kummer2_membership.json").read_text())["parity_equations"]]
cutoff = local.PRECISION
wp = [[w**i for i in range(105)] for w in roots]


def divided(z, v):
    ring = z.ring
    parts = [None]*3
    for i,a in enumerate(z.parts):
        q, j = divmod(i-v,3)
        c = list(map(int,a))
        if q<0:
            f = 2**-q
            assert all(b%f==0 for b in c)
            c = [b//f for b in c]
        else:
            c = [b<<q for b in c]
        parts[j] = nmod_poly(c,local.MODULUS)
    u = local.Elt(ring,tuple(parts))
    assert u.valuation() == 0
    return u


def dyadic_profile(h, norm):
    terms = [(i,local.v2(int(c)),int(c)) for i,c in enumerate(h(X+1)) if c]
    base = min(i+3*v for i,v,c in terms)
    vals, codes = [], []
    for k,w in enumerate(roots):
        ring = w.ring
        z = ring.zero
        for i,v,c in terms:
            d = i+3*v-base
            if d<cutoff:
                z += wp[k][i]*ring.pi_powers[d]*(c>>v)
        v = z.valuation()
        if v>cutoff-9:
            return None
        vals.append(base+v)
        codes.append(ring.coordinate(divided(z,v)))
    assert local.v2(abs(norm)) == 7*vals[0]+28*vals[1]
    return vals,local.combine(codes)


def full_profile(row):
    h = fmpz_poly(row["coefficients"])
    norm = int(G.resultant(h))
    v = abs(norm)
    assert v//(v&-v) == prod(p**e for p,e in row["odd_factorization"])
    d = dyadic_profile(h if norm>0 else -h,norm)
    if d is None:
        return None
    vs, u = d
    output = {(2,i):v for i,v in enumerate(vs) if v}
    for p,e in row["odd_factorization"]:
        gn, gs = prime_factors(p)
        common = gn.gcd(nmod_poly(list(map(int,h)),p))
        hits = [(g,m,j) for g,m,j in gs if (common%g).is_zero()]
        assert hits
        if len(hits)==1:
            g,_,j=hits[0]
            assert e%g.degree()==0
            output[p,j]=e//g.degree()
        elif sum(g.degree() for g,_,_ in hits)==e:
            for _,_,j in hits:
                output[p,j]=1
        else:
            for g,m,j in hits:
                assert m==1
                output[p,j]=hensel_valuation(h,gn,g,p,e//g.degree())
            assert sum(g.degree()*output[p,j] for g,_,j in hits)==e
    return output,u,h if norm>0 else -h



def root_balls():
    ctx.prec = 2200
    F = arb_poly(CURVE["F_ascending"])
    A = arb_poly(CURVE["A_star_ascending"])
    B = arb_poly(CURVE["B_star_ascending"])
    intervals = json.loads((HERE/"real_sign_witnesses.json").read_text())["root_intervals"]
    assert len(intervals) == 7
    previous = None
    values = []
    for l,h in intervals:
        l,h = fmpq(l), fmpq(h)
        assert l < h and (previous is None or previous < l)
        previous = h
        left_sign = F(arb(l))
        assert (left_sign>0 and F(arb(h))<0) or (left_sign<0 and F(arb(h))>0)
        for _ in range(1050):
            mid = (l+h)/2
            value = F(arb(mid))
            assert value>0 or value<0
            if (value>0) == (left_sign>0):
                l = mid
            else:
                h = mid
        theta = arb(l).union(arb(h))
        denominator = B(theta)
        assert denominator>0 or denominator<0
        values.append(-A(theta)/denominator)
    return values


def sign_bits(h, real_roots):
    polynomial = arb_poly(list(map(int,h)))
    values = [polynomial(r) for r in real_roots]
    assert all(v>0 or v<0 for v in values)
    return sum((v<0)<<i for i,v in enumerate(values))


def real_obstruction(code):
    return ((code & 1)
            | ((((code>>1)^(code>>2))&1)<<1)
            | ((((code>>3)^(code>>4))&1)<<2)
            | ((((code>>5)^(code>>6))&1)<<3))


def verify_basis():
    def load(s):
        return json.loads((HERE/s).read_text())
    rows = [{"coefficients":[2],"odd_factorization":[]},
            {"coefficients":[-1,1],"odd_factorization":[]},
            {**load("dyadic_principal.json"),"odd_factorization":[]}]
    rows += load("principal_witnesses.json") + load("new_relations.json")
    basis = load("unit_basis_witnesses.json")
    assert len(rows)==4143 and len(basis)==55
    real_roots = root_balls()

    @cache
    def profile(i):
        vals, code, h = full_profile(rows[i])
        return vals, code, sign_bits(h,real_roots)

    raw = BinarySpan()
    local2 = BinarySpan()
    joint = BinarySpan()
    data = []
    obstruction_columns = []
    for w in basis:
        val = defaultdict(int)
        code = signature = 0
        combination = w["combination"]
        assert len({i for i,_ in combination}) == len(combination)
        for i,e in combination:
            assert 0 <= i < len(rows) and e!=0
            valuations,u,s = profile(i)
            for prime,exponent in valuations.items():
                val[prime] += e*exponent
            if e&1:
                code ^= u
                signature ^= s
        assert not any(val.values()) and signature.bit_count()%2==0
        assert code == int(w["unit_code"],16) and raw.add(code)
        ob = sum(((m&code).bit_count()&1)<<i for i,m in enumerate(masks))
        local2.add(ob)
        column = ob | (real_obstruction(signature)<<len(masks))
        joint.add(column)
        obstruction_columns.append(column)
        data.append({"unit_local_code":hex(code),"real_signature":hex(signature),
                     "dyadic_obstruction":hex(ob)})
    assert len(raw)==55 and len(local2)==len(joint)==46
    diagonal = (1<<21) | (1<<106)
    assert all((diagonal & m).bit_count()%2 == 0 for m in masks)
    assert raw.reduce(diagonal) != 0
    kernel = dependencies(obstruction_columns)
    assert len(kernel) == 9
    kernel_codes = []
    for c in kernel:
        code = 0
        for j,w in enumerate(data):
            if c>>j & 1:
                code ^= int(w["unit_local_code"],16)
        kernel_codes.append(code)
    unit_selmer = BinarySpan()
    assert all(unit_selmer.add(code) for code in kernel_codes)
    parent = load("row375_results.json")["unit_squareclasses_at_2"]
    old = BinarySpan()
    assert len(parent)==8 and all(old.add(int(v,16)) and not unit_selmer.reduce(int(v,16))
                                  for v in parent)
    return {"unit_squareclass_basis_dimension":len(raw),
            "rational_odd_prime_valuation_and_dyadic_checks":profile.cache_info().currsize,
            "dyadic_obstruction_rank":len(local2),"joint_dyadic_real_obstruction_rank":len(joint),
            "unit_Selmer_dimension":55-len(joint),
            "unramified_diagonal_in_unit_image":False,
            "kernel_basis_as_unit_bitmasks":list(map(hex,kernel)),
            "kernel_basis_local_codes":list(map(hex,kernel_codes)),
            "known_rational_unit_directions_contained":len(old),
            "basis_images":data}


if __name__=="__main__":
    print(json.dumps(verify_basis(),indent=2))
