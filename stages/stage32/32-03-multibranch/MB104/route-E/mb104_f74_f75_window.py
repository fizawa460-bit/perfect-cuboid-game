#!/usr/bin/env python3
"""MB104 F74 Gaussian sieve and F75 Hermitian necessary-class enumeration.

Input: fixed F74/F75 numerical windows from PR #1850 head
33ef9d164684a655b97b5cb5e4d0d47a142e9938.
This is NOT an existence search or a proof of F74's conditional geometric premises.
Requires: Python >=3.9; standard library only.
"""
from math import isqrt


def norm(z):
    a, b = z
    return a*a + b*b


def div_round(a, b):
    # Round Gaussian quotient a/b to nearest Gaussian integer.
    x, y = a
    u, v = b
    n = norm(b)
    return ((2*(x*u+y*v)+n)//(2*n), (2*(y*u-x*v)+n)//(2*n))


def gaussian_gcd_norm(a, b):
    while b != (0, 0):
        q = div_round(a, b)
        x, y = a
        u, v = b
        p, r = q
        a, b = b, (x-p*u+r*v, y-p*v-r*u)
    return norm(a)


def primitive_counts(max_total=4):
    elements = [(x, y) for x in range(-2, 3) for y in range(-2, 3)
                if 1 <= x*x+y*y <= max_total]
    out = {}
    for total in range(2, max_total + 1):
        pairs = [(a, b) for a in elements for b in elements
                 if norm(a)+norm(b) == total and gaussian_gcd_norm(a, b) == 1]
        out[total] = len(pairs)
    return out


# Label, h, g(E), r0=g(Y/T), k, F75 bound for d, F75 bound for gamma.
ROWS = [
    ("h2_g0_k4", 2, 0, 0, 4, 42, 7),
    ("h2_g1_k4", 2, 1, 1, 4, 46, 9),
    ("h2_g0_k8", 2, 0, 0, 8, 27, 13),
    ("h2_g1_k8", 2, 1, 1, 8, 31, 17),
    ("h4_g0_k4", 4, 0, 0, 4, 88, 7),
    ("h4_g1_r0_k4", 4, 1, 0, 4, 92, 7),
    ("h4_g1_r1_k4", 4, 1, 1, 4, 92, 9),
    ("h4_g0_k8", 4, 0, 0, 8, 58, 13),
    ("h4_g1_r0_k8", 4, 1, 0, 8, 60, 13),
    ("h4_g1_r1_k8", 4, 1, 1, 8, 62, 17),
]


def enumerate_row(row):
    name, h, g, r0, k, dmax, gammamax = row
    # gamma>=2 => both projections Y->E have degree >=2.
    Amax = (dmax*k)//(4*h)
    nbidegrees = nclasses = nclasses_parity = npassports = 0
    for a1 in range(2, Amax-1):
        for a2 in range(2, Amax-a1+1):
            if 4*h*(a1+a2) > k*dmax:
                continue
            nbidegrees += 1
            # NS(A) = Herm_2(Z[i]), H_D=[[a2,c],[conj(c),a1]].
            # D^2/2 = det(H_D) = a1*a2 - |c|^2 >=1.
            for x in range(-isqrt(a1*a2), isqrt(a1*a2)+1):
                for y in range(-isqrt(a1*a2), isqrt(a1*a2)+1):
                    determinant = a1*a2 - x*x - y*y
                    if determinant < 1:
                        continue
                    nclasses += 1
                    # New k=8 sieve: free diagonal 2-torsion translation on Y.
                    # It forces odd gamma, even total delta and even det(H_D).
                    if k == 8 and determinant % 2:
                        continue
                    nclasses_parity += 1
                    for gamma in range(2, min(gammamax, determinant+1)+1):
                        if k == 8 and gamma % 2 == 0:
                            continue
                        F = 2*gamma-2-k*(r0-1)
                        if 0 <= F <= 4*k:
                            npassports += 1
    return (name, Amax, nbidegrees, nclasses,
            nclasses_parity, npassports)


def main():
    counts = primitive_counts()
    if counts != {2: 16, 3: 32, 4: 0}:
        raise RuntimeError(f"unexpected Gaussian primitive counts: {counts}")
    print("F74 primitive Gaussian (alpha,beta) ordered counts by Nalpha+Nbeta:")
    for A, count in sorted(counts.items()):
        print(f"  A={A}: {count}")
    print("F74 MB101 conditional: I=8; A=2+k*(g+1)/8")
    print("  (g,k)=(0,4): A=5/2, impossible")
    print("  (g,k)=(0,8): A=3, graph degree-2, reflection obstruction")
    print("  (g,k)=(1,4): A=3, graph degree-2, reflection obstruction")
    print("  (g,k)=(1,8): A=4, no primitive Gaussian pair")
    print("\nF75 Hermitian necessary classes, labelled by ordered a1,a2,c:")
    print("row | max(a1+a2) | bidegrees | NS | NS after k8 parity | (NS,gamma) passports")
    result = [enumerate_row(row) for row in ROWS]
    for r in result:
        print(" | ".join(map(str, r)))
    expected = {
        'h2_g0_k4': (21,171,26191,26191,149316),
        'h2_g1_k4': (23,210,37794,37794,284216),
        'h2_g0_k8': (27,300,71844,35726,200452),
        'h2_g1_k8': (31,406,124862,62223,461920),
        'h4_g0_k4': (22,190,31550,31550,180846),
        'h4_g1_r0_k4': (23,210,37794,37794,217102),
        'h4_g1_r1_k4': (23,210,37794,37794,284216),
        'h4_g0_k8': (29,351,95679,47625,269030),
        'h4_g1_r0_k8': (30,378,109498,54523,309266),
        'h4_g1_r1_k8': (31,406,124862,62223,461920),
    }
    for row in result:
        if row[1:] != expected[row[0]]:
            raise RuntimeError('count mismatch '+repr(row))
    print("PASS: exact integer arithmetic and expected certificates match")

if __name__ == '__main__':
    main()
