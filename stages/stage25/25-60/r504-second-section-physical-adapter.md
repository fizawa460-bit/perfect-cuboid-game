# Stage25-60 R504 explicit second section and physical Stage19 adapter

STATUS=THEOREM_CANDIDATE_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

The hostile audit of PR #993 accepted the nonsplit base change
\[
k=\phi(u)=\frac{N}{M}=\frac{u^2+4u-3}{7-u^2}
\]
and the generic rank jump `rank E_phi(Q(u)) >= 2`.  This note materializes a Q(u)-rational second section and pushes the first new physical coset point all the way to an explicit Stage19 family.

Put
\[
N=u^2+4u-3,\qquad M=7-u^2,\qquad H=N^4+M^4.
\]
After clearing the fourth-power denominator of `k^4+1`, work on
\[
E_H:\quad y^2=x^3-4H^2x.
\]
The inherited section is
\[
P=(-4N^2M^2,\ 4NM(N^4-M^4)).
\]

## 1. Explicit new section

Define
\[
G=u^4+4u^3+22u^2+36u+53.
\]
Then
\[
\boxed{
R=\left(
4G^2,
-64(u+1)(u^2+5)(u^2+2u+7)(u^2+4u+9)G
\right)
}
\]
satisfies the equation of `E_H` identically.  This section is the explicit rational-function representative obtained from the second E0 quotient accepted in PR #993.  The prior hostile audit already certifies that its quotient direction is independent of the inherited E0 direction; this note does not re-prove that rank statement.

The physical quartic is a 2-covering.  The inherited rational quartic point determines the physical coset; adding `2R` therefore stays in that coset.  Direct elliptic addition gives an especially clean quartic point for
\[
Q=P+2R.
\]

Define
\[
\begin{aligned}
A={}&u^{10}+4u^9-15u^8-320u^7-1814u^6-5976u^5\\
&-14686u^4-19936u^3-29883u^2-14284u-64099,\\
B={}&u^{10}+16u^9+93u^8+464u^7+1658u^6+4368u^5\\
&+6346u^4-2576u^3-38763u^2-82272u-119319,\\
C={}&u^{16}+16u^{15}+216u^{14}+1904u^{13}+11532u^{12}+51024u^{11}\\
&+176584u^{10}+498992u^9+1465974u^8+4632112u^7+16670632u^6\\
&+49968720u^5+132646892u^4+257203824u^3+414710328u^2\\
&+414710032u+297433361.
\end{aligned}
\]
They satisfy the exact identity
\[
\boxed{A^4+B^4=HC^2.}
\]
Moreover the elliptic coordinates of `Q=P+2R` are
\[
x(Q)=-\frac{4A^2B^2}{C^2},\qquad
y(Q)=\frac{4AB(A^4-B^4)}{C^3}.
\]
Hence the polynomial-twist quartic point is
\[
\boxed{t=A/B,\qquad Z=C/B^2}
\]
with
\[
t^4+1=HZ^2.
\]
Returning to the original base `k=N/M`, put
\[
\boxed{z=M^2C/B^2.}
\]
Then identically
\[
\boxed{t^4+1=(k^4+1)z^2.}
\]
Thus the second rank direction has now been materialized inside the physical R504 quartic receiver.

## 2. Explicit Stage19 box

Using the shared-edge receiver with `t=A/B` and clearing the `M^2` denominator gives
\[
\boxed{
\begin{aligned}
e&=2NMAB,\\
x&=N^2B^2-M^2A^2,\\
y&=N^2A^2-M^2B^2,\\
d&=HC.
\end{aligned}}
\]
The two guaranteed face diagonals are
\[
h_x=N^2B^2+M^2A^2,\qquad
h_y=N^2A^2+M^2B^2,
\]
and direct expansion gives
\[
e^2+x^2=h_x^2,\qquad
e^2+y^2=h_y^2,\qquad
e^2+x^2+y^2=d^2.
\]
At `u=3` all of `e,x,y,d` are positive and `e<x<y<d`; by continuity there is a nonempty rational compact interval around `3` with the same strict sign/order pattern.

## 3. Primitive-height scale

Homogenize with `u=a/b`, `gcd(a,b)=1`.  The forms `N,M` have degree `2`, `A,B` degree `10`, `C` degree `16`, and `H` degree `8`; therefore all physical coordinates have homogeneous degree at most `24`, and `d=HC` has degree exactly `24`.

