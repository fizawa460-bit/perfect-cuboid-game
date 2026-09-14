# Anthropic FLT source harvest for the perfect-cuboid Arsenal

Status: PROVISIONAL_EXTERNAL_SOURCE_SCREEN. Date: 2026-09-14.
Source repository: anthropics/fermats-last-theorem, exact commit `aa2d8b34692b16c70f699536de0d8e75b9a3e9ef`.
Arsenal baseline: `4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c`. No Stage controller, authority, audit status, credit, runkey, or workflow is modified.

## Evidence and inspection boundary

This is source inspection and conditional reuse design, NOT an independent verification of the upstream FLT proof. No Lean build, comparator replay, nanoda run, solver run, or cuboid computation was performed. The upstream README reports successful checks; those reports are not a local audit receipt. The external package uses Lean 4.33.1 and a pinned Mathlib dependency according to its README; no compatibility with this repository is assumed.

Read: [proof route](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/PROOF-PATH.md), [final axiom check](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/FinalCheck.lean), exact definitions of modularity/FreyPackage, selected theorem statements, and comparator challenge/solution/config. Large theorem wrappers were processed outside chat context to select named declarations; their proof bodies and transitive dependency closure were not audited. No recursive repository tree or full upstream checkout was used. Search misses were not treated as absence.

No upstream proof code is vendored. Upstream licensing/attribution remains at [LICENSE](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/LICENSE), [NOTICE](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/NOTICE), and [ATTRIBUTION](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/ATTRIBUTION.md). Future code extraction must preserve applicable notices and dependency licences.

Dedup scope: canonical Arsenal registry at the baseline and its registered promotion sources, with targeted terms Fermat, semistable, level lowering, comparator, axiom and Lean. S31-W01 supplies a genus-one quartic/elliptic adapter; S31-WF01 concerns Mordell-Weil completeness, not modularity. S30-WF02 supplies immutable layered certificate replay; the new workflow adds a separately authored formal target and allowed-axiom/constant-identity checking rather than replacing that procedure. No claim of exhaustive unregistered-branch discovery.

## FLT-PW01 — SEMISTABLE_MODEL_MODULARITY_ADAPTER

Maturity: PROVISIONAL. Type: conditional external theorem adapter. Priority: on-demand only; no active Stage assignment.

Input: an explicit integral Weierstrass model W over Z, nonzero discriminant, and proof that every prime dividing its discriminant does not divide c4. The upstream predicate is on the chosen equation, not an unchecked label attached to an elliptic curve. Also require an exact Q-isomorphism/variable change from the receiver's elliptic model to W, with all exceptional cases of the receiver map accounted for.

Output: modularity of W over Q in the upstream definition: existence of a positive level and a normalized weight-two cusp eigenform whose coefficients match Frobenius traces at the specified common good primes. This is not a rank bound, a rational-point list, a modular parametrization, or an L-function theorem.

Source: [modularity definition](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Definitions/Def_FLTPrelim_Modularity.lean), blob `9f2ad60d351dbc01aba577f418e2642524c7b997`; [named theorem](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_WeierstrassCurve_modularity_of_semistableModel.lean), blob `cf9263491f5a4c437773e6261b74c0e5fea58390`. Named declaration: `WeierstrassCurve.modularity_of_semistableModel`.

Cuboid use: after a receiver-specific genus-one-to-elliptic adapter (route first to S31-W01 where appropriate), this can supply one modular-method premise. Before implementation, exhibit the actual receiver, W, coordinate transformations, discriminant and c4, and prove the model condition. No such cuboid-specific instance is supplied here.

Critical limits: modular elliptic curves can have rational points. Modularity alone excludes no cuboid and provides no finite degree window for multibranch curves. Failure of this particular model condition does not imply that a better model is impossible, nor that the curve is nonmodular. No transfer to arbitrary non-semistable curves, surfaces, Picard vectors or all FULL178 terminals.

Acceptance gate: locked Lean dependency closure builds; target statement and axioms verified; exact cuboid-to-W forward implication and all hypotheses independently audited. Until then discovery routing only, zero pruning/receiver/endpoint credit.

## FLT-PW02 — LEVEL_TWO_CUSPFORM_CONTRADICTION_GATE

Maturity: PROVISIONAL. Type: conditional terminal obstruction. Priority: speculative, only after a concrete upstream receiver-to-form adapter exists.

Input: a proof that every object in one explicitly named cuboid receiver produces a NONZERO weight-two cusp form on Gamma0(2). A contradiction needs only a total forward implication for exclusion; a converse is required only if claiming an equivalence or classification. The receiver and all excluded degeneracies must be stated.

Output: that exact receiver is empty, conditional on the forward implication, because every such cusp form is zero.

