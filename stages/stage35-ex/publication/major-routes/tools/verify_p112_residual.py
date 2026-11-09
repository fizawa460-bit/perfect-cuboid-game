#!/usr/bin/env python3
"""Rebuild historical P112 three-mask sets and compare later LOW exclusions.
Only exact integer set arithmetic; no physical-source/global theorem audit.
"""
from json import dumps

def prime_factors(n):
    assert n >= 1
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def odd_kernel(n):
    return {p for p, e in prime_factors(n).items() if e % 2}

def c181_all(n):
    return any(j > 0 and j % 3 == 0 and
               all(p == 5 or p % 20 in (13, 17) for p in odd_kernel(j // 3))
               for j in (n - 1, n + 1))

def c181_ae(n):
    return any(j > 0 and j % 3 == 0 and
               all(p == 5 or p % 5 in (2, 3) for p in odd_kernel(j // 3))
               for j in (n - 1, n + 1))

def c212_all(n):
    if n % 8 == 0:
        return False
    for j in (n - 1, n + 1):
        f = prime_factors(j)
        outside = [p for p in f if p not in (3, 5, 7)]
        if f.get(3, 0) and len(outside) == 1 and outside[0] >= 11 and outside[0] % 8 in (3, 5):
            return True
    return False

def band(lo, hi):
    ns = set(range(lo, hi + 1, 2))
    a = {n for n in ns if c181_all(n)}
    b = {n for n in ns if c212_all(n)}
    c = {n for n in ns if n % 8 != 0 and c181_ae(n)}
    return {"all": ns, "A": a, "B": b, "C": c, "old": a | b,
            "additional": c - a - b, "covered": a | b | c,
            "uncovered": ns - (a | b | c)}

def main():
    low = band(12, 154)
    mid = band(156, 196)
    assert tuple(len(low[k]) for k in ("all", "A", "B", "old", "C", "additional", "covered", "uncovered")) == (72,16,10,24,27,12,36,36)
    assert tuple(len(mid[k]) for k in ("all", "A", "B", "old", "C", "additional", "covered", "uncovered")) == (21,4,9,10,5,2,12,9)
    assert sorted(low["additional"]) == [20,22,44,46,62,68,70,82,106,140,142,154]
    assert sorted(mid["additional"]) == [188,190]
    assert sorted(mid["uncovered"]) == [156,162,168,174,176,180,184,186,192]
    r367 = {18}
    r368 = {24,32,36,54,56,64,66,80,84,88,92,94,96,104,114,122,124,126,128,144,152}
    r369 = {48,78,90,120,132}
    assert (r367 | r368 | r369) <= low["uncovered"]
    assert len(r367 | r368 | r369) == 27
    remain = low["uncovered"] - r367 - r368 - r369
    assert sorted(remain) == [12,30,42,60,72,102,108,138,150]
    signs = {sgn*n for n in remain for sgn in (-1,1)} - {12,30}
    assert sorted(signs) == [-150,-138,-108,-102,-72,-60,-42,-30,-12,42,60,72,102,108,138,150]
    print(dumps({"historical_P112_low": {k:len(low[k]) for k in ("all","A","B","old","C","additional","covered","uncovered")},
                 "historical_P112_mid": {k:len(mid[k]) for k in ("all","A","B","old","C","additional","covered","uncovered")},
                 "later_absolute_exclusions":27,"LOW_residual_absolute":sorted(remain),
                 "LOW_residual_signed":sorted(signs),"new_math":False,
                 "all_masks_mathematical_audit":"DEPENDENT_ON_RETAINED_PROOFS"},ensure_ascii=False,indent=2))
if __name__ == "__main__":
    main()
