# Stage14-4co — singular Cayley squareclass lock and H-audit integration

## Status

`COMPLETE_SINGULAR_CAYLEY_GCD_SQUARE_RESIDUAL_SQUARECLASS_LOCK_AND_H_AUDIT_INTEGRATION`

Stage14-4co consumes merged `14-4cn`, `14-s7-28`, and `14-X5`, and records the completed independent H audit for the smooth reciprocal Edwards proposal.

The unconditional whole-family bound remains

```text
V(B) << B^(7/8+o(1)).
```

No new whole-family power saving is claimed.

---

## 1. Imported singular packet

Retain the full signed allocation

```text
D-A = c_x^- L_x^-,
D+A = c_x^+ L_x^+,
Q-P = c_k^- L_k^-,
Q+P = c_k^+ L_k^+,
```

with

```text
gcd(L_x^-,L_x^+)=1,
gcd(L_k^-,L_k^+)=1.
```

Write

```text
a=c_x^+,
b=c_x^-,
c=c_k^+,
d=c_k^-,

u=L_x^+,
v=L_x^-,
n=L_k^+,
m=L_k^-.
```

Then

```text
D=(a*u+b*v)/2,
A=(a*u-b*v)/2,
Q=(c*n+d*m)/2,
P=(c*n-d*m)/2.
```

The original reciprocal equations are

```text
(a*u)^2-(b*v)^2
 = 4*r*s*epsilon_k*m*n,                    (1.1)

(c*n)^2-(d*m)^2
 = 4*X*Y*epsilon_x*u*v.                    (1.2)
```

Merged `s7-27/4cm` also gives

```text
oddpart(a*b)=oddpart(u_res),
oddpart(c*d)=oddpart(v_res).                (1.3)
```

Merged `4cn/X5` classifies the only physical singular value as `lambda=4`, with exact component

```text
D*(Q-P)=A*(Q+P).                            (1.4)
```

---

## 2. Singular Mobius lift is primitive

Equation (1.4) gives

```text
(a*u+b*v)*d*m
 = (a*u-b*v)*c*n,
```

hence

```text
n/m
 = d*(a*u+b*v) / (c*(a*u-b*v)).            (2.1)
```

Define

```text
G_k = gcd(
  d*(a*u+b*v),
  c*(a*u-b*v)
).
```

Because `gcd(m,n)=1`, the primitive reduction is exact:

```text
n = d*(a*u+b*v)/G_k,
m = c*(a*u-b*v)/G_k.                       (2.2)
```

The equivalent relation

```text
Q*(D-A)=P*(D+A)
```

gives dually

```text
u/v
 = b*(c*n+d*m) / (a*(c*n-d*m)).            (2.3)
```

With

```text
G_x = gcd(
  b*(c*n+d*m),
  a*(c*n-d*m)
),
```

we obtain

```text
u = b*(c*n+d*m)/G_x,
v = a*(c*n-d*m)/G_x.                       (2.4)
```

There is therefore no extra absolute scale in either singular Mobius lift.

---

## 3. Original reciprocal equations force two gcd-square identities

From (2.2),

```text
m*n
 = c*d*((a*u)^2-(b*v)^2)/G_k^2.
```

Substitution into (1.1), followed by cancellation of the positive difference of squares, gives

```text
boxed:
G_k^2 = 4*r*s*epsilon_k*c*d.               (3.1)
```

Similarly, (2.4) in (1.2) gives

```text
boxed:
G_x^2 = 4*X*Y*epsilon_x*a*b.               (3.2)
```

Thus every physical singular packet must satisfy both square conditions

```text
4*r*s*epsilon_k*c*d is a square,
4*X*Y*epsilon_x*a*b is a square.           (3.3)
```

These conditions use the original reciprocal equations and are strictly stronger than the scale-free statement `lambda=4` alone.

---

## 4. Residual squareclasses are exactly locked

The factors `epsilon_x,epsilon_k` are powers of two.  Taking odd squarefree kernels in (3.1)-(3.2), and using (1.3), yields

```text
boxed:
sf(oddpart(v_res)) = sf(oddpart(r*s)),      (4.1)

boxed:
sf(oddpart(u_res)) = sf(oddpart(X*Y)).      (4.2)
```

Equivalently,

```text
oddpart(r*s*v_res) is a square,
oddpart(X*Y*u_res) is a square.             (4.3)
```

So the singular branch occupies prescribed residual squareclasses; a generic residual pair cannot lie on it.

