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

The sharpened local analysis shows that on each of those 24 split exceptional components there are exactly two `G3` attachment points, while a unit endpoint contact landing at any other point of that reduced fiber component is unramified for the rank-4 map. The retained AN endpoint model has enough landing-parameter freedom to place all 140 split-exceptional unit contacts away from those finite attachment loci.

Therefore the universal local adapter

`every O-contact contributes >=1 to degree-113 rank4 ramification`

is **locally false** in the retained endpoint model. This does not construct a global V6 carrier and does not exclude O266; it removes one naive route to the Riemann–Hurwitz contradiction.

The quantitative budget is fixed. Once those 140 locally-zeroable contacts receive zero forced ramification, only `266-140=126` O-contacts remain. A degree-113 genus-one map has exact total ramification `226`, so contradiction needs a forced lower bound at least `227`. Charging at most one unit to every remaining contact gives only `126`, leaving an exact deficit of `101`.

Retained files:

- `stages/stage32-ex6/post1697-rank4-degree113-adapter-wall.md`
- `stages/stage32-ex6/post1697-rank4-local-unramified-contact-wall.md`
- `stages/stage32-ex6/post1697-rank4-local-unramified-contact-contract.json`
- `stages/stage32-ex6/post1697-rank4-degree113-one-unit-budget-wall.md`
- `stages/stage32-ex6/post1697-rank4-degree113-one-unit-budget-contract.json`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_rank4_local_unramified_contact_contract.py`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_rank4_degree113_one_unit_budget_contract.py`

A useful future rank-4 re-entry must force actual/global V6 landing points into attachment or critical loci, force more than one ramification unit at enough remaining contacts, produce an independent lower bound away from the O-contact ledger, or avoid the per-contact ramification premise entirely.

## Latest bounded re-entry result — FSM16 adapter correction and route dominance

Freitag–Salvati Manni Theorem 3.1 gives `d<=176+16g` for curves whose normalization map is bijective. For genus one this is `d<=192`, so the fixed V6 degree `d=186` survives the published theorem by `6`. The counterfactual exact-47-node version still gives only `d<=188`, and the actual O266 multibranch branchwise bound is only `d<=1064`.

The prior EX6 leaf incorrectly stated that the FSM16 cusp parameters lacked an adapter to the retained Stage32 AN pair. Post1648AN/AR already source-lock

`a1=4*A`, `a2=4*B`, `m=min(A,B)`,

and identify the unique FSM-minimal Stage32 type `(A,B)=(1,1)`. Hence

`FSM16 (a1,a2)=(4,4) <=> Stage32 FSM-minimal (A,B)=(1,1)`.

At O266, `t=0`, and the two exact factor slack identities imply

`q81_node<=52`, `q105_node<=28`.

Every nonminimal endpoint branch consumes at least one unit from one of those two node-boundary ledgers, so

`#nonminimal<=80`,

and therefore

`S_cusp=#(4,4) branches >=186`.

The FSM16 tensor cardinality argument only requires `S_cusp>=47` for degree 186 genus one. Its lower bound is therefore weaker than the retained Stage32 lower bound by `139` branches.

Consequently any future strategy whose sole new output is an upper bound on `S_cusp` is strictly dominated by the existing AR minimal-branch inequality: AR would already close against `S_cusp<=185`, whereas the tensor-cardinality argument requires the much stronger `S_cusp<=46`.

Decision:

`FSM16_STAGE32_BRANCH_ADAPTER = SOURCE_LOCKED`;

`FSM16_S_CUSP_CARDINALITY_ROUTE = DOMINATED_BY_AR_MINIMAL_BRANCH_BOUND`.

Retained files:

