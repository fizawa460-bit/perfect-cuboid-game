"""Rebuild check (audit round 2): reconstruct g3_data_<tag>.json from the
bundled stage1 data (picard_base_rows / stage1_classes / stage1_G) with the
original exact construction, and assert every field -- including pair140 --
 matches the bundled copy. Closes the 'pair140 construction not bundled' gap
up to the stage1 bundle data itself (P2)."""
#!/usr/bin/env python3
"""G3 lattice setup: for the two P.F=40 maps, build
  W = (span{G,F})^perp  (rank 62, negative definite) with a verified Z-basis,
  Lambda_known (38 common curves), Lambda' = orthogonal complement in W,
  u = P perp to span{G,F};  check -b^2 = 296/3 for b = proj_{Lambda'} u.
All arithmetic exact. Saves g3_data_B{8,16}.json for the enumeration stage.
"""
import json
import os
import sys
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g3_common import load_all, pair, f_class
from sympy import Matrix, Rational, zeros
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_form


def egcd(a, b):
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def kernel_one_row(a):
    """Z-basis of {x in Z^n : a.x = 0} for a nonzero integer row a.
    Returns list of n-1 integer vectors (lists)."""
    n = len(a)
    assert any(v != 0 for v in a)
    perm = list(range(n))
    for i, v in enumerate(a):
        if v != 0:
            perm[0], perm[i] = perm[i], perm[0]
            break
    ap = [a[perm[i]] for i in range(n)]
    # prefix gcds and Bezout vectors
    d = []
    t = []
    for i in range(n):
        if i == 0:
            d.append(abs(ap[0]))
            t.append([1 if ap[0] > 0 else -1])
        else:
            g, p, q = egcd(d[i - 1], ap[i])
            d.append(g)
            t.append([p * t[i - 1][j] for j in range(i)] + [q])
    basis = []
    for i in range(1, n):
        v = [0] * n
        v[i] = d[i - 1] // d[i]
        c = ap[i] // d[i]
        for j in range(i):
            v[j] = -c * t[i - 1][j]
        # un-permute: original coordinate perm[i] gets v[i]
        w = [0] * n
        for i2 in range(n):
            w[perm[i2]] = v[i2]
        basis.append(w)
    return basis


def kernel_of_rows(rows, n):
    """Z-basis (list of column lists) of {x in Z^n : r.x = 0 for all r in rows}."""
    basis = None  # matrix with basis vectors as columns, as list of lists (n x k)
    for r in rows:
        if basis is None:
            cols = kernel_one_row(r)
            basis = [[cols[j][i] for j in range(len(cols))] for i in range(n)]
        else:
            k = len(basis[0])
            # functional values on current basis
            a = [sum(r[i] * basis[i][j] for i in range(n)) for j in range(k)]
            if all(v == 0 for v in a):
                continue
            ker = kernel_one_row(a)  # coords in current basis
            newbasis = []
            for i in range(n):
                row = []
                for kv in ker:
                    row.append(sum(basis[i][j] * kv[j] for j in range(k)))
                newbasis.append(row)
            basis = newbasis
    return basis  # list of n lists, each of length = final rank


def cols_to_matrix(basis_lists, n):
    k = len(basis_lists[0])
    return Matrix([[basis_lists[i][j] for j in range(k)] for i in range(n)])


def saturation_index(K):
    """[sat(col K) : col K] = product of SNF diagonal entries."""
    dm = DomainMatrix.from_Matrix(K)
    snf = smith_normal_form(dm).to_Matrix()
    prod = 1
    for i in range(min(snf.rows, snf.cols)):
        prod *= abs(int(snf[i, i]))
    return prod


def solve_coords(K, target):
    """Solve K z = target over Q; K full column rank. Returns z (Rational vector)."""
    KtK = K.T * K
    z = KtK.LUsolve(K.T * target)
    assert K * z == target
    return z


