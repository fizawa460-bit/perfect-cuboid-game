# Stage14-s7-19 — cross-split collision composition into a primitive Pythagorean two-leg incidence

## Status

`COMPLETE_CROSS_SPLIT_PYTHAGOREAN_COMPOSITION_AND_TWO_LEG_DIVISOR_REDUCTION`

Merged Stage14-s7-18 proves that every off-diagonal same-`(xi,k)` collision on the old `7/8` critical shell is genuinely cross-split and has a large switching product.  Stage14-s7-19 now composes the two exact split-`k` equations before any auxiliary-prime average.

The product-square condition has an exact difference-of-squares composition.  Every surviving cross-split collision therefore produces a primitive integer Pythagorean triple whose hypotenuse is divisible by the switching part of `k`, while a second leg retains a large squarefree divisor inherited from `xi`.

This is unconditional and elementary.  It does not prove the requested power-saving count yet, but it replaces the mixed-split quartic pair by a much more rigid positive pair object.

The current whole-family exponent remains `7/8`.

---

## 1. Imported cross-split data

Take two distinct reduced states with the same squarefree labels

```text
xi=ker(P_1 Q_1)=ker(P_2 Q_2),
k =ker(Q_1^2-P_1^2)=ker(Q_2^2-P_2^2).
```

For state `i`, put

```text
g_i=gcd(Q_i-P_i,Q_i+P_i) in {1,2},
u_i=(Q_i-P_i)/g_i,
v_i=(Q_i+P_i)/g_i.
```

Merged s7-18 gives

```text
u_i=k_{-,i} r_i^2,
v_i=k_{+,i} s_i^2,
F_i:=v_i^2-u_i^2=xi z_i^2,
gcd(k,xi*z_i)=1.                                   (1.1)
```

For two different allocations of the same squarefree `k`, there are unique pairwise-coprime squarefree cells

```text
alpha,beta,gamma,delta
```

such that

```text
k_{-,1}=alpha*beta,
k_{+,1}=gamma*delta,
k_{-,2}=alpha*gamma,
k_{+,2}=beta*delta,
alpha*beta*gamma*delta=k.                           (1.2)
```

Define

```text
K_agree = alpha*delta,
K_switch= beta*gamma.                               (1.3)
```

Merged s7-18 proves, for every off-diagonal collision,

```text
K_switch >= k*sqrt(xi)/(sqrt(32) X^2),             (1.4)
```

where `P_i,Q_i<=X`.

Hence on the old critical shell

```text
xi~B^(3/4),
k>=B^(3/4-o(1)),
X<=B^(1/2+o(1)),
```

we have

```text
K_switch>=B^(1/8-o(1)).                            (1.5)
```

At the merged 4cd maximal-`k` endpoint `k=B^(1-o(1))`,

```text
K_switch>=B^(3/8-o(1)).                            (1.6)
```

---

## 2. Hyperbolic composition identity

Write

```text
U_1=alpha*beta*r_1^2,
V_1=gamma*delta*s_1^2,
U_2=alpha*gamma*r_2^2,
V_2=beta*delta*s_2^2.
```

Then

```text
V_1^2-U_1^2=xi*z_1^2,
V_2^2-U_2^2=xi*z_2^2.                               (2.1)
```

Use the exact identity

```text
(A^2-B^2)(C^2-D^2)
 =(AC+BD)^2-(AD+BC)^2.                             (2.2)
```

Define positive integers

```text
H = V_1*V_2 + U_1*U_2,
L = V_1*U_2 + U_1*V_2,
W = xi*z_1*z_2.                                     (2.3)
```

Then (2.1)-(2.2) give

```text
boxed:
H^2=L^2+W^2.                                       (2.4)
```

Thus every same-`(xi,k)` cross-split collision canonically produces an integer Pythagorean triple.

No character sum, square sieve, or auxiliary prime is used.

---

## 3. The switching and agreement products land on different Pythagorean legs

Expanding (2.3) with the four cells gives

```text
H
 = beta*gamma * (
     delta^2*s_1^2*s_2^2
     + alpha^2*r_1^2*r_2^2
   ),                                               (3.1)

L
 = alpha*delta * (
     gamma^2*s_1^2*r_2^2
     + beta^2*r_1^2*s_2^2
   ).                                               (3.2)
```

Therefore

```text
boxed:
K_switch | H,
K_agree  | L.                                       (3.3)
```

Also merged s7-18 gives

```text
gcd(k,W)=1.                                         (3.4)
```

Let

```text
d=gcd(H,L,W),
H_0=H/d,
L_0=L/d,
W_0=W/d.                                            (3.5)
```

Because `d|W` and `gcd(k,W)=1`,

```text
boxed:
gcd(d,k)=1.                                         (3.6)
```

Hence the full `k`-divisibility survives primitive reduction:

```text
boxed:
K_switch | H_0,
K_agree  | L_0.                                     (3.7)
```

Moreover

