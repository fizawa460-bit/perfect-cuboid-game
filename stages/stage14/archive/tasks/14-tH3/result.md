# Stage14-tH3 — all-order ray-class / hyperbola conductor adapter

## Purpose

Stage14-tH1 fixed the Gaussian primary/ray-class normalization for arbitrary multiplicative character order. Stage14-tH2 independently converted the divisor-coupled norm skeleton

\[
N(U)=m,\qquad N(V)=k\delta,\qquad k\mid\varepsilon m,
\qquad m\delta\le Y
\]

into

\[
N(U)=hr,\qquad N(V)=gh\delta,
\qquad g\mid\varepsilon,
\qquad (h,\varepsilon/g)=1,
\qquad hr\delta\le Y.
\]

Stage14-tH3 joins these two roadworks layers.

Its job is not to prove a large sieve. Its job is to define, exactly and without hidden unit/modulus duplication, the character-family record which a later large-sieve or dispersion theorem receives.

The adapter must preserve three facts simultaneously:

1. local Mellin modes may have arbitrary multiplicative order;
2. the Stage14 Mellin support which is trivial on \(\mu_4\) has no ramified \((1+i)\)-conductor correction;
3. the `U` and `V` characters may use the **same auxiliary Gaussian prime modulus**, and that shared modulus must be stored once rather than tensorised into two independent copies.

The minimum dependencies are merged Stage14-tH1 and Stage14-tH2. No future `t` stage is required.

---

## 1. Local character record imported from tH1

For a rational split prime

\[
p\equiv1\pmod4,
\]

fix an orientation

\[
\mathfrak l_{p,\rho},\qquad \rho\in\{+1,-1\},
\]

and a local character exponent

\[
j\in\mathbf Z/(p-1)\mathbf Z.
\]

The tH1 local record is

```text
LocalCharKey = (p, rho, j mod p-1).
```

Its exact order is

\[
\operatorname{ord}(\psi)=\frac{p-1}{\gcd(j,p-1)}
\]

for `j!=0`, with the trivial character at `j=0`.

Its unit signature is

\[
s(p,\rho,j)=\rho j\pmod4.
\]

For a finite product on one coordinate, the signatures add modulo four and tH1 gives the exact primitive conductor

\[
\mathfrak f
=(1+i)^{e_2(J)}\prod_{j_s\ne0}\mathfrak l_s,
\]

where

\[
e_2(0)=0,\qquad e_2(2)=2,\qquad e_2(1)=e_2(3)=3.
\]

Stage14-tH3 uses this record without changing it.

---

## 2. Stage14 \(\mu_4\)-trivial modes have no ramified conductor

The split-torus Mellin support isolated by the live t route is the subfamily

\[
\psi|_{\mu_4}=1.
\]

Under the tH1 normalization,

\[
\psi(i)=i^{\rho j}.
\]

Therefore

\[
\psi|_{\mu_4}=1
\iff
\rho j\equiv0\pmod4
\iff
\boxed{j\equiv0\pmod4}.
\tag{H3.1}
\]

Every local unit signature is then zero. Hence every finite CRT product of Stage14 Mellin modes has

\[
J=0,
\qquad
\boxed{e_2(J)=0}.
\tag{H3.2}
\]

Thus for the Stage14 \(\mu_4\)-trivial family the primitive coordinate conductor is purely odd:

\[
\boxed{
\mathfrak f_{\mu_4}
=\prod_{j_s\ne0}\mathfrak l_s.
}
\tag{H3.3}
\]

There is no hidden factor `2`, `4`, or `8` in the conductor norm.

This is an exact algebraic simplification, not an asymptotic estimate.

```text
MU4_TRIVIAL_MODE_IFF_J_MULTIPLE_OF_4=true
MU4_TRIVIAL_FAMILY_UNIT_SIGNATURE_ZERO=true
MU4_TRIVIAL_FAMILY_TWO_ADIC_CONDUCTOR_EXPONENT_ZERO=true
```

