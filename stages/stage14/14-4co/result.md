# Stage14-4co — singular Cayley gcd-square and residual squareclass lock

## Status

`COMPLETE_SINGULAR_CAYLEY_GCD_SQUARE_AND_RESIDUAL_SQUARECLASS_LOCK`

Stage14-4co consumes merged `14-4cn`, merged `14-s7-28`, and merged `14-X5`.  The smooth `lambda != 4` branch is not modified here.  This stage attacks only the physical singular component

```text
lambda=4,
D*(Q-P)=A*(Q+P).
```

No whole-family saving is promoted.  The unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported exact data

Use the full signed allocation of merged `s7-27/4cn`:

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

Put

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

The two reciprocal equations are

```text
(a*u)^2-(b*v)^2
 =4*r*s*epsilon_k*m*n,                     (1.1)

(c*n)^2-(d*m)^2
 =4*X*Y*epsilon_x*u*v.                     (1.2)
```

The quotient products satisfy

```text
oddpart(a*b)=oddpart(u_res),
oddpart(c*d)=oddpart(v_res).                (1.3)
```

---

## 2. Singular component as a primitive Mobius lift

Merged 4cn/X5 gives

```text
D*(Q-P)=A*(Q+P).                            (2.1)
```

Substitute the signed factors.  Equation (2.1) is equivalent to

```text
(a*u+b*v)*d*m
 =(a*u-b*v)*c*n.                            (2.2)
```

Hence

```text
n/m
 = d*(a*u+b*v) / (c*(a*u-b*v)).            (2.3)
```

Define

```text
G_k := gcd(
  d*(a*u+b*v),
  c*(a*u-b*v)
).                                           (2.4)
```

Since `gcd(m,n)=1`, primitive reduction is exact:

```text
n = d*(a*u+b*v)/G_k,
m = c*(a*u-b*v)/G_k.                        (2.5)
```

Thus there is no hidden common scale in the Mobius lift.

Dually, from

```text
Q*(D-A)=P*(D+A)
```
we obtain

```text
u/v
 = b*(c*n+d*m) / (a*(c*n-d*m)).            (2.6)
```

With

```text
G_x := gcd(
  b*(c*n+d*m),
  a*(c*n-d*m)
),                                           (2.7)
```

we have exactly

```text
u = b*(c*n+d*m)/G_x,
v = a*(c*n-d*m)/G_x.                        (2.8)
```

---

## 3. The original reciprocal equations become fixed gcd-square identities

Insert (2.5) into (1.1).  Since

```text
m*n
 = c*d*((a*u)^2-(b*v)^2)/G_k^2,
```

and the difference of squares is positive, cancellation gives

```text
boxed:
G_k^2 = 4*r*s*epsilon_k*c*d.               (3.1)
```

Likewise, insert (2.8) into (1.2):

```text
boxed:
G_x^2 = 4*X*Y*epsilon_x*a*b.               (3.2)
```

These are exact necessary identities for every physical singular packet.  They are stronger than the scale-free `lambda=4` condition: they retain both original reciprocal equations and primitive reduction.

In particular

```text
4*r*s*epsilon_k*c*d is a square,
4*X*Y*epsilon_x*a*b is a square.           (3.3)
```

---

## 4. Exact odd residual squareclass locks

The factors `epsilon_x,epsilon_k` are powers of two, and (1.3) gives the odd parts of the quotient products.  Taking odd squarefree kernels in (3.1)-(3.2) yields

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

Thus the singular branch is not allowed on a generic residual pair.  Its two residual squareclasses are completely prescribed by the endpoint-small product `r*s` and the primitive-root product `X*Y`.

---

## 5. Fixed-root residual support is halved

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

For a fixed squareclass `s`, the number of positive integers `n<=N` with `sf(oddpart(n))=s` is `N^(1/2+o(1))` uniformly for polynomially bounded `s`.  Therefore after fixing the root direction and endpoint-small data, (4.1)-(4.2) imply

```text
#u_res <= B^((5/8-2*phi)/2+o(1)),
#v_res <= B^((2*phi-3/8)/2+o(1)).           (5.2)
```

The sum of the two exponents is exactly

```text
boxed: 1/8.                                  (5.3)
```

