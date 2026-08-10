# Stage14-s7-08 — shared-xi cell switch and the first post-20/21 bound

## Purpose

Merged Stage14-s7-07 identifies the balanced fixed-quartic receiver

```text
F(P,Q)=P*Q*(Q-P)*(Q+P),
ker(F(P,Q))=ker(F(R,S)),
Q*S<<B.
```

Merged Stage14-4bv then makes a decisive advance: after the product-square descent

```text
P=a*x^2,
Q=b*y^2,
R=c*z^2,
S=d*h^2,
ab=cd=xi,
```

it proves an exact inert additive Fourier transform and a square-sieve packet bound

```text
N_packet << M*H^(-1/2)*B^o(1),
H=min(X,Y,Z,W).
```

Thus every **thick** square-part packet receives a genuine square-root relative saving.  4bv leaves only the thin branch, where a small square part forces a large squarefree coefficient but the common-label constraint `ab=cd=xi` couples the coefficients.

This stage resolves that coupling by a four-cell factorisation of the common squarefree label.  A large coefficient forces a large cell.  Varying that cell turns the residual same-kernel equation into a one-variable nondegenerate quartic character problem.  The physical inequalities `0<R/S<P/Q<1` exclude every square-polynomial degeneration.  A standard Weil bound plus the square sieve therefore gives the same square-root relative saving in the large cell.

Re-optimising the denominator, square-part, and numerator thresholds gives the first whole-family improvement below `20/21`:

```text
boxed:
V(B) << B^(18/19+o(1)).
```

The improvement is

```text
20/21 - 18/19 = 2/399.
```

No open PR is used as a theorem input.

---

## 1. Merged inputs

We use the following merged results.

### 1.1 s7-07 fixed-quartic receiver

Every physical ordered edge produces two reduced coordinates

```text
u=P/Q,
v=R/S,
0<v<u<1,
```

such that

```text
ker(F(P,Q))=ker(F(R,S)),
F(A,B)=A*B*(B-A)*(B+A),
Q*S<<B.
```

Fixed-coordinate partner multiplicity is `B^o(1)`.

### 1.2 s7-06 torsion exclusion

The common squarefree twist is `n>1`, and the two physical points on

```text
E_n : Y^2=X^3+4n^2X
```

have infinite-order difference.

### 1.3 merged 4bv thick-packet theorem

The product-square condition gives a common squarefree label `xi` and a decomposition

```text
P=a*x^2,
Q=b*y^2,
R=c*z^2,
S=d*h^2,

ab=cd=xi,
```

where `a,b,c,d` are squarefree and

```text
gcd(a,b)=gcd(c,d)=1.
```

Put

```text
G_ab(x,y)=b^2*y^4-a^2*x^4,
G_cd(z,h)=d^2*h^4-c^2*z^4.
```

The remaining same-kernel condition is

```text
G_ab(x,y)*G_cd(z,h)=square.
```

For a fixed coefficient packet and square-part box volume

```text
M=X*Y*Z*H4,
Hmin=min(X,Y,Z,H4),
```

merged 4bv proves

```text
boxed:
N_packet << M*Hmin^(-1/2)*B^o(1).                 (1.1)
```

Moreover the total product-square packet volume satisfies

```text
sum_packets M << U*V*B^o(1) << B^(1+o(1)).       (1.2)
```

This is the thick-side input.

---

## 2. Exact four-cell factorisation of the shared squarefree label

The obstruction in 4bv is that `a,b,c,d` are coupled by

```text
ab=cd=xi.
```

Because all four coefficients are squarefree and the two displayed pairs are coprime, define

```text
r = gcd(a,c),
s = gcd(a,d),
t = gcd(b,c),
j = gcd(b,d).                                      (2.1)
```

Prime-by-prime, every prime dividing `xi` chooses one of `a/b` and independently one of `c/d`.  Therefore the four cells are pairwise coprime and

```text
boxed:
a=r*s,
b=t*j,
c=r*t,
d=s*j,
xi=r*s*t*j.                                       (2.2)
```

Conversely every four-tuple of pairwise-coprime squarefree cells `(r,s,t,j)` gives a unique coefficient quadruple satisfying the common-label constraint.

So the shared-`xi` coupling is not an opaque divisor relation.  It is an exact `2 x 2` squarefree cell matrix.

---

## 3. Physical coordinates in cell variables

With square parts `x,y,z,h`, the two reduced coordinates are

```text
u = r*s*x^2 / (t*j*y^2),
v = r*t*z^2 / (s*j*h^2),                           (3.1)
```

with

```text
0<v<u<1.                                          (3.2)
```

The two quartic factors become

```text
G1=(t*j*y^2)^2-(r*s*x^2)^2,
G2=(s*j*h^2)^2-(r*t*z^2)^2.                       (3.3)
```

