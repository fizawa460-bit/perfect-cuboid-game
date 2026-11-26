#!/usr/bin/env python3
"""Exact verification of the Farkas certificates for P3 (added in audit round 2).

Claim being certified: the dual cone {x in W : x . E >= 0 for all 140 known
curves E} is {0}. Here W is the 62-dimensional lattice spanned by G, F and the
38 common vertical curves; pair140[k] is the vector of pairings of the k-th
known curve with a fixed basis of W (exact integers, in g3_data_<tag>.json).

Farkas certificate: rationals lambda_k > 0 (k = 1..140) with
sum_k lambda_k * pair140[k] = 0 exactly. If such lambda exist, then any
x in W with x . E_k >= 0 for all k satisfies
0 = sum_k lambda_k (x . E_k) and every term is >= 0 with lambda_k > 0,
so x . E_k = 0 for all k; the pairing matrix has rank 62 (the certificate
also carries 62 pivot rows whose exact minor determinant is nonzero),
hence x = 0. This script checks all of that in exact rational arithmetic.

Usage: python3 g3_farkas_verify.py   (needs sympy; reads the two
g3_data_<tag>.json and g3_farkas_<tag>.json files next to this script)
"""
import json
import os

from sympy import Matrix, Rational

HERE = os.path.dirname(os.path.abspath(__file__))


def check(tag):
    data = json.load(open(os.path.join(HERE, f"g3_data_{tag}.json")))
    cert = json.load(open(os.path.join(HERE, f"g3_farkas_{tag}.json")))
    A = data["pair140"]                      # 140 x 62 ints
    assert len(A) == 140 and all(len(row) == 62 for row in A), "pair140 shape"
    lam = [Rational(x) for x in cert["lambda"]]
    assert len(lam) == 140, "lambda length"
    assert all(x > 0 for x in lam), "all lambda_k must be > 0"
    total = [Rational(0)] * 62
    for k in range(140):
        if lam[k]:
            row = A[k]
            for j in range(62):
                total[j] += lam[k] * row[j]
    assert all(t == 0 for t in total), "sum lambda_k a_k must be 0"
    piv = cert["pivot_rows"]
    assert len(piv) == 62 and len(set(piv)) == 62, "62 distinct pivot rows"
    minor = Matrix([[A[r][j] for j in range(62)] for r in piv])
    det = minor.det()
    assert det != 0 and int(det) == int(cert["minor_det"]), "pivot minor determinant"
    print(f"{tag}: lambda>0 OK, sum lambda*a = 0 OK, rank-62 minor det != 0 OK")
    return True


def main():
    for tag in ("B8", "B16"):
        check(tag)
    print("FARKAS CERTIFICATES VERIFIED (dual cone = {0}, both maps)")


if __name__ == "__main__":
    main()
