# N101 — exact indexed-terminal Picard leaf compression redesign

## Verdict

`BLOCKED_WITH_EXACT_REDESIGN`: the repository already contains exact downstream quotient/compression machinery, but the current retained indexed-terminal layer does not contain a source-locked adapter proving that the downstream Picard leaf/effectivity predicate factors through those quotient states. No FULL178 terminal may therefore be merged or pruned on that basis yet.

This is an algorithmic/interface result only. It grants no FULL178 numerical, theorem, receiver, route, or hostile-audit credit.

## Reuse scan

The current indexed terminal family is the exact eleven-coordinate Stage32 pairing-prefix family `x0,...,x10`. `compressed_terminal_family.py` source-locks its prefix filters and symbolic count, while `compressed_terminal_indexer.py` gives exact random access/rank-unrank to the same terminal set. The retained production state records the exact FULL178 terminal population

`688101306360803751427719294`

and explicitly says that terminal-set semantics are preserved while numerical Picard leaf checks are incomplete.

Three existing downstream routes are directly relevant:

1. `direct_picard_reynolds_rank2_quotient_class_map.py` gives an exact Smith-coordinate map `y=(y0,y1,y2,u,v) -> (B*T*y) mod 64` into the complete `16384`-element Reynolds projection image. It also constructs the exact quotient by the free `(u,v)` subgroup. Its own certificate marks this as representation-only and says the map does not by itself prune.
2. `build_stage32_21ad_full178_antifixed_coset_census.py` applies the audited anti-fixed coset bound to FULL178 `(row,e,a)` continuous-KKT surviving slices. Its semantics explicitly record `terminal_family_materialization_run=false`, so it does not certify a map from an indexed eleven-coordinate terminal to the quotient class/coset used by the evaluator.
3. `diagnose_stage32_21am_quotient_dp.py` is an exact residual-quotient dynamic program. Its certificate says Smith reconstruction is exact, the reduction preserves all mod2/mod4/mod8 constraints, and vacuous-orbit upper bounds are preserved. But it is a representative sampled downstream diagnostic; it records `full_affine_pairing_fiber_feasibility_solved=false`, `full178_numerical_credit=false`, and `terminal_family_materialization_run=false`.

Therefore the missing component is not another rank/unrank codec and not another generic finite quotient. It is the semantic bridge from the indexed terminal coordinates to a sufficient downstream Picard state.

## Exact redesign

Let `T(e,d)` be the canonical indexed terminal set and let `P(t)` be the complete downstream numerical Picard leaf/effectivity decision for a terminal `t in T(e,d)`.

Introduce a source-locked finite signature `sigma(t)`. A valid implementation must prove both conditions below.

### S1 — semantic sufficiency

There is an exact function `F` such that `P(t) = F(sigma(t))` for every admissible terminal in the current FULL178 family. Equivalently, two terminals may be merged only after proving that equal signatures imply identical downstream Picard feasibility semantics (or an identical exact transition multiset if more downstream DP remains).

The signature may reuse the existing rank-2 Reynolds quotient/coset data and the 21am residual quotient state, but it must also carry every affine-pairing/slack datum on which the final predicate depends. A projection class or positive norm penalty alone is not sufficient.

### S2 — prefix transition closure

For each indexed-prefix state and each next local coordinate choice, the child signature must be computable exactly from the parent signature plus that local choice: `sigma(child) = Delta(sigma(parent), local_choice)`.

No terminal leaf may need to be materialized merely to reconstruct information omitted from `sigma`.

### Quotient-DP algorithm

Once S1 and S2 are source-locked, replace terminal enumeration by a multiplicity map `M_k : signature -> nonnegative integer` at prefix depth `k`. Start with multiplicity one at the empty prefix. For every legal local choice, apply the exact transition `Delta` and add the parent multiplicity to the child signature. Equal child signatures are merged by integer addition. At terminal depth evaluate `F` once per distinct signature and weight the result by its exact multiplicity.

### Preservation certificate

The proof is induction on prefix depth. At depth zero the multiplicity map represents exactly the singleton empty prefix. If `M_k` is the exact count of prefixes in each signature class, exact enumeration of the legal local choices and exact transition closure S2 gives the exact count of depth-`k+1` prefixes in every child class. Hence the terminal multiplicities partition the canonical terminal set exactly. S1 then makes one evaluation of `F` per terminal signature semantically identical to evaluating `P` on every represented terminal.

A production certificate must additionally assert and replay `sum_sigma M_terminal(sigma) = 688101306360803751427719294` for the full manifest, together with deterministic hashes of the transition/signature tables.

## Exact blocker

No retained source inspected by N101 supplies `sigma` or `Delta` from the current indexed terminal representation. In particular, the current terminal layer exposes the eleven pairing-prefix values, whereas the reusable quotient evaluator is keyed by downstream Smith/rank-2 coordinates `(d,e,a,u,v)` and later affine-pairing information. The existing 21ad and 21am routes explicitly did not materialize the terminal family and therefore cannot be treated as proof that the final predicate factors through their quotient state.

Consequently:

- exact indexed streaming/random access: retained PASS;
- downstream Reynolds quotient compression: retained exact machinery exists;
- safe reduced FULL178 terminal-family cardinality: **not established**;
- merging terminals by the `16384` Reynolds projection classes alone: **not authorized**;
- blind terminal enumeration or renewed prefix DFS: **not authorized by N101**.

The number `16384` is a quantified downstream projection-state envelope, not a claimed reduction of the `688101306360803751427719294` indexed terminals.

## Reopen condition

Reopen N101 only when a source-locked adapter (or equivalent prefix recurrence) is available with all four items:

1. exact `indexed terminal/prefix -> Picard sufficient signature` construction;
2. proof that every downstream Picard leaf/lift/effectivity predicate factors through that signature;
3. exact multiplicity conservation replay against the canonical 27-digit FULL178 count;
4. a certified distinct-signature count materially below the terminal count (or an exact pruning count).

At that point the quotient-DP construction above is directly implementable and its semantic-preservation proof is already fixed by S1/S2 plus multiplicity conservation.

## Sources inspected

- `stages/stage32/residual-32-01-production/state.json`
- `stages/stage32/residual-32-01-production/compressed_terminal_family.py`
- `stages/stage32/residual-32-01-production/compressed_terminal_indexer.py`
- `stages/stage32/residual-32-01-production/full178-prefix-indexed-compression-main-checkpoint.json`
- `stages/stage32/residual-32-01-production/direct_picard_reynolds_antifixed_coset_penalty.py`
- `stages/stage32/residual-32-01-production/direct_picard_reynolds_rank2_quotient_class_map.py`
- `stages/stage32/residual-32-01-production/build_stage32_21ad_full178_antifixed_coset_census.py`
- `stages/stage32/residual-32-01-production/diagnose_stage32_21am_quotient_dp.py`
