# Stage14-t72 — kappa denominator tag, full signed Cayley root line, and Pell-smooth small-kappa reduction

## Purpose

Merged t71 restores the physical Gaussian product structure inside the small-`J` branch and proves that a same-squareclass pair with squarefree kernel `kappa` carries a four-cell numerator/denominator split. Stage14-t72 sharpens that split in two ways.

1. The state-local signed split is not an independent allocation: it is exactly the set of prime factors of `kappa` carried by the reduced square-scale denominator.
2. For two states with the same `kappa`, the entire odd part of `kappa` compresses by CRT to one signed linear root line for the primitive Cayley pair `(Pplus,Pminus)`.

This closes the large-`kappa` branch at the natural Cayley-pair root-line scale. The complementary small-`kappa` branch is reduced to a real-quadratic norm/Pell equation with the physical canonical-largest-prime and smooth-companion filters retained. That remaining averaged Pell-smooth energy is not proved here.

The current whole-family exponent remains the merged `5/8` bound. No additional whole-family saving is claimed by t72.

## 1. State-local signed split is the denominator `kappa` tag

Write the reduced square scale as

```text
s = kappa*(u/v)^2,
gcd(u,v)=1,
kappa squarefree.
```

Let

```text
d = gcd(kappa,v).
```

Because every prime of `d` occurs once in `kappa` and to an even positive exponent in `v^2`, reduction of `kappa*u^2/v^2` cancels exactly one copy of that prime. Hence the reduced numerator and denominator squarefree kernels are

```text
alpha = kappa/d,
beta  = d.
```

Therefore the t71 split is exact:

```text
SIGNED_SPLIT_BETA = gcd(kappa,v)
SIGNED_SPLIT_ALPHA = kappa / gcd(kappa,v).
```

In particular the `2^omega(kappa)` split choices are not extra physical variables. They are merely the denominator support tag already present in `v`.

For two same-`kappa` states put

```text
d_i = gcd(kappa,v_i),
d_j = gcd(kappa,v_j),
g   = gcd(d_i,d_j).
```

Ignoring the harmless prime `2`, the t71 agree/switch products become

```text
K_switch = d_i*d_j/g^2,
K_agree  = kappa_odd / K_switch.
```

Thus `K_switch` is exactly the squarefree symmetric difference of the two denominator `kappa`-supports, while `K_agree` is the complementary agreement support.

## 2. Full odd kappa is an exact signed cross-resultant modulus

Let

```text
N_i=Pplus_i, D_i=Pminus_i,
N_j=Pplus_j, D_j=Pminus_j,
K=oddpart(kappa).
```

Merged t69/t71 gives

```text
gcd(N_i D_i N_j D_j, K)=1.
```

Define

```text
Delta_K = N_j*D_i - N_i*D_j,
Sigma_K = N_j*D_i + N_i*D_j.
```

For an odd prime `r|K`:

- if the two states place `r` on the same signed side, both Cayley ratios are congruent to the same element of `{+1,-1}`, hence `r|Delta_K` and `r∤Sigma_K`;
- if they place `r` on opposite sides, the two ratios have opposite signs, hence `r|Sigma_K` and `r∤Delta_K`.

Consequently, exactly

```text
K_agree  = gcd(K, |Delta_K|),
K_switch = gcd(K, Sigma_K),
gcd(K_agree,K_switch)=1,
K_agree*K_switch=K.
```

This is stronger than retaining only the largest t71 four-cell.

## 3. CRT compresses all sign cells to one primitive Cayley root line

Choose `lambda mod K` by

```text
lambda == +1 mod K_agree,
lambda == -1 mod K_switch.
```

Then

```text
lambda^2 == 1 mod K
```

and the two primitive Cayley pairs satisfy

```text
N_j*D_i == lambda*N_i*D_j mod K.
```

The number of possible `lambda` is exactly `2^omega(K)`, hence `B^o(1)` on polynomial-size moduli.

For a fixed anchor `(N_i,D_i)`, fixed orientation, and a dyadic partner rectangle

```text
1<=N_j<=N0,
1<=D_j<=D0,
gcd(N_j,D_j)=1,
```

