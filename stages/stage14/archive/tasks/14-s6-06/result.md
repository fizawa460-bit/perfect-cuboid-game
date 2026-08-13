# Stage14-s6-06 — physical conjugate gap and half-angle denominator reduction

## Purpose

Stage14-s6-05 replaces maximal halving by the exact compact 2-torsion translate

```text
Q = P_phys + (0,0)
```

on

```text
E_{S,X}: W^2 = Z(Z-S^2)(Z+X^2).
```

The translated point is compact, non-torsion, nonzero modulo `2E(Q)`, and still remembers the physical partner exactly.  Its reduced denominator was denoted `D_T`.

Stage14-s6-06 now eliminates the abstract s3 variables `q,z,X0` completely.  It expresses both the original physical point and the compact translate directly in the two primitive oriented face triples and the physical space diagonal.

The main outcome is an exact conjugate factorization.  If

```text
F  = (S,X,H),
F2 = (S2,X2,H2),
g  = gcd(S,S2),
G  = g*d,
R  = H2-S2,
```

then every physical edge satisfies

```text
G^2 = S^2 H2^2 + X^2 S2^2,
```

and

```text
Z_P = (H G + S^2 H2 + X^2 S2)/R,
Z_T = -(H G - S^2 H2 - X^2 S2)/R.
```

Writing

```text
U = G-H*S2,
V = H*H2-G,
```

one obtains the stronger product form

```text
Z_T = -U*V/X2^2.
```

Consequently the physical compact denominator is not merely polynomially bounded:

```text
D_T^2 | H2-S2,
D_T | X2.
```

For the Euclid parameters `m2>n2` of the primitive partner face this sharpens to

```text
D_T | (m2-n2)   if S2=2m2n2,
D_T | n2        if S2=m2^2-n2^2.
```

Thus the s6-04/s6-05 denominator gate becomes a half-angle divisor/root-sign problem in the actual physical partner variables.  No physical reconstruction is discarded.

This stage does not yet prove a new full-family exponent.  It also explains why denominator size alone cannot beat the current `41/42`: the elementary count of primitive partner faces with the relevant half-angle parameter `t<=B^(10/21)` is already of order `B^(41/42+o(1))`.  The next saving must therefore use the newly exposed square-cancellation/root-sign condition, not only `D_T<=t`.

No external theorem is used.

---

## 1. Exact physical gluing scales

A raw physical pair is represented by two primitive oriented Pythagorean faces

```text
S^2+X^2=H^2,
S2^2+X2^2=H2^2.
```

They arise from two actual cuboid faces sharing one physical edge.  Put

```text
g=gcd(S,S2).
```

Because the ambient cuboid is primitive, the two face scaling factors are

```text
r1=S2/g,
r2=S/g.
```

Hence the actual three cuboid edges attached to this ordered pair are

```text
shared edge = S*S2/g,
first other = X*S2/g,
second other = X2*S/g.
```

The actual first and second face diagonals are respectively

```text
H*S2/g,
H2*S/g.
```

Let `d` be the integer space diagonal.  Multiplying the space-diagonal identity by `g^2` gives

```text
(gd)^2
 = S^2*S2^2 + X^2*S2^2 + S^2*X2^2
 = H^2*S2^2 + S^2*X2^2
 = X^2*S2^2 + S^2*H2^2.
```

Thus, with `G=gd`,

```text
boxed:
G^2 = S^2 H2^2 + X^2 S2^2.
```

Equivalently

```text
(S*H2)^2 + (X*S2)^2 = G^2.
```

So every physical pair carries a third integral Pythagorean triple

```text
(S H2, X S2, G).
```

We record

```text
PHYSICAL_GLUE_THIRD_PYTHAGOREAN_IDENTITY=true.
```

---

## 2. Eliminate the s3 half-angle variables

Stage14-s3 uses

```text
q = X2/(H2+S2),
z = g*d/(H*H2),
Yq = z*(1+q^2),
X0 = (Yq+1)/q^2,
A0 = 1-2*(X/H)^2,
x = (A0+X0)/(2*(S/H)^2),
Z_P=S^2*x.
```

For the primitive Pythagorean partner,

```text
q^2=(H2-S2)/(H2+S2),
1+q^2=2H2/(H2+S2).
```

Therefore

```text
X0
 = [H(H2+S2)+2gd]/[H(H2-S2)].
```

Also

```text
A0=(S^2-X^2)/H^2.
```

Substitution and `H^2=S^2+X^2` give the exact closed form