The residual condition is

```text
G1*G2=square.                                      (3.4)
```

Each cell appears quadratically in **both** factors.  This is exactly what allows the thin coefficient branch to be switched to a one-variable cell sieve.

---

## 4. One-cell quartics and the degeneracy test

Fix the other three cells and all four square parts, and vary one cell `q` in a dyadic interval `q~T`.

The product `G1*G2` is, up to a fixed nonzero square/sign, of the form

```text
H_q(Qvar)
 =(A^2-B^2*Qvar^2)(C^2-D^2*Qvar^2).              (4.1)
```

For a good odd prime, this quartic is a square polynomial only if the two quadratic factors have the same pair of roots, i.e.

```text
A*D = +/- B*C.                                    (4.2)
```

For the four cells, the rational degeneracy conditions have an exact physical interpretation.

### 4.1 Cells `r` and `j`

For `r`, condition (4.2) is

```text
t^2*y^2*z^2 = s^2*x^2*h^2.
```

Using (3.1), this is exactly

```text
v/u = 1.                                          (4.3)
```

The same condition occurs for the opposite cell `j`.

But physical points satisfy `v/u<1`.  Hence the `r` and `j` cell quartics are nondegenerate over `Q`.

### 4.2 Cells `s` and `t`

For `s`, condition (4.2) becomes

```text
j^2*y^2*h^2 = r^2*x^2*z^2,
```

which is exactly

```text
u*v = 1.                                          (4.4)
```

The same condition occurs for `t`.

But `0<v<u<1` implies `u*v<1`.  Hence the `s` and `t` cell quartics are also nondegenerate over `Q`.

Therefore:

```text
boxed:
PHYSICAL_CELL_QUARTIC_SQUARE_DEGENERATION=false.  (4.5)
```

Modulo a prime, degeneration can occur only at primes dividing the fixed nonzero discriminant integer produced by (4.3) or (4.4), together with primes dividing the fixed coefficients.  The number of such primes in a polynomial-size auxiliary interval is `B^o(1)` and they are deleted from the sieve set.

This is the key new point: the physical open condition removes the exact square-polynomial resonance that would otherwise destroy the coefficient switch.

---

## 5. One-cell character bound

For a good odd auxiliary prime `p`, the cell polynomial `H_q(T)` is a squarefree quartic.  We use the standard Weil bound for quadratic/mixed character sums of a non-square polynomial of bounded degree:

```text
sum_{t mod p} chi_p(H_q(t))*e_p(k*t) << p^(1/2)   (5.1)
```

uniformly in the additive frequency `k`.

For a squarefree product `m` of two good auxiliary primes, CRT gives

```text
complete additive Fourier transform << m^(1/2)*B^o(1).  (5.2)
```

Consequently, for an arbitrary interval `I` of length `T` and `m~T`, Fourier completion gives

```text
sum_{q in I} chi_m(H_q(q)) << T^(1/2)*B^o(1).     (5.3)
```

The original cell is required to be squarefree and coprime to the other cells.  For an upper bound these restrictions may simply be dropped; they only reduce the set being counted.

---

## 6. One-cell square sieve

Let the varying cell lie in a dyadic interval

```text
q~T,
T>=B^epsilon.
```

Choose good auxiliary primes of size

```text
L=T^(1/2).
```

The square sieve for

```text
H_q(q)=square
```

has diagonal term

```text
T/L = T^(1/2),
```

and, by (5.3), the averaged off-diagonal term is also

```text
T^(1/2)*B^o(1).
```

Hence

```text
boxed:
# {q~T : H_q(q)=square}
 << T^(1/2)*B^o(1).                               (6.1)
```

Relative to the ambient `T` choices for the cell, this is

```text
boxed:
CELL_SWITCH_RELATIVE_SAVING=T^(-1/2).             (6.2)
```

The estimate is uniform after fixing the other cells and square parts.  Dyadic enlargement removes any issue from the simultaneous physical interval constraints: we count the entire dyadic cell interval containing the physical solutions.

Because the cell parametrisation (2.2) is bijective, summing the ambient cell-volume over all fixed remaining variables reconstructs the same product-square universe as (1.2).  Therefore if every state in a sector is assigned canonically to a cell of size at least `B^sigma`, then

```text
boxed:
N_cell-sector << B^(1-sigma/2+o(1)).              (6.3)
```

---

## 7. General threshold ledger

We now re-optimise the full s7/4bv receiver instead of keeping the historical `10/21` and `2/21` thresholds fixed.

Choose three exponents:

```text
lambda : small-denominator threshold,
tau    : square-part thickness threshold,
theta  : small-numerator threshold.               (7.1)
```

We may assume

```text
0<2*tau<theta<=lambda<1/2.                         (7.2)
```

### 7.1 Small denominator

If

