#!/usr/bin/env python3
"""E7 counting code: exact degree-one prime counts for the row383 tail.

Semantics (identical to row382_inputs.degree_one_count and to the
original row379 C++ generator roots379.cpp): for a rational prime p,

    c(p) = deg gcd(f mod p, x^p - x)  in F_p[x]

where f is the degree-105 stem polynomial (curve_C29.json, F_ascending).
c(p) is the number of DISTINCT roots of f in F_p, i.e. the number of
degree-one prime ideals of the stem field above p as the row383
certificate counts them (a repeated root mod p is counted once, since
x^p - x is separable; this matches both prior implementations).

Usage:
    count_roots.py LO HI OUT.csv [--workers W]

Counts every prime p with LO < p <= HI and writes "p,c" lines.
Checkpointing is the caller's job: run per range chunk, one CSV each.
"""
import json
import sys
import time
from math import isqrt
from multiprocessing import Pool
from pathlib import Path

from flint import nmod_poly

HERE = Path(__file__).resolve().parent
COEFF = json.loads((HERE / "curve_C29.json").read_text())["F_ascending"]
assert len(COEFF) == 106 and COEFF[-1] == 1


def primes_between(lo, hi):
    """All primes p with lo < p <= hi (sieve of Eratosthenes)."""
    sieve = bytearray(b"\1") * (hi + 1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(hi) + 1):
        if sieve[p]:
            sieve[p * p::p] = b"\0" * ((hi - p * p) // p + 1)
    return [p for p in range(max(lo + 1, 2), hi + 1) if sieve[p]]


def count_one(p):
    f = nmod_poly(COEFF, p)
    x = nmod_poly([0, 1], p)
    return p, int(f.gcd(x.pow_mod(p, f) - x).degree())


def main():
    lo, hi, out = int(sys.argv[1]), int(sys.argv[2]), Path(sys.argv[3])
    workers = 3
    if "--workers" in sys.argv:
        workers = int(sys.argv[sys.argv.index("--workers") + 1])
    primes = primes_between(lo, hi)
    t0 = time.time()
    if workers > 1:
        with Pool(workers) as pool:
            rows = pool.map(count_one, primes, chunksize=256)
    else:
        rows = [count_one(p) for p in primes]
    dt = time.time() - t0
    assert [p for p, _ in rows] == primes
    assert all(0 <= c <= 105 for _, c in rows)
    out.write_text("".join(f"{p},{c}\n" for p, c in rows))
    print(f"({lo}, {hi}]: {len(rows)} primes, sum(c) = {sum(c for _, c in rows)}, "
          f"{dt:.1f}s ({1000 * dt / max(len(rows), 1):.3f} ms/prime, {workers} workers)",
          flush=True)


if __name__ == "__main__":
    main()
