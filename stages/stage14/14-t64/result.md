# Stage14-t64 — square-lifted cross-ratio quotient for the transverse fixed-U obstruction

## Purpose

Merged Stage14-t63 identifies the live fixed-`U` obstruction with the transverse Frobenius / vertical Kummer defect of merged tH15. The remaining issue is arithmetic decorrelation of transverse physical states; functional-analytic wrappers such as full vertical Schatten-4 or generic Bessel are stronger than necessary.

Stage14-t64 returns to the exact projective trace. For the dominant invisible/invisible fixed-`U` branch, it proves that the apparent `(4,4)` K3-type squareclass surface has an exact even quotient of much lower complexity. After passing to squared projective slopes, the squareclass map is a rational cross-ratio, every fixed squareclass quotient is a rational conic, and the only nontrivial lift back to physical slopes is a smooth genus-one Jacobi quartic.

This does **not** prove the transverse energy bound. It replaces the broad K3/incidence formulation by a narrower square-lifted cross-ratio incidence and records exactly why ordinary quadratic large sieve remains circular.

No global Stage14 power saving is claimed.

---

## 1. Inputs and branch scope

Import merged t55, t58, t63 and tH15.

For every reciprocal physical state write

\[
 t=\frac ab,\qquad x=\frac pq.
\]

Merged t55 proves the exact squareclass identity

\[
[\widetilde F]=\left[\frac{x^2-t^2}{1-t^2x^2}\right].
\tag{64.1}
\]

For the dominant invisible fixed-`U` branch, multiplication by fixed primitive `U` is only a row-side PGL2 reparameterization of the moving canonical Gaussian prime, so (64.1) is a legal coordinate description of the same physical state. The t58 reciprocal chamber gives

\[
0<t<x<1.
\tag{64.2}
\]

The mixed invisible/visible branch remains a separate obligation. No asymptotic negligibility is inferred from its small frozen count.

---

## 2. Exact even quotient

Set

\[
T=t^2,\qquad X=x^2.
\tag{64.3}
\]

Define the rational cross-ratio coordinate

\[
\boxed{
R(T,X)=\frac{X-T}{1-TX}.
}
\tag{64.4}
\]

Then (64.1) becomes simply

\[
\boxed{[\widetilde F]=[R(T,X)].}
\tag{64.5}
\]

In integer coordinates,

\[
A=b^2p^2-a^2q^2,
\qquad
B=b^2q^2-a^2p^2,
\tag{64.6}
\]

and

\[
R=\frac AB,
\qquad
\widetilde F=AB,
\qquad
\frac{\widetilde F}{R}=B^2.
\tag{64.7}
\]

Thus the auxiliary quadratic character of a good prime `r` may be written exactly as

\[
\chi_r(\widetilde F)=\chi_r(R),
\tag{64.8}
\]

where the character of the rational number uses `B^{-1}` modulo `r`. Since a quadratic character satisfies `chi(B^{-1})=chi(B)`, (64.8) is identical to `chi_r(AB)`.

This is not a squareclass pre-collapse. Each physical state is still retained, together with its exact rational value `R` and all physical labels.

```text
INVISIBLE_PROJECTIVE_TRACE_FACTORS_THROUGH_SQUARED_SLOPES=true
EXACT_RATIONAL_CROSS_RATIO_COORDINATE_PROVED=true
VERTICAL_KUMMER_CHARACTER_EQUALS_RATIONAL_CROSS_RATIO_CHARACTER=true
STATE_TO_SQUARECLASS_PRECOLLAPSE_USED=false
```

---

## 3. Physical chamber gives a positive unit cross-ratio

From `0<T<X<1`,

\[
X-T>0,
\qquad
1-TX>0.
\]

Moreover

\[
X-T<1-TX
\iff
X(1+T)<1+T
\iff X<1.
\]

Hence every reciprocal physical state satisfies

\[
\boxed{0<R(T,X)<1.}
\tag{64.9}
\]

Thus only positive rational squareclasses occur in this quotient, and the degenerate values `R=0,1,-1` are excluded by the physical chamber.

---

## 4. Fixed squareclass quotient is a rational conic

Let `kappa>0` be a positive squareclass representative. A state lies in squareclass `kappa` iff there exists `w in Q^*` with

\[
R(T,X)=\kappa w^2.
\tag{64.10}
\]

Writing

\[
s=\kappa w^2,
\tag{64.11}
\]

and solving (64.4) for `X` gives the exact Möbius transport

\[
\boxed{
X=M_s(T):=\frac{T+s}{1+sT}.
}
\tag{64.12}
\]

Equivalently the fixed-squareclass double-cover equation may be written

\[
(X-T)(1-TX)=\kappa Z^2,
\tag{64.13}
\]

