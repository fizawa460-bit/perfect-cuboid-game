# Stage25-60 R504 full split normal-form analysis

STATUS=ACTIVE_RESEARCH
ROUTE=R504
CHECKPOINT=60

The complete Q-degree-2 source descent is hostile-audited PASS.  This artifact executes the full split stratum rather than the former strict subfamily.

## 1. Full split form

After Q-source conjugacy of the deck involution to `u -> -u`, every split degree-two map has
\[
\phi(u)=\frac{A u^2+B}{C u^2+D},\qquad A,B,C,D\in\mathbf Q,
\]
with
\[
\Delta_M=AD-BC\ne0.
\]
The former family `(a*u^2+b)/(u^2+1)` is the special slice `C=D=1`; it is not used as a complete normal form here.

After clearing the fourth-power denominator, the pullback twist cover is
\[
Y^2=Q(u^2),\qquad
Q(x)=(Ax+B)^4+(Cx+D)^4.
\]
Write
\[
Q(x)=q_4x^4+q_3x^3+q_2x^2+q_1x+q_0.
\]
Then
\[
q_4=A^4+C^4,
\quad q_3=4(A^3B+C^3D),
\quad q_2=6(A^2B^2+C^2D^2),
\]
\[
q_1=4(AB^3+CD^3),
\quad q_0=B^4+D^4.
\]

## 2. Q-rational reciprocal extra involution

A reciprocal source involution
\[
u\longmapsto \lambda/u,
\qquad \lambda\in\mathbf Q^*,
\]
induces `x -> L/x`, `L=lambda^2`, so the even octic must satisfy
\[
q_1=Lq_3,\qquad q_0=L^2q_4.
\]
Eliminating `L` gives the exact factorization
\[
\boxed{
q_0q_3^2-q_4q_1^2
=16(AB-CD)(AB+CD)(AD-BC)^3(AD+BC).
}
\]
Since `AD-BC != 0`, the candidate loci are
\[
AB=CD,\qquad AB=-CD,\qquad AD=-BC.
\]

### Locus S1: `AB=CD`

For nondegenerate points (`B C != 0`, `A^2 != C^2`) put `D=AB/C`. Then
\[
L=\frac{B^2}{C^2},\qquad \lambda=B/C\in\mathbf Q.
\]
Thus this is a genuine Q-rational reciprocal-involution locus.

Using `X=u+lambda/u`, the complementary genus-one quotient is a binary quartic with invariants
\[
I_1=
8\frac{B^2}{C^2}(A-C)^4
(5A^4+4A^3C+6A^2C^2+4AC^3+5C^4),
\]
\[
J_1=
-64\frac{B^3}{C^3}(A-C)^8
(A^2+AC+C^2)(7A^2+10AC+7C^2).
\]
In particular `J_1 != 0` at every nondegenerate rational point: both quadratic factors have negative discriminant and `A=C` is degenerate.

### Locus S2: `AB=-CD`

Put `D=-AB/C`. Then
\[
L=-\frac{B^2}{C^2}.
\]
For nonzero rational `B,C`, this is not a square in Q. Hence there is no Q-rational `lambda` and no Q-rational reciprocal source involution in this locus.

### Locus S3: `AD=-BC`

For nondegenerate points put `D=-BC/A`. Then
\[
L=\frac{B^2}{A^2},\qquad \lambda=B/A\in\mathbf Q.
\]
The complementary genus-one quotient has
\[
I_3=
64\frac{B^2C^4}{A^2}(3A^4+4C^4),
\]
\[
J_3=
-1024\frac{B^3C^8}{A^3}(9A^4+8C^4).
\]
Again `J_3 != 0` at every nondegenerate rational point.

Therefore the Q-rational reciprocal/commuting-involution loci in the **complete split normal form** are completely explicit:

```text
R504_FULL_SPLIT_NORMAL_FORM=(A*u^2+B)/(C*u^2+D)
R504_FULL_SPLIT_DETERMINANT=AD-BC!=0
R504_FULL_SPLIT_RECIPROCAL_LOCUS=(AB-CD)*(AB+CD)*(AD+BC)=0
R504_FULL_SPLIT_S1=AB-CD=0;Q_RATIONAL_LIFT=true
R504_FULL_SPLIT_S2=AB+CD=0;Q_RATIONAL_LIFT=false
R504_FULL_SPLIT_S3=AD+BC=0;Q_RATIONAL_LIFT=true
R504_FULL_SPLIT_S1_COMPLEMENT_J_ZERO=false
R504_FULL_SPLIT_S3_COMPLEMENT_J_ZERO=false
R504_FULL_SPLIT_RECIPROCAL_ANALYSIS=CLOSED_WITH_SYMBOLIC_CERTIFICATE
```

## 3. Scope firewall

This closes only the Q-rational reciprocal/commuting extra-involution mechanism inside the complete split stratum. It does **not** claim that every possible additional `E0`-isogeny factor must arise from such an involution. A non-bielliptic Prym factor remains possible and is kept live.

It also does not touch the nonsplit squareclass stratum.

```text
R504_FULL_SPLIT_PRYM_RESIDUAL=LIVE
R504_NONSPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_FULL_Q_RATIONAL_EXTRA_FACTOR_LOCUS_CLOSED=false
R504_PRYM_AS_SOLE_GLOBAL_DEGREE2_RESIDUAL=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

## 4. Next attack

Pass to the hostile-audited nonsplit form
\[
\phi(u)=\frac{A(u^2+d)+Bu}{C(u^2+d)+Du},
\qquad d\in\mathbf Q^*/(\mathbf Q^*)^2,
\]
with deck involution `u -> d/u`.  First classify Q-rational commuting extra involutions and their lift obstruction uniformly in `d`; then keep any non-bielliptic Prym/isogeny mechanism separate.