---

## 5. Fixed-root residual-pair support drops from exponent 1/4 to 1/8

On the merged top-theta edge

```text
theta=5/16,
3/16 <= phi <= 1/4,
```

4cg gives

```text
u_res <= B^(5/8-2*phi+o(1)),
v_res <= B^(2*phi-3/8+o(1)).               (5.1)
```

For a fixed odd squareclass, integers up to `N` in that squareclass have support `N^(1/2+o(1))`.  Hence after fixing the primitive root and endpoint-small data, (4.1)-(4.2) give

```text
#u_res <= B^((5/8-2*phi)/2+o(1)),
#v_res <= B^((2*phi-3/8)/2+o(1)).           (5.2)
```

The exponent sum is exactly

```text
boxed: 1/8.                                  (5.3)
```

whereas the raw residual-pair box has exponent `1/4`.

Therefore

```text
FIXED_ROOT_SINGULAR_RESIDUAL_PAIR_SUPPORT_EXPONENT=1/8
FIXED_ROOT_RAW_RESIDUAL_PAIR_SUPPORT_EXPONENT=1/4
FIXED_ROOT_SINGULAR_RESIDUAL_SUPPORT_SAVING=1/8
```

This is not promoted to a whole-family saving: the charged-once switch-product quantifier order differs, and the primitive modulus pair remains moving.

---

## 6. The rational singular component can still carry a linear primitive family

The exact algebra above does not imply a divisor-many singular fiber.

Take the synthetic coefficient packet

```text
a=b=c=1,
d=4,
r=s=X=Y=epsilon_x=epsilon_k=1.
```

For every positive odd `t`, set

```text
u=4*t+1,
v=1,
m=t,
n=4*t+2.                                  (6.1)
```

Then

```text
gcd(u,v)=gcd(m,n)=1,
```

and exactly

```text
u^2-v^2 = 4*m*n,
n^2-(4*m)^2 = 4*u*v.                       (6.2)
```

Moreover

```text
D=2*t+1,
A=2*t,
Q=4*t+1,
P=1
```

satisfy

```text
D*(Q-P)=A*(Q+P).                            (6.3)
```

The corresponding primitive gcds are `G_k=4`, `G_x=2`, exactly as (3.1)-(3.2) require.

This family is only a relaxed algebraic counterexample; it is not asserted to satisfy all perfect-cuboid masks.  It proves that rational singular geometry plus the reciprocal equations alone does not yield `B^o(1)` multiplicity.

```text
SINGULAR_RELAXED_PRIMITIVE_LINEAR_FAMILY_EXISTS=true
SINGULAR_CAYLEY_FIBER_BO1_PROVED=false
```

---

## 7. Completed H audit of the smooth genus-one proposal

The independent audit requested by 4cn is now complete:

```text
PHYSICAL_RECIPROCAL_EDWARDS_GENUS_ONE_H_AUDIT=COMPLETE
FIXED_LAMBDA_DETERMINANT_METHOD_APPLICABLE=true
SEGRE_PROJECTIVE_DEGREE=4
FIXED_LAMBDA_UNIFORM_POINT_BOUND=B^(7/32+phi/2+o(1))
OPTIMISTIC_FIXED_LAMBDA_SAVING_RANGE=phi<17/80
FULL_TOP_EDGE_DETERMINANT_SAVING_PROVED=false
POSITIVE_GENUS_UNIFORM_IMPROVEMENT_EXISTS=true
REQUIRED_WORST_EDGE_DELTA_GT=3/22
REQUIRED_DELTA_CERTIFIED_BY_AVAILABLE_THEOREM=false
RANK_SENSITIVE_ELLIPTIC_BOUND_DIRECTLY_APPLICABLE=false
PHYSICAL_LAMBDA_FAMILY_AVERAGE_COST_CONTROLLED=false
ORIGINAL_RECIPROCAL_FILTER_EXPLOITED_BY_GENERIC_DETERMINANT_METHOD=false
GENERIC_GENUS_ONE_RECEIVER_IS_MINIMAL=false
```

Interpretation:

- fixed `lambda` permits a degree-4 Segre/determinant-method treatment;
- the resulting bound is potentially useful only on the subrange `phi<17/80`;
- it does not certify a saving uniformly across the full top edge;
- no available theorem in the audited package certifies the required worst-edge `delta>3/22`;
- averaging over the physical moving `lambda` family is itself uncontrolled;
- generic determinant methods do not exploit the original reciprocal divisibility filter.

