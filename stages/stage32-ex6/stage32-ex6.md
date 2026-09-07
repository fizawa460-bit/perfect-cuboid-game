# Stage32EX6 — O266 endpoint attack

Status: **O266_ENDPOINT_NOT_CLOSED — STOPPED PENDING NEW ENDPOINT INPUT**. Stage32 MAIN remains frozen at its current O210/Q602/V6 frontier. EX6 does not change MAIN authority, current survivors, or advancement state.

## Current result

The first O266 pass is complete.

Exact endpoint semantics:

- `D_E=sum_P m_P P`, `sum m_P=e=266`;
- `O=#{P:m_P odd}`;
- hence `O<=B<=266`;
- at `O=266`, necessarily `B=S1=266` and every exceptional contact has multiplicity `m_P=1`.

This endpoint profile is **not excluded** by the retained data. Post1648AN already gives an explicit local witness with `M_j` pairwise-separated minimal branches at each met node. The exact two-factor endpoint slack remains feasible, and the corrected Rosati/conductor identities remain nonexcluding.

Decision certificate:

- `stages/stage32-ex6/post1697-o266-endpoint-contract.json`
- `stages/stage32-ex6/post1697-o266-endpoint-source-note.md`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_o266_endpoint_contract.py`

A future re-entry requires genuinely new member-level landing/jet information, a stronger simultaneous two-factor constraint, or an independent correspondence/conductor inequality. EX6 does not descend to O264 by guesswork.

## Latest bounded re-entry result — degree-113 rank-4 local wall

A bounded search of the other Stoll–Testa rank-4 genus-5 fibrations found a unique last-four fibration class with V6 degree `113`. Its six split `G3` bad fibers use 24 exceptional curves carrying total V6 exceptional mass `140`.

The first re-entry only established that the naive implication

`O=266 => R_rank4 >= 266`

was unsupported. The sharpened local analysis now shows more: on each of those 24 split exceptional components there are exactly two `G3` attachment points, while a unit endpoint contact landing at any other point of that reduced fiber component is unramified for the rank-4 map. The retained AN endpoint model has enough landing-parameter freedom to place all 140 split-exceptional unit contacts away from those finite attachment loci.

Therefore the universal local adapter

`every O-contact contributes >=1 to degree-113 rank4 ramification`

is **locally false** in the retained endpoint model. This does not construct a global V6 carrier and does not exclude O266; it removes one naive route to the Riemann–Hurwitz contradiction.

The quantitative budget is now also fixed. Once those 140 locally-zeroable contacts receive zero forced ramification, only `266-140=126` O-contacts remain. A degree-113 genus-one map has exact total ramification `226`, so contradiction needs a forced lower bound at least `227`. Charging at most one unit to every remaining contact gives only `126`, leaving an exact deficit of `101`. Thus the bounded route “zero credit on the 140 locally avoidable contacts + no independent ramification lower bound + at most one forced unit on each remaining contact” is `NUMERICALLY_INSUFFICIENT`.

The machine-readable re-entry threshold is now explicit: continuation through this same contact-sum architecture must supply at least `101` additional forced ramification units beyond the one-unit remaining-contact ledger, by extra ramification multiplicity, recovered positive forced credit from the 140 locally-zeroable contacts, an independent ramification source, or a different simultaneous-fibration/correspondence inequality.

Retained files:

- `stages/stage32-ex6/post1697-rank4-degree113-adapter-wall.md`
- `stages/stage32-ex6/post1697-rank4-local-unramified-contact-wall.md`
- `stages/stage32-ex6/post1697-rank4-local-unramified-contact-contract.json`
- `stages/stage32-ex6/post1697-rank4-degree113-one-unit-budget-wall.md`
- `stages/stage32-ex6/post1697-rank4-degree113-one-unit-budget-contract.json`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_rank4_local_unramified_contact_contract.py`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_rank4_degree113_one_unit_budget_contract.py`

A useful future rank-4 re-entry must now force actual/global V6 landing points into attachment or critical loci, force more than one ramification unit at enough remaining contacts, produce an independent lower bound away from the O-contact ledger, or avoid the per-contact ramification premise entirely.

## Latest bounded re-entry result — FSM16 modular-tensor near miss

Freitag–Salvati Manni Theorem 3.1 gives `d<=176+16g` for curves whose normalization map is bijective. For genus one this is `d<=192`, so the fixed V6 degree `d=186` already survives the published theorem by `6`.

Using the proof itself and replacing the universal 48-node pole count by the exact 47-node positive support would give `d<=188` in a counterfactual bijective-normalization case. This is still nonexcluding by `2`, and the actual O266 population is not bijective: it has `B=266` normalization points over the exceptional divisor.

The same proof architecture extends branchwise to the safe inequality

`d <= 16g - 16 + 4B`.

At `g=1,B=266`, this gives only `d<=1064`.

The modular cusp congruences sharpen the internal threshold. A branch has positive tensor pole budget only at the minimal cusp pair `(a1,a2)=(4,4)`, contributing at most `8k`; the next allowed sum is at least 16 and gives no positive pole. If `S_cusp` is the number of `(4,4)` branches, degree `186` and genus one require `S_cusp>=47`. Thus this tensor route would exclude the V6 carrier if a global/member-level theorem forced

`S_cusp <= 46`.

No branch-level adapter from these FSM16 cusp parameters to the Stage32 AN local FSM pair `(A,B)` is currently source-locked, so the two notions are not identified here.

Retained files:

- `stages/stage32-ex6/post1697-fsm16-modular-tensor-multibranch-wall.md`
- `stages/stage32-ex6/post1697-fsm16-modular-tensor-multibranch-contract.json`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_fsm16_modular_tensor_multibranch_contract.py`

