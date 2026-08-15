# Stage25-60 R504 explicit nonsplit rank-jump base change

STATUS=THEOREM_CANDIDATE_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

The complete Q-degree-2 descent is already hostile-audited PASS.  The nonsplit N2 commuting-lift locus contains an explicit base change for which the pullback twist cover acquires a second elliptic factor Q-isomorphic to `E0`.

## 1. Explicit degree-two map

Set
\[
\boxed{
 k=\phi(u)=\frac{u^2+4u-3}{7-u^2}.
}
\]
Its derivative is
\[
\phi'(u)=\frac{4(u^2+2u+7)}{(u^2-7)^2},
\]
so the critical points are `u=-1+-sqrt(-6)`: this is genuinely nonsplit, in squareclass `-6`.

The two critical values have product `1` and sum `-10/7`; equivalently their branch polynomial is
\[
k^2+\frac{10}{7}k+1.
\]
Thus this is a concrete point of the nonsplit N2 locus (`k -> 1/k`).

The source deck involution is obtained from `phi(v)=phi(u)`:
\[
\boxed{\delta(u)=-\frac{u+7}{u+1}}.
\]
The two lifts of `k -> 1/k` are
\[
\epsilon_1(u)=-u-2,
\qquad
\boxed{\epsilon_2(u)=\frac{5-u}{u+1}},
\]
and `epsilon_2=delta*epsilon_1`.

## 2. Pullback twist cover

Put
\[
N=u^2+4u-3,
\qquad M=7-u^2.
\]
The untwisting cover of the pulled-back R504 elliptic curve is the genus-three hyperelliptic curve
\[
C:\quad Y^2=N^4+M^4.
\]
The inherited quotient by `delta` is the original genus-one twist cover `s^2=k^4+1`, whose Jacobian is the audited constant curve
\[
E_0:y^2=x^3-4x.
\]
Hence `J(C)` already contains one `E0` factor.

## 3. A second genus-one quotient

For `epsilon_2(u)=(5-u)/(u+1)`, direct substitution gives
\[
F(\epsilon_2(u))=\frac{1296}{(u+1)^8}F(u),
\qquad F=N^4+M^4.
\]
Thus the lift on `C` is
\[
(u,Y)\mapsto
\left(\frac{5-u}{u+1},\frac{36Y}{(u+1)^4}\right).
\]
Define the invariant functions
\[
x=\frac{u^2+5}{u+1},
\qquad
W=\frac{Y}{(u^2+2u-5)^2}.
\]
They satisfy
\[
W^2=
\frac{2(x^2-8)(x^2+8x+8)}{(x^2+4x-20)^2}.
\]
Therefore, with
\[
V=W(x^2+4x-20),
\]
the quotient `D=C/<epsilon_2>` has the genus-one model
\[
\boxed{
D:\quad V^2=2(x^2-8)(x^2+8x+8)
=2(x^4+8x^3-64x-64).
}
\]

For this binary quartic, the exact invariants are
\[
I=3072,
\qquad J=0.
\]
Its Jacobian is therefore
\[
E_D:\quad y^2=x^3-82944x.
\]
Since
\[
82944/4=20736=12^4,
\]
the rational scaling
\[
x=144X,
\qquad y=1728Y
\]
gives
\[
\boxed{E_D\simeq_{\mathbf Q}E_0: Y^2=X^3-4X.}
\]
Thus `J(C)` contains a **second Q-defined E0 quotient factor**.

## 4. Independence of the two E0 factors

The inherited quotient is attached to `delta`; the new quotient is attached to the distinct commuting involution `epsilon_2`.  Their product is `epsilon_1`.  The quotient by the generated V4 is rational: after first quotienting by `delta`, `epsilon_2` descends to `k -> 1/k` on the genus-one curve `s^2=k^4+1`, whose quotient is P1.

Hence the invariant differential lines of the `delta` and `epsilon_2` quotients are distinct (their intersection would descend to a differential on the genus-zero V4 quotient).  The induced homomorphisms
\[
J(C)\longrightarrow E_0
\]
are therefore independent.

Consequently
\[
\boxed{
\operatorname{rank}_{\mathbf Z}\operatorname{Hom}_{\mathbf Q}(J(C),E_0)\ge2.
}
\]

## 5. Mordell-Weil consequence for R504

For the pulled-back elliptic curve
\[
E_{\phi}:\quad
Y^2=X^3-4(\phi(u)^4+1)^2X
\]
over `Q(u)`, the same audited twist-descent used for the original R504 base identifies free sections with the nonconstant Q-homomorphism lattice from the untwisting cover Jacobian to `E0` (the hyperelliptic deck involution acts as `-1` on the Jacobian).

The two independent `E0` quotient factors therefore give
\[
\boxed{
\operatorname{rank}E_{\phi}(\mathbf Q(u))\ge2.
}
\]
This is a genuine rank jump from the hostile-audited original-base rank `1`.

```text
R504_EXPLICIT_NONSPLIT_BASE_CHANGE=(u^2+4u-3)/(7-u^2)
R504_EXPLICIT_NONSPLIT_SQUARECLASS=-6
R504_EXPLICIT_BRANCH_TRACE=-10/7
R504_EXPLICIT_BRANCH_NORM=1
R504_EXPLICIT_DECK=-(u+7)/(u+1)
R504_SECOND_INVOLUTION=(5-u)/(u+1)
R504_SECOND_QUOTIENT_BINARY_QUARTIC=2*(x^4+8*x^3-64*x-64)
R504_SECOND_QUOTIENT_I=3072
R504_SECOND_QUOTIENT_J=0
R504_SECOND_QUOTIENT_JACOBIAN_Q_ISOMORPHIC_E0=true
R504_PULLBACK_MW_RANK_LOWER=2
R504_GENERIC_RANK_JUMP_PROVED=true
```

## 6. What this does NOT yet prove

The new section is presently obtained through the quotient/Jacobian correspondence; an explicit low-height rational-function section has not yet been materialized.  Therefore this theorem does **not** yet improve the global Stage19 population lower bound beyond the audited `B^(1/4)` supplied by R501/R502.

The next high-value task is to extract an explicit second section (or a controlled degree bound for one), then compute its physical cuboid height, primitive gcd, exactly-two-face exceptions, and parameter multiplicity.

```text
R504_EXPLICIT_SECOND_SECTION_MATERIALIZED=false
R504_SECOND_SECTION_PHYSICAL_HEIGHT_DEGREE=UNKNOWN
R504_GLOBAL_QUARTER_LOWER_UPGRADE_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_REQUIRED_NOW=true
```