---

## 3. Two-coordinate packet: coordinate conductors versus joint modulus envelope

A Stage14 spectral packet carries one character on the `U` coordinate and one character on the `V` coordinate.

Write their exact primitive conductors as

\[
\mathfrak f_U,
\qquad
\mathfrak f_V.
\]

These remain distinct character conductors because `U` and `V` are different variables.

For bookkeeping across a theorem which evaluates both coordinates, define the **joint modulus envelope**

\[
\boxed{
\mathfrak q_{UV}
=\operatorname{lcm}(\mathfrak f_U,\mathfrak f_V).
}
\tag{H3.4}
\]

This is an evaluation modulus, not the primitive conductor of a fictitious one-variable product character.

If

\[
A_U=\{\mathfrak l:\mathfrak l\mid\mathfrak f_U\},
\qquad
A_V=\{\mathfrak l:\mathfrak l\mid\mathfrak f_V\},
\]

then

\[
\boxed{
\mathfrak q_{UV}
=(1+i)^{\max(e_{2,U},e_{2,V})}
\prod_{\mathfrak l\in A_U\cup A_V}\mathfrak l.
}
\tag{H3.5}
\]

So a Gaussian prime ideal which is active on both coordinates appears **once** in the joint modulus envelope.

For the \(\mu_4\)-trivial Stage14 family,

\[
\boxed{
\mathfrak q_{UV}
=\prod_{\mathfrak l\in A_U\cup A_V}\mathfrak l.
}
\tag{H3.6}
\]

This is the exact modulus object later tH stages must preserve.

---

## 4. Same auxiliary modulus is not squared

Consider one oriented split prime ideal \(\mathfrak l\mid p\) and two local modes

\[
\xi(U),\qquad \zeta(V)
\]

at that same ideal.

If at least one mode is nontrivial, then

\[
\boxed{
\mathfrak q_{UV}=\mathfrak l,
\qquad N\mathfrak q_{UV}=p.
}
\tag{H3.7}
\]

Even when both modes are nontrivial, the joint modulus is **not** \(\mathfrak l^2\) and its norm is not \(p^2\).

The two-dimensionality lies in the character pair `(xi,zeta)`, not in two independent copies of the modulus.

This is precisely the data which an independent-modulus tensorisation would destroy.

The tH3 downstream rule is therefore:

```text
same auxiliary prime ideal
  -> one modulus_group_id
  -> two coordinate character indices
  -> one joint modulus factor.
```

```text
SHARED_AUXILIARY_MODULUS_PRESERVED=true
SHARED_PRIME_JOINT_MODULUS_SQUARED=false
```

---

## 5. Conjugate prime ideals remain distinct

The two oriented primes

\[
\mathfrak l_{p,+},\qquad \mathfrak l_{p,-}
\]

are distinct prime ideals even though both have norm `p`.

If a character genuinely contains nontrivial factors at both conjugate ideals, then the odd conductor contains both and contributes

\[
N(\mathfrak l_{p,+}\mathfrak l_{p,-})=p^2.
\]

Thus tH3 does **not** collapse Gaussian orientation.

The rules are:

```text
same oriented Gaussian prime used by U and V -> count once in joint envelope
conjugate Gaussian primes both genuinely active -> count both
```

This distinguishes shared-modulus geometry from accidental equality of rational norms.

---

## 6. Exact one-prime spectral cardinality

For one oriented split prime \(\mathfrak l\mid p\), characters trivial on \(\mu_4\) are exactly the exponents

\[
j=0,4,8,\dots,p-5.
\]

Hence the local Stage14 Mellin character space has size

\[
\boxed{H_p=\frac{p-1}{4}}.
\tag{H3.8}
\]

A two-coordinate same-modulus packet has

\[
\boxed{H_p^2}
\]

ordered pairs `(j_U,j_V)`.

