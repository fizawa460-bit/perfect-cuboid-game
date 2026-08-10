# Stage14-t69 — exact noncanonical Cayley cofactors and common-support orientation modulus

## Purpose

Merged Stage14-t68 removes the misleading shortcut in which the private canonical prime `ell_i` of one state is expected to become a cross-state determinant modulus.  After same-`M`, same-`ell`, nested-canonical and cross-factor-contaminated pairs are charged, the live dominant invisible pair is **mutually Cayley-private**.

Stage14-t69 asks what arithmetic remains after the private canonical primes are removed.  The answer is exact:

1. the noncanonical Cayley factors are precisely the primitive row/cover angular deficits already present in t65;
2. the canonical prime is in fact the unique largest odd prime of the **entire** reduced Cayley pair `P+ P-`, not merely of the denominator;
3. for two states, every common noncanonical odd prime has one of four `(+,+),(-,-),(+,-),(-,+)` root orientations and their gcds give an exact common-support modulus;
4. same-sign common support divides the square-scale cross determinant and opposite-sign common support divides the rotated cross resultant;
5. the fixed packet modulus `H=odd(h)` is always present in the negative/negative common support, and `gcd(odd(delta_i),odd(delta_j))` is always present in the positive/positive support;
6. nevertheless the squareclass condition plus the private-largest-prime tag does **not** force any additional common noncanonical prime.  Hence a generic small-prime-overlap argument cannot by itself close the remaining energy.

The current global Stage14 bound remains the merged/mainline

```text
V(B) << B^(3/4+o(1)).
```

No additional whole-family saving is claimed here.

---

## 1. Imported square-scale packet

Fix one legal dominant invisible packet

```text
(U, epsilon, k, h, kappa)
```

and write

```text
H = odd(h),
D = odd(delta),
D_pi = b^2-a^2 > 0,
D_V  = q^2-p^2 > 0.
```

Merged t65 gives

```text
a^2+b^2 = ell*m,
p^2+q^2 = k*delta,
h*k = epsilon*m,
gcd(delta,h)=1,
ell > 2*epsilon*m*delta.
```

For the exact cross-ratio square scale

```text
s = kappa*(u/v)^2,
gcd(u,v)=1,
0<s<1,
```

put

```text
raw+ = v^2+kappa*u^2,
raw- = v^2-kappa*u^2,
G    = gcd(raw+,raw-),
P+   = raw+/G,
P-   = raw-/G.
```

Then

```text
gcd(P+,P-)=1,
C(s)=P+/P-.
```

Merged t66/t67 retain

```text
D | P+,
ell*H | P-,
ell = LPF_odd(M),
M=ell*H*D,
2*(M/ell)<ell.
```

Merged t68 removes pairs on which one canonical prime divides either Cayley factor of the other state.

---

## 2. Exact angular cofactor factorization

Merged t65 proved that the only moving odd cancellation in

```text
C(s)=epsilon*delta*D_pi/(ell*h*D_V)
```

is

```text
g = gcd(odd(D_pi), odd(D_V)).
```

Define the primitive angular cofactors

```text
R_pi := odd(D_pi)/g,
R_V  := odd(D_V)/g.
```

Since `P+/P-` is the reduced Cayley fraction, t65 (65.16)--(65.17) gives exactly

```text
boxed:
odd(P+) = D * R_pi,

boxed:
odd(P-) = ell * H * R_V.
```

Moreover

```text
gcd(R_pi,R_V)=1,
gcd(D,ell*H*R_V)=1,
gcd(ell*H,R_pi)=1.
```

Thus there is no hidden noncanonical Cayley object.  The residual numerator is the uncancelled row deficit `b^2-a^2`; the residual denominator is the uncancelled cover deficit `q^2-p^2`.

```text
NONCANONICAL_CAYLEY_COFACTORS_IDENTIFIED_WITH_ANGULAR_DEFICITS=true
ODD_PPLUS_EXACT_ANGULAR_FACTORIZATION_PROVED=true
ODD_PMINUS_EXACT_ANGULAR_FACTORIZATION_PROVED=true
```

---

