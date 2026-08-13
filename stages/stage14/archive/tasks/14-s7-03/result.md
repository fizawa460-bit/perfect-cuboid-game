# Stage14-s7-03 — first nonboundary multiplicative-height receiver

## Purpose

Merged Stage14-s7-02 proves that every physical nonboundary point in the direction family has infinite order.  Thus physical activation is now unconditionally contained in the positive-rank specialization set.  The remaining obstruction is not torsion or generic sections; it is the height of the first admissible nonboundary point.

This stage replaces the coarse statement

```text
physical hit below B => canonical height O(log B)
```

by an arithmetic height which is directly expressed in the primitive half-angle coordinates of the actual partner face and is uniformly comparable, up to an absolute constant, with the exact reconstructed physical space diagonal.

The resulting height is a product of two reduced rational-coordinate denominators on the Jacobi/Legendre models.  Therefore the first physical hit problem becomes, at power scale, a first rational point problem for a multiplicative denominator height rather than an abstract canonical-height window.

No counting exponent is improved in this stage.

---

## 1. Merged inputs

We use only merged results.

### 1.1 s7-02 positive-rank gate

For a physical rational direction `r=a/b`, `0<a<b`, the normalized Jacobi quartic is

```text
C_r: v^2=(1-u^2)(1-r^4*u^2).
```

Merged s7-02 proves that all rational torsion points are the eight boundary points and every physical nonboundary point has infinite order.  Hence

```text
physical activation => positive rank.
```

The converse is not available.

### 1.2 4bn exact physical-pair bijection

Let

```text
F2=(S2,X2,H2),
F3=(S3,X3,H3)
```

be primitive oriented Pythagorean faces.  Merged 4bn proves that a positive cross-square pair, together with the sharp cutoff

```text
d_rec = gcd(H,X2)*H3 <= B,
```

is exactly equivalent to a physical ordered edge below `B`.

In primitive half-angle coordinates write

```text
S2 = kappa2*(b^2-a^2)/2,
X2 = kappa2*a*b,
H2 = kappa2*(a^2+b^2)/2,

S3 = kappa3*(d^2-c^2)/2,
X3 = kappa3*c*d,
H3 = kappa3*(c^2+d^2)/2,
```

with

```text
0<a<b,
0<c<d,
gcd(a,b)=gcd(c,d)=1,
kappa2,kappa3 in {1,2}.
```

The transferred square condition is

```text
Delta0
=(a*d-b*c)(a*d+b*c)(b*d-a*c)(b*d+a*c)
=square>0.
```

For the physical orientation this implies

```text
a*d>b*c,
b*d>a*c.
```

---

## 2. Two natural rational coordinates

Merged s7-00 used

```text
r=a/b,
x=c/d,
u=(b/a)*x.
```

Therefore the physical Jacobi coordinate is exactly

```text
boxed:
u = b*c/(a*d).                                      (2.1)
```

Since `a*d>b*c`, one has

```text
0<u<1.
```

For the Legendre quotient, s7-00 gives

```text
U=u^2,
X=r^4*U.
```

Substituting (2.1),

```text
boxed:
X=(a*c/(b*d))^2.                                  (2.2)
```

Put

```text
w := sqrt(X)=a*c/(b*d).
```

Since `b*d>a*c`,

```text
0<w<1.
```

Thus a physical point supplies two rational coordinates in `(0,1)`:

```text
u=b*c/(a*d),
w=a*c/(b*d).
```

---

## 3. Exact reduced denominators

Define

```text
q_u := gcd(b*c,a*d),
q_x := gcd(a*c,b*d).
```

Then the reduced denominators of `u` and `w` are exactly

```text
boxed:
D_u = a*d/q_u,                                      (3.1)

D_x = b*d/q_x.                                      (3.2)
```

Because `gcd(a,b)=gcd(c,d)=1`, every prime dividing both `a*b` and `c*d` belongs to exactly one of the four cross-pair gcd cells.  The two diagonal products above partition those cells, hence

```text
boxed:
q_u*q_x = gcd(a*b,c*d).                             (3.3)
```

In particular `gcd(q_u,q_x)=1`.

Define the multiplicative coordinate height

