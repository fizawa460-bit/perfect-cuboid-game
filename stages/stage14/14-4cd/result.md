# Stage14-4cd — four-root lattice congruence and maximal-k endpoint localization

## Purpose

Merged Stage14-4cc localizes the current whole-family `7/8` critical residual to

```text
xi = ker(PQ) = B^(3/4+o(1)),
k  = ker(Q^2-P^2) >= B^(3/4-o(1)),
```

for the shorter reduced coordinate `u=P/Q`, with `0<P<Q`, `gcd(P,Q)=1`, and `Q<=B^(1/2+o(1))`.

Merged Stage14-s7-15 then splits the difference kernel through `Q-P` and `Q+P`, while merged Stage14-tH14 / t51 isolate the still-unproved selector-sensitive off-diagonal Gaussian completion.  Stage14-4cd does **not** assume that completion.

Instead, 4cd combines the canonical square-part roots of

```text
P,
Q,
Q-P,
Q+P
```

before any square sieve.  The four roots force one exact rank-one congruence lattice on the two squarefree difference kernels.  On the critical `xi` shell this gives a new support exponent

```text
1/8 + (d+kappa)/2,
```

where

```text
Q-P ~ B^d,
k   ~ B^kappa.
```

Consequently every fixed-power departure from either

```text
d=1/2
```

or

```text
kappa=1
```

is already strictly below `7/8`.

The only residual capable of saturating the current exponent is therefore the endpoint

```text
P,Q,Q-P,Q+P ~ B^(1/2),
xi ~ B^(3/4),
k ~ B,
```

with essentially squarefree difference factors.  The current global exponent remains `7/8`; the point of this stage is the stronger unconditional localization.

---

## 1. Merged inputs

We use only merged results.

### 1.1 Current physical bound and critical xi shell

Merged s7-13 / 4cb / 4cc give

```text
V(B) << B^(7/8+o(1)).
```

A block can approach the `7/8` ceiling only when the shorter reduced coordinate has

```text
P,Q ~ B^(1/2),
P=a*x^2,
Q=b*y^2,
a,b ~ B^(3/8),
x,y ~ B^(1/16),
xi=ab ~ B^(3/4).
```

In particular

```text
P*Q = xi*(x*y)^2
```

forces

```text
x*y = B^(1/8+o(1)).                              (1.1)
```

### 1.2 Difference-kernel split

Merged s7-15 gives

```text
g = gcd(Q-P,Q+P) in {1,2},
A = (Q-P)/g,
C = (Q+P)/g,
A = k_- * r^2,
C = k_+ * s^2,
```

with

```text
k_-, k_+ squarefree,
gcd(k_-,k_+)=1,
k = k_-*k_+ = ker(Q^2-P^2).                      (1.2)
```

Merged 4cc gives the weaker shell receiver

```text
N_k-shell(kappa) << B^((1+kappa)/2+o(1)).
```

Stage14-4cd improves this specifically on the critical `xi` shell by using `x,y,r,s` simultaneously.

### 1.3 tH14 / t51 boundary

Merged tH14 closes the same-modulus residue-collision contribution but leaves

```text
SelectorSensitiveGaussianCompletion
```

unproved.  Merged t51 closes the alias-free exact-pair diagonal and leaves only the off-diagonal residue/frequency dispersion.

No statement from either stage that is marked unproved is used below.

---

## 2. Primitive coprimality of all four square-part roots

Write the canonical decompositions

```text
P = a*x^2,
Q = b*y^2,
A = k_-*r^2,
C = k_+*s^2.
```

Because `gcd(P,Q)=1`,

```text
gcd(x,y)=1.                                       (2.1)
```

Because `gcd(A,C)=1`,

```text
gcd(r,s)=1.                                       (2.2)
```

More importantly,

```text
boxed:
gcd(x*y,r*s)=1.                                   (2.3)
```

For an odd prime `ell`, if for example `ell|x` and `ell|r`, then `ell|P` and `ell|(Q-P)`, hence `ell|Q`, contradicting `gcd(P,Q)=1`.  The other three cross-pairs are identical.

At `ell=2`, if `g=1` then `P,Q` have opposite parity, so `Q-P` and `Q+P` are odd and therefore `r,s` are odd.  If `g=2`, then primitive `P,Q` are both odd, so `x,y` are odd.  Thus no factor 2 is shared either.

