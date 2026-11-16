# Reduction of f(x) = x((2+i)P) on y^2 = x^3 - x at the two primes above 5 (exact, F_5 arithmetic).
# f = ((3-4i)x^5 + (10+20i)x^3 - 25x) / (25x^4 - (10+20i)x^2 - (3-4i))   (ANSWER-14, par. 3.2)
P = 5
def trim(a):
    while a and a[-1] % P == 0: a.pop()
    return a
def pmod(a): return trim([c % P for c in a])
def sub(a, b):
    n = max(len(a), len(b)); return pmod([(a[k] if k < len(a) else 0) - (b[k] if k < len(b) else 0) for k in range(n)])
def scal(a, c): return pmod([c * x for x in a])
def divmod_(a, b):
    a = a[:]; q = [0] * max(len(a) - len(b) + 1, 0); inv = pow(b[-1], P - 2, P)
    while len(a) >= len(b) and a:
        c = a[-1] * inv % P; d = len(a) - len(b); q[d] = c
        for k, y in enumerate(b): a[k + d] = (a[k + d] - c * y) % P
        a = trim(a)
    return trim(q), a
def gcd(a, b):
    while b: a, b = b, divmod_(a, b)[1]
    return scal(a, pow(a[-1], P - 2, P)) if a else a
def der(a): return pmod([k * a[k] for k in range(1, len(a))])
def gauss_div(z, w):            # exact division of Gaussian integers z / w (asserts exactness)
    (a, b), (c, d) = z, w; n = c * c + d * d; re, im = a * c + b * d, b * c - a * d
    assert re % n == 0 and im % n == 0; return (re // n, im // n)
num = [(0, 0), (-25, 0), (0, 0), (10, 20), (0, 0), (3, -4)]      # low degree first, Gaussian integers
den = [(-3, 4), (0, 0), (-10, -20), (0, 0), (25, 0)]
for name, ival, pr in (("(2+i)", 3, (2, 1)), ("(2-i)", 2, (2, -1))):   # i = 3 mod (2+i), i = 2 mod (2-i)
    N, D = num, den
    while all((a + b * ival) % P == 0 for a, b in N + D):     # remove the common factor of the prime
        N = [gauss_div(z, pr) for z in N]; D = [gauss_div(z, pr) for z in D]
    n = pmod([a + b * ival for a, b in N]); d = pmod([a + b * ival for a, b in D])
    print("prime", name, ": numerator", n, " denominator", d, " (coefficients mod 5, low degree first)")
    if len(der(n)) == 0 and len(d) == 1:
        print("   reduction is purely inseparable: f = %d * x^5" % (n[-1] * pow(d[0], P - 2, P) % P)); continue
    # fibre types over the six points of B mod this prime: 0, inf, 1, -1, i, -i
    for label, beta in (("0", 0), ("inf", None), ("1", 1), ("-1", P - 1), ("i", ival), ("-i", (-ival) % P)):
        F = d if beta is None else sub(n, scal(d, beta))
        g = gcd(F, der(F)); simple = (len(F) - 1) - 2 * (len(g) - 1); atinf = 5 - (len(F) - 1)
        ok = len(gcd(g, der(g))) <= 1
        print("   over %3s: degree of F %d, double points %d, simple points %d, multiplicity at infinity %d, all multiplicities <= 2: %s"
              % (label, len(F) - 1, len(g) - 1, simple, atinf, ok))
