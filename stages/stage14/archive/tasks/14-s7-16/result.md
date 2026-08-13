# Stage14-s7-16 — split-k inert Fourier self-duality and centered-completion barrier

## Status

`COMPLETE_SPLIT_K_INERT_FOURIER_SELF_DUALITY_AND_ABSOLUTE_COMPLETION_BARRIER`

Stage14-s7-15 isolated the off-diagonal collision energy

```text
C_off = sum_(xi,k) r_B(xi,k)(r_B(xi,k)-1).
```

Stage14-s7-16 does not wait for a separate support/supervisor line.  It attacks the s-route split-`k` quartic directly and proves an exact inert-prime Fourier transform.  The result is stronger than a generic Weil estimate and identifies precisely why individual-modulus completion still cannot break the current `7/8` bound.

Merged tH14 R2 is reference material only.  Its latest boundary reduces the t-route to `PhysicalWeightedSquareclassFiberEnergy`; s7-16 does not import that unproved statement and is not blocked by it.

---

## 1. Split-k quartic

Merged s7-15 gives, after parity normalization,

```text
g=gcd(Q-P,Q+P) in {1,2},
(Q-P)/g = k_- r^2,
(Q+P)/g = k_+ s^2,
k=k_- k_+,
gcd(k_-,k_+)=1.
```

The shared label `xi=ker(PQ)` satisfies

```text
k_+^2 s^4-k_-^2 r^4 = epsilon_g * xi * z^2.
```

Hence for fixed `k` and fixed split `(k_-,k_+)`, recurrence of the same `xi` is recurrence of the squareclass of

```text
F_(A,B)(r,s)=A s^4-B r^4,
A=k_+^2,
B=k_-^2.
```

Merged 4cc localizes the only `7/8`-critical residual to

```text
xi=B^(3/4+o(1)),
k>=B^(3/4-o(1)).
```

For `k~B^kappa`, the fixed-`k` source mass is at most

```text
H_k <= B^((1-kappa)/2+o(1)).
```

At `kappa=3/4`, `H_k<=B^(1/8+o(1))`.

---

## 2. Exact inert quartic trace

Let `p=3 mod 4` and let `chi` be the quadratic character on `F_p`, extended by `chi(0)=0`.  For every `c!=0`,

```text
sum_(t mod p) chi(t^4-c) = -1.
```

Indeed, writing `u=t^2`, the number of preimages is `1+chi(u)`, so

```text
sum_t chi(t^4-c)
 = sum_u chi(u^2-c) + sum_u chi(u(u^2-c)).
```

The first sum is `-1`; the second cancels under `u -> -u` because `chi(-1)=-1`.

---

## 3. Exact 2D Fourier self-duality

For `A,B in F_p^*`, define

```text
K_(A,B)(r,s)=chi(A s^4-B r^4)
```

and

```text
T_p(h,j)=sum_(r,s mod p) K_(A,B)(r,s)e_p(hr+js).
```

Then for every additive frequency `(h,j)`, including `(0,0)`,

```text
boxed:
T_p(h,j)=p*chi(A h^4-B j^4).
```

For `j!=0`, write `s=tr` on `r!=0`.  The inner `r`-sum is `p-1` at the unique `t=-h/j` and `-1` elsewhere.  The exact quartic trace above cancels the residual term with the `r=0` line, leaving exactly

```text
p*chi(A(-h/j)^4-B)=p*chi(Ah^4-Bj^4).
```

For `j=0,h!=0`, the same decomposition gives `p chi(A)=p chi(Ah^4)`.  At `(0,0)` both sides vanish.

Thus the s-route split-`k` quartic is an exact Fourier eigenfamily over every inert prime.

---

## 4. Squarefree inert composite moduli

If `m` is odd squarefree, every `p|m` satisfies `p=3 mod 4`, and `gcd(AB,m)=1`, CRT gives

```text
T_m(h,j)=m*chi_m(Ah^4-Bj^4),
```

because the CRT frequency scaling enters through fourth powers and is invisible to the quadratic character.  Hence

```text
|T_m(h,j)|<=m
```

for all frequencies with no exceptional set and no hidden Weil constant.

For interval boxes this gives the standard individual completion bound

```text
S_m(I,J) << m log^2(2m).
```

On elementary dyadic split-`k` box/hyperbola refinements one may record schematically

```text
S_m(block) << min(H_block,m) B^o(1).
```

This is an individual-modulus estimate only; it does not assert arbitrary physical-selector cancellation.

---

## 5. Exact absolute-completion barrier

Let a fixed split-`k` block contain `H` states and let the inert-prime amplifier contain