Hence every coefficient used below is invertible modulo `x^2 y^2`.

---

## 3. Exact two-kernel congruence lattice

From

```text
Q-P = g*k_-*r^2,
Q+P = g*k_+*s^2,
```

we obtain

```text
2P = g*(k_+*s^2-k_-*r^2),
2Q = g*(k_+*s^2+k_-*r^2).
```

Put

```text
c_g = 2/g in {1,2}.
```

Using `P=a*x^2`, `Q=b*y^2`,

```text
k_+*s^2-k_-*r^2 = c_g*a*x^2,                    (3.1)
k_+*s^2+k_-*r^2 = c_g*b*y^2.                    (3.2)
```

Therefore

```text
k_+*s^2 ==  k_-*r^2  (mod x^2),                  (3.3)
k_+*s^2 == -k_-*r^2  (mod y^2).                  (3.4)
```

By (2.3), `r*s` is a unit modulo `x^2 y^2`.  Since `gcd(x,y)=1`, CRT gives a unique unit

```text
lambda = lambda(x,y,r,s) mod M,
M=x^2*y^2,
```

such that the two congruences are equivalent to

```text
boxed:
k_+ == lambda*k_- (mod M).                        (3.5)
```

This is an exact pre-sieve dimension reduction: the two moving squarefree difference kernels lie in one rank-one congruence lattice of determinant `M=x^2 y^2`.

No character cancellation is used.

---

## 4. Rectangle count in the congruence lattice

Let

```text
k_- ~ K_-,
k_+ ~ K_+.
```

Dropping squarefreeness and all coprimality restrictions only enlarges the set.  The number of positive integer pairs in the rectangle satisfying (3.5) is

```text
boxed:
N_lattice(K_-,K_+;M)
 << K_-*K_+/M + K_- + K_+ + 1.                   (4.1)
```

This is the standard determinant-`M` lattice box estimate.  It can also be seen directly by fixing `k_-`: each row contains at most `K_+/M+1` admissible `k_+`, and then symmetrizing the boundary term.

Now dyadically fix

```text
x~X,
y~Y,
r~R,
s~S.
```

There are `O(XYRS)` root quadruples.  Thus

```text
N_block
 << XYRS * (
      K_-*K_+/(X^2Y^2)
      + K_-
      + K_+
      + 1
    ) * B^o(1).                                   (4.2)
```

The `B^o(1)` absorbs dyadic endpoints and the harmless factor-2 parity split.

---

## 5. Critical-shell exponent calculation

Remain on the only shell that can approach the current `7/8` bound:

```text
P,Q ~ B^(1/2),
xi ~ B^(3/4).
```

Write

```text
Q-P ~ B^d,            0<=d<=1/2,                 (5.1)
k   ~ B^kappa,        3/4-o(1)<=kappa<=d+1/2.   (5.2)
```

Since `Q+P~B^(1/2)`,

```text
Q^2-P^2
 = (Q-P)(Q+P)
 ~ B^(d+1/2).                                      (5.3)
```

By (1.2),

```text
Q^2-P^2 = g^2*k*(r*s)^2.
```

Hence

```text
R*S = B^((d+1/2-kappa)/2+o(1)).                  (5.4)
```

From (1.1),

```text
X*Y = B^(1/8+o(1)).                               (5.5)
```

### 5.1 Main lattice-volume term

The product `K_-K_+` is, up to `B^o(1)`,

```text
K_-K_+
 = k
 ~ B^kappa.                                       (5.6)
```

Equivalently using the factor sizes,

```text
K_-K_+ ~ B^(d+1/2)/(R^2S^2).
```

The first term of (4.2) therefore has exponent

```text
kappa - 2*(1/8) + 1/8 + (d+1/2-kappa)/2
= 1/8 + (d+kappa)/2.                              (5.7)
```

Thus

```text
boxed:
E_main(d,kappa)=1/8+(d+kappa)/2.                  (5.8)
```

### 5.2 Boundary terms do not dominate in the 4cc critical range

Let

```text
alpha_- = log_B K_-,
alpha_+ = log_B K_+.
```

Since `K_-*R^2~B^d` and `K_+*S^2~B^(1/2)`,

```text
alpha_-<=d,
alpha_+<=1/2,
alpha_-+alpha_+=kappa.                            (5.9)
```