```text
boxed:
Z_P
 = [H*G + S^2*H2 + X^2*S2]/(H2-S2).
```

Define

```text
Nplus = H*G + S^2*H2 + X^2*S2,
Nminus= H*G - S^2*H2 - X^2*S2,
R=H2-S2.
```

Then

```text
Z_P=Nplus/R.
```

Hence

```text
S3_Z_PHYSICAL_CLOSED_FORM=true.
```

---

## 3. Conjugate numerator product

Use the gluing identity from Section 1:

```text
G^2=S^2H2^2+X^2S2^2.
```

Then

```text
Nplus*Nminus
 = H^2 G^2 - (S^2 H2+X^2 S2)^2
 = S^2 X^2 (H2-S2)^2.
```

Thus

```text
boxed:
Nplus*Nminus=S^2*X^2*R^2.
```

The compact `T0=(0,0)` translation from s6-05 is

```text
Z_T=-S^2 X^2/Z_P.
```

Rationalizing with the conjugate product gives

```text
boxed:
Z_T=-Nminus/R.
```

The apparently reciprocal torsion transform is therefore just the conjugate of the physical numerator in the direct second-face variables.

```text
CONJUGATE_NUMERATOR_PRODUCT_IDENTITY=true
T0_COMPACT_CONJUGATE_FORM_EXACT=true.
```

---

## 4. Physical gap variables

Put

```text
U=G-H*S2,
V=H*H2-G.
```

Every physical point from s6-05 has `Z_P>S^2`; equivalently the gluing geometry gives

```text
G>H*S2,
G<H*H2,
```

so

```text
U>0,
V>0.
```

The gluing identity gives two exact difference-of-squares factorizations:

```text
U*(G+H*S2)=S^2*X2^2,
V*(H*H2+G)=X^2*X2^2.
```

A direct expansion also gives

```text
U*V=(H2+S2)*Nminus.
```

Since

```text
X2^2=(H2-S2)(H2+S2)=R*(H2+S2),
```

we obtain

```text
boxed:
Z_T=-U*V/X2^2.
```

Similarly

```text
Nplus=(G+H*S2)*(H*H2+G)/(H2+S2),
```

so even the original physical point can be written as

```text
Z_P=(G+H*S2)*(H*H2+G)/X2^2.
```

Thus both the physical point and its compact torsion translate have square denominator controlled by the actual primitive partner leg `X2`.

```text
PHYSICAL_GAP_FACTORIZATION_EXACT=true
T0_COMPACT_COORDINATE_GAP_PRODUCT=true.
```

---

## 5. Exact denominator formulas

Reduce

```text
Z_T=-Nminus/R.
```

Let

```text
c=gcd(Nminus,R).
```

Then the reduced denominator is

```text
R/c.
```

By the monic integral Weierstrass denominator theorem already proved in s6-01, a reduced rational `Z` coordinate has square denominator.  Therefore

```text
boxed:
D_T^2 = R/gcd(Nminus,R).
```

In particular

```text
D_T^2 | H2-S2.
```

Using the equivalent gap product gives the second exact formula

```text
boxed:
D_T^2
 = X2^2 / gcd(X2^2,U*V).
```

Hence also

```text
D_T | X2.
```

These are equivalent formulas for the same s6-05 compact selector.

```text
TORSION_DENOMINATOR_SQUARE_DIVIDES_H2_MINUS_S2=true
TORSION_DENOMINATOR_DIVIDES_PARTNER_LEG=true.
```

The first divisibility is stronger for uniform size control; the second is better for prime-by-prime root-sign analysis.

---

## 6. Euclid half-angle divisor

Write the primitive partner triple in its unique Euclid form

```text
m2>n2>0,
gcd(m2,n2)=1,
m2,n2 opposite parity.
```

There are two orientations.

### 6.1 `S2` is the even leg

If

```text
S2=2m2n2,
X2=m2^2-n2^2,
H2=m2^2+n2^2,
```

then

```text
R=H2-S2=(m2-n2)^2.
```

Since `D_T^2|R`, necessarily

```text
boxed: D_T | m2-n2.
```

### 6.2 `S2` is the odd leg

If

```text
S2=m2^2-n2^2,
X2=2m2n2,
H2=m2^2+n2^2,
```

then

```text
R=H2-S2=2n2^2.
```

A square divisor of `2n2^2` has 2-adic exponent at most that of `n2^2`, so again

```text
boxed: D_T | n2.
```

Define the partner half-angle denominator parameter

```text
t = m2-n2   in the even-S2 orientation,
t = n2      in the odd-S2 orientation,
```

