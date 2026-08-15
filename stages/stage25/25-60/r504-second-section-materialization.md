# Stage25-60 R504 second-section materialization

STATUS=THEOREM_CANDIDATE_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

This continues the hostile-audited PASS rank-jump theorem from PR #993. The goal is to extract the new independent section explicitly and determine whether it improves the Stage19 population exponent.

## 1. Polynomial model and explicit new section

Let
\[
N=u^2+4u-3,\qquad M=7-u^2,\qquad H=N^4+M^4.
\]
After denominator scaling the pulled-back R504 elliptic curve is
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
\qquad
G=u^4+8u^3+26u^2+56u+73.
\]
Put
\[
S=u^4+4u^3+22u^2+36u+53.
\]
The exact identity
\[
F^2+G^2=2S^2
\]
gives the explicit polynomial section
\[
\boxed{R=(4S^2,\ 4S(F^2-G^2)).}
\]
Direct expansion verifies `R in E_H(Q(u))`. The prior hostile audit already certifies that the second E0 quotient direction is independent of the inherited E0 direction; this artifact materializes that direction rather than re-opening the rank proof.

## 2. Physical 2-cover and the first new lift

The physical quartic receiver is
\[
t^4+1=(k^4+1)z^2,
\qquad k=N/M.
\]
Its map to `E_H` has negative-square `x`. The combinations `P+R` and `P-R` do not lift over `Q(u)`: inversion gives
\[
t(P+R)^2=\frac{(u^4+4u^3+6u^2+4u-107)^2}{32(u+1)^6},
\]
\[
t(P-R)^2=\frac{(u^4+4u^3+6u^2+4u-11)^2}{128(u+1)^2},
\]
and the constants `32,128` are nonsquares in Q.

The first new rank direction that stays in the physical 2-cover coset is `P+2R`. Define
\[
\begin{aligned}
A={}&u^{10}+4u^9-15u^8-320u^7-1814u^6-5976u^5-14686u^4\\
&-19936u^3-29883u^2-14284u-64099,\\
B={}&u^{10}+16u^9+93u^8+464u^7+1658u^6+4368u^5+6346u^4\\
&-2576u^3-38763u^2-82272u-119319,\\
C={}&u^{16}+16u^{15}+216u^{14}+1904u^{13}+11532u^{12}+51024u^{11}\\
&+176584u^{10}+498992u^9+1465974u^8+4632112u^7+16670632u^6\\
&+49968720u^5+132646892u^4+257203824u^3+414710328u^2\\
&+414710032u+297433361.
\end{aligned}
\]
Exact group-law simplification gives
\[
x(P+2R)=-4\left(\frac{AB}{C}\right)^2,
\qquad
y(P+2R)=\frac{4AB(A^4-B^4)}{C^3},
\]
and the key identity
\[
\boxed{A^4+B^4=HC^2.}
\]
Therefore
\[
\boxed{t=A/B,\qquad z=M^2C/B^2}
\]
satisfies identically
\[
\boxed{t^4+1=(k^4+1)z^2.}
\]
So the new rank direction is now explicit inside the physical R504 receiver.

## 3. Explicit Stage19 family

Clearing the `M^2` denominator gives
\[
\boxed{
E=2NMAB,
\quad X=N^2B^2-M^2A^2,
\quad Y=N^2A^2-M^2B^2,
\quad D=HC.
}
\]
The two guaranteed face diagonals are
\[
H_X=N^2B^2+M^2A^2,
\qquad
H_Y=N^2A^2+M^2B^2,
\]
and direct expansion gives
\[
E^2+X^2=H_X^2,
\qquad E^2+Y^2=H_Y^2,
\qquad E^2+X^2+Y^2=D^2.
\]
At `u=3`, all four physical coordinates are positive and satisfy
\[
0<E<X<Y<D.
\]
Hence by continuity there is a nonempty rational compact interval around `3` with the same strict sign/order pattern.

## 4. Primitive height is degree 24