the standard primitive determinant/root-line spacing gives

```text
#partners <= (1 + N0*D0/K) * B^o(1).
```

Write

```text
Z=N0*D0.
```

Therefore the branch

```text
K >= Z*B^(-o(1))
```

is near-linear after fixed-anchor summation. This is the precise large-`kappa` statement of t72. It is parametric in the Cayley-pair area `Z`; no unsupported global lower bound for `kappa` is asserted.

## 4. Relation to the t70 common-support root line

The t70 common Cayley support `J` and the t72 squareclass modulus are arithmetically orthogonal:

```text
gcd(J,kappa)=1.
```

However they act on different primitive coordinates:

- t70: a root line for the square-scale pair `(u,v)`;
- t72: a signed root line for the Cayley pair `(Pplus,Pminus)`.

They must therefore not be multiplied into one fictitious linear modulus on a single coordinate pair. The correct object is a transverse two-chart constraint linked by

```text
Pplus/Pminus = (v^2+kappa*u^2)/(v^2-kappa*u^2)
```

after the exact common gcd reduction.

## 5. Small-kappa branch becomes a canonical-largest-prime Pell/norm equation

For one state, t71 gives the unique signed square decomposition

```text
d0 = gcd(Pplus-Pminus, Pplus+Pminus) in {1,2},
eta = 2/d0,

eta*Pplus  = alpha*r^2 + beta*t^2,
eta*Pminus = beta*t^2 - alpha*r^2,
alpha*beta = kappa,
gcd(r,t)=1.
```

Set

```text
x = beta*t,
y = r.
```

Then exactly

```text
x^2 - kappa*y^2 = beta*eta*Pminus,
x^2 + kappa*y^2 = beta*eta*Pplus.
```

This is a real-quadratic norm equation when `kappa>1` is nonsquare. For `kappa=1` it degenerates to the elementary factorization

```text
(t-r)(t+r)=eta*Pminus.
```

The physical t69 largest-prime structure must be retained. Writing

```text
c_odd = oddpart(Pminus)/ell,
```

we have

```text
ell = LPF_odd(Pplus*Pminus),
v_ell(Pminus)=1,
2*c_odd < ell,
all odd primes dividing Pplus*c_odd are < ell.
```

Moreover the angular/radial factorization is exact:

```text
oddpart(Pplus) = oddpart(delta) * R_pi,
c_odd          = oddpart(h) * R_V,
```

where

```text
R_pi = oddpart(b^2-a^2)/g_cross,
R_V  = oddpart(q^2-p^2)/g_cross,
g_cross=gcd(oddpart(b^2-a^2),oddpart(q^2-p^2)).
```

Thus the small-`kappa` receiver is not a generic Pell-point problem. It is a Pell/norm orbit with a distinguished largest split prime on the negative value, an `ell`-smooth companion positive value, the sharp physical radial hyperbola, and the fixed-`U` Gaussian/angular masks.

## 6. Why a generic Pell bound is not yet enough

For fixed nonsquare `kappa` and fixed norm RHS, a Pell equation can carry an infinite unit orbit. Hence a statement of the form "fixed quadratic form has divisor-many representations" is false without controlling unit orbits.

Conversely, dropping the physical largest-prime/smooth-value condition loses the strongest restriction available in the present family. The needed theorem must exploit that the same `ell` is

```text
- the unique largest odd prime of Pplus*Pminus,
- present to exponent one in Pminus,
- larger than twice the odd negative cofactor,
- absent from the positive companion value.
```

No class-number/regulator factor of fixed power in `kappa` may be silently absorbed into `B^o(1)` when `kappa` moves.

## 7. Minimal remaining receiver

After the large-`K` Cayley root-line branch is removed, define

```text
SharedUSmallOddKappaCanonicalLargestPrimePellSmoothPhysicalEnergy
```

for the remaining same-`kappa` energy with