Decision: `FSM16_MODULAR_TENSOR_O266 = NUMERICALLY_NONEXCLUDING`.

## Purpose

Attack the opposite endpoint of the currently retained fixed-V6 O-range by studying the hypothetical `O=266` population first.

The first question is deliberately narrow:

> Does the exact endpoint condition `O=266` force enough equalities / saturation / incidence rigidity to exclude that endpoint?

EX6 does not assume in advance that `O=266` means “all exceptional mass is used” in any stronger sense than the source-locked definition of `O` proves. The first leaf must recover the exact definition of `O`, the proof of the retained upper endpoint `266`, and every inequality whose equality is forced at `O=266`.

## Target outcomes

### Endpoint exclusion

`O266_ENDPOINT_EXCLUDED`

A replayable proof that the fixed Stage32 V6 genus-1 population with `O=266` is empty under the exact retained hypotheses.

### Endpoint remains open

`O266_ENDPOINT_NOT_CLOSED`

A precise blocker stating which endpoint equalities are insufficient and what genuinely new input would be required. This is a valid stopping point for EX6; it does not authorize descending to lower O values by guesswork.

## Roadmap

### EX6-00 — source-lock the endpoint

Recover from retained Stage32 authority:

- the exact definition and quantification domain of `O`;
- why the relevant fixed-V6 range has upper endpoint `266`;
- the exact relation, if any, between `O`, exceptional mass `266`, branch/contact counts, normalization fibres, and local multiplicities;
- which statements are equalities and which are only inequalities.

Exit: a compact endpoint contract with no heuristic identification hidden inside it.

### EX6-01 — equality/saturation consequences at O=266

Take every source-locked inequality involving `O` and determine what becomes equality when `O=266`.

Materialize all forced consequences, for example only where actually justified:

- support saturation;
- multiplicity saturation;
- disappearance of slack terms;
- forced local branch/contact types;
- forced distribution across the 48 ambient nodes or other loci;
- parity or orbit constraints.

Exit: an exact list of endpoint-only constraints.

### EX6-02 — local realizability test

Test whether the endpoint constraints can be realized simultaneously in the exact local surface/curve models already retained for Stage32.

The goal is not to re-run O210 diagnostics blindly. Use only consequences that become stronger specifically because `O=266` is an endpoint.

Exit: either a local contradiction, or an explicit residual endpoint ledger.

### EX6-03 — global coupling test

Couple the surviving endpoint ledger to the fixed V6 global invariants and any already-audited applicable geometry: adjunction/genus, factor degrees, ramification, conductor, exceptional incidences, Picard/intersection constraints, and finite symmetry data.

Avoid promoting a necessary condition into exclusion. A contradiction must apply to the entire `O=266` population under the same hypotheses.

Exit: `O266_ENDPOINT_EXCLUDED` or a sharply identified surviving endpoint configuration/blocker.

### EX6-04 — endpoint decision

If `O=266` is excluded, package an exact certificate/verifier and stop. Do **not** automatically claim anything about `O=264` or lower values.

Only after an audited O266 exclusion should a separate follow-up ask whether the proof has a monotone or near-endpoint form that descends to `264`, `262`, ... .

If O266 is not excluded, record `O266_ENDPOINT_NOT_CLOSED` and stop EX6 until genuinely new endpoint input appears.

## Scope boundary

- Stage32 MAIN stays at the existing O210/Q602/V6 frontier.
- Existing Q602 survivors `[73,97,235]` are untouched.
- O266 exclusion, if obtained, is only an endpoint result until a separate argument proves extension to lower O.
- No automatic O212+ MAIN advance, Stage32 closure, receiver/theorem/endpoint credit, or Perfect Cuboid conclusion follows from EX6 alone.
- No merge is implied by creating or advancing this lane.
