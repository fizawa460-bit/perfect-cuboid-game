# Stage34-02 — audited Route D, D1 local closure, D2 common-Jacobian preparation

Status: `ACTIVE_D2_EXPLICIT_QUARTIC_JACOBIAN_MAPS_AFTER_D1_LOCAL_REDUCTION`.

## Audited route

PR #1480 hostile audit PASSed the Face-3 factorization, genus-5 cover, finite squareclass support and Route-D selection on audited head `d54ee6f0eda2814781301cc80ff11a47f92a8c24`.

The exact cover remains

```text
E_q: y^2=x(x+1)(x+q^2)
C_q: z^2=(x^2+q^2)((1+q^2)x^2+4q^2x+q^2(1+q^2)).
```

All Face-3 poles `x=+/-q` are exact order-4 torsion and lie outside the non-torsion receiver population.

## D1 — finite squareclass descent

The audited factorization gives `104` raw squareclasses `d|rad(2ab)`.

- sum-of-two-squares valuation filter: `104 -> 30`;
- exact good-prime projective residue filter: `30 -> 22`;
- complete local classification of the remaining 22: `22 -> 14` locally viable classes.

The eight additional classes

```text
80/39: d=5,10,13,26,65,130
60/11: d=5,10
```

are all `Q_7`-insoluble: after normalizing a hypothetical 7-adic point, exhaustive `P^1(F_7)` reduction gives zero residues satisfying the three split square equations.

Every remaining locally viable class is simply `d=1` or `d=2` on each of the seven fibers. These are genuinely locally soluble because they have explicit rational torsion witnesses:

```text
d=1: x=0,
d=2: x=q.
```

This local solubility does not give non-torsion receiver survival.

Evidence:

- `d1-qp-local-classification.json`
- `verify_d1_qp_local_classification.py`

## Exact MW reduction panel

The audited full Paper-C MW bases define exact reduction maps

```text
rank 1: Z x Z/4 x Z/2 -> E_q(F_p)
rank 2: Z^2 x Z/4 x Z/2 -> E_q(F_p)
```

at common good primes `107,109,113,127`. `d1-mw-reduction-panel.json` and its verifier commit the rank-one four-prime CRT states and rank-two per-prime coefficient states by canonical hashes.

Finite congruence survivors remain. Therefore this panel is useful exact D1 pruning, but is not a proof-complete global MW sieve and grants no receiver closure.

## D2 compression — 14 split covers -> 7 common Jacobians

For `d=1`, parameterizing `x^2+q^2=u^2` gives

```text
K_{q,1}:
W^2=(1+q^2)t^4+8q t^3+2(1+q^2)t^2-8q t+(1+q^2).
```

For `d=2`, parameterizing `x^2+q^2=2u^2` gives

```text
K_{q,2}:
W^2=4(q+1)^2t^4-8(q+1)^2t^3+8(1+q^2)t^2-4(q-1)^2t+(q-1)^2.
```

Both have discriminant

```text
65536*q^2*(q-1)^4*(q+1)^4
```

and the same binary-quartic invariants

```text
I=16(q^4+14q^2+1),
J=128(q^2+1)(q^2-6q+1)(q^2+6q+1).
```

Thus the two locally viable split quartics on each fiber share the same Jacobian

```text
J_q: y^2=x^3-(I/48)x-(J/1728).
```

This convention is cross-checked against the audited Stage31 quartic/elliptic adapter.

## Seven unconditional Jacobian MW ranks

GitHub Actions run `33497875525`, job `99824168746`, with explicit run-key generation 1, ran Ubuntu 24.04 `eclib-tools` / `mwrank -q -v 1 -o`. Every curve reported:

`The rank and full Mordell-Weil basis have been determined unconditionally.`

Ranks:

```text
rank 2: 20/21, 24/7, 20/99
rank 1: 80/39, 84/13, 48/55, 60/11
```

Evidence:

- `d2-split-genus1-quotient-lock.json`
- `d2-jacobian-mw-certificate.json`
- `d2-jacobian-mw-execution.json`

No rank-zero shortcut occurs.

## Current exact leaf

```text
D2_MATERIALIZE_EXPLICIT_K_q_d_TO_J_q_BIRATIONAL_MAPS_AND_EXCEPTIONAL_LOCI
  -> exact round-trip verification using S31-W01 workflow pattern;
  -> use the certified full J_q Mordell-Weil bases in the covering / elliptic-Chabauty layer;
  -> pull every resulting point back through K_{q,d} -> C_q -> E_q;
  -> classify torsion/poles separately from non-torsion receiver points.
```

## Firewalls

```text
D1_LOCAL_CLASSIFICATION_COMPLETE=true
D1_LOCALLY_VIABLE_CLASSES=14
D1_FINITE_MW_PANEL_COMPLETE=true
D1_GLOBAL_MW_SIEVE_COMPLETE=false
D2_COMMON_JACOBIAN_RANKS_CERTIFIED=true
D2_EXPLICIT_BIRATIONAL_MAPS_COMPLETE=false
DIRECT_COVER_RATIONAL_POINTS_COMPLETE=false
ALL_MULTIPLES_CLOSED=false
R29_EXT_CHANG_C_closed=false
PARENT_ROUTE_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
