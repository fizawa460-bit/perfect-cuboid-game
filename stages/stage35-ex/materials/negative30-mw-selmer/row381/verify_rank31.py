#!/usr/bin/env python3
"""Verify the 31-adic rank witness with iterative Cantor reduction."""
import json
from pathlib import Path
from random import Random
from functools import cache

from flint import fmpq, fmpq_poly, nmod_poly, nmod_mat

HERE = Path(__file__).resolve().parent
P = 31
R = P * P
GENUS = 52
N = 393648362324456806647414264130928641711553162973261279756877858799612593368832


def integers(f):
    return list(map(int, f))


def modp(f):
    return nmod_poly(integers(f), P)


def modr(f):
    return nmod_poly(integers(f), R)


def exact_div(a, b):
    q, r = divmod(a, b)
    assert not r
    return q


class Nonunit(Exception):
    pass


def inverse(a, u):
    d, b, _ = modp(a).xgcd(modp(u))
    if d != 1:
        raise Nonunit
    b = modr(b)
    b = (b * (2 - a*b)) % u
    assert (a*b) % u == 1
    return b


def negative(D):
    u, v = D
    return u, -v


def solve_mod_r(rows, rhs):
    n = len(rhs)
    A = [[z % R for z in row] + [b % R] for row,b in zip(rows,rhs)]
    assert len(A) == n and all(len(row) == n+1 for row in A)
    for j in range(n):
        k = next((i for i in range(j,n) if A[i][j] % P), None)
        if k is None:
            raise Nonunit
        A[j], A[k] = A[k], A[j]
        inv = pow(A[j][j], -1, R)
        A[j][j:] = [(z*inv)%R for z in A[j][j:]]
        for i in range(n):
            if i != j and A[i][j]:
                m = A[i][j]
                A[i][j:] = [(x-m*y)%R for x,y in zip(A[i][j:],A[j][j:])]
    x = [r[-1] for r in A]
    assert all((sum(a*b for a,b in zip(row,x))-z)%R==0 for row,z in zip(rows,rhs))
    return x


