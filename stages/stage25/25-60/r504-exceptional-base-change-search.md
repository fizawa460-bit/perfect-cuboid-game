# Stage25-60 R504 exceptional base-change search

STATUS=ACTIVE_RESEARCH
ROUTE=R504
CHECKPOINT=60

## Purpose

The hostile repair-2 audit left exactly one repo-native lane live:

```text
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
```

This artifact executes that search rather than relabeling it as an external gate.

## Previously closed concrete candidates

The already audited candidates are

```text
BC1: phi(u)=u^2 -> CLOSED_NO_RANK_JUMP
BC2: phi(u)=(u^2-1)/(2u) -> CLOSED_NO_RANK_JUMP
```

The later symbolic mutations are also closed:

```text
BC3: phi_a(u)=(u^2-a)/(2u)
J3(a)=-1024*a*(8*a^2+9)
R504_BC3_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR

BC4: phi_a(u)=(u^2+a)/(2u)
J4(a)=+1024*a*(8*a^2+9)
R504_BC4_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR

BC5: phi_a(u)=a*u^2
extra quotient j-invariants=8000,8000
R504_BC5_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
```

No finite parameter scan is used in these closures.

## Correct general degree-two normalization

The previous note that degree-two branch data was one-dimensional was too aggressive. The target coordinate `k` is fixed by the quartic `k^4+1`; only its finite dihedral automorphism group is available. Modulo source `PGL2`, a generic degree-two rational map therefore has a two-dimensional unordered branch-value parameter.

After moving the two ramification points on the source to `0` and `infinity` and using the residual scaling of the source coordinate, a generic map may be written

\[
\boxed{\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1}},
\]

with `a != b`; the values `b` and `a` are its branch values at `0` and `infinity`.

The pullback twist cover is

\[
C_{a,b}:\quad y^2=(a u^2+b)^4+(u^2+1)^4.
\]

It is an even genus-three hyperelliptic curve. The involution `u -> -u` gives the inherited quotient birational to `s^2=k^4+1`, hence the inherited `E0` factor.

```text
R504_GENERAL_DEGREE2_NORMAL_FORM=phi_(a,b)(u)=(a*u^2+b)/(u^2+1)
R504_GENERAL_DEGREE2_PARAMETER_DIMENSION=2
R504_PREVIOUS_ONE_DIMENSION_BRANCH_CLAIM=SUPERSEDED
```

## Full extra-involution locus in the normalized two-parameter family

Write

\[
Q_{a,b}(x)=(ax+b)^4+(x+1)^4
=A x^4+B x^3+C x^2+D x+E,
\]
where
\[
A=a^4+1,\quad B=4(a^3b+1),\quad C=6(a^2b^2+1),
\]
\[
D=4(ab^3+1),\quad E=b^4+1.
\]

A second rational involution of the form
\[
u\mapsto \lambda/u
\]
requires the reciprocal symmetry
\[
D=L B,\qquad E=L^2 A,
\]
with `L=lambda^2 in Q^(2)`. Eliminating `L` gives the exact algebraic condition

\[
\boxed{E B^2-A D^2
=16(a-b)^3(a+b)(ab-1)(ab+1)=0.}
\]

Thus every extra-involution member of this normalized family lies on one of four explicit loci. The locus `a=b` is degree-zero/constant and is discarded. For a Q-rational involution, the nondegenerate loci reduce to

```text
L1: a=-b, with L=1;
L2: ab=1, with L=a^(-2).
```

The factor `ab=-1` has `L=-a^(-2)` and therefore supplies no Q-rational involution.

```text
R504_GENERAL_EXTRA_INVOLUTION_LOCUS=(a-b)^3*(a+b)*(ab-1)*(ab+1)=0
R504_Q_RATIONAL_EXTRA_INVOLUTION_NONDEGENERATE_LOCI=a_plus_b_zero;ab_equal_1
```

## L1: a=-b

Here the extra involution is `u -> 1/u`. The complementary elliptic quotient has binary-quartic invariants

\[
I=64a^4(4a^4+3),
\]
\[
\boxed{J=-1024a^8(8a^4+9)}.
\]

For nonzero rational `a`, `J` never vanishes. Hence this full one-dimensional locus has no complementary `j=1728` quotient and no extra quotient Q-isogenous to `E0` through this involution.

```text
R504_GENERAL_INVOLUTION_LOCUS_L1_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
```

## L2: ab=1

Put `b=1/a`, `a != 0,1`. The Q-rational involution is `u -> (1/a)/u`. The complementary quotient has

\[
I=8(a-1)^4(5a^4+4a^3+6a^2+4a+5)/a^2,
\]
\[
\boxed{
J=-64(a-1)^8(a^2+a+1)(7a^2+10a+7)/a^3.
}
\]

The two quadratic factors have negative discriminant, and `a=1` is the constant-map degeneration. Therefore no nondegenerate rational point on this locus gives `J=0`.

```text
R504_GENERAL_INVOLUTION_LOCUS_L2_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
```

## What this proves, and what it does not

This closes the **entire Q-rational extra-involution / bielliptic-quotient locus** inside the generic normalized degree-two family. It is stronger than checking finitely many ansatz classes.

It does **not** prove that an arbitrary `C_{a,b}` cannot have an `E0`-isogeny factor in its Jacobian arising from a higher-degree map to an elliptic curve without an extra curve involution. Such an elliptic factor need not be visible as a degree-two quotient.

Therefore the remaining live object is now narrower:

```text
R504_EXTRA_INVOLUTION_DEGREE2_LOCUS=CLOSED_WITH_SYMBOLIC_CERTIFICATE
R504_RESIDUAL=NON_BIELLIPTIC_E0_ISOGENY_FACTOR_LOCUS_IN_PRYM_SURFACE
R504_GENERAL_DEGREE2_FULL_RANK_JUMP_CLASSIFICATION_PROVED=false
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_PRYM_ISOGENY_LOCUS
R504_NEW_RANK_JUMP_PROVED=false
R504_NEW_STAGE19_FAMILY_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

## Next attack

Study the two-dimensional Prym surface of `C_(a,b) -> E0`. The next theorem-level target is to determine whether the locus where this Prym admits an elliptic factor Q-isogenous to `E0` is empty, a proper algebraic curve, or contains a rationally parametrized component. A proof must use a Prym/Humbert/isogeny invariant or produce an explicit higher-degree map `C_(a,b) -> E0`; absence of an additional involution alone is not sufficient.