```text
min(Q,S)<=B^lambda,
```

then reduced-coordinate counting plus fixed-coordinate partner multiplicity gives

```text
N_den-small << B^(2lambda+o(1)).                   (7.3)
```

Thus the remaining balanced region has

```text
B^lambda <= Q,S <= B^(1-lambda+o(1)).             (7.4)
```

### 7.2 Thick square parts

If

```text
min(x,y,z,h)>=B^tau,
```

merged 4bv gives

```text
N_thick << B^(1-tau/2+o(1)).                      (7.5)
```

### 7.3 Small numerator

In the balanced region, if

```text
P<=B^theta
```

then the number of possible reduced first coordinates is at most

```text
B^(theta+1-lambda+o(1)),
```

and fixed-coordinate partner multiplicity is `B^o(1)`.  Hence

```text
N_num-small << B^(theta+1-lambda+o(1)).           (7.6)
```

The same applies to `R`.

### 7.4 Hard thin numerator square part

Assume now

```text
P,R>=B^theta
```

and one numerator square part is thin, say

```text
x<B^tau.
```

Since `P=a*x^2`,

```text
a >= B^(theta-2tau).                               (7.7)
```

But `a=r*s`, so at least one of `r,s` satisfies

```text
q >= B^((theta-2tau)/2).                           (7.8)
```

The cell switch (6.3) therefore gives

```text
N_num-thin
 << B^(1-(theta-2tau)/4+o(1)).                    (7.9)
```

The same holds for a thin `z`.

### 7.5 Hard thin denominator square part

If instead

```text
y<B^tau,
```

then from `Q=b*y^2` and `Q>=B^lambda`,

```text
b >= B^(lambda-2tau).
```

Since `b=t*j`, one cell is at least

```text
B^((lambda-2tau)/2),
```

and

```text
N_den-thin
 << B^(1-(lambda-2tau)/4+o(1)).                   (7.10)
```

Because `theta<=lambda`, the numerator-thin exponent (7.9) is the worse of the two thin-cell bounds.

---

## 8. Exact optimisation

The whole architecture is therefore bounded by

```text
E(lambda,tau,theta)
 = max(
     2lambda,
     1-tau/2,
     1+theta-lambda,
     1-(theta-2tau)/4
   ).                                               (8.1)
```

(The denominator-thin term is no larger because `theta<=lambda`.)

For fixed `lambda,tau`, balance the two `theta`-dependent terms:

```text
1+theta-lambda
 = 1-(theta-2tau)/4.
```

This gives

```text
theta = (4lambda+2tau)/5.                          (8.2)
```

The common value is

```text
1-lambda/5+2tau/5.                                 (8.3)
```

Balance (8.3) with the thick exponent `1-tau/2`:

```text
tau = 2lambda/9.                                   (8.4)
```

The common non-denominator value becomes

```text
1-lambda/9.                                        (8.5)
```

Finally balance with the small-denominator exponent:

```text
2lambda = 1-lambda/9.
```

Hence

```text
boxed:
lambda = 9/19,
tau    = 2/19,
theta  = 8/19.                                     (8.6)
```

Every active term equals

```text
boxed:
E=18/19.                                           (8.7)
```

The denominator-thin term is strictly smaller:

```text
1-(lambda-2tau)/4
 = 1-5/76
 = 71/76
 < 18/19.                                          (8.8)
```

### 8.1 Optimality inside this architecture

The value `18/19` is not merely a convenient choice.

Suppose every term in (8.1) were strictly below `18/19`.

From

```text
2lambda < 18/19
```

we get

```text
lambda < 9/19.                                     (8.9)
```

From

```text
1-tau/2 < 18/19
```

we get

```text
tau > 2/19.                                        (8.10)
```

From

```text
1+theta-lambda < 18/19
```

we get

```text
theta < lambda-1/19 < 8/19.                       (8.11)
```

But from

```text
1-(theta-2tau)/4 < 18/19
```

we get

```text
theta > 2tau+4/19 > 8/19,                         (8.12)
```

contradicting (8.11).

Therefore `18/19` is the exact optimum of the present four-sector adaptive architecture.

---

## 9. Whole-family recombination

Use the optimised thresholds

```text
lambda=9/19,
tau=2/19,
theta=8/19.
```

Every physical edge lies in one of the following exhaustive sectors.

### Sector A: small denominator

```text
min(Q,S)<=B^(9/19)
```

contributes

```text
B^(18/19+o(1)).
```

### Sector B: balanced denominator, thick square parts

```text
min(x,y,z,h)>=B^(2/19)
```

contributes by merged 4bv

```text
B^(18/19+o(1)).
```

### Sector C: balanced denominator, small numerator

```text
min(P,R)<=B^(8/19)
```

contributes

```text
B^(8/19+10/19+o(1))
 = B^(18/19+o(1)).
```