which, after the even quotient `(t,x)->(T,X)`, is a bidegree `(2,2)` conic-bundle equation with the rational section `X=T, Z=0`.

More explicitly, using `w` itself gives the rational parametrization (64.12). Therefore the generic K3-type label from tH15 is not the minimal geometry for the invisible squareclass problem: the K3 surface is a finite square-lift cover of a rational quotient.

```text
FIXED_SQUARECLASS_EVEN_QUOTIENT_RATIONAL=true
FIXED_SQUARECLASS_MOBIUS_PARAMETERIZATION_PROVED=true
GENERIC_K3_THEOREM_REQUIRED_AT_QUOTIENT_LEVEL=false
```

This does **not** make the physical problem rational, because `T` and `X` are required to be rational squares.

---

## 5. Cayley multiplicativity

Define the Cayley coordinate

\[
C(z)=\frac{1+z}{1-z}.
\tag{64.14}
\]

A direct calculation from (64.12) gives

\[
\boxed{C(X)=C(T)C(s).}
\tag{64.15}
\]

In original integer variables,

\[
C(X)=\frac{p^2+q^2}{q^2-p^2},
\qquad
C(T)=\frac{a^2+b^2}{b^2-a^2},
\tag{64.16}
\]

so

\[
\boxed{
C(R)=
\frac{p^2+q^2}{q^2-p^2}
\frac{b^2-a^2}{a^2+b^2}.
}
\tag{64.17}
\]

Thus the invisible squareclass geometry has an exact split-torus law after squaring and Cayley transform. This is an algebraic identity only; it does not by itself turn the physical canonical-prime / primitive-cover selector into an independent product.

---

## 6. The physical square lift is a Jacobi quartic

Fix the exact cross-ratio value `s` with `0<s<1`. Requiring both `T=t^2` and `X=x^2` to be rational squares turns (64.12) into

\[
\boxed{
x^2=\frac{t^2+s}{1+st^2}.}
\tag{64.18}
\]

Set

\[
y=x(1+st^2).
\]

Then

\[
\boxed{
y^2=(t^2+s)(1+st^2).}
\tag{64.19}
\]

For `s notin {0,1,-1}`, the four branch roots over the algebraic closure are

\[
t=\pm\sqrt{-s},
\qquad
t=\pm\sqrt{-1/s},
\]

and are distinct. Therefore the smooth projective model of (64.19) has genus one.

Because the physical chamber has `0<s<1`, every physical exact-cross-ratio fiber is automatically in the nondegenerate genus-one regime.

This gives a third exact genus-one fibration of the invisible projective geometry: fix the cross-ratio `s`, rather than fixing the row or column coordinate as in the earlier t36/t38 slices.

```text
PHYSICAL_SQUARE_LIFT_JACOBI_QUARTIC_PROVED=true
PHYSICAL_EXACT_CROSS_RATIO_FIBER_GENUS_ONE=true
PHYSICAL_CROSS_RATIO_DEGENERATE_FIBERS_EXCLUDED=true
```

No uniform point-count bound for this moving Jacobi-quartic family is claimed at t64.

---

## 7. Exact transverse equal-squareclass pair geometry

Let two physical invisible states have exact cross-ratios `s_1,s_2 in (0,1)`. Then

\[
[\widetilde F_1]=[\widetilde F_2]
\iff
\frac{s_1}{s_2}\in\mathbf Q^{*2}.
\tag{64.20}
\]

Hence there exists `q in Q^*` with

\[
s_2=s_1/q^2.
\tag{64.21}
\]

Before imposing square lifts, the pair incidence is rational:

\[
X_1=M_{s_1}(T_1),
\qquad
X_2=M_{s_1/q^2}(T_2).
\tag{64.22}
\]

The actual physical incidence is exactly the simultaneous requirement that all four quantities

\[
T_1, X_1, T_2, X_2
\]

are rational squares, together with the fixed-`U` canonical-prime / primitive-`V` / hyperbola / reconstruction masks.

Equivalently, it is a coupled pair of smooth Jacobi quartics whose parameters differ by a rational square.

Define the exact principal receiver

```text
SharedUTransverseJacobiSquareLiftIncidence
```

as the number of transverse physical pairs satisfying (64.20). For the dominant invisible packet this is exactly the transverse principal collision count `I_U^tr` from tH15/t63.

```text
TRANSVERSE_EQUAL_SQUARECLASS_EQUALS_CROSS_RATIO_SQUARE_QUOTIENT=true
TRANSVERSE_PAIR_QUOTIENT_RATIONAL_BEFORE_SQUARE_LIFT=true
TRANSVERSE_PAIR_REDUCES_TO_COUPLED_JACOBI_SQUARE_LIFTS=true
SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED=false
```

