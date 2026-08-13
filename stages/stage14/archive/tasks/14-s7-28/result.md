# Stage14-s7-28 — singular classification, primitive-ratio rigidity, and one-pair reconstruction

## Status

`COMPLETE_RATIO_SINGULAR_CLASSIFICATION_AND_PRIMITIVE_MODULUS_PAIR_RECONSTRUCTION`

Stage14-s7-28 consumes merged `s7-27`.  The previous stage reduced the top-theta endpoint to the exact ratio equation

```text
((c_x^+)^2 x^2-(c_x^-)^2)
((c_k^+)^2 y^2-(c_k^-)^2)
 = K x y,

K=16*r*s*X*Y*epsilon_x*epsilon_k,

x=L_x^+/L_x^-,
y=L_k^+/L_k^-.
```

with

```text
gcd(L_x^-,L_x^+)=1,
gcd(L_k^-,L_k^+)=1.
```

The two main conclusions are:

1. the singular/reducible specialization of this `(2,2)` family is classified exactly and is rational;
2. more importantly, the apparent absolute modulus scale is not present on the physical packet at all: the reduced rational ratios recover the four agreement moduli exactly.

After using the original two reciprocal quadratic equations rather than only their product, the moving root product `X*Y` is reconstructed from the primitive modulus data.  Therefore a generic fixed-coefficient genus-one rational-point theorem is **not** the minimal next receiver.  The remaining fixed-power freedom can be placed in one primitive coprime xi-agreement modulus pair, after which the opposite agreement product, the opposite signed split, `X*Y`, switch products and physical cells are divisor/reconstruction data.

No whole-family power saving is promoted here:

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported full signed system

Write

```text
a=c_x^+,
b=c_x^-,
c=c_k^+,
d=c_k^-.
```

All four are positive integers.  Merged s7-27 gives

```text
D-A=b*L_x^-,
D+A=a*L_x^+,

Q-P=d*L_k^-,
Q+P=c*L_k^+,
```

and the exact reciprocal equations

```text
(a L_x^+)^2-(b L_x^-)^2
 =4*r*s*epsilon_k*L_k^-L_k^+,                 (1.1)

(c L_k^+)^2-(d L_k^-)^2
 =4*X*Y*epsilon_x*L_x^-L_x^+.                 (1.2)
```

The quotient quadruple `(a,b,c,d)` has only `B^o(1)` possibilities after fixing `(C,u_res,v_res)`.

The top-theta strip remains

```text
theta=5/16,
3/16 <= phi <= 1/4.
```

---

## 2. Exact singularity criterion for the ratio curve

Consider the affine curve

```text
F(x,y)
 =(a^2 x^2-b^2)(c^2 y^2-d^2)-Kxy=0,          (2.1)
```

where all `a,b,c,d,K` are positive.

The partial derivatives are

```text
F_x=2a^2 x(c^2y^2-d^2)-Ky,
F_y=2c^2 y(a^2x^2-b^2)-Kx.                   (2.2)
```

At an affine singular point, `x` and `y` are nonzero: if one were zero, (2.1) forces the other square factor to vanish, while the transverse derivative is nonzero because `K>0`.

Combining `F=F_x=0` gives

```text
(a^2x^2+b^2)(c^2y^2-d^2)=0.
```

The second factor cannot vanish on a singular point, so

```text
a^2x^2=-b^2.
```

Similarly

```text
c^2y^2=-d^2.
```

Substitution into (2.2) yields

```text
Kxy=4b^2d^2.
```

Squaring gives

```text
K^2=16a^2b^2c^2d^2.                                (2.3)
```

Since the physical coefficient `K` is positive,

```text
boxed:
ratio curve singular
<=> K=4abcd.                                        (2.4)
```

There are no additional singular points at the projective boundary: on `x=infinity` the curve meets `y=+-d/c` and the `x`-transverse derivative contains the nonzero `K` term; symmetrically for `y=infinity`.  The corner `(infinity,infinity)` is not on the curve.

```text
RATIO_CURVE_SINGULAR_IFF_K_EQUALS_4ABCD=true.
```

---

## 3. Singular specialization is explicitly reducible and rational

When `K=4abcd`, (2.1) factors exactly:

```text
F(x,y)
 = [a*x*(c*y-d)-b*(c*y+d)]
   [a*x*(c*y+d)+b*(c*y-d)].                         (3.1)
```

Conversely, with all five coefficients nonzero, a nontrivial reducible `(2,2)` divisor has intersecting components in `P^1 x P^1`; such an intersection is singular.  By (2.4), no other reducible specialization occurs in this coefficient family.

Hence

