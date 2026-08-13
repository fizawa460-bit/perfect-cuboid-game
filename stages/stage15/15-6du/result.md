# Stage15-6du — union exhaustive/blind audit after k=1 versus k>1 repair

Base: repaired Stage15-6ds/6dt. The survivor completion receiver is not uniformly Pell: it is the disjoint union
\[
\boxed{
\{k=1:\ \text{primitive factor-gap branch}\}
\ \cup\ 
\{k>1:\ \text{real-quadratic Pell branch}\}.
}
\]
The controller-required fresh `EXHAUSTIVE_VIEW_AUDIT` and `BLIND_REDISCOVERY` are therefore rerun on the **union**, with the physical measure and the single 6da completion charge preserved.

## 1. EXHAUSTIVE_VIEW_AUDIT on the repaired union

| Candidate | k=1 factor branch | k>1 Pell branch | Union verdict |
|---|---|---|---|
| Pointwise fourth-variable reconstruction | Primitive factor pair determines `V` in `B^{o(1)}` | Ideal/unit orbit determines `V` in `B^{o(1)}` | CONSUMED / EXACT; one 6da charge only |
| Second survivor condition | Second primitive factor-gap equation, postfilter | Second same-field Pell norm, postfilter | Genuine filter but no outer exponent from current pointwise inputs |
| Double eliminant / mixed linear factors | Cramer-equivalent to the two quadrics; explicit factor form | Recovered after Pell elimination | EQUIVALENT / CONSUMED as independent codimension |
| k=1 primitive factor-gap family average | Exact simultaneous divisor-gap condition | N/A | LIVE only as input to residual complementary switch; no standalone fixed-power theorem |
| Pell/Lucas recurrence theorem | N/A | Could rigidify unit indices but only inside `B^{o(1)}` fiber unless base-zero density is proved | EXTERNAL GATE, not current saving |
| Norm/divisor averaging | Divisor moments | Ideal/divisor moments | EXPONENT-NEUTRAL by AR-016 |
| Local valuations / fixed-prime sieve | Can reject factor-gap configurations | Can reject recurrence classes | LIVE QUALITATIVE BACKUP; AR-035 lacks same-measure effective adapter |
| Root-ratio character/Ramanujan dispersion | Applies before branch completion | Applies before branch completion | CURRENT-INPUT NEGATIVE CERTIFIED in 6dp–6dr |
| Orientation-blind pair resultant | Same | Same | CURRENT-INPUT NEGATIVE CERTIFIED for centered bias |
| Shared-support pair energy | Same | Same | DOMINATED for remaining one-point/complementary gate |
| Direct root-line lattice | Same | Same | LIVE LOCAL ENGINE only |
| Residual-cell complementary divisor switch | Factor gaps give explicit complementary data | Can switch channel divisors before Pell postfilter | LIVE / UNTESTED / SELECTED |
| External genus-one/height theorem | Degenerates to rational factor branch | Earlier quartic/twist route | PARKED external species; no exact current exponent adapter |

No candidate is removed merely because one branch degenerates or another branch is Pell.

## 2. k=1 branch audit: is there a distinct thinning mechanism?

For `k=1`, the two primitive factor equations are
\[
r_1s_1=(a^2MU)^2,
\qquad
r_2s_2=(c^2NU)^2,
\]
with the exact gap compatibility
\[
\frac{s_1-r_1}{2d^2N}
=
\frac{s_2-r_2}{2b^2M}.
\]
This presentation is reversible to `(P,Q,V)` and hence to the original two survivor quadrics. Since 6dg proves the double eliminants are Cramer-equivalent to those quadrics for `Delta!=0`, **there is no third algebraic constraint and no new pointwise dimension drop**.

The only potentially new family-level leverage is to switch one large factor/divisor against its complementary factor before the completion is attached. That is not a new independent route: it is exactly the untested **residual-cell complementary divisor switch** already preserved in 6cy. Therefore the `k=1` branch is classified as
\[
\boxed{\text{ALGEBRAICALLY EQUIVALENT, BUT SUPPLIES EXPLICIT INPUT TO THE RESIDUAL SWITCH}.}
\]
No fixed-power contribution is charged now.

## 3. k>1 branch audit: Pell negative certificate retained

For squarefree `k>1`, exact survivors are intersections of two rank-one unit orbits in `Q(sqrt(k))`. The second norm genuinely removes unit exponents, but all pointwise seed/unit multiplicity is already `B^{o(1)}`. Norm-ideal averaging, recurrence periodicity, and currently available local restrictions do not prove that a polynomial fraction of reconstructed bases/cores have zero legal intersection.

Thus the 6dt current-input negative certificate is retained unchanged:
\[
\boxed{\text{CURRENT k>1 PELL INPUTS DO NOT PROVE A SAME-MEASURE FIXED POWER}.}
\]
This is not an impossibility theorem.

## 4. BLIND_REDISCOVERY from the repaired union

