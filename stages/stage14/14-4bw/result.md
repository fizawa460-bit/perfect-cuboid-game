# Stage14-4bw — shared-xi four-cell sieve and the 18/19 whole-family bound

## Purpose

Merged Stage14-4bv proves a strict saving on every thick square-part packet but leaves the thin packet as the obstruction.  The thin packet cannot be discarded because squarefree numerators or denominators naturally have square-part `1`.  What 4bv does prove is that every hard thin state carries a large squarefree coefficient.

The remaining issue is the shared product-square label

```text
ab = cd = xi,
```

which couples the coefficient variables.  Stage14-4bw keeps this coupling exactly, decomposes it into four pairwise-coprime gcd cells, and shows that a single large cell itself supports a one-variable square sieve.  This closes the thin branch without dropping the shared label.

After a three-parameter reoptimization, the whole-family exponent improves from `20/21` to

```text
18/19.
```

The square-root upper bound is still not proved.

---

## 1. Merged inputs

We use only merged results.

- Stage14-4bv: product-square packet
  `P=a*x^2, Q=b*y^2, R=c*z^2, S=d*w^2`,
  `ab=cd=xi`, and same-kernel square condition
  `G_ab(x,y)G_cd(z,w)=square`.
- Stage14-4bv: thick packet bound
  `N_thick(tau) << B^(1-tau/2+o(1))`.
- Stage14-s7-04/s7-07: fixed-coordinate `B^o(1)` opposite-fiber multiplicity and denominator hyperbola `QS<<B`.
- Stage14-4br/4bs: previous whole-family exponent `20/21`.

Write

```text
G_ab(x,y)=b^2*y^4-a^2*x^4.
```

The current task is only the thin square-part complement of 4bv, but we reoptimize all cutoffs at the end.

---

## 2. Exact four-cell decomposition of the shared label

The squarefree pairs satisfy

```text
gcd(a,b)=1,
gcd(c,d)=1,
ab=cd=xi.
```

Define

```text
alpha = gcd(a,c),
beta  = gcd(a,d),
gamma = gcd(b,c),
delta = gcd(b,d).
```

Prime by prime, every prime of `xi` occupies exactly one of these four cells.  Hence the cells are pairwise coprime and

```text
boxed:
a = alpha*beta,
b = gamma*delta,
c = alpha*gamma,
d = beta*delta,                                    (2.1)
```

with

```text
boxed:
xi = alpha*beta*gamma*delta.                       (2.2)
```

Conversely every four-tuple of pairwise-coprime squarefree cells produces a valid shared-label packet by (2.1).

Thus the shared `xi` condition is not dropped or relaxed: it is parametrized exactly.

---

## 3. The same-kernel polynomial in one shared cell

Substituting (2.1),

```text
G1 = (gamma*delta)^2*y^4-(alpha*beta)^2*x^4,
G2 = (beta*delta)^2*w^4-(alpha*gamma)^2*z^4.       (3.1)
```

The physical same-kernel condition is

```text
G1*G2 = square.                                    (3.2)
```

Fix every variable except `alpha`.  Then

```text
G1*G2
 = (A-B*alpha^2)(C-D*alpha^2),                    (3.3)
```

where

```text
A=(gamma*delta)^2*y^4,
B=beta^2*x^4,
C=(beta*delta)^2*w^4,
D=gamma^2*z^4.
```

The polynomial in (3.3) is a square polynomial only if

```text
A*D = B*C.
```

Since all variables are positive, this is equivalent to

```text
gamma*y*z = beta*x*w.                              (3.4)
```

But the two physical reduced coordinates are

```text
u=P/Q,
v=R/S,
0<v<u<1.
```

Using (2.1),

```text
sqrt(v/u)=gamma*y*z/(beta*x*w).                    (3.5)
```

Therefore (3.4) is exactly the forbidden boundary `v=u`.

Hence on the physical open chamber, the `alpha`-polynomial is a genuine nonsquare quartic.

The same check for the other cells gives:

```text
alpha degeneracy  <=> sqrt(v/u)=1,
delta degeneracy  <=> sqrt(v/u)=1,
beta  degeneracy  <=> sqrt(u*v)=1,
gamma degeneracy  <=> sqrt(u*v)=1.                (3.6)
```

Since `0<v<u<1`, neither boundary can occur.

Thus every one of the four shared cells is a valid one-variable nonsquare-quartic sieve variable.

---

## 4. One-cell Weil/completion contract

Let `t` denote any one of `alpha,beta,gamma,delta`, with all other packet variables fixed.  On the physical open chamber the square detector has the form

```text
H(t)=(A-B*t^2)(C-D*t^2),                           (4.1)
```

with `A*D != B*C`.

