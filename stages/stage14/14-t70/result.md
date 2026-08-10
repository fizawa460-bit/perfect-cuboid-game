# Stage14-t70 — full common-support CRT root line and small-overlap reduction

## Purpose

Merged Stage14-t69 reduces the dominant fixed-`U` invisible collision problem to mutually Cayley-private pairs in a fixed packet `(U,epsilon,k,h,kappa)`.  For each state `i`, after removing the private canonical prime `ell_i`, define

```text
C_i^+ = odd(P_i^+),
C_i^- = odd(P_i^-)/ell_i.
```

For a pair `(i,j)`, t69 defines four pairwise-coprime common-support components

```text
J++ = gcd(C_i^+,C_j^+),
J-- = gcd(C_i^-,C_j^-),
J+- = gcd(C_i^+,C_j^-),
J-+ = gcd(C_i^-,C_j^+),
J   = J++ J-- J+- J-+.
```

The planned t69 next step was to split according to the extra quotient

```text
E = J/(odd(h)*gcd(odd(delta_i),odd(delta_j))).
```

Stage14-t70 sharpens this plan.  The primitive spacing modulus is the **full `J`**, not only `E`: the forced radial base and the extra angular overlap lie on the same CRT root line and must not be uncharged before spacing.

The result is:

1. every common-support pair gives one primitive linear root line modulo `J`, with only `B^o(1)` orientation choices;
2. on a dyadic square-scale box `u~U_0, v~V_0`, a fixed anchor has at most `B^o(1)(1+U_0V_0/J)` partners on that line;
3. hence the branch `J >= U_0V_0 B^{-o(1)}` is near-linear;
4. the complementary small-`J` branch is not closed by common-support algebra alone, and even finite pairwise-`J=1` cliques satisfying the private-largest-prime square-scale axioms exist;
5. the remaining receiver must retain the physical fixed-`U` Gaussian/canonical-prime reconstruction, rather than replacing it by a generic small-prime-overlap theorem.

Merged s7-30 now supplies the shared whole-family exponent `11/16`.  t70 does not improve that exponent further.

---

## 1. Imported t69 packet

Write

```text
s_i = kappa*(u_i/v_i)^2,
gcd(u_i,v_i)=1,
0 < kappa*u_i^2 < v_i^2.
```

Merged t66/t69 give

```text
P_i^+ = (v_i^2+kappa*u_i^2)/G_i,
P_i^- = (v_i^2-kappa*u_i^2)/G_i,
gcd(P_i^+P_i^-,kappa)=1,
ell_i = LPF_odd(P_i^+P_i^-),
```

and every odd prime in `C_i^+C_i^-` is strictly smaller than `ell_i`.

For mutually Cayley-private pairs, neither `ell_i` nor `ell_j` occurs in the other state's full Cayley support.  The only cross-state modulus retained at t70 is therefore the noncanonical common support `J` above.

Because any odd prime `r|P_i^+P_i^-` is coprime to `kappa` and

```text
gcd(u_i,v_i)=1,
```

we also have

```text
gcd(r,u_i v_i)=1.
```

Thus every `u_i,v_i` is a unit modulo every prime-power divisor of its noncanonical Cayley support.

---

## 2. Prime-power orientation dictionary

Set the projective square-scale slope

```text
z_i = v_i/u_i
```

modulo an odd prime power dividing a common-support component.

### Same-sign components

If `r^e | J++`, then

```text
z_i^2 == -kappa (mod r^e),
z_j^2 == -kappa (mod r^e).
```

Hence

```text
(z_j/z_i)^2 == 1 (mod r^e).
```

For odd prime powers the only roots of `X^2=1` are `+1,-1`, so

```text
z_j == +/- z_i (mod r^e).
```

Exactly the same argument applies to `J--`, where both squares are `+kappa`.

### Opposite-sign components

If `r^e | J+-` or `r^e | J-+`, the two states have opposite signs:

```text
z_i^2 == -kappa,
z_j^2 == +kappa
```

or vice versa.  Therefore

