# Stage14-X5 — singular locus of the reciprocal biquadratic ratio family

## Status

`COMPLETE_RECIPROCAL_BIQUADRATIC_SINGULAR_LOCUS_AND_POSITIVE_COMPONENT_REDUCTION`

Merged Stage14-s7-27 has now reached the same exact scale-free bidegree `(2,2)` ratio equation that X5 was independently deriving. X5 therefore does not claim that reduction as new. Instead it consumes the merged ratio receiver and classifies its singular/reducible coefficient fibers exactly.

The outcome is sharp:

```text
- after a positive diagonal rescaling, every ratio fiber is
    (u^2-1)(v^2-1)=lambda*u*v;
- physical lambda is strictly positive;
- for lambda>0, the projective (2,2) curve is singular/reducible iff lambda=4;
- lambda=4 factors into two (1,1) components;
- the physical chamber u>1,v>1 can lie on only one component;
- the singular physical branch is the exact Möbius relation
    D(Q-P)=A(Q+P),
  equivalently A/D + P/Q + (A/D)(P/Q)=1;
- every lambda>0, lambda!=4 fiber is a smooth geometrically irreducible genus-one curve.
```

No whole-family power saving is claimed. The current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

The remaining X problem splits cleanly into a rational singular branch and a smooth genus-one branch.

---

## 1. Imported exact ratio receiver

Use the merged s7-27 notation. After fixing the charged-once common-core residual data and one of the `B^o(1)` full signed quotient quadruples, the four odd agreement moduli satisfy

```text
(L_x^+ c_x^+)^2-(L_x^- c_x^-)^2
 =4*r*s*epsilon_k*L_k^-*L_k^+,

(L_k^+ c_k^+)^2-(L_k^- c_k^-)^2
 =4*X*Y*epsilon_x*L_x^-*L_x^+.
```

Put

```text
x=L_x^+/L_x^-,
y=L_k^+/L_k^-.
```

Merged s7-27 proves the exact ratio equation

```text
((c_x^+)^2*x^2-(c_x^-)^2)
((c_k^+)^2*y^2-(c_k^-)^2)
 =K*x*y,                                           (1.1)

K=16*r*s*X*Y*epsilon_x*epsilon_k>0.                (1.2)
```

No dominant-sign split is needed.

---

## 2. Universal positive normalization

All quotient factors are positive. Define

```text
u := (c_x^+/c_x^-)*x,
v := (c_k^+/c_k^-)*y,                              (2.1)
```

and

```text
lambda
 := K/(c_x^-*c_x^+*c_k^-*c_k^+).                  (2.2)
```

Then (1.1) becomes exactly

```text
boxed:
(u^2-1)(v^2-1)=lambda*u*v.                         (2.3)
```

Every factor in (2.2) is positive, so

```text
boxed:
lambda>0.                                          (2.4)
```

At an actual physical packet,

```text
u=(D+A)/(D-A)>1,
v=(Q+P)/(Q-P)>1.                                (2.5)
```

This chamber information will distinguish the two components of the unique positive singular fiber.

---

## 3. No singular points at infinity for nonzero lambda

Compactify (2.3) in `P^1 x P^1`:

```text
(U1^2-U0^2)(V1^2-V0^2)
-lambda*U1*U0*V1*V0=0.                             (3.1)
```

If `U0=0`, then `V1^2-V0^2=0`, so the only boundary points are `v=+1` and `v=-1`. In the local coordinate `z=U0/U1`, the equation is

```text
(1-z^2)(v^2-1)-lambda*z*v=0.
```

At `z=0`, `v=+/-1`, the `z` derivative is `-lambda*v`, nonzero for `lambda!=0`. The same argument applies with `u,v` reversed. The point `u=v=infinity` is not on the curve.

Hence

```text
boxed:
all singularities for lambda!=0 are affine.        (3.2)
```

---

## 4. Exact affine singular-locus calculation

Write

```text
F(u,v)=(u^2-1)(v^2-1)-lambda*u*v.
```

Then

```text
F_u=2u(v^2-1)-lambda*v,
F_v=2v(u^2-1)-lambda*u.                             (4.1)
```

For `lambda!=0`, a singular point cannot have `u=0` or `v=0`: the possible curve points on either axis have the other coordinate `+/-1`, where the transverse derivative is nonzero.

