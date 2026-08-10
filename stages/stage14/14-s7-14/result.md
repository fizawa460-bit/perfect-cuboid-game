# Stage14-s7-14 — large shared-label shell and the transverse `k`-collision receiver

## Purpose

Merged Stage14-s7-13 proves the unconditional whole-family bound

```text
V(B) << B^(7/8+o(1)).
```

Its equality geometry is

```text
P,Q ~ B^(1/2),
a,b ~ B^(3/8),
x,y ~ B^(1/16),
xi=ab ~ B^(3/4),
```

for the canonical decomposition

```text
P=a*x^2,
Q=b*y^2,
```

with `a,b` squarefree and coprime.

The natural next idea is that the very large common squarefree label

```text
xi=ab=cd
```

might itself be sparse enough to beat `7/8`.

Stage14-s7-14 audits that idea exactly.

The conclusion is a structural closure rather than a new exponent:

1. after summing by the shared label `xi`, the coordinate support has exponent `(1+gamma)/2` on `xi~B^gamma`;
2. the already-proved adjacent two-cell theorem gives exponent `1-gamma/6` on the same shell;
3. these two valid bounds cross exactly at `gamma=3/4`, with value `7/8`;
4. the large shared label therefore does **not** by itself improve the merged `7/8` theorem;
5. the remaining genuinely transverse label is
   `k=ker(Q^2-P^2)`;
6. physical activation is an off-diagonal collision in the joint label `(xi,k)`, and a power-saving average bound for that collision energy is the next required theorem.

No new whole-family exponent is claimed in this stage.

---

## 1. Merged inputs

We use only merged repository inputs.

### 1.1 Stage14-s7-13

For the shorter reduced coordinate

```text
u=P/Q,
0<P<Q,
```

merged s7-13 gives

```text
P,Q <= B^(1/2+o(1)),
P=a*x^2,
Q=b*y^2,
```

and the exact shared-label relation

```text
xi=ab=cd.
```

The current unconditional bound is

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8.
```

### 1.2 Shared four-cell factorization

The squarefree coefficient pairs admit the exact factorization

```text
a=r*s,
b=t*j,
c=r*t,
d=s*j,
xi=r*s*t*j,
```

with the four cells pairwise coprime and squarefree.

### 1.3 Adjacent two-cell theorem

Merged s7-10 / 4by proves that if a selected adjacent coefficient

```text
C in {a,b,c,d}
```

has size at least `B^rho`, then the corresponding restricted physical packet collection satisfies

```text
#states << B^(1-rho/3+o(1)).
```

This theorem is used only once on any packet.  No pairwise saving is multiplied.

### 1.4 Fixed `(xi,k)` genus-one receiver

Merged s7-05/s7-06 identifies

```text
xi = ker(PQ),
k  = ker(Q^2-P^2),
```

and the genus-one quartic

```text
C_{k,xi}: k*v^2 = 1-xi^2*z^4.
```

A physical pair is an off-diagonal two-point incidence on one such quartic.  For fixed `(xi,k)`, the Stage14 bounded-height genus-one mechanism gives only `B^o(1)` points in the relevant polynomial-height range.

---

## 2. Exact support count on a shared-label shell

Dyadically fix

```text
xi ~ B^gamma,
0<=gamma<=1.
```

Because `a,b` are coprime squarefree and

```text
ab=xi,
```

every prime divisor of `xi` is allocated to exactly one of `a` and `b`.

Hence the number of ordered coefficient pairs `(a,b)` for a fixed squarefree `xi` is exactly

```text
2^omega(xi).
```

Uniformly in the Stage14 polynomial range,

```text
2^omega(xi) <= tau(xi) = B^o(1).                   (2.1)
```

So the allocation of the squarefree support is exponent-neutral.

Now

```text
P=a*x^2 <= B^(1/2+o(1)),
Q=b*y^2 <= B^(1/2+o(1)).
```

Multiplying,

```text
P*Q = xi*(x*y)^2 <= B^(1+o(1)),
```

and therefore

```text
x*y <= B^((1-gamma)/2+o(1)).                       (2.2)
```

The number of positive pairs `(x,y)` with product at most `X` is

```text
O(X log(2X))=X^(1+o(1)).
```

Thus, for fixed `xi`, the number of canonical reduced-coordinate candidates is at most

```text
B^((1-gamma)/2+o(1)).                              (2.3)
```

There are at most

```text
B^(gamma+o(1))
```

squarefree labels in the shell.  Consequently

```text
boxed:
N_support(gamma)
 << B^((1+gamma)/2+o(1)).                           (2.4)