```text
(z_j/z_i)^2 == -1 (mod r^e).
```

In particular `r == 1 (mod 4)`, and there are exactly two prime-power orientations `+i_r,-i_r`.

Thus each prime-power divisor of `J` contributes at most two actual root orientations once its plus/minus role is fixed.

```text
COMMON_SUPPORT_PRIME_POWER_ROOT_ORIENTATION_PROVED=true
OPPOSITE_SIGN_COMMON_SUPPORT_PRIMES_SPLIT_MOD4=true
```

---

## 3. CRT compresses all four roles to one primitive linear root line

The four t69 components are pairwise coprime.  Choose, at each prime power `r^e||J`, the actual local ratio

```text
lambda_{r^e} = z_j/z_i (mod r^e).
```

It satisfies

```text
lambda_{r^e}^2 = +1   on J++*J--,
lambda_{r^e}^2 = -1   on J+-*J-+.
```

By CRT there is a unique `lambda mod J` for these local choices.  Therefore the whole pair obeys the single linear congruence

```text
boxed:
v_j*u_i == lambda*u_j*v_i (mod J).
```

Since `u_i,v_i` are units modulo `J`, for fixed anchor `i` this is a standard primitive root line

```text
boxed:
v_j == r_{i,J,lambda} u_j (mod J).
```

The role allocation and local signs contribute at most

```text
4^omega(J) <= tau(J)^2 = B^o(1)
```

possible root lines.  No fixed power is lost.

This is strictly stronger than retaining only the two quadratic resultants

```text
J++J-- | v_i^2u_j^2-u_i^2v_j^2,
J+-J-+ | v_i^2u_j^2+u_i^2v_j^2.
```

The quadratic resultant pair has been compressed back to a primitive **linear** root-line condition.

```text
FOUR_ORIENTATION_COMMON_SUPPORT_CRT_COMPRESSES_TO_ONE_LINEAR_ROOT_LINE=true
COMMON_SUPPORT_ROOT_LINE_MULTIPLICITY=Bo1
```

---

## 4. The full J, including radial base, is chargeable spacing

Merged t69 proves

```text
H := odd(h) | J--,
gcd(D_i,D_j) | J++,
D_i := odd(delta_i).
```

Hence

```text
J_base = H*gcd(D_i,D_j) | J.
```

There is no reason to divide `J_base` out before applying the root-line spacing lemma.  Both the forced radial support and any extra angular support occur in the same congruence of Section 3.

Therefore the correct spacing parameter is

```text
boxed: J,
```

not merely

```text
E = J/J_base.
```

A large radial gcd can close a pair even when `E=1`.  Conversely `E` is useful only as a diagnostic of where the extra support came from.

```text
T69_EXTRA_ONLY_DICHOTOMY_SUPERSEDED=true
FULL_COMMON_SUPPORT_MUST_BE_USED_BEFORE_RADIAL_UNCHARGING=true
```

---

## 5. Primitive root-line partner bound

Fix:

- one packet `(U,epsilon,k,h,kappa)`;
- one anchor state `i`;
- one odd divisor `J | C_i^+C_i^-`;
- one CRT orientation `lambda`;
- one dyadic primitive square-scale box

```text
u_j ~ U_0,
v_j ~ V_0.
```

Every partner is a primitive positive point on one line

```text
v_j == r u_j (mod J),
gcd(r,J)=1.
```

The primitive determinant-spacing lemma used in merged s7-29 gives

```text
# {(u_j,v_j) in the box}
 <= 1 + 6 U_0 V_0/J.
```

For a fixed primitive pair `(u_j,v_j)`, the exact value

```text
s_j = kappa*(u_j/v_j)^2
```

is fixed.  Merged t65 proves fixed `(U,s_j)` invisible physical multiplicity `O(1)`.  Hence the same estimate holds for physical partners, up to `B^o(1)` packet/divisor/orientation bookkeeping:

```text
boxed:
N_i(J;U_0,V_0)
 <= (1 + U_0V_0/J) B^o(1).
```

