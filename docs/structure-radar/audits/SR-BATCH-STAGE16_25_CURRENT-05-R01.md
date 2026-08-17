# StructureRadar audit — SR-BATCH-STAGE16_25_CURRENT-05-R01

```text
AUDIT_VERDICT=PASS
AUDITED_SUBMISSION_HEAD=8a6d9f5c55a7ef691eebf8b52c9ffda615b7740f
PR=1085
TASK=SR-CENSUS-STAGE16_25_CURRENT-01
SOURCES_REVIEWED=60
STRUCTURES_ADDED=3
STRUCTURES_UPDATED=4
STRUCTURE_CARRIER_SOURCES=30
DUPLICATE_OR_NO_DISTINCT_SOURCES=30
SEARCHES_COMPLETED=0
ARSENAL_DECISIONS=0
CODEX_REQUIRED=false
AUDIT_REQUIRED=false
MERGE_ALLOWED=true
```

## Independent audit scope

The audit fixed PR #1085 at submission head `8a6d9f5c55a7ef691eebf8b52c9ffda615b7740f` and checked:

- the seven canonical StructureRadar files changed by the main batch;
- all three new cards `SR-STR-156` through `SR-STR-158` against their theorem/audit carriers;
- the four existing-card updates `SR-STR-008`, `SR-STR-015`, `SR-STR-018`, `SR-STR-155` for overclaim, stale provenance and double charging;
- the 60-source progress accounting and unique task membership;
- generated queue/controller consistency and the exact-head StructureRadar controller CI.

## Mathematical verdicts

### SR-STR-156 — PASS

The Yoshida family adapter

`E_{1,s}: y^2=x(x-(2s)^2)(x+(s^2-1)^2)`

with `(a,b,c)=(2s,s^2-1,s^2+1)` is exactly the plus-sign Pythagorean/Frey family, and the accepted geometric generic Mordell-Weil rank is zero. The displayed fixed-fiber orbit and displayed positive-rank parameter sequence have quadratic logarithmic height in the orbit index, hence only `O(sqrt(log B))` / `O(sqrt(log X))` displayed members under bounded physical/rational height. The card correctly withholds any conclusion that all positive-rank specializations are sparse and leaves base change, multisection and quantitative exceptional-fiber routes open.

### SR-STR-157 — PASS

For target-fixed degree-two `phi in Q(u)`, the quadratic function-field extension has a unique Q-rational deck involution. Up to source `PGL2(Q)`, the audited complete descent splits into:

- split: `(A*u^2+B)/(C*u^2+D)`;
- nonsplit squareclass `d`: `(A*(u^2+d)+B*u)/(C*(u^2+d)+D*u)`.

The split reciprocal locus and nonsplit commuting-lift equations were rechecked. For the nonsplit deck `u -> d/u`, the lift criterion gives the genuine loci

`BD=4*d*A*C`

and

`D^2-B^2+4*d*(A^2-C^2)=0`,

while the third candidate `B^2+D^2=4*d*(A^2+C^2)` has discriminant `-(AD-BC)^2` and therefore no nondegenerate Q-rational involutive lift. The card correctly restricts the classification to commuting Q-rational lifts and does not claim a full Prym/rank-jump classification. The earlier strict even-subfamily completeness claim remains superseded.

### SR-STR-158 — PASS

For

`phi(u)=(u^2+4u-3)/(7-u^2)`,

the nontrivial deck is `-(u+7)/(u+1)` and the second involution `(5-u)/(u+1)` sends `phi` to `1/phi`. The second genus-one quotient is

`V^2=2*(x^4+8*x^3-64*x-64)`

with binary-quartic invariants `I=3072`, `J=0`; its Jacobian `y^2=x^3-82944*x` is Q-isomorphic to `E0:y^2=x^3-4*x`. The two audited invariant differential lines are distinct, giving the accepted generic pullback rank lower `rank E_phi(Q(u)) >= 2`. The card correctly refuses to turn the rank jump itself into a Stage19 population lower bound.

## Existing-card updates — PASS

- `SR-STR-008`: R501/R502 degree-eight primitive-height rigidity is family-specific support for the current quarter-power lower; no global upper or true-exponent claim is introduced.
- `SR-STR-015`: the expanded R504 toolkit matches the audited original-base rank-one/3P theorem, physical `P+2E_H` coset and parity certificate, `P+2R` fixed-class growth, known-rank-two aggregate upper, generic `Hom_K=0`, and exceptional Prym external gate. It explicitly withholds `Hom_Kbar=0`, exceptional-locus finiteness and any improvement over `N2(B)>>B^(1/4)`.
- `SR-STR-018`: Stage25 path identities remain exact count cancellation on matched populations, not probabilistic independence.
- `SR-STR-155`: checkpoint40 fixed-finite-curve refinement remains a moving-family quantifier firewall, not a global family count.

## Corpus/accounting verdict

The submitted task contains 60 distinct source IDs. Progress records exactly 30 structure-carrier sources and 30 duplicate/no-distinct sources, totaling 60 decisions. The batch adds exactly three cards (`156`–`158`) and updates exactly four existing cards (`008`, `015`, `018`, `155`). No literature searches or arsenal decisions are charged in this batch.

The final pre-audit-record submission diff contains only the seven canonical StructureRadar state files; temporary 10-source ledgers, helper workflow and handoff sentinel are absent.

## CI / lifecycle

Submission-head `StructureRadar controller` workflow id `335978592`, run `32069789428`, completed successfully on exact head `8a6d9f5c55a7ef691eebf8b52c9ffda615b7740f`.

This audit record is added on top of that audited submission. A fresh exact-head controller run must also succeed before merge. Main-lane self-audit is not used; this file is the independent audit record.

```text
FINAL_AUDIT_STATUS=PASS
MAIN_BATCH_STATUS=AUDITED_PASS
AUDIT_REQUIRED=false
MERGE_ALLOWED=true
NEXT_EXPECTED_ACTION=merge PR #1085; then StructureRadar-main-batch
NO_AUTO_MERGE=true
```