Write `u=a/b` with `gcd(a,b)=1` and homogenize. The forms `N,M` have degree `2`, `A,B` degree `10`, `C` degree `16`, and `H` degree `8`. Thus the physical coordinates are homogeneous of degree at most `24`, and `D=HC` has degree exactly `24`.

For a clean absolute primitive-gcd certificate use the physical edge polynomials directly. In the dehomogenized variable,
\[
\boxed{\operatorname{Res}(E/2,X)=2^{688}3^{256}},
\]
\[
\boxed{\operatorname{Res}(E/2,Y)=2^{656}3^{272}7^8}.
\]
If a common prime `p` does not divide `b`, the two Bezout-resultant identities force `p in {2,3}`. If `p|b`, primitivity gives `p\nmid a`; the leading coefficient of `E/2` is `-1`, so no odd such `p` divides all three edges. For `p=2`, the explicit leading factor in `E` gives the remaining one power when `b` is even. Consequently the coarse uniform bound
\[
\boxed{\gcd(E,X,Y)\le 2^{689}3^{256}}
\]
is valid for all reduced rational parameters. This bound is deliberately coarse; only absolute boundedness is used.

On the fixed compact interval around `u=3`, `|b|` is comparable to `T=max(|a|,|b|)` and the homogeneous form `D(a,b)` is bounded above and below by positive constants times `T^{24}`. Primitive reduction changes this only by the absolute gcd constant, hence
\[
\boxed{D_{\rm prim}=\Theta(T^{24}).}
\]

## 5. Exactly-two-face exceptions are finite

The missing face factors exactly as
\[
\boxed{X(u)^2+Y(u)^2=256(u+1)^2Q_{44}(u)},
\]
where `Q_44` has degree `44` and is the product of one degree-8 factor and three degree-12 factors. The deterministic verifier reconstructs the factorization and checks
\[
\gcd(Q_{44},Q_{44}')=1\pmod{11}.
\]
Thus `Q_44` is squarefree over Q. The smooth projective curve
\[
w^2=Q_{44}(u)
\]
has genus `21`, so Faltings gives only finitely many rational parameters producing a third square face.

## 6. Multiplicity and exact family growth

On the ordered interval, the scale-invariant ratio `E/X` is a nonconstant rational function of degree at most `24`. Hence one primitive canonical box has only `O(1)` parameters in this subfamily. Reduced rationals of height at most `T` in a fixed nonempty interval number `Theta(T^2)`.

Combining bounded multiplicity, finite third-face exceptions, bounded primitive reduction, and the exact degree-24 height scale yields
\[
\boxed{N_{R504,P+2R}(B)=\Theta(B^{1/12}).}
\]

This is a fully explicit Stage19 family generated by the new rank-jump direction, but it is weaker than the original R504 `3P` family `Theta(B^(1/10))` and the global R501/R502 `B^(1/4)` lower. Therefore the global Stage25 lower does not change.

```text
R504_EXPLICIT_SECOND_MW_SECTION=R=(4*S^2,4*S*(F^2-G^2))
R504_P_PLUS_R_PHYSICAL_LIFT=false
R504_P_MINUS_R_PHYSICAL_LIFT=false
R504_P_PLUS_2R_PHYSICAL_LIFT=true
R504_P_PLUS_2R_T_DEGREE=10
R504_P_PLUS_2R_Z_NUMERATOR_DEGREE=20
R504_P_PLUS_2R_PHYSICAL_HEIGHT_DEGREE=24
R504_P_PLUS_2R_PRIMITIVE_GCD_BOUND=2^689*3^256
R504_P_PLUS_2R_THIRD_FACE_EXCEPTION_GENUS=21
R504_P_PLUS_2R_PARAMETER_MULTIPLICITY=O(1)
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

## 7. Remaining live R504 work

This theorem does not prove that every physical class in the rank-two lattice has height degree at least `24`, and the full-split Prym/isogeny residual remains open. After audit, the next high-value task is a height-pairing/coset analysis of physical classes `(2m+1)P+2nR` to decide whether another class can have lower physical degree, followed separately by the full-split Prym/isogeny residual.