### Sector D: hard thin square part

We have

```text
Q,S>=B^(9/19),
P,R>=B^(8/19),
min(x,y,z,h)<B^(2/19).
```

If a numerator square part is thin, the corresponding coefficient is at least

```text
B^(4/19),
```

so one shared-`xi` cell is at least

```text
B^(2/19).
```

If a denominator square part is thin, one cell is even larger:

```text
B^(5/38).
```

Assign every thin state to a canonical largest eligible cell.  The one-cell square sieve gives at least the relative saving

```text
B^(-1/19).
```

against the total product-square universe `B^(1+o(1))`.  Hence

```text
N_thin << B^(18/19+o(1)).
```

Combining A--D gives

```text
boxed:
V(B) << B^(18/19+o(1)).                            (9.1)
```

This is the first proved whole-family exponent below the merged `20/21` barrier.

---

## 10. New exponent ledger

Previous whole-family exponent:

```text
20/21.
```

New exponent:

```text
18/19.
```

Strict improvement:

```text
20/21 - 18/19
 = 2/399.                                          (10.1)
```

Relative to the old pre-post-local `41/42` exponent, the cumulative saving is

```text
41/42 - 18/19
 = 23/798.                                         (10.2)
```

Remaining gap to square root:

```text
18/19 - 1/2
 = 17/38.                                          (10.3)
```

So this is a genuine quantitative step, but it is nowhere near the final square-root target.

---

## 11. What the inert-prime second-moment audit taught us

The original s7-08 plan was a marginal multi-modulus second moment on the fixed quartic.  That route remains insufficient by itself: separate-side `L^2`/Cauchy control stops at an exponent-one ceiling and does not force cross-scale support transversality.

Merged 4bv shows the correct way to use inert cancellation: **first descend to an exact product-square packet**, where additive Fourier completion sees the actual square condition.  The present stage then applies the same philosophy to the thin branch by switching to the shared-`xi` cell variable.

Thus the useful principle is now:

```text
marginal squareclass equidistribution        -> insufficient
packet-level Fourier / cell-level square sieve -> effective
```

---

## 12. Remaining obstruction and next stage

The adaptive architecture itself is now optimised and closes at `18/19`.

To move below `18/19`, one must improve at least one of the four active terms:

```text
small denominator      2lambda,
thick packet           1-tau/2,
small numerator        1+theta-lambda,
thin cell              1-(theta-2tau)/4.
```

At the optimum all four equal `18/19`, so merely retuning thresholds cannot help.

The cleanest new target is the **cell quartic itself**.  The current one-variable square sieve gives relative saving `T^(-1/2)`.  A stronger average over the four cell choices / fixed square-part packets, or a two-cell dispersion exploiting the exact `2 x 2` cell matrix, could improve the thin term and break the `18/19` optimisation barrier.

A second target is to improve the merged 4bv thick-packet exponent beyond `H^(-1/2)` by coupling the two quartic factors instead of square-sieving them independently.

Stage14-s7-09 should therefore audit a **two-cell / two-factor dispersion** on

```text
G1=(t*j*y^2)^2-(r*s*x^2)^2,
G2=(s*j*h^2)^2-(r*t*z^2)^2,
```

while retaining the physical nondegeneracy certificates `v/u!=1` and `uv!=1`.

---

## Boundary

```text
STAGE14_S7_08=COMPLETE_SHARED_XI_CELL_SWITCH_AND_18_19_WHOLE_FAMILY_BOUND
MERGED_S7_07_IMPORTED=true
MERGED_4BV_IMPORTED=true
SHARED_XI_FOUR_CELL_FACTORIZATION_EXACT=true
SHARED_XI_CELLS_PAIRWISE_COPRIME=true
PHYSICAL_CELL_QUARTIC_SQUARE_DEGENERATION=false
CELL_QUARTIC_STANDARD_WEIL_BOUND_APPLICABLE=true
CELL_SWITCH_RELATIVE_SAVING=T^(-1/2)
GENERAL_SMALL_DENOMINATOR_EXPONENT=2lambda
GENERAL_THICK_PACKET_EXPONENT=1-tau/2
GENERAL_SMALL_NUMERATOR_EXPONENT=1+theta-lambda
GENERAL_THIN_CELL_EXPONENT=1-(theta-2tau)/4
OPTIMAL_LAMBDA=9/19
OPTIMAL_TAU=2/19
OPTIMAL_THETA=8/19
ADAPTIVE_ARCHITECTURE_OPTIMAL_EXPONENT=18/19
PREVIOUS_WHOLE_FAMILY_EXPONENT=20/21
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
IMPROVEMENT_OVER_20_21=2/399
CUMULATIVE_SAVING_FROM_41_42=23/798
CURRENT_GAP_TO_SQRT=17/38
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-09
```
