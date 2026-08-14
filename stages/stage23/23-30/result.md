# Stage23-30 — asymptotic upper thinning and lower-gate attack

EVIDENCE_LEVEL=PROVED
CHECKPOINT=30
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Frozen interfaces

Stage23 compares the matched primitive/canonical populations under the common integral-space cutoff `R=d<=B`:

- `N1(B)`: exactly one integral face diagonal plus integral space diagonal;
- `N2(B)`: exactly two integral face diagonals plus integral space diagonal.

The audited source theorem is

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\qquad \kappa>0.
\]

The audited target theorem is only the upper bound

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

No matching target lower bound or true target exponent is imported.

## 2. Stage23 ratio theorem available now

Since the source has a positive leading constant, for sufficiently large `B`,

\[
N_1(B)\gg B(\log B)^3.
\]

Therefore for every fixed `epsilon>0`,

\[
\boxed{
\frac{N_2(B)}{N_1(B)}
\ll_\varepsilon
\frac{B^{-1/2+\varepsilon}}{(\log B)^3}
}.
\]

Choosing any fixed `epsilon<1/2` gives

\[
\boxed{N_2(B)/N_1(B)\to0}.
\]

Thus the Stage17 -> Stage19 transition is rigorously zero-density even though the true target exponent remains unresolved.

This is an upper thinning theorem only. It is not promoted to

\[
N_2/N_1\asymp B^{-1/2}(\log B)^{-3}
\]

and no ratio leading constant is claimed.

## 3. Required lower-bound / obstruction attack

Checkpoint20 did not stop at the inherited Stage19 upper bound. It materialized the Stage17-family slicing attack on the explicit infinite AR-039 family. On the one-parameter slice `n=1, m=t`, the second-face equations become generically:

- one degree-8 hyperelliptic square-value curve, genus 3;
- one degree-6 hyperelliptic square-value curve, genus 2 after removal of the obvious square factor.

The exact derivation and the strict integer scan are recorded in `stages/stage23/23-20/new-view-attack.md`. The scan `t=2 mod 14`, `2<=t<200000` found zero second-face hits on both branches.

This attack is Stage17-originating rather than a repeat of the Stage14/15 target-first squareclass route. It shows that a natural explicit infinite Stage17 family becomes a higher-genus integral-point problem when the second face is imposed.

The finite zero-hit scan is not a proof of nonexistence. Nor does the generic genus computation by itself prove that every Stage17 family has only finitely many Stage19 hits.

## 4. What remains open

The aggressive-search ledger currently supports:

```text
ZERO_DENSITY_TRANSITION_PROVED=true
RATIO_UPPER_BOUND=O_epsilon(B^(-1/2+epsilon)/(log B)^3)
TRUE_RATIO_ORDER_IDENTIFIED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
TARGET_UNBOUNDEDNESS_PROVED=false
INFINITE_PRIMITIVE_STAGE19_FAMILY_FOUND=false
POSITIVE_POWER_TARGET_LOWER_BOUND_FOUND=false
MATCHING_HALF_POWER_FAMILY_FOUND=false
HALF_POWER_INTRINSIC=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
```

`HALF_POWER_INTRINSIC=false` above means "not established as intrinsic", not "proved false".

## 5. Checkpoint boundary

The upper theorem is now mathematically sufficient to prove Stage23 zero density, but controller policy forbids treating that as completion of the exponent problem. The lower-bound / obstruction attack remains live for later checkpoints.

```text
UPPER_BOUND_REUSE=PASS
UPPER_BOUND_ONLY_COMPLETION=false
LOWER_BOUND_OR_OBSTRUCTION_ATTACK_REQUIRED=true
LOWER_BOUND_OR_OBSTRUCTION_ATTACK_STATUS=PASS_MATERIALIZED_AT_CHECKPOINT20
NEW_ANALYTIC_INPUT=false
FINITE_DATA_USED_AS_PROOF=false
NEXT_CHECKPOINT_AFTER_PASS=40
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
