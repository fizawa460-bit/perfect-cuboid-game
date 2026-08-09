#!/usr/bin/env python3
"""Stage14-t19: conditioned discriminant / missing-face squareclass ledger audit."""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt, sqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t19/conditioned_discriminant_ledger.json'
MAX_B = 2_000_000
CUTS = (1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000)
EXPECTED = {1000:2,2000:5,5000:15,10000:25,20000:42,50000:62,100000:89,200000:116,500000:188,1000000:255,2000000:356}


def is_square_fraction(q):
    if q < 0:
        return False
    return isqrt(q.numerator) ** 2 == q.numerator and isqrt(q.denominator) ** 2 == q.denominator


def sqrt_fraction(q):
    assert is_square_fraction(q)
    return Fraction(isqrt(q.numerator), isqrt(q.denominator))


def squarefree_core(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    out = 1
    e = 0
    while n and n % 2 == 0:
        n //= 2
        e ^= 1
    if e:
        out *= 2
    p = 3
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 2
    if n > 1:
        out *= n
    return sign * out


def squareclass(q):
    assert q != 0
    return squarefree_core(q.numerator) * squarefree_core(q.denominator)


def prime_support_squarefree(n):
    n = abs(n)
    out = []
    if n % 2 == 0:
        out.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            n //= p
        p += 2
    if n > 1:
        out.append(n)
    return out


def missing_face_value(a, b, c, mask):
    vals = (a*a+b*b, a*a+c*c, b*b+c*c)
    missing = [vals[i] for i in range(3) if not (mask & (1 << i))]
    assert len(missing) == 1
    return missing[0]


def conditioned_discriminant(face, partner):
    """Return the t12->t14 quotient-x discriminant for a fixed raw point.

    If t=X/S and q is the partner half-angle, put u=2q/(1-q^2)=X2/S2.
    The raw quartic value R^2 is already a square on every exact raw pair.
    The quotient reciprocal quadratic has discriminant Delta_x satisfying

      Delta_x = [t(1+t^2)(1-q^2)R/q^2]^2 * (t^2+u^2).

    Thus its squareclass is exactly the missing-face squareclass.
    """
    S, X, H = face
    S2, X2, H2 = partner
    t = Fraction(X, S)
    q = Fraction(X2, H2 + S2)
    u = Fraction(X2, S2)
    assert u == 2*q/(1-q*q)

    A = Fraction(1 - t*t, 1 + t*t)
    R2 = q**4 + 2*A*q*q + 1
    assert is_square_fraction(R2)
    R = sqrt_fraction(R2)

    y = q*q
    K = t*t * (2*(1-t*t) + (1+t*t)*(y + 1/y))
    C = K + 2
    Delta = C*C - 4
    scale = t*(1+t*t)*(1-q*q)*R/(q*q)
    missing_normalized = t*t + u*u
    assert Delta == scale*scale*missing_normalized
    return Delta, missing_normalized


def main():
    mod = runpy.run_path(str(GRAPH))
    keep, _ = mod['enumerate_multi'](MAX_B)
    object_edges = mod['object_edges']
    assert len(keep) == 356

    ledger = []
    oriented_checks = 0
    for (a,b,c,d),(mask,ds) in keep.items():
        assert mask.bit_count() == 2  # frozen Stage14 census has T=0 through 2m
        edges = object_edges(a,b,c,mask,ds)
        assert len(edges) == 1
        f1, f2 = edges[0]
        miss = missing_face_value(a,b,c,mask)
        cls = squareclass(Fraction(miss))
        assert cls != 1

        for face, partner in ((f1,f2),(f2,f1)):
            Delta, missing_normalized = conditioned_discriminant(face, partner)
            assert squareclass(Delta) == cls
            assert squareclass(missing_normalized) == cls
            assert not is_square_fraction(Delta)
            oriented_checks += 1

        ledger.append({'d':d,'a':a,'b':b,'c':c,'missing_face_squareclass':cls})

    assert oriented_checks == 712
    ledger.sort(key=lambda r:(r['d'],r['a'],r['b'],r['c']))
    lines = ''.join(f"{r['d']}|{r['a']},{r['b']},{r['c']}|{r['missing_face_squareclass']}\n" for r in ledger)
    ledger_sha = sha256(lines.encode()).hexdigest()
    assert ledger_sha == 'f6f86ab2509aabc2c0ebc59bf20d1d4d9df984b4218ec26f7bd350543c89c8f0'

    rows = []
    for B in CUTS:
        z = [r for r in ledger if r['d'] <= B]
        M = len(z)
        assert M == EXPECTED[B]
        cnt = Counter(r['missing_face_squareclass'] for r in z)
        Q = sum(v*v for v in cnt.values())
        primes = set()
        for k in cnt:
            primes.update(prime_support_squarefree(k))
        rank = len(primes)
        entropy = M / (2 ** rank)
        cs_bound = entropy + sqrt((1 - 2 ** (-rank)) * (Q - M*M/(2 ** rank)))
        rows.append({
            'B':B,
            'raw_exactly_two_objects':M,
            'conditioned_oriented_incidences':2*M,
            'conditioned_discriminant_square_hits':0,
            'distinct_object_squareclasses':len(cnt),
            'max_object_squareclass_multiplicity':max(cnt.values()),
            'collision_Q_object':Q,
            'collision_Q_over_M':Q/M,
            'observed_prime_coordinate_rank':rank,
            'fourier_cs_bound_diagnostic':cs_bound,
        })
        assert len(cnt) == M
        assert max(cnt.values()) == 1
        assert Q == M

    report = {
        'stage':'14-t19',
        'identity':{
            'statement':'For a fixed exact raw physical point, the t12->t14 quotient-x discriminant has the same Q*/Q*2 class as the missing third-face squared length.',
            'formula':'Delta_x = [t(1+t^2)(1-q^2)R/q^2]^2 * (t^2+u^2), with u=2q/(1-q^2) and R^2=q^4+2(1-t^2)/(1+t^2)q^2+1.',
            'consequence':'Conditioned on an actual raw pair, Delta_x square iff the missing face diagonal is rational; for integer sides this is exactly the triple gate.',
        },
        'finite_ledger':{
            'max_B':MAX_B,
            'object_count':len(ledger),
            'oriented_conditioned_incidence_count':oriented_checks,
            'conditioned_C0_entries':0,
            'object_squareclasses_distinct':len({r['missing_face_squareclass'] for r in ledger}),
            'max_object_squareclass_multiplicity':1,
            'collision_Q_object':len(ledger),
            'observed_prime_coordinate_rank_B2m':rows[-1]['observed_prime_coordinate_rank'],
            'ledger_sha256':ledger_sha,
            'first_records':ledger[:5],
            'last_records':ledger[-3:],
        },
        'rows':rows,
        'decision':{
            'STAGE14_T19':'COMPLETE_CONDITIONED_DISCRIMINANT_IDENTITY_AND_FINITE_COLLISION_LEDGER',
            'CONDITIONED_DISCRIMINANT_SQUARECLASS_EQUALS_MISSING_FACE':True,
            'CONDITIONED_DISCRIMINANT_IS_NEW_INDEPENDENT_GATE':False,
            'FINITE_RAW_OBJECTS_B2M':356,
            'FINITE_CONDITIONED_ORIENTED_INCIDENCES_B2M':712,
            'FINITE_CONDITIONED_C0_ENTRIES_B2M':0,
            'OBJECT_SQUARECLASS_INJECTIVE_AT_ALL_FROZEN_CUTOFFS':True,
            'FINITE_COLLISION_Q_EQUALS_M':True,
            'OBSERVED_PRIME_COORDINATE_RANK_B2M':554,
            'FINITE_B2M_FOURIER_CS_BOUND_DIAGNOSTIC':rows[-1]['fourier_cs_bound_diagnostic'],
            'FINITE_ZERO_IMPLIES_ASYMPTOTIC_ZERO':False,
            'COLLISION_BOUND_Q_O_B_PROVED':False,
            'T_O_SQRT_B_PROVED':False,
            'PERFECT_CUBOID_NONEXISTENCE_PROVED':False,
            'NEXT':'Stage14-t20 derive/count equal missing-face squareclass collisions over the raw-pair family and target Q_Delta(B)=o(B)',
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report['finite_ledger'], indent=2))
    print(json.dumps(report['decision'], indent=2))


if __name__ == '__main__':
    main()
