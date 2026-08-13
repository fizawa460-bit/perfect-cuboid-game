# Stage14-4ce — dual split-switch rigidity and primewise residue lock

## Status

`COMPLETE_DUAL_SPLIT_SWITCH_RIGIDITY_AND_PRIMEWISE_RESIDUE_LOCK`

Stage14-4cd localized the only remaining `7/8` mainline endpoint to

```text
P,Q,Q-P,Q+P ~ B^(1/2),
xi=ker(PQ) ~ B^(3/4),
k=ker(Q^2-P^2)=B^(1-o(1)),
x,y ~ B^(1/16),
r,s=B^o(1).
```

Merged Stage14-s7-18 then proved that any off-diagonal same-`(xi,k)` pair is cross-split in the `k=k_-k_+` allocation and, at the 4cd endpoint, has a switching product at least `B^(3/8-o(1))`.

Stage14-4ce applies the same integer-divisibility mechanism to the *other* squarefree split

```text
xi=a*b
```

and combines the two switch structures with the exact Legendre signatures from 4cd.

The result is an unconditional pair-level hard-core theorem:

1. same `xi`-split collisions are absent at the endpoint;
2. every surviving collision switches a positive-power part of both `k` and `xi`;
3. every odd prime that switches side in either split is `1 mod 4`;
4. therefore the remaining obstruction is a genuinely two-sided split-prime incidence, not a one-split support problem.

No whole-family exponent improvement is claimed in this stage. The current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

No mainline H branch is required.

---

## 1. Inputs

We use only merged results.

### 1.1 4cd endpoint

For a primitive reduced state

```text
0<P<Q<=X,
gcd(P,Q)=1,
```

write

```text
P=a*x^2,
Q=b*y^2,
xi=a*b=ker(PQ),
```

and

```text
g=gcd(Q-P,Q+P) in {1,2},
(Q-P)/g=k_-*r^2,
(Q+P)/g=k_+*s^2,
k=k_-*k_+=ker(Q^2-P^2).
```

Merged 4cd gives the endpoint

```text
X=B^(1/2+o(1)),
xi=B^(3/4+o(1)),
k=B^(1-o(1)).
```

It also proves the odd-prime signatures

```text
ell|a   => ( k/ell)=+1,
ell|b   => (-k/ell)=+1,
ell|k_- => ( xi/ell)=+1,
ell|k_+ => (-xi/ell)=+1.                 (1.1)
```

### 1.2 s7-18 k-split disagreement

For two off-diagonal states with the same `(xi,k)`, write their two `k` splits as

```text
k_{-,1}=alpha*beta,
k_{+,1}=gamma*delta,
k_{-,2}=alpha*gamma,
k_{+,2}=beta*delta,
```

with pairwise-coprime squarefree cells. Define

```text
K_agree = alpha*delta,
K_switch = beta*gamma.
```

Merged s7-18 proves

```text
(K_agree)^2 * xi <= 32 X^4                    (1.2)
```

for every off-diagonal same-`(xi,k)` pair, hence

```text
K_switch >= k*sqrt(xi)/(sqrt(32)*X^2).         (1.3)
```

At the 4cd endpoint this is

```text
K_switch >= B^(3/8-o(1)).                      (1.4)
```

---

## 2. Symmetric xi-split four-cell decomposition

Take two reduced states `s_1,s_2` with the same squarefree labels `(xi,k)`.

Their `xi` factorizations are coprime squarefree splits

```text
xi=a_1*b_1=a_2*b_2.
```

There are unique pairwise-coprime squarefree cells

```text
A,B,C,D
```

such that

```text
a_1=A*B,
b_1=C*D,
a_2=A*C,
b_2=B*D,
A*B*C*D=xi.                                      (2.1)
```

Define

```text
Xi_agree=A*D,
Xi_switch=B*C.                                    (2.2)
```

The two xi splits are identical exactly when `Xi_switch=1`.

---

## 3. Fixed xi split is injective in the endpoint range

For one fixed split `(a,b)`, two states satisfy

```text
b^2*y_1^4-a^2*x_1^4 = k*h_1^2,
b^2*y_2^4-a^2*x_2^4 = k*h_2^2.                   (3.1)
```

Cross multiplication gives

```text
b^2 (y_1^4 h_2^2-y_2^4 h_1^2)
 =a^2 (x_1^4 h_2^2-x_2^4 h_1^2).                 (3.2)
```

Since `gcd(a,b)=1`, the left bracket is divisible by `a^2` and the right bracket by `b^2`.

The elementary bounds

```text
x_i^2<=X/a,
y_i^2<=X/b,
h_i^2<(X^2)/k
```

