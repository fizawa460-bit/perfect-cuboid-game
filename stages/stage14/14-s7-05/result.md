# Stage14-s7-05 — joint squareclass collision to isotrivial `j=1728` twist pairs

## Purpose

Stage14-s7-04 shows that the first-point multiplicative height

```text
H_mult = D_u D_x
```

cannot be exploited by counting the two rational projections separately: fixed-coordinate fibers are genus one, but there are quadratically many rational coordinates of denominator at most `L`, so the separate hyperbola split stops at exponent `1`.

The exact joint receiver retained by s7-04 is

```text
u=P/Q,
w=R/S,
0<w<u<1,
gcd(P,Q)=gcd(R,S)=1,
QS=H_mult<=O(B),
PR/(QS) is a rational square,
ker(Q^2-P^2)=ker(S^2-R^2).
```

This stage compresses the two square conditions into a single two-label twist family.  The result is a new exact formulation of the first-small-point problem:

> a physical pair gives two distinct rational points on the same isotrivial genus-one quartic
>
> ```text
> C_{k,xi}: k y^2 = 1-xi^2 z^4,
> ```
>
> and the Jacobian is the `j=1728` curve
>
> ```text
> E_{k,xi}: Y^2=X^3+4(k xi)^2 X.
> ```

The Jacobian depends only on the product `n=k xi`, while the torsor class retains the ordered pair `(k,xi)`.

This is a substantial structural compression, but fixed-twist bounded-height counting alone still gives only the trivial global scale `B^(1+o(1))`.  To beat the merged Stage14-4br whole-family bound `B^(20/21+o(1))`, one needs a genuine **off-diagonal two-point twist incidence saving**.

No new whole-family exponent is claimed in s7-05.

---

## 1. Merged inputs and current baseline

### 1.1 s7-04 joint reduced-coordinate receiver

Merged s7-04 gives the exact joint conditions above and proves that the separate `D_u` / `D_x` projection method is noncompetitive.

The physical half-angle pair may be reconstructed from

```text
r^2 = w/u,
x^2 = uw,
```

where `r=a/b` is the direction parameter and `x=c/d` is the partner slope.

### 1.2 s7-03 multiplicative height

Merged s7-03 proves

```text
H_mult=Q*S
```

for the reduced joint coordinates and

```text
(1/2)H_mult <= d_rec <= 4H_mult.
```

Thus the denominator-product cutoff is power-equivalent to the physical space-diagonal cutoff.

### 1.3 current merged whole-family theorem

Merged Stage14-4br improves the whole physical family to

```text
V(B) << B^(20/21+o(1)).
```

Hence a new s7 family argument must beat exponent `20/21`, not the older `41/42` or `61/63` baselines.

Relative to the naive joint-coordinate scale `B^1`, the required direct saving is

```text
1-20/21 = 1/21.
```

---

## 2. A canonical squareclass label for a rational coordinate

Let

```text
u=P/Q,
0<P<Q,
gcd(P,Q)=1.
```

Define the positive squarefree integer

```text
xi := ker(PQ).
```

Since

```text
PQ = xi*h^2
```

for a unique positive integer `h`, put

```text
z := h/Q.
```

Then exactly

```text
boxed:
u = xi*z^2.                                           (2.1)
```

Equivalently, `xi` is the rational squareclass of `u`.

Now define

```text
k := ker(Q^2-P^2).
```

Writing

```text
Q^2-P^2 = k*A^2
```

and

```text
y := A/Q,
```

one obtains

```text
boxed:
1-u^2 = k*y^2.                                       (2.2)
```

Substituting (2.1),

```text
boxed:
k*y^2 = 1-xi^2*z^4.                                 (2.3)
```

Thus every reduced coordinate `u in (0,1)` determines a canonical pair of positive squarefree labels

```text
(k,xi)
```

and a rational point on the quartic (2.3).

---