Therefore no saving from the H audit is entered into the exponent ledger.

---

## 8. Receiver correction after the H audit

The H audit shows that the smooth genus-one formulation is not the minimal arithmetic receiver.  Merged `s7-28` already reconstructs the packet from one primitive agreement pair and identifies the sharper object

```text
TopThetaPrimitiveAgreementQuadraticValueDivisibilityIncidence.
```

Stage14-4co adds that its singular specialization carries the squareclass/gcd-square locks (3.1)-(4.2).

Thus the next mainline step should not continue a generic genus-one point-counting program.  It should work on the primitive quadratic-value/divisibility receiver and use, as applicable,

- primewise splitting of the quadratic difference value;
- the two exact singular squareclass locks;
- squarefree and pairwise-coprime cell masks;
- CRT/root-line information;
- the original common-core switch-product reconstruction.

The completed H audit is informative but not a blocker and does not request another generic genus-one H task.

```text
PREFERRED_MINIMAL_RECEIVER=TopThetaPrimitiveAgreementQuadraticValueDivisibilityIncidence
MAINLINE_H_AUDIT_COMPLETE=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_CONTINUATION_RECOMMENDED=false
```

---

## Stage boundary

```text
STAGE14_4CO=COMPLETE_SINGULAR_CAYLEY_GCD_SQUARE_RESIDUAL_SQUARECLASS_LOCK_AND_H_AUDIT_INTEGRATION
MERGED_4CN_IMPORTED=true
MERGED_S7_28_IMPORTED=true
MERGED_X5_IMPORTED=true
SINGULAR_MOBIUS_PRIMITIVE_LIFT_PROVED=true
SINGULAR_K_GCD_SQUARE_IDENTITY=G_k^2=4*r*s*epsilon_k*c_k^+*c_k^-
SINGULAR_X_GCD_SQUARE_IDENTITY=G_x^2=4*X*Y*epsilon_x*c_x^+*c_x^-
SINGULAR_ODD_VRES_SQUARECLASS_EQUALS_ODD_RS=true
SINGULAR_ODD_URES_SQUARECLASS_EQUALS_ODD_XY=true
FIXED_ROOT_SINGULAR_RESIDUAL_PAIR_SUPPORT_EXPONENT=1/8
FIXED_ROOT_RAW_RESIDUAL_PAIR_SUPPORT_EXPONENT=1/4
FIXED_ROOT_SINGULAR_RESIDUAL_SUPPORT_SAVING=1/8
WHOLE_FAMILY_SAVING_FROM_THIS_LEDGER_ALONE=false
SINGULAR_RELAXED_PRIMITIVE_LINEAR_FAMILY_EXISTS=true
SINGULAR_CAYLEY_FIBER_BO1_PROVED=false
PHYSICAL_RECIPROCAL_EDWARDS_GENUS_ONE_H_AUDIT=COMPLETE
FIXED_LAMBDA_DETERMINANT_METHOD_APPLICABLE=true
SEGRE_PROJECTIVE_DEGREE=4
FIXED_LAMBDA_UNIFORM_POINT_BOUND=B^(7/32+phi/2+o(1))
OPTIMISTIC_FIXED_LAMBDA_SAVING_RANGE=phi<17/80
FULL_TOP_EDGE_DETERMINANT_SAVING_PROVED=false
REQUIRED_WORST_EDGE_DELTA_GT=3/22
REQUIRED_DELTA_CERTIFIED_BY_AVAILABLE_THEOREM=false
PHYSICAL_LAMBDA_FAMILY_AVERAGE_COST_CONTROLLED=false
ORIGINAL_RECIPROCAL_FILTER_EXPLOITED_BY_GENERIC_DETERMINANT_METHOD=false
GENERIC_GENUS_ONE_RECEIVER_IS_MINIMAL=false
PREFERRED_MINIMAL_RECEIVER=TopThetaPrimitiveAgreementQuadraticValueDivisibilityIncidence
TOP_THETA_PRIMITIVE_AGREEMENT_QUADRATIC_VALUE_DIVISIBILITY_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
MAINLINE_H_AUDIT_COMPLETE=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_CONTINUATION_RECOMMENDED=false
NEXT=Stage14-4cp attack TopThetaPrimitiveAgreementQuadraticValueDivisibilityIncidence primewise, importing the singular squareclass locks where lambda=4
```
