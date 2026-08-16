# Stage27-19-r401c — affine-linear moving-u multisection classification

```text
TASK_ID=Stage27-19-r401c
OWNER_STAGE=Stage27
PARENT_ROUTE=Stage27-19-r401b
TRIGGER_CHECKPOINT=40
ROUTE_KIND=LOWER_REENTRY
ROUTE_LABEL=AFFINE_LINEAR_MOVING_U_CLASSIFICATION
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Audited parent boundary

Stage27-19-r401b hostile audit passed and PR #1033 merged at

```text
dcc04e4d778aaaa31f9abb0d39dd98117c33ddb4
```

The current lower remains

\[
N_2(B)\gg B^{1/4},
\]

and the accepted lower-progress gate remains

\[
\kappa/h>1/4.
\]

The natural split fibration from r401a is

\[
\tau V^2=G_\tau(u),
\]

where

\[
G_\tau(u)=(u^2+\tau+1)
\bigl((\tau+2)u^2-4(\tau+1)u+(\tau+1)(\tau+2)\bigr).
\]

r401b closed all constant rational `u=c` as rational-parametric escapes: the only rational genus-zero degenerations are nonphysical boundary cases. The present route classifies the next complete ansatz

\[
\boxed{u=a\tau+b,\qquad a,b\in\mathbf Q.}
\]

No physical-height promotion is attempted unless a nondegenerate genus-zero member survives.

## 2. Exact affine-linear base receiver

Put

\[
H_{a,b}(\tau):=\tau G_\tau(a\tau+b).
\]

Then the affine-linear pullback is the double cover

\[
\boxed{S^2=H_{a,b}(\tau)},
\qquad S=\tau V.
\]

For `a!=0`, `H_{a,b}` is a degree-six polynomial in `tau` with leading coefficient `a^4`. Therefore a squarefree member has genus two.

Write

\[
A_{a,b}(\tau)=(a\tau+b)^2+\tau+1,
\]

\[
Q_{a,b}(\tau)=(\tau+2)(a\tau+b)^2
-4(\tau+1)(a\tau+b)+(\tau+1)(\tau+2),
\]

so that

\[
H_{a,b}(\tau)=\tau A_{a,b}(\tau)Q_{a,b}(\tau).
\]

Direct expansion gives the exact auxiliary invariants

\[
\operatorname{Disc}_\tau(A_{a,b})=-(4a^2-4ab-1),
\]

\[
\operatorname{Disc}_\tau(Q_{a,b})=-(b-1)^2F(a,b),
\]

\[
\operatorname{Res}_\tau(A_{a,b},Q_{a,b})=16a^3(a-b)^3,
\]

and

\[
A_{a,b}(0)=b^2+1,
\qquad
Q_{a,b}(0)=2(b-1)^2,
\]

where

\[
\boxed{
\begin{aligned}
F(a,b)={}&16a^4-32a^3b+20a^2b^2-32a^2b+44a^2\\
&-4ab^3+32ab^2-44ab-b^2+6b-1.
\end{aligned}}
\]

Using `Disc(fg)=Disc(f)Disc(g)Res(f,g)^2` repeatedly yields

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_\tau(H_{a,b})={}&1024a^6(a-b)^6(b-1)^6(b^2+1)^2\\
&\times(4a^2-4ab-1)F(a,b).
\end{aligned}}
\]

Thus the generic moving affine-linear pullback is genus two, not genus zero or genus one.

```text
AFFINE_LINEAR_RECEIVER_DERIVED=true
AFFINE_LINEAR_GENERIC_DEGREE=6
AFFINE_LINEAR_GENERIC_GENUS=2
AFFINE_LINEAR_DISCRIMINANT_FACTORIZATION_PROVED=true
```

## 3. Rational discriminant components

The factor `b^2+1` has no rational zero. For `a!=0`, every rational discriminant-zero affine line therefore lies on at least one of the four components

\[
C_R:a=b,
\qquad
C_0:b=1,
\]

\[
C_A:4a^2-4ab-1=0,
\qquad
C_Q:F(a,b)=0.
\]

Each has a direct geometric meaning:

- `C_R`: `A` and `Q` share a root, because `Res(A,Q)=0`;
- `C_0`: the root `tau=0` collides with the `Q` factor;
- `C_A`: the quadratic `A` acquires a double root;
- `C_Q`: the cubic `Q` acquires a repeated root.

Away from intersections of these components, exactly one square factor is removed. The squareclass model then has degree four, hence genus one. In particular, a single discriminant mechanism never creates a genus-zero moving family.

Two useful exact factorizations are

\[
a=b\quad\Longrightarrow\quad
H=\tau(\tau+1)^2
(a^2\tau+a^2+1)
\bigl(a^2\tau^2+3a^2\tau+2a^2-4a\tau-4a+\tau+2\bigr),
\]

and

\[
b=1\quad\Longrightarrow\quad
H=\tau^3
(a^2\tau+2a^2-2a+1)
(a^2\tau^2+2a\tau+\tau+2).
\]

After deleting the displayed square factors, both are quartic double covers.

On `C_A`, writing

\[
b=a-\frac1{4a}
\]

makes the entire `A` factor a square; after deleting it, the squareclass is `tau` times a cubic, again degree four.

On `C_Q`, the cubic `Q` has a repeated rational factor over `Q` (the gcd with its derivative is nonconstant over `Q[tau]`); after deleting the square factor, the remaining squareclass is again degree four unless another discriminant mechanism occurs.

```text
AFFINE_LINEAR_SINGLE_DEGENERATION_GENUS=1
AFFINE_LINEAR_CODIM1_GENUS_ZERO_ROUTE=false
```

## 4. Simultaneous degenerations over Q

A genus-zero affine-linear escape would require at least two independent degeneration mechanisms (or an equivalent higher collision). The pairwise intersections can be checked exactly.

For `C_R`:

\[
F(a,a)=-a^2+6a-1,
\qquad
(4a^2-4ab-1)|_{b=a}=-1.
\]

Hence `C_R cap C_A` is empty and `C_R cap C_Q` has only

\[
a=3\pm2\sqrt2,
\]

so no rational point. The intersection `C_R cap C_0` is the single rational point

\[
(a,b)=(1,1).
\]

For `C_0`:

\[
F(a,1)=4(2a^2-2a+1)^2,
\]

which has no rational zero, while

\[
4a^2-4a-1=0
\]

has discriminant `32`, so `C_0 cap C_A` also has no rational point.

Finally,

\[
\operatorname{Res}_a(4a^2-4ab-1,F(a,b))
=256(2b-11)^2.
\]

Thus a point of `C_A cap C_Q` must have `b=11/2`, after which

\[
4a^2-22a-1=0
\]

has discriminant `500=100\cdot5`, so again there is no rational point.

Therefore the only rational simultaneous degeneration among moving affine-linear lines is

\[
\boxed{(a,b)=(1,1).}
\]

But this is precisely

\[
u=\tau+1,
\]

and r401b already proved that the reconstruction satisfies

\[
\boxed{z=1}
\]

identically. It is entirely outside the nondegenerate Stage19 physical population.

The `a=0` degree-drop locus is exactly the constant-u route already classified in r401b: every rational nondegenerate member is genus one, while its genus-zero degenerations are also nonphysical.

Hence

\[
\boxed{
\text{there is no nondegenerate physical genus-zero member in the full affine-linear ansatz }u=a\tau+b.
}
\]

```text
AFFINE_LINEAR_RATIONAL_SIMULTANEOUS_DEGENERATION=(1,1)_ONLY
AFFINE_LINEAR_ONLY_RATIONAL_GENUS_ZERO_MOVING_LINE=u=tau+1
AFFINE_LINEAR_ONLY_RATIONAL_GENUS_ZERO_MOVING_LINE_PHYSICAL=false
AFFINE_LINEAR_PHYSICAL_GENUS_ZERO_ROUTE_EXISTS=false
ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=true
```

## 5. Lower-bound consequence

This result closes a natural low-degree shortcut but does not improve the lower exponent. There is no surviving affine-linear rational curve on which to perform a new physical-height count.

The current theorem remains

\[
\boxed{N_2(B)\gg B^{1/4}}.
\]

No claim is made that all degree-two multisections of the surface arise from `u=a tau+b`, and no claim is made that the master surface is nonrational in every birational model.

The next useful calibration is nonlinear: either

1. classify quadratic moving `u=a tau^2+b tau+c` degenerations, or
2. embed the already-audited R501/R502 quarter-power families into the `(tau,u)` fibration to learn which nonlinear multisection degree and physical-height growth a genuine physical family actually has.

The second option is preferred because it calibrates the fibration against known physical Stage19 families before a larger blind polynomial search.

```text
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
MASTER_SURFACE_RATIONALITY_DISPROVED=false
ALL_DEGREE_TWO_MULTISECTIONS_CLASSIFIED=false
```

## 6. Frozen exit

```text
STAGE27_19_R401C_ATTACK_EXECUTED=true
PARENT_R401B_AUDITED_PASS_MERGED=true
AFFINE_LINEAR_RECEIVER_DERIVED=true
AFFINE_LINEAR_GENERIC_GENUS=2
AFFINE_LINEAR_DISCRIMINANT_FACTORIZATION_PROVED=true
AFFINE_LINEAR_SINGLE_DEGENERATION_GENUS=1
ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=true
AFFINE_LINEAR_PHYSICAL_GENUS_ZERO_ROUTE_EXISTS=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_DERIVED_ROUTE=27-19-r401d
NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit
```
