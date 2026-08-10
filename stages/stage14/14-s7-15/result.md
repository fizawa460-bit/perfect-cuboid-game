# Stage14-s7-15 — centered k-collision amplifier and the post-diagonal mean-square receiver

## Purpose

Merged Stage14-s7-14 reduces the current `7/8` obstruction to the critical shared-label shell

```text
xi = ker(PQ) = ab ~ B^(3/4)
```

and the transverse label

```text
k = ker(Q^2-P^2),
gcd(k,xi)=1.
```

For fixed `xi`, let `r_xi(k)` be the number of reduced-coordinate states in the critical common refinement carrying label `k`.  The physical two-point condition uses two distinct states with the same `(xi,k)`, so the relevant quantity is the factorial/off-diagonal collision energy

```text
C_off(xi) = sum_k r_xi(k)(r_xi(k)-1).
```

This stage has two goals.

1. refine `k` exactly through the coprime factors `Q-P` and `Q+P`;
2. derive an amplifier identity which sees `C_off` after removing the unavoidable state diagonal exactly.

The main conclusion is a new receiver, not a new unconditional exponent.  The raw Frobenius theorem requested by merged Stage14-t50 has natural size `H*P^2`, where `H` is the number of states and `P` is the number of auxiliary primes.  That scale includes the state diagonal and therefore does not by itself improve the s7 `7/8` exponent.  For s7 one needs a **centered selector-sensitive two-modulus second moment** after subtracting the diagonal exactly.

A natural-scale centered theorem would immediately give a power saving; in particular amplifier size `P=B^(1/7+o(1))` would turn the critical `7/8` shell into `6/7`.

No such centered theorem is claimed in this stage.

---

## 1. Merged inputs

We use only merged inputs.

- Stage14-s7-14: current whole-family exponent `7/8`, critical `xi~B^(3/4)`, and the exact `(xi,k)` collision receiver.
- Stage14-s7-10 / 4by: adjacent two-cell theorem used in the previous shell reduction.
- Stage14-t50: auxiliary bad-prime aggregate is harmless at polynomial amplifier scales, while the good part requires a selector-sensitive two-modulus second moment and triggers Stage14-tH14.

The current theorem ledger remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 2. Exact parity-normalized factorization of k

Let `0<P<Q` and `gcd(P,Q)=1`.  Put

```text
A0 = Q-P,
B0 = Q+P,
g  = gcd(A0,B0).
```

Since

```text
gcd(Q-P,Q+P) | 2 gcd(P,Q),
```

we have

```text
g in {1,2}.
```

Define

```text
A=A0/g,
B=B0/g.
```

Then

```text
gcd(A,B)=1.
```

Let

```text
k_minus = ker(A),
k_plus  = ker(B).
```

Because `A` and `B` are coprime,

```text
boxed:
gcd(k_minus,k_plus)=1,
k = k_minus*k_plus.                                (2.1)
```

There are integers `r,s>=1` with

```text
A = k_minus*r^2,
B = k_plus*s^2.                                    (2.2)
```

Thus every `k`-label has an exact parity-normalized split into the squarefree kernels of the two difference factors.

For fixed squarefree `k`, the number of ordered coprime splittings

```text
k=k_minus*k_plus
```

is `2^omega(k)=B^o(1)` in the Stage14 polynomial range.  Therefore refining a collision by the two `k`-splits costs no power of `B`.

---

## 3. The split-k quartic

The product-square relation is

```text
PQ = xi*h^2.                                       (3.1)
```

Using `A0=gA`, `B0=gB`, we have

```text
Q = g(A+B)/2,
P = g(B-A)/2.
```

Hence

```text
PQ = g^2(B^2-A^2)/4.
```

Substituting (2.2),

```text
k_plus^2*s^4 - k_minus^2*r^4
 = epsilon_g * xi*h^2,                             (3.2)
```

where

```text
epsilon_g = 4  if g=1,
epsilon_g = 1  if g=2.
```

Thus, after the `B^o(1)` refinement by `(g,k_minus,k_plus)`, the fixed `(xi,k)` coordinate problem lies on the explicit genus-one quartic

```text
boxed:
k_plus^2*s^4-k_minus^2*r^4 = epsilon_g*xi*h^2.    (3.3)
```

This is the factorized version of the s7-05 quartic/Jacobian receiver.  It does not by itself give a fixed power saving: bounded-height point multiplicity remains only `B^o(1)`.

