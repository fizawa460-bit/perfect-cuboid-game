# Stage36 36-09EX — T6 controlled-radical relaxation

## Purpose

36-09EW reduced one T6 realization route to the progression

```text
u = 6147 (mod 11480),
a = 2u,
b = 2u+729,
```

plus five simultaneous primality conditions on

```text
u,
2u+729,
4u+729,
s=(8u^2-729^2)/7,
t=(8u^2+8*729*u+729^2)/41.
```

This leaf asks whether exact primality of all five values is genuinely needed. The answer is no: controlled factor splitting can enlarge the labelled radical support while the exact 36-09EP support matrix still has maximal rank.

Entry authority is V280, exact head `fbf7ed844e859dfb46d5852d3fef94ab66dcae75`, CI `34409767705 / 102661214291`.

## Primitive refinement of the EW progression

For composite values, primitivity must be protected explicitly because

```text
gcd(2u,2u+729) | 729.
```

Refine the progression by

```text
u = 17627 (mod 34440).
```

This is exactly the EW progression together with

```text
u = 2 (mod 3).
```

Hence every retained row has `gcd(2u,2u+729)=1`, while the EW congruences modulo `8,7,41,5` and therefore the shallow dyadic branch and uniform mod-5 no-3 witness remain unchanged.

The bounded search that suggested the seeds below is diagnostic only. No exhaustive, density, or infinitude statement is attached to the progression.

## Exact controlled-radical templates

Eight primitive parameters in the refined progression have `Sel2_dim=2` although at least one of the five EW values is composite. Their canonical labelled-Legendre patterns are pairwise distinct and are named `T10..T17`.

For each seed, factor the five EW values exactly, build the labelled radical datum, canonicalize it with the same P/Q-swap convention as 36-09ES, and construct the abstract support matrix from the pattern alone. The resulting abstract matrix has

```text
rank_F2 = 2n-2
```

for every one of `T10..T17`.

Therefore, by the already exact-green 36-09EP/36-09ES abstract-pattern theorem, matching any one of `T10..T17` is a global sufficient condition for

```text
dim_F2 Sel^2(E_rho,p/Q)=2.
```

This is the desired relaxation: the T6 arithmetic skeleton can survive controlled radical refinement. Exact primality of all five EW values is not necessary.

The eight seed values are

```text
u = 1154147,
    1774067,
    3806027,
    3909347,
    4115987,
    5355827,
    5941307,
    6526787.
```

The support sizes vary: `n=12,14,15,16` occur, so these are genuinely larger radical supports, not hidden replays of the eight-vertex T6 coarse profile.

One representative example is

```text
u = 1154147 = 17 * 67891,
2u+729 = 2309023,
4u+729 = 4617317,
s = 89 * 1033 * 16558609,
t = 286831 * 906727.
```

Its labelled support has twelve odd vertices, hence `n=14`, and the exact support matrix has rank `26=2n-2`.

## EH conditions and literal orbits

The refined progression still has `u=2 mod 5`. Thus every listed seed has the same exact mod-5 no-3 witness as EW:

```text
psi_3(X)=3X^4+4X^2+4 (mod 5),
values on F5 = 4,1,3,3,1.
```

The verifier separately checks the no-4 square condition on every seed. All eight pass. Therefore the 36-09EH fixed-p exclusion criterion applies to every seed, and 36-09EK supplies its complete positive four-point literal orbit.

The eight new orbits are pairwise disjoint and disjoint from the exact 44-value registry already promoted at V280. Thus, after exact-head CI consumption, this leaf can promote

```text
8 new orbits = 32 new fixed parameters,
44 -> 76.
```

## What is global and what is finite

The global result is only the template implication:

```text
parameter matches one of T10..T17
=> abstract support matrix rank = 2n-2
=> Sel2_dim = 2.
```

The existence statements certified here are the eight exact seed orbits. The diagnostic search that found them is not claimed exhaustive, and the eight templates are not claimed to classify all controlled-radical refinements or all maximal-rank patterns.

## Next leaf

The next useful question is to compress `T10..T17` into a structural criterion rather than continuing hash-by-hash:

```text
36-09EY_RHO_T6_RADICAL_REFINEMENT_RANK_COMPRESSION_PREFLIGHT.
```

The target is a graph/Pfaffian or block-rank condition stable under splitting one T6 support vertex into several same-labelled radical vertices.

## Credit firewall

This leaf does not prove infinitely many controlled-radical hits, exhaust all maximal-rank patterns, prove a uniform Sel2 theorem, shrink the parent candidate ledger, prove receiver emptiness, close R29/Q11, close the endpoint, or prove Perfect Cuboid nonexistence.