## 3. The two s7-04 square conditions are exactly equality of the two labels

Let

```text
u=P/Q,
w=R/S
```

be reduced positive rational coordinates.

### 3.1 Product-square condition

The s7-04 product-square condition is

```text
PR/(QS) is a rational square.
```

Since multiplication by `Q^2 S^2` is a square,

```text
PR/(QS) square
<=> PQRS square
<=> ker(PQ)=ker(RS).
```

Therefore

```text
boxed:
product-square <=> xi_u=xi_w.                       (3.1)
```

### 3.2 Difference-squarefree-kernel condition

By definition,

```text
k_u=ker(Q^2-P^2),
k_w=ker(S^2-R^2).
```

Hence the second s7-04 condition is simply

```text
boxed:
same difference kernel <=> k_u=k_w.                 (3.2)
```

Combining (3.1) and (3.2):

> The entire joint arithmetic receiver is equality of one ordered squarefree label pair `(k,xi)`.

---

## 4. Exact same-twist two-point formulation

Suppose the s7-04 joint conditions hold and let the common labels be `(k,xi)`.

Write

```text
u=xi*z1^2,
w=xi*z2^2.
```

Then both pairs satisfy

```text
boxed:
C_{k,xi}: k*y^2 = 1-xi^2*z^4.                       (4.1)
```

Thus the physical pair supplies two rational points

```text
(z1,y1), (z2,y2) in C_{k,xi}(Q).
```

Because physical orientation has

```text
0<w<u<1,
```

one has

```text
0<z2<z1
```

for the positive square roots chosen above.  In particular the two coordinate points are distinct; the exact diagonal `u=w` is not physical.

### 4.1 Converse reconstruction

Conversely, suppose two rational points on the same `C_{k,xi}` satisfy

```text
0<xi*z2^2<xi*z1^2<1.
```

Set

```text
u=xi*z1^2,
w=xi*z2^2.
```

Then automatically

```text
w/u = (z2/z1)^2,
uw  = (xi*z1*z2)^2.
```

Therefore define

```text
boxed:
r=z2/z1,                                             (4.2)

boxed:
x=xi*z1*z2.                                          (4.3)
```

These are rational and satisfy

```text
0<r<1,
0<x<1.
```

Moreover

```text
(1-u^2)(1-w^2)
 = k^2*y1^2*y2^2
```

is a rational square.  Hence the Jacobi cross-square condition is recovered exactly.

After primitive reduction and the s7-03 sharp denominator-product cutoff, this is precisely the joint first-point receiver.

Thus s7-05 has an exact equivalence at the rational-coordinate level:

```text
joint product-square + same-kernel receiver
<=>
ordered distinct rational-point pair on one C_{k,xi}.
```

---

## 5. Binary-quartic invariants and the `j=1728` Jacobian

Multiply (4.1) by `k` and put

```text
Y=k*y.
```

Then

```text
Y^2 = k-k*xi^2*z^4.
```

The associated binary quartic is

```text
F(Z,T) = -k*xi^2*Z^4 + k*T^4.
```

For a binary quartic

```text
F=a4 Z^4+a3 Z^3T+a2 Z^2T^2+a1 ZT^3+a0 T^4,
```

the standard invariants are

```text
I=12*a4*a0-3*a3*a1+a2^2,
J=72*a4*a2*a0+9*a3*a2*a1-27*a0*a3^2-27*a4*a1^2-2*a2^3.
```

Here

```text
a4=-k*xi^2,
a0=k,
a3=a2=a1=0,
```

so exactly

```text
I=-12*k^2*xi^2,
J=0.
```

The standard Jacobian model

```text
y^2=x^3-(I/3)x-(J/27)
```

therefore becomes

```text
boxed:
E_{k,xi}: y^2=x^3+4*k^2*xi^2*x.                     (5.1)
```

Put

```text
n:=k*xi.
```

Then

