# Stage34-02 — audited Route D, D1 local closure, D2 fiber-product MW-sieve preparation

Status: `ACTIVE_D2_MATCHING_X_FIBER_PRODUCT_MW_SIEVE`.

## Locked foundation

- Stage34-01 exact object/global population: hostile-audited CLOSED.
- Stage34-02 Route-D algebraic reduction: hostile-audited PASS on `d54ee6f0eda2814781301cc80ff11a47f92a8c24`.
- Exact genus-5 target:

```text
E_q: y^2=x(x+1)(x+q^2)
C_q: z^2=(x^2+q^2)((1+q^2)x^2+4q^2x+q^2(1+q^2)).
```

## D1 completed local layer

```text
104 raw squareclasses -> 30 -> 22 -> 14 locally viable.
```

Exactly `d=1,2` survive for each of the seven q. All other classes are rigorously locally obstructed. The finite E_q MW congruence panel is exact but not a global sieve.

## D2: fourteen split quartics and seven Jacobians

The fourteen surviving split curves are the two quartics `K_{q,1}, K_{q,2}` for each q. Each pair has the same binary-quartic invariants and common Jacobian `J_q`. All seven `J_q(Q)` full free Mordell-Weil bases are unconditionally certified (rank 2 for `20/21,24/7,20/99`; rank 1 for the other four fibers).

Generation-2 official-Magma execution materialized all fourteen birational maps, inverse defining polynomials and exact `E -> J_q` isomorphisms. The complete self-contained formulas are now permanently stored in

`d2-quartic-map-certificate.json`.

## Coordinate base loci are not curve-level holes

Magma V2.29 documents `EllipticCurve(C,P)` as returning a birational map from the genus-one curve to an elliptic curve. The Stacks Project, Lemma 53.2.2 / Theorem 53.2.6, implies that rational maps from normal projective curves to proper curves extend uniquely; applying this to the forward birational map and its inverse gives mutually inverse global morphisms.

Therefore every

```text
K_{q,d} ~= J_q   over Q
```

is a global curve isomorphism. The zeros of one chosen homogeneous coordinate presentation are not missing curve points.

Evidence:

- `d2-quartic-map-lock.json`
- `d2-birational-extension-theorem-lock.json`
- `d2-quartic-map-certificate.json`

Two attempted CAS-only hardenings (runs `33500019489`, `33500164959`) hit Magma datatype limitations for `CrvEll` in `EvaluateByPowerSeries` / `Extend`; they failed before any mathematical assertion and grant no credit.

## Exact split-to-receiver pullback

For reduced `q=a/b`, projective parameter `[T:S]` maps to receiver x by

```text
d=1: [T:S] -> [a(T^2-S^2) : 2bTS]
d=2: [T:S] -> [a(2T^2-4TS+S^2) : b(2T^2-S^2)].
```

Both are genuine projective maps with no base point.

Rational exceptional fibers are already outside the receiver:

```text
d=1: t=0,infinity -> x=infinity -> E_q origin;
d=2: t=0,1 -> x=-q; t=1/2,infinity -> x=+q -> order-4 E_q torsion.
```

Thus for the audited non-torsion receiver population the global problem is exactly:

> classify rational pairs `(P_E,P_J)` in `E_q(Q) x J_q(Q)` such that the corresponding `K_{q,d}` point and `P_E` have the same finite non-pole x.

The forward/reverse equivalence is locked in `d2-split-to-receiver-pullback-lock.json`.

## Current exact leaf

```text
D2_BUILD_PROOF_COMPLETE_FIBER_PRODUCT_MORDELL_WEIL_SIEVE_ON_MATCHING_X_USING_FULL_E_q_AND_J_q_BASES
```

Use the certified full MW bases on both elliptic sides, reduce them through exact finite groups, and sieve the matching-x condition. Finite residue statistics alone are not closure; any surviving MW cosets must be refined or sent to elliptic-Chabauty/covering until completeness is proved.

## Credit boundary

```text
D1_LOCAL_CLASSIFICATION_COMPLETE=true
D2_COMMON_JACOBIAN_RANKS_CERTIFIED=true
D2_EXPLICIT_BIRATIONAL_MAPS_COMPLETE=true
D2_EXCEPTIONAL_LOCI_COMPLETE=true
D2_SPLIT_TO_RECEIVER_PULLBACK_COMPLETE=true
D2_FIBER_PRODUCT_MW_SIEVE_COMPLETE=false
DIRECT_COVER_RATIONAL_POINTS_COMPLETE=false
ALL_MULTIPLES_CLOSED=false
R29_EXT_CHANG_C_closed=false
PARENT_ROUTE_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