## 3. The reduced Cayley pair is coprime to the squareclass kernel

The t66 gcd identity can be sharpened for the reduced factors themselves.

Let `r` be a prime divisor of the squarefree representative `kappa`.

If `r` does not divide `v`, then

```text
raw+ == raw- == v^2 != 0 (mod r),
```

so `r` divides neither reduced factor.

If `r | v`, then `r` does not divide `u`.  Since `kappa` is squarefree,

```text
v_r(kappa*u^2)=1,
v_r(v^2)>=2,
```

hence

```text
v_r(raw+)=v_r(raw-)=1.
```

That common `r` is removed by `G`.  The same argument includes `r=2` when `2|kappa`.

Therefore

```text
boxed:
gcd(P+*P-, kappa)=1.
```

Every prime in the reduced Cayley support is a genuine unit prime for the square-scale root congruences.

```text
REDUCED_CAYLEY_SUPPORT_COPRIME_TO_KAPPA=true
```

---

## 4. `ell` is the unique largest odd prime of the full Cayley support

Merged t65 already proves that `ell` is the unique largest odd prime of `P-`.  The physical inequalities show more.

### 4.1 Radial numerator primes

For any odd prime `r|D`,

```text
r <= delta < ell
```

by `ell>2*epsilon*m*delta`.

### 4.2 Fixed negative cofactor primes

Since `h*k=epsilon*m` and `k>=1`,

```text
H <= h <= epsilon*m < ell/2.
```

Thus every odd prime of `H` is below `ell`.

### 4.3 Row angular primes

If odd `r|D_pi=b^2-a^2`, then `r` divides one of `b-a,b+a`.  Hence

```text
r <= a+b < sqrt(2(a^2+b^2))
            = sqrt(2*ell*m)
            < ell,
```

where the last inequality is exactly `2m<ell`, a consequence of the super-root budget.

### 4.4 Cover angular primes

Likewise, if odd `r|D_V=q^2-p^2`, then

```text
r <= p+q < sqrt(2(p^2+q^2))
            = sqrt(2n)
            < ell,
```

because merged t65 gives `ell>2n`.

Combining with Section 2,

```text
boxed:
ell = LPF_odd(P+*P-),
```

and merged t66 gives exponent one for `ell` in `P-`.

So the physical Cayley support has one distinguished private maximum prime; every other odd prime is strictly smaller.

```text
CANONICAL_ELL_UNIQUE_LARGEST_ODD_PRIME_OF_FULL_CAYLEY_PAIR=true
ALL_NONCANONICAL_ODD_CAYLEY_PRIMES_LT_ELL=true
```

This strengthening is state-local.  It does not make `ell_i` divide a cross determinant; t68 remains in force.

---

## 5. Four cross-state noncanonical support gcds

Take a mutually Cayley-private pair `i,j` in the same fixed packet and same squareclass `kappa`.  Since each canonical prime occurs once in its own negative factor and neither occurs in the other state's Cayley support, define the odd noncanonical factors

```text
C_i^+ := odd(P_i^+),
C_i^- := odd(P_i^-)/ell_i,

C_j^+ := odd(P_j^+),
C_j^- := odd(P_j^-)/ell_j.
```

By `gcd(P+,P-)=1`, the four cross gcds

```text
J_++ := gcd(C_i^+, C_j^+),
J_-- := gcd(C_i^-, C_j^-),
J_+- := gcd(C_i^+, C_j^-),
J_-+ := gcd(C_i^-, C_j^+)
```

are pairwise coprime.  Therefore

```text
boxed:
J_ij := gcd(C_i^+ C_i^-, C_j^+ C_j^-)
      = J_++ J_-- J_+- J_-+.
```

This `J_ij` is the **complete common odd support left after deleting both canonical primes**.

The physical radial pieces give two automatic inclusions:

```text
H | J_--,
gcd(D_i,D_j) | J_++.
```

Because `gcd(H,D_iD_j)=1`,

```text
H*gcd(D_i,D_j) | J_ij.
```

This recovers the common-modulus gcd seen by tH18, but `J_ij` may additionally contain angular or cross-role primes.

