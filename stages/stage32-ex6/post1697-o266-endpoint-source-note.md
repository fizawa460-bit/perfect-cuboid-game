# Stage32EX6 post-1697 — O266 endpoint source lock and decision

Status: **EXPLORATORY EXACT BOUNDED RESULT**. This note does not modify Stage32 MAIN authority.

## Question

For the exact recovered V6 class `g1-d186`, can the upper endpoint `O=266` be excluded purely from endpoint saturation plus the retained local/global constraints?

## Source locks

1. Stage32 post-1473 multibranch Beauville odd-branch note, exact historical head `131d7869c145563d3c9ee1116a9def9e671a6a63`, path `stages/stage32/residual-32-01-production/post1473-specific-class-multibranch-beauville-odd-branch-wall.md`, blob SHA1 `cb20a9b287430c2e238f79d3151500c262905468`.
2. Stage32 post-1484 modular-factor note, exact historical head `0a888aa5195c558e2104c30a4351067ed1828287`, path `stages/stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-source-note.md`, blob SHA1 `deeecac5599f3b542b445cd87c2070dae488bc85`.
3. Consolidated post1648AN A1 strict-transform feasibility note, exact consolidation head `82b551d92ad2ef1a86f8303758c7aa17c0a6d960`, path `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`, blob SHA1 `512fcc70afb1acf16956fd4b7a2b9b935a052150`.
4. Consolidated post1648AR two-factor slack note, same consolidation head, path `stages/stage32/residual-32-01-production/post1648ar-two-factor-slack-minimal-branches-source-note.md`, blob SHA1 `da9b6ba755b8bd43d5b342d5540053caeb218f57`.
5. Hostile-audited post1500 Rosati repair note, historical head `a004dbc8e02fa57fb4c1d374710849aa571dae8e`, path `stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md`, blob SHA1 `b0ea281eae453929c292059a919bc1f68b3080b3`.
6. Consolidated post1648AT conductor source note, consolidation head `82b551d92ad2ef1a86f8303758c7aa17c0a6d960`, path `stages/stage32/residual-32-01-production/post1648at-intermediate-quotient-blowup-conductor-source-note.md`, blob SHA1 `59849336b9e49610c00709b58989d17b9df1c6a7`.

The AN/AR/AT inputs are used only as already-produced retained/consolidated evidence. EX6 does not promote them into Stage32 MAIN.

## Exact meaning of O and the upper endpoint

For a hypothetical integral genus-one V6 carrier with normalization `N`, the exceptional pullback is

`D_E = sum_P m_P P`,

with every `m_P` a positive integer and

`sum_P m_P = e = C.E = 266`.

Define

- `B = #supp(D_E)`;
- `O = #{P : m_P is odd}`;
- `S1 = #{P : m_P=1}`.

Thus every point counted by `O` consumes at least one unit of exceptional mass, so

`O <= B <= e = 266`.

This is the exact reason `266` is the endpoint in this fixed-V6 branch-count problem.

## Forced endpoint equalities

Assume `O=266`. Since the total mass is also `266`, every one of the 266 odd contacts must have multiplicity exactly one and there can be no additional positive even contact. Hence

- `B=266`;
- `S1=266`;
- every exceptional contact has `m_P=1`;
- at each exceptional curve `E_j`, the number of normalization preimages is exactly the fixed intersection multiplicity `M_j=C.E_j`;
- the exact positive support remains 47 nodes, and AN's fixed vector has 38 nodes with `M_j>1`, so those 38 are multibranch at this endpoint.

A crucial non-consequence is that `m=1` does **not** force every branch to have FSM type `(A,B)=(1,1)`. The source-locked local model has `m=min(A,B)`. Thus endpoint branches may also have `(A,B)=(1,2k+1)` or `(2k+1,1)`, `k>=1`, with node-boundary contact `k`. The endpoint forces unit exceptional multiplicity, not zero boundary contact.

## Local realizability: no contradiction

AN already supplies an explicit local endpoint witness stronger than necessary: at each met node, take exactly `M_j` branches of the FSM-minimal type `(A,B)=(1,1)` and choose pairwise distinct nonzero exceptional landing parameters `lambda`.

This realizes