For an odd good prime `p` not dividing the coefficients or the quartic discriminant, the standard Weil bound for a fixed-degree nonsquare multiplicative-character polynomial, with an optional additive twist, gives uniformly in `h mod p`

```text
sum_{t mod p} chi_p(H(t))*e_p(h*t) << sqrt(p).     (4.2)
```

The implied constant is absolute because the degree is four.

For distinct good inert primes `p,q` of size `L`, CRT gives the corresponding bound modulo `m=pq`

```text
complete Fourier mode << sqrt(m) << L.             (4.3)
```

Fourier completion on an interval `I` of length `T` therefore gives

```text
boxed:
sum_{t in I} chi_m(H(t))
 << B^o(1)*(T/L+L).                                 (4.4)
```

The finitely many primes dividing packet coefficients, `A*D-B*C`, or the discriminant are excluded.  Since all packet integers have polynomial size in `B`, this removes only `B^o(1)` primes per fixed fiber.

---

## 5. One-cell square sieve

Apply the standard square sieve to `H(t)` over a dyadic cell interval `t~T`, using good inert primes `p=3 mod 4` in `[L,2L]`.

Equations (4.4) and the usual diagonal term give

```text
N_cell(T)
 << B^o(1)*(T/L + L).                              (5.1)
```

Choose

```text
L=T^(1/2).
```

Then

```text
boxed:
N_cell(T) << T^(1/2)*B^o(1).                       (5.2)
```

Thus a cell of size at least `B^rho` supplies the relative saving

```text
boxed:
B^(-rho/2+o(1)).                                   (5.3)
```

This is the coefficient-side analogue of the 4bv square-part saving, but crucially it preserves `ab=cd=xi` exactly because the moving variable is a shared gcd cell rather than an independent coefficient.

---

## 6. Summing one-cell fibers does not create a new power loss

For dyadic cells and square parts, the unsieved product-square state count is

```text
alpha*beta*gamma*delta
```

weighted by the square-part box sizes forced by

```text
P< Q~U,
R< S~V.
```

For fixed cells the square-part volume is, up to constants,

```text
UV/(alpha*beta*gamma*delta).
```

Therefore grouping one selected cell, say `alpha~T`, gives total raw cell-volume

```text
T * UV/(T*beta*gamma*delta)
 = UV/(beta*gamma*delta).
```

Summing dyadically over the remaining squarefree cells costs only reciprocal divisor sums and logarithms, hence `B^o(1)`.  Consequently the total unsieved volume over all one-cell fibers is still

```text
boxed:
UV*B^o(1) << B^(1+o(1)).                           (6.1)
```

A canonical tie-breaking rule chooses one large cell for every thin state, so there is no multiplicity beyond `O(1)`.

Combining (5.3) with (6.1), a sector in which the selected cell satisfies `t>=B^rho` obeys

```text
boxed:
N_selected-cell(rho) << B^(1-rho/2+o(1)).          (6.2)
```

---

## 7. General three-cutoff decomposition

Introduce three exponents.

```text
theta : denominator lower cutoff,
nu    : numerator lower cutoff,
tau   : square-part thickness cutoff.
```

### 7.1 Small denominator

If

```text
min(Q,S) <= B^theta,
```

then fixed-coordinate multiplicity gives

```text
E_den(theta)=2*theta.                               (7.1)
```

### 7.2 Balanced denominator and small numerator

On the complement,

```text
Q,S >= B^theta,
QS << B,
```

so

```text
Q,S <= B^(1-theta+o(1)).
```

If `P<=B^nu` or `R<=B^nu`, the corresponding reduced coordinate has at most

```text
B^(nu+1-theta+o(1))
```

choices and its physical opposite fiber has multiplicity `B^o(1)`.  Hence

```text
E_num(theta,nu)=1+nu-theta.                        (7.2)
```

### 7.3 Thick square-part packet

If

```text
min(x,y,z,w) >= B^tau,
```

merged 4bv gives

```text
E_thick(tau)=1-tau/2.                              (7.3)
```

### 7.4 Thin numerator square part

Assume `P,R>=B^nu`.  If, for example,

```text
x < B^tau,
```

then

```text
a=P/x^2 >= B^(nu-2tau-o(1)).
```

Since `a=alpha*beta`, one of the two cells is at least

```text
B^((nu-2tau)/2-o(1)).
```

By (6.2),

```text
E_numcell(nu,tau)
 = 1-(nu-2tau)/4.                                  (7.4)
```

The same holds for thin `z`.

### 7.5 Thin denominator square part

If, for example,

```text
y < B^tau,
```

then

```text
b=Q/y^2 >= B^(theta-2tau-o(1)).
```

One of `gamma,delta` is therefore at least

```text
B^((theta-2tau)/2-o(1)),
```

