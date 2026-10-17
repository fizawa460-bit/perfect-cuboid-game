#!/usr/bin/env python3
"""Stage32 BOUNDARY-G0-D044-HECKE: computational checks behind the Hecke-index proof (see CONTRACT.md).

Fail-closed checks:
  1. Hecke degrees.  For Delta = (2,3,8) (quaternion algebra over Q(sqrt2) ramified only at (sqrt2) and one real place),
     the Hecke degrees of commensurator elements outside Delta are products over unramified primes P^k of
     N(P)^(k-1) (N(P)+1).  Unramified primes of Z[sqrt2]: p = ±1 mod 8 split (norm p), p = ±3 mod 8 inert (norm p^2).
     Every degree h <= 1056 with 11 | h is supported on ONE prime ideal (k = 1) of norm >= 241; the list is exactly
     {242, 264, 440, 594, 770, 858, 968, 1034}.
  2. Numerical consistency for g0-d044 (NOT a machine proof of the geometry, which is in CONTRACT.md §1): e = nu = 48,
     d = 44, n1 = n2 = 22; genus 23 for D; the Riemann-Hurwitz bookkeeping 44 = 22*2; divisors of 22; 11 > 4.
  3. The Bolza curve w^2 = x^5 - x is branched at the 6 points {0, inf, ±1, ±i} (octahedron vertices = cusps of X(4)).
  4. g1-d048 (open): lists the Hecke degrees compatible with index in {6, 8, 12, 24}: exactly {8 (P|7), 24 (P|23)}.
No MAIN / theorem credit; the proof itself requires hostile audit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from sympy import I, Poly, primerange, symbols

HERE = Path(__file__).resolve().parent
RESULT = HERE / "RESULT.json"
LIMIT = 1056


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def hecke_degrees(limit: int) -> dict[int, list[tuple[str, ...]]]:
    local = []
    for p in primerange(3, limit + 1):
        if p % 8 in (1, 7):
            norms = [(p, f"split p={p}")] * 2           # two distinct primes of norm p
        elif p * p <= limit:
            norms = [(p * p, f"inert p={p}")]
        else:
            continue
        for idx, (N, tag) in enumerate(norms):
            k = 1
            while N ** (k - 1) * (N + 1) <= limit:
                local.append((N ** (k - 1) * (N + 1), f"{tag}#{idx} k={k}"))
                k += 1
    out: dict[int, list[tuple[str, ...]]] = {}

    def rec(i, prod, parts):
        if parts:
            out.setdefault(prod, []).append(tuple(parts))
        for j in range(i, len(local)):
            h, tag = local[j]
            # one entry per prime (do not combine two powers of the same prime)
            if parts and tag.split(" k=")[0] in {p.split(" k=")[0] for p in parts}:
                continue
            if prod * h <= limit:
                rec(j + 1, prod * h, parts + [tag])

    rec(0, 1, [])
    return out


def main() -> None:
    res = json.loads(RESULT.read_text(encoding="utf-8"))
    req(res.get("canonical_sha256_without_this_field") == canon(res), "RESULT.json canonical drift")
    req(not any(res["credit"].values()), "credit firewall")

    deg = hecke_degrees(LIMIT)
    d11 = sorted(h for h in deg if h % 11 == 0)
    req(d11 == res["hecke"]["degrees_le_1056_divisible_by_11"], f"Hecke list drift: {d11}")
    for h in d11:
        req(all(len(parts) == 1 for parts in deg[h]), f"degree {h} not from a single prime")
        req(h - 1 >= 241, f"degree {h} from a small prime")
    req(min(d11) > 22, "orbit-size contradiction needs h > 22")
    print("PASS: every Hecke degree h <= 1056 with 11 | h is supported on a single prime ideal (k=1) of norm >= 241:", d11)

    # equality-case numerics (g0-d044)
    g, d, e, nu = 0, 44, 48, 48
    req(2 * nu == e + d - 4 * g + 4, "equality case")
    n = d // 2
    genus_D = (2 * (2 * g - 2) + 48) // 2 + 1
    req(genus_D == 23 and 2 * genus_D - 2 == n * (2 * 2 - 2), "D genus 23 and f_i étale of degree 22 onto genus 2")
    req(sorted(k for k in range(1, 23) if 22 % k == 0) == [1, 2, 11, 22], "divisors of 22")
    req(22 // 2 > 4, "index-2 case forces degree >= 11 > 4 onto the image in YxY")
    print("PASS (numerical consistency only; the geometric derivation is in CONTRACT.md §1): g0-d044 genus/degree bookkeeping "
          "(D genus 23, 2*23-2 = 22*2), divisors of 22 = {1,2,11,22}, index-2 degree bound 11 > 4")

    # Bolza branch points
    x = symbols("x")
    roots = Poly(x ** 5 - x, x).all_roots()
    req(set(roots) == {0, 1, -1, I, -I}, "Bolza finite branch points")
    print("PASS: Bolza w^2 = x^5 - x branched at {0, ±1, ±i} and infinity (octahedron vertices)")

    # g1-d048 open candidates
    cands = sorted(h for h in deg if any(h * s in (6, 8, 12, 24) for s in (1, 2, 3, 4, 6, 8, 12, 16, 24, 48)))
    req(cands == res["g1_d048_open"]["compatible_hecke_degrees"], f"g1 candidate drift: {cands}")
    print("OPEN: g1-d048 compatible Hecke degrees", cands, "(P|7 and P|23)")
    print("PASS: computational side of the g0-d044 Hecke argument (proof: see CONTRACT.md and EXTERNAL-AUDIT-RECEIPT.md); zero credit")


if __name__ == "__main__":
    main()
