# Stage14-4cn — primitive ratio injectivity and reciprocal Edwards/Jacobi split

## Status

`COMPLETE_PRIMITIVE_RATIO_INJECTIVITY_AND_RECIPROCAL_EDWARDS_SINGULAR_SMOOTH_SPLIT`

Stage14-4cn consumes merged `14-4cm` and merged `s7-27` on the same top-theta common-core packet.

Merged `s7-27` already proves that after fixing `(C,u_res,v_res)`, the full signed quotient quadruple is divisor-bounded and all fixed-power agreement freedom is carried by four odd moduli

```text
L_x^-, L_x^+, L_k^-, L_k^+.
```

They satisfy

```text
(L_x^+ c_x^+)^2-(L_x^- c_x^-)^2
 = 4*r*s*epsilon_k*L_k^-*L_k^+,

(L_k^+ c_k^+)^2-(L_k^- c_k^-)^2
 = 4*X*Y*epsilon_x*L_x^-*L_x^+.
```

Stage14-4cn proves three further facts:

1. the modulus-ratio map has no hidden scale multiplicity because each allocation pair is primitive;
2. the `(2,2)` ratio equation has a canonical reciprocal Edwards/Jacobi form;
3. the only possible physical singular specialization is `lambda=4`, giving one explicit Cayley-type rational component.

No whole-family power saving is claimed. The unconditional endpoint remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported exact packet

Use

```text
A=alpha*r,
D=delta*s,
P=R*X,
Q=J*Y,

r=r_1*r_2,
s=s_1*s_2,
X=x_1*x_2,
Y=y_1*y_2,
```

with

```text
D>A>0,
Q>P>0.
```

The complete odd agreement allocations are

```text
L_x^- = gcd(oddpart(R*J),D-A),
L_x^+ = gcd(oddpart(R*J),D+A),

L_k^- = gcd(oddpart(alpha*delta),Q-P),
L_k^+ = gcd(oddpart(alpha*delta),Q+P).
```

Merged `4cm/s7-27` give exactly

```text
L_x^-*L_x^+ = oddpart(R*J),
gcd(L_x^-,L_x^+)=1,

L_k^-*L_k^+ = oddpart(alpha*delta),
gcd(L_k^-,L_k^+)=1.                         (1.1)
```

Retain both signed quotients

```text
c_x^-=(D-A)/L_x^-,
c_x^+=(D+A)/L_x^+,

c_k^-=(Q-P)/L_k^-,
c_k^+=(Q+P)/L_k^+.
```

For fixed `(C,u_res,v_res)` their full quadruple has only `B^o(1)` possibilities by merged `s7-27`.

Let

```text
epsilon_x=(R*J)/oddpart(R*J),
epsilon_k=(alpha*delta)/oddpart(alpha*delta).
```

---

## 2. Primitive ratio injectivity

Define

```text
x=L_x^+/L_x^-,
y=L_k^+/L_k^-.
```

Because of (1.1), both fractions are already in lowest terms. Hence

```text
boxed:
(L_x^-,L_x^+)=(den(x),num(x)),
(L_k^-,L_k^+)=(den(y),num(y)).                (2.1)
```

Therefore

```text
boxed:
(x,y) determines the four odd allocation moduli uniquely.      (2.2)
```

The ratio map has exact fiber one.

The wording in `s7-27` that one keeps the ratio equation together with one scale equation can now be sharpened: after canonical primitive lifting, the remaining original reciprocal equation is a **filter** on that unique lift, not a separate moving scale with additional multiplicity.

Once the products

```text
R*J=epsilon_x L_x^-L_x^+,
alpha*delta=epsilon_k L_k^-L_k^+
```

are fixed, their labelled squarefree cell splits are divisor-many. The switched products and physical roots remain subject to the already merged reconstruction masks. No polynomial scale charge is introduced by passing to `(x,y)`.