```text
boxed:
H_mult(F2,F3) := D_u*D_x.                           (3.4)
```

Using (3.1)--(3.3),

```text
boxed:
H_mult
= a*b*d^2 / gcd(a*b,c*d).                           (3.5)
```

This is an integer.

On logarithmic scale,

```text
h_mult := log H_mult
        = log D_u + log D_x.
```

So the relevant first-point height is genuinely multiplicative in the two natural rational coordinate denominators.

---

## 4. Exact sharp diagonal in half-angle data

We now eliminate the reconstructed first face from the sharp cutoff.

For a positive cross-square pair put

```text
A=S3*X2,
C=X3*S2,
h0=gcd(A,C).
```

The reconstructed first face has

```text
H=A/h0.
```

Because each primitive face satisfies `gcd(Si,Xi)=1`, prime-by-prime support separation gives

```text
h0 = gcd(S3,S2)*gcd(X2,X3).
```

These two factors are coprime.  Therefore

```text
H
=(S3/gcd(S3,S2))
 *(X2/gcd(X2,X3)).
```

Since `gcd(S3,X3)=1`, the first factor is coprime to `gcd(X2,X3)`.  Hence

```text
boxed:
gcd(H,X2)=X2/gcd(X2,X3).                           (4.1)
```

The exact reconstructed physical diagonal from 4bn becomes

```text
boxed:
d_rec
= [X2/gcd(X2,X3)]*H3.                              (4.2)
```

Substituting half-angle formulas,

```text
d_rec
= [kappa2*a*b / gcd(kappa2*a*b,kappa3*c*d)]
  * [kappa3*(c^2+d^2)/2].                           (4.3)
```

This formula depends only on the two primitive half-angle pairs and their two orientation constants.

---

## 5. Uniform comparison with the multiplicative height

Let

```text
G := gcd(a*b,c*d)=q_u*q_x.
```

Since `kappa2,kappa3` are each `1` or `2`, one has

```text
G
<= gcd(kappa2*a*b,kappa3*c*d)
<= 2*G.                                              (5.1)
```

Also

```text
d^2/2
<= H3
<= 2*d^2.                                           (5.2)
```

Combining (4.3), (5.1), (5.2), and (3.5) gives the uniform absolute comparison

```text
boxed:
(1/2)*H_mult <= d_rec <= 4*H_mult.                  (5.3)
```

Equivalently,

```text
|log d_rec - log H_mult| <= log 4                   (5.4)
```

up to the harmless asymmetric lower constant already displayed in (5.3).

The crucial point is that the error is **absolute**.  It does not grow like `log a`, `log b`, or `log B`.

This is stronger for family counting than the earlier canonical-height comparison, whose family-dependent coefficient term is logarithmic in the direction height.

---

## 6. First physical height versus first multiplicative point height

For a fixed primitive direction `F2`, define

```text
mu_phys(F2)
:= min d_rec(F2,F3)
```

over all primitive positive cross-square partners `F3`.  If no such partner exists, put `mu_phys(F2)=infinity`.

By merged 4bn,

```text
F2 is physically active below B
<=> mu_phys(F2)<=B.                                  (6.1)
```

Define the first multiplicative point height

```text
eta(F2)
:= min H_mult(F2,F3)                                (6.2)
```

over the same partner set, and `eta=infinity` if the set is empty.

Taking minima in (5.3),

```text
boxed:
(1/2)*eta(F2)
<= mu_phys(F2)
<= 4*eta(F2).                                       (6.3)
```

Hence if

```text
A_eta(Y)
:= #{primitive directions F2 : eta(F2)<=Y},
```

then

```text
boxed:
A_eta(B/4)
<= A_phys(B)
<= A_eta(2*B).                                      (6.4)
```

Thus `A_eta` and the exact physical active-direction count have the same power exponent.

The Stage14 first-hit problem is therefore power-scale equivalent to counting directions whose Jacobi specialization contains an admissible nonboundary infinite-order point with

```text
D_u*D_x <= B
```

up to an absolute constant.

---

## 7. Positive-rank formulation

Merged s7-02 gives

```text
eta(F2)<infinity
=> rank C_r(Q)>0.                                   (7.1)
```

The reverse implication is false in the present state of the proof: a positive-rank specialization may have no rational point satisfying simultaneously