A coarse but fully uniform primitive-gcd certificate is enough for the exponent.  In the dehomogenized variable,
\[
\operatorname{Res}(e/2,x)=2^{688}3^{256},
\]
\[
\operatorname{Res}(e/2,y)=2^{656}3^{272}7^8.
\]
For a common prime `p` with `p\nmid b`, the two resultant identities imply `p in {2,3}`.  If `p|b`, primitivity gives `p\nmid a`; the leading coefficient of `e/2` is `-1`, so no odd such `p` divides all three edges, and for `p=2` the edge `e` has only the explicit leading factor `2`.  Consequently a coarse global bound is
\[
\boxed{\gcd(e,x,y)\le 2^{689}3^{256}.}
\]
No unbounded primitive cancellation can reduce the degree-24 scale.

On the compact positivity interval around `u=3`, `b` is comparable to `T=max(|a|,|b|)` and the homogeneous form `d(a,b)` is bounded above and below by positive constants times `T^{24}`.  After primitive reduction the same is true up to the absolute gcd constant:
\[
\boxed{d_{\rm prim}=\Theta(T^{24}).}
\]

## 4. Exactly-two-face exceptions

The missing face factors exactly as
\[
\boxed{x^2+y^2=256(u+1)^2Q_{44}(u)}
\]
where `Q_44` has degree `44` and factors as `F8*F12a*F12b*F12c` with
\[
\begin{aligned}
F_8={}&5u^8+40u^7+116u^6+136u^5-82u^4-488u^3+1940u^2+4792u+14165,\\
F_{12a}={}&u^{12}+4u^{11}+18u^{10}+52u^9-101u^8-472u^7+460u^6+17768u^5\\
&+79975u^4+190740u^3+350594u^2+364964u+562013,\\
F_{12b}={}&u^{12}+12u^{11}+86u^{10}+420u^9+1567u^8+4568u^7+9652u^6+13736u^5\\
&+5935u^4-19428u^3+9238u^2+67252u+459985,\\
F_{12c}={}&u^{12}+20u^{11}+194u^{10}+1188u^9+4843u^8+12872u^7+21292u^6+5576u^5\\
&-61049u^4-164124u^3-126606u^2+34516u+471277.
\end{aligned}
\]
The deterministic verifier checks
\[
\gcd(Q_{44},Q_{44}')=1\pmod {11}.
\]
Thus `Q_44` is squarefree over Q.  The smooth projective curve
\[
w^2=Q_{44}(u)
\]
has genus `21`, so Faltings gives only finitely many rational parameters for which the missing third face is also square.

## 5. Parameter multiplicity and family growth

The scale-invariant ratio `e/x` is a nonconstant rational function whose numerator and denominator have degree at most `24`.  Hence any fixed primitive canonical box has at most `24` parameters in the chosen ordered interval.  Reduced rationals in a fixed nonempty compact interval have `Theta(T^2)` points of height at most `T`.

Combining bounded multiplicity, finite third-face exceptions, bounded primitive cancellation, and the exact degree-24 height scale gives
\[
\boxed{N_{R504,P+2R}(B)=\Theta(B^{1/12}).}
\]

This is an explicit new Stage19 family arising from the audited rank-jump direction, but it is weaker than both the old R504 `3P` family `Theta(B^(1/10))` and the global R501/R502 `B^(1/4)` lower.  Therefore
\[
\boxed{\text{GLOBAL_STAGE25_LOWER_CHANGED=false}.}
\]

The positive rank jump is real, but this first physical point on the new direction is too height-expensive to improve the population exponent.

```text
R504_SECOND_SECTION_MATERIALIZED=true
R504_SECOND_SECTION=R
R504_FIRST_NEW_PHYSICAL_COSET_POINT=P+2R
R504_SECOND_DIRECTION_QUARTIC_POINT=t=A/B;z=M^2*C/B^2
R504_SECOND_DIRECTION_PHYSICAL_HEIGHT_DEGREE=24
R504_SECOND_DIRECTION_PRIMITIVE_GCD_ABSOLUTELY_BOUNDED=true
R504_SECOND_DIRECTION_THIRD_FACE_EXCEPTION_GENUS=21
R504_SECOND_DIRECTION_PARAMETER_MULTIPLICITY_BOUND=24
R504_SECOND_DIRECTION_EXACT_FAMILY_GROWTH=Theta(B^(1/12))
R504_SECOND_DIRECTION_BEATS_R504_3P=false
R504_SECOND_DIRECTION_BEATS_GLOBAL_QUARTER=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_REQUIRED_NOW=true
```
