# Stage25-60 R504 full-split Prym generic E0-factor test

STATUS=THEOREM_CANDIDATE_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

This continues the hostile-audited full-split reciprocal-involution analysis and the hostile-audited rank-two/growing-lattice closures.  The remaining full-split question is whether the two-dimensional Prym factor can contain an additional elliptic factor Q-isogenous to

\[
E_0:\ y^2=x^3-4x
\]

without coming from a Q-rational extra involution on the genus-three cover.

The present round does **not** claim to classify every exceptional specialization.  It proves first that such an `E0` factor is not generic in the complete split family.

## 1. Complete split family and Prym factor

Use the hostile-audited complete split normal form

\[
\phi(u)=\frac{Au^2+B}{Cu^2+D},\qquad AD-BC\ne0.
\]

After clearing the fourth-power denominator, the untwisting genus-three curve is

\[
C_{A,B,C,D}:\quad Y^2=Q(u^2),
\]

where

\[
Q(x)=(Ax+B)^4+(Cx+D)^4.
\]

The involution `u -> -u` has elliptic quotient

\[
E_{A,B,C,D}:\quad Y^2=Q(x).
\]

Thus, over the smooth parameter locus,

\[
J(C)\sim E\times P,
\]

where `P` is the dimension-two Prym factor.  The question is whether

\[
\operatorname{Hom}(P,E_0)\ne0.
\]

## 2. A non-reciprocal full-split specialization

Take

\[
(A,B,C,D)=(1,1,1,2).
\]

Then

\[
AD-BC=1\ne0,
\]

and the three reciprocal-locus factors are

\[
AB-CD=-1,\qquad AB+CD=3,\qquad AD+BC=3.
\]

So this point is outside every previously classified Q-rational reciprocal/commuting-involution locus.

The quotient polynomial is

\[
Q(x)=(x+1)^4+(x+2)^4
=2x^4+12x^3+30x^2+36x+17,
\]

and the genus-three curve is

\[
C_*:\quad Y^2=2u^8+12u^6+30u^4+36u^2+17.
\]

## 3. Good reduction at p=5

Modulo `5`,

\[
Q(x)=2(x^2-2)(x^2+x+2).
\]

The verifier checks

\[
\gcd(Q,Q')=1\pmod5,
\qquad
\gcd(Q(u^2),(Q(u^2))')=1\pmod5.
\]

Hence both the elliptic quotient and the genus-three curve have good smooth hyperelliptic reduction at `p=5`.

## 4. Exact point counts over F5 and F25

The deterministic verifier enumerates the curves over `F_5` and `F_25` (using `F_25=F_5[w]/(w^2-2)`).  Including the two points at infinity when the leading coefficient is a square, it obtains

\[
\#C_*(\mathbf F_5)=4,
\qquad
\#E_*(\mathbf F_5)=4,
\]

and

\[
\#C_*(\mathbf F_{25})=36,
\qquad
\#E_*(\mathbf F_{25})=32.
\]

Let `S_r(X)` denote the power sum of Frobenius eigenvalues on `H^1(X)`.  Then

\[
S_1(C_*)=6-4=2,
\qquad
S_1(E_*)=6-4=2,
\]

so

\[
S_1(P_*)=0.
\]

For the quadratic extension,

\[
S_2(C_*)=26-36=-10,
\qquad
S_2(E_*)=26-32=-6,
\]

hence

\[
S_2(P_*)=-4.
\]

For an abelian surface the degree-four Frobenius polynomial in the `L(T)=prod(1-alpha_i T)` convention is therefore

\[
\boxed{L_{P_*,5}(T)=1+2T^2+25T^4.}
\]

## 5. Excluding the E0 factor

For

\[
E_0:y^2=x^3-4x
\]

over `F_5`, direct counting gives trace `a_5(E_0)=2`, so

\[
L_{E_0,5}(T)=1-2T+5T^2.
\]

Exact polynomial division gives nonzero remainder

\[
1+2T^2+25T^4
=(1-2T+5T^2)\left(5T^2+2T+\frac15\right)
+\left(\frac45-\frac85T\right).
\]

Thus

\[
\boxed{L_{E_0,5}\nmid L_{P_*,5}.}
\]

Consequently `P_*` has no `E0` isogeny factor over Q: a nonzero homomorphism to/from `E0` would give a common two-dimensional Frobenius factor after good reduction.

## 6. Generic-family consequence

Work over the normal smooth open of the full-split parameter space containing the specialization above.  A homomorphism between the generic abelian schemes extends over that open.  Therefore, if the **generic** Prym factor contained an `E0` isogeny factor, the specialization `P_*` would inherit a nonzero `E0` homomorphism.  Section 5 excludes this.

Hence

\[
\boxed{
\operatorname{Hom}(P_{\eta},E_0)=0
}
\]

for the generic full-split Prym `P_eta`.

Equivalently:

```text
R504_FULL_SPLIT_GENERIC_PRYM_E0_FACTOR=false
R504_FULL_SPLIT_GENERIC_PRYM_E0_HOM=0
R504_FULL_SPLIT_GENERIC_RANK_JUMP_FROM_PRYM=false
```

This is stronger than the previous reciprocal-involution calculation: it excludes a generic **non-bielliptic** `E0` factor as well.

## 7. What remains exceptional

This does not prove that no special rational tuple `(A,B,C,D)` can make the Prym acquire an `E0`-isogeny factor.  Such a factor would be a specialization jump in the Hom lattice.  The previously audited reciprocal loci cover the explicit degree-two/extra-involution mechanism; the present theorem removes the generic Prym mechanism.  What remains is an exceptional isogeny/Hecke locus of special parameters, potentially with unbounded isogeny degree.

The current safe boundary is therefore

```text
R504_FULL_SPLIT_RECIPROCAL_ANALYSIS=CLOSED_WITH_SYMBOLIC_CERTIFICATE_AUDITED_PASS
R504_FULL_SPLIT_GENERIC_PRYM_E0_FACTOR=false
R504_FULL_SPLIT_EXCEPTIONAL_PRYM_E0_ISOGENY_LOCUS=OPEN
R504_FULL_SPLIT_EXCEPTIONAL_PRYM_E0_ISOGENY_DEGREE=UNBOUNDED_NOT_CLASSIFIED
R504_FULL_SPLIT_PRYM_RESIDUAL=NARROWED_TO_EXCEPTIONAL_ISOGENY_JUMP_LOCUS
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_REQUIRED_NOW=true
```

No claim is made that the exceptional locus is empty, finite, or already an external-theorem gate.  A fresh hostile audit should first certify the specialization/generic argument; only after that should Stage25 decide whether the exceptional Hecke locus admits another repo-native bounded-degree attack or has genuinely reached an external theorem boundary.