- the physical interval `0<u,w<1`;
- the square-`U` lift;
- primitive partner half-angle conditions;
- positive cross-square reconstruction;
- small multiplicative height.

Therefore the correct family receiver is

```text
positive-rank specialization
+ admissible nonboundary lift
+ first multiplicative height <= B,
```

not positive rank alone.

---

## 8. Hyperbola split for the next stage

For a physical hit below `B`, (5.3) gives

```text
H_mult=D_u*D_x <= 2*B.                              (8.1)
```

Consequently

```text
boxed:
min(D_u,D_x) <= sqrt(2*B).                          (8.2)
```

More generally, for any threshold `L>=1`, every physical point lies in one of the two sectors

```text
D_u <= L,
```

or

```text
D_x <= 2*B/L.                                       (8.3)
```

This is the first exact family-level denominator receiver produced by s7.  The next stage can choose `L` anisotropically and attack the two projections separately rather than counting all positive-rank fibers indiscriminately.

The two sectors correspond to two different cross-gcd diagonals:

```text
D_u = a*d / gcd(b*c,a*d),
D_x = b*d / gcd(a*c,b*d).
```

Thus the first-small-point event is tied directly to shared arithmetic between the moving direction and its first admissible partner.

---

## 9. What is and is not proved

Proved here:

1. the exact physical Jacobi coordinate `u=b*c/(a*d)`;
2. the exact Legendre square-root coordinate `w=a*c/(b*d)`;
3. exact reduced denominators `D_u,D_x`;
4. exact cross-gcd product `q_u q_x=gcd(ab,cd)`;
5. exact sharp diagonal formula
   `d_rec=[X2/gcd(X2,X3)]H3`;
6. absolute comparison
   `(1/2)H_mult<=d_rec<=4H_mult`;
7. first-height sandwich (6.3)--(6.4);
8. every physical active direction is positive rank by merged s7-02;
9. the hyperbola split (8.3).

Not proved:

- a positive power saving for the number of directions with `eta<=B`;
- a density theorem for positive-rank specializations;
- a uniform lower bound for `eta` on positive-rank fibers;
- square-root upper bound or asymptotic.

The next task is no longer to refine canonical-height constants.  It is to count the two small-denominator projection sectors in (8.3), while retaining the fourth-power Legendre/Jacobi relation and the physical lift conditions.

---

## Boundary

```text
STAGE14_S7_03=COMPLETE_PHYSICAL_FIRST_POINT_MULTIPLICATIVE_HEIGHT_RECEIVER
MERGED_S7_02_POSITIVE_RANK_GATE_IMPORTED=true
MERGED_4BN_EXACT_PHYSICAL_BIJECTION_IMPORTED=true
JACOBI_PHYSICAL_U=bc/(ad)
LEGENDRE_SQRT_X=ac/(bd)
REDUCED_DENOMINATOR_DU=ad/gcd(ad,bc)
REDUCED_DENOMINATOR_DX=bd/gcd(ac,bd)
CROSS_GCD_PRODUCT_IDENTITY=gcd(ab,cd)=q_u*q_x
SHARP_DIAGONAL_FORMULA=d_rec=(X2/gcd(X2,X3))*H3
MULTIPLICATIVE_FIRST_POINT_HEIGHT=DU*DX
MULTIPLICATIVE_TO_PHYSICAL_COMPARISON=(1/2)*H_mult<=d_rec<=4*H_mult
FIRST_PHYSICAL_AND_MULTIPLICATIVE_HEIGHT_POWER_EXPONENTS_EQUAL=true
ACTIVE_DIRECTION_MULTIPLICATIVE_HEIGHT_SANDWICH=true
PHYSICAL_HIT_IMPLIES_DU_TIMES_DX_LE_2B=true
PHYSICAL_HIT_IMPLIES_ONE_DENOMINATOR_LE_SQRT_2B=true
PHYSICAL_ACTIVATION_IMPLIES_POSITIVE_RANK_UNCONDITIONALLY=true
POSITIVE_RANK_IMPLIES_SMALL_MULTIPLICATIVE_POINT=false
FAMILY_SMALL_FIRST_POINT_COUNT_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-04
```