```text
NONCANONICAL_COMMON_SUPPORT_MODULUS_DEFINED=true
COMMON_H_NEGATIVE_ROOT_MODULUS_RETAINED=true
COMMON_DELTA_GCD_POSITIVE_ROOT_MODULUS_RETAINED=true
```

---

## 6. Same-sign support gives determinant divisibility; opposite-sign support gives rotated divisibility

For every odd prime power dividing `C_i^-`, Section 3 makes `u_i` a unit and

```text
(v_i/u_i)^2 = +kappa.
```

For every odd prime power dividing `C_i^+`,

```text
(v_i/u_i)^2 = -kappa.
```

Define the homogeneous square-scale cross forms

```text
Delta_uv(i,j)
 := v_i^2*u_j^2-u_i^2*v_j^2,

Sigma_uv(i,j)
 := v_i^2*u_j^2+u_i^2*v_j^2.
```

If a prime power occurs with the same sign in both states, the two square roots have the same square and hence it divides `Delta_uv`.  If it occurs with opposite signs, their squares differ by `-1` and it divides `Sigma_uv`.

Prime-power by prime-power,

```text
boxed:
J_++*J_-- | Delta_uv(i,j),

boxed:
J_+-*J_-+ | Sigma_uv(i,j).
```

Since the four gcds are pairwise coprime,

```text
boxed:
J_ij | Delta_uv(i,j)*Sigma_uv(i,j).
```

Thus every genuinely shared noncanonical prime does create a cross-state root/resultant modulus.  This is the exact counterpart to t68: **private canonical primes do not transfer, but primes genuinely present in both reduced Cayley supports do.**

```text
NONCANONICAL_COMMON_SUPPORT_RESULTANT_DICTIONARY_PROVED=true
SAME_SIGN_COMMON_SUPPORT_DIVIDES_SQUARE_SCALE_DETERMINANT=true
OPPOSITE_SIGN_COMMON_SUPPORT_DIVIDES_ROTATED_RESULTANT=true
```

---

## 7. The angular form of the same dictionary

Section 2 identifies the nonradial pieces as

```text
R_pi = odd((b-a)(b+a))/g,
R_V  = odd((q-p)(q+p))/g.
```

Consequently an odd prime shared by two row cofactors forces

```text
r | (a_i*b_j)^2-(b_i*a_j)^2,
```

a prime shared by two cover cofactors forces

```text
r | (p_i*q_j)^2-(q_i*p_j)^2,
```

and mixed row/cover sharing forces one of

```text
r | (a_i*q_j)^2-(b_i*p_j)^2,
r | (p_i*b_j)^2-(q_i*a_j)^2.
```

These are endpoint-root (`slope^2=1`) resultants.  They are useful only to the extent that a pair actually shares noncanonical support.

```text
ANGULAR_FOUR_ORIENTATION_RESULTANT_DICTIONARY_PROVED=true
```

---

## 8. No algebraic lower bound on the common noncanonical support

The same-squareclass condition itself does not force `J_ij` to be large, or even nontrivial beyond the fixed packet factor `H`.

A synthetic guard already exists inside the exact square-scale algebra.  Take `kappa=1`, `H=D_1=D_2=1` and

```text
state 1: (u,v)=(3,4)
P_1^- = 7,
P_1^+ = 25,
ell_1=7;

state 2: (u,v)=(5,14)
P_2^- = 171 = 19*3^2,
P_2^+ = 221 = 13*17,
ell_2=19.
```

For both states

```text
0<s=(u/v)^2<1,
ell_i occurs to exponent one in P_i^-,
2*(odd(P_i^-)/ell_i)<ell_i,
ell_i=LPF_odd(P_i^+P_i^-).
```

The canonical primes are mutually private and

```text
gcd(25, (171/19)*221)=1.
```

Hence

```text
J_12=1.
```

Both states are in squareclass `1`, yet there is no shared noncanonical odd prime at all.  This is an arithmetic guard for the reduced Cayley packet, not a claim that the two tuples reconstruct full physical cuboid states.

Therefore a proof that begins by demanding a large shared small-prime modulus would insert an unproved hypothesis.