The `K_-` boundary term in (4.2) has exponent at most

```text
E_- <= 3/8 + 3d/2 - kappa/2.                     (5.10)
```

For the live range `kappa>=3/4` and `d<=1/2`,

```text
E_- - E_main <= 1/4+d-kappa <= 0.                 (5.11)
```

The `K_+` boundary term has exponent at most

```text
E_+ <= 7/8 + d/2 - kappa/2,                      (5.12)
```

and

```text
E_+ - E_main <= 3/4-kappa <= 0.                  (5.13)
```

The root-count-only term is smaller still.

Hence throughout the 4cc critical `k` range,

```text
boxed:
N_critical(d,kappa)
 << B^(1/8+(d+kappa)/2+o(1)).                     (5.14)
```

This is unconditional.

---

## 6. Maximal-k endpoint localization

Because

```text
d<=1/2,
kappa<=1,
```

(5.14) implies

```text
1/8+(d+kappa)/2 <= 7/8.                           (6.1)
```

Moreover, for every fixed `delta>0`, either condition

```text
d <= 1/2-delta                                   (6.2)
```

or

```text
kappa <= 1-delta                                 (6.3)
```

gives

```text
boxed:
N_critical
 << B^(7/8-delta/2+o(1)).                         (6.4)
```

Therefore a sequence of blocks can remain at the `7/8` exponent only if

```text
boxed:
d = 1/2-o(1),
kappa = 1-o(1).                                   (6.5)
```

That is,

```text
boxed:
Q-P ~ B^(1/2+o(1)),
k = B^(1-o(1)).                                    (6.6)
```

Since `Q+P~B^(1/2)`, both difference factors are at the full square-root scale.

This strictly sharpens the 4cc residual `k>=B^(3/4-o(1))` to an endpoint condition.

---

## 7. Difference square parts become subpolynomial

From (5.4) and (6.5),

```text
R*S = B^o(1).                                      (7.1)
```

Hence individually

```text
r,s = B^o(1).                                      (7.2)
```

Therefore

```text
k_- = B^(1/2+o(1)),
k_+ = B^(1/2+o(1)).                                (7.3)
```

In words: on the only remaining `7/8` endpoint, both

```text
(Q-P)/g
```

and

```text
(Q+P)/g
```

are squarefree up to a subpolynomial square factor.

Combining with the already-merged `xi` equality geometry gives the full hard core

```text
boxed:
P,Q,Q-P,Q+P          ~ B^(1/2),
a,b                  ~ B^(3/8),
x,y                  ~ B^(1/16),
xi=ab                 ~ B^(3/4),
k_-,k_+              ~ B^(1/2),
r,s                   = B^o(1),
k=k_-k_+              ~ B.                        (7.4)
```

---

## 8. Twist band collapses to its top edge

Merged 4cc only knew

```text
B^(3/2-o(1)) <= n=xi*k <= B^(7/4+o(1)).
```

Using

```text
xi=B^(3/4+o(1)),
k=B^(1+o(1)),
```

from the endpoint localization,

```text
boxed:
n=xi*k = B^(7/4+o(1)).                            (8.1)
```

Thus the entire `7/8` obstruction lies at the **top edge** of the squarefree `j=1728` twist range, not throughout the former `[3/2,7/4]` band.

---

## 9. Exact odd-prime residue signature of the endpoint packet

The two equations (3.1)-(3.2) also give a transverse quadratic-residue graph between the four large squarefree coefficients.

For every odd prime `ell` dividing `a`, equation (3.1) modulo `ell` gives

```text
k_+*s^2 == k_-*r^2 (mod ell),
```

hence

```text
boxed:
(k/ell)=+1.                                        (9.1)
```

For every odd `ell|b`, equation (3.2) gives

```text
k_+*s^2 == -k_-*r^2 (mod ell),
```

hence

```text
boxed:
(-k/ell)=+1.                                       (9.2)
```

For every odd `ell|k_-`, reducing (3.1) and (3.2) gives

```text
c_g*a*x^2 == c_g*b*y^2 (mod ell),
```

and therefore

```text
boxed:
(xi/ell)=+1.                                       (9.3)
```

For every odd `ell|k_+`, the same calculation with the sign from (3.1) gives

```text
boxed:
(-xi/ell)=+1.                                      (9.4)
```

