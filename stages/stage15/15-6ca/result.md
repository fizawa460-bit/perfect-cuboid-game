# Stage15-6ca — structural channel-gcd / physical-height gate

Base: Stage15-6bz. Main-batch work unit 3.

Elementary size bounds give
\[
G_S\le \min(m^2+n^2,|r^2-s^2|),\qquad
G_O\le \min(|m^2-n^2|,r^2+s^2),
\]
but their product is not pointwise bounded by `B^o(1)` and these inequalities alone do not yield a `B^{1+o(1)}` first moment under the physical height.

The exhaustive internal-route check therefore leaves one live non-equivalent obstruction: prove an averaged structural estimate for the product `G_S G_O` after the primitive gcd normalization. No second independent obstruction is exposed, so the controller split trigger is not met.

Arsenal/Stage14 trigger-signature check: the closest signatures are angular-gcd splitting/divisor switching (t75/t78) and projective root-line spacing (t76). They are useful guidance but were proved under fixed-U/fixed-tag packets and cannot be imported as a whole-family theorem. No exact Stage14 weapon currently discharges this receiver.

Frozen next gate:
\[
\sum_{P\in A(B)}G_S(P)G_O(P)\ll B^{1+o(1)}
\]
via a physical-height-aware divisor switch / gcd-moment estimate, or a stronger pointwise structural domination if discovered.

```text
STAGE15_6_SUBSTAGE=6ca
STAGE15_6CA_INTERNAL_ROUTE_SEARCH=EXHAUSTED_FOR_CURRENT_NORMAL_FORM
STAGE15_6CA_ARSENAL_SIGNATURES=t75,t76,t78
STAGE15_6CA_ARSENAL_DIRECT_DISCHARGE=false
STAGE15_6CA_SPLIT_TRIGGER=false
STAGE15_6CA_AUDIT_REQUIRED=true
STAGE15_6CA_CODEX_REQUIRED=false
STAGE15_6CA_EXIT=FRESH_AUDIT_OF_PHYSICAL_GCD_PRODUCT_MOMENT_GATE
```