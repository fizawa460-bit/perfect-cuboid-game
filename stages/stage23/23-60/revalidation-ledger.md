# Stage23-60 — source-level revalidation ledger

EVIDENCE_LEVEL=ATTACK_LEDGER
CHECKPOINT=60
POLICY=REVALIDATE_PRIOR_DEAD_ATTACKS_BEFORE_SYNTHESIS

The checkpoint60 policy requires at least eight high-value Stage14/15/Stage23 branches to be reopened at source level before causal synthesis. This ledger does that. Every listed source artifact was opened directly and retested against the literal Stage23 target: primitive canonical exactly-two-face cuboids with integral space diagonal `d=R<=B`.

Allowed verdicts are the controller values `DEAD_CONFIRMED`, `DEAD_REASON_WEAKENED`, `REVIVED_LIVE`, `POPULATION_MISMATCH_ONLY`, and `NEEDS_NEW_INPUT`. A verdict applies only to the stated route, not to the whole method family.

## R60-01 / Q01 — Stage15 explicit ambient exactly-two family

```text
ATTACK_ID=S1415-ATTACK-0709
SOURCE=stages/stage15/15-2/result.md
PRIOR_ROLE=explicit primitive exactly-two lower family without integral space diagonal
VERDICT=DEAD_CONFIRMED
LOWER_BOUND_RELEVANCE=HIGH
```

The source family uses coprime odd `p<q<2p` and

\[
e=4pq,\quad x=4p^2-q^2,\quad y=4q^2-p^2,
\]
with exactly two integral faces, primitivity, and

\[
R^2=17(p^4+q^4).
\]

To enter Stage19 it must additionally satisfy

\[
D^2=17(p^4+q^4).
\]

But for odd `p,q`, `p^4=q^4=1 (mod 16)`, hence

\[
17(p^4+q^4)\equiv2\pmod{16},
\]
which is not a square residue modulo 16. Therefore this entire strong ambient lower family contributes **zero** Stage19 objects. This is a global congruence proof, not finite absence.

```text
ORIGINAL_AMBIENT_LINEAR_LOWER_BOUND_TRANSFERS=false
STAGE19_SPACE_LIFT_GLOBAL_MOD16_OBSTRUCTION=true
FINITE_ZERO_HIT_USED=false
```

## R60-02 / Q03 — elliptic / Selmer-only lower route

```text
ATTACK_ID=S1415-ATTACK-0259
SOURCE=stages/stage14/archive/tasks/14-s1/result.md
PRIOR_ROLE=full-2-torsion elliptic/Selmer interface
VERDICT=DEAD_CONFIRMED
SCOPE=SELMER_OR_POSITIVE_RANK_ALONE_AS_STAGE19_LOWER_MECHANISM
```

The exact source model

\[
E_F:Y^2=Z(Z-S^2)(Z+X^2)
\]
is legitimate arithmetic geometry for the face fiber. However the source audit already showed that nontrivial Selmer and even certified positive Mordell-Weil rank do not separate physical survivors: many inactive controls have positive rank. Stage23 checkpoint40 strengthened this warning on its selected Stage17 slice by a global mod-8 exclusion.

Revalidation under the literal Stage19 contract therefore confirms that `positive rank` or `Selmer beyond torsion` alone cannot certify a primitive integral second-face survivor, let alone an infinite target family. A new small/integral-point density theorem would be a new input and a different route.

## R60-03 / Q04 — generic K3/Kummer packet geometry

```text
ATTACK_ID=S1415-ATTACK-0204
SOURCE=stages/stage14/archive/tasks/14-X2/result.md
PRIOR_ROLE=Kummer/common-core packet rank collapse
VERDICT=DEAD_CONFIRMED
SCOPE=Q04_AS_AN_INDEPENDENT_STAGE23_ATTACK
```

The source proves a strong fixed-packet Pluecker rank-one collapse and `B^o(1)` short-vector mass, but explicitly does not prove the remaining whole-family packet multiplicity bound. Stage23 checkpoint40 subsequently opened the more literal Stage14-4ah/tH15/t64 chain, transferred physical height exactly (`H_M=d`), and sharpened the target receiver to the moving transverse Jacobi square-lift incidence.

Thus the older generic Q04 packet route is not an independent missing Stage23 weapon. Its useful geometry has been subsumed by the sharper Q06/t64 boundary, which still lacks a moving-family count theorem.

## R60-04 / Q05 — moving genus-one exact target receiver

```text
ATTACK_ID=S1415-ATTACK-0724
SOURCE=stages/stage15/15-6ai/result.md
PRIOR_ROLE=moving smooth genus-one two-quadric receiver
VERDICT=NEEDS_NEW_INPUT
STAGE19_POPULATION_COMPATIBILITY=PASS
```

The source classifies the exact low-core Stage15 survivor receiver as a smooth geometrically integral `(2,2)` genus-one curve in `P^3` throughout the physical chamber. Its pencil cross-ratio moves with the outer ratio, so it is not one fixed elliptic curve. On a populated fiber the physical survivor supplies a rational point, but that observation is circular for a lower-bound construction.