```text
SAME_SQUARECLASS_FORCES_NONTRIVIAL_NONCANONICAL_OVERLAP=false
GENERIC_SMALL_PRIME_OVERLAP_CLOSURE_VALID=false
```

---

## 9. Revised live receiver

After t68/t69, a same-squareclass principal pair has:

- one private largest odd prime `ell_i` in each state;
- all remaining odd Cayley primes smaller than that state's `ell_i`;
- a completely explicit common-support modulus `J_ij`;
- exact determinant/resultant divisibility by the portions of `J_ij` that are genuinely shared;
- no algebraic lower bound forcing `J_ij` beyond the common fixed/radial pieces.

Define

```text
SharedUPrivateLargestPrimeCayleyCommonModulusEnergy
```

as the remaining mutually-private squareclass energy with the exact `J_ij` orientation data retained.

This is sharper than a generic root large sieve and sharper than the t68 receiver because it separates what really transfers between two states from what remains state-local.

The next t-stage should split according to the size of

```text
J_ij / (H*gcd(D_i,D_j)),
```

and test whether:

1. large common support is countable by primitive root-line/determinant spacing; while
2. small/coprime support can be reconstructed or charged by the angular factorizations `D_pi=(b-a)(b+a)` and `D_V=(q-p)(q+p)`.

No such dichotomy estimate is claimed at t69.

```text
SHARED_U_PRIVATE_LARGEST_PRIME_CAYLEY_COMMON_MODULUS_ENERGY_PROVED=false
SHARED_U_MUTUALLY_CAYLEY_PRIVATE_SQUARE_SCALE_ENERGY_PROVED=false
```

---

## 10. tH decision

Merged tH18 has already established that private canonical roots alone do not supply `1/Q` spacing and that the generic large sieve remains at `(Q^2+N)B^o(1)`.  Stage14-t69 identifies the exact additional modulus that can transfer: it is the pair-dependent common noncanonical support `J_ij`, not another canonical-prime theorem.

Before opening a new analytic tH task, the internal `J_ij` large/small dichotomy and its physical height balance must be determined.

```text
TH18_CONSUMED=true
TH19_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

---

## Shared exponent ledger

Merged Stage14-s7-29 and mainline Stage14-4cp give

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
```

Stage14-t69 proves no further global exponent saving.

---

## Locked boundary

```text
STAGE14_T69=COMPLETE_NONCANONICAL_CAYLEY_FACTOR_AND_COMMON_SUPPORT_REDUCTION
MERGED_T68_IMPORTED=true
MERGED_TH18_IMPORTED=true
NONCANONICAL_CAYLEY_COFACTORS_IDENTIFIED_WITH_ANGULAR_DEFICITS=true
REDUCED_CAYLEY_SUPPORT_COPRIME_TO_KAPPA=true
CANONICAL_ELL_UNIQUE_LARGEST_ODD_PRIME_OF_FULL_CAYLEY_PAIR=true
ALL_NONCANONICAL_ODD_CAYLEY_PRIMES_LT_ELL=true
NONCANONICAL_COMMON_SUPPORT_MODULUS_DEFINED=true
COMMON_H_NEGATIVE_ROOT_MODULUS_RETAINED=true
COMMON_DELTA_GCD_POSITIVE_ROOT_MODULUS_RETAINED=true
NONCANONICAL_COMMON_SUPPORT_RESULTANT_DICTIONARY_PROVED=true
ANGULAR_FOUR_ORIENTATION_RESULTANT_DICTIONARY_PROVED=true
SAME_SQUARECLASS_FORCES_NONTRIVIAL_NONCANONICAL_OVERLAP=false
GENERIC_SMALL_PRIME_OVERLAP_CLOSURE_VALID=false
SHARED_U_PRIVATE_LARGEST_PRIME_CAYLEY_COMMON_MODULUS_ENERGY_PROVED=false
SHARED_U_MUTUALLY_CAYLEY_PRIVATE_SQUARE_SCALE_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4
T69_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH18_CONSUMED=true
TH19_NEEDED=false
NEXT=Stage14-t70
```