def main():
    gram, curves, vH, vP, vG, stage3 = load_all()
    curve_labels = sorted(curves)
    Cmat = Matrix.hstack(*[curves[l] for l in curve_labels])  # 64 x 140

    for B in ([8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23]):
        tag = f"B{B[0]}"
        F = f_class(gram, curves, vH, B)
        assert pair(gram, vP, F) == 40 and pair(gram, vG, F) == 4
        # A rows: pairings with G and F
        rowG = [int(v) for v in (gram * vG)]
        rowF = [int(v) for v in (gram * F)]
        basis = kernel_of_rows([rowG, rowF], 64)
        K = cols_to_matrix(basis, 64)
        assert K.shape == (64, 62), K.shape
        AK = Matrix([rowG, rowF]) * K
        assert all(v == 0 for v in AK), "kernel check failed"
        si = saturation_index(K)
        assert si == 1, f"W basis not saturated, index {si}"
        Qpos = -(K.T * gram * K)
        assert Qpos == Qpos.T
        detW = int(Qpos.det())
        # positive definiteness via exact LDL
        L, D = Qpos.LDLdecomposition()
        assert all(D[i, i] > 0 for i in range(62)), "Qpos not pos def"

        # common curves and their K-coords
        common = [l for l in curve_labels
                  if pair(gram, curves[l], vG) == 0 and pair(gram, curves[l], F) == 0]
        assert len(common) == 38
        ZL = Matrix.hstack(*[solve_coords(K, curves[l]) for l in common])
        assert all(v.q == 1 for v in ZL), "curve coords not integral"
        ZL = Matrix([[int(v) for v in row] for row in ZL.tolist()])

        # u = P - alpha G - beta F with u.G = u.F = 0
        GF = Matrix([[pair(gram, vG, vG), pair(gram, vG, F)],
                     [pair(gram, F, vG), pair(gram, F, F)]])
        ab = GF.LUsolve(Matrix([pair(gram, vP, vG), pair(gram, vP, F)]))
        u = vP - ab[0] * vG - ab[1] * F
        assert pair(gram, u, vG) == 0 and pair(gram, u, F) == 0
        assert pair(gram, u, u) == -384
        bu = solve_coords(K, u)  # rational coords

        # kappa over Lambda_known in K coords (form = -Qpos in original pairing)
        GL = ZL.T * Qpos * ZL  # positive Gram of Lambda_known in -form
        rhs = ZL.T * Qpos * bu
        kap_known = rhs.T * GL.LUsolve(rhs)
        kap_known = Rational(kap_known[0])
        assert kap_known == Rational(856, 3), kap_known

        # Lambda' : kernel of pairing map z -> ZL^T Qpos z  (38 x 62)
        Pi = (ZL.T * Qpos)
        rows = [[int(Pi[i, j]) for j in range(62)] for i in range(38)]
        basis_p = kernel_of_rows(rows, 62)
        Zp = cols_to_matrix(basis_p, 62)
        assert Zp.shape == (62, 24), Zp.shape
        assert all(v == 0 for v in Pi * Zp)
        si_p = saturation_index(Zp)
        assert si_p == 1, f"Lambda' basis not saturated in Z^62, index {si_p}"
        Gp = Zp.T * Qpos * Zp
        rhsp = Zp.T * Qpos * bu
        b_sq = Rational((rhsp.T * Gp.LUsolve(rhsp))[0])  # = -b^2
        assert b_sq == Rational(296, 3), b_sq
        assert kap_known + b_sq == 384

        # linear forms on z (K coords of v = K z)
        hvec = [int(v) for v in (K.T * gram * vH)]     # H.v
        pvec = [int(v) for v in (K.T * gram * vP)]     # P.v
        pair140 = Cmat.T * gram * K                    # (140 x 62): pair(v, C_label)
        pair140 = [[int(pair140[i, j]) for j in range(62)] for i in range(140)]

        data = {
            "B": B,
            "K": [[int(v) for v in row] for row in K.tolist()],
            "Qpos": [[int(v) for v in row] for row in Qpos.tolist()],
            "detW": detW,
            "common_labels": common,
            "ZL": [[int(v) for v in row] for row in ZL.tolist()],
            "bu": [str(v) for v in bu],
            "Zp": [[int(v) for v in row] for row in Zp.tolist()],
            "Gp": [[int(v) for v in row] for row in Gp.tolist()],
            "rhsp": [str(v) for v in rhsp],
            "hvec": hvec,
            "pvec": pvec,
            "pair140": pair140,
            "curve_labels": curve_labels,
            "kappa_known": str(kap_known),
            "b_sq": str(b_sq),
        }
        ref_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                f"g3_data_{tag}.json")
        ref = json.load(open(ref_path))
        for key, val in data.items():
            assert ref[key] == val, f"{tag}: field {key} differs from bundled g3_data"
        print(f"{tag}: rebuilt from stage1 bundle data; all fields match bundled g3_data (detW={detW}, kappa_known={kap_known}, -b^2={b_sq})")


if __name__ == "__main__":
    main()