The four conditions are compatible with `gcd(xi,k)=1` and are exact; no probabilistic independence is asserted.

They define the next arithmetic receiver:

```text
(a,b)  <-->  (k_-,k_+)
```

through a signed quadratic-residue incidence graph at scales

```text
a,b ~ B^(3/8),
k_-,k_+ ~ B^(1/2).
```

Merely multiplying local half-densities is forbidden; any power saving must come from a genuine bilinear/dispersion theorem on this graph or from the merged tH14/t51 selector-sensitive Gaussian route.

---

## 10. tH / selector-sensitive status

Stage14-tH14 has now been completed and merged.

What it proves:

```text
same-modulus residue collision energy is at target scale;
nonexact two-prime residue collisions are divisor-controlled.
```

What it does **not** prove:

```text
SelectorSensitiveGaussianCompletion.
```

Merged t51 additionally closes the alias-free exact-pair diagonal and leaves

```text
OffDiagonalTwoAuxiliaryGaussianResidueDispersion
```

as the live t-track theorem.

Accordingly 4cd does not request a new supervisor stage:

```text
TH14_CONSUMED=true,
TH15_NEEDED=false.
```

The t-track can continue with t52 while the 14-4 line attacks the endpoint residue graph independently.

---

## 11. Current exponent and next receiver

No new global fixed-power saving is claimed because the exact endpoint

```text
d=1/2,
kappa=1
```

still permits the support exponent `7/8` in (5.14).

Therefore

```text
boxed:
V(B) << B^(7/8+o(1))
```

remains the current unconditional physical upper bound.

But the obstruction is now much narrower than at 4cc:

```text
xi~B^(3/4)
```

alone is no longer enough, nor is merely

```text
k>=B^(3/4).
```

The surviving endpoint requires all four linear factors

```text
P,
Q,
Q-P,
Q+P
```

to be at square-root scale with the exact squarefree/square-part pattern (7.4), plus the residue signature (9.1)-(9.4).

The next 14-4 task should attack this endpoint via one of two genuinely transverse routes:

1. bilinear quadratic-residue dispersion between `(a,b)` and `(k_-,k_+)`;
2. an exact bridge from this endpoint packet into the merged tH14/t51 off-diagonal Gaussian selector problem.

Accordingly

```text
NEXT=Stage14-4ce.
```

---

## 12. Stage boundary

```text
STAGE14_4CD=FOUR_ROOT_LATTICE_CONGRUENCE_AND_MAXIMAL_K_ENDPOINT_LOCALIZATION
MERGED_4CC_IMPORTED=true
MERGED_S7_15_IMPORTED=true
MERGED_TH14_IMPORTED=true
MERGED_T51_IMPORTED=true
FOUR_CANONICAL_SQUAREPART_ROOTS_USED_SIMULTANEOUSLY=true
CROSS_ROOT_COPRIMALITY_GCD_XY_RS_EQ_1=true
DIFFERENCE_KERNEL_CONGRUENCE_LATTICE_EXACT=true
DIFFERENCE_KERNEL_LATTICE_MODULUS=x^2*y^2
CRITICAL_LATTICE_SUPPORT_EXPONENT=1/8+(d+kappa)/2
KAPPA_BELOW_ONE_BY_DELTA_SAVING=delta/2
Q_MINUS_P_BELOW_HALF_BY_DELTA_SAVING=delta/2
SEVEN_EIGHT_RESIDUAL_REQUIRES_Q_MINUS_P_EXPONENT=1/2-o(1)
SEVEN_EIGHT_RESIDUAL_REQUIRES_K_EXPONENT=1-o(1)
DIFFERENCE_SQUAREPART_PRODUCT=B^o(1)
K_MINUS_EXPONENT=1/2+o(1)
K_PLUS_EXPONENT=1/2+o(1)
CRITICAL_TWIST_PARAMETER_EXPONENT=7/4+o(1)
ENDPOINT_QUADRATIC_RESIDUE_SIGNATURE_EXACT=true
SELECTOR_SENSITIVE_GAUSSIAN_COMPLETION_PROVED=false
OFFDIAGONAL_TWO_AUXILIARY_RESIDUE_DISPERSION_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH14_CONSUMED=true
TH15_NEEDED=false
NEXT=Stage14-4ce
```