```

Reducedness, ordering, and the physical chamber can only decrease this count.

Using the merged fixed-coordinate `B^o(1)` physical multiplicity, (2.4) transfers to the whole physical family on the same shell.

### 2.1 Why `xi~B^(3/4)` reproduces `7/8`

At

```text
gamma=3/4,
```

(2.4) is

```text
B^((1+3/4)/2+o(1)) = B^(7/8+o(1)).
```

Equivalently, at the s7-13 equality block,

```text
#xi shells      ~ B^(3/4),
internal xy mass ~ B^(1/8),
```

and their product is exactly `B^(7/8)` at exponent scale.

Thus merely regrouping by the large shared label does not create a new power saving.

---

## 3. The existing two-cell theorem on the same `xi` shell

Because

```text
a*b=xi,
```

at least one of `a,b` satisfies

```text
max(a,b) >= xi^(1/2) >= B^(gamma/2-o(1)).           (3.1)
```

Both `a=r*s` and `b=t*j` are legitimate adjacent two-cell products.

Select the larger one canonically.  The merged two-cell theorem then gives

```text
boxed:
N_2cell(gamma)
 << B^(1-gamma/6+o(1)).                             (3.2)
```

Again this is a separate upper bound on the same `xi` shell; it is not multiplied with (2.4).

Therefore the valid shared-label receiver is

```text
boxed:
N_xi-shell(gamma)
 << B^( min((1+gamma)/2, 1-gamma/6) + o(1)).        (3.3)
```

---

## 4. Exact `xi`-only minimax: the barrier is still `7/8`

Define

```text
F(gamma)
 = min((1+gamma)/2, 1-gamma/6).
