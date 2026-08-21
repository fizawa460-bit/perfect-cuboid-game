#!/usr/bin/env python3
"""Exact finite-field regression for Stage29-02e.

No external packages are required.  For each listed odd prime, this script:
  1. enumerates F_p-points of the three singular coordinate-sign K3 models;
  2. detects rational singular points by Jacobian rank;
  3. adds p for every rational A1 exceptional curve to obtain the smooth K3 count;
  4. subtracts 1+p^2 to obtain the H^2 trace;
  5. compares with the candidate modular/Tate trace formulas.

The script is a finite-prime exact regression oracle, not by itself a proof that
any two global l-adic representations are isomorphic.
"""

from itertools import product

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def roots_table(p):
    table = {x: [] for x in range(p)}
    for y in range(p):
        table[(y * y) % p].append(y)
    return table


def normalize_projective(v, p):
    for x in v:
        x %= p
        if x:
            inv = pow(x, -1, p)
            return tuple((y * inv) % p for y in v)
    return None


def rank_mod_p(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    nrow = len(a)
    ncol = len(a[0]) if nrow else 0
    r = 0
    for c in range(ncol):
        pivot = next((i for i in range(r, nrow) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(nrow):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [(a[i][j] - f * a[r][j]) % p for j in range(ncol)]
        r += 1
        if r == nrow:
            break
    return r


def points_kc(p):
    # coords (a1,a2,a3,b1,b2,b3)
    # a1^2+a2^2=b3^2, a1^2+a3^2=b2^2, a2^2+a3^2=b1^2
    rt = roots_table(p)
    pts = set()
    for a1, a2, a3 in product(range(p), repeat=3):
        for b3 in rt[(a1*a1 + a2*a2) % p]:
            for b2 in rt[(a1*a1 + a3*a3) % p]:
                for b1 in rt[(a2*a2 + a3*a3) % p]:
                    q = normalize_projective((a1,a2,a3,b1,b2,b3), p)
                    if q is not None:
                        pts.add(q)
    return pts


def jac_kc(v, p):
    a1,a2,a3,b1,b2,b3 = v
    return [
        [2*a1, 2*a2, 0, 0, 0, -2*b3],
        [2*a1, 0, 2*a3, 0, -2*b2, 0],
        [0, 2*a2, 2*a3, -2*b1, 0, 0],
    ]


def points_kb(p):
    # representative K_b1; coords (a1,a2,a3,b2,b3,c)
    # equivalent equations:
    # a2^2+b2^2=c^2, a3^2+b3^2=c^2, a1^2+a2^2+a3^2=c^2
    rt = roots_table(p)
    pts = set()
    for a1, a2, a3 in product(range(p), repeat=3):
        for b2 in rt[(a1*a1 + a3*a3) % p]:
            for b3 in rt[(a1*a1 + a2*a2) % p]:
                for c in rt[(a1*a1 + a2*a2 + a3*a3) % p]:
                    q = normalize_projective((a1,a2,a3,b2,b3,c), p)
                    if q is not None:
                        pts.add(q)
    return pts


def jac_kb(v, p):
    a1,a2,a3,b2,b3,c = v
    return [
        [0, 2*a2, 0, 2*b2, 0, -2*c],
        [0, 0, 2*a3, 0, 2*b3, -2*c],
        [2*a1, 2*a2, 2*a3, 0, 0, -2*c],
    ]


def points_ka(p):
    # representative K_a1; coords (a2,a3,b1,b2,b3,c)
    # a2^2+a3^2=b1^2, a2^2+b2^2=c^2, a3^2+b3^2=c^2
    rt = roots_table(p)
    pts = set()
    for a2, a3, c in product(range(p), repeat=3):
        for b1 in rt[(a2*a2 + a3*a3) % p]:
            for b2 in rt[(c*c - a2*a2) % p]:
                for b3 in rt[(c*c - a3*a3) % p]:
                    q = normalize_projective((a2,a3,b1,b2,b3,c), p)
                    if q is not None:
                        pts.add(q)
    return pts


def jac_ka(v, p):
    a2,a3,b1,b2,b3,c = v
    return [
        [2*a2, 2*a3, -2*b1, 0, 0, 0],
        [2*a2, 0, 0, 2*b2, 0, -2*c],
        [0, 2*a3, 0, 0, 2*b3, -2*c],
    ]


def singular_model_count(point_fn, jac_fn, p):
    pts = point_fn(p)
    singular = sum(rank_mod_p(jac_fn(v, p), p) < 3 for v in pts)
    return len(pts), singular


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1)//2, p)
    return -1 if r == p - 1 else r


def chi_m1(p): return legendre(-1, p)
def chi_m2(p): return legendre(-2, p)
def chi_2(p): return legendre(2, p)


def ap_h16(p):
    # CM by Q(i): choose the odd coordinate x in p=x^2+y^2.
    if p % 4 == 3:
        return 0
    for x in range(1, int(p**0.5) + 1):
        y2 = p - x*x
        y = int(y2**0.5)
        if y*y == y2:
            if x % 2 == 1:
                return 2*(x*x - y*y)
            if y % 2 == 1:
                return 2*(y*y - x*x)
    raise AssertionError(("no Q(i) CM representation", p))


def ap_h8(p):
    # CM by Q(sqrt(-2)): choose odd x in p=x^2+2y^2.
    if p % 8 in (5, 7):
        return 0
    for x in range(1, int(p**0.5) + 1):
        rem = p - x*x
        if rem >= 0 and rem % 2 == 0:
            y2 = rem // 2
            y = int(y2**0.5)
            if y*y == y2 and x % 2 == 1:
                return 2*(x*x - 2*y*y)
    raise AssertionError(("no Q(sqrt(-2)) CM representation", p))


def ap_h32(p):
    # Horie--Yamauchi: V_h8 ~= chi_2 tensor V_h32.
    return chi_2(p) * ap_h8(p)


def predicted_kc(p):
    return ap_h32(p) + p*(16 + chi_m1(p) + 3*chi_2(p))


def predicted_kb(p):
    return ap_h16(p) + p*(15 + 5*chi_m1(p))


def predicted_ka(p):
    return ap_h8(p) + p*(13 + 4*chi_m1(p) + 2*chi_2(p) + chi_m2(p))


def check_one(label, point_fn, jac_fn, prediction, p):
    model_points, rational_nodes = singular_model_count(point_fn, jac_fn, p)
    # All singularities in these odd-characteristic checks are ordinary A1 nodes.
    smooth_points = model_points + p*rational_nodes
    trace = smooth_points - 1 - p*p
    expected = prediction(p)
    assert trace == expected, (label, p, trace, expected)
    return model_points, rational_nodes, trace


def main():
    print("p Kc_pts Kc_nodes Kc_trace Kb_pts Kb_nodes Kb_trace Ka_pts Ka_nodes Ka_trace")
    for p in PRIMES:
        kc = check_one("Kc", points_kc, jac_kc, predicted_kc, p)
        kb = check_one("Kb", points_kb, jac_kb, predicted_kb, p)
        ka = check_one("Ka", points_ka, jac_ka, predicted_ka, p)
        print(p, *kc, *kb, *ka)
    print("PASS: all exact finite-field trace identities matched")


if __name__ == "__main__":
    main()
