#!/usr/bin/env python3
"""Specify a unit Selmer class outside the eight known rational classes."""
from functools import reduce
from hashlib import sha256
from math import isqrt
from operator import xor
from pathlib import Path
import json

from flint import fmpz_poly

from row382_inputs import input_bytes

HERE = Path(__file__).resolve().parent
HASHES = {
    "units381_exact.json": "78136c1f3c1fed53c429d26fc754af33edb0106d6c119fc738f7ea9f24373bd2",
    "unit_basis_witnesses.json": "d0705fa3cb0b70084fd7f5693b7a418fcb7f226decadce578d2c356ec0cc1b3e",
    "row375_results.json": "28794c519ca99152599ccd1ef7a818f0106e2113f8a5b959daa35b6f79985d01",
    "ninth_generator_inputs.json": "0cfdd21556cb33b26d255b31b828d74ccbe00f5c03380196d3a2b9e12725fb79",
}


def read(name):
    data = (HERE/name).read_bytes()
    assert sha256(data).hexdigest() == HASHES[name]
    return json.loads(data)


def span(vectors):
    out = {0}
    for v in vectors:
        out |= {v^u for u in out}
    return out


def components(mask, rows):
    return [i for i in range(len(rows)) if mask>>i & 1]


def linear(mask, rows, col):
    return reduce(xor, (int(rows[i][col],16) for i in components(mask,rows)), 0)


def real_member(signature):
    return signature&1 == 0 and all((signature>>k) & 1 == (signature>>(k+1)) & 1 for k in (1,3,5))


def main():
    unit = read("units381_exact.json")
    basis = read("unit_basis_witnesses.json")
    images = unit["basis_images"]
    assert len(basis)==len(images)==55
    assert all(r["unit_code"]==s["unit_local_code"] for r,s in zip(basis,images,strict=True))
    kernel = [int(s,16) for s in unit["kernel_basis_as_unit_bitmasks"]]
    assert len(kernel)==9 and len(span(kernel))==512
    kernel_codes = [linear(m,images,"unit_local_code") for m in kernel]
    assert kernel_codes == [int(v,16) for v in unit["kernel_basis_local_codes"]]
    assert len(span(kernel_codes))==512
    assert all(linear(m,images,"dyadic_obstruction")==0 and real_member(linear(m,images,"real_signature")) for m in kernel)
    known = [int(v,16) for v in read("row375_results.json")["unit_squareclasses_at_2"]]
    known_space = span(known)
    assert len(known)==8 and len(known_space)==256 and known_space <= span(kernel_codes)
    complement = []
    for mask in span(kernel):
        code = linear(mask,images,"unit_local_code")
        if code in known_space:
            continue
        selected = components(mask,basis)
        odd = set()
        for i in selected:
            odd.symmetric_difference_update(j for j,e in basis[i]["combination"] if e&1)
        complement.append((len(odd),len(selected),mask,code,sorted(odd)))
    assert len(complement)==256
    factor_count, units_count, mask, code, odd = min(complement)
    assert factor_count==122 and units_count==21 and mask==0x4125e122ae5103
    factor_inputs = read("ninth_generator_inputs.json")
    assert [i for i,_ in factor_inputs]==odd
    C = json.loads(input_bytes("curve_C29.json"))
    A, B = (fmpz_poly(C[k]) for k in ["A_star_ascending","B_star_ascending"])
    X = fmpz_poly([0,1])
    G = A(-X*X)+X*B(-X*X)
    assert G.degree()==105 and G.leading_coefficient()==1
    signs = []
    norm = 1
    for i,coeffs in factor_inputs:
        n = int(G.resultant(fmpz_poly(coeffs)))
        assert n
        norm *= abs(n)
        signs.append([i,1 if n>0 else -1])
    assert isqrt(norm)**2 == norm
    print(json.dumps({
        "unit_basis_mask":hex(mask),
        "unit_basis_indices_zero_based":components(mask,basis),
        "known_rational_unit_span_dimension":8,
        "unit_selmer_dimension":9,
        "independent_local_code":hex(code),
        "real_signature":hex(linear(mask,images,"real_signature")),
        "dyadic_obstruction":hex(linear(mask,images,"dyadic_obstruction")),
        "complement_coset_size":256,
        "odd_normalized_polynomial_factors":factor_count,
        "factor_indices_and_signs":signs,
        "norm_of_squareclass_representative_is_positive_square":True,
        "four_lift_membership":"NOT_DETERMINED"
    },indent=2))


if __name__=="__main__":
    main()