```text
boxed:
E_n: y^2=x^3+4*n^2*x.                                (5.2)
```

Consequences:

1. every curve in the new receiver has `J=0` binary-quartic invariant and elliptic `j=1728`;
2. over an algebraic closure the genus-one family is isotrivial;
3. the Jacobian depends only on the **one scalar product** `n=k xi`;
4. the torsor/cover class still remembers the ordered factorization `(k,xi)`.

This is substantially more rigid than an arbitrary moving genus-one family.

We do **not** infer here that two distinct physical points force a non-torsion difference on `E_n`.  That torsion-difference possibility is a separate exact gate and must be audited before replacing the two-point torsor problem by a positive-rank quadratic-twist problem.

---

## 6. Dyadic two-point twist energy

For `U>=1`, define

```text
M_{k,xi}(U)
```

to be the number of reduced coordinates

```text
u=P/Q,
0<u<1,
Q~U,
```

with canonical twist label `(k,xi)`.

The one-block state count satisfies trivially

```text
sum_{k,xi} M_{k,xi}(U) << U^2.
```

The joint s7-04 block with

```text
Q~U,
S~V,
UV<=O(B)
```

is majorized by the mixed twist collision energy

```text
boxed:
E_tw(U,V)
 := sum_{k,xi} M_{k,xi}(U) M_{k,xi}(V).              (6.1)
```

The physical receiver uses only the ordered off-diagonal part satisfying `w<u`; exact equal-coordinate pairs are excluded.

### 6.1 What fixed-twist genus-one counting gives

For a fixed `(k,xi)`, the usual bounded-height genus-one mechanism gives only subpolynomial multiplicity in a polynomial height box.

Using this separately on the two sides and Cauchy gives at best

```text
E_tw(U,V) << U*V*B^o(1).                             (6.2)
```

On the critical denominator hyperbola `UV~B`, this is

```text
B^(1+o(1)).
```

Therefore:

```text
fixed-twist genus-one sparsity alone
DOES NOT beat the merged B^(20/21+o(1)) theorem.
```

This is the same quantifier phenomenon encountered earlier in s6/t41: subpolynomial fixed-fiber multiplicity is not a global family power saving.

---

## 7. Exact saving threshold after the 4br improvement

The current merged whole-family exponent is

```text
20/21.
```

The natural joint-twist baseline on `UV~B` is exponent `1`.

Hence a direct mixed-energy theorem of the form

```text
E_tw^off(U,V) << (UV)^(1-delta+o(1))
```

would improve the current whole-family theorem only when

```text
delta > 1/21.                                        (7.1)
```

If one instead proves symmetric squared-energy bounds

```text
sum_{k,xi} M_{k,xi}(U)^2 << U^(2-eta+o(1)),
sum_{k,xi} M_{k,xi}(V)^2 << V^(2-eta+o(1)),
```

then one Cauchy step gives

```text
E_tw(U,V) << (UV)^(1-eta/2+o(1)).
```

Thus the corresponding squared-energy threshold is

```text
boxed:
eta > 2/21.                                          (7.2)
```

These replace the obsolete s7-00 `1/63` target, because the main route has already moved to `20/21`.

---

## 8. Relation to the merged t41 Kummer-energy barrier

Merged t41 proves a general warning:

> near-linear row and column energies do not imply a global same-squareclass energy bound; off-fiber collisions form a Kummer-type surface and a perfect-matching configuration can saturate the local information.

The s7-05 receiver exhibits the same logical danger.  A fixed `(k,xi)` curve is genus one, but summing two-point incidences over moving twist labels is a global collision problem.

However s7-05 is **more rigid** than the generic t41 collision:

- both points lie on the **same** quartic twist;
- the quartics are isotrivial with `j=1728`;
- the Jacobian is the one-parameter family `E_n: y^2=x^3+4n^2x`;
- the physical contribution is off-diagonal in the reduced coordinate.

