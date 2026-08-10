# Stage14-s7-16 — split-k inert Fourier self-duality and the centered-completion barrier

## Status

`COMPLETE_SPLIT_K_INERT_FOURIER_SELF_DUALITY_AND_ABSOLUTE_COMPLETION_BARRIER`

Stage14-s7-15 isolated the exact off-diagonal collision object

```text
C_off = sum_(xi,k) r_B(xi,k)(r_B(xi,k)-1)
```

and gave an exact centered prime-amplifier receiver.  The previous draft plan was to wait for a separate support line.  Stage14-s7-16 does **not** do that.  The s-route keeps moving and attacks the centered collision problem directly.

The main new fact is an exact finite-field transform identity for the split-`k` quartic arising in s7-15.  It is stronger than a generic Weil bound: over every inert prime `p=3 mod 4`, the two-dimensional additive Fourier transform reproduces the same quartic character with coefficient exactly `p`.

This gives a completely explicit local completion theory.  It also proves that applying this completion separately for each auxiliary modulus and then taking absolute values cannot improve the current `7/8` whole-family bound.  The remaining theorem is therefore a genuinely **centered, jointly averaged dual-frequency dispersion**, not another local character-sum estimate.

No sH/supervisor branch is introduced.  Merged tH14/t51 are reference material only; s7-16 does not wait for them and does not import their unproved `SSGC` as a theorem.

---

## 1. Merged inputs and the critical shell

Merged s7-15 writes, after parity normalization,

```text
g = gcd(Q-P,Q+P) in {1,2},
A0=(Q-P)/g,
B0=(Q+P)/g,
A0=k_- r^2,
B0=k_+ s^2,
```

with

```text
k = k_- k_+,
gcd(k_-,k_+)=1.
```

The shared squarefree label `xi=ker(PQ)` is detected by the split-`k` quartic

```text
k_+^2 s^4 - k_-^2 r^4 = epsilon_g * xi * z^2.      (1.1)
```

Thus for fixed `k` and a fixed ordered factorization `(k_-,k_+)`, recurrence of the same `xi` is exactly recurrence of the squareclass of

```text
F_(A,B)(r,s)=A s^4-B r^4,
A=k_+^2,
B=k_-^2.                                           (1.2)
```

Merged 4cc independently localizes the only `7/8`-critical residual to

```text
xi = B^(3/4+o(1)),
k  >= B^(3/4-o(1)).                                (1.3)
```

For `k~B^kappa`, the difference-of-squares parameter has source mass per fixed `k`, up to divisor/split factors,

```text
H_k <= B^((1-kappa)/2+o(1)).                       (1.4)
```

At the endpoint `kappa=3/4`, this is `B^(1/8+o(1))`.

---

## 2. One-variable inert quartic identity

Let `p` be an odd prime with

```text
p = 3 mod 4,
```

and let `chi` be the quadratic character of `F_p`, extended by `chi(0)=0`.

For every nonzero `c in F_p`,

```text
boxed:
sum_(t mod p) chi(t^4-c) = -1.                    (2.1)
```

Proof.  The number of `t` with `t^2=u` is `1+chi(u)`, including `u=0`.  Therefore

```text
sum_t chi(t^4-c)
 = sum_u (1+chi(u)) chi(u^2-c)
 = sum_u chi(u^2-c) + sum_u chi(u(u^2-c)).         (2.2)
```

The first sum is the standard quadratic sum `-1` because `c!=0`.  In the second sum, the terms at `u` and `-u` cancel because

```text
chi(-1)=-1
```

for `p=3 mod 4`, while `u^2-c` is unchanged.  The `u=0` term is zero.  Hence the second sum vanishes and (2.1) follows.

This elementary identity is the source of the exact two-dimensional transform below.

---

## 3. Exact two-dimensional Fourier self-duality

Fix `A,B in F_p^*` and define

```text
K_(A,B)(r,s)=chi(A s^4-B r^4).                     (3.1)
```

For additive frequencies `(h,j) in F_p^2`, put

```text
T_p(h,j)
 = sum_(r,s mod p) K_(A,B)(r,s) e_p(h r+j s),      (3.2)
```

where `e_p(x)=exp(2 pi i x/p)`.

Then for **every** `(h,j)`, including `(0,0)`,

