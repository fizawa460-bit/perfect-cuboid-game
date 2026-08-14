# Stage21-50 fresh re-audit

AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=COMMITTED
UNSYNCED_AUDIT_STATE=NONE
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=60
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true

## Re-audit finding

The prior FAIL correctly identified that the frozen AR-039 lower bound alone did not prove that the entire constructed family was negligible in `N_1(B)`.

The bounded repair supplies the missing upper-side count from the original Stage11 two-parameter construction. For admissible `m>n`,

\[
p=m^2+n^2,\qquad d=\frac{p^2+1}{2}=\frac{(m^2+n^2)^2+1}{2}.
\]

Thus `d<=B` implies

\[
m<(2B)^{1/4}.
\]

Dropping congruence and coprimality restrictions only enlarges the parameter set, so the number of candidate pairs is at most

\[
\sum_{m<(2B)^{1/4}}(m-1)=O(B^{1/2}).
\]

The construction is injective: the cuboid determines `d`, hence `p` from `p^2=2d-1`; the primitive Pythagorean triple with legs `a,b` and hypotenuse `p` then determines the Euclid parameters `m>n` uniquely. Therefore

\[
N_{\rm AR039}(B)=O(B^{1/2}).
\]

Combined with the audited AR-039 lower bound,

\[
N_{\rm AR039}(B)=\Theta(B^{1/2}).
\]

Using the matched E-1e denominator,

\[
M_1(B)\sim\frac{3}{4\pi^2}B^2\log B,
\]

we get

\[
\frac{N_{\rm AR039}(B)}{M_1(B)}=\Theta(B^{-3/2}(\log B)^{-1}).
\]

Since audited Stage17 gives `N_1(B)~const*B(log B)^3`, it follows that

\[
N_{\rm AR039}(B)=o(N_1(B)).
\]

Hence the entire known AR-039 family is asymptotically negligible in the Stage17 population and cannot explain the full Stage21 `(log B)^2` enhancement. The bulk mechanism remains open.

```text
REPAIR_ROUTE=AR039_ELEMENTARY_UPPER_COUNT
AR039_COUNT=Theta(B^1/2)
AR039_NEGLIGIBLE_IN_N1=true
OPEN_GATE=LOG_SQUARED_ENHANCEMENT_BULK_MECHANISM_UNRESOLVED
CHECKPOINT30_40_REOPENED=false
```