Thus at a singular point `uv!=0`. Equating the two expressions for `lambda` from (4.1) gives

```text
u^2(v^2-1)=v^2(u^2-1),
```

hence

```text
u^2=v^2.                                           (4.2)
```

There are two cases.

### Case `v=u`

The derivative equation gives

```text
lambda=2(u^2-1).
```

Using `F=0`, and excluding `lambda=0`, yields

```text
u^2=-1,
lambda=-4.                                         (4.3)
```

### Case `v=-u`

Now

```text
lambda=-2(u^2-1),
```

and `F=0` yields

```text
u^2=-1,
lambda=+4.                                         (4.4)
```

Therefore, over characteristic zero,

```text
boxed:
for lambda!=0, singular fibers occur exactly at
lambda=+4 or lambda=-4.                             (4.5)
```

Since the physical family has `lambda>0`, only

```text
boxed:
PHYSICAL_SINGULAR_LAMBDA=4.                        (4.6)
```

can occur.

`lambda=0` is the obvious four-line degeneration `(u^2-1)(v^2-1)=0`, but is impossible in the physical family by (2.4).

---

## 5. Reducibility is classified at the same time

For `lambda=4`, the universal polynomial factors exactly:

```text
(u^2-1)(v^2-1)-4uv
=(uv+u+v-1)(uv-u-v-1).                             (5.1)
```

For `lambda=-4` there is an analogous pair of `(1,1)` components.

Conversely, for `lambda!=0,+/-4`, Section 3-4 proves the projective `(2,2)` curve is smooth. Any nontrivial decomposition of a divisor of bidegree `(2,2)` on `P^1 x P^1` has components with positive intersection somewhere; such an intersection would be singular. Therefore the smooth fibers are geometrically irreducible.

Hence on the physical positive family

```text
boxed:
ratio fiber reducible/singular iff lambda=4.       (5.2)
```

Every `lambda>0`, `lambda!=4` fiber is a smooth geometrically irreducible genus-one curve, since a smooth `(2,2)` curve has genus `(2-1)(2-1)=1`.

```text
SMOOTH_PHYSICAL_RATIO_FIBER_GENUS=1.               (5.3)
```

---

## 6. Only one singular component meets the physical chamber

At a physical point, (2.5) gives `u>1` and `v>1`. Therefore

```text
uv+u+v-1>0,
```

so the first component in (5.1) cannot vanish.

The physical singular branch is exactly

```text
boxed:
uv-u-v-1=0,                                        (6.1)
```

or

```text
boxed:
(u-1)(v-1)=2.                                      (6.2)
```

It has the rational Möbius parameterization

```text
v=(u+1)/(u-1),
u>1.                                                       (6.3)
```

The other `(1,1)` component has no positive physical point with `u,v>1`.

---

## 7. Physical host form of the singular branch

From (2.5), put

```text
t=A/D in (0,1),
z=P/Q in (0,1).
```

Then

```text
u=(1+t)/(1-t),
v=(1+z)/(1-z).                                    (7.1)
```

Substitution into (6.1) gives

```text
boxed:
t+z+t*z=1.                                        (7.2)
```

Equivalently,

```text
boxed:
D(Q-P)=A(Q+P),                                     (7.3)
```

or equally

```text
boxed:
Q(D-A)=P(D+A).                                     (7.4)
```

This is a new exact description of the dangerous singular branch in the original physical host variables.

The physical coefficient parameter can also be written without quotient decorations:

```text
lambda
 =16*A*D*P*Q / ((D^2-A^2)(Q^2-P^2)).              (7.5)
```

Thus `lambda=4` is exactly

```text
(D^2-A^2)(Q^2-P^2)=4*A*D*P*Q,                     (7.6)
```

whose positive factorization is (7.2).

---

## 8. Receiver split

The merged s7-27 receiver now splits disjointly into two theorem shapes.

### Singular rational receiver

```text
SingularPositiveReciprocalMobiusIncidence
```

counts physical packets satisfying

```text
lambda=4,
D(Q-P)=A(Q+P),
```

with the full charged-once residual, signed-quotient, squarefree-cell, orientation and reconstruction masks.

