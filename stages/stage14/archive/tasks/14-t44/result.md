# Stage14-t44 — canonical-prime twist-support routing and generic cross-good Kummer reduction

## Purpose

Stage14-t43 showed that the frozen principal excess and heavy nonprincipal squareclass energy are not explained by degree-1/2 elliptic correspondences.  The remaining live object is the genuinely generic twisted-Kummer incidence

\[
K^{(\tau)}_{\gamma,\gamma'}:\qquad
Y^2=\tau f_\gamma(x)f_{\gamma'}(y).
\]

Stage14-t44 inserts the canonical super-square-root prime into this incidence.  The main point is an exact support dichotomy:

- for a principal collision with two distinct canonical primes, each canonical prime is automatically absent from the other state's physical value;
- for a nonprincipal twist, if a foreign canonical prime does enter the other state's physical value, that prime is forced into the squarefree twist `tau`.

Thus bad cross-support is not part of the genuinely generic Kummer surface.  It is a twist-supported exceptional slice with only `O(1)` possible super-square-root canonical primes for a fixed twist.

No critical-strip power saving is claimed here.

---

## 1. Own canonical-prime valuation is always even

For a Stage14 state let

\[
F=g_1g_2g_3g_4,
\]

with the t28 four linear factors.  Let `ell>2sqrt(B)` be the canonical D/sum prime.

### Invisible branch

By definition no `g_i` is divisible by `ell`, hence

\[
\boxed{v_\ell(F)=0.}
\tag{44.1}
\]

### Visible branch

The t29 matching and t31 size argument give exactly two matched factors divisible by `ell`, each with valuation one.  Hence

\[
\boxed{v_\ell(F)=2.}
\tag{44.2}
\]

Therefore in every branch

\[
\boxed{v_\ell(F)\equiv0\pmod2.}
\tag{44.3}
\]

This is a squareclass statement: the state's own canonical prime never appears in `[F]`.

---

## 2. A distinct foreign canonical prime can occur in at most one factor

Take another active state with direction discriminant support

\[
\Delta=2ab(b^2-a^2)(a^2+b^2).
\]

The t29 determinant/gcd routing gives

\[
\gcd(g_i,g_j)\mid\Delta\qquad(i\ne j).
\tag{44.4}
\]

Let `lambda>2sqrt(B)` be a canonical prime belonging to a different state.  If `lambda` divided two of the present state's `g_i`, then `lambda|Delta`.

The t30 prime-size gates show that a prime above `2sqrt(B)` cannot lie in the `a`, `b`, or `b^2-a^2` columns; it can only lie in the sum column `a^2+b^2`.  Since `a^2+b^2<=2B` on the physical scale, there cannot be two distinct prime divisors both exceeding `2sqrt(B)`.  Hence a distinct foreign canonical prime cannot divide `Delta`.

Therefore it divides at most one `g_i`.  Also t31 gives

\[
|g_i|<2B<\lambda^2,
\]

so

\[
\boxed{v_\lambda(F)\in\{0,1\}}
\tag{44.5}
\]

for a distinct foreign canonical prime.

---

## 3. Principal collisions are automatically cross-good when the canonical primes differ

Suppose

\[
[F_x]=[F_y]
\]

and their canonical primes satisfy

\[
\ell_x\ne\ell_y.
\]

Then `F_x/F_y` is a rational square, so for every rational prime the two valuations have the same parity.

At `ell_x`, equation (44.3) gives an even valuation on `F_x`, while (44.5) gives valuation `0` or `1` on `F_y`.  Parity forces the latter to be zero.  Symmetrically,

\[
\boxed{
\ell_x\nmid F_y,
\qquad
\ell_y\nmid F_x.
}
\tag{44.6}
\]

Thus every principal off-direction pair with distinct canonical primes lies in the **cross-good** Kummer family.  Cross-support degeneracy is impossible there.

The only canonical-prime support exception for the principal energy is therefore the same-`ell` slice.

---

## 4. Nonprincipal cross-bad primes are forced into the twist

For a general pair define

\[
\tau=\operatorname{sqf}(F_xF_y).
\]

Again take distinct canonical primes.  At `ell_x`, the own valuation of `F_x` is even, and the foreign valuation on `F_y` is `0` or `1`.  Hence

\[
\boxed{
\ell_x\mid\tau
\iff
v_{\ell_x}(F_y)=1.
}
\tag{44.7}
\]

and likewise with `x,y` interchanged.

So a foreign canonical prime entering the partner value is not an uncontrolled Kummer degeneracy: it is **visible in the squarefree twist support**.

This gives the exact split

```text
generic cross-good:
    ell_x != ell_y,
    ell_x does not divide F_y,
    ell_y does not divide F_x

exceptional same-prime:
    ell_x = ell_y

exceptional twist-supported cross-bad:
    ell_x != ell_y and one foreign ell divides the partner F;
    that ell necessarily divides tau
```

---

## 5. Fixed twist exposes only O(1) super-square-root canonical primes

T40 gives the safe physical bound

\[
|F|\le256B^4.
\]

Therefore

\[
\tau\le |F_xF_y|\le2^{16}B^8.
\tag{44.8}
\]

If `r` distinct prime divisors of `tau` are all larger than `2sqrt(B)`, then

\[
(2\sqrt B)^r\le2^{16}B^8.
\]

Hence

\[
\boxed{
\omega_{p>2\sqrt B}(\tau)\le16+o(1).
}
\tag{44.9}
\]

Thus for each fixed twist, the cross-bad part can involve only `O(1)` canonical-prime slices.  This is the correct interface for a future fixed-`ell` / heavy-light estimate.

Equation (44.9) does **not** by itself prove a power saving: one still needs a bound for the mass carried by each exposed canonical-prime slice.

---

## 6. Frozen audit

Using the reciprocal quotient of the t36 frozen population:

```text
H* = 560
own invisible canonical valuation v_ell(F)=0    419
own visible   canonical valuation v_ell(F)=2    141
```

### Principal blocks

The 16 off-direction principal blocks split as

```text
distinct canonical ell                 14
distinct ell and cross-good            14
same canonical ell                       2
```

All 14 distinct-prime blocks satisfy (44.6) exactly.

### All off-direction pairs

```text
pairs                                309,906
same ell                               3,490
distinct-ell cross-good              305,334
distinct-ell cross-bad                 1,082
twist-support routing checks           1,084
```

The two counts `1082` and `1084` differ because two foreign canonical primes can be routed in a single ordered pair.

### Heavy nonprincipal tail (`c(tau)>20`)

```text
heavy kernels                             72
heavy pair mass                         1834

distinct-ell cross-good mass            1816
distinct-ell cross-bad mass                0
same-ell mass                              14
same-direction mass                         4
```

The top eight heavy kernels are

```text
91:40, 209:38, 286:34, 34034:34,
41:32, 329:32, 4641:32, 11:30
```

and every one has zero cross-bad mass.

Thus the frozen heavy tail is **not** generated by canonical-prime support collisions.  It lies almost entirely in the genuinely generic distinct-prime cross-good Kummer family.

The largest number of observed super-square-root canonical primes exposed by any one frozen twist is `4`, consistent with the general `O(1)` support bound (44.9).

---

## 7. What t44 closes and what it does not

Closed:

- own canonical-prime valuation is always even;
- a distinct foreign canonical prime is one-factor/valuation-`<=1`;
- principal distinct-canonical-prime collisions are automatically cross-good;
- every nonprincipal cross-bad foreign canonical prime is forced into `tau`;
- a fixed twist exposes only `O(1)` super-square-root canonical primes;
- the frozen heavy tail has zero cross-bad mass.

Still open:

- an aggregate bound for the generic distinct-prime cross-good Kummer incidence;
- a power-saving estimate for the same-`ell` exceptional slice;
- a power-saving estimate for twist-supported cross-bad slices;
- global principal/fourth energy saving;
- critical-square-root-strip saving;
- `A_{1,1}` power saving and `T(B)=o(sqrt(B))`.

The next live stage should attack the cross-good family by using the two **distinct, good canonical primes** as arithmetic moduli rather than treating the Kummer surface as a featureless two-dimensional variety.

---

## tH handoff

`tH` should be reopened as **Stage14-tH12**.

Requested roadwork:

```text
Build a reusable receiver for the generic cross-good twisted-Kummer family.
Do not assume a future t44 theorem beyond already merged/stable inputs.

Study three decompositions:
1. fixed common-core / moving canonical prime;
2. fixed canonical prime / moving common-core;
3. tH10 heavy/light kernel mass with two good canonical moduli.

Try to convert the cross-good two-prime condition into a reusable
quadratic-character, Gaussian-Dirichlet-symbol, lattice-incidence, or
multi-modulus dispersion packet.  Explicitly stress-test quantifiers and
record countermodels when local/fiber bounds do not globalize.
```

```text
STAGE14_T44=COMPLETE_CANONICAL_PRIME_TWIST_SUPPORT_ROUTING_AND_GENERIC_CROSS_GOOD_REDUCTION
CANONICAL_OWN_VALUATION_EVEN=true
PRINCIPAL_DISTINCT_ELL_CROSS_SUPPORT_GOOD=true
NONPRINCIPAL_CROSS_BAD_PRIME_ROUTES_INTO_TWIST=true
FIXED_TWIST_SUPER_SQRT_EXPOSED_CANONICAL_PRIMES=O(1)
FROZEN_HEAVY_CROSS_BAD_MASS=0
GENERIC_CROSS_GOOD_KUMMER_REMAINS_PRIMARY=true
CROSS_BAD_HEAVY_MASS_POWER_SAVING_PROVED=false
GENERIC_CROSS_GOOD_KUMMER_INCIDENCE_BOUND_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t45 attack the distinct-canonical-prime cross-good Kummer incidence by a two-canonical-prime quadratic-character/dispersion receiver; treat same-ell and tau-supported cross-bad pieces as exceptional slices
```
