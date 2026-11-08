#!/usr/bin/env python3
"""Exact construction of local Jacobian Kummer generators for C29."""

import json
from pathlib import Path

from flint import fmpz_poly, nmod_mat, nmod_poly


PRECISION = 9
MODULUS = 2 ** (PRECISION // 3)
R7 = [0, 1, 7]
R28 = [0, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 20, 21, 22, 24, 28]


def coefficients(mask):
    return [(mask >> i) & 1 for i in range(mask.bit_length())]


def bitmask(poly):
    return sum((int(c) % 2) << i for i, c in enumerate(poly))


def binary_poly(mask):
    return nmod_poly(coefficients(mask), 2)


def v2(n):
    return (n & -n).bit_length() - 1


def irreducible(modulus, degree):
    x = nmod_poly([0, 1], 2)
    base = x % modulus
    power = base
    for i in range(1, degree + 1):
        power = power.pow_mod(2, modulus)
        if i <= degree // 2 and (power - base).gcd(modulus) != 1:
            return False
    return power == base


class Elt:
    """Triple of unramified coefficients in the basis 1, pi, pi^2."""

    __slots__ = ("ring", "parts")

    def __init__(self, ring, parts):
        self.ring = ring
        self.parts = parts

    def __add__(self, other):
        if isinstance(other, int):
            other = self.ring.constant(other)
        return Elt(self.ring, tuple(a + b for a, b in zip(self.parts, other.parts)))

    __radd__ = __add__

    def __neg__(self):
        return Elt(self.ring, tuple(-a for a in self.parts))

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if isinstance(other, int):
            return Elt(self.ring, tuple(a * other for a in self.parts))
        a, b, c = self.parts
        d, e, f = other.parts
        h = self.ring.modulus
        return Elt(self.ring, (
            (a*d + 2*(b*f + c*e)) % h,
            (a*e + b*d + 2*c*f) % h,
            (a*f + b*e + c*d) % h,
        ))

    __rmul__ = __mul__

    def __eq__(self, other):
        if isinstance(other, int):
            other = self.ring.constant(other)
        return self.parts == other.parts

    def __pow__(self, exponent):
        result = self.ring.one
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent >>= 1
        return result

    def valuation(self):
        vals = [3*v2(int(c))+i for i, a in enumerate(self.parts) for c in a if c]
        return min(vals, default=PRECISION)

    def digit(self, level):
        assert self.valuation() >= level
        k, i = divmod(level, 3)
        return sum(((int(c) >> k) & 1) << j for j, c in enumerate(self.parts[i]))

    def dump(self):
        return [[int(c) for c in a] for a in self.parts]


class LocalRing:
    def __init__(self, mask):
        self.h = binary_poly(mask)
        self.degree = self.h.degree()
        assert irreducible(self.h, self.degree)
        self.modulus = nmod_poly(coefficients(mask), MODULUS)
        self.zero = self.constant(0)
        self.one = self.constant(1)
        self.pi = Elt(self, (self.zero.parts[0], self.one.parts[0], self.zero.parts[0]))
        self.pi_powers = [self.pi**i for i in range(PRECISION)]
        assert self.pi**3 == 2
        self.basis_inverses = None

    def constant(self, n):
        zero = nmod_poly([], MODULUS)
        return Elt(self, (nmod_poly([n], MODULUS), zero, zero))

    def lift(self, mask):
        return Elt(self, (nmod_poly(coefficients(mask), MODULUS), self.zero.parts[0], self.zero.parts[0]))

    def load(self, parts):
        assert len(parts) == 3
        assert all(len(a) <= self.degree and all(0 <= c < MODULUS for c in a) for a in parts)
        return Elt(self, tuple(nmod_poly(a, MODULUS) for a in parts))

    def fpow(self, mask, power):
        return bitmask(binary_poly(mask).pow_mod(power, self.h))

    def sqrt_residue(self, mask):
        return self.fpow(mask, 2**(self.degree - 1))

    def inverse(self, value):
        a = bitmask(value.parts[0])
        assert a
        x = self.lift(self.fpow(a, 2**self.degree - 2))
        for _ in range((PRECISION - 1).bit_length()):
            x = x * (2 - value*x)
        assert x*value == 1
        return x

    def scalar_polynomial(self, coeffs):
        return [self.constant(c) for c in coeffs]

    def scaled_polynomial(self, shifted, scale):
        result = []
        for i, c in enumerate(shifted):
            c = int(c)
            if not c:
                result.append(self.zero)
                continue
            v = v2(c)
            power = 3*v + 2*i - scale
            assert power >= 0
            result.append(self.zero if power >= PRECISION else (c >> v)*self.pi_powers[power])
        return result

    def hensel(self, coeffs, target, residue):
        value = self.lift(residue)
        derivative = [i*c for i, c in enumerate(coeffs) if i]
        assert (evaluate(coeffs, value)-target).valuation() >= 1
        for _ in range((PRECISION - 1).bit_length()):
            error = evaluate(coeffs, value)-target
            if error == 0:
                break
            value = value - error*self.inverse(evaluate(derivative, value))
        assert evaluate(coeffs, value) == target
        assert evaluate(derivative, value).valuation() == 0
        return value

    def conjugates(self):
        h = self.scalar_polynomial([int(c) for c in self.h])
        z = bitmask(nmod_poly([0, 1], 2) % self.h)
        return [self.hensel(h, self.zero, self.fpow(z, 2**i)) for i in range(self.degree)]

    def coordinate(self, value):
        residue = value.digit(0)
        assert residue != 0
        root = self.lift(self.sqrt_residue(residue))
        u = value * self.inverse(root)**2
        if self.basis_inverses is None:
            self.basis_inverses = {
                i: [self.inverse(self.one+self.pi_powers[i]*self.lift(1 << j))
                    for j in range(self.degree)]
                for i in (1, 3, 5)
            }
        code = 0
        for level in range(1, 6):
            c = (u-self.one).digit(level)
            if level % 2:
                code |= c << ((level//2)*self.degree)
                for j in range(self.degree):
                    if (c >> j) & 1:
                        u = u*self.basis_inverses[level][j]
            elif c:
                correction = self.one + self.pi_powers[level//2]*self.lift(self.sqrt_residue(c))
                u = u*self.inverse(correction)**2
            assert (u-self.one).valuation() >= level+1
        c = (u-self.one).digit(6)
        trace = 0
        for _ in range(self.degree):
            trace ^= c
            c = self.fpow(c, 2)
        assert trace in (0, 1)
        return code | (trace << (3*self.degree))

    def square_root_mod_pi7(self, value):
        root = self.lift(self.sqrt_residue(value.digit(0)))
        u = value*self.inverse(root)**2
        for i in (2, 4):
            c = (u-self.one).digit(i)
            w = self.one+self.pi_powers[i//2]*self.lift(self.sqrt_residue(c))
            root *= w
            u *= self.inverse(w)**2
        c = (u-self.one).digit(6)
        r = next(r for r in range(2**self.degree) if self.fpow(r, 2)^r == c)
        root *= self.one + self.pi_powers[3]*self.lift(r)
        assert (root**2-value).valuation() >= 7
        return root


def evaluate(poly, x):
    value = x.ring.zero
    for c in reversed(poly):
        value = value*x + c
    return value


def conjugate(x, z):
    out = x.ring.zero
    for i, a in enumerate(x.parts):
        out += evaluate([int(c) for c in a], z)*x.ring.pi_powers[i]
    return out


def product_polynomial(factors):
    ring = factors[0][0].ring
    q = [ring.one]
    for factor in factors:
        product = [ring.zero]*(len(q)+len(factor)-1)
        for i, a in enumerate(q):
            for j, b in enumerate(factor):
                product[i+j] += a*b
        q = product
    assert all(a.degree() <= 0 for c in q for a in c.parts)
    return [[int(a[0]) for a in c.parts] for c in q]


def norm_polynomial(x, conjugates):
    return product_polynomial([[-conjugate(x, z), x.ring.one] for z in conjugates])


def evaluate_cubic_norm(q, theta):
    ring = theta.ring
    d = len(q)-1
    terms = [ring.zero for _ in range(3)]
    power = ring.one
    for j, c in enumerate(q):
        for k, ck in enumerate(c):
            if ck:
                terms[(2*d+j+k) % 3] += ck*ring.pi_powers[k]*power
        power *= theta
    a, b, c = terms
    norm = a**3+b**3+c**3-3*a*b*c
    assert norm == (a+b+c)*((a-c)**2-(a-c)*(b-c)+(b-c)**2)
    return (-1)**d*norm


class Span:
    def __init__(self):
        self.rows = {}

    def add(self, vector):
        while vector:
            pivot = vector.bit_length()-1
            if pivot not in self.rows:
                self.rows[pivot] = vector
                return pivot
            vector ^= self.rows[pivot]
        return None


def source_data(root):
    j = json.loads((root / "curve_C29.json").read_text())
    t = fmpz_poly([0, 1])
    f = fmpz_poly(j["F_ascending"])
    a = fmpz_poly(j["A_star_ascending"])
    b = fmpz_poly(j["B_star_ascending"])
    assert f == a*a+t*b*b and f.degree() == 105 and b.degree() == 52
    assert f[105] == b[52] == 1 and f(1) == f(-1) == 2**70
    return f(t-1), b(t-1)


def local_roots(f_shift):
    masks = [sum(1 << i for i in exponents) for exponents in (R7, R28)]
    data = []
    for mask in masks:
        ring = LocalRing(mask)
        d = ring.degree
        order = 2**d-1
        z = 2
        if order % 3 == 0:
            order //= 3
            assert ring.fpow(z, order) == 1
        w = ring.fpow(z, pow(3, -1, order))
        assert ring.fpow(w, 3) == z
        theta = ring.hensel(ring.scaled_polynomial(f_shift, 210), ring.zero, ring.fpow(w, 2))
        assert theta.digit(0) == ring.fpow(w, 2)
        data.append(theta)
    return data


def known_rows(b_shift, roots):
    values = []
    for theta in roots:
        ring = theta.ring
        h = evaluate(ring.scaled_polynomial(b_shift, 104), theta)
        dplus = ring.pi-theta
        dminus = -theta
        values.append([ring.coordinate(x) for x in (h, dplus, dminus)])
    rows = [[values[0][i], values[1][i]] for i in range(3)]
    assert [row[0] % 128 for row in rows] == [0x3C, 0x77, 0]
    return rows


def combine(coords):
    return coords[0] | (coords[1] << 22)


def check_scaled_residual(f_shift):
    ring = LocalRing(3)
    r7, r28 = [binary_poly(sum(1 << i for i in e)) for e in (R7, R28)]
    h0 = nmod_poly([a.digit(0) for a in ring.scaled_polynomial(f_shift, 210)], 2)
    assert h0.degree() == 105
    assert h0 == (r7*r28)(nmod_poly([0, 0, 0, 1], 2))
    assert h0.gcd(h0.derivative()) == 1


def check_basis(root, f_shift, b_shift, roots):
    data = json.loads((root / "local_basis.json").read_text())
    assert data["precision"] == PRECISION
    assert data["roots_scaled"] == [theta.dump() for theta in roots]
    known = known_rows(b_shift, roots)
    assert known == data["known_rows"]
    span = Span()
    vectors = [combine(row) for row in known]
    for v in vectors:
        assert span.add(v) is not None
    points = 0
    critical = 0
    rings = {}
    for witness in data["accepted"]:
        mask = witness["unramified_mask"]
        if mask not in rings:
            ring = LocalRing(mask)
            h = ring.scaled_polynomial(f_shift, 210)
            deriv = [i*c for i,c in enumerate(h) if i]
            rings[mask] = ring, h, deriv, ring.conjugates()
        ring, h, deriv, conjugates = rings[mask]
        x = ring.load(witness["X"])
        value = evaluate(h, x)
        assert value.valuation() == 0 and ring.coordinate(value) == 0
        if "Y" in witness:
            y = ring.load(witness["Y"])
            assert evaluate(deriv, x).valuation() == 0
            assert y**2 == value
        else:
            assert witness["square_test"]
            assert evaluate(deriv, x).valuation() > 0
            y = ring.square_root_mod_pi7(value)
            assert (y**2-value).valuation() >= 7
            critical += 1
        assert y.valuation() == 0
        q = norm_polynomial(x, conjugates)
        assert q == witness["norm_poly"]
        evaluated = [evaluate_cubic_norm(q, theta) for theta in roots]
        assert all(a.valuation() == 0 for a in evaluated)
        coords = [a.ring.coordinate(a) for a in evaluated]
        assert coords == witness["coordinates"]
        v = combine(coords)
        pivot = span.add(v)
        assert pivot is not None and pivot == witness["pivot"]
        vectors.append(v)
        points += 1
    assert points == 50 and critical == 5
    assert len(span.rows) == data["rank"] == 53
    return span, vectors


def membership_conditions(span, vectors):
    width = 107
    pivots = sorted(span.rows)
    minor = nmod_mat([[(v >> j) & 1 for j in pivots] for v in vectors], 2)
    assert minor.det() == 1
    equations = []
    for j in range(width):
        if j in span.rows:
            continue
        functional = 1 << j
        for pivot in pivots:
            if (span.rows[pivot] & functional).bit_count() % 2:
                functional ^= 1 << pivot
        assert all((v & functional).bit_count() % 2 == 0 for v in vectors)
        equations.append(functional)
    assert len(equations) == width-53
    dual = nmod_mat([[(v >> j) & 1 for j in range(width)] for v in equations], 2)
    assert dual.rank() == len(equations)
    return {
        "unit_widths_K21_K84": [22, 85],
        "basis": [hex(v) for v in vectors],
        "pivot_columns_zero_based": pivots,
        "minor_determinant_mod_2": int(minor.det()),
        "parity_equations": [hex(v) for v in equations],
        "membership": "Both valuations even, and parity(v & equation) = 0 for every equation.",
    }


def main():
    root = Path(__file__).resolve().parent
    f_shift, b_shift = source_data(root)
    check_scaled_residual(f_shift)
    roots = local_roots(f_shift)
    span, vectors = check_basis(root, f_shift, b_shift, roots)
    certificate = membership_conditions(span, vectors)
    (root / "kummer2_membership.json").write_text(json.dumps(certificate, indent=2)+"\n")
    print("scaled F integral and squarefree modulo pi; both local roots verified modulo pi^9")
    print("53 vectors: 3 known, 45 ordinary disks, 5 derivative-zero disks")
    print("50 local points, square roots, norms, unit squareclasses and pivots verified")
    print("rank 53, 53-by-53 minor determinant mod 2 = 1")
    print("107 unit coordinates, 54 independent membership equations, both valuations even")


if __name__ == "__main__":
    main()