class Cantor:
    def __init__(self, F):
        self.F = nmod_poly(F, R)
        self.Fp = nmod_poly(F, P)
        assert self.Fp.gcd(self.Fp.derivative()) == 1
        self.steps = self.reductions = self.rejected = self.function_reductions = 0

    def check(self, D):
        u, v = D
        assert u.leading_coefficient() == 1 and v.degree() < u.degree() <= GENUS
        assert not (self.F - v*v) % u

    def add(self, D, E):
        u, v = D
        w, z = E
        if u.degree() == 0:
            return E
        if w.degree() == 0:
            return D
        if D == E:
            v += u * ((exact_div(self.F-v*v,u) * inverse(2*v,u)) % u)
        else:
            v += u * (((z-v) * inverse(u,w)) % w)
        u *= w
        assert not (self.F-v*v) % u
        if u.degree() > GENUS:
            try:
                u, v = self.iterative_reduce(u,v)
            except Nonunit:
                u, v = self.function_reduce(u,v)
        self.check((u,v))
        self.steps += 1
        return u, v

    def iterative_reduce(self,u,v):
        while u.degree() > GENUS:
            # A nilpotent leading coefficient of v can hide a pole at infinity
            # even when F-v^2 has a unit leading coefficient.
            if 2*v.degree() > self.F.degree() and int(v.leading_coefficient()) % P == 0:
                raise Nonunit
            q = exact_div(self.F-v*v,u)
            assert q.degree() < u.degree()
            leading = int(q.leading_coefficient())
            if leading % P == 0:
                raise Nonunit
            u = q * pow(leading,-1,R)
            v = (-v) % u
            self.reductions += 1
        return u,v

    def function_reduce(self,u,v):
        # Solve directly over Z/31^2 for a(x)-y*b(x) with exact pole m+g.
        m = u.degree()
        pole = m + GENUS
        Amax = pole//2
        Bmax = (pole - self.F.degree())//2
        x = nmod_poly([0,1],R)
        cols = [v]
        for _ in range(Bmax):
            cols.append(x*cols[-1] % u)
        if pole % 2 == 0:
            rows = [[int(c[i]) for c in cols] for i in range(Amax,m)]
            b = nmod_poly(solve_mod_r(rows,[1]+[0]*(m-Amax-1)),R)
        else:
            rows = [[int(c[i]) for c in cols[:-1]] for i in range(Amax+1,m)]
            rhs = [-int(cols[-1][i]) for i in range(Amax+1,m)]
            b = nmod_poly(solve_mod_r(rows,rhs)+[1],R)
        a = b*v % u
        assert a.degree()<=Amax and b.degree()<=Bmax
        f = a*a - self.F*b*b
        assert f.degree() == pole and int(f.leading_coefficient()) % P != 0
        q = exact_div(f,u)
        assert q.degree()==GENUS
        q *= pow(int(q.leading_coefficient()),-1,R)
        inverse(b,u)
        w = (-a*inverse(b,q)) % q
        self.function_reductions += 1
        return q,w

    def attempt(self, D, E):
        if D is None or E is None:
            return None
        try:
            return self.add(D,E)
        except Nonunit:
            self.rejected += 1
            return None

    def auxiliary(self):
        squares = {a*a % P for a in range(P)}
        pairs = []
        for b in range(P):
            for c in range(P):
                if (b*b-4*c) % P in squares:
                    continue
                u = nmod_poly([c,b,1],R)
                f = self.Fp % modp(u)
                if not f:
                    continue
                for y in range(P):
                    for x in range(P):
                        if ((x*x-c*y*y) % P, (2*x*y-b*y*y) % P) == (int(f[0]),int(f[1])):
                            v = nmod_poly([x,y],R)
                            v = (v+(self.F-v*v)*inverse(2*v,u)) % u
                            self.check((u,v))
                            pairs.append((u,v))
                            break
                    else:
                        continue
                    break
        assert len(pairs) == 226
        return pairs

    def anchors(self, seed, pool):
        # Eight anchors have pairwise disjoint quadratic supports.
        random = Random(seed)
        choices = random.sample(pool, 8*26)
        out = []
        for i in range(8):
            u, v = nmod_poly([1],R), nmod_poly([],R)
            for q, w in choices[26*i:26*i+26]:
                if random.randrange(2):
                    w = -w
                v += u * (((w-v)*inverse(u,q)) % q)
                u *= q
            self.check((u,v))
            assert modp(u).gcd(modp(u.derivative())) == 1
            assert modp(u).gcd(modp(v)) == 1
            out.append((u,v))
        return out

    def multiply(self, D, anchors):
        @cache
        def translation(i,j):
            return self.attempt(anchors[j], negative(anchors[i]))

        @cache
        def double_anchor(j):
            return self.attempt(anchors[j],anchors[j])

        @cache
        def correction(j,k,bit):
            if j == k:
                c = negative(anchors[j])
            else:
                d = double_anchor(j)
                c = None if d is None else self.attempt(anchors[k],negative(d))
            return self.attempt(c,D) if bit else c

        Q = anchors[0]
        current = 0
        indices = tuple(range(len(anchors)))
        for char in bin(N)[2:]:
            bit = int(char)
            chosen = None
            for j in (current,)+tuple(j for j in indices if j!=current):
                q = Q if j==current else self.attempt(Q,translation(current,j))
                r = self.attempt(q,q)
                if r is None:
                    continue
                for k in (j,)+tuple(k for k in indices if k!=j):
                    w = self.attempt(r,correction(j,k,bit))
                    if w is not None:
                        chosen = k,w
                        break
                if chosen is not None:
                    break
            if chosen is None:
                raise Nonunit
            current,Q = chosen
        # Induction shows Q=[N]D+anchors[current].
        return anchors[current],Q

    def log_digit(self, A, Q):
        u, v = A
        U, V = Q
        assert modp(U) == modp(u) and modp(V) == modp(v)
        diff = integers(U-u)
        assert all(c % P == 0 for c in diff)
        u0, v0 = modp(u),modp(v)
        d, reciprocal, _ = (2*v0).xgcd(u0)
        assert d == 1
        z = (-nmod_poly([c//P for c in diff],P)*reciprocal) % u0
        out = []
        for _ in range(GENUS):
            out.append(int(z[GENUS-1])*pow(N,-1,P) % P)
            z = (z*nmod_poly([0,1],P)) % u0
        return out


def rational_divisors():
    curve = json.loads((HERE/"curve_C29.json").read_text())
    F = curve["F_ascending"]
    QF = fmpq_poly(F)
    a = fmpq_poly(curve["A_star_ascending"])
    b = fmpq_poly(curve["B_star_ascending"])
    divisors = [("H", b, -a % b), ("D+",fmpq_poly([-1,1]),fmpq_poly([2**35])),
                ("D-",fmpq_poly([1,1]),fmpq_poly([2**35]))]
    extra = json.loads((HERE/"mw_divisors.json").read_text())
    for w in extra:
        if w["name"] == "D15b":
            continue
        divisors.append((w["name"],fmpq_poly(w["u"]),fmpq_poly([fmpq(c) for c in w["v"]])))
    assert [n for n,u,v in divisors] == ["H","D+","D-","D5a","D5b","D7","D14","D15a"]
    result = []
    for name,u,v in divisors:
        assert u.leading_coefficient() == 1 and v.degree() < u.degree() <= GENUS
        assert not (QF-v*v) % u and u.gcd(u.derivative()) == 1 and u.gcd(v) == 1
        reduced = tuple(nmod_poly([int(c.numerator)*pow(int(c.denominator),-1,R)%R for c in h],R)
                        for h in (u,v))
        result.append((name,reduced))
    return F,result


def rank_check():
    F,D = rational_divisors()
    assert F[:2] == [1,-7] and N % P == 13
    J = Cantor(F)
    pool = J.auxiliary()
    logs, seeds = [], []
    for i,(name,d) in enumerate(D):
        J.check(d)
        for retry in range(32):
            seed = 86291+113*i+retry
            anchors = J.anchors(seed,pool)
            try:
                a,q = J.multiply(d,anchors)
            except Nonunit:
                continue
            break
        else:
            raise AssertionError(f"all shifts failed for {name}")
        logs.append(J.log_digit(a,q))
        seeds.append(seed)
    old = json.loads((HERE/"row375_results.json").read_text())
    assert logs == old["log31_div31_digits"]
    M = nmod_mat([r[:10] for r in logs]+[[1,0]+[0]*8,[0,1]+[0]*8],P)
    assert M.det() == 6
    return {"divisors":[n for n,d in D],"seeds":seeds,
            "successful_additions":J.steps,"iterative_reductions":J.reductions,
            "rejected_chart_operations":J.rejected,"rational_function_reductions":J.function_reductions,"first_log_coordinates":logs,
            "augmented_minor_det_mod31":int(M.det())}


if __name__=="__main__":
    print(json.dumps(rank_check(),indent=2))