give

```text
|y_1^4 h_2^2-y_2^4 h_1^2| <= 2 X^4/(b^2 k),
|x_1^4 h_2^2-x_2^4 h_1^2| <= 2 X^4/(a^2 k).       (3.3)
```

Therefore if

```text
xi^2*k=a^2*b^2*k > 2 X^4,                         (3.4)
```

both brackets vanish. Positivity gives

```text
x_1/y_1=x_2/y_2.
```

Because `gcd(x_i,y_i)=1`, the primitive pairs coincide, hence the reduced state coincides.

Thus

```text
FixedXiSplitInjectivity:
xi^2*k>2X^4 => a fixed xi split contains at most one state.   (3.5)
```

At the 4cd endpoint

```text
xi^2*k = B^(5/2-o(1)),
X^4     = B^(2+o(1)),
```

so the injectivity margin is `1/2` in exponent.

---

## 4. Cross-xi-split square divisibility

Using (2.1), the two same-`(xi,k)` equations are

```text
(CD)^2 y_1^4-(AB)^2 x_1^4 = k h_1^2,
(BD)^2 y_2^4-(AC)^2 x_2^4 = k h_2^2.              (4.1)
```

Cross multiplication yields

```text
D^2(
 C^2 y_1^4 h_2^2-B^2 y_2^4 h_1^2
)
=
A^2(
 B^2 x_1^4 h_2^2-C^2 x_2^4 h_1^2
).                                                  (4.2)
```

Since `gcd(A,D)=1`,

```text
A^2 | C^2 y_1^4 h_2^2-B^2 y_2^4 h_1^2,
D^2 | B^2 x_1^4 h_2^2-C^2 x_2^4 h_1^2.            (4.3)
```

The state-specific bounds give

```text
|C^2 y_1^4 h_2^2-B^2 y_2^4 h_1^2|
 <= 2 X^4/(D^2 k),

|B^2 x_1^4 h_2^2-C^2 x_2^4 h_1^2|
 <= 2 X^4/(A^2 k).                                 (4.4)
```

Hence if

```text
(A D)^2 k > 2 X^4,                                 (4.5)
```

both brackets vanish.

If `B>1`, choose a prime `ell|B`. In the first vanishing equality the right side is divisible by `ell`, while the left side is not: `ell` is coprime to `C,D,y_1,h_2` by primitive reducedness and `gcd(xi,k)=1`. Contradiction. Therefore `B=1`. The same argument forces `C=1`.

Thus (4.5) forces identical xi splits, and Section 3 then forces identical states in the endpoint range.

Consequently every off-diagonal endpoint collision satisfies

```text
boxed:
(Xi_agree)^2 * k <= 2 X^4.                         (4.6)
```

Equivalently,

```text
boxed:
Xi_switch >= xi*sqrt(k)/(sqrt(2)*X^2).              (4.7)
```

At the 4cd endpoint,

```text
boxed:
Xi_switch >= B^(1/4-o(1)).                          (4.8)
```

This is independent of the s7-18 `K_switch` bound.

---

## 5. Dual-switch endpoint

Combining (1.4) and (4.8), every off-diagonal same-`(xi,k)` pair capable of surviving at the current `7/8` endpoint has

```text
boxed:
K_switch  >= B^(3/8-o(1)),
Xi_switch >= B^(1/4-o(1)).                          (5.1)
```

Thus neither squarefree allocation may stay nearly fixed.

The residual collision is genuinely two-sided:

```text
xi allocation changes by positive power,
k  allocation changes by positive power.
```

In particular, neither a fixed-`k`-split projective theorem nor a fixed-`xi`-split theorem can by itself see the hard core.

---

## 6. Every odd switching prime is split modulo 4

Now apply the exact 4cd signatures (1.1) to both states.

### 6.1 xi-switch primes

Let an odd prime `ell|B`. Then `ell|a_1` and `ell|b_2`. Hence

```text
(k/ell)=+1,
(-k/ell)=+1.
```

Since `ell∤k`, division gives

```text
(-1/ell)=+1,
```

so

```text
ell == 1 mod 4.                                    (6.1)
```

The same argument applies to every odd `ell|C`.

Therefore

```text
boxed:
every odd prime dividing Xi_switch is 1 mod 4.      (6.2)
```

### 6.2 k-switch primes

Let an odd prime `ell|beta`. Then `ell|k_{-,1}` and `ell|k_{+,2}`. Hence

```text
(xi/ell)=+1,
(-xi/ell)=+1.
```

Since `ell∤xi`, again

```text
(-1/ell)=+1,
```

and therefore `ell==1 mod 4`. The same holds for `gamma`.

