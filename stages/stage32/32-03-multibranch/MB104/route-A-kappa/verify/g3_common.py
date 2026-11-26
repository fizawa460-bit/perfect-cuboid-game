#!/usr/bin/env python3
"""Shared exact lattice setup for the G3 attack on the kappa lemma.

Coordinates: classes are integer vectors in the retained 64-dim basis;
pairing is via the Gram matrix in picard_base_rows.json.
Correct P is stage1_G.json's vP (stage1_classes.json's vP is wrong).
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy
from sympy import Matrix, Rational, zeros

HERE = Path(__file__).resolve().parent


def load_all():
    bundle = json.loads((HERE / "picard_base_rows.json").read_text())
    gram = Matrix(bundle["picard_gram_64x64"])
    classes_j = json.loads((HERE / "stage1_classes.json").read_text())
    g_j = json.loads((HERE / "stage1_G.json").read_text())
    stage3 = json.loads((HERE / "stage3_kappa.json").read_text())
    curves = {int(k): Matrix(v) for k, v in classes_j["classes"].items()}
    vH = Matrix(classes_j["vH"])
    vP = Matrix(g_j["vP"])  # correct P
    vG = Matrix(g_j["vG"])
    return gram, curves, vH, vP, vG, stage3


def pair(gram, x, y):
    return (x.T * gram * y)[0]


def f_class(gram, curves, vH, B):
    """F_j with 2F = H - sum_{n in B} E_n, E_n = curve label 93+n."""
    tot = vH.copy()
    for n in B:
        tot -= curves[93 + n]
    assert all(int(v) % 2 == 0 for v in tot), "2F not divisible"
    return Matrix([int(v) // 2 for v in tot])


def proj_square(gram, basis_vecs, target):
    """-(proj of target onto span of basis_vecs)^2, exact Rational.
    basis_vecs: list of column Matrices assumed linearly independent."""
    if not basis_vecs:
        return Rational(0)
    Bm = Matrix.hstack(*basis_vecs)
    G = Bm.T * gram * Bm
    rhs = Bm.T * gram * target
    coeff = G.LUsolve(rhs)
    proj = Bm * coeff
    return -pair(gram, proj, proj)


def kappa_for(gram, curves, vH, vP, vG, B):
    F = f_class(gram, curves, vH, B)
    common = [lab for lab, c in sorted(curves.items())
              if pair(gram, c, vG) == 0 and pair(gram, c, F) == 0]
    vecs = [curves[lab] for lab in common]
    # rank of common span
    M = Matrix.hstack(*vecs)
    rank = M.rank()
    kap = proj_square(gram, independent_subset(gram, vecs), vP)
    return F, common, rank, kap


def independent_subset(gram, vecs):
    """Greedy independent subset (w.r.t. the ambient coordinates)."""
    out = []
    M = None
    r = 0
    for v in vecs:
        cand = out + [v]
        Mc = Matrix.hstack(*cand)
        rc = Mc.rank()
        if rc > r:
            out, r = cand, rc
    return out


if __name__ == "__main__":
    pass
