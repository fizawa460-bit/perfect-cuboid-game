# Stage25-60 R504 second-section materialization

STATUS=THEOREM_CANDIDATE_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

This continues the hostile-audited PASS rank-jump theorem from PR #993.  The goal is to extract the new independent section explicitly and determine whether it improves the Stage19 population exponent.

## 1. Polynomial model of the pulled-back elliptic curve

Let

\[
N=u^2+4u-3,\qquad M=7-u^2,
\]
\[
H=N^4+M^4.
\]
After the standard denominator scaling, the pulled-back R504 curve is

\[
\mathcal E_H:\quad y^2=x^3-4H^2x.
\]
The inherited section is

\[
P=(-4N^2M^2,\ 4NM(N^4-M^4)).
\]

The rank-jump factorization is

\[
H=2FG,
\]
where

\[
F=u^4+2u^2-16u+17,
\]
\[
G=u^4+8u^3+26u^2+56u+73.
\]
Put

\[
S=u^4+4u^3+22u^2+36u+53.
\]
Then the exact identity

\[
F^2+G^2=2S^2
\]
gives the explicit independent polynomial section

\[
\boxed{
R=(4S^2,\ 4S(F^2-G^2)).
}
\]
Direct expansion verifies `R in E_H(Q(u))`.  This is the section represented abstractly by the second `E0` quotient in the audited rank-jump theorem.

## 2. Why the new generator itself is not yet a physical quartic point

The physical quartic receiver is the 2-cover

\[
t^4+1=(k^4+1)z^2,
\qquad k=N/M,
\]
whose map to `E_H` has

\[
x=-4\left(M^2t/z\right)^2.
\]
Thus not every Mordell-Weil point lies on the physical 2-cover.

The combinations `P+R` and `P-R` have negative-square `x`, but inversion of the quartic map gives

\[
t(P+R)^2=\frac{(u^4+4u^3+6u^2+4u-107)^2}{32(u+1)^6},
\]
\[
t(P-R)^2=\frac{(u^4+4u^3+6u^2+4u-11)^2}{128(u+1)^2}.
\]
Since `32` and `128` are nonsquares in `Q`, neither is a `Q(u)`-rational physical quartic section.

## 3. The physical lift `P+2R`

Doubling `R` and adding `P` gives a point whose `x`-coordinate is exactly a negative rational square.  Define

\[
A=u^{10}+4u^9-15u^8-320u^7-1814u^6-5976u^5-14686u^4-19936u^3-29883u^2-14284u-64099,
\]
\[
B=u^{10}+16u^9+93u^8+464u^7+1658u^6+4368u^5+6346u^4-2576u^3-38763u^2-82272u-119319,
\]
\[
C=u^{16}+16u^{15}+216u^{14}+1904u^{13}+11532u^{12}+51024u^{11}+176584u^{10}+498992u^9+1465974u^8+4632112u^7+16670632u^6+49968720u^5+132646892u^4+257203824u^3+414710328u^2+414710032u+297433361.
\]
Then exact group-law simplification gives

\[
x(P+2R)=-4\left(\frac{AB}{C}\right)^2,
\]
and inversion of the quartic covering gives

\[
\boxed{t(u)=A/B},
\]
\[
\boxed{z(u)=M^2C/B^2}.
\]
The verifier checks the exact quartic identity

\[
\boxed{
A^4+B^4=(N^4+M^4)C^2.
}
\]
Hence `P+2R` is an explicit nondegenerate rational section of the physical R504 quartic receiver.

## 4. Homogeneous Stage19 family and physical height

Write `u=a/b` in lowest terms and homogenize

\[
N_h=a^2+4ab-3b^2,\qquad M_h=7b^2-a^2,
\]
with degree-10 forms `A_h,B_h` and degree-16 form `C_h` obtained from `A,B,C`.

The physical Stage19 coordinates are

\[
E=2N_hM_hA_hB_h,
\]
\[
X=N_h^2B_h^2-M_h^2A_h^2,
\]
\[
Y=N_h^2A_h^2-M_h^2B_h^2,
\]
\[
D=(N_h^4+M_h^4)C_h.
\]
The face diagonals are

\[
H_X=N_h^2B_h^2+M_h^2A_h^2,
\]
\[
H_Y=N_h^2A_h^2+M_h^2B_h^2.
\]
All seven displayed coordinates are homogeneous of degree `24`, and exact expansion gives

\[
E^2+X^2=H_X^2,
\qquad E^2+Y^2=H_Y^2,
\qquad E^2+X^2+Y^2=D^2.
\]