- exactly 266 normalization preimages over the nodes;
- every exceptional contact odd of multiplicity one;
- exact nodewise exceptional masses;
- pairwise separated strict transforms on each exceptional curve;
- forced exceptional-locus delta contribution `0`.

The remaining V6 strict-transform genus defect `472` is locally compatible with a smooth-locus singularity budget, as witnessed in AN. Therefore endpoint saturation alone does not create a local contradiction.

## Exact two-factor slack at the endpoint

AR defines

`t = e-N = sum(a-1)`

for the `N` node branches, where `a=min(A,B)` is exceptional contact. At `O=266` the endpoint equalities give `N=266` and `t=0`.

The two exact factor identities therefore specialize to

`52 = q81_node + eta81 + rho81`,

`28 = q105_node + eta105 + rho105`,

with all terms nonnegative. Here `q*_node` is node-boundary contact, `eta*` is excess smooth-boundary contact multiplicity, and `rho*` is ramification away from the six special fibres.

These equations remain feasible. For example the scalar residual choice

- `q81_node=0, eta81=0, rho81=52`;
- `q105_node=0, eta105=0, rho105=28`

is consistent with all nonnegativity identities and with AN's all-minimal local endpoint witness. This is not a construction of global factor maps; it proves only that the retained scalar Hurwitz identities do not contradict the endpoint.

The usual AR consequence also remains: at most 80 endpoint node branches can be nonminimal, so at least 186 of the 266 branches are FSM-minimal. At O266 this is a necessary bound, not an exclusion.

## Rosati/correspondence check

The post1500 repair retains O-independent fixed-class/deck arithmetic

- `Gamma^2=15806`;
- `sigma(Gamma)=1204`;
- `Q(T)=602`;
- `p_a(Gamma)=8090`;
- pair-map birationality for the fixed q'=4 class.

For general O, the connected Beauville pullback has

`g(Y)=1+O/2`.

Therefore at O266,

`g(Y)=134`,

`delta_Gamma = p_a(Gamma)-g(Y) = 8090-134 = 7956`.

This does not change the fixed Rosati value `Q=602`; the O210 shorthand `Q=8586-delta_Gamma` is not an O-independent formula because the constant there already substituted `g(Y)=106`. The general identity is

`Q = 8691 - O/2 - delta_Gamma`,

which at O266 gives `602 = 8691-133-7956`.

The retained post1500 Weierstrass lower bound `delta_Gamma>=1924` is therefore nonexcluding at O266. The retained D4⊕D4 representation/nonexclusion of Q602 is unchanged.

## Conductor check

AT's exact factor-pair conductor decomposition is structural and O-independent at the fixed V6 class level. It explains the required conductor rather than imposing an upper bound that O266 violates. It therefore supplies no endpoint contradiction without additional member-level landing/jet data.

## Decision

`O266_ENDPOINT_NOT_CLOSED`

The endpoint is much more rigid than generic O: it forces complete splitting of the exceptional mass into 266 unit odd contacts and fixes `B=S1=266`. However, the retained local model explicitly realizes that endpoint profile, the exact two-factor slack identities still have residual solutions, and the corrected Rosati/conductor data remain compatible.

The missing input is genuinely member-level/global. A future O266 re-entry needs at least one of:

1. a source-locked restriction on exceptional landing parameters/tangent collisions that forbids the AN endpoint witness;
2. a global jet/separation bound preventing the required smooth-locus genus defect together with 266 unit node branches;
3. a stronger global coupling of the two factor maps that bounds `q*_node`, `eta*`, or `rho*` beyond the current nonnegative slack identities;
4. an independent correspondence/conductor inequality whose O266 value exceeds the exact available defect.

Absent such an input, descending to O264 is not authorized by EX6.

## Firewalls

- `O266_ENDPOINT_EXCLUDED=false`.
- `O266_ENDPOINT_NOT_CLOSED=true`.
- Stage32 MAIN O210/Q602/V6 authority is unchanged.
- Q602 survivors `[73,97,235]` are unchanged.
- No O212+ MAIN advance follows.
- No Stage32 closure, endpoint, receiver, theorem, or Perfect Cuboid credit follows.
- No merge is authorized by this result.
