#!/usr/bin/env python3
"""Exact first 31-adic log digits on the row370 genus-52 curve."""
from itertools import combinations
import json
from pathlib import Path
import random
from time import perf_counter

from flint import fmpz_poly, nmod_mat, nmod_poly

P = 31
P2 = P*P
GENUS = 52
N = 393648362324456806647414264130928641711553162973261279756877858799612593368832


def coeffs(f):
    return [int(c) for c in f]


def poly(f, modulus):
    return nmod_poly(coeffs(f), modulus)


def divide(a, b):
    q, r = divmod(a, b)
    assert not r
    return q


def divided_digit(f):
    return nmod_poly([exact_divide(int(c), P) for c in f], P)


def exact_divide(n, d):
    q, r = divmod(n, d)
    assert r == 0
    return q


class BadChart(Exception):
    pass


class Jacobian:
    def __init__(self, f):
        self.f = nmod_poly(f, P2)
        self.f0 = nmod_poly(f, P)
        self.one = nmod_poly([1], P2)
        self.zero = nmod_poly([], P2)
        self.x = nmod_poly([0, 1], P2)
        self.finite_crosschecks = 0

    def inverse(self, a, u):
        if u.degree() == 0:
            return self.zero
        d, s, _ = poly(a, P).xgcd(poly(u, P))
        if d != 1:
            raise BadChart("nonunit polynomial inverse")
        t = poly(s, P2)
        inv = (t*(2-(a*t % u))) % u
        assert (a*inv) % u == 1
        return inv

    def solve(self, rows, rhs):
        if not rows:
            return []
        a = nmod_mat(rows, P)
        if a.det() == 0:
            raise BadChart("singular reduction system")
        inv = a.inv()
        b = nmod_mat([[x] for x in rhs], P)
        x0 = inv*b
        a2 = nmod_mat(rows, P2)
        b2 = nmod_mat([[x] for x in rhs], P2)
        residual = b2-a2*nmod_mat([[int(x)] for x in x0.entries()], P2)
        x1 = inv*nmod_mat([[exact_divide(int(x), P)] for x in residual.entries()], P)
        result = [int(x)+P*int(y) for x, y in zip(x0.entries(), x1.entries())]
        assert a2*nmod_mat([[r] for r in result], P2) == b2
        return result

    def validate(self, D):
        u, v = D
        assert u.leading_coefficient() == 1
        assert v.degree() < u.degree() <= GENUS
        assert (self.f-v*v) % u == 0

    def reduce(self, u, v):
        m = u.degree()
        if m <= GENUS:
            return u, v
        pole = m+GENUS
        a_max = pole//2
        b_max = (pole-self.f.degree())//2
        cols = [v]
        for _ in range(b_max):
            cols.append((self.x*cols[-1]) % u)
        if pole % 2 == 0:
            rows = [[int(col[i]) for col in cols] for i in range(a_max, m)]
            rhs = [1]+[0]*(m-a_max-1)
            assert len(rows) == len(cols)
            b = nmod_poly(self.solve(rows, rhs), P2)
        else:
            rows = [[int(col[i]) for col in cols[:-1]] for i in range(a_max+1, m)]
            rhs = [-int(cols[-1][i]) for i in range(a_max+1, m)]
            assert len(rows) == len(cols)-1
            b = nmod_poly(self.solve(rows, rhs)+[1], P2)
        a = (b*v) % u
        assert a.degree() <= a_max and b.degree() <= b_max
        if pole % 2 == 0:
            assert a[a_max] == 1
        else:
            assert b[b_max] == 1
        q = divide(a*a-self.f*b*b, u)
        assert q.degree() == GENUS and q.leading_coefficient() == (1 if pole % 2 == 0 else P2-1)
        if pole % 2:
            q = -q
        w = (-a*self.inverse(b, q)) % q
        self.validate((q,w))
        return q, w

    def add(self, D, E):
        u, v = D
        r, s = E
        if u.degree() == 0:
            return E
        if r.degree() == 0:
            return D
        if D == E:
            correction = (divide(self.f-v*v, u)*self.inverse(2*v, u)) % u
        else:
            correction = ((s-v)*self.inverse(u, r)) % r
        combined_u, combined_v = u*r, v+u*correction
        assert (self.f-combined_v*combined_v) % combined_u == 0
        out = self.reduce(combined_u, combined_v)
        over_p = lambda pair: tuple(poly(f,P) for f in pair)
        assert over_p(out) == self.finite_add(over_p(D),over_p(E))
        self.finite_crosschecks += 1
        return out

    def neg(self, D):
        return D[0], -D[1]

    def finite_add(self, D, E):
        """Independent usual gcd-Cantor arithmetic over the residue field."""
        u, v = D
        r, s = E
        if u.degree() == 0:
            return E
        if r.degree() == 0:
            return D
        h, c1, c2 = u.xgcd(r)
        d, a, b = h.xgcd(v+s)
        w = divide(u*r, d*d)
        z = divide(a*c1*u*s + a*c2*r*v + b*(v*s+self.f0), d) % w
        assert (self.f0-z*z) % w == 0
        while w.degree() > GENUS:
            q = divide(self.f0-z*z, w)
            q *= pow(int(q.leading_coefficient()), -1, P)
            z = (-z) % q
            w = q
        return w, z

    def finite_mul(self, D, n):
        Q = nmod_poly([1], P), nmod_poly([], P)
        A = tuple(poly(f, P) for f in D)
        for bit in bin(n)[2:]:
            Q = self.finite_add(Q,Q)
            if bit == "1":
                Q = self.finite_add(Q,A)
        return Q

    def quadratic_lifts(self):
        square = {a*a % P for a in range(P)}
        out = []
        for c in range(1,P):
            for b in range(P):
                if (b*b-4*c) % P in square:
                    continue
                u = nmod_poly([c,b,1], P2)
                a = self.f0 % poly(u,P)
                if not a:
                    continue
                target = int(a[0]), int(a[1])
                root = next(((r,s) for s in range(P) for r in range(P)
                             if ((r*r-c*s*s)%P,(2*r*s-b*s*s)%P)==target),None)
                if root is None:
                    continue
                v0 = nmod_poly(list(root),P2)
                v = (v0+(P*poly(divided_digit((self.f-v0*v0)%u),P2)*
                         self.inverse(2*v0,u))%u)%u
                self.validate((u,v))
                out.append((u,v))
        return out

    def make_shifts(self, quadratics, seed, count=8):
        rng = random.Random(seed)
        pieces = rng.sample(quadratics, count*(GENUS//2))
        shifts = []
        for j in range(count):
            Q = self.one,self.zero
            for D in pieces[j*(GENUS//2):(j+1)*(GENUS//2)]:
                Q = self.add(Q,D if rng.randrange(2) else self.neg(D))
            u, v = Q
            assert u.degree()==GENUS
            assert poly(u,P).gcd(poly(u.derivative(),P))==1
            assert poly(u,P).gcd(poly(v,P))==1
            self.validate(Q)
            shifts.append(Q)
        return shifts

    def shifted_mul(self, D, n, shifts, target):
        """Keep [m]D+T_i in an integral chart along the scalar bits."""
        count = len(shifts)
        failed = 0
        changes = 0
        offsets = {}
        transitions = {}
        second = {}

        def try_add(A, B):
            nonlocal failed
            try:
                return self.add(A,B)
            except BadChart:
                failed += 1
                return None

        def move(Q, i, j):
            if i == j:
                return Q
            key = i,j
            if key not in transitions:
                transitions[key] = try_add(shifts[j], self.neg(shifts[i]))
            T = transitions[key]
            return None if T is None else try_add(Q,T)

        def correction(j,k,bit):
            key = j,k,bit
            if key in offsets:
                return offsets[key]
            if j == k:
                T = self.neg(shifts[j])
            else:
                if j not in second:
                    second[j] = try_add(shifts[j],shifts[j])
                U = second[j]
                T = None if U is None else try_add(shifts[k],self.neg(U))
            if T is not None and bit:
                T = try_add(T,D)
            offsets[key] = T
            return T

        Q, i = shifts[target],target
        for idx, char in enumerate(bin(n)[2:]):
            bit = int(char)
            found = None
            for j in [i]+[k for k in range(count) if k!=i]:
                Qj = move(Q,i,j)
                if Qj is None:
                    continue
                twice = try_add(Qj,Qj)
                if twice is None:
                    continue
                for k in [target]+[z for z in range(count) if z!=target]:
                    C = correction(j,k,bit)
                    Qk = None if C is None else try_add(twice,C)
                    if Qk is not None:
                        found = Qk,k
                        changes += int(j!=i)+int(k!=j)
                        break
                if found is not None:
                    break
            if found is None:
                raise BadChart(f"no chart at bit {idx}")
            Q,i = found
        R = move(Q,i,target)
        if R is None:
            for j in range(count):
                if j!=i and j!=target:
                    A = move(Q,i,j)
                    R = None if A is None else move(A,j,target)
                    if R is not None:
                        break
        if R is None:
            raise BadChart("cannot translate to terminal chart")
        return R,{"chart_rejections":failed,"chart_changes":changes}

    def first_log_digit(self, F, E):
        u, v = F
        U, V = E
        u0,v0 = poly(u,P),poly(v,P)
        assert (poly(U,P),poly(V,P)) == (u0,v0)
        delta = divided_digit(U-u)
        d, w, _ = (2*v0).xgcd(u0)
        assert d == 1
        q = (-delta*w) % u0
        x = nmod_poly([0,1],P)
        values = []
        for _ in range(GENUS):
            values.append(int(q[GENUS-1]))
            q = (q*x) % u0
        # Independent direct trace in each irreducible quadratic residue disc.
        trace = [0]*GENUS
        unit, parts = u0.factor()
        assert unit == 1 and len(parts) == GENUS//2
        for factor, multiplicity in parts:
            assert factor.degree()==2 and multiplicity==1
            d, inv, _ = (2*u0.derivative()*v0).xgcd(factor)
            assert d==1
            h = (-delta*inv) % factor
            for i in range(GENUS):
                trace[i] = (trace[i]+2*int(h[0])-int(factor[1])*int(h[1]))%P
                h = (h*x)%factor
        assert values == trace
        return values


def main():
    root = Path(__file__).resolve().parent
    source = json.loads((root/"curve_C29.json").read_text())
    f = source["F_ascending"]
    fz, az, bz = (fmpz_poly(source[key])
                  for key in ("F_ascending","A_star_ascending","B_star_ascending"))
    assert fz == az*az+fmpz_poly([0,1])*bz*bz
    assert fz.degree() == 2*GENUS+1 and fz[2*GENUS+1] == 1
    assert az.degree() == bz.degree() == GENUS and bz[GENUS] == 1
    assert az.gcd(bz) == 1
    assert az[0]==1 and abs(int(bz[0]))==1 and bz.degree()==GENUS
    assert fz(1)==fz(-1)==2**70
    A = nmod_poly(source["A_star_ascending"],P2)
    B = nmod_poly(source["B_star_ascending"],P2)
    J = Jacobian(f)
    assert J.f0.gcd(J.f0.derivative())==1
    classes = [(nmod_poly([-a,1],P2),nmod_poly([y],P2))
               for a,y in [(0,1),(1,2**35),(-1,2**35)]]
    for D in [*classes,(B,(-A)%B)]:
        J.validate(D)
        if J.finite_mul(D,N)[0] != 1:
            raise ArithmeticError("candidate multiplier does not kill reduction")
    assert N%P==13
    print("finite checks passed",N,flush=True)
    qs = J.quadratic_lifts()
    print("usable quadratic discs",len(qs),flush=True)
    all_runs=[]
    for seed,target in [(371,0),(372,4)]:
        shifts = J.make_shifts(qs,seed)
        F = shifts[target]
        rows=[]
        print("start charts",seed,target,flush=True)
        for i,D in enumerate(classes):
            begin = perf_counter()
            E,stats = J.shifted_mul(D,N,shifts,target)
            digit = J.first_log_digit(F,E)
            print("digit",seed,i,stats,"seconds",round(perf_counter()-begin,3),digit,flush=True)
            rows.append({"digit_N_log":digit,"chart":stats,
                         "terminal":list(map(coeffs,E))})
        all_runs.append({"seed":seed,"target":target,"initial":list(map(coeffs,F)),
                         "rows":rows})
    assert [r["digit_N_log"] for r in all_runs[0]["rows"]] == [r["digit_N_log"] for r in all_runs[1]["rows"]]
    rows = [[c*pow(N*(2 if i==0 else 1),-1,P)%P for c in r["digit_N_log"]]
            for i,r in enumerate(all_runs[0]["rows"])]
    e = [[int(j==i) for j in range(GENUS)] for i in range(2)]
    matrix = nmod_mat(rows+e,P)
    rank = matrix.rank()
    pivots=None
    for extra in combinations(range(2,GENUS),3):
        v=(0,1)+extra
        det=int(nmod_mat([[r[j] for j in v] for r in rows+e],P).det())
        if det:
            pivots={"columns":v,"det_mod31":det}
            break
    half = B,(-A)%B
    direct_H, direct_stats = J.shifted_mul(half,N,shifts,target)
    direct_digit = J.first_log_digit(F,direct_H)
    assert [(r*pow(N,-1,P))%P for r in direct_digit]==rows[0]
    assert nmod_mat(rows,P).rank()==3 and rank==5
    assert pivots=={"columns":(0,1,2,3,4),"det_mod31":20}
    c = pivots["columns"]
    A = nmod_mat([[row[j] for j in c] for row in rows+e], P)
    iA = A.inv()
    separating = []
    for index in (3,4):
        sparse = [0]*GENUS
        for j,col in enumerate(c):
            sparse[col] = int(iA[j,index])
        want = [int(i==index) for i in range(5)]
        assert [sum(x*y for x,y in zip(row,sparse))%P for row in rows+e] == want
        separating.append(sparse)
    print("log digits H,+1,-1",rows,flush=True)
    print("known rank",nmod_mat(rows,P).rank(),"with forced jets",rank,pivots,flush=True)
    print("direct H agrees",direct_stats,"finite_Cantor_addition_crosschecks",J.finite_crosschecks,flush=True)
    (root/"logs_mod31.json").write_text(json.dumps({"p":P,"N":N,
        "known_log_div31":rows,"rank_known":nmod_mat(rows,P).rank(),
        "rank_with_jets":rank,"rank_witness":pivots,"known_span_separators":separating,
        "direct_H_check":{"digit_N_log":direct_digit,"terminal":list(map(coeffs,direct_H)),"chart":direct_stats},
        "finite_Cantor_addition_crosschecks":J.finite_crosschecks,"runs":all_runs},indent=2)+"\n")


if __name__ == "__main__":
    main()