This receiver is directly compatible with Stage19 and remains mathematically useful. What is missing is a uniform moving-family theorem controlling rational/integral points in the original physical height and outer measure. Hence the route is not dead, but it cannot currently prove unboundedness or a positive-power lower bound.

## R60-05 / Q07 — normalized root-ratio / discrepancy route

```text
ATTACK_ID=S1415-ATTACK-0791
SOURCE=stages/stage15/15-6cx/result.md
PRIOR_ROLE=root-ratio discrepancy dispersion on exact normalized forms
VERDICT=NEEDS_NEW_INPUT
```

The source produces exact S/O root-ratio coordinates, bounded local branching, mixed norm/split algebra, and a discrepancy-first formulation. This maps cleanly to the Stage19 target and remains more precise than a generic local sieve.

However the route requires a whole-family discrepancy/dispersion theorem before absolute values. Pointwise local density and divisor-like root multiplicity do not give a target lower family or a fixed-power upper improvement. Checkpoint50 Q11 encountered the same uniformity wall from the fixed-prime side.

## R60-06 / Q08 — physical channel-gcd first-moment route

```text
ATTACK_ID=S1415-ATTACK-0771
SOURCE=stages/stage15/15-6cd/result.md
PRIOR_ROLE=physical-height-aware channel-gcd product first moment
VERDICT=DEAD_REASON_WEAKENED
```

At this source snapshot the route had one live global first-moment obstruction and one untested pointwise-domination possibility. Later Stage15 work materially changed the receiver: exact survivor reconstruction reduced fourth-variable completion to `B^o(1)`, while subsequent pointwise and complementary-switch tests showed that this multiplicity control alone does not create a density saving.

Thus the original parking reason is no longer the canonical description of the problem, but the hoped-for fixed-power gain was not recovered. The live obstruction migrated from a raw gcd-product moment to distribution on the reconstructed target graph.

## R60-07 / Q09 — modulus occupancy / pair-resultant energy

```text
ATTACK_ID=S1415-ATTACK-0804
SOURCE=stages/stage15/15-6dk/result.md
PRIOR_ROLE=centered modulus-occupancy bias receiver
VERDICT=NEEDS_NEW_INPUT
```

For an occupied switched modulus `q`, the source proves

\[
q\mid m^4-n^4
\]
and for two occupied graph nodes an exact orientation-blind square lock

\[
q^2\mid\mathcal R(x,y).
\]

But the safe unconditional occupancy second moment remains quadratic in graph mass, whereas the desired square-root-scale occupancy theorem is unproved. Divisor support controls how many moduli one node can occupy, not the density of graph nodes at one fixed modulus. This route is exact and target-compatible, but requires a genuinely centered distribution/energy theorem.

## R60-08 / Q10 — character large-sieve / p-adic occupancy route

```text
ATTACK_ID=S1415-ATTACK-0811
SOURCE=stages/stage15/15-6dr/result.md
PRIOR_ROLE=character large-sieve attack on centered occupancy operator
VERDICT=DEAD_CONFIRMED
SCOPE=CURRENT_CHARACTER_LARGE_SIEVE_INPUTS_ONLY
```

The source proves an exact centered Fourier/operator reformulation but certifies only `kappa=1`; no `kappa<1`, positive `delta`, or inverse-threshold `sigma` follows. The obstruction is substantive: completion phases move with modulus/orientation, so a standard fixed-coefficient large sieve is not legally applicable to the exact reconstructed graph. The source explicitly states this is a current-input negative certificate, not mathematical impossibility.

The preserved successor `PELL_UNIT_ORBIT_SECOND_NORM_CORRELATION` is a separate live route requiring new quantitative input; it is not silently promoted here.

## Revalidation summary

```text
SOURCE_LEVEL_BRANCHES_OPENED=8
MIN_REQUIRED=8
MIN_REQUIREMENT_SATISFIED=true
LOWER_BOUND_PRIORITY_USED=true
FINITE_ZERO_HIT_ALONE_USED_TO_CONFIRM_DEAD=false
R60_01=DEAD_CONFIRMED_GLOBAL_MOD16
R60_02=DEAD_CONFIRMED_SELMER_ONLY
R60_03=DEAD_CONFIRMED_AS_INDEPENDENT_ROUTE
R60_04=NEEDS_NEW_INPUT
R60_05=NEEDS_NEW_INPUT
R60_06=DEAD_REASON_WEAKENED
R60_07=NEEDS_NEW_INPUT
R60_08=DEAD_CONFIRMED_CURRENT_CHARACTER_INPUTS
REVIVED_BRANCH_PROMOTION_REQUIRED=false
SYNTHESIS_UNBLOCKED=true
```

The most useful new revalidation result is R60-01: the canonical Stage15 explicit linear-size exactly-two family is globally incompatible with an integral space diagonal by a mod-16 obstruction. This helps explain why a large ambient Stage18 lower family does not automatically produce any Stage19 lower law.