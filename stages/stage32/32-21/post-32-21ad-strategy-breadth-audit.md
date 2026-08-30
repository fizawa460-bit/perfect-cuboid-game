# Stage32 post-32-21ad strategy breadth audit

Status: `EXHAUSTIVE_VIEW_AUDIT_AND_BLIND_REDISCOVERY_ACTIVE_ROUTE_SELECTED`

Scope: strategy selection after audited 32-21ad FULL178 zero-prune checkpoint, merged by PR #1466 at `d8fa4446af9bcc36b34d2421733333f0c74d23d5`.

This is a breadth audit, not a claim that all mathematical viewpoints have been exhausted.

## Trigger

The exact receiver is the unresolved anti-fixed lift behind the `679337` FULL178 projected rank-2 survivors. Three lightweight post-checkpoint reformulations strengthened the available anti-fixed norm information on deterministic row shard 0/16 without invalidating a single existing witness:

- 32-21ae: actual residue-specific 32-21aa penalty instead of the 128-class coset minimum. The penalty was strictly stronger at `45982 / 51462` existing witnesses, but all `51462` witnesses survived.
- 32-21af: exact two-coordinate modular lower bounds from the top 12 aa-active retained coordinates, 66 positive-definite pairs. `16378 / 16384` projection classes improved; `51081 / 51462` witnesses received a stronger penalty; all `51462` survived.
- 32-21ag: coordinate Cauchy norms restricted from the 61-dimensional slice kernel to the true 59-dimensional Reynolds anti-fixed kernel `ker N`. Sixty of 64 coordinate dual norms strictly decreased, `16283 / 16384` classes improved, and `48543 / 51462` witnesses received a stronger penalty; all `51462` survived. The smallest projected-margin / strengthened-penalty ratio was exactly `161`.

The same essential receiver therefore survived repeated norm-penalty reformulation, and the Cycle Exploration Safety Protocol requires deliberate broadening rather than automatic escalation to triples, larger coordinate subsets, or a 59-dimensional CVP.

## Blind pass from the exact receiver

The blind pass starts only from:

- an exact projected fixed part `p=P(x)` parameterized by rank-2 integers `(u,v)`;
- `q=x-p` lies in the true Reynolds anti-fixed space `ker N`, rank 59;
- every original integral Picard lift has `x=p+q`, `x^2=p^2+q^2` with `q^2<=0`;
- all 140 original halfspace pairings must be nonnegative integers;
- the fixed projection retains only the stabilizer averages of those 140 inequalities;
- projected integrality is exact, but `anti_fixed_lift_not_solved=true` remains the explicit missing receiver.

Generated materially distinct lenses:

1. **Original-halfspace integrality functionals on `ker N`.** For each original halfspace functional `ell_i(x)=<x,E_i> in Z`, the fixed part gives rational `ell_i(p)`. Hence `ell_i(q)=integer-ell_i(p)` has an exact modulo-one condition. Compute the dual norm of `ell_i` on the true anti-fixed kernel and use exact Cauchy lower bounds. This restores information from the original 140 functionals rather than only retained basis coordinates.

2. **Orbitwise integer-composition constraints.** Inside each stabilizer orbit, the 140 nonnegative integer pairings have a fixed orbit sum determined by `p`. Their deviations from the orbit average sum to zero and belong to a finite integer-composition family when the orbit sum is small. Multi-functional exact bounds could use this structure rather than independent coordinate residues.

3. **Exact affine anti-fixed fiber lattice.** Because the fixed-image basis is the exact column lattice of `N`, every projected state has an integral preimage. The remaining problem can be written as an affine rank-59 lattice point problem with a negative-definite norm cap and 140 linear halfspaces. Exact SNF/LLL/dual-certificate approaches could attack this fiber without materializing the 27-digit terminal family.

4. **Targeted full anti-fixed closest-vector norm.** An exact 59-dimensional CVP would give the strongest pure norm-only necessary condition for a fixed projection class. It is potentially decisive but currently has no audited cost/algorithm justification and remains blocked as an immediate production route.

5. **Modular reductions of the affine fiber plus original halfspaces.** Reduce the anti-fixed affine lattice and selected halfspace constraints modulo small primes/powers before any norm enumeration. This can expose local integrality obstructions that averaging and real/continuous QP cannot see.