and

```text
kappa=1     in the even-S2 orientation,
kappa=2     in the odd-S2 orientation.
```

Then uniformly

```text
R=kappa*t^2,
D_T|t.
```

Set

```text
k=t/D_T.
```

The exact cancellation in Section 5 becomes

```text
boxed:
gcd(Nminus,R)=kappa*k^2.
```

Thus

```text
D_T=t/k
```

and the denominator problem is exactly a square-cancellation cofactor problem in the partner half-angle parameter.

```text
PARTNER_HALF_ANGLE_DIVISOR_D_T=true
HALF_ANGLE_CANCELLATION_COFACTOR_EXACT=true.
```

---

## 7. The compact cover equations become physical gap square identities

Write the compact packet as in s6-05:

```text
d0=-e0,
d1=-e1,
d2=e2,
```

with positive squarefree `e0,e1,e2`, and

```text
A_T=-e0*u0^2,
A_T-S^2D_T^2=-e1*u1^2,
A_T+X^2D_T^2=e2*u2^2.
```

Because

```text
A_T=-Nminus/(kappa*k^2),
D_T^2=R/(kappa*k^2),
```

we obtain three exact physical factorizations:

```text
boxed:
Nminus = kappa*k^2*e0*u0^2,

H*(G-H*S2) = kappa*k^2*e1*u1^2,

H*(H*H2-G) = kappa*k^2*e2*u2^2.
```

Indeed

```text
Nminus+S^2R = H*(G-H*S2)=H*U,
X^2R-Nminus = H*(H*H2-G)=H*V.
```

So the half-angle cancellation cofactor `k^2` is a common square divisor of all three physical gap quantities after the fixed orientation factor `kappa` is removed.

The squarefree kernels retain the s6-01 support:

```text
e0 supported on 2*S*X,
e1 supported on 2*S*H,
e2 supported on 2*X*H.
```

This is now an exact statement in physical partner variables, not an ambient coordinate-density condition.

```text
COMPACT_GAP_SQUARE_KERNEL_FACTORIZATION=true.
```

---

## 8. Good odd partner-leg prime root-sign law

Let

```text
ell^e || X2
```

for an odd prime `ell` with

```text
ell not dividing H*S*X.
```

Because the partner triple is primitive, `ell` divides exactly one of

```text
H2-S2,
H2+S2
```

and its exponent there is exactly `2e`.

The gluing identity gives

```text
G^2 == H^2*S2^2 (mod ell^(2e)).
```

All displayed factors are units modulo `ell`, so

```text
G == +H*S2
or
G == -H*S2
(mod ell^(2e)).
```

For the `T0=(0,0)` compact selector, the gap-product formula gives the exact rule.

### Plus half-angle factor

If

```text
ell^(2e) | H2+S2,
```

then one of `U=G-HS2` and `V=HH2-G` absorbs the full `ell^(2e)` for either root sign.  Hence

```text
v_ell(D_T)=0.
```

### Minus half-angle factor

If

```text
ell^(2e) | H2-S2,
```

then

```text
v_ell(D_T)=e
```

exactly when

```text
G == -H*S2 (mod ell^(2e)).
```

For the positive root sign `G==+HS2`, the full prime power cancels and `v_ell(D_T)=0`.

Thus the odd good-prime support of `D_T` is confined to the `H2-S2` half-angle factor and is selected by one explicit root sign.

```text
GOOD_ODD_T0_ROOT_SIGN_LAW=true.
```

This is the first formulation of the physical denominator gate as a moving root-sign/cancellation statistic rather than a generic rational-height statistic.

---

## 9. Size ledger and the exact remaining barrier

Because `H2<=d<=B` for a primitive partner face,

```text
R=H2-S2 <= B.
```

Therefore

```text
boxed: D_T <= B^(1/2).
```

The critical denominator scale inherited from 4bj is

```text
B^(10/21).
```

The entire unknown range is therefore only

```text
10/21 <= log_B D_T <= 1/2,
```

a width of

```text
1/2-10/21 = 1/42.
```

This is a substantial sharpening of the earlier polynomial height box.

However, size alone does not improve the current exponent.  Let `t` be the half-angle parameter from Section 6.  The elementary number of primitive partner triples with

```text
t<=T,
H2<=B
```

is

```text
O(T*sqrt(B))
```

(up to logarithmic/subpolynomial coprimality bookkeeping): for each `t`, the complementary Euclid parameter has `O(sqrt(B))` possible values.

At

```text
T=B^(10/21),
```