```text
K=oddpart(kappa) << Z,
small t70 J,
private canonical ell,
fixed U / divisor fan,
alpha=kappa/gcd(kappa,v),
beta=gcd(kappa,v),
x^2-kappa*y^2=beta*eta*Pminus,
ell=LPF_odd(Pplus*Pminus),
2*oddpart(Pminus/ell)<ell,
oddpart(Pplus)=oddpart(delta)*R_pi,
oddpart(Pminus)/ell=oddpart(h)*R_V,
ell*delta physical hyperbola,
primitive/reconstruction masks.
```

A near-linear uniform bound for this receiver is not proved in t72.

## 8. tH19 decision

`tH19` is now needed.

Requested object:

```text
SmallOddKappaCanonicalLargestPrimePellSmoothEnergy
```

The independent audit should test, in this order:

1. uniform counting of primitive solutions to moving real-quadratic norm equations
   `x^2-kappa*y^2 = beta*eta*2^e*ell*c` with squarefree moving `kappa`;
2. primitive-divisor / Lucas-Pell / S-unit / smooth-value theorems capable of exploiting that every odd prime of the companion `Pplus*c` is `<ell`;
3. largest-prime-factor sieve with `ell` distinguished, exponent one, and `2c<ell`;
4. average estimates over `kappa`, `ell`, and the sharp `ell*delta` physical hyperbola;
5. whether class-number/regulator/unit-orbit costs remain `B^o(1)` in the actual small-`kappa` range.

Do **not**:

```text
- drop the canonical-largest-prime / smooth-companion filter;
- replace the problem by a generic fixed-RHS Pell count;
- absorb moving class-number or regulator losses without a uniform theorem;
- collapse back to a Legendre-symbol-only quadratic large sieve;
- forget the fixed-U Gaussian and angular cofactor identities.
```

The t route does not wait for tH19. Stage14-t73 should separately attack the degenerate `kappa=1` branch and the fixed denominator-tag subclasses while tH19 audits the genuine nonsquare Pell-smooth receiver.

## 9. Shared exponent

Merged s7-31 and s7-32 leave the proved whole-family exponent at

```text
5/8.
```

s7-32 sharpens the saturation geometry to the unique top corner `(theta,phi)=(5/16,1/4)` but does not lower the exponent. t72 also proves no additional whole-family power saving.

## Boundary

```text
STAGE14_T72=COMPLETE_KAPPA_DENOMINATOR_TAG_FULL_CAYLEY_ROOTLINE_AND_PELL_SMOOTH_REDUCTION
SIGNED_SPLIT_BETA_EQUALS_GCD_KAPPA_V=true
SIGNED_SPLIT_ALPHA_EQUALS_KAPPA_OVER_BETA=true
SAME_KAPPA_AGREE_SWITCH_RECOVERABLE_FROM_DENOMINATOR_TAGS=true
ODD_KAPPA_CROSS_RESULTANT_PARTITION_PROVED=true
ODD_KAPPA_CRT_COMPRESSES_TO_ONE_CAYLEY_ROOT_LINE=true
ODD_KAPPA_ROOT_LINE_MULTIPLICITY=Bo1
FIXED_ANCHOR_KAPPA_ROOTLINE_PARTNER_BOUND_PROVED=true
FIXED_ANCHOR_KAPPA_ROOTLINE_PARTNER_BOUND=(1+Z/Kodd)*Bo1
LARGE_ODD_KAPPA_CAYLEY_ROOTLINE_BRANCH_NEAR_LINEAR=true
T70_J_AND_T72_KAPPA_MODULI_COPRIME=true
T70_J_AND_T72_KAPPA_ACT_ON_DIFFERENT_COORDINATE_CHARTS=true
SMALL_KAPPA_REAL_QUADRATIC_NORM_REDUCTION_PROVED=true
KAPPA_ONE_DEGENERATES_TO_DIFFERENCE_OF_SQUARES_FACTORIZATION=true
CANONICAL_LARGEST_PRIME_PELL_SMOOTH_FILTER_PROVED=true
SHARED_U_SMALL_ODD_KAPPA_CANONICAL_LARGEST_PRIME_PELL_SMOOTH_PHYSICAL_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
T72_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH19_NEEDED=true
TH19_REQUESTED_OBJECT=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy
T_ROUTE_BLOCKED_WAITING_FOR_TH19=false
NEXT=Stage14-t73
```