Thus

```text
boxed:
every odd prime dividing K_switch is 1 mod 4.       (6.3)
```

The prime `2` contributes only an `O(1)` parity split and is kept separate.

---

## 7. Primewise residue lock is stronger than a single Jacobi condition

The switch-prime statement retains the individual local conditions

```text
ell|Xi_switch => (k/ell)=+1,
ell|K_switch  => (xi/ell)=+1,                      (7.1)
```

as well as `ell==1 mod4`.

After fixing the finite 2-adic case, quadratic reciprocity may package these into odd-part Jacobi identities. But replacing (7.1) by one product Jacobi symbol loses information and is not used as a proof shortcut.

In particular, the following are forbidden:

- multiplying a local `1/2` density independently over switch primes without a sieve/dispersion theorem;
- replacing primewise conditions by one Jacobi sign and claiming a power saving;
- assuming the `1 mod 4` support itself is power-sparse.

The set of integers supported on primes `1 mod 4` has only logarithmic-density type sparsity, not a fixed-power exponent loss. Therefore (6.2)-(6.3) do not by themselves lower `7/8`.

---

## 8. Correct live receiver

The remaining object is now narrower than the s7-18 `LargeDisagreementCrossSplitKCollision` receiver.

Define

```text
DualSwitchPrimewiseResidueIncidence:

same xi,
same k,
off-diagonal physical pair,
Xi_switch >= B^(1/4-o(1)),
K_switch  >= B^(3/8-o(1)),
all odd switch primes == 1 mod 4,
(k/ell)=+1 for ell|Xi_switch,
(xi/ell)=+1 for ell|K_switch,
with the exact square-divisibility systems on both splits retained.
```

A fixed-power improvement requires a genuine bilinear/centered dispersion theorem on this physical pair space. Mere support counting or independent local-density multiplication is insufficient.

The preferred next order is

```text
same (xi,k) pair
-> k split four cells
-> xi split four cells
-> dual square-divisibility
-> force large K_switch and Xi_switch
-> retain primewise residue graph
-> centered bilinear switch dispersion
-> only then recombine globally.
```

---

## 9. Relation to t/tH/toolbox branches

Merged tH15 and t55 concern the different fixed-U shared-bipartite principal receiver. They are not imported as a theorem for 4ce.

Merged toolbox-ap correctly forbids cross-promoting fixed-U bipartite energy or projective-slope adapters into this mainline collision theorem.

Stage14-4ce therefore remains self-contained on the mainline arithmetic geometry.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_WAITING_FOR_TH15=false
```

No new mainline H stage is requested.

---

## 10. Exponent ledger

At the 4cd endpoint

```text
xi exponent     = 3/4,
k exponent      = 1,
X exponent      = 1/2.
```

The two switch lower bounds are

```text
log_B Xi_switch
 >= 3/4 + 1/2 - 1
 = 1/4,

log_B K_switch
 >= 1 + 3/8 - 1
 = 3/8.                                             (10.1)
```

The current whole-family exponent remains

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8.
```

No fixed-power saving is declared because the primewise residue graph has not yet been given a centered bilinear estimate.

---

## 11. Stage boundary

```text
STAGE14_4CE=COMPLETE_DUAL_SPLIT_SWITCH_RIGIDITY_AND_PRIMEWISE_RESIDUE_LOCK
MERGED_4CD_IMPORTED=true
MERGED_S7_18_IMPORTED=true
FIXED_XI_SPLIT_INJECTIVITY_IF_xi2_k_GT_2_X4=true
CROSS_XI_SPLIT_AGREEMENT_NECESSARY_BOUND=(Xi_agree)^2*k<=2*X^4
FOUR_CD_ENDPOINT_XI_SWITCH_LOWER_EXPONENT=1/4
FOUR_CD_ENDPOINT_K_SWITCH_LOWER_EXPONENT=3/8
DUAL_SWITCH_POSITIVE_POWER_REQUIRED=true
ODD_XI_SWITCH_PRIMES_ARE_1_MOD_4=true
ODD_K_SWITCH_PRIMES_ARE_1_MOD_4=true
PRIMEWISE_RESIDUE_LOCK_EXACT=true
PRIMEWISE_LOCAL_DENSITIES_MAY_BE_MULTIPLIED_WITHOUT_DISPERSION=false
SPLIT_PRIME_SUPPORT_ALONE_GIVES_FIXED_POWER_SAVING=false
DUAL_SWITCH_PRIMEWISE_RESIDUE_INCIDENCE_REQUIRED=true
DUAL_SWITCH_PRIMEWISE_RESIDUE_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_WAITING_FOR_TH15=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cf
```
