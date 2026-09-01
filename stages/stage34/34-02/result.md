# Stage34-02 — audited Route D, D1 local closure, D2 explicit-map layer

Status: `ACTIVE_D2_EXCEPTIONAL_LOCUS_AND_ROUNDTRIP_AFTER_14_MAPS_MATERIALIZED`.

## Audited route

PR #1480 hostile audit PASSed the Face-3 factorization, genus-5 cover, finite squareclass support and Route-D selection on audited head `d54ee6f0eda2814781301cc80ff11a47f92a8c24`.

The exact cover remains

```text
E_q: y^2=x(x+1)(x+q^2)
C_q: z^2=(x^2+q^2)((1+q^2)x^2+4q^2x+q^2(1+q^2)).
```

All Face-3 poles `x=+/-q` are exact order-4 torsion and lie outside the non-torsion receiver population.

## D1 — local squareclass closure

The finite descent is now

```text
104 raw squareclasses
 -> 30 by sum-of-two-squares valuation
 -> 22 by exact good-prime projective residues
 -> 14 locally viable classes by complete remaining Q_p classification.
```

The eight final nontrivial classes on `80/39` and `60/11` are all `Q_7`-insoluble. Every locally viable class is exactly `d=1` or `d=2` on each of the seven fibers, with rational torsion witnesses `x=0` and `x=q` respectively. This does not give non-torsion receiver survival.

The exact MW reduction panel at `107,109,113,127` leaves congruence survivors, so D1 finite congruence pruning is not a complete global MW sieve.

## D2 compression — 14 split covers -> 7 common Jacobians

The locally viable split quartics are

```text
K_{q,1}: W^2=(1+q^2)t^4+8q t^3+2(1+q^2)t^2-8q t+(1+q^2),
K_{q,2}: W^2=4(q+1)^2t^4-8(q+1)^2t^3+8(1+q^2)t^2-4(q-1)^2t+(q-1)^2.
```

Both have the same binary-quartic invariants

```text
I=16(q^4+14q^2+1),
J=128(q^2+1)(q^2-6q+1)(q^2+6q+1),
```

hence the common Jacobian

```text
J_q: y^2=x^3-(I/48)x-(J/1728).
```

All seven `J_q` have unconditional full free Mordell-Weil bases certified by Actions run `33497875525`: rank 2 for `20/21,24/7,20/99`, rank 1 for `80/39,84/13,48/55,60/11`.

## D2 explicit quartic -> Jacobian maps

The formal Stage31 `S31-W01` pattern has now been instantiated computationally for all fourteen `K_{q,d}`.

Dedicated generation-2 run:

```text
workflow run: 33499349144
job:          99828863469
head:         ac383f76d085e5ebbad6787075d6c3b8e1c9838e
artifact:     9797053559
artifact sha: 6cea01c06135204eb591f1192d2ac84b196e1fdebc7df89f445f02853378d303
```

For every `(q,d)` the official Magma calculator successfully executed

```text
E, phi := EllipticCurve(K_{q,d}, P);
DefiningPolynomials(phi);
InverseDefiningPolynomials(phi);
IsIsomorphic(E,J_q);
IsomorphismData(E -> J_q);
BaseScheme(phi).
```

All fourteen cases have exactly three forward and three inverse defining polynomials, and the selected rational base point is sent to the elliptic origin. The generation-2 artifact is self-contained; `d2-quartic-map-lock.json` records a deterministic SHA for each complete map-data block and the exact `E -> J_q` isomorphism data.

A strong structural pattern appears in every case:

```text
d=1: third forward coordinate = (X-Z)^3,
d=2: third forward coordinate = X^3.
```

This exposes a tiny exceptional-locus problem rather than fourteen unrelated map problems. However, the exact naive forward/inverse base schemes and the round-trip extension at those exceptional points have not yet been promoted.

Evidence:

- `d2-quartic-map-preflight.json`
- `run_d2_magma_quartic_maps.py`
- `d2-quartic-map-execution.json`
- `d2-quartic-map-lock.json`

## Current exact leaf

```text
D2_CERTIFY_EXCEPTIONAL_LOCI_AND_ROUNDTRIP_EXTENSION_FOR_14_MAPS
  -> prove the exact forward/inverse base points from the materialized formulas;
  -> certify K -> E -> K round-trip on a nonexceptional rational test point and the curve-place extension at the exceptional points;
  -> only then bind the explicit J_q coordinates to the certified full MW bases;
  -> proceed to covering / elliptic-Chabauty and exact pullback to C_q -> E_q.
```

## Firewalls

```text
D1_LOCAL_CLASSIFICATION_COMPLETE=true
D1_LOCALLY_VIABLE_CLASSES=14
D1_GLOBAL_MW_SIEVE_COMPLETE=false
D2_COMMON_JACOBIAN_RANKS_CERTIFIED=true
D2_MAP_MATERIALIZATION_EXECUTION_COMPLETE=true
D2_EXPLICIT_BIRATIONAL_MAPS_COMPLETE=false
D2_EXCEPTIONAL_LOCI_COMPLETE=false
DIRECT_COVER_RATIONAL_POINTS_COMPLETE=false
ALL_MULTIPLES_CLOSED=false
R29_EXT_CHANG_C_closed=false
PARENT_ROUTE_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