The unconstrained `u_res,v_res` box has exponent `1/4`.  Hence the singular squareclass condition removes an exact `1/8` of raw residual-pair support **at fixed root/small data**.

This is not promoted to a whole-family `1/8` saving because the charged-once `s7-25` switch-product quantifier order is different and the singular primitive modulus pair remains moving.

```text
FIXED_ROOT_SINGULAR_RESIDUAL_PAIR_SUPPORT_EXPONENT=1/8
FIXED_ROOT_RAW_RESIDUAL_PAIR_SUPPORT_EXPONENT=1/4
FIXED_ROOT_SINGULAR_RESIDUAL_SUPPORT_SAVING=1/8
WHOLE_FAMILY_SAVING_FROM_THIS_LEDGER_ALONE=false
```

---

## 6. Exact algebra does not make the singular branch divisor-many

A quantifier guard is essential.  The singular component is rational, and when the coefficient compatibility (3.1)-(3.2) holds it can carry an infinite primitive family.

For example take the synthetic coefficient packet

```text
a=b=c=1,
d=4,
r=s=X=Y=epsilon_x=epsilon_k=1.
```

Then `lambda=4`, `G_k=4`, `G_x=2`.  For every odd positive `t`, set

```text
u=4*t+1,
v=1,
m=t,
n=4*t+2.                                  (6.1)
```

Whenever `gcd(t,4*t+2)=1` (in particular for odd `t`), both modulus pairs are primitive and

```text
u^2-v^2 = 4*m*n,
n^2-(4*m)^2 = 4*u*v,                       (6.2)
```

while

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

Thus

```text
SINGULAR_RELAXED_PRIMITIVE_LINEAR_FAMILY_EXISTS=true.
```

This synthetic family is not asserted to satisfy all perfect-cuboid physical masks.  Its role is to prove that singular rational geometry plus the two reciprocal equations does **not** imply a divisor-many fiber by itself.

---

## 7. New minimal singular receiver

After the exact squareclass locks, the singular branch reduces to

```text
TopThetaSquareclassLockedSingularCayleyPrimitivePairIncidence.
```

It counts primitive positive pairs `(u,v)` in the top-edge anisotropic ranges such that

- the Mobius lift (2.5) is integral and primitive;
- both gcds equal the fixed square roots from (3.1)-(3.2);
- the reconstructed agreement cells are squarefree, pairwise coprime and lie in their dyadic ranges;
- the common-core plus-host reconstruction gives legal switch products;
- all original orientation and physical masks hold.

The unresolved issue is therefore a primewise/congruence distribution problem on a rational singular component, not a genus-one rational-point problem.

---

## 8. H-line decision

The mainline H request created by 4cn remains correct **only for the smooth branch**:

```text
PhysicalReciprocalEdwardsGenusOneAverageIncidence.
```

Stage14-4co does not send the singular branch to that H line.  The singular branch is rational and has the explicit primitive family of Section 6, so a generic genus-one theorem is the wrong object.

For the singular branch, first use the exact squareclass locks, fixed gcd-square values, squarefree-cell masks, and primewise congruence structure in `Stage14-4cp`.

```text
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=false
SMOOTH_BRANCH_H_NEEDED=true
SINGULAR_BRANCH_H_NEEDED=false
MAINLINE_H_REQUESTED_OBJECT=PhysicalReciprocalEdwardsGenusOneAverageIncidence
```

---

## Stage boundary

```text
STAGE14_4CO=COMPLETE_SINGULAR_CAYLEY_GCD_SQUARE_AND_RESIDUAL_SQUARECLASS_LOCK
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
TOP_THETA_SQUARECLASS_LOCKED_SINGULAR_CAYLEY_PRIMITIVE_PAIR_INCIDENCE_PROVED=false
TOP_THETA_SMOOTH_RECIPROCAL_EDWARDS_GENUS_ONE_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=false
SMOOTH_BRANCH_H_NEEDED=true
SINGULAR_BRANCH_H_NEEDED=false
MAINLINE_H_REQUESTED_OBJECT=PhysicalReciprocalEdwardsGenusOneAverageIncidence
NEXT=Stage14-4cp attack the squareclass-locked singular primitive pair by primewise gcd/congruence splitting and the original squarefree cell masks; keep the smooth genus-one H line independent
```
