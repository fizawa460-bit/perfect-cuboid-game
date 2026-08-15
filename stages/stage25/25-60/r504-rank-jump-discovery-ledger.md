# Stage25-60 R504 full-split / nonsplit rank-jump discovery ledger

STATUS=AUDITED_COMPLETE
ROUTE=R504
CHECKPOINT=60

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=R504_HOSTILE_AUDITED_Q_DEGREE2_DESCENT;R504_TWIST_DESCENT;R504_BC1_BC2_NO_RANK_JUMP;R504_GROWING_MULTIPLE_CLOSURE;R504_BC3_BC5_SYMBOLIC_WORK;S1415_ATTACK_0522;S1415_ATTACK_0544;S1415_ATTACK_0583;S1415_ATTACK_0748
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=FULL_SPLIT_AND_NONSPLIT_ANALYSES_WERE_EXPLICITLY_LEFT_REQUIRED_BY_HOSTILE_AUDIT_AND_THE_NEW_NONSPLIT_EQUATION_IS_NOT_THE_FROZEN_STAGE14_DIRECTION_FAMILY
POPULATION_ADAPTERS_PROVED=NONE_FOR_NEW_RANK_JUMP;PHYSICAL_STAGE19_ADAPTER_REMAINS_OPEN
```

## Required discovery block

```text
DISCOVERY_CHECKPOINT=60
SEARCHED_PATHS=R504_Q_DEGREE2_DESCENT;R504_TWIST_DESCENT;R504_BASE_CHANGE_BOUNDARY;STAGE14_15_BOUND_ATTACK_LEDGER_PARTS;STAGE14_T13;STAGE14_T15;STAGE14_T43;STAGE15_6BG
SEARCH_TERMS=FULL_SPLIT;NONSPLIT_SQUARECLASS;GENUS3;V4_QUOTIENT;E0_FACTOR;ISOGENY;TWISTED_KUMMER;RANK_JUMP;PHYSICAL_HEIGHT
STRUCTURAL_SIGNATURES=TARGET_FIXED_SOURCE_PGL2Q;NONSPLIT_DECK;GENUS3_HYPERELLIPTIC_COVER;V4_ELLIPTIC_QUOTIENTS;E0_ISOGENY_FACTOR
DEPENDENCY_NEIGHBORS=R504_ORIGINAL_RANK1;R504_Q_DEGREE2_DESCENT;S1415_ATTACK_0522;S1415_ATTACK_0544;S1415_ATTACK_0583;S1415_ATTACK_0748
CANDIDATES_FOUND=FULL_SPLIT_RECIPROCAL;NONSPLIT_COMMUTING_LIFTS;NONSPLIT_N2_EXPLICIT_E0_QUOTIENT;NON_BIELLIPTIC_PRYM
CANDIDATES_ACCEPTED=FULL_SPLIT_RECIPROCAL_LOCUS_CLASSIFICATION;NONSPLIT_COMMUTING_LIFT_CLASSIFICATION;EXPLICIT_NONSPLIT_GENERIC_RANK_JUMP
CANDIDATES_REJECTED_WITH_REASON=FULL_SPLIT_J_NONZERO_DOES_NOT_PROVE_NONISOGENY;STAGE14_T43_OLD_FROZEN_DIRECTION_NONISOGENY_RESULT_NOT_A_BLOCK_FOR_NEW_EXACT_NONSPLIT_EQUATION;STAGE15_6BG_HEIGHT_MEASURE_MISMATCH_BLOCKS_DIRECT_STAGE19_COUNT_PROMOTION
POPULATION_ADAPTERS_PROVED=NONE_FOR_NEW_RANK_JUMP
DISCOVERY_LEDGER_STATUS=COMPLETE
```

## Stage14/15 attack-ledger binding required by the new-mechanism claim

The hostile audit searched the bound attack ledger and opened every `review_required=true` source used below.

- `S1415-ATTACK-0522` / Stage14-t13 — **accepted as structural predecessor**. It proves that an exact degree-eight squarefree branch equation naturally gives a genus-three cover and explicitly points to involutions/quotients as the next attack. It does not contain the present nonsplit map or rank jump.
- `S1415-ATTACK-0544` / Stage14-t15 — **accepted as structural predecessor and scope warning**. It gives a V4 quotient skeleton with two elliptic factors plus a genus-three factor, while warning that quotient points alone do not satisfy the physical square-lift/height gate. This is why the present generic rank jump is not promoted to a Stage19 count.
- `S1415-ATTACK-0583` / Stage14-t43 — **rejected as a blocker, retained as an isogeny warning**. Its frozen direction family found no degree-2 isogenous direction pairs and left higher-degree isogenies unclassified. The current R504 map is a materially new explicit nonsplit base-change equation and produces a second quotient Q-isomorphic to E0, so this is a legitimate new mechanism rather than reuse of the old frozen exception set.
- `S1415-ATTACK-0748` / Stage15-6bg — **rejected as a direct population adapter**. Its Kummer-type support receiver is measured in the physical diagonal height `Y=S` and carries moving rational-denominator issues. It therefore cannot convert the present function-field rank jump into a Stage19 population lower without a new exact height/primitive/multiplicity adapter.

```text
ATTACK_LEDGER_SEARCH=PASS
ATTACK_IDS_REVIEWED=S1415-ATTACK-0522,S1415-ATTACK-0544,S1415-ATTACK-0583,S1415-ATTACK-0748
ATTACK_IDS_ACCEPTED_STRUCTURALLY=S1415-ATTACK-0522,S1415-ATTACK-0544
ATTACK_IDS_REJECTED_AS_DIRECT_ADAPTER=S1415-ATTACK-0583,S1415-ATTACK-0748
REVIEW_REQUIRED_SOURCE_READS=PASS
NEW_MECHANISM_DISCOVERY_AUDIT_EVIDENCE=COMPLETE
```

## R504 paths and executed sublanes

Searched/reused directly:
- `stages/stage25/25-60/r504-q-degree2-complete-descent.md`
- `stages/stage25/25-60/r504-q-degree2-descent-audit-recheck.md`
- `stages/stage25/25-60/r504-twist-descent.md`
- `stages/stage25/25-60/r504-base-change-boundary.md`
- `stages/stage25/25-60/r504-exceptional-base-change-search.md`

At entry:
```text
FULL_SPLIT_GENERAL_RECIPROCAL=LIVE
NONSPLIT_COMMUTING_LIFTS=LIVE
NONSPLIT_N2_EXCEPTIONAL_FACTOR=UNTESTED
NONCOMMUTING_PRYM=LIVE
```

Executed:
1. full split reciprocal-lift locus and complementary quartic invariants;
2. nonsplit commuting-lift classification and square obstructions;
3. explicit map `phi(u)=(u^2+4u-3)/(7-u^2)`;
4. second involution `epsilon_2=(5-u)/(u+1)` and quotient quartic `2*(x^4+8*x^3-64*x-64)`;
5. `I=3072`, `J=0`, Jacobian Q-isomorphic to `E0:y^2=x^3-4x`;
6. hostile differential-eigenspace check proving independence of the inherited and new elliptic quotient maps.

## Scope boundary

The full split reciprocal/commuting-involution locus is classified. On its checked complementary quotients, `J != 0` rules out Q-isomorphism to the `j=1728` curve `E0`; it does **not** rule out an elliptic curve merely Q-isogenous to `E0`. The split Prym/isogeny residual therefore remains live.

No finite census or numerical rank scan is proof here. No Stage19 exponent upgrade is submitted because the explicit second rational-function section and the physical height/primitive/exactly-two/multiplicity adapter remain absent.

```text
FINITE_DATA_USED_AS_PROOF=false
R504_GENERIC_RANK_JUMP_PROVED=true
R504_EXPLICIT_SECOND_SECTION_MATERIALIZED=false
R504_FULL_SPLIT_NO_E0_ISOGENY_PROVED=false
R504_FULL_SPLIT_PRYM_ISOGENY_RESIDUAL=OPEN
R504_GLOBAL_QUARTER_LOWER_UPGRADE_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
```
