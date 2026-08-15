# Stage25-60 R504 full-split / nonsplit rank-jump discovery ledger

STATUS=COMPLETE_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=R504_HOSTILE_AUDITED_Q_DEGREE2_DESCENT;R504_TWIST_DESCENT;R504_BC1_BC2_NO_RANK_JUMP;R504_GROWING_MULTIPLE_CLOSURE;R504_BC3_BC5_SYMBOLIC_WORK
REUSE_MATCH_STATUS=MATCHED_R504_SAME_ELLIPTIC_SURFACE_AND_SOURCE_EQUIVALENCE
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=FULL_SPLIT_AND_NONSPLIT_ANALYSES_WERE_EXPLICITLY_LEFT_REQUIRED_BY_HOSTILE_AUDIT
POPULATION_ADAPTERS_PROVED=NO_NEW_POPULATION_ADAPTER_YET;GLOBAL_LOWER_UNCHANGED
```

## SEARCHED_PATHS

- `stages/stage25/25-60/r504-q-degree2-complete-descent.md`
- `stages/stage25/25-60/r504-q-degree2-descent-audit-recheck.md`
- `stages/stage25/25-60/r504-twist-descent.md`
- `stages/stage25/25-60/r504-base-change-boundary.md`
- `stages/stage25/25-60/r504-exceptional-base-change-search.md`
- prior Stage14 Kummer/isogeny receiver PRs already materialized in the preceding R504 round

## SEARCH_TERMS

```text
full split degree-two normal form
nonsplit squareclass deck involution
commuting reciprocal lift obstruction
k -> -k
k -> 1/k
k -> -1/k
second elliptic quotient
E0 factor
rank jump
```

## STRUCTURAL_SIGNATURES

- target fixed / source `PGL2(Q)` equivalence;
- split deck `u -> -u`;
- nonsplit deck `u -> d/u`;
- fixed constant curve `E0:y^2=x^3-4x`;
- pullback untwisting cover `C_phi:s^2=phi(u)^4+1`;
- rank controlled by Q-homomorphisms `J(C_phi)->E0` under the already audited twist descent.

## LIVE_ROUTE_CANDIDATES

At start of this round:

```text
FULL_SPLIT_GENERAL_RECIPROCAL=LIVE
NONSPLIT_COMMUTING_LIFTS=LIVE
NONSPLIT_N2_EXCEPTIONAL_FACTOR=UNTESTED
NONCOMMUTING_PRYM=LIVE
```

Executed outcomes:

```text
FULL_SPLIT_GENERAL_RECIPROCAL=CLOSED_WITH_SYMBOLIC_CERTIFICATE
NONSPLIT_COMMUTING_LIFTS=CLOSED_WITH_SYMBOLIC_CERTIFICATE
NONSPLIT_N2_EXCEPTIONAL_FACTOR=POSITIVE_HIT_EXPLICIT_RANK_JUMP
NONCOMMUTING_PRYM=STILL_LIVE_BUT_NOT_NEEDED_TO_ESTABLISH_RANK_JUMP
```

## SUBLANES_EXECUTED

1. **Full split**: exact factorization of the reciprocal lift locus in `(A,B,C,D)` and exact complementary binary-quartic invariants.
2. **Nonsplit lift descent**: transport the three Q-rational reduced involutions of the inherited elliptic quotient through `m(t)` and compute the lift square obstruction.
3. **N2 positive hit**: identify branch trace `-10/7`, norm `1`, squareclass `-6`, then construct the explicit Q-map
   `phi(u)=(u^2+4u-3)/(7-u^2)`.
4. **Second quotient**: compute exact invariant functions for `epsilon_2=(5-u)/(u+1)` and obtain the quotient quartic `2*(x^4+8*x^3-64*x-64)`.
5. **Jacobian check**: binary quartic invariants `I=3072`, `J=0`, Jacobian coefficient `-82944=-4*12^4`, hence Q-isomorphic to `E0`.

## DISCOVERY BOUNDARY

No finite census or numerical rank scan is used as proof. The new theorem is algebraic and symbolic.  No Stage19 exponent upgrade is submitted because an explicit second section and its physical-height adapter have not yet been materialized.

```text
FINITE_DATA_USED_AS_PROOF=false
R504_GENERIC_RANK_JUMP_PROVED=true
R504_EXPLICIT_SECOND_SECTION_MATERIALIZED=false
R504_GLOBAL_QUARTER_LOWER_UPGRADE_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
```
