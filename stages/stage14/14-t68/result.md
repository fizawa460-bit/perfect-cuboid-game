# Stage14-t68 — cross-resultant dictionary and canonical-prime transfer no-go

## Purpose

Merged Stage14-t67 reduces the dominant fixed-`U` invisible squareclass problem, after same-modulus, same-canonical-prime and nested-prime removal, to private canonical-prime pairs. For one fixed packet `(U,epsilon,k,h)` and one fixed squareclass `kappa`, each state has

```text
s = kappa*(u/v)^2,
gcd(u,v)=1,
P+ = (v^2+kappa*u^2)/G,
P- = (v^2-kappa*u^2)/G,
M = ell*odd(h)*odd(delta),
ell = LPF_odd(M),
2*(M/ell) < ell.
```

The t67 private condition for two states `i,j` is

```text
ell_i != ell_j,
ell_i not | M_j,
ell_j not | M_i.
```

Stage14-t68 asks whether the two large private canonical primes force a cross-determinant or cross-resultant divisibility. The generic answer is no. There is an exact cross-resultant dictionary, but a canonical prime divides a cross resultant iff it is an additional plus/minus Cayley-factor divisor of the other state. Those cross-factor-contaminated pairs are divisor-many and near-linear by merged t36. After removing them, neither canonical prime divides any natural quadratic cross resultant. Moreover, after conditioning on the common squareclass `kappa`, the canonical-prime quadratic square test is identically coherent across the whole fiber.

Thus the t67 proposal `PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve` is not the minimal remaining theorem: the private canonical prime is a root modulus only for its own state, not for the other state in a principal pair.

Merged Stage14-s7-29 now supplies the shared whole-family bound

```text
V(B) << B^(3/4+o(1)).
```

Stage14-t68 does not improve that exponent further; it sharpens only the fixed-`U` t-route receiver.

---

## 1. Imported private-pair packet

Fix one merged-t67 packet and one squareclass `kappa`. For each state `i`, write

```text
s_i = kappa*(u_i/v_i)^2,
(u_i,v_i)=1,
```

and

```text
G_i = gcd(v_i^2+kappa*u_i^2,
          v_i^2-kappa*u_i^2),

P_i^+ = (v_i^2+kappa*u_i^2)/G_i,
P_i^- = (v_i^2-kappa*u_i^2)/G_i.
```

Merged t66 gives

```text
odd(delta_i) | P_i^+,
ell_i*odd(h) | P_i^-,
gcd(ell_i*odd(h)*odd(delta_i),kappa)=1.
```

Merged t67 defines

```text
M_i = ell_i*odd(h)*odd(delta_i)
    = ell_i*c_i,
2*c_i < ell_i,
ell_i = LPF_odd(M_i).
```

For a private pair `(i,j)`,

```text
ell_i != ell_j,
ell_i not | M_j,
ell_j not | M_i.
```

This says the canonical primes do not occur in the other state's physical radial modulus. It does not yet exclude their occurrence as uncharged divisors of the other state's full reduced Cayley factors `P_j^+P_j^-`.

---

## 2. Exact canonical cross-resultants

For two states in the same `kappa` fiber define

```text
Delta_ij
 := u_i^2*v_j^2 - v_i^2*u_j^2
  = (u_i*v_j-v_i*u_j)(u_i*v_j+v_i*u_j),

Sigma_ij
 := u_i^2*v_j^2 + v_i^2*u_j^2.
```

Because `ell_i | P_i^-`, merged t66 gives

```text
v_i^2 == kappa*u_i^2  (mod ell_i),
```

and `u_i` is a unit modulo `ell_i`. Hence

```text
Delta_ij
 == u_i^2*(v_j^2-kappa*u_j^2)  (mod ell_i),

Sigma_ij
 == u_i^2*(v_j^2+kappa*u_j^2)  (mod ell_i).
```

Also `ell_i` is coprime to `kappa`, while every odd prime factor of `G_j` divides `kappa`; therefore `ell_i not | G_j`. Consequently

```text
boxed:
ell_i | Delta_ij
<=> ell_i | P_j^-,

boxed:
ell_i | Sigma_ij
<=> ell_i | P_j^+.
```

The same statements hold with `i,j` reversed.

Equivalently, for