```text
boxed:
RATIO_CURVE_REDUCIBLE_IFF_SINGULAR=true.            (3.2)
```

On a physical point all signed quantities are positive and

```text
c*y-d = 2P/L_k^- >0,
c*y+d = 2Q/L_k^- >0.
```

Therefore the second factor in (3.1) is strictly positive.  The physical singular branch lies on the first rational component:

```text
a*x*(c*y-d)=b*(c*y+d),                              (3.3)
```

or

```text
boxed:
y = d*(a*x+b)/(c*(a*x-b)).                         (3.4)
```

Using the physical reconstruction

```text
a*x=(D+A)/L_x^-,
b=(D-A)/L_x^-,
```

this is equivalent to

```text
boxed:
(D+A)P=(D-A)Q,                                      (3.5)
```

or

```text
D(Q-P)=A(Q+P).                                      (3.6)
```

Stage14-s7-28 does **not** declare this rational singular branch empty.  It is simply no longer a genus-one problem and must be retained under the same primitive divisibility masks.

```text
SINGULAR_PHYSICAL_BRANCH_RATIONAL=true
SINGULAR_PHYSICAL_BRANCH_EMPTY_PROVED=false.
```

---

## 4. Smooth specialization is genus one only after freezing a nonminimal coefficient

A nonsingular divisor of bidegree `(2,2)` in `P^1 x P^1` has genus

```text
(2-1)(2-1)=1.
```

Thus, if `K` is frozen independently and (2.4) fails, the ratio curve is a smooth genus-one curve.  A physical packet supplies a rational point, so each such frozen physical specialization may be viewed as an elliptic curve after choosing that point.

However

```text
K=16*r*s*X*Y*epsilon_x*epsilon_k
```

contains the moving physical root product `X*Y`.  The charged-once top-theta quantifier does not provide `X*Y` as an independent fixed outer coefficient.  Freezing it first would reintroduce a polynomial root-coordinate support which s7-25 deliberately avoided.

More strongly, the original reciprocal equation (1.2) reconstructs `X*Y` from the primitive modulus data.  Therefore the fixed-`K` genus-one family is a valid derived slice, but it is not the minimal physical receiver.

```text
FIXED_K_SMOOTH_RATIO_CURVE_GENUS_ONE=true
GENERIC_GENUS_ONE_RECEIVER_MINIMAL=false
GENERIC_GENUS_ONE_H_REQUESTED=false.
```

---

## 5. There is no absolute modulus scale: the ratios are already primitive

Merged s7-27 gives

```text
gcd(L_x^-,L_x^+)=1,
gcd(L_k^-,L_k^+)=1.                                 (5.1)
```

Write the rational ratios in lowest terms:

```text
x=u/v,
gcd(u,v)=1,

y=p/q,
gcd(p,q)=1.                                        (5.2)
```

Since

```text
x=L_x^+/L_x^-,
y=L_k^+/L_k^-,
```

and both physical pairs are already coprime, uniqueness of reduced fractions gives exactly

```text
boxed:
(u,v)=(L_x^+,L_x^-),
(p,q)=(L_k^+,L_k^-).                                (5.3)
```

There is no hidden common scale `lambda_x` or `lambda_k` to sum over.

```text
PRIMITIVE_RATIO_RECOVERS_X_MODULUS_PAIR_EXACTLY=true
PRIMITIVE_RATIO_RECOVERS_K_MODULUS_PAIR_EXACTLY=true
ABSOLUTE_MODULUS_SCALE_DEFECT=1.
```

This corrects the only remaining ambiguity in the phrase "ratio/scale solutions" used in s7-27: the physical prime-allocation coprimality has already saturated the scale.

---

## 6. One primitive xi-agreement pair reconstructs the opposite product

Fix the residual triple, one of its `B^o(1)` full quotient quadruples `(a,b,c,d)`, the endpoint-small decorations `(r,s)`, and the finite 2-primary values `(epsilon_x,epsilon_k)`.

Take a primitive positive pair

```text
(u,v)=(L_x^+,L_x^-),
gcd(u,v)=1.                                         (6.1)
```

The signed equations reconstruct

```text
boxed:
D=(a*u+b*v)/2,
A=(a*u-b*v)/2.                                      (6.2)
```

A physical completion requires

```text
D>A>0,
r | A,
s | D,
alpha=A/r,
delta=D/s.                                         (6.3)
```

Equation (1.1) then determines the **entire opposite odd agreement product**:

```text
boxed:
N_k:=L_k^-L_k^+
 = ((a*u)^2-(b*v)^2)/(4*r*s*epsilon_k).             (6.4)
```

For a physical point this is a positive integer and equals `oddpart(alpha*delta)`.