```

The support branch increases with `gamma`, while the two-cell branch decreases.

Their crossing is

```text
(1+gamma)/2 = 1-gamma/6
<=> 3+3gamma = 6-gamma
<=> 4gamma=3
<=> boxed: gamma=3/4.                               (4.1)
```

At the crossing,

```text
(1+3/4)/2 = 7/8,
1-(3/4)/6 = 7/8.                                   (4.2)
```

Hence

```text
boxed:
max_{0<=gamma<=1} F(gamma)=7/8.                    (4.3)
```

This exactly reproduces the merged s7-13 exponent.

Therefore

```text
LARGE_SHARED_LABEL_SUPPORT_ALONE_BEATS_7_8=false.
```

The shared-label reorganization is useful because it isolates the true remaining degree of freedom, but it is not itself a new power-saving theorem.

---

## 5. A critical cell pattern saturates the existing one-/two-cell receivers

The `xi=3/4` shell is not ruled out by the exact four-cell geometry.

At exponent scale consider

```text
r ~ B^(1/4),
s ~ B^(1/8),
t ~ B^(1/8),
j ~ B^(1/4).                                       (5.1)
```

Then

```text
a=r*s ~ B^(3/8),
b=t*j ~ B^(3/8),
c=r*t ~ B^(3/8),
d=s*j ~ B^(3/8),
xi=r*s*t*j ~ B^(3/4).                              (5.2)
```

This exponent vector is compatible with pairwise-coprime squarefree cells: the prime supports can be chosen disjoint.  We do **not** claim that physical solutions actually saturate this vector; it is an architecture witness showing that the present inequalities do not exclude it.

For this vector:

- the largest individual cell exponent is `1/4`;
- the merged one-cell relative saving `T^(-1/2)` gives the global envelope
  ```text
  1-(1/4)/2 = 7/8;
  ```
- every physical adjacent coefficient has exponent `3/8`;
- the merged two-cell relative saving `C^(-1/3)` gives
  ```text
  1-(3/8)/3 = 7/8.
  ```

Thus neither the already-proved one-cell theorem nor the already-proved adjacent two-cell theorem separates the critical large-`xi` shell.

Merged s7-11 additionally proves that simply adding a third or fourth cell to the **same** square detector does not produce an independent arithmetic condition.  Therefore the next gain must use information transverse to the shared-label/cell decomposition.

---

## 6. The transverse label `k`

For every reduced coordinate define

```text
boxed:
k = ker(Q^2-P^2).                                   (6.1)
```

Since `gcd(P,Q)=1`,

```text
gcd(Q^2-P^2,P)=1,
gcd(Q^2-P^2,Q)=1.
```

Also

```text
xi=ker(PQ).
```

Therefore

```text
boxed:
gcd(k,xi)=1.                                       (6.2)
```

This is exact, not just a generic statement.

Because `P<Q<=B^(1/2+o(1))`,

```text
Q^2-P^2 <= B^(1+o(1)),
```

so

```text
boxed:
k <= B^(1+o(1)).                                   (6.3)
```

On the critical large-label shell

```text
xi ~ B^(3/4),
```

the associated `j=1728` Jacobian twist parameter

```text
n=k*xi
```

therefore obeys the sharper critical-shell range

```text
boxed:
n <= B^(7/4+o(1)).                                 (6.4)
```

This improves the coarse earlier `n<<B^2` range only on the newly isolated critical shell; it is not by itself a counting saving.

---

## 7. Exact `(xi,k)` collision-energy receiver

Let `C_B(xi)` be the set of canonical reduced coordinates `P/Q` in the Stage14 physical height window with

```text
ker(PQ)=xi.
```

For squarefree `k`, define

```text
r_B(xi,k)
 = #{P/Q in C_B(xi): ker(Q^2-P^2)=k}.              (7.1)
```

The merged s7-05 exact label identities say that a physical off-diagonal pair must have the **same** `xi` and the **same** `k`.

Hence the ordered off-diagonal collision count is bounded by

```text
boxed:
E_off(B)
 = sum_xi sum_k r_B(xi,k)*(r_B(xi,k)-1).            (7.2)
```

The physical chamber, primitive orientation, and first-point condition select a subset of these collisions, so (7.2) is a valid receiver.

On the critical shell `xi~B^(3/4+o(1))`, the current support theorem gives

```text
sum_xi sum_k r_B(xi,k)
 << B^(7/8+o(1)).                                   (7.3)
```

To beat the present exponent it is enough to prove a genuinely average collision saving of the form

```text
boxed:
E_off,critical(B)
 << B^(7/8-delta+o(1))                              (7.4)
```

for some fixed `delta>0`, followed by the standard small slack split away from the critical `xi` shell.

Equation (7.4), or an equivalent first-point/twist-incidence theorem, is the next s7 target.

---

## 8. Why fixed-twist `B^o(1)` multiplicity is not enough

For fixed `(xi,k)`, the genus-one bounded-height theorem gives

```text
r_B(xi,k) <= B^o(1).                                (8.1)
```

But (8.1) alone only implies

```text
E_off(B)
 <= B^o(1) * sum_xi,k r_B(xi,k),                   (8.2)