---

## 4. Off-diagonal collision energy is the correct target

Fix a critical `xi` shell and a dyadic common-refinement block.  Let `S_xi` be its coordinate-state set and write

```text
H_xi = #S_xi.
```

Each state `s` carries a squarefree `k_s`.  Set

```text
r_xi(k)=#{s in S_xi : k_s=k}.
```

Then

```text
A1_xi = sum_k r_xi(k)^2
      = H_xi + C_off(xi),                          (4.1)
```

where

```text
boxed:
C_off(xi)=sum_k r_xi(k)(r_xi(k)-1).                (4.2)
```

The diagonal term `H_xi` is unavoidable and is not physical two-point recurrence.  Hence a theorem of the form

```text
A1_xi << H_xi*B^o(1)
```

is not enough to beat the global `7/8` exponent: after subtracting `H_xi`, the remaining collision can still be of order `H_xi`.

This is the key difference between the s7 receiver and the raw principal-energy target in t49/t50.

---

## 5. Auxiliary-prime character matrix

Choose a family `Pcal` of odd split auxiliary primes `p=1 mod 4` in a polynomial range.  The split condition is not needed for the abstract quadratic-character identity, but it aligns the receiver with the merged t50/tH Gaussian interface.

For state `s`, let `Bad(s)` contain all auxiliary primes excluded by the physical selector, coefficient denominators, or `p|k_s`.  Merged t50 proves that for a polynomial-size state datum and a fixed polynomial prime scale,

```text
#Bad(s)=B^o(1),
```

and its aggregate contribution is separately chargeable.

Define

```text
c_s(p) = 0                  if p in Bad(s),
       = (k_s/p)            otherwise.             (5.1)
```

For `p,q in Pcal`, set

```text
G_xi(p,q)=sum_{s in S_xi} c_s(p)c_s(q),            (5.2)
D_xi(p,q)=sum_{s in S_xi} c_s(p)^2 c_s(q)^2.       (5.3)
```

`D_xi(p,q)` is exactly the number of states good at both auxiliary primes.

For an ordered state pair `(s,t)`, define its amplifier correlation

```text
A_st = sum_{p in Pcal} c_s(p)c_t(p).                (5.4)
```

If `s!=t` but `k_s=k_t`, every prime good for both states contributes `1`.  If

```text
b=max_s #Bad(s),
P=#Pcal,
```

then

```text
boxed:
|A_st| >= P-2b
for every off-diagonal same-k pair.                (5.5)
```

---

## 6. Exact centered Frobenius identity

Expand the nonnegative pair sum

```text
R_cent(xi)
 = sum_{s!=t} |A_st|^2.                             (6.1)
```

Changing the order of summation gives the exact identity

```text
boxed:
R_cent(xi)
 = sum_{p,q in Pcal}
   ( G_xi(p,q)^2 - D_xi(p,q) ).                    (6.2)
```

Although an individual summand on the right may have either sign, the full sum is nonnegative because of (6.1).

Combining (5.5) and (6.1),

```text
boxed:
C_off(xi)*(P-2b)^2 <= R_cent(xi).                  (6.3)
```

This is the exact amplifier receiver needed by s7.

The distinction from the raw Frobenius norm is explicit:

```text
sum_{p,q} G_xi(p,q)^2
 = sum_{p,q} D_xi(p,q) + R_cent(xi).               (6.4)
```

The first term is the state diagonal.  It is of natural size `H_xi*P^2`; retaining it makes a raw `O(H_xi P^2)` theorem exponent-neutral for `C_off`.

---

## 7. Diagonal-prime contribution and natural centered scale

The terms `p=q` in (6.2) are explicit.  Put

```text
H_xi(p)=#{s in S_xi : p notin Bad(s)}.
```

Then

```text
G_xi(p,p)=H_xi(p),
D_xi(p,p)=H_xi(p),
```

so

```text
sum_p (G_xi(p,p)^2-D_xi(p,p))
 <= P*H_xi^2.                                      (7.1)
```

Therefore a natural random-scale theorem for the off-diagonal auxiliary modes would be

```text
sum_{p!=q}
( G_xi(p,q)^2-D_xi(p,q) )
 << H_xi^2*P*B^o(1),                               (7.2)
```

or, more safely, the corresponding upper bound for the whole centered quantity

```text
boxed:
R_cent(xi) << H_xi^2*P*B^o(1).                    (7.3)
```