Because the exact gcd `J` is a divisor of the fixed anchor integer `C_i^+C_i^-`, summing over all possible `J` costs only `tau(C_i^+C_i^-)=B^o(1)`.

For the hyperbolic union `u_j v_j <= M`, dyadic decomposition gives the equivalent form

```text
boxed:
N_i(J;M)
 <= (1 + M/J) B^o(1).
```

```text
FIXED_ANCHOR_COMMON_SUPPORT_ROOTLINE_PARTNER_BOUND_PROVED=true
FIXED_ANCHOR_COMMON_SUPPORT_ROOTLINE_PARTNER_BOUND=(1+M/J)*Bo1
```

---

## 6. Large-J branch is near-linear

Let `R_U` be the number of physical states in one fixed packet/squareclass block and suppose a dyadic square-scale block has `u v <= M`.

For any threshold `L`, Section 5 gives

```text
I_{J>=L}
 <= R_U (1 + M/L) B^o(1).
```

In particular, at root-line scale

```text
L >= M B^{-o(1)},
```

we obtain

```text
boxed:
I_{J>=L} <= R_U B^o(1).
```

If one insists on the t69 extra quotient

```text
E = J/(H*gcd(D_i,D_j)),
```

then `J >= H E`, so

```text
I_{E>=L}
 <= R_U (1 + M/(H L)) B^o(1).
```

This is valid but weaker because it throws away the useful factor `gcd(D_i,D_j)`.

```text
LARGE_FULL_COMMON_SUPPORT_ROOTLINE_BRANCH_NEAR_LINEAR=true
LARGE_EXTRA_COMMON_SUPPORT_PARAMETRIC_BOUND_PROVED=true
```

No new whole-family exponent follows automatically: one still needs to control the complementary branch in which `J` is small relative to the square-scale area.

---

## 7. Why small J is the genuine remaining branch

For

```text
J << M,
```

the primitive root-line estimate is only

```text
M/J,
```

which can be a fixed power.  Splitting `J` into the linear angular factors

```text
b_i-a_i,
 b_i+a_i,
 q_i-p_i,
 q_i+p_i
```

does not by itself improve this: it only refines the same small modulus into divisor-many local orientations.

More importantly, same squareclass and private-largest-prime axioms do not force any nontrivial common noncanonical support.  A finite synthetic guard with `kappa=1`, `H=D=1` contains the six primitive square-scale states

```text
(ell,u,v) =
(  7,  3,  4),
( 19,  5, 14),
( 41, 20, 21),
( 47, 12, 35),
(127, 42, 85),
(151, 60, 91).
```

For each state:

- `ell` divides `P^-` to exponent one;
- `ell` is the unique largest odd prime of `P^+P^-`;
- its noncanonical support is coprime to the noncanonical support of every other listed state;
- every canonical `ell_i` is private from every other state's full Cayley support.

Thus every one of the `15` pairs has

```text
J_ij = 1.
```

This is not a physical cuboid family and is not an asymptotic lower bound.  It is an exact algebraic guard showing that no deterministic small-support reconstruction theorem follows from the Cayley square-scale axioms alone.

```text
GENERIC_SMALL_J_CAYLEY_RECONSTRUCTION_VALID=false
SMALL_J_SYNTHETIC_PAIRWISE_DISJOINT_CLIQUE_SIZE=6
```

The physical fixed-`U` Gaussian multiplication, canonical Gaussian prime orientation, primitive-`V` reconstruction and chamber constraints must therefore remain in the next receiver.

---

## 8. Minimal remaining receiver

After t70, the large common-support branch is no longer the obstruction.  Define

```text
SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy
```

as the mutually Cayley-private same-`kappa` pair count restricted to dyadic blocks where

```text
J_ij < U_0V_0 B^{-o(1)}.
```

The definition retains:

```text
fixed U, epsilon, k, h,
canonical Gaussian prime pi_i, pi_j,
primitive V_i,V_j,
physical chamber,
sharp super-root inequalities,
exact Cayley factors,
private largest-prime tags.
```