Restart from the exact common data, without route names:
\[
HMNUV\le B,\qquad(q,H)=1,
\]
\[
a^4M^2U^2+d^4N^2V^2=kP^2,
\qquad
b^4M^2V^2+c^4N^2U^2=kQ^2,
\]
\[
kg^2\mid\Delta,
\qquad
\Delta=(abM)^4-(cdN)^4,
\]
plus the decorated S/O switched divisors with exact `phi(d_S)phi(e_O)` weights.

Both branches agree on one key fact: **after three residual variables are fixed, the fourth-variable completion is already only `B^{o(1)}`**. Therefore another pointwise completion theorem cannot yield the missing polynomial exponent. A fixed-power gain must act on the outer reconstructed base/channel-divisor population *before* the completion postfilter.

For `k=1`, the factor-gap equations visibly expose complementary factors. For `k>1`, the Pell description can remain a postfilter after the same channel divisors are switched. The common branch-independent internal move is therefore:

1. stay in the cross-gcd cell variables
   \[
   m=abM,\ n=cdN,\ r=acU,\ s=bdV;
   \]
2. preserve `(q,H)=1` and the decorated `(d_S,e_O)` assignment;
3. switch large residual channel divisors to exact complementary cofactors with multiplicity one;
4. only after that attach the branchwise completion postfilter:
   - primitive factor-gap when `k=1`,
   - Pell/unit orbit when `k>1`.

This blind derivation independently returns the same route selected before the audit repair.

## 5. Confirmed next internal route

Confirm
\[
\boxed{\text{RESIDUAL_CELL_COMPLEMENTARY_SWITCH_WITH_PELL_POSTFILTER}.}
\]
Here `PELL_POSTFILTER` is shorthand for the nondegenerate `k>1` branch only; the implementation must explicitly use a **factor-gap postfilter for `k=1`**. The route is therefore branch-aware even though the controller name is retained for continuity.

The next main task is to write the exact cell-normalized S/O residual forms and complementary cofactor variables for decorated `(d_S,e_O)`, prove the switch is multiplicity one under `(q,H)=1`, and test whether the switched family obtains either

- an inverse-threshold moment yielding `sigma>0`, or
- a one-sided/small-modulus fringe saving yielding `delta>0`,

before either branch's `B^{o(1)}` completion postfilter is attached.

A positive result must be on the same physical measure. A negative result must not turn the completion multiplicity into a fake saving.

## 6. Parking, split, and quantitative ledger

Parking remains **rejected** because the residual-cell complementary switch is materially distinct and still untested. Fixed-prime local thinning remains a qualitative backup.

The repaired union still has
\[
\delta>0:\ \text{unproved},
\qquad
\sigma>0:\ \text{unproved}.
\]
No polynomial overlap window is executable. There are not yet two independently quantified live obstructions, so the split trigger remains false.

## 7. Controller exit

```text
STAGE15_6_SUBSTAGE=6du
STAGE15_6DU_EXHAUSTIVE_VIEW_AUDIT=true
STAGE15_6DU_BLIND_REDISCOVERY=true
STAGE15_6DU_CORE_UNION_AUDITED=K1_FACTOR|KGT1_PELL
STAGE15_6DU_K1_FACTOR_BRANCH=ALGEBRAICALLY_EQUIVALENT_NO_FIXED_POWER
STAGE15_6DU_K1_FACTOR_ROLE=INPUT_TO_RESIDUAL_COMPLEMENTARY_SWITCH
STAGE15_6DU_KGT1_PELL_NEGATIVE_CERTIFICATE=CURRENT_INPUTS_ONLY
STAGE15_6DU_COMPLETION_MULTIPLICITY_CHARGED_ONCE=true
STAGE15_6DU_MIXED_NORM_LINEAR_ROUTE=EQUIVALENT_TO_DOUBLE_ELIMINANT
STAGE15_6DU_RESIDUAL_CELL_SWITCH=LIVE_UNTESTED_SELECTED
STAGE15_6DU_SELECTED_ROUTE=RESIDUAL_CELL_COMPLEMENTARY_SWITCH_WITH_PELL_POSTFILTER
STAGE15_6DU_BRANCH_AWARE_POSTFILTER=K1_FACTOR_GAP|KGT1_PELL
STAGE15_6DU_FIXED_PRIME_SIEVE=LIVE_QUALITATIVE_BACKUP
STAGE15_6DU_PARKING_ALLOWED=false
STAGE15_6DU_DELTA_PROVED=false
STAGE15_6DU_SIGMA_PROVED=false
STAGE15_6DU_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6DU_SPLIT_TRIGGER=false
STAGE15_6DU_AUDIT_REQUIRED=true
STAGE15_6DU_CODEX_REQUIRED=false
STAGE15_6DU_MERGE_ALLOWED=false
STAGE15_6DU_EXIT=FRESH_AUDIT_OF_BRANCH_SPLIT_NEGATIVE_CERTIFICATES_AND_RESIDUAL_SWITCH_SELECTION
```

Controller output:
```text
CURRENT_SUBSTAGE=Stage15-6du
NEXT_GATE=FRESH_AUDIT_OF_BRANCH_SPLIT_NEGATIVE_CERTIFICATES_AND_RESIDUAL_SWITCH_SELECTION
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
SPLIT_TRIGGER=false
```