With `b=o(P)`, (6.3) would imply

```text
boxed:
C_off(xi) << H_xi^2/P * B^o(1).                   (7.4)
```

This is precisely the occupancy/near-injectivity gain missing from s7-14.

Stage14-s7-15 does **not** prove (7.3).

---

## 8. Critical-shell exponent contract

Merged s7-14 gives, on the exponent-critical shell,

```text
#xi labels <= B^(3/4+o(1)),
H_xi <= B^(1/8+o(1)),
sum_xi H_xi <= B^(7/8+o(1)).                       (8.1)
```

Consequently

```text
sum_xi H_xi^2
 <= (max_xi H_xi) * sum_xi H_xi
 <= B^(1+o(1)).                                    (8.2)
```

If the centered theorem (7.3) holds uniformly and

```text
P=B^(rho+o(1)),
rho>1/8,
```

then summing (7.4) over `xi` yields

```text
sum_xi C_off(xi)
 << B^(1-rho+o(1)).                                (8.3)
```

Thus any `rho>1/8` beats the current `7/8` ceiling.

A concrete target is

```text
rho=1/7.
```

Then

```text
1-rho = 6/7,
```

so the centered theorem at a `B^(1/7)` auxiliary-prime family would give

```text
boxed conditional:
V(B) << B^(6/7+o(1)).                               (8.4)
```

The improvement would be

```text
7/8 - 6/7 = 1/56.                                  (8.5)
```

This `6/7` statement is conditional and is not promoted to the current theorem ledger.

---

## 9. Relation to t50 and the tH14 request

Merged t50 proves that bad auxiliary-prime incidences are not the obstruction and identifies a selector-sensitive two-modulus Gaussian second moment as the live good-prime problem.  It also sets

```text
TH14_NEEDED=true.
```

The s7 specialization is sharper in one respect: because the target is `C_off=A1-H`, the tH14 adapter must preserve the exact state diagonal and control the **centered** quantity (6.2), not merely the raw Frobenius norm.

Accordingly the s7-side tH14 request is:

```text
CenteredXiKCollisionSecondMoment:
for critical xi-shell common-refinement blocks,
retain the physical/canonical selector, divisor-coupled hyperbola,
and two distinct split auxiliary primes,
and prove
R_cent(xi) << H_xi^2*P*B^o(1)
(or any bound yielding a fixed power saving after division by P^2).
```

As in t49/t50, state pairs must not be collapsed to product kernels before the physical signed aggregation: that move can reintroduce the unresolved pair-energy circularity.

---

## 10. Current boundary

No new unconditional whole-family saving is claimed.

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8.
```

The new information is that the exact missing object is no longer generic `(xi,k)` multiplicity and no longer the raw t50 Frobenius norm.  It is the diagonal-subtracted, selector-sensitive centered two-modulus mean square.

If tH14 supplies the natural centered scale at amplifier exponent `1/7`, the next s7 stage can immediately promote `6/7`.

---

## Boundary

```text
STAGE14_S7_15=COMPLETE_CENTERED_XI_K_COLLISION_AMPLIFIER_AND_TH14_CONTRACT
MERGED_S7_14_IMPORTED=true
MERGED_T50_BAD_AUXILIARY_CLOSURE_IMPORTED=true
K_DIFFERENCE_FACTOR_GCD_IN_1_2=true
K_PARITY_NORMALIZED_SPLIT_EXACT=true
K_SPLIT_COUNT_PER_K=B^o(1)
SPLIT_K_QUARTIC_EXACT=true
OFF_DIAGONAL_COLLISION_ENERGY=C_off=sum_k_r_k_(r_k-1)
RAW_A1_NEAR_LINEAR_ALONE_BEATS_7_8=false
CENTERED_FROBENIUS_IDENTITY_EXACT=true
SAME_K_OFF_DIAGONAL_PAIR_AMPLIFIER_LOWER_BOUND=(P-2b)^2
CENTERED_COLLISION_RECEIVER_EXACT=true
CENTERED_NATURAL_SCALE_THEOREM_PROVED=false
CONDITIONAL_AUXILIARY_PRIME_EXPONENT=1/7
CONDITIONAL_PHYSICAL_UPPER_BOUND_EXPONENT=6/7
CONDITIONAL_IMPROVEMENT_OVER_7_8=1/56
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
TH14_NEEDED=true
TH14_S7_REQUEST=CenteredXiKCollisionSecondMoment
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-16
```