```text
gcd(H_0,L_0,W_0)=1,
H_0^2=L_0^2+W_0^2.                                  (3.8)
```

For a Pythagorean triple, (3.8) implies pairwise coprimality.  Thus `(H_0,L_0,W_0)` is a primitive Pythagorean triple.

---

## 4. A large squarefree part of xi survives on the primitive transverse leg

Define

```text
xi_0 = xi/gcd(xi,d).                                (4.1)
```

Since `xi` is squarefree, `xi_0` is squarefree.  Every prime of `xi_0` is absent from `d`, while `xi|W`; hence

```text
boxed:
xi_0 | W_0.                                         (4.2)
```

The three large divisors are now separated:

```text
K_switch | H_0,
K_agree  | L_0,
xi_0     | W_0,                                     (4.3)
```

with

```text
gcd(K_switch*K_agree,xi_0)=1.                      (4.4)
```

This is stronger bookkeeping than merely knowing `F_1 F_2` is a square: the switching support, agreement support, and surviving shared squarefree support occupy pairwise-coprime primitive Pythagorean coordinates.

---

## 5. The primitive gcd d cannot absorb too much of xi

From `K_switch|H_0` and `K_agree|L_0`,

```text
k=K_switch*K_agree | H_0*L_0.                      (5.1)
```

Since `0<L_0<H_0`,

```text
k < H_0^2=(H/d)^2.                                 (5.2)
```

For `P_i,Q_i<=X`,

```text
u_i=(Q_i-P_i)/g_i < X,
v_i=(Q_i+P_i)/g_i <= 2X,
```

so

```text
H=v_1 v_2+u_1 u_2 <= 5X^2.                         (5.3)
```

Combining (5.2)-(5.3),

```text
boxed:
d <= 5X^2/sqrt(k).                                 (5.4)
```

Therefore

```text
xi_0
 =xi/gcd(xi,d)
 >=xi/d
 >=xi*sqrt(k)/(5X^2).                              (5.5)
```

At exponent scale, if

```text
xi~B^gamma,
k~B^kappa,
X<=B^(1/2+o(1)),
```

then

```text
boxed:
log_B xi_0 >= gamma+kappa/2-1-o(1).                (5.6)
```

On the old `7/8` critical residual `gamma=3/4`, `kappa>=3/4-o(1)`,

```text
boxed:
xi_0>=B^(1/8-o(1)).                                (5.7)
```

At the merged 4cd endpoint `kappa=1-o(1)`,

```text
boxed:
xi_0>=B^(1/4-o(1)).                                (5.8)
```

Thus primitive reduction cannot hide the shared-label geometry inside a large common gcd.

---

## 6. Primitive Pythagorean parametrization

By the elementary parametrization of primitive Pythagorean triples, there exist coprime integers

```text
m>n>0,
gcd(m,n)=1,
m not congruent n (mod 2),
```

such that

```text
H_0=m^2+n^2,                                       (6.1)
```

and, after possibly exchanging the two legs,

```text
{L_0,W_0}={m^2-n^2, 2mn}.                          (6.2)
```

Consequently every surviving collision satisfies the exact norm-divisor condition

```text
boxed:
K_switch | m^2+n^2.                                (6.3)
```

At the same time the primitive transverse leg carries

```text
boxed:
xi_0 | W_0,
xi_0>=B^(1/8-o(1))                                 (6.4)
```

on the old critical shell, and `xi_0>=B^(1/4-o(1))` at the 4cd endpoint.

If `W_0=2mn`, the squarefree support of `xi_0` is allocated between the coprime factors `2,m,n`.  If `W_0=m^2-n^2`, it is allocated between the essentially coprime factors `m-n,m+n`.  In either orientation the allocation count is `B^o(1)`.

This creates a concrete two-leg divisor incidence rather than an abstract same-squareclass condition.

---

## 7. Exact local signature of switching primes

Let `ell` be an odd prime dividing `K_switch`.

From (6.3),

```text
m^2 == -n^2 (mod ell).
```

Because `gcd(m,n)=1`, `n` is invertible modulo `ell`, so `-1` is a quadratic residue modulo `ell`.  Hence

```text
boxed:
ell == 1 (mod 4).                                  (7.1)
```

There is also a statewise condition.  If `ell|beta`, then in state 1 it divides the minus kernel and in state 2 it divides the plus kernel.  Reducing (2.1) modulo `ell` gives both `xi` and `-xi` as nonzero quadratic residues.  The `gamma` case is symmetric.  Thus

```text
boxed:
(xi/ell)=+1,
(-1/ell)=+1
for every odd ell|K_switch.                        (7.2)
```

This is exact, but by itself it gives at most a thin-prime / logarithmic type restriction; no fixed-power global saving is claimed from (7.1)-(7.2) alone.

---

## 8. Correct live receiver after s7-19

The cross-split collision problem can now be routed through