this gives exactly

```text
B^(10/21+1/2)=B^(41/42).
```

So the half-angle divisor `D_T|t` by itself reproduces, but does not beat, the current `41/42` exponent.

The next improvement must use at least one of:

1. the exact square-cancellation cofactor `k=t/D_T`;
2. the good-prime root-sign law of Section 8;
3. the common physical gap-square identities of Section 7;
4. a complementary compact 2-torsion selector, if/when an independently proved parallel result is merged.

We therefore record

```text
HALF_ANGLE_SIZE_ONLY_BARRIER_EXPONENT=41/42
HALF_ANGLE_SIZE_ONLY_BEATS_CURRENT_BOUND=false.
```

No positive `delta_post` is claimed here.

---

## 10. Why the quantifier problem is now different

In s6-02 through s6-04, the main obstruction was that a sparse set of coordinates inside an abstract packet could still contain one witness for every packet.

The present variables are different.  `F2,d,G,U,V,D_T,t,k` are reconstructed directly from an actual physical partner of the first face, and the map back to the physical point is exact.  We have not enlarged to all globally soluble representatives.

Therefore a future count of tuples satisfying the Section 1/7/8 physical identities is already a count of physical incidences.  It does not require multiplying an unweighted local packet count by a fixed-packet coordinate density.

This does **not** mean a saving has already been proved; it means the receiver for a valid physical-incidence saving is now correctly quantified.

```text
PHYSICAL_RECONSTRUCTION_RETAINED=true
ABSTRACT_EXISTENCE_COORDINATE_MULTIPLICATION_NOT_REQUIRED_FOR_NEXT_RECEIVER=true.
```

---

## 11. Parallel-track compatibility

At the time this stage was prepared, the 14-4 main track had an open `4bk` draft exploring a different compact rational 2-torsion translate.  s6-06 does not depend on that open result.

The present stage uses the already-merged s6-05 selector `T0=(0,0)` and proves the stronger half-angle divisibility

```text
D_T^2 | H2-S2.
```

If a complementary compact selector is later merged, its prime-support/root-sign law can be combined with Section 8 without changing any theorem above.

---

## 12. Status and next stage

Stage14-s6-06 proves:

1. the exact third Pythagorean gluing identity;
2. a closed physical formula for the s3 point;
3. the conjugate numerator factorization;
4. positive physical gap variables `U,V` and their divisor identities;
5. exact compact denominator formulas in `R` and `X2^2`;
6. `D_T` divides one Euclid half-angle parameter of the primitive partner;
7. the exact square-cancellation cofactor `k=t/D_T`;
8. three physical gap square-kernel identities carrying the same `k^2`;
9. the good odd-prime root-sign law selecting the denominator support;
10. the sharp size-only barrier `41/42`.

The global upper bound remains

```text
V(B) << B^(41/42+epsilon).
```

and the square-root gap remains `10/21` at the post-local level.

```text
STAGE14_S6_06=COMPLETE_PHYSICAL_CONJUGATE_GAP_AND_HALF_ANGLE_DENOMINATOR_REDUCTION
PHYSICAL_GLUE_THIRD_PYTHAGOREAN_IDENTITY=true
S3_Z_PHYSICAL_CLOSED_FORM=true
CONJUGATE_NUMERATOR_PRODUCT_IDENTITY=true
PHYSICAL_GAP_FACTORIZATION_EXACT=true
T0_COMPACT_COORDINATE_GAP_PRODUCT=true
TORSION_DENOMINATOR_SQUARE_DIVIDES_H2_MINUS_S2=true
TORSION_DENOMINATOR_DIVIDES_PARTNER_LEG=true
PARTNER_HALF_ANGLE_DIVISOR_D_T=true
HALF_ANGLE_CANCELLATION_COFACTOR_EXACT=true
COMPACT_GAP_SQUARE_KERNEL_FACTORIZATION=true
GOOD_ODD_T0_ROOT_SIGN_LAW=true
PHYSICAL_RECONSTRUCTION_RETAINED=true
ABSTRACT_EXISTENCE_COORDINATE_MULTIPLICATION_NOT_REQUIRED_FOR_NEXT_RECEIVER=true
HALF_ANGLE_SIZE_ONLY_BARRIER_EXPONENT=41/42
HALF_ANGLE_SIZE_ONLY_BEATS_CURRENT_BOUND=false
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
NEXT=Stage14-s6-07 count the moving physical gap/root-sign cancellation cofactor k=t/D_T, combining a complementary compact torsion selector only if it is merged and independently validated
```