It does **not** replace these masks by a generic abstract square-scale family, because Section 7 shows that such a theorem is false as a deterministic algebraic reconstruction principle.

```text
SHARED_U_PRIVATE_LARGEST_PRIME_SMALL_COMMON_SUPPORT_PHYSICAL_SQUARE_SCALE_ENERGY_PROVED=false
SHARED_U_PRIVATE_LARGEST_PRIME_CAYLEY_COMMON_MODULUS_ENERGY_PROVED=false
```

The next internal step is to express the small common-support condition directly in the Gaussian row coordinate `pi*U` and the primitive cover `V`, rather than asking a broad common-root large sieve.

---

## 9. Relation to tH18 and tH decision

Merged tH18 proved that the pre-t68 private-root fractions do not have `1/Q` spacing and left the strong analytic contract `PRCTORLS`.  t68/t69/t70 move in a different direction:

- t68 removes canonical-prime transfer;
- t69 identifies the actual shared noncanonical modulus;
- t70 shows that this **actual shared modulus** does produce primitive `1/J` root-line spacing.

Therefore tH18 remains consumed and does not reopen.

A new tH19 is **not yet needed**.  The live small-`J` branch still carries unused exact physical algebra: `a+ib = pi U` and `p+iq = V` (up to the frozen conventions), while the noncanonical factors are exactly the angular deficits `b^2-a^2` and `q^2-p^2`.  Stage14-t71 should use that Gaussian multiplication before asking for an external average theorem.

```text
TH18_CONSUMED=true
TH19_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

---

## Shared exponent ledger

Merged s7-30 proves

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=11/16
IMPROVEMENT_OVER_3_4=1/16
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
```

for the shared Stage14 whole family.  The later 4cq branch was based on the older `3/4` ledger and does not invalidate the stronger merged s7-30 proof.  Stage14-t70 itself proves no additional whole-family saving.

```text
MERGED_S7_30_GLOBAL_11_16_LEDGER_IMPORTED=true
T70_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
```

---

## Locked boundary

```text
STAGE14_T70=COMPLETE_FULL_COMMON_SUPPORT_CRT_ROOTLINE_AND_SMALL_OVERLAP_REDUCTION
MERGED_T69_IMPORTED=true
MERGED_TH18_IMPORTED=true
MERGED_S7_30_GLOBAL_11_16_LEDGER_IMPORTED=true
COMMON_SUPPORT_PRIME_POWER_ROOT_ORIENTATION_PROVED=true
OPPOSITE_SIGN_COMMON_SUPPORT_PRIMES_SPLIT_MOD4=true
FOUR_ORIENTATION_COMMON_SUPPORT_CRT_COMPRESSES_TO_ONE_LINEAR_ROOT_LINE=true
COMMON_SUPPORT_ROOT_LINE_MULTIPLICITY=Bo1
T69_EXTRA_ONLY_DICHOTOMY_SUPERSEDED=true
FULL_COMMON_SUPPORT_MUST_BE_USED_BEFORE_RADIAL_UNCHARGING=true
FIXED_ANCHOR_COMMON_SUPPORT_ROOTLINE_PARTNER_BOUND_PROVED=true
FIXED_ANCHOR_COMMON_SUPPORT_ROOTLINE_PARTNER_BOUND=(1+M/J)*Bo1
LARGE_FULL_COMMON_SUPPORT_ROOTLINE_BRANCH_NEAR_LINEAR=true
LARGE_EXTRA_COMMON_SUPPORT_PARAMETRIC_BOUND_PROVED=true
GENERIC_SMALL_J_CAYLEY_RECONSTRUCTION_VALID=false
SMALL_J_SYNTHETIC_PAIRWISE_DISJOINT_CLIQUE_SIZE=6
SHARED_U_PRIVATE_LARGEST_PRIME_SMALL_COMMON_SUPPORT_PHYSICAL_SQUARE_SCALE_ENERGY_PROVED=false
SHARED_U_PRIVATE_LARGEST_PRIME_CAYLEY_COMMON_MODULUS_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=11/16
T70_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH18_CONSUMED=true
TH19_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-t71
```