- `stages/stage32-ex6/post1697-fsm16-modular-tensor-multibranch-wall.md`
- `stages/stage32-ex6/post1697-fsm16-modular-tensor-multibranch-contract.json`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_fsm16_modular_tensor_multibranch_contract.py`

Do not loop on the old `S_cusp<=46` counting target.

## Latest bounded re-entry result — FSM16 weighted node-divisor pole debt

The FSM16 proof gives the exact signed local divisor order of its pulled-back tensor at a node branch:

`ord_branch(T)=(a1+a2-16)k`.

At O266, `m=min(A,B)=1`. Writing the other exponent as `1+2b`, with `b=|A-B|/2>=0`, gives

`a1+a2=8+8b`

and therefore

`ord_branch(T)=8(b-1)k`.

Thus a minimal `(A,B)=(1,1)` branch contributes a pole `8k`, a `{1,3}` branch is neutral, and `b>=2` contributes a node zero.

The retained AR semantics identify the exact sum of `b` over the 266 endpoint node branches with

`q81_node+q105_node`.

Hence the total signed node divisor is

`D_node = 8(q81_node+q105_node-266)k`.

At O266 the two factor slack identities give `q81_node+q105_node<=80`, so

`D_node <= -1488k`.

Equivalently, the endpoint forces a net node pole debt of at least `1488k`.

With

`E=eta81+rho81+eta105+rho105>=0`,

the two exact slack identities sharpen this to

`q81_node+q105_node=80-E`,

so

`D_node=-(1488+8E)k`.

Because the normalization has genus one, the pulled-back tensor divisor has total degree zero. Therefore the complementary non-node signed divisor must satisfy the exact identity

`D_nonnode=(1488+8E)k >=1488k`.

This is now the useful FSM16 re-entry threshold. A future global/member-level theorem closing this architecture must force an upper bound

`D_nonnode <1488k`

or, retaining the slack variable, the sharp inequality

`D_nonnode <(1488+8E)k`.

No such upper bound is presently source-locked. The published FSM16 proof supplies lower bounds on zeros, not the required upper bound on the non-node signed divisor. Therefore this weighted calculation is a quantitative blocker/re-entry target, not an endpoint exclusion.

Decision:

`FSM16_WEIGHTED_NODE_DIVISOR = EXACT_POLE_DEBT_THRESHOLD_OBTAINED`.

Retained files:

- `stages/stage32-ex6/post1697-fsm16-weighted-node-divisor-wall.md`
- `stages/stage32-ex6/post1697-fsm16-weighted-node-divisor-contract.json`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_fsm16_weighted_node_divisor_contract.py`

Useful continuation should now target an actual upper bound on the non-node tensor divisor, a stronger replacement tensor, or an independent global inequality. Do not return to cusp-cardinality counting unless it brings genuinely new member-level information.

## Latest bounded re-entry result — FSM16 f-divisor residual split

The published FSM16 proof gives an independent canonical-divisor contribution inside the nonnode budget. Their auxiliary modular form `f` can be chosen nonzero along the curve and at all 48 nodes, and its zero divisor is a `2k`-multiple of the canonical divisor. Since the retained V6 carrier degree is `d=186`, the pullback `f`-zero divisor has exact degree

`2kd = 372k`.

This is entirely nonnode. Subtracting it from the previously retained exact nonnode signed budget gives

`D_res_nonnode := D_nonnode - deg(div(f)|_N)`

and hence

`D_res_nonnode = (1116+8E)k >=1116k`.

Thus the published `f` zeros explain only `372k` of the required `(1488+8E)k` nonnode compensation. The residual `1116+8E` units per `k` must come from the remaining tensor factors in signed divisor degree.

This is an independent sharpening because the `372k` degree comes from the canonical divisor class in FSM16, not by replaying the Stage32 factor Riemann–Hurwitz `q/eta/rho` ledger.

The residual is a signed divisor difference; no pointwise effectiveness or globally descended `T/f` tensor is claimed.

A future closure in this architecture now needs an independent member-level upper bound

`D_res_nonnode < (1116+8E)k`,

or the uniform sufficient bound

`D_res_nonnode <=1115k`,

or an independent support/landing obstruction carrying the same force. Reusing the same factor-RH ledger as the alleged upper bound is not independent.

Decision:

`FSM16_F_DIVISOR_CONTRIBUTION_PER_K = 372`;

`FSM16_RESIDUAL_NONNODE_MINIMUM_PER_K = 1116`;

`FSM16_F_ZEROS_ALONE_CLOSE_ENDPOINT = false`.

Retained files:

- `stages/stage32-ex6/post1697-fsm16-f-residual-divisor-wall.md`
- `stages/stage32-ex6/post1697-fsm16-f-residual-divisor-contract.json`
- verifier: `stages/stage32-ex6/verify_stage32_ex6_fsm16_f_residual_divisor_contract.py`

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