```text
M=L^(1+o(1))
```

primes of size `p~L`.

The s7-15 centered receiver has

```text
C_off * M^2 <= R_cent
```

up to `B^o(1)` bad-prime losses.

If the centered subtraction is discarded and each modulus is bounded in absolute value, then

```text
R_cent <= sum_(p,q)|S_pq|^2.
```

The `p=q` terms contribute at most `M H^2`.  For `p!=q`, the modulus has size `pq~L^2`, so the exact local completion gives at best

```text
|S_pq| << min(H,L^2) B^o(1).
```

Therefore

```text
boxed:
C_off << H^2/L + min(H,L^2)^2
```

up to `B^o(1)`.

This cannot improve the already known `C_off<<H B^o(1)`:

- if `L<=H^(1/2)`, then `H^2/L>=H^(3/2)`;
- if `L>=H^(1/2)`, then `min(H,L^2)^2=H^2`.

So the obstruction is not local cancellation.  It is the loss of the centered variance when one takes modulus-by-modulus absolute values.

---

## 6. Centered variance is the live object

For good primes set

```text
c_z(p)=chi_p(F(z)),
S_pq=sum_z c_z(p)c_z(q),
D_pq=sum_z c_z(p)^2c_z(q)^2.
```

The exact s7-15 identity is

```text
R_cent = sum_(p,q)(|S_pq|^2-D_pq).
```

The subtraction is essential: on the random scale both `|S_pq|^2` and `D_pq` are size `H`.  The desired centered scale appears only after this baseline cancels before absolute values are applied.

Because the finite-field transform is exactly self-dual, the next s-route problem is now a dual-frequency covariance problem for the same quartic phase

```text
chi_p(Ah^4-Bj^4).
```

No additional local Weil theorem is missing.

---

## 7. Relation to merged tH14 R2 / t51

Merged tH14 R2 proves a quadratic-large-sieve adapter but leaves

```text
PhysicalWeightedSquareclassFiberEnergy
```

unproved.  Merged t51 closes a residue diagonal but leaves its off-diagonal selector dispersion.

These results are compatible with s7-16, but they are not prerequisites.  The s-route has its own exact split-`k` Fourier identity and continues independently.

No sH line is created.

---

## 8. Quantitative target

Merged s7-15 showed that a centered natural-scale theorem

```text
R_cent(xi) << H_xi^2 M B^o(1)
```

with `M=B^(1/7+o(1))` would imply

```text
V(B) << B^(6/7+o(1)).
```

Stage14-s7-16 does not prove this global centered theorem, so `6/7` remains conditional and the current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

The new conclusion is sharper: all remaining fixed-power content lies in the jointly averaged centered dual-frequency dispersion, not in the local split-`k` transform.

---

## 9. Next receiver

Stage14-s7-17 should attack

```text
DualSplitKCenteredDispersion
```

directly, keeping

```text
sum_(p,q)(|S_pq|^2-D_pq)
```

centered throughout the auxiliary-prime and dual-frequency average.  Blockwise absolute recombination is forbidden because s7-16 proves it cannot improve the current collision bound.

---

## 10. Stage boundary

```text
STAGE14_S7_16=COMPLETE_SPLIT_K_INERT_FOURIER_SELF_DUALITY_AND_ABSOLUTE_COMPLETION_BARRIER
MERGED_S7_15_IMPORTED=true
MERGED_4CC_K_SHELL_LOCALIZATION_IMPORTED=true
MERGED_TH14_R2_REFERENCE_ONLY=true
MERGED_T51_REFERENCE_ONLY=true
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14=false
SPLIT_K_QUARTIC=F_A_B(r,s)=A*s^4-B*r^4
INERT_ONE_VARIABLE_QUARTIC_TRACE=-1
INERT_TWO_DIMENSIONAL_FOURIER_SELF_DUALITY_EXACT=true
INERT_FOURIER_FORMULA=T_p(h,j)=p*chi_p(A*h^4-B*j^4)
INERT_SQUAREFREE_COMPOSITE_FOURIER_SELF_DUALITY_EXACT=true
INDIVIDUAL_MODULUS_COMPLETION_BOUND=m*B^o(1)
ABSOLUTE_PER_MODULUS_COMPLETION_BEATS_POINTWISE_COLLISION=false
CENTERED_DIAGONAL_SUBTRACTION_ESSENTIAL=true
DUAL_FREQUENCY_CENTERED_DISPERSION_REQUIRED=true
DUAL_FREQUENCY_CENTERED_DISPERSION_PROVED=false
CONDITIONAL_PHYSICAL_UPPER_BOUND_EXPONENT=6/7
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-17
```
