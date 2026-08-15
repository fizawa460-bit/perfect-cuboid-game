# Stage25-60 R504 hostile fresh audit

Status: **PASS — original-base section lattice and 3P quantitative family accepted; base-change/growing-multiple gates remain open**

## Scope

This fresh audit treats PR #987 as an unaudited mathematical submission despite its merge, and audits the clean hardening PR #989 against the exact R504 claims.

The audit independently attacked:

1. the isotrivial twist/cover identification;
2. the deck action and anti-invariant descent;
3. the claim `rank E_F(Q(k))=1`;
4. the identification of the explicit Stage25 section with the primitive free generator;
5. the homogenized 3P Stage19 family, primitive gcd and degree-20 physical height;
6. the genus-15 third-face exception argument;
7. bounded parameter multiplicity and the two-sided `Theta(B^(1/10))` count;
8. scope firewalls for finite base change, multisections and growing multiples.

## A. Twist descent — PASS

Let `F=k^4+1` and

\[
E_F: Y^2=X^3-4F^2X.
\]

Over `s^2=F`, the substitution

\[
u=X/F,\qquad v=Y/(Fs)
\]

untwists to

\[
E_0:v^2=u^3-4u.
\]

The cover `C:s^2=k^4+1` is Q-birational to `E_0` through

\[
Q=\left(2(s+1)/k^2,\;4(s+1)/k^3\right),
\]

with inverse `k=2u/v` away from the usual exceptional points. Direct substitution verifies the equation.

For `T=(0,0)`, the deck involution `s -> -s` acts by

\[
\tau(Q)=T-Q.
\]

A `Q(k)`-point on the twist therefore becomes an anti-invariant Q-defined map `R:C->E_0`. Since `C` is a genus-one curve birational over Q to `E_0`, nonconstant maps modulo translation are `End_Q(E_0)`. For `E_0` with `j=1728`, the nonintegral CM endomorphisms require `i`, hence

\[
End_Q(E_0)=Z.
\]

Writing `R=[n]Q+S`, anti-invariance gives

\[
nT+2S=0.
\]

The duplication formula

\[
x([2]S)=\frac{(x^2+4)^2}{4x(x^2-4)}
\]

shows that `[2]S=T` would force `x^2=-4`; thus `T` is not twice a Q-rational point. Hence `n` must be even. For even `n`, only rational 2-torsion translations remain, so the free anti-invariant lattice is rank one with primitive coefficient 2.

The submitted explicit section untwists to `-(T+[2]Q)`, so it realizes that primitive coefficient. Therefore

\[
\boxed{E_F(Q(k))_{free}=ZP,\qquad rank\,E_F(Q(k))=1.}
\]

This conclusion is accepted **only on the original base Q(k)**.

## B. 3P Stage19 family — PASS

For reduced `k=u/v`, the homogenized coordinates in `r504-section-lattice.md` satisfy exactly

\[
E^2+X^2=H_X^2,\qquad E^2+Y^2=H_Y^2,\qquad E^2+X^2+Y^2=D^2.
\]

For coprime positive `u,v`, the common primitive gcd is

\[
\boxed{g=2^{7[u,v\text{ both odd}]}\le128.}
\]

The odd-prime exclusion in the proof is valid, and the 2-adic minimum is exactly attained by `E` in the both-odd case.

The raw space diagonal obeys

\[
H^{20}\le D\le128H^{20},\qquad H=max(u,v),
\]

so after primitive reduction

\[
\boxed{H^{20}/128\le D_{prim}\le128H^{20}.}
\]

Thus primitive height has exact parameter degree 20.

## C. Exactly-two and multiplicity — PASS

The missing face factors as

\[
X(k)^2+Y(k)^2=(k-1)^2(k+1)^2(k^2+1)^2Q_{32}(k),
\]

where the submitted four degree-eight factors multiply to `Q_32`. Independent symbolic expansion agrees with the displayed factorization. The committed mod-3 certificate gives

\[
gcd(Q_{32},Q_{32}')=1,
\]

so `Q_32` is squarefree over Q. Hence `w^2=Q_32(k)` has genus 15 and, by the already accepted Faltings contract, only finitely many rational third-face exceptions.

On the strict physical interval around `k=5/2`, the canonical order is fixed. The scale-free ratio `E/X` is a nonconstant rational function of degree at most 16, so each primitive canonical box has at most 16 R504 parameters there.

The compact rational subinterval supplies `gg H^2` reduced rational parameters. Combined with degree-20 height, finite third-face exceptions and bounded fibers,

\[
\boxed{N_{R504,3P}(B)=Theta(B^{1/10}).}
\]

This is family-specific and is weaker than the audited global quarter-power lower.

## D. Hostile scope firewall

Accepted:

- no second independent `Q(k)`-rational section exists on the original symmetric-k surface;
- the explicit 3P family has exact growth `Theta(B^(1/10))`;
- this family does not improve `N2(B)>>B^(1/4)`.

Not accepted / still open:

- rank after a nontrivial finite base change;
- low-degree multisections that become sections after base change;
- any uniform aggregation theorem over growing multiples;
- any global lower exponent above `1/4`;
- matching half-power lower or true target exponent.

Accordingly R504 is closed only as an **original-base independent-section global-upgrade route**. The remaining base-change/multisection/growing-multiple mutations remain explicit OPEN_GATEs.

## Verdict

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_TWIST_DESCENT_ACCEPTED=true
R504_GENERIC_QK_RANK=1
R504_SECOND_INDEPENDENT_QK_SECTION_EXISTS=false
R504_EXPLICIT_P_PRIMITIVE_FREE_GENERATOR_ACCEPTED=true
R504_3P_PRIMITIVE_GCD_BOUND=128
R504_3P_HEIGHT_DEGREE=20
R504_3P_THIRD_FACE_EXCEPTION_GENUS=15
R504_3P_EXACT_FAMILY_GROWTH=Theta(B^(1/10))
R504_3P_BEATS_GLOBAL_QUARTER=false
R504_ORIGINAL_SURFACE_SECTION_ROUTE=CLOSED_NO_GLOBAL_UPGRADE
R504_LOW_DEGREE_BASE_CHANGE_ROUTE=OPEN_GATE
R504_MULTI_SECTION_ROUTE=OPEN_GATE
R504_GROWING_MULTIPLE_UNIFORM_AGGREGATION=OPEN_GATE
GLOBAL_STAGE25_LOWER_CHANGED=false
GLOBAL_LOWER_EXPONENT_ABOVE_QUARTER_PROVED=false
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
NEXT_EXPECTED_COMMAND=merge PR #989; then Stage25-main-batch at checkpoint60
```