"""Recompute the same-source finite slope conditions with both characters zero."""
from concurrent.futures import ProcessPoolExecutor
from math import prod
from pathlib import Path
from hashlib import sha256
import json

from flint import nmod_poly
from verify_row378 import possible_slopes, quadratic_artin

HERE = Path(__file__).resolve().parent
DATA = (HERE / "curve_factors.json").read_bytes()
assert sha256(DATA).hexdigest() == "0eb486cfb6e11c20558d2176909bfb13f67effe1880500abac8508339c32cdc2"
COEFF = json.loads(DATA)["ascending_coefficients"]


def one_prime(row):
    p = row["p"]
    roots = {}
    for x in range(p):
        roots.setdefault(x*x % p, []).append(x)
    polynomials = [nmod_poly(c, p) for c in COEFF]
    _, slopes = possible_slopes(p, COEFF, polynomials, roots, {})
    assert len(slopes) == row["retained_slopes"]
    factors = [nmod_poly(c, p) for c in row["factors_ascending"]]
    assert prod(factors) == polynomials[0]
    possible = [
        s for s in slopes if not s[3] or
        quadratic_artin(s[-1], factors, roots) == quadratic_artin(-s[-1] % p, factors, roots) == 0
    ]
    assert len(possible) >= 2
    before_abc = all(s[2]*s[3]*s[4] % p == 0 for s in slopes)
    before_a = all(s[2] == 0 for s in slopes)
    after_abc = all(s[2]*s[3]*s[4] % p == 0 for s in possible)
    after_a = all(s[2] == 0 for s in possible)
    return [p, len(slopes), len(possible), before_abc, before_a, after_abc, after_a]


def zero_pair_sieve():
    table_bytes = (HERE / "row378_exact.json").read_bytes()
    assert sha256(table_bytes).hexdigest() == "f4f616732f3985260959bb9751d6cf50810f46cd52d6ad0fb7b4a8a1991f39b4"
    table = json.loads(table_bytes)["prime_tables"]
    with ProcessPoolExecutor(max_workers=6) as pool:
        rows = list(pool.map(one_prime, table, chunksize=8))
    before, after = [sum(r[i] for r in rows) for i in (1,2)]
    new_abc = [r[0] for r in rows if r[5] and not r[3]]
    new_a = [r[0] for r in rows if r[6] and not r[4]]
    all_a = [r[0] for r in rows if r[6]]
    return {"prime_count":len(rows), "retained_before":before, "retained_after":after,
            "forced_ABC_count":sum(r[5] for r in rows), "forced_A_count":len(all_a),
            "new_forced_ABC_primes":new_abc, "new_forced_A_primes":new_a,
            "A_modulus_without_p199":str(8*prod(all_a)), "per_prime":rows}


if __name__ == "__main__":
    print(json.dumps(zero_pair_sieve(),indent=2))