This does not say every rational ratio point is physical; the original reciprocal equation and all physical masks may still reject it.

---

## 3. Canonical reciprocal Edwards/Jacobi form

Merged `s7-27` gives

```text
((c_x^+)^2*x^2-(c_x^-)^2)
((c_k^+)^2*y^2-(c_k^-)^2)
 =16*r*s*X*Y*epsilon_x*epsilon_k*x*y.        (3.1)
```

Scale the rational coordinates by the fixed quotient decoration:

```text
u=(c_x^+/c_x^-)*x=(D+A)/(D-A),

v=(c_k^+/c_k^-)*y=(Q+P)/(Q-P).              (3.2)
```

Every physical point lies in

```text
u>1,
v>1.                                           (3.3)
```

Then (3.1) becomes exactly

```text
boxed:
(u^2-1)(v^2-1)=lambda*u*v,                    (3.4)
```

with

```text
boxed:
lambda =
  16*r*s*X*Y*epsilon_x*epsilon_k
  /(c_x^-*c_x^+*c_k^-*c_k^+).                 (3.5)
```

Thus `lambda` is positive rational on every physical packet. It is not charged as an independent free parameter; it is the exact image of the same residual/root/2-primary packet.

---

## 4. Exact singularity classification

Homogenize (3.4) in `P^1 x P^1`:

```text
(U_1^2-U_0^2)(V_1^2-V_0^2)
 - lambda*U_1*U_0*V_1*V_0 = 0.                (4.1)
```

An elementary Jacobian calculation gives the exact singular parameter set

```text
boxed:
lambda in {0,4,-4}.                              (4.2)
```

For all other values the projective `(2,2)` curve is smooth, hence has genus

```text
(2-1)(2-1)=1.
```

Since every physical packet has `lambda>0`, the only possible physical singular coefficient is

```text
boxed:
lambda=4.                                        (4.3)
```

No generic nonsingularity assumption remains hidden.

---

## 5. The unique physical singular component

At `lambda=4`, (3.4) factors exactly:

```text
(u*v-u-v-1)(u*v+u+v-1)=0.                     (5.1)
```

For `u>1,v>1`, the second factor is strictly positive. Therefore every physical singular point lies on

```text
boxed:
u*v-u-v-1=0,                                    (5.2)
```

or

```text
boxed:
v=(u+1)/(u-1).                                  (5.3)
```

Using (3.2), this is exactly

```text
boxed:
D*(Q-P)=A*(Q+P),                                  (5.4)
```

or equivalently

```text
Q*(D-A)=P*(D+A).                                  (5.5)
```

This is not the proportional branch eliminated in `4cl/X4`; it is a distinct Cayley-type cross-role relation.

Define

```text
TopThetaCayleySingularCrossRoleIncidence.          (5.6)
```

The rational parametrization alone is not promoted to a saving.

---

## 6. Smooth branch and physical height box

For `lambda !=4`, every physical ratio point lies on the smooth genus-one curve

```text
E_lambda:
(u^2-1)(v^2-1)=lambda*u*v.                         (6.1)
```

The raw ratio coordinates are primitive and determine the four allocation moduli exactly. The diagonal rescaling `(x,y)->(u,v)` is fixed once one of the divisor-many quotient decorations is chosen.

On the top-theta edge

```text
theta=5/16,
3/16<=phi<=1/4,
```

the signed linear factors give the uniform windows

```text
L_x^-,L_x^+ <= B^(5/16+o(1)),
L_k^-,L_k^+ <= B^(phi+1/8+o(1)) <= B^(3/8+o(1)).     (6.2)
```

Merged `4cm/s7-26` also gives at least one xi modulus `>=B^(phi-o(1))` and one k modulus `>=B^(5/16-o(1))`.

No rational-point theorem is inserted here.

---

## 7. Exact remaining decomposition

Up to the already explicit `B^o(1)` quotient and labelled product-split refinements,