```text
boxed:
T_p(h,j)=p * chi(A h^4-B j^4).                     (3.3)
```

### 3.1 Case `j!=0`

For `r!=0`, write `s=t r`.  Then

```text
K_(A,B)(r,tr)=chi(A t^4-B)
```

because `r^4` is a nonzero square.  Hence

```text
sum_(r!=0) e_p(r(h+j t))
 = p-1  if h+j t=0,
 = -1   otherwise.                                (3.4)
```

Let `t0=-h/j`.  Using (2.1),

```text
sum_t chi(A t^4-B)=-chi(A),                        (3.5)
```

so the `r!=0` contribution is

```text
p chi(A t0^4-B)+chi(A).                            (3.6)
```

The `r=0` contribution is

```text
chi(A) sum_(s!=0) e_p(j s)=-chi(A).                (3.7)
```

They cancel except for the first term, giving

```text
T_p(h,j)=p chi(A t0^4-B)
        =p chi(A h^4-B j^4),                       (3.8)
```

because `j^4` is a square.

### 3.2 Case `j=0`, `h!=0`

Now the `r!=0` additive sum is always `-1`, so (3.5) contributes `chi(A)`.  The `r=0` line contributes `(p-1)chi(A)`.  Therefore

```text
T_p(h,0)=p chi(A)=p chi(A h^4),                    (3.9)
```

which is again (3.3).

### 3.3 Zero frequency

The complete sum is

```text
T_p(0,0)=0,                                        (3.10)
```

and the right-hand side of (3.3) is also zero.

Thus the split-`k` character kernel is an exact Fourier eigenfamily: the same binomial quartic reappears on the dual side.

---

## 4. Squarefree inert composite moduli

Let

```text
m=prod p,
```

be odd squarefree with every `p|m` satisfying `p=3 mod 4`, and assume `gcd(AB,m)=1`.  Write `chi_m` for the Jacobi symbol.

Chinese remaindering factorizes the transform.  The CRT scaling multiplies both additive frequencies by the same local unit; its fourth power is a square and therefore disappears under the quadratic character.  Consequently

```text
boxed:
T_m(h,j)=m * chi_m(A h^4-B j^4).                   (4.1)
```

In particular,

```text
|T_m(h,j)| <= m                                    (4.2)
```

with no exceptional additive frequency and no hidden Weil constant.

This is stronger than the generic mixed-Fourier `O(m)` input one would normally seek: here both the magnitude and the dual phase are explicit.

---

## 5. Individual incomplete completion

For intervals `I,J` modulo `m`, ordinary Fourier inversion and (4.2) give

```text
sum_(r in I, s in J) chi_m(A s^4-B r^4)
 << m log^2(2m).                                   (5.1)
```

More generally, dyadic rectangle decompositions and the usual divisor/Mobius refinements preserve

```text
boxed:
S_m(block) << min(H_block,m) * B^o(1),             (5.2)
```

for the elementary split-`k` box/hyperbola selectors to which individual absolute completion applies.

Equation (5.2) is deliberately an **individual-modulus** statement.  It does not claim arbitrary sparse physical-selector cancellation; merged t50/tH14 already show why such a jump would be invalid.

---

## 6. Why individual completion cannot beat the centered collision bound

Let a fixed split-`k` source block contain `H` states and let an auxiliary inert-prime family contain

```text
M = L^(1+o(1))
```

primes of size `p~L`.  Ignore only `B^o(1)` bad-prime losses.

For a same-squareclass off-diagonal pair, the quadratic-character amplifier has size `M+O(B^o(1))`, so the exact centered receiver from s7-15 has the schematic lower bound

```text
C_off * M^2 <= R_cent.                              (6.1)
```

If one now destroys the centering by taking absolute values modulus-by-modulus, then

```text
R_cent
 <= sum_(p,q) |S_pq|^2.                             (6.2)
```

The diagonal auxiliary pairs `p=q` contribute at most

```text
M H^2.                                             (6.3)
```

For `p!=q`, the modulus has size `pq~L^2`, so (5.2) gives

```text
|S_pq| << min(H,L^2) B^o(1).                       (6.4)
```

There are `M^2` such pairs.  Dividing (6.2) by `M^2`, one obtains only

