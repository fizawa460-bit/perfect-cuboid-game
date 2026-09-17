# MB104 U10 etale-correspondence commensurator arithmetic wall — 2026-09-17

## Scope

Zero-credit preflight for the retained MB104 equality geometry. No MAIN, receiver, effectivity, theorem, endpoint, or merge credit is changed.

## Retained input

The archived equality-rigidity adapter proves that any actual genus-one F1-P5 equality realization produces a connected curve

```text
Z subset C8 x C8
```

whose two projections

```text
f1,f2 : Z -> C8
```

are finite etale maps of equal degree

```text
n = 14 e l,
e in {1,2,4}.
```

The archived Beauville source adapter identifies

```text
C8 = H*/Gamma[8]
```

as the compact modular curve `X(8)` of genus five.

## Candidate high-level obstruction

For a compact hyperbolic curve `C = H/Gamma`, an etale self-correspondence is controlled by the commensurator of the cocompact uniformizing surface group. If `Gamma` is non-arithmetic, Margulis' commensurator criterion makes `Comm(Gamma)` discrete with `Gamma` of finite index. In that case the degrees of irreducible etale self-correspondences are bounded by a finite commensurator-index problem, which would immediately give an explicit large-`l` bound for `n=14el`.

This would have been an exact U4-style large-parameter reducer.

## Arithmeticity test for C8

Published modular-curve results identify `X(8)` as the genus-five curve with automorphism group of order `192`; the natural compact modular quotient to `X(1)` has orbifold signature `(2,3,8)`. Equivalently, the compact uniformizing surface group of `C8` is a torsion-free finite-index subgroup of the cocompact triangle group

```text
Delta(2,3,8).
```

Takeuchi's classification of arithmetic triangle groups includes `(2,3,8)`. Arithmeticity is invariant under passage to finite-index subgroups. Therefore the cocompact surface group uniformizing `C8` is arithmetic.

Primary/standard references used for this preflight:

- K. Takeuchi, *Arithmetic triangle groups*, J. Math. Soc. Japan 29 (1977), 91-106, DOI `10.2969/jmsj/02910091`.
- Modular-curve literature identifying `X(8)` as genus five with automorphism group `SL_2(Z/8Z)/{+-1}` of order `192` and the Wiman genus-five curve; see the retained Freitag--Salvati Manni adapter for the exact `C8=X(8)` identification.

## Consequence

The proposed non-arithmetic finite-commensurator argument cannot bound

```text
n = 14 e l
```

on this curve. In the arithmetic case the commensurator is non-discrete/dense, and arithmetic/Hecke-type etale correspondences of unbounded degree are not excluded by commensurator finiteness.

This does **not** prove that an MB104 correspondence exists for every `l`, nor that every integer `14el` occurs as a correspondence degree. It proves only that non-arithmetic commensurator finiteness is the wrong uniform obstruction for `C8`.

A possible re-entry would require a genuinely packet-sensitive arithmetic statement: for example, an exact description of the relevant arithmetic correspondence index spectrum together with the fixed `(Z/2)^3` / fourteen-node descent passport, strong enough to exclude `n=14el` uniformly or for all large `l`. Degree arithmetic alone is not currently source-locked as such an obstruction.

## Verdict

```text
U10_NONARITHMETIC_COMMENSURATOR_BOUND=BLOCKED
C8_COMPACT_UNIFORMIZING_GROUP_ARITHMETIC=true
TRIANGLE_COMMENSURABILITY_CLASS=(2,3,8)
UNIFORM_DEGREE_BOUND_FROM_DISCRETE_COMMENSURATOR=false
ARITHMETIC_INDEX_SPECTRUM_PACKET_ROUTE=UNTESTED
MAIN_CREDIT=0
RECEIVER_CREDIT=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
MERGE_AUTHORIZED=false
```