```text
R_ij := Delta_ij*Sigma_ij
      = u_i^4*v_j^4-v_i^4*u_j^4,
```

we have

```text
ell_i | R_ij
<=> ell_i | P_j^+*P_j^-.
```

Thus the natural determinant/resultant does not create a new canonical-prime divisibility law; it only detects whether the canonical prime is an extra divisor of the other state's two Cayley factors.

```text
CANONICAL_CROSS_RESULTANT_DICTIONARY_PROVED=true
PRIVATE_ELL_FORCES_CROSS_DETERMINANT=false
```

---

## 3. Cross-factor contamination is divisor-many

Call an ordered pair `(i,j)` cross-factor contaminated when

```text
ell_i | P_j^+*P_j^-.
```

Fix `j`. The integer `P_j^+*P_j^-` has physical height `B^{O(1)}`, hence only `B^{o(1)}` distinct prime divisors. For each fixed candidate canonical prime `ell`, merged t36 gives near-linear fixed-direction squareclass energy. A rational prime `ell=1 mod 4` has only `O(1)` Gaussian prime associates, so fixed `(U,ell,kappa)` contains only `B^{o(1)}` states in the squareclass fiber.

Therefore every fixed state has only `B^{o(1)}` cross-factor-contaminated partners, and

```text
boxed:
I_cross-factor <= R_U*B^{o(1)}.
```

This removes every private pair for which either canonical prime actually divides a natural cross determinant or its `sqrt(-1)` companion.

```text
CROSS_FACTOR_CONTAMINATION_NEAR_LINEAR=true
```

---

## 4. Mutually Cayley-private pairs

After t67 removal and Section 3, the live pair satisfies

```text
ell_i not | M_j,
ell_j not | M_i,

ell_i not | P_j^+*P_j^-,
ell_j not | P_i^+*P_i^-.
```

Call such a pair mutually Cayley-private. By Section 2,

```text
ell_i not | Delta_ij*Sigma_ij,
ell_j not | Delta_ij*Sigma_ij.
```

Hence neither large canonical prime supplies determinant spacing for the primitive square-scale vectors `(u_i,v_i)` and `(u_j,v_j)`.

`Delta_ij` detects equality/opposition of the negative roots; `Sigma_ij` detects the `sqrt(-1)`-rotated positive root. These are exactly the two local root orientations isolated in t66. Once both fail, the other state lies on neither canonical root line modulo `ell_i`.

```text
MUTUALLY_CAYLEY_PRIVATE_PAIR_DEFINED=true
CANONICAL_PRIME_DETERMINANT_SPACING_AVAILABLE=false
```

---

## 5. Canonical quadratic tests are coherent on a fixed squareclass

The principal pair already has the same rational squareclass `kappa`. From

```text
v_i^2 == kappa*u_i^2 (mod ell_i)
```

we obtain

```text
(kappa/ell_i)=+1.
```

For any other state `j` in the same squareclass,

```text
s_j = kappa*(u_j/v_j)^2.
```

The local `ell_i`-adic valuation of `s_j` is even, and its unit squareclass is the product of a rational square with the already-square unit `kappa`. Therefore

```text
boxed:
s_j in Q_{ell_i}^{*2}
```

for every `j` in the same `kappa` fiber. When `u_jv_j` is a unit modulo `ell_i`, this is simply

```text
(s_j/ell_i)=+1.
```

Thus the private canonical-prime quadratic square test is identically coherent on the principal squareclass fiber. It cannot distinguish one state in that fiber from another.

```text
CANONICAL_PRIME_LOCAL_SQUARE_TEST_IDENTICALLY_COHERENT_ON_KAPPA_FIBER=true
```

---

## 6. Root orientation does not transfer across a clean private pair

For its own state, `ell_i` carries

```text
(v_i/u_i)^2 == +kappa (mod ell_i).
```

For another state `j`, the condition

```text
(v_j/u_j)^2 == +kappa (mod ell_i)
```

is equivalent, homogeneously, to `ell_i | P_j^-`; the condition with `-kappa` is equivalent to `ell_i | P_j^+`. Both alternatives are excluded on a mutually Cayley-private pair.

Therefore the local `+sqrt(kappa)` versus `+i*sqrt(kappa)` orientation is state-local. It does not propagate merely because two states share the same rational squareclass.