Once `N_k` is fixed, the coprime ordered factorization

```text
N_k=L_k^-L_k^+,
gcd(L_k^-,L_k^+)=1                                 (6.5)
```

has at most divisor-many choices:

```text
# {(L_k^-,L_k^+)} <= tau(N_k)=B^o(1)                (6.6)
```

for each fixed `(u,v)`.

Thus the second modulus ratio is not an independent ambient two-dimensional variable after the first primitive pair is chosen.

```text
OPPOSITE_AGREEMENT_PRODUCT_RECONSTRUCTED_FROM_PRIMITIVE_X_PAIR=true
OPPOSITE_SIGNED_SPLIT_FIXED_X_PAIR_MULTIPLICITY=Bo1.
```

---

## 7. The opposite split reconstructs `P,Q` and `X*Y`

For each divisor-many split (6.5), define

```text
boxed:
Q=(c*L_k^+ + d*L_k^-)/2,
P=(c*L_k^+ - d*L_k^-)/2.                           (7.1)
```

A physical completion requires `Q>P>0` and integral parity.

The full xi-agreement product is

```text
R*J=epsilon_x*u*v.                                  (7.2)
```

Equation (1.2) now reconstructs the moving root product exactly:

```text
boxed:
X*Y
 = ((c*L_k^+)^2-(d*L_k^-)^2)
   /(4*epsilon_x*u*v).                              (7.3)
```

Equivalently, using `4PQ=(Q+P)^2-(Q-P)^2`,

```text
X*Y = P*Q/(R*J).                                    (7.4)
```

There is no independent `X*Y` coefficient left after the primitive modulus pair and opposite split are fixed.

The cell split

```text
R*J=epsilon_x*u*v
```

has divisor-many possibilities.  For each split, the physical root products are forced by

```text
X=P/R,
Y=Q/J,                                              (7.5)
```

when integral, followed by the existing divisor/root/orientation masks.

```text
MOVING_XY_RECONSTRUCTED_FROM_PRIMITIVE_MODULI=true
FIXED_PRIMITIVE_PAIR_ROOT_PRODUCT_MULTIPLICITY=Bo1.
```

---

## 8. Switch products are also reconstructed, not independent

The same primitive pair gives `A,D`, hence

```text
H_k^+=D^2+A^2.                                      (8.1)
```

The common-core identity gives

```text
oddpart(H_k^+)=C*oddpart(S*T).                      (8.2)
```

Therefore

```text
boxed:
oddpart(S*T)=oddpart(H_k^+)/C.                      (8.3)
```

The 2-primary exponent has only `O(log B)=B^o(1)` choices and the split `(S,T)` is divisor-bounded under the balanced-cell masks.

After `P,Q` are reconstructed, the symmetric identity

```text
oddpart(H_xi^+)=C*oddpart(beta*gamma),
H_xi^+=Q^2+P^2                                     (8.4)
```

likewise reconstructs `beta*gamma` up to divisor-many 2-primary/split choices.

Thus, after fixing residual/quotient/small-decoration data, the only fixed-power parameter left before physical masks is the single primitive coprime pair `(u,v)`.

```text
XI_SWITCH_PRODUCT_RECONSTRUCTED_FROM_PRIMITIVE_X_PAIR=true
K_SWITCH_PRODUCT_RECONSTRUCTED_AFTER_OPPOSITE_SPLIT=true.
```

---

## 9. The `(2,2)` curve is a consistency envelope, not the minimal counting object

The product equation from s7-27 is recovered automatically by multiplying (1.1) and (1.2).  Sections 5--8 show the stronger quantifier order:

```text
fixed residual + full quotient decoration + small roots
-> choose one primitive coprime pair (L_x^+,L_x^-)
-> reconstruct A,D and alpha*delta
-> divisor-many signed split (L_k^-,L_k^+)
-> reconstruct P,Q and X*Y
-> divisor-many cell/switch/root completion.         (9.1)
```

Accordingly, the smooth genus-one curve obtained by freezing `X*Y` is not where the remaining multiplicity lives.  The true residual multiplicity is the number of primitive `(u,v)` for which the reconstructed quadratic values satisfy all integrality, balanced-cell, common-core and root-divisibility masks.

Define the new receiver

```text
TopThetaPrimitiveAgreementQuadraticValueDivisibilityIncidence.  (9.2)
```

A convenient first equation is

```text
N_k(u,v)
 = ((a*u)^2-(b*v)^2)/(4*r*s*epsilon_k)              (9.3)
```

with `N_k` required to be a positive integer admitting the physical opposite signed split.  Simultaneously

```text
oddpart(D(u,v)^2+A(u,v)^2)/C                        (9.4)
```