```text
boxed:
C_off
 << H^2/L + min(H,L^2)^2
    all times B^o(1).                              (6.5)
```

This never improves the already-known pointwise/genus-one bound `C_off<<H B^o(1)`:

- if `L<=H^(1/2)`, the first term satisfies

  ```text
  H^2/L >= H^(3/2);
  ```

- if `L>=H^(1/2)`, the second term is

  ```text
  H^2.
  ```

Thus even the exact self-dual local transform cannot help once the centered variance is replaced by separate absolute values.

This is a genuine architecture barrier, not a failure of the local character sum.

---

## 7. The missing cancellation is precisely the centered variance

For a state `z` write

```text
c_z(p)=chi_p(F(z))
```

on good primes.  For a pair of auxiliary primes define

```text
S_pq=sum_z c_z(p)c_z(q),
D_pq=sum_z c_z(p)^2 c_z(q)^2.                      (7.1)
```

Then the exact s7-15 identity is

```text
boxed:
R_cent
 = sum_(p,q) ( |S_pq|^2-D_pq ).                   (7.2)
```

The subtraction `D_pq` is not cosmetic.  On a random-sign model,

```text
|S_pq|^2 ~ H,
D_pq      ~ H,
```

and the desired `H^2 M` centered scale appears only **after** this baseline is cancelled before absolute values are taken.

The exact Fourier self-duality (3.3) therefore changes the next problem into a dual-frequency covariance problem.  It does not license the estimate

```text
sum |S_pq|^2 << H^2 M
```

by individual completion.

The next theorem must retain the signed/centered sum in (7.2) while averaging the dual quartic phases

```text
chi_p(A h^4-B j^4)
```

across distinct inert auxiliary primes.

---

## 8. Quantitative target and relation to the `6/7` conditional ledger

Merged s7-15 showed that on the critical `xi` shell

```text
max H_xi <= B^(1/8+o(1)),
sum H_xi <= B^(7/8+o(1)),
sum H_xi^2 <= B^(1+o(1)).                          (8.1)
```

Its sufficient centered theorem was

```text
R_cent(xi) << H_xi^2 M B^o(1).                    (8.2)
```

With `M=B^(1/7+o(1))`, (8.2) would imply

```text
V(B) << B^(6/7+o(1)).                              (8.3)
```

Stage14-s7-16 does **not** prove (8.2), so `6/7` remains conditional.

What s7-16 proves is that the local split-`k` transform needed for a direct attack is already exact.  Therefore the unresolved fixed-power content of (8.2) is entirely in the jointly averaged centered selector/dual-frequency dispersion.

---

## 9. Relation to merged tH14 and t51

Merged tH14 proves useful residue-collision bookkeeping and defines `SelectorSensitiveGaussianCompletion`, but explicitly leaves that completion theorem unproved.

Merged t51 closes its exact/residue diagonal in an alias-free range and leaves an off-diagonal residue dispersion.

Stage14-s7-16 uses neither unproved claim.  The overlap is conceptual only:

- t-route object: Gaussian physical-selector two-auxiliary dispersion;
- s-route object: split-`k` quartic centered collision dispersion;
- s7-16 supplies an exact Fourier formula specific to the s-route quartic, so the s-route continues independently.

No sH line is created and no s-stage waits for a supervisor result.

---

## 10. Next receiver

The next s-stage should work directly with the dual form supplied by (3.3):

```text
DualSplitKCenteredDispersion.
```

A sufficient target is a jointly averaged estimate of the shape

```text
sum_(p,q in Pcal)
  ( |S_pq|^2-D_pq )
 << H^2 M B^o(1),                                  (10.1)
```

uniformly over the critical split-`k` common-refinement blocks, with no blockwise absolute recombination.

The exact self-duality means that after Poisson completion the dual arithmetic is again the same quartic family.  Stage14-s7-17 should exploit this reciprocity rather than repeat another local completion.

---

## 11. Stage boundary

```text
STAGE14_S7_16=COMPLETE_SPLIT_K_INERT_FOURIER_SELF_DUALITY_AND_ABSOLUTE_COMPLETION_BARRIER
MERGED_S7_15_IMPORTED=true
MERGED_4CC_K_SHELL_LOCALIZATION_IMPORTED=true
MERGED_TH14_REFERENCE_ONLY=true
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
