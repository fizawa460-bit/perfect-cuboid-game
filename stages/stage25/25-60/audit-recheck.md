# Stage25 checkpoint60 hostile re-audit — R502 repair

Status: **PASS — previous FAIL repaired; checkpoint60 remains iterative**

## Scope

This re-audit is deliberately narrow. The previous checkpoint60 hostile audit already accepted the causal cross-ratio theorem, the R501 primitive-height rigidity theorem, and the R504 generic non-torsion moving section. The only failed item was the unsupported removal of R502 from the live route set.

The repair selected the stronger permitted option: certify R502 itself under the same standard used for R501/R507.

## R502 source-level audit

For Meskhishvili's third one-parameter NPC parametrization, after homogenizing with reduced `t=m/n`, the submitted family satisfies the exact identities

\[
A^2+C^2=D_{AC}^2,\qquad B^2+C^2=D_{BC}^2,\qquad A^2+B^2+C^2=D^2.
\]

On the fixed cone `7/2 < m/n < 4`, the ordering is

\[
0<A<B<C.
\]

The exact primitive gcd claim

\[
g_{502}=2^{5[m,n\text{ both odd}]}3^{4[3\mid m]}
\]

was attacked prime-by-prime and independently regression-checked. No prime greater than 3 can occur; the 2-adic minimum is exactly 5 in the both-odd case and 0 otherwise; the 3-adic minimum is exactly 4 when `3|m` and 0 otherwise. Hence

\[
\boxed{g_{502}\le2592}.
\]

The required diagonals remain divisible by `g502`, so primitive reduction preserves both guaranteed face diagonals and the space diagonal. Moreover

\[
D/g_{502}\ge m^8/2592,
\]

while raw height is `O(T^8)` for `m,n<=T`. Thus primitive reduction cannot hide an exponent improvement.

## Exactly-two and multiplicity audit

The missing face is governed by

\[
P_{502}(t)=t^{16}+16t^{14}-196t^{12}+112t^{10}+5926t^8+1008t^6-15876t^4+11664t^2+6561.
\]

The verifier recomputes `gcd(P502,P502')=1` modulo 5, so `P502` is squarefree over `Q`; the smooth hyperelliptic curve `w^2=P502(t)` has genus 7. Faltings is used only for qualitative finiteness of the rational third-face exceptions.

The scale-free invariant `C/D` gives a nonzero polynomial equation of degree at most 8 for fixed similarity class, so parameter multiplicity is uniformly bounded by 8.

Combining `gg T^2` reduced rational parameters in the cone, height `O(T^8)`, finite third-face exceptions, and bounded multiplicity gives the lower bound. The primitive-height reverse estimate gives the matching family-specific upper. Therefore

\[
\boxed{N_{R502}(B)=\Theta(B^{1/4}).}
\]

This closes R502 as a **family-specific no-upgrade route**. It is not a global upper bound for `N2(B)` and it does not identify the true global exponent.

## Documentation erratum found during re-audit

In `r502-primitive-height-no-upgrade.md`, section 6 displays the factorization of `P502` with a `+` between the two degree-eight factors. The correct operation is multiplication:

\[
P_{502}(t)=
(t^8-8t^6-2t^4+216t^2+81)
(t^8+24t^6-2t^4-72t^2+81).
\]

The expanded polynomial, the mechanical `P502` binding, the mod-5 squarefree calculation, and the genus conclusion are all correct. This is a non-load-bearing transcription error, not a theorem failure. The corrected product above is the authoritative reading for this audited revision.

## Continuation boundary

The previous audit asymmetry is repaired. R502 may now be classified `CLOSED_NO_UPGRADE_WITH_CERTIFICATE`.

Checkpoint60 still does **not** close because R503, R504, R505, and R506 remain live/actionable under the checkpoint60 continuation policy. Therefore Stage70 remains disallowed.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_REAUDIT=true
CORE_MATHEMATICS_PREVIOUSLY_ACCEPTED=true
R502_ROUTE_BOUNDARY_ACCEPTED=true
R502_EXACT_FAMILY_GROWTH_ACCEPTED=Theta(B^(1/4))
R502_GCD_BOUND_ACCEPTED=2592
R502_PARAMETER_FIBER_BOUND_ACCEPTED=8
R502_THIRD_FACE_EXCEPTION_CURVE_GENUS_ACCEPTED=7
R502_HIDDEN_GCD_EXPONENT_UPGRADE=false
R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE
R502_DOCUMENTATION_FACTOR_SIGN_ERRATUM=NONBLOCKING_CORRECTED_IN_REAUDIT
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #985; then Stage25-main-batch at checkpoint60
```