must be a legal balanced xi-switch product.  These are binary quadratic value/divisor conditions on one primitive pair, with reciprocal reconstruction retained.

This is strictly smaller than a generic genus-one rational-point problem.

---

## 10. Singular branch under the primitive parameterization

The singular criterion remains useful as a structural subcase.  On a reconstructed physical packet, `K=4abcd` is equivalent to

```text
(D^2-A^2)(Q^2-P^2)=4ADPQ,                           (10.1)
```

and hence, by positivity, to the rational relation

```text
(D+A)P=(D-A)Q.                                      (10.2)
```

In primitive coordinates this is one additional bilinear relation between `(u,v)` and the divisor-many opposite split.  It is therefore an algebraic subreceiver of (9.2), not a separate elliptic family.

No asymptotic sparsity for this singular subreceiver is claimed yet.

---

## 11. Current exponent and next obligation

What is closed in s7-28:

```text
- exact singular/reducible classification of the ratio biquadratic;
- rational parameterization of the physical singular component;
- exact proof that the physical modulus ratios carry no absolute scale;
- reconstruction of the opposite agreement product from one primitive pair;
- divisor-many reconstruction of the opposite signed split;
- exact reconstruction of X*Y;
- divisor-many reconstruction of switch products/cell splits;
- removal of generic fixed-K genus-one counting as the minimal receiver.
```

Still open:

```text
- average number of primitive (u,v) satisfying the coupled quadratic value/divisibility masks;
- singular subreceiver sparsity;
- a fixed-power saving on the top-theta edge.
```

Therefore

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

---

## 12. H / tH decision

No auxiliary theorem line is started in s7-28.

The anticipated smooth-genus-one H target disappears as the minimal coefficient space once primitive ratio rigidity and the reconstruction of `X*Y` are restored.  The new receiver is an elementary-looking but coupled primitive binary-quadratic value/divisibility problem.  It should first be primewise factorized and tested by gcd/divisor/CRT methods.

```text
TH17_CROSS_PROMOTED_TO_S7_28=false
GENERIC_GENUS_ONE_H_REQUESTED=false
S7_28_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

If s7-29 leaves a genuine average theorem after primewise splitting of (9.3)--(9.4), that theorem should be requested directly for `TopThetaPrimitiveAgreementQuadraticValueDivisibilityIncidence`, not for generic `(2,2)` curves.

---

## Stage boundary

```text
STAGE14_S7_28=COMPLETE_RATIO_SINGULAR_CLASSIFICATION_AND_PRIMITIVE_MODULUS_PAIR_RECONSTRUCTION
MERGED_S7_27_IMPORTED=true
RATIO_CURVE_SINGULAR_IFF_K_EQUALS_4ABCD=true
RATIO_CURVE_REDUCIBLE_IFF_SINGULAR=true
SINGULAR_PHYSICAL_BRANCH_RATIONAL=true
SINGULAR_PHYSICAL_RELATION=(D+A)P=(D-A)Q
SINGULAR_PHYSICAL_BRANCH_EMPTY_PROVED=false
FIXED_K_SMOOTH_RATIO_CURVE_GENUS_ONE=true
GENERIC_GENUS_ONE_RECEIVER_MINIMAL=false
PRIMITIVE_RATIO_RECOVERS_X_MODULUS_PAIR_EXACTLY=true
PRIMITIVE_RATIO_RECOVERS_K_MODULUS_PAIR_EXACTLY=true
ABSOLUTE_MODULUS_SCALE_DEFECT=1
OPPOSITE_AGREEMENT_PRODUCT_RECONSTRUCTED_FROM_PRIMITIVE_X_PAIR=true
OPPOSITE_SIGNED_SPLIT_FIXED_X_PAIR_MULTIPLICITY=Bo1
MOVING_XY_RECONSTRUCTED_FROM_PRIMITIVE_MODULI=true
FIXED_PRIMITIVE_PAIR_ROOT_PRODUCT_MULTIPLICITY=Bo1
XI_SWITCH_PRODUCT_RECONSTRUCTED_FROM_PRIMITIVE_X_PAIR=true
K_SWITCH_PRODUCT_RECONSTRUCTED_AFTER_OPPOSITE_SPLIT=true
REMAINING_RECEIVER=TopThetaPrimitiveAgreementQuadraticValueDivisibilityIncidence
TOP_THETA_PRIMITIVE_AGREEMENT_QUADRATIC_VALUE_DIVISIBILITY_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
TH17_CROSS_PROMOTED_TO_S7_28=false
GENERIC_GENUS_ONE_H_REQUESTED=false
S7_28_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT=Stage14-s7-29
```
