# Stage25-reentry-20 — Stage24 reattack / directional quarter-power synthesis

```text
TASK_ID=Stage25-u24-r002a
REENTRY_PHASE=20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=PROVED_CANDIDATE_FROM_AUDITED_FAMILIES_PLUS_NEW_CONE_ADAPTER
THEOREM_INTERFACE_VALID=true
REENTRY_RESEARCH_COMPLETE=false
STRONGER_RESULT_CANDIDATE=true
STRONGER_RESULT_PROVED=false
NEW_REUSABLE_WEAPON_CANDIDATE=true
NEW_REUSABLE_WEAPON_PROVED=false
```

## Authorization

Phase10 `Stage25-um-r001a` received hostile audit PASS in PR #1002 and merged as `5cb7dc8792faf575c1e21fce8166f094af6d7b14`. Phase20 is therefore authorized. Stage26 remains blocked.

## Current Stage24 surface

Under the common primitive/canonical physical contract

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad R=\sqrt{a^2+b^2+c^2}\le B,
\]

Stage18 and the post-Stage25 Stage19 interface give

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Thus the audited global Stage24 survivor envelope remains

\[
B^{-3/4}(\log B)^{-5}\ll \frac{N_2(B)}{M_2(B)}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

Phase20 does **not** improve this global exponent interval.

## New candidate: all three shared-edge directions have quarter-power mass

The detailed proof is in `directional-quarter-power.md`.

1. **canonical shared edge `b`** — the already-audited R501 cone `7/2<t<4` has `0<B<C<A`; the guaranteed faces `(A,C)` and `(B,C)` share raw edge `C`, which becomes canonical `b`. Hence `N_{2,b}(B)>>B^(1/4)`.
2. **canonical shared edge `c`** — audited R502 on `7/2<t<4` has `0<A<B<C` and exact family growth `Theta(B^(1/4))`; the same guaranteed-face pattern shares raw `C`, now canonical `c`. Hence `N_{2,c}(B)>>B^(1/4)`.
3. **canonical shared edge `a`** — re-use the audited R501 formulas on the fresh open cone `9/2<t<5`. Exact factor identities show `C<B` and `C<A`, so the shared raw edge `C` becomes canonical `a`. A coprime rational-height subset supplies `gg T^2` parameters, the audited height is `O(T^8)`, similarity fibers are at most eight, and the same fixed genus-seven third-face exception curve removes only finitely many rational parameters. Therefore `N_{2,a}(B)>>B^(1/4)`.

Candidate theorem:

\[
\boxed{N_{2,j}(B)\gg_j B^{1/4}\quad(j=a,b,c).}
\]

## Directional Stage24 survivor and interaction consequence

Stage24 already imports the audited Stage18 directional asymptotics

\[
M_{2,j}(B)\sim C_jB(\log B)^5,\qquad C_j>0,
\]
for all three shared-edge chambers. Since `N_{2,j}<=N_2`, the whole-family Stage19 upper also gives the directional upper. Therefore the candidate directional envelope is

\[
\boxed{
B^{-3/4}(\log B)^{-5}
\ll_j \frac{N_{2,j}(B)}{M_{2,j}(B)}
\ll_{\varepsilon,j}B^{-1/2+\varepsilon}(\log B)^{-5}
}
\]
for every `j=a,b,c`.

With the audited Stage16S ambient space-survival baseline `S_0(B)\asymp B^{-1}`, define

\[
J_{2,j}=\frac{N_{2,j}/M_{2,j}}{S_0}.
\]
Then

\[
\boxed{J_{2,j}(B)\gg_j B^{1/4}(\log B)^{-5}\to\infty}
\]
for all three directions. Thus, if audited, the positive-divergent Stage24 interaction is no longer merely global or one-chamber: it occurs in every shared-edge direction.

## Stage23 receiver consequence

A Stage19 object with shared canonical edge `a`, `b`, or `c` lies respectively in the raw pair-overlap channels

\[
A_{ab,ac},\qquad A_{ab,bc},\qquad A_{ac,bc}.
\]

Hence the same candidate implies

\[
\boxed{A_{ab,ac}(B)\gg B^{1/4}},\quad
\boxed{A_{ab,bc}(B)\gg B^{1/4}},\quad
\boxed{A_{ac,bc}(B)\gg B^{1/4}}.
\]

The middle bound was already current from R501. The `ac,bc` channel upgrades the older C17 `sqrt(log B)` lower, and the `ab,ac` quarter-power lower is new.

## What did not break

The true `N2` exponent remains unidentified. No strict whole-family sub-half upper was obtained. AR-023/AR-024 block transfer of savings merely from a shared inner kernel across different outer measures; AR-035 retains fixed-prime ordered limits and cannot be silently upgraded to a growing-modulus power saving; AR-028 forbids recharging already-consumed support/core factors. R503/R504/R505 remain audited external gates.

Therefore the phase20 search does **not** claim that the quarter-power exponent is optimal or that moving-family/growing-modulus uniformity has been solved.

## Propagation

This is theorem-changing if accepted, so it is not applied directly to frozen Stage19/23/24 artifacts before audit. One derived route is reserved:

```text
DERIVED_ROUTE=Stage25-um-r008a
ACTION=QUEUE_DERIVED_ROUTE
AFFECTED_STAGES=19,23,24
STATUS=QUEUED_UNTIL_PHASE20_AUDIT_PASS
```

Phase30 is not authorized until the phase20 audit and any required theorem-changing backflow synchronization are complete.

```text
REPO_REUSE_PREFLIGHT=PASS
STRONGEST_KNOWN_CHECK=PASS
FORMULA_SUBSTITUTION_ONLY=false
FRESH_COMPATIBLE_RECEIVER_MUTATION=R20-M01_R501_NEW_CANONICAL_A_CONE
GLOBAL_N2_EXPONENT_UPGRADED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
MOVING_FAMILY_UNIFORMITY_PROVED=false
GROWING_MODULUS_SIEVE_UNIFORMITY_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_REENTRY_PHASE=20
LIVE_DERIVED_ROUTES=NONE
QUEUED_DERIVED_ROUTE=Stage25-um-r008a
STAGE26_ALLOWED=false
MERGE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_EXPECTED_COMMAND=Stage25-reentry-audit
```