Exactly one pair is trivial on both coordinates. Therefore

\[
\boxed{
H_p^2-1
}
\tag{H3.9}
\]

pairs have joint modulus envelope exactly `mathfrak l`, not `mathfrak l^2`.

Character-space multiplicity and conductor size are therefore separate quantities in the adapter.

---

## 7. Finite CRT products: support subsets, not modulus powers

Let `S` be a finite set of distinct oriented Gaussian prime ideals. At every `mathfrak l in S`, attach a pair of local indices

\[
(j_{U,\mathfrak l},j_{V,\mathfrak l}).
\]

Define the active support

\[
\boxed{
\operatorname{Supp}_{UV}
=
\{\mathfrak l:\ (j_{U,\mathfrak l},j_{V,\mathfrak l})\ne(0,0)\}.
}
\tag{H3.10}
\]

For the Stage14 \(\mu_4\)-trivial family,

\[
\boxed{
\mathfrak q_{UV}
=\prod_{\mathfrak l\in\operatorname{Supp}_{UV}}\mathfrak l.
}
\tag{H3.11}
\]

Thus the full family decomposes canonically by an active **support subset**.

No prime ideal receives exponent two merely because both coordinates use it.

For a general arbitrary-order family outside the \(\mu_4\)-trivial specialization, the only extra factor is

\[
(1+i)^{\max(e_{2,U},e_{2,V})},
\]

whose norm is at most `8`. Hence arbitrary unit signatures alter conductor scale only by an absolute constant factor.

---

## 8. Good-modulus condition on a tH2 hyperbola block

Stage14-tH2 gives

\[
N(U)=hr,
\qquad
N(V)=gh\delta.
\]

For a rational split auxiliary prime `p`, the condition that both Gaussian coordinates are units at every prime ideal above `p` is

\[
p\nmid N(U)N(V).
\]

But

\[
N(U)N(V)=g h^2 r\delta.
\]

Therefore

\[
\boxed{
p\nmid N(U)N(V)
\iff
p\nmid ghr\delta.
}
\tag{H3.12}
\]

For a finite support of rational auxiliary primes with radical

\[
Q_{\rm rat}=\prod_{p\in S_{\rm rat}}p,
\]

the joint good-modulus condition is

\[
\boxed{
\gcd(Q_{\rm rat},ghr\delta)=1.
}
\tag{H3.13}
\]

This condition is exact and lives directly on the tH2 transformed variables.

In particular, once a finite state `g` is fixed, sufficiently large auxiliary primes automatically avoid `g`; the remaining coprimality restriction is on the shared factor `h` and the two free hyperbola variables `r,delta`.

---

## 9. Canonical adapter record

Later tH stages should exchange spectral data using the following structure.

```text
GaussianSpectralHyperbolaPacket:
  # tH2 arithmetic block
  epsilon_state
  g
  H, R, D
  sharp_budget: h*r*delta <= Y
  U_norm: h*r
  V_norm: g*h*delta
  balance_ratio: R/(g*D)

  # tH1/tH3 character data
  modulus_groups:
    - gaussian_prime_key: (p,rho)
      U_mode: j_U mod p-1
      V_mode: j_V mod p-1
      U_order
      V_order
      same_modulus_group: true

  U_primitive_conductor
  V_primitive_conductor
  joint_modulus_envelope: lcm(U_conductor,V_conductor)
  active_union_support
  rational_support_radical
  good_block_condition: gcd(rational_support_radical,g*h*r*delta)=1
```

For Stage14 \(\mu_4\)-trivial Mellin packets, every mode satisfies `j_U,j_V == 0 mod 4`, so the two-adic conductor fields are identically zero and may be omitted from the live fast path.

---

## 10. Large-sieve input/output boundary

The exact object presented to a later analytic theorem is now:

```text
arithmetic domain
  = exact/dyadic tH2 hyperbola blocks

character family
  = arbitrary-order oriented Gaussian residue/ray-class modes

conductor scale
  = norm of joint modulus envelope

same-modulus coupling
  = retained by modulus_group_id

good-prime mask
  = gcd(Q_rat,g*h*r*delta)=1
```

A theorem may sum over character pairs, modulus groups, or active-support subsets, but it must not silently replace a shared modulus by two independent modulus variables.

This adapter makes the distinction mechanically visible.

---

## 11. Compatibility with the live t route

Stage14-tH3 does not depend on t34 or t35.

Nevertheless the current merged live route provides a useful compatibility check:

- t34 showed that arbitrary Mellin orders can be handled by an order-free Gaussian large sieve;
- t35 showed that keeping the `U/V` auxiliary modulus shared is essential for the collision geometry.

The tH3 record is intentionally compatible with both facts:

```text
arbitrary order -> preserved
mu4 support -> explicit
same modulus -> preserved
independent modulus tensorisation -> not performed
```

Thus tH3 remains useful if the live t route later changes its signed-trace argument.

```text
TH3_REQUIRES_T34_OR_T35=false
TH3_OPTIONALLY_COMPATIBLE_WITH_T34_T35=true
```

---

## 12. Deterministic audit

The dedicated audit uses

```text
p = 5,13,17,29,37,41
rho = +/-1
```

and checks every local `mu4`-trivial exponent and every same-modulus two-coordinate pair.

Frozen totals:

```text
mu4-trivial local modes checked                         68
nontrivial mu4 local modes                              56
same-modulus mu4 two-coordinate pairs                  512
pairs with joint odd modulus p                         500
trivial/trivial pairs                                    12
same-modulus conductor-squaring violations               0
```

The audit also checks all arbitrary-order `(j_U,j_V)` pairs at those oriented primes:

```text
arbitrary-order same-modulus pairs                    8192
joint e2=0                                             512
joint e2=2                                            1536
joint e2=3                                            6144
```

For two-prime CRT products over

```text
5,13,17,29,37
```

with one fixed orientation, it checks `7518` `mu4`-trivial packet combinations. Their joint-modulus active-support sizes are

```text
support size 0      10
support size 1     604
support size 2    6904
```

Finally, on the tH2 transformed domain with

```text
epsilon in {1,2,3,4,6,8,12}
Y=64
p in {5,13,17,29}
```

it checks `52,420` good-modulus predicates and finds zero failures of

\[
p\nmid N(U)N(V)\iff p\nmid ghr\delta.
\]

---

## Proof boundary

Stage14-tH3 closes the character/conductor **adapter**, not the analytic estimate.

```text
STAGE14_TH3=COMPLETE_ALL_ORDER_RAY_CLASS_HYPERBOLA_CONDUCTOR_ADAPTER
TH_REQUIRES_FUTURE_T_RESULT=false
ALL_ORDER_LOCAL_CHARACTER_RECORD_IMPORTED=true
MU4_TRIVIAL_MODE_IFF_J_MULTIPLE_OF_4=true
MU4_TRIVIAL_FAMILY_TWO_ADIC_CONDUCTOR_EXPONENT_ZERO=true
COORDINATE_PRIMITIVE_CONDUCTORS_PRESERVED=true
JOINT_MODULUS_ENVELOPE_IS_LCM=true
SHARED_AUXILIARY_MODULUS_PRESERVED=true
SHARED_PRIME_JOINT_MODULUS_SQUARED=false
CONJUGATE_GAUSSIAN_PRIMES_REMAIN_DISTINCT=true
FINITE_CRT_ACTIVE_SUPPORT_ADAPTER_PROVED=true
HYPERBOLA_GOOD_MODULUS_CONDITION=gcd(Q_rat,g*h*r*delta)=1
TH3_REQUIRES_T34_OR_T35=false
ALL_CHARACTER_MELLIN_HECKE_LARGE_SIEVE_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH4
```