Source: [zero-space theorem](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_ModularForm_S2_Gamma0_2_eq_zero.lean), blob `308964318e901e3f9395f40e4b9b389b4a0320c7`, declaration `ModularForm.S2_Gamma0_2_eq_zero`. The inspected statement quantifies over `CuspForm (CongruenceSubgroup.Gamma0 2) 2`.

Missing bridge: FLT-PW01 supplies neither level 2 nor nonzeroness at level 2. The upstream [level-lowering theorem](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_FreyPackage_level_lowering_to_two.lean), blob `c4612f847f4ed77c205d994a41d81ab189b97cb5`, takes a `FreyPackage`, modularity and an irreducibility premise. The [package definition](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Definitions/Def_FLTPrelim_FreyPackage.lean), blob `db1cdbbec434a118a917b33580fc8c81c4fff221`, already assumes a nonzero integer solution of a^p+b^p=c^p for prime p>=5, gcd normalization and parity conditions.

Cuboid face equations have exponent 2. They do not supply the prime-exponent FLT package. Constructing an elliptic curve with rational 2-torsion likewise supplies neither that package nor the required residual irreducibility/level lowering. An arbitrary semistable curve cannot be sent to level 2 by citing this Frey-specialized theorem.

Implementation gate: first prove a cuboid-specific residual-representation/conductor/ramification and level-lowering bridge, or another genuine route to the required nonzero form. This harvest supplies none of those bridges. No attempt to run a general Ribet theorem, assume rational torsion classification, or infer cuboid nonexistence is authorized. Stop at BLOCKED_MISSING_RECEIVER_TO_LEVEL2_ADAPTER if no bridge is available.

Dedup: distinct from existing finite congruence or MW-sieve filters; the certified target would be a modular-form space. The conditional logical implication is simple; the missing adapter, not the vanishing step, is the research burden. Zero current pruning or endpoint credit.

## FLT-WF01 — FORMAL_TARGET_IDENTITY_AND_AXIOM_GATE

Maturity: PROVISIONAL workflow; not a mathematical selector. Potential consumers: any future Lean-formalized cuboid lemma or endpoint, not an automatic rewrite of existing Python certificates.

Reusable procedure:
1. Pin the toolchain, dependencies and proof source; use S30-WF02 for immutable evidence handling.
2. Write an independent trusted target using standard mathematical definitions. For a cuboid endpoint, include positive edges and all three face-square conditions plus the body-square condition; do not substitute an easier named predicate. Decide primitive versus all cuboids explicitly.
3. Separate the target specification from the solution imports. Prove the exact target in the solution environment, and validate the adapter if its representation differs.
4. Check the target's transitive axiom dependencies against an explicit allowed set; reject sorryAx or other extra axioms. A grep for sorry is not sufficient.
5. Use a comparator-style check of the theorem and constants against the independently written target. A successful proof of a redefined predicate is not a proof of the intended cuboid proposition.
6. Optionally replay with an independent kernel; retain checker versions, patches, logs and exact scope. Do not treat an unrun optional checker as successful.
7. Report separately statement identity, kernel acceptance, semantic interpretation and repository promotion. None replaces the Stage-specific audit/endpoint gate.

Concrete source: [FinalCheck](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/FinalCheck.lean), blob `3ffbd60b8f9736f5569e4dd4774701a114d18266`, guards the final theorem's axiom list. [Challenge](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/verification/comparator/Challenge.lean), [Solution](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/verification/comparator/Solution.lean), and [config](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/verification/comparator/config.json) separate target/solution and permit propext, Quot.sound, Classical.choice. The challenge deliberately contains sorry as an unproved specification; this must not be imported as solution evidence. Comparator config has enable_nanoda=false; nanoda is a separate upstream checking path, not established by that config.

Validation performed here: source wiring/definitions inspected only. No Lean installation, build or checker replay. Future whole-package verification is a high-resource task and requires its own compute/storage preflight and authorization; do not attach it to ordinary PR updates.

Nonduplication: this is a narrow formal-language extension alongside S30-WF02, not another generic source-lock or CI card. It cannot certify current Stage32 numeric certificates without a faithful formal encoding and proof.

## Rejected automatic transfers

FLT itself does not rule out exponent-two cuboid equations. Frey-specific irreducibility is not general Mazur torsion/isogeny classification. Level lowering in this package is not a general theorem for all cuboid-associated representations. No descent/Kummer card was added merely on namespace/name matches: existing squareclass/descent cards already cover that search direction, and exact transferable new contracts were not established in this bounded pass.

## Credit and execution firewall

All three entries are PROVISIONAL, source-inspected only, not locally kernel-verified or hostile-audited. Cards do not alter live ownership or priority, authorize compute, release any Stage dependency, or change mathematical authority. No new finite pruning, full-population closure, effectivity, receiver, theorem, endpoint, perfect-cuboid existence/nonexistence or merge credit.