6. **Higher-dimensional retained-coordinate Cauchy/CVP bounds.** Triples or larger subsets can strengthen 32-21af, but the representative evidence shows a minimum margin/penalty ratio of 161 even after the true anti-fixed one-coordinate restriction. This lens remains mathematically distinct but has lower expected information gain than restoring original halfspace integrality.

## Comparison with repository history and classification

`LIVE`

- `ORIGINAL_140_HALFSPACE_FUNCTIONAL_INTEGRALITY_ON_TRUE_ANTIFIXED_KERNEL`: cheap, exact, directly restores discarded original constraints, and needs no heavy run-key. Selected as the next active route (32-21ah).

`UNTESTED`

- `ORBITWISE_NONNEGATIVE_INTEGER_COMPOSITION_BOUND`.
- `AFFINE_ANTIFIXED_FIBER_MODULAR_SIEVE`.
- `AUDITED_AFFINE_ANTIFIXED_FIBER_LATTICE_SOLVER`.
- `HIGHER_DIMENSIONAL_TRUE_ANTIFIXED_MULTI_FUNCTIONAL_BOUND`.

`EQUIVALENT`

- `PROJECTED_PREIMAGE_INTEGRALITY_ALONE`: no new filter. The rank-2 projected lattice already uses an exact basis of the integer column lattice of `N`, so every projected lattice state has an integral preimage before anti-fixed halfspace/norm conditions are imposed.

`DOMINATED`

- `REARM_32_21AD_COSET_MINIMUM_FULL178_CENSUS_WITHOUT_SEMANTIC_CHANGE`.
- `BLIND_512M_OR_1B_LEGACY_PREFIX_DFS_ESCALATION`.

`BLOCKED`

- `59D_ANTIFIXED_CVP_AS_IMMEDIATE_PRODUCTION`: blocked until a separate exact algorithm/cost justification and compute/storage preflight exists.
- `ANY_NEW_HEAVY_PRODUCTION_IN_THIS_RECONNAISSANCE_PR`: no dedicated fresh run-key and no heavy release.

## Selected next gate

32-21ah tests the 140 original halfspace *integrality functionals* on `ker N` first. For a projection residue `r=Nx mod 64`, and an integral pairing row `ell_i`,

`ell_i(q) = integer - ell_i(p)`, with `p=Nx/64`,

so the fractional class of `ell_i(q)` is determined exactly by `ell_i(r)/64 mod Z`. If `nu_i` is the exact squared dual norm of `ell_i` restricted to the positive norm `-q^2` on `ker N`, then

`-q^2 >= dist(ell_i(r)/64, Z)^2 / nu_i`.

Take the maximum over all 140 functionals, together with the already derived true anti-fixed retained-coordinate bound. This is a safe necessary lower bound, uses exact rational arithmetic, and does not solve a 59-dimensional CVP.

A surviving old witness proves that slice survives this strengthening. A failing old witness is only a candidate for further exact `(u,v)` search; it is not a prune until all relevant rank-2 integer pairs are exhausted.

## Safety fields

`CYCLE_ROUTE_STATUS=PASS_NEW_GATE_FROM_STRONGER_VIEW`

`CYCLE_ACTIVE_RECEIVER=ORIGINAL_140_HALFSPACE_FUNCTIONAL_INTEGRALITY_ON_TRUE_ANTIFIXED_KERNEL`

`CYCLE_LIVE_CANDIDATES=1`

`CYCLE_UNTESTED_CANDIDATES=4`

`CYCLE_EXHAUSTIVE_VIEW_AUDIT=true`

`CYCLE_BLIND_REDISCOVERY=true`

`CYCLE_SPLIT_TRIGGERED=false`

`CYCLE_PARKING_AUDIT_COMPLETE=false`

`CYCLE_NEW_VIEW=Use the modulo-one integrality of all 140 original halfspace pairings as anti-fixed dual-norm constraints, rather than only retained-coordinate residues.`

`CYCLE_NEW_VIEW_SOURCE=BLIND`

No theorem, receiver, route-color, numerical-row, existence, or nonexistence credit changes in this audit. `UNKNOWN != UNSAT` remains explicit.