---

## 8. Why this does not permit a quadratic-large-sieve shortcut

Equation (64.8) makes the vertical family one-dimensional in the **exact value** `R`. One might therefore try to aggregate states by `R` and apply a quadratic large sieve.

However quadratic characters depend only on the rational squareclass of `R`. If all exact values in one squareclass are aggregated to the associated quadratic character, the coefficient energy contains

\[
\sum_\kappa
\left|\sum_{s:[R_s]=\kappa}a_s\right|^2.
\tag{64.23}
\]

For unit physical weights, the principal term is precisely the unresolved fixed-`U` squareclass energy. Thus exact-value compression followed by character deduplication recreates the same circular coefficient energy identified at tH15/tH16.

The new content of t64 is geometric: it identifies what must be proved about states inside one squareclass, namely square-lifted cross-ratio/Jacobi incidence. It is not a new large-sieve proof.

```text
RATIONAL_CROSS_RATIO_QUADRATIC_LARGE_SIEVE_DIRECT_CLOSURE=false
QUADRATIC_CHARACTER_DEDUPLICATION_RETURNS_SQUARECLASS_ENERGY=true
E4_COEFFICIENT_ENERGY_USED=false
```

---

## 9. New minimal invisible theorem shape

For the dominant fixed-`U` invisible branch, it is sufficient to prove

\[
\boxed{
I_{U,\mathrm{inv}}^{\rm tr}
\ll R_{U,\mathrm{inv}}B^{o(1)},
}
\tag{64.24}
\]

where `I^tr` is expressed by (64.20)--(64.22) and all physical masks remain attached.

This may be viewed equivalently as either

```text
SharedUTransverseJacobiSquareLiftIncidence
```

or the principal part of

```text
SharedUTransverseVerticalKummerDispersion.
```

The former is now the sharper arithmetic-geometric description.

The mixed invisible/visible fixed-`U` branch remains separate and is not closed by the invisible quotient argument.

---

## 10. tH decision

`tH18` is **not needed at t64**.

Reason: t64 does not require importing a new external theorem. It performs an exact internal quotient and discovers that a generic K3/Chebotarev theorem is not yet the right target. The next direct step should exploit the new variables `s=R`, the Cayley product law, and the physical norm/hyperbola constraints to determine whether the moving Jacobi parameter has divisor-scale rigidity or whether a genuinely new uniform incidence theorem remains.

If Stage14-t65 leaves a theorem of the form

```text
uniform square-lifted Jacobi-quartic incidence
or
square-ratio energy for the physical cross-ratio values
```

without an internal arithmetic reduction, that is the correct trigger for tH18.

```text
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

---

## Locked boundary

```text
STAGE14_T64=COMPLETE_SQUARE_LIFTED_CROSS_RATIO_QUOTIENT_AND_JACOBI_FIBRATION
MERGED_T63_IMPORTED=true
MERGED_T55_IMPORTED=true
INVISIBLE_PROJECTIVE_TRACE_FACTORS_THROUGH_SQUARED_SLOPES=true
EXACT_RATIONAL_CROSS_RATIO_COORDINATE_PROVED=true
VERTICAL_KUMMER_CHARACTER_EQUALS_RATIONAL_CROSS_RATIO_CHARACTER=true
PHYSICAL_CROSS_RATIO_RANGE=(0,1)
FIXED_SQUARECLASS_EVEN_QUOTIENT_RATIONAL=true
FIXED_SQUARECLASS_MOBIUS_PARAMETERIZATION_PROVED=true
CAYLEY_MULTIPLICATIVE_IDENTITY_PROVED=true
PHYSICAL_SQUARE_LIFT_JACOBI_QUARTIC_PROVED=true
PHYSICAL_EXACT_CROSS_RATIO_FIBER_GENUS_ONE=true
TRANSVERSE_EQUAL_SQUARECLASS_EQUALS_CROSS_RATIO_SQUARE_QUOTIENT=true
TRANSVERSE_PAIR_REDUCES_TO_COUPLED_JACOBI_SQUARE_LIFTS=true
GENERIC_K3_THEOREM_REQUIRED_AT_QUOTIENT_LEVEL=false
RATIONAL_CROSS_RATIO_QUADRATIC_LARGE_SIEVE_DIRECT_CLOSURE=false
QUADRATIC_CHARACTER_DEDUPLICATION_RETURNS_SQUARECLASS_ENERGY=true
SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-t65 exploit the exact cross-ratio/Cayley/Jacobi variables together with fixed-U norm, canonical-prime and sharp hyperbola constraints; decide whether the moving s-parameter has divisor-scale rigidity or requires a new incidence theorem
```