```text
LargeSwitchPrimitivePythagoreanTwoLegIncidence:

H_0^2=L_0^2+W_0^2,
gcd(H_0,L_0,W_0)=1,
K_switch | H_0,
K_agree  | L_0,
xi_0     | W_0,
K_switch*K_agree=k,
xi_0=xi/gcd(xi,d),
gcd(k,xi_0)=1.
```

Quantitatively, on the old critical shell,

```text
K_switch >= B^(1/8-o(1)),
xi_0      >= B^(1/8-o(1)).                         (8.1)
```

On the actual merged 4cd endpoint capable of saturating `7/8`,

```text
K_switch >= B^(3/8-o(1)),
xi_0      >= B^(1/4-o(1)).                         (8.2)
```

The preferred next count keeps the physical lift `(alpha,beta,gamma,delta,r_i,s_i)` attached to the primitive pair `(m,n)`.  Counting bare Pythagorean triples and discarding the lift would lose the original selector/reconstruction geometry and is not declared sufficient.

---

## 9. Relation to toolbox-H0 and tH

Merged `Stage14-toolbox-H0` warns that a common coefficient space does not supply a statewise bridge from same `k` to the selector-sensitive Gaussian character rows.  Stage14-s7-19 does not assume such a bridge.

The Pythagorean reduction here is an exact positive **pair-level integer identity**.  It does not prove H0-C3 for the t/tH Gaussian rows and therefore must not be advertised as a completion of the Gaussian dispersion interface.

No new supervisor line is needed:

```text
TH15_NEEDED_BY_S7_19=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14_OR_TH15=false
```

The s-route can continue directly on the primitive two-leg divisor incidence.  Auxiliary-prime dispersion should be introduced only if the physical-lift count does not close by integer/bilinear geometry.

---

## 10. Quantitative ledger

Old critical shell:

```text
gamma=3/4,
kappa>=3/4.
```

Merged s7-18 switch lower exponent:

```text
kappa+gamma/2-1 >= 1/8.
```

New primitive shared-label divisor exponent:

```text
gamma+kappa/2-1 >= 1/8.
```

At the 4cd endpoint `kappa=1`:

```text
K_switch exponent >= 3/8,
xi_0 exponent      >= 1/4,
d exponent         <= 1/2.
```

No new unconditional whole-family exponent is claimed:

```text
V(B) << B^(7/8+o(1)).
```

The requested power-saving cross-split pair count remains open.

---

## 11. Next receiver

Stage14-s7-20 should attack the physical lifts of

```text
K_switch | m^2+n^2,
xi_0 | W_0,
{L_0,W_0}={m^2-n^2,2mn},
```

with the endpoint lower scales

```text
K_switch>=B^(3/8-o(1)),
xi_0>=B^(1/4-o(1)),
```

before introducing a new auxiliary character average.

The first target remains

```text
E_off,critical(B) << B^(7/8-delta+o(1))
```

for some fixed `delta>0`.

---

## 12. Stage boundary

```text
STAGE14_S7_19=COMPLETE_CROSS_SPLIT_PYTHAGOREAN_COMPOSITION_AND_TWO_LEG_DIVISOR_REDUCTION
MERGED_S7_18_IMPORTED=true
MERGED_4CD_ENDPOINT_IMPORTED=true
MERGED_TOOLBOX_H0_BOUNDARY_IMPORTED=true
CROSS_SPLIT_HYPERBOLIC_COMPOSITION_EXACT=true
CROSS_SPLIT_PYTHAGOREAN_TRIPLE_EXACT=true
PYTHAGOREAN_PRIMITIVE_GCD_D_DEFINED=true
GCD_D_K=1
K_SWITCH_DIVIDES_PRIMITIVE_HYPOTENUSE=true
K_AGREE_DIVIDES_PRIMITIVE_LEG=true
XI0_DIVIDES_PRIMITIVE_TRANSVERSE_LEG=true
PRIMITIVE_GCD_BOUND=d<=5*X^2/sqrt(k)
CRITICAL_PRIMITIVE_XI0_LOWER_EXPONENT=1/8
FOUR_CD_ENDPOINT_PRIMITIVE_XI0_LOWER_EXPONENT=1/4
CRITICAL_SWITCH_PRODUCT_LOWER_EXPONENT=1/8
FOUR_CD_ENDPOINT_SWITCH_PRODUCT_LOWER_EXPONENT=3/8
ODD_SWITCH_PRIMES_ARE_1_MOD_4=true
ODD_SWITCH_PRIMES_SEE_XI_AS_QUADRATIC_RESIDUE=true
LARGE_SWITCH_PRIMITIVE_PYTHAGOREAN_TWO_LEG_INCIDENCE_REQUIRED=true
LARGE_SWITCH_PRIMITIVE_PYTHAGOREAN_TWO_LEG_INCIDENCE_POWER_SAVING_PROVED=false
LARGE_DISAGREEMENT_CROSS_SPLIT_K_COLLISION_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH15_NEEDED_BY_S7_19=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14_OR_TH15=false
NEXT=Stage14-s7-20
```