```text
TopThetaReciprocalBiquadraticModulusRatioIncidence
 -> TopThetaCayleySingularCrossRoleIncidence
  + TopThetaSmoothReciprocalEdwardsGenusOneIncidence.      (7.1)
```

For the smooth part, ratio-to-four-modulus multiplicity is exactly one, and the original reciprocal equation is only a physical filter. Therefore an upper bound for physical rational points on the smooth curves transfers with no extra scale loss.

For the singular part, (5.4)-(5.5) gives an explicit bilinear/Cayley relation for the next exact arithmetic attack.

Neither branch is bounded at the required whole-family scale in this stage.

---

## 8. H-line decision

The exact determinant/divisor attack requested by `4cm` has now exposed a genuine smooth genus-one rational-point obligation. A generic binary-quartic or Gaussian large-sieve theorem is still the wrong target, but a mainline H audit is now justified for the smooth branch.

The exact H object should be

```text
PhysicalReciprocalEdwardsGenusOneAverageIncidence
```

for the physical coefficient family

```text
lambda = 16*r*s*X*Y*epsilon_x*epsilon_k
         /(c_x^-c_x^+c_k^-c_k^+),
lambda>0,
lambda!=4,
```

with primitive raw modulus coordinates, top-edge anisotropic height windows, and the original reciprocal equation retained as a filter.

The audit should test determinant-method / genus-one rational-point estimates on this physical coefficient family and determine whether a uniform or coefficient-averaged fixed-power saving sufficient to beat `7/8` is available. It must not replace the packet by an unrestricted ambient quartic count.

The mainline does not need to wait: `4co` can attack the explicit singular relation (5.4) and further physical coefficient divisibility in parallel.

```text
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_H_TARGET_VALID=false
MAINLINE_H_REQUESTED_OBJECT=PhysicalReciprocalEdwardsGenusOneAverageIncidence
```

`tH17/tH18` are fixed-U coefficient spaces and are not cross-promoted.

---

## Stage boundary

```text
STAGE14_4CN=COMPLETE_PRIMITIVE_RATIO_INJECTIVITY_AND_RECIPROCAL_EDWARDS_SINGULAR_SMOOTH_SPLIT
MERGED_4CM_IMPORTED=true
MERGED_S7_27_IMPORTED=true
FIXED_RESIDUAL_FULL_SIGNED_QUOTIENT_QUADRUPLE_MULTIPLICITY=Bo1
XI_RATIO_ALLOCATION_PAIR_PRIMITIVE=true
K_RATIO_ALLOCATION_PAIR_PRIMITIVE=true
RATIO_TO_FOUR_ODD_MODULI_FIBER=1
ORIGINAL_SCALE_EQUATION_IS_FILTER_NOT_MULTIPLICITY=true
RECIPROCAL_EDWARDS_NORMAL_FORM_PROVED=true
RECIPROCAL_EDWARDS_LAMBDA_POSITIVE=true
RECIPROCAL_EDWARDS_SINGULAR_VALUES={0,4,-4}
ONLY_PHYSICAL_SINGULAR_VALUE=4
LAMBDA4_FACTORIZATION_PROVED=true
PHYSICAL_LAMBDA4_COMPONENT=u*v-u-v-1=0
CAYLEY_SINGULAR_CROSS_ROLE_RELATION=D*(Q-P)=A*(Q+P)
SMOOTH_BRANCH_GENUS=1
TOP_THETA_CAYLEY_SINGULAR_CROSS_ROLE_INCIDENCE_PROVED=false
TOP_THETA_SMOOTH_RECIPROCAL_EDWARDS_GENUS_ONE_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=false
MAINLINE_H_REQUESTED_OBJECT=PhysicalReciprocalEdwardsGenusOneAverageIncidence
NEXT=Stage14-4co attack the lambda=4 Cayley singular cross-role relation and physical coefficient divisibility while the smooth genus-one H audit may run independently
```
