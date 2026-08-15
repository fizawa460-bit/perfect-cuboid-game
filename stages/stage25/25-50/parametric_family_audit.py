#!/usr/bin/env python3
from math import gcd


def family(m, n):
    A = 16*m*m*n*n*(m**4 - 9*n**4)
    B = (m**4 - 10*m*m*n*n + 9*n**4) * (m**4 + 2*m*m*n*n + 9*n**4)
    C = 4*m*n*(m*m + 3*n*n)*(m**4 - 10*m*m*n*n + 9*n**4)
    DAC = 4*m*n*(m*m + 3*n*n)*(m**4 - 2*m*m*n*n + 9*n**4)
    DBC = (m**4 - n**4)*(m**4 - 81*n**4)
    D = m**8 + 46*m**4*n**4 + 81*n**8
    return A, B, C, DAC, DBC, D


def missing_homogeneous(m, n):
    return (
        m**16 - 16*m**14*n**2 + 316*m**12*n**4 - 112*m**10*n**6
        - 3290*m**8*n**8 - 1008*m**6*n**10 + 25596*m**4*n**12
        - 11664*m**2*n**14 + 6561*n**16
    )


# Polynomial helpers, coefficients low degree first, over F_p.
def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    n = max(len(a), len(b))
    out = [0]*n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def mul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return trim(out)


def deriv(a, p):
    if len(a) <= 1:
        return [0]
    return trim([(i*a[i]) % p for i in range(1, len(a))])


# Q(u)=u^8+4u^7+u^6+3u^5+2u^3+u^2+u+1 mod 5.
p = 5
Q = [1, 1, 1, 2, 0, 3, 1, 4, 1]
Qp = deriv(Q, p)
S = [2, 1, 0, 2, 1, 2, 2]                       # 2u^6+2u^5+u^4+2u^3+u+2
T = [4, 4, 0, 4, 2, 2, 4, 1]                    # u^7-u^6+2u^5+2u^4-u^3-u-1
bezout = add(mul(S, Q, p), mul(T, Qp, p), p)
assert bezout == [1], bezout
assert Q[0] == 1

# Exact integer regression over many admissible reduced parameters.
seen = 0
for n in range(3, 61):
    for k in range(1, (n-1)//2 + 1):
        if 2*k >= n or gcd(k, n) != 1:
            continue
        m = 4*n - k
        assert gcd(m, n) == 1
        assert 7*n < 2*m < 8*n
        A, B, C, DAC, DBC, D = family(m, n)
        assert 0 < B < C < A
        assert A*A + C*C == DAC*DAC
        assert B*B + C*C == DBC*DBC
        assert A*A + B*B + C*C == D*D
        assert A*A + B*B == missing_homogeneous(m, n)
        g = gcd(gcd(A, B), C)
        assert DAC % g == 0 and DBC % g == 0 and D % g == 0
        seen += 1

assert seen > 200

# Height constant used by the counting proof.
# If m,n<=T then D <= (1+46+81)T^8 = 128 T^8.
assert 1 + 46 + 81 == 128

print('MESKHISHVILI_HOMOGENEOUS_IDENTITIES_REGRESSION=PASS')
print(f'ADMISSIBLE_REDUCED_SAMPLE_COUNT={seen}')
print('PHYSICAL_CONE_ORDER_B_LT_C_LT_A=PASS')
print('PRIMITIVE_DIAGONAL_DIVISIBILITY_REGRESSION=PASS')
print('MISSING_FACE_HYPERELLIPTIC_POLYNOMIAL=PASS')
print('Q_MOD5_BEZOUT_SQUAREFREE_CERTIFICATE=PASS')
print('HYPERELLIPTIC_DEGREE=16')
print('HYPERELLIPTIC_GENUS=7')
print('HEIGHT_CONSTANT_128=PASS')
print('PARAMETER_FIBER_BOUND_DEGREE=8')
print('STAGE25_50_PARAMETRIC_FAMILY_AUDIT=PASS')