Therefore the correct next task is not another generic square sieve.  It is to classify and count off-diagonal rational-point collisions in this special CM/isotrivial twist family, beginning with torsion correspondences and exceptional low-degree self-correspondences.

---

## 9. What is and is not proved

### Proved / frozen

- exact canonical labels `xi=ker(PQ)`, `k=ker(Q^2-P^2)`;
- product-square is exactly equality of `xi` labels;
- same-difference-kernel is exactly equality of `k` labels;
- exact same-twist two-point receiver `C_{k,xi}`;
- exact inverse formulas `r=z2/z1`, `x=xi z1 z2`;
- physical receiver is off-diagonal in the twist coordinate;
- exact binary-quartic invariants `I=-12k^2xi^2`, `J=0`;
- exact Jacobian `y^2=x^3+4(kxi)^2x` and `j=1728`;
- Jacobian depends only on `n=kxi`;
- fixed-twist genus-one counting alone yields only `B^(1+o(1))` globally;
- direct off-diagonal twist-energy saving required to beat current main: `>1/21`;
- symmetric squared-energy saving required before one Cauchy: `>2/21`.

### Not proved

- that the difference of the two physical points on `C_{k,xi}` is always non-torsion on `E_n`;
- a positive-density or density-zero theorem for active `(k,xi)` twists;
- a power-saving bound for `E_tw^off(U,V)`;
- a whole-family exponent below `20/21`;
- the `B^(1/2+o(1))` target.

---

## 10. Next stage

`Stage14-s7-06` should analyze the off-diagonal same-twist receiver itself:

1. classify the rational torsion of `E_n: y^2=x^3+4n^2x` relevant to differences of two points on `C_{k,xi}`;
2. identify the induced torsion/self-correspondences on the quartic and test whether any can occur with `0<w<u<1`;
3. if the torsion branch is excluded, promote a physical twist collision to a positive-rank event in the one-parameter `j=1728` twist family;
4. isolate exceptional/isogenous correspondences before any global second-moment or determinant argument;
5. target an off-diagonal saving `delta>1/21` (or squared-energy saving `eta>2/21`).

---

## Boundary

```text
STAGE14_S7_05=COMPLETE_JOINT_SQUARECLASS_TO_J1728_TWIST_PAIR_RECEIVER
MERGED_S7_04_IMPORTED=true
MERGED_4BR_CURRENT_WHOLE_FAMILY_EXPONENT=20/21
JOINT_LABEL_XI=ker(PQ)
JOINT_LABEL_K=ker(Q^2-P^2)
PRODUCT_SQUARE_IFF_XI_LABELS_EQUAL=true
SAME_DIFFERENCE_KERNEL_IFF_K_LABELS_EQUAL=true
JOINT_RECEIVER_IS_SAME_TWIST_TWO_POINT_INCIDENCE=true
TWIST_QUARTIC=k*y^2=1-xi^2*z^4
PHYSICAL_TWIST_PAIR_OFF_DIAGONAL=true
TWIST_BINARY_QUARTIC_J_INVARIANT=0
TWIST_JACOBIAN=y^2=x^3+4*(k*xi)^2*x
TWIST_JACOBIAN_J_INVARIANT=1728
TWIST_JACOBIAN_DEPENDS_ONLY_ON_N=k*xi
FIXED_TWIST_GENUS_ONE_ALONE_GLOBAL_BOUND=B^(1+o(1))
FIXED_TWIST_GENUS_ONE_ALONE_BEATS_20_21=false
DIRECT_OFF_DIAGONAL_TWIST_SAVING_REQUIRED_GT=1/21
SQUARED_TWIST_ENERGY_SAVING_REQUIRED_GT=2/21
PHYSICAL_TWIST_PAIR_IMPLIES_POSITIVE_RANK_ON_E_N=false
OFF_DIAGONAL_TWIST_ENERGY_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-06
```