On any compact rational subinterval of a sufficiently small neighborhood of `u=0`, none of `E,X,Y,D` vanishes and their signs/order are fixed.  Hence with `H=max(|a|,|b|)` the raw physical height is `Theta(H^24)` on that interval.

## 5. Primitive reduction is bounded

The dehomogenized resultants are

\[
\operatorname{Res}(N,M)=-96=-2^5\,3,
\]
\[
\operatorname{Res}(A,B)=2^{115}3^{49}.
\]
For coprime `(a,b)`, the standard homogeneous resultant Bezout identities therefore give uniform bounds for `gcd(N_h,M_h)` and `gcd(A_h,B_h)`.

If a prime power divides all of `E,X,Y`, use `E=2N_hM_hA_hB_h`.  If a high valuation lies in one member of each pair `(N_h,M_h)` and `(A_h,B_h)`, one of `X,Y` contains a low-low term; if the two terms have equal valuation then `v_p(E)` itself is bounded by twice the two resultant bounds.  Thus

\[
\boxed{\gcd(E,X,Y)\le K_{504}}
\]
for an absolute constant.  A coarse explicit admissible bound is

\[
K_{504}=2^{241}3^{100}.
\]
No polynomial-height cancellation is possible under primitive reduction.

Therefore the primitive physical height remains `Theta(H^24)` on the chosen interval.

## 6. Exactly-two-face exceptions are finite

Dehomogenize at `b=1`.  The missing face factors as

\[
X(u)^2+Y(u)^2=256(u+1)^2Q_{44}(u),
\]
where `Q_44` has degree `44` and factors over `Q` as one degree-8 factor and three degree-12 factors.  The deterministic verifier reconstructs these factors and checks

\[
\gcd(Q_{44},Q_{44}')=1\pmod{11}.
\]
Hence `Q_44` is squarefree over `Q`.  The smooth projective curve

\[
w^2=Q_{44}(u)
\]
has genus `21`, so only finitely many rational parameters produce a third square face.

## 7. Parameter multiplicity and family growth

On the fixed-sign/order interval, the scale-invariant ratio `E/X` is a nonconstant rational function of degree at most `24`.  Hence each primitive canonical cuboid is represented by only `O(1)` parameters in this subfamily.

There are `Theta(T^2)` reduced rational parameters `u=a/b` of height at most `T` in a fixed nonempty rational interval.  Combining bounded primitive gcd, degree-24 physical height, bounded multiplicity, and finite third-face exceptions gives

\[
\boxed{
N_{R504,P+2R}(B)=\Theta(B^{1/12}).
}
\]

This is a fully explicit second R504 Stage19 family produced by the new rank-jump direction, but it is weaker than both the original R504 `3P` family `Theta(B^(1/10))` and the global R501/R502 lower `B^(1/4)`.

```text
R504_EXPLICIT_SECOND_MW_SECTION=R=(4*S^2,4*S*(F^2-G^2))
R504_P_PLUS_R_PHYSICAL_LIFT=false
R504_P_MINUS_R_PHYSICAL_LIFT=false
R504_P_PLUS_2R_PHYSICAL_LIFT=true
R504_P_PLUS_2R_T_DEGREE=10
R504_P_PLUS_2R_Z_NUMERATOR_DEGREE=20
R504_P_PLUS_2R_PHYSICAL_HEIGHT_DEGREE=24
R504_P_PLUS_2R_PRIMITIVE_GCD=O(1)
R504_P_PLUS_2R_THIRD_FACE_EXCEPTION_GENUS=21
R504_P_PLUS_2R_EXACT_FAMILY_GROWTH=Theta(B^(1/12))
R504_P_PLUS_2R_BEATS_R504_3P=false
R504_P_PLUS_2R_BEATS_GLOBAL_QUARTER=false
R504_EXPLICIT_SECOND_SECTION_MATERIALIZED=true
R504_PHYSICAL_STAGE19_ADAPTER_PROVED=true
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_REQUIRED_NOW=true
```

## 8. Remaining live R504 work

This theorem does not prove that every physical section in the rank-two lattice has height degree at least `24`, and it does not close the full-split Prym/isogeny residual.  The next high-value R504 subproblem is a height-pairing/coset analysis of the rank-two lattice to determine whether another physical class `(2m+1)P+2nR` has degree below the present global-quarter threshold, or whether the rank jump is quantitatively harmless for Stage19 population growth.