```

which on the critical shell is still

```text
B^(7/8+o(1)).
```

There is no power saving.

This is not a technicality.  Even an abstract family with multiplicity exactly two on `N/2` labels has

```text
max r = 2,
sum r = N,
sum r(r-1)=N,
```

so uniformly bounded pointwise multiplicity does not imply a sparse collision set.

What is missing is an **average recurrence theorem** for the map

```text
P/Q -> (xi,k),
```

not a stronger fixed-fiber bound.

---

## 9. Updated architecture ledger

The current unconditional whole-family exponent remains

```text
boxed:
V(B) << B^(7/8+o(1)).                               (9.1)
```

No new power saving is promoted in s7-14.

The cumulative saving from the post-local baseline remains

```text
41/42 - 7/8 = 17/168.                               (9.2)
```

The remaining gap to square root remains

```text
7/8 - 1/2 = 3/8.                                   (9.3)
```

The value of this stage is the sharper obstruction statement:

```text
large xi support
+ squarefree-support allocation
+ one-cell dispersion
+ adjacent two-cell dispersion
+ fixed-(xi,k) genus-one multiplicity
```

still does not force an exponent below `7/8`.

The next theorem must control **off-diagonal recurrence in the transverse `k` label**.

---

## 10. Next receiver

Stage14-s7-15 should work directly with the critical-shell collision energy

```text
sum_{xi~B^(3/4)} sum_k r_B(xi,k)(r_B(xi,k)-1),
```

while retaining

```text
xi squarefree,
k squarefree,
gcd(xi,k)=1,
xi~B^(3/4),
k<=B^(1+o(1)),
n=xi*k<=B^(7/4+o(1)).
```

The first options to audit are:

1. a squareclass large sieve in the **difference label** `k`, conditioned on `xi`;
2. a two-point determinant/dispersion theorem for the quartics `C_{k,xi}` averaged over `xi`;
3. a collision-energy estimate that keeps the small squarepart variables `(x,y)` before Cauchy;
4. an exact bridge to any already-merged Stage14 squareclass/Frobenius receiver, but only after proving that its operator is the same `(xi,k)` incidence and not merely analogous.

No tH result is imported here without such an exact bridge.

---

## 11. Stage boundary

```text
STAGE14_S7_14=COMPLETE_LARGE_SHARED_LABEL_SHELL_AND_TRANSVERSE_K_COLLISION_RECEIVER
MERGED_S7_13_IMPORTED=true
MERGED_S7_10_TWO_CELL_THEOREM_IMPORTED=true
SHARED_LABEL_XI=ker(PQ)=a*b
FIXED_XI_ORDERED_AB_PARTITION_COUNT=2^omega(xi)
FIXED_XI_PARTITION_MULTIPLICITY=B^o(1)
XI_SHELL_COORDINATE_SUPPORT_EXPONENT=(1+gamma)/2
XI_SHELL_SELECTED_TWO_CELL_EXPONENT=1-gamma/6
XI_ONLY_MINIMAX_CRITICAL_EXPONENT=gamma=3/4
XI_ONLY_MINIMAX_BARRIER=7/8
CRITICAL_INTERNAL_SQUAREPART_PRODUCT_EXPONENT=1/8
CRITICAL_ANISOTROPIC_CELL_PATTERN=(1/4,1/8,1/8,1/4)
EXISTING_ONE_CELL_ENVELOPE_ON_CRITICAL_PATTERN=7/8
EXISTING_TWO_CELL_ENVELOPE_ON_CRITICAL_PATTERN=7/8
LARGE_XI_SUPPORT_ALONE_BEATS_7_8=false
TRANSVERSE_LABEL_K=ker(Q^2-P^2)
GCD_K_XI=1
CRITICAL_K_MAX_EXPONENT=1
CRITICAL_J1728_TWIST_N_MAX_EXPONENT=7/4
PHYSICAL_PAIR_REQUIRES_SAME_XI_AND_SAME_K=true
OFF_DIAGONAL_XI_K_COLLISION_ENERGY_RECEIVER_DEFINED=true
FIXED_XI_K_POINTWISE_MULTIPLICITY_ALONE_GIVES_POWER_SAVING=false
OFF_DIAGONAL_XI_K_COLLISION_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-15
```