and

```text
E_dencell(theta,tau)
 = 1-(theta-2tau)/4.                               (7.5)
```

The same holds for thin `w`.

Thus the whole architecture is bounded by

```text
boxed:
E(theta,nu,tau)=max(
  2*theta,
  1+nu-theta,
  1-tau/2,
  1-(nu-2tau)/4,
  1-(theta-2tau)/4
).                                                  (7.6)
```

---

## 8. Exact minimax optimization

The exact optimum of (7.6) is

```text
boxed:
theta = 9/19,
nu    = 8/19,
tau   = 2/19.                                      (8.1)
```

Indeed the first four active branches are equal:

```text
2*theta
 = 18/19,

1+nu-theta
 = 18/19,

1-tau/2
 = 18/19,

1-(nu-2tau)/4
 = 18/19.                                          (8.2)
```

The denominator-thin cell branch is strictly smaller:

```text
1-(theta-2tau)/4
 = 71/76
 < 18/19.                                          (8.3)
```

Conversely, from

```text
2theta<=E,
1+nu-theta<=E,
1-tau/2<=E,
1-(nu-2tau)/4<=E,
```

one obtains the linear-programming lower bound `E>=18/19`; equality forces (8.1).  Hence `18/19` is the exact optimum of the current adaptive one-cell architecture, not an arbitrary threshold choice.

---

## 9. New whole-family upper bound

Using (8.1), every physical state lies in one of the following controlled sectors:

1. `min(Q,S)<=B^(9/19+o(1))`: exponent `18/19`;
2. balanced denominator but `min(P,R)<=B^(8/19+o(1))`: exponent `18/19`;
3. hard numerator and all square parts `>=B^(2/19-o(1))`: exponent `18/19` by merged 4bv;
4. hard numerator with a thin numerator square part: a selected shared cell is `>=B^(2/19-o(1))`, exponent `18/19` by the one-cell sieve;
5. hard numerator with a thin denominator square part: selected cell is `>=B^(5/38-o(1))`, exponent `71/76`.

Therefore

```text
boxed:
V(B) << B^(18/19+o(1)).                            (9.1)
```

This is a genuine new whole-family power saving.

Relative to the previous `20/21`, the gain is

```text
20/21 - 18/19 = 2/399.                             (9.2)
```

Relative to the post-local baseline `41/42`, the cumulative proved saving is

```text
41/42 - 18/19 = 23/798.                            (9.3)
```

The remaining exponent gap to square root is

```text
18/19 - 1/2 = 17/38.                               (9.4)
```

---

## 10. New barrier and next receiver

Threshold retuning inside the current architecture cannot improve `18/19`, because Section 8 is the exact minimax solution.

Four branches are simultaneously active at `18/19`:

```text
small denominator,
small numerator,
thick square-part dispersion,
thin numerator -> one-cell dispersion.
```

Therefore the next improvement must correlate at least two of these mechanisms rather than optimize one cutoff in isolation.  Natural next targets are:

- two-cell dispersion instead of selecting only one large cell;
- retaining the denominator hyperbola inside the cell square sieve;
- coupling small-numerator counting to the shared-cell support rather than using the raw rectangular count;
- combining the 4bv flat two-variable Fourier transform with the 4bw one-cell Weil receiver on a common refinement.

No square-root estimate is claimed here.

---

## Boundary

```text
STAGE14_4BW=SHARED_XI_FOUR_CELL_ONE_VARIABLE_SIEVE_AND_18_19_BOUND
MERGED_4BV_IMPORTED=true
SHARED_XI_FOUR_CELL_DECOMPOSITION_EXACT=true
SHARED_XI_DROPPED_IN_THIN_SWITCH=false
CELL_QUARTIC_NONSQUARE_ON_PHYSICAL_INTERIOR=true
ONE_CELL_WEIL_COMPLETION_ADAPTER_PROVED=true
ONE_CELL_SQUARE_SIEVE_RELATIVE_SAVING=T^(-1/2)
ONE_CELL_PACKET_TOTAL_VOLUME=B^(1+o(1))
OPTIMAL_DENOMINATOR_CUTOFF_EXPONENT=9/19
OPTIMAL_NUMERATOR_CUTOFF_EXPONENT=8/19
OPTIMAL_SQUAREPART_THRESHOLD_EXPONENT=2/19
ADAPTIVE_ONE_CELL_ARCHITECTURE_OPTIMAL_EXPONENT=18/19
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19
WHOLE_FAMILY_IMPROVEMENT_OVER_20_21=2/399
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=23/798
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
REMAINING_GAP_TO_SQRT=17/38
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4bx correlate the four active 18/19 bottlenecks using a joint two-cell / denominator-hyperbola dispersion receiver
```