```text
PRIVATE_CANONICAL_ROOT_ORIENTATION_TRANSFERS_TO_OTHER_STATE=false
```

---

## 7. Synthetic arithmetic no-go regression

Take the abstract square-scale packet

```text
kappa=1,
h=delta=1,

ell_1=101,
(u_1,v_1)=(50,51),

ell_2=109,
(u_2,v_2)=(54,55).
```

Then

```text
v_1^2-u_1^2 = 101,
v_2^2-u_2^2 = 109,
```

so each canonical prime is the unique negative-factor prime with cofactor `1 < ell/2`. The two primes are mutually private, while direct calculation gives

```text
101 not | Delta_12,
101 not | Sigma_12,
109 not | Delta_12,
109 not | Sigma_12.
```

Thus even the sharp largest-prime tag plus common squareclass does not force either canonical prime into the cross determinant or its positive-orientation companion. This is an arithmetic no-go regression, not a claim that the synthetic tuple reconstructs a physical cuboid state.

---

## 8. Revised minimal receiver

The live dominant invisible receiver is now

```text
SharedUMutuallyCayleyPrivateSquareScaleEnergy.
```

It counts same-`kappa` pairs after removing

```text
same M,
same ell,
nested canonical-prime pairs,
cross-factor-contaminated pairs,
```

while retaining the physical reconstruction, primitive `V`, chamber, fixed-`U` packet and sharp radial constraints.

For these pairs the large canonical primes are local state tags, not shared moduli. The next arithmetic must come from the noncanonical factors of `P_i^+P_i^-`, their common small-prime support, or a direct primitive square-scale incidence.

```text
SHARED_U_MUTUALLY_CAYLEY_PRIVATE_SQUARE_SCALE_ENERGY_PROVED=false
SHARED_U_PRIVATE_CANONICAL_PRIME_ROOT_MODULUS_ENERGY_PROVED=false
```

---

## 9. tH decision

The t66/t67 request

```text
PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve
```

is superseded by t68. A private canonical prime is not a root modulus for the other state except on the cross-factor-contaminated pairs already removed at `R_U B^{o(1)}` cost. On the clean principal fiber its quadratic squareclass test is identically coherent.

No tH18 branch or PR exists on the repository at this checkpoint. Therefore the old tH18 target should not be started. If a later t-stage isolates a genuine theorem on the remaining noncanonical cofactor incidence, a new tH target can be opened then.

```text
TH18_PREVIOUS_REQUEST_SUPERSEDED=true
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH18=false
```

---

## Shared exponent ledger

Merged Stage14-s7-29 proves

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
```

for the global Stage14 problem. This saving comes from the s7 primitive common-core root-line argument, not from t68. The local t68 result neither weakens nor further improves that bound.

```text
MERGED_S7_29_GLOBAL_3_4_LEDGER_IMPORTED=true
T68_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
```

---

## Locked boundary

```text
STAGE14_T68=COMPLETE_CANONICAL_CROSS_RESULTANT_DICTIONARY_AND_PRIVATE_PRIME_TRANSFER_NOGO
MERGED_T67_IMPORTED=true
MERGED_S7_29_GLOBAL_3_4_LEDGER_IMPORTED=true
CANONICAL_CROSS_RESULTANT_DICTIONARY_PROVED=true
PRIVATE_ELL_FORCES_CROSS_DETERMINANT=false
CROSS_FACTOR_CONTAMINATION_NEAR_LINEAR=true
MUTUALLY_CAYLEY_PRIVATE_PAIR_DEFINED=true
CANONICAL_PRIME_DETERMINANT_SPACING_AVAILABLE=false
CANONICAL_PRIME_LOCAL_SQUARE_TEST_IDENTICALLY_COHERENT_ON_KAPPA_FIBER=true
PRIVATE_CANONICAL_ROOT_ORIENTATION_TRANSFERS_TO_OTHER_STATE=false
SHARED_U_MUTUALLY_CAYLEY_PRIVATE_SQUARE_SCALE_ENERGY_PROVED=false
SHARED_U_PRIVATE_CANONICAL_PRIME_ROOT_MODULUS_ENERGY_PROVED=false
SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
T68_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH18_PREVIOUS_REQUEST_SUPERSEDED=true
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH18=false
NEXT=Stage14-t69
```