This is a rational `(1,1)` branch, so a generic elliptic-curve theorem is irrelevant here. It must be attacked by its primitive ratio and remaining absolute-scale/divisor equations.

### Smooth genus-one receiver

```text
SmoothChargedOnceReciprocalEllipticRatioIncidence
```

counts the `lambda>0`, `lambda!=4` fibers. These are uniformly smooth geometrically irreducible genus-one curves as abstract fibers; what is not yet proved is the **physical height/lift transfer and average rational-point bound** across the moving coefficient family.

The two receivers must not be recombined by a generic `(2,2)` point count that loses the singular distinction.

---

## 9. Finite diagnostic and theorem boundary

The dedicated X5 audit checks the universal factor identities and runs the merged s7-27 physical enumeration. It records the number of finite `lambda=4` physical packets as a diagnostic only.

No finite absence or rarity is promoted to an asymptotic statement.

The exact asymptotic facts proved in X5 are the singular-locus classification, factorization, positive-component selection and host identity (7.3).

Still unproved:

```text
SINGULAR_POSITIVE_RECIPROCAL_MOBIUS_INCIDENCE_PROVED=false
PHYSICAL_SMOOTH_RATIO_CURVE_HEIGHT_TRANSFER_PROVED=false
SMOOTH_CHARGED_ONCE_RECIPROCAL_ELLIPTIC_RATIO_INCIDENCE_PROVED=false
```

Therefore

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

---

## 10. H / tH decision

No X5-specific H line is needed yet.

The singular branch is now elementary/Möbius and should be exhausted algebraically first. The smooth branch has a legitimate genus-one theorem shape, but its physical height map and coefficient averaging are not yet frozen. X6 should:

```text
1. primitive-reduce D(Q-P)=A(Q+P) and attack the singular scale/product fiber;
2. derive the exact height/lift map for lambda!=4 smooth fibers;
3. only then decide whether an elliptic-height/rank H audit is useful.
```

```text
X5_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false.
```

---

## Boundary

```text
STAGE14_X5=COMPLETE_RECIPROCAL_BIQUADRATIC_SINGULAR_LOCUS_AND_POSITIVE_COMPONENT_REDUCTION
MERGED_X4_IMPORTED=true
MERGED_S7_27_IMPORTED=true
X1_CHARGED_ONCE_QUANTIFIER_ORDER_PRESERVED=true
NORMALIZED_RATIO_CURVE=(u^2-1)(v^2-1)=lambda*u*v
PHYSICAL_LAMBDA_POSITIVE=true
NONZERO_RATIO_CURVE_SINGULAR_LAMBDA_VALUES=+4,-4
PHYSICAL_SINGULAR_LAMBDA=4
PHYSICAL_RATIO_FIBER_SINGULAR_OR_REDUCIBLE_IFF_LAMBDA_4=true
LAMBDA_4_FACTORIZATION=(uv+u+v-1)(uv-u-v-1)
PHYSICAL_RATIO_CHAMBER=u>1,v>1
PHYSICAL_SINGULAR_COMPONENT=uv-u-v-1=0
PHYSICAL_SINGULAR_SLOPE_IDENTITY=A/D+P/Q+(A/D)*(P/Q)=1
PHYSICAL_SINGULAR_HOST_IDENTITY=D*(Q-P)=A*(Q+P)
SMOOTH_PHYSICAL_RATIO_FIBER_GENUS=1
SMOOTH_PHYSICAL_RATIO_FIBER_GEOMETRICALLY_IRREDUCIBLE=true
SINGULAR_POSITIVE_RECIPROCAL_MOBIUS_INCIDENCE_PROVED=false
PHYSICAL_SMOOTH_RATIO_CURVE_HEIGHT_TRANSFER_PROVED=false
SMOOTH_CHARGED_ONCE_RECIPROCAL_ELLIPTIC_RATIO_INCIDENCE_PROVED=false
REMAINING_RECEIVERS=SingularPositiveReciprocalMobiusIncidence+SmoothChargedOnceReciprocalEllipticRatioIncidence
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
X5_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
NEXT_RECOMMENDED=Stage14-X6 primitive-reduce the singular Mobius branch and derive the smooth-fiber physical height/lift map before any elliptic H audit
```
