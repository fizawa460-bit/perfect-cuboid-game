# Stage32 MB104 — `000707000f0f` e=2 support-specific intermediate `H` quotient model

Status: **RETAINED EXPLICIT `P/H_diag -> B` FUNCTION-FIELD MODEL / RESIDUAL SHEET IS ONE SIMULTANEOUS SIGN BIT / CONDUCTOR PREIMAGE VALUES STILL MISSING / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Put

```text
P=C8 x C8,
G=<T,T',R> ~= (Z/2)^3,
H=<T',TT'R> ~= (Z/2)^2,
X_H=P/H_diag,
B=P/G_diag,
R=C8/H ~= P1_r.
```

For the active support the used singular types are `T'` and `TT'R`; the absent type is `T`. Thus

```text
X_H -> B
```

is the support-specific residual degree-two quotient with deck class represented by diagonal `T`.

This leaf gives an explicit function-field model of that quotient. It does not evaluate a hypothetical carrier branch at a particular point of `X_H`.

## 1. One-factor coordinates

Use the source-locked theta coordinates

```text
a=theta00(w),
e=theta10(w),
b=theta01(w),
c=theta00(2w),
d=theta10(2w)
```

with

```text
a^2=c^2+d^2,
b^2=c^2-d^2,
e^2=2cd.
```

On `d!=0` define

```text
r=e/d,
u=a/d,
v=b/d.
```

Since

```text
r^2=2c/d,
```

we obtain exactly

```text
u^2=(r^4+4)/4,                                (U1)
v^2=(r^4-4)/4.                                (V1)
```

The source-locked sign actions give

```text
T'    : (r,u,v) -> ( r, u,-v),
TT'R  : (r,u,v) -> ( r,-u, v),
T     : (r,u,v) -> (-r, u, v).                (ACT)
```

Therefore `H` fixes `r` and independently changes the signs of `u` and `v`; the residual class `T H` changes only the sign of `r`.

This recovers

```text
k(R)=C(r),
G/H : r -> -r.
```

## 2. Two-factor diagonal-`H` quotient

For the two factors write

```text
(r_z,u_z,v_z),
(r_w,u_w,v_w).
```

Over

```text
R x R=P/(H x H),
```

the quotient

```text
X_H=P/H_diag -> R x R
```

has generic degree `4`. Define the diagonal-`H` invariants

```text
U=u_z*u_w,
V=v_z*v_w.
```

From `(U1)/(V1)`,

```text
U^2=((r_z^4+4)(r_w^4+4))/16,                 (U2)
V^2=((r_z^4-4)(r_w^4-4))/16.                 (V2)
```

The relative group

```text
(H x H)/H_diag ~= H
```

changes the signs of `U` and `V` independently: one generator flips `U`, the other flips `V`. Hence the two quadratic generators account for the full generic degree four, so

```text
k(X_H)=C(r_z,r_w)(U,V)
```

with the two equations `(U2),(V2)`.

The residual deck involution induced by diagonal `T` is

```text
tau:(r_z,r_w,U,V)->(-r_z,-r_w,U,V).          (TAU)
```

Thus

```text
B=X_H/<tau>
```

at the function-field level.

## 3. Exact expression in box coordinates

Use the source-locked two-factor notation

```text
x=theta00(2z), y=theta10(2z),
X=theta00(2w), Y=theta10(2w).
```

Then

```text
C-W3=2yY,
C+W3=2xX,
W1-iW2=2yX,
W1+iW2=2xY.
```

Therefore on the displayed chart

```text
r_z^2 = 2*(C+W3)/(W1-iW2),                   (BZ1)
r_w^2 = 2*(C+W3)/(W1+iW2),                   (BZ2)
r_z*r_w = 2*Z3/(C-W3),                       (BZ3)
U = 2*Z2/(C-W3),                              (BZ4)
V = 2*Z1/(C-W3).                              (BZ5)
```

In particular

```text
r_z^2,
r_w^2,
r_z*r_w,
U,
V
```

are all rational functions on the box quotient `B`. The only residual ambiguity in lifting a generic box point to `X_H` is therefore

```text
(r_z,r_w) <-> (-r_z,-r_w).                   (BIT)
```

Equivalently,

```text
k(X_H)=k(B)(r_z)=k(B)(r_w)
```

on this chart, because `r_z*r_w` is already in `k(B)` and `tau` negates either generator.

This is the full two-factor version of the retained one-factor Kummer equation `r^2=2*f_t`.

## 4. Meaning for the `e=2` equality component

In the retained `e=2` case the product-cover component has stabilizer exactly

```text
K=H.
```

Hence

```text
E=Z/H
```

and the inclusion of the normalized product-cover component `Z` in `P` descends to a rational/morphism-level map on the appropriate normalization chart

```text
j:E -> X_H.
```

The two factor maps `E->R` are simply the `r_z,r_w` projections of this lift.

For two normalization preimages `x_i,x_j` identified by the singular carrier and lying over the same generic point of `B`, the residual bit is now exactly the following two-valued test:

```text
chi_res=0  <=> (r_z,r_w)(x_j)=( r_z,r_w)(x_i),
chi_res=1  <=> (r_z,r_w)(x_j)=(-r_z,-r_w)(x_i).   (PAIR)
```

The invariants `U,V` cannot distinguish the two cases because they are fixed by `tau`, exactly as required.

Equation `(PAIR)` is an explicit ambient evaluator, not an evaluation of any particular Stage32 conductor pair. The missing information is now reduced to the actual specialization of one simultaneous square-root choice on each conductor normalization preimage.

## 5. Relation to the retained residual character and Fourier channel

The involution `(TAU)` is the same finite quotient character used by the retained modular evaluator

```text
chi_res:G->G/H~=Z/2.
```

The recently retained relative-`G` Picard Fourier refinement gives the same character a unique explicit Picard orbit channel `K_res`. The present quotient model gives its function-field channel: the simultaneous sign of `(r_z,r_w)`.

No identification between `K_res` and a divisor of `r_z` or `r_w` is asserted here. A later semantic adapter may compare them only after proving the relevant divisor/pullback statement.

## What remains open

The quotient equation itself is no longer missing. What remains missing is branch-specific data:

```text
normalization preimage x
 -> j(x) in X_H
 -> one of the two simultaneous-sign lifts over its B-point.
```

Equivalently, one still needs the relative sign of `r_z` (or `r_w`) at conductor-identified normalization preimages. Without that specialization there is no conductor sign and no weighted-cut upper bound.

## Firewalls

- All displayed formulas are function-field/chart formulas; no claim is made that one affine chart contains every conductor point.
- The existence of the ambient two-valued lift does not choose a lift for a normalization branch.
- No conductor pair is assigned `chi_res=0` or `1`.
- No equality between the Picard Fourier class `K_res` and the ambient half-branch class is asserted.
- No weighted-cut upper bound is proved.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- Active leaf remains unchanged.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
