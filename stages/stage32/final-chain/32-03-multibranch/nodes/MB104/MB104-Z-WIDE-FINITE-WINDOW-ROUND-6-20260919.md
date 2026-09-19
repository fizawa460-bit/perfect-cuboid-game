# Stage32 32-03 — Z-wide population finite-window scan, Round 6 (Z26-Z30) — 2026-09-19

Status: **FINAL BREADTH ROUND COMPLETE / WHOLE R29-LG2-MB POPULATION / NO MATHEMATICAL CREDIT**

## Scope

This is the final planned breadth batch. Each route receives one shallow hostile test only. Balanced `000707` may kill a proposed population-wide mechanism, but no route is deepened inside this round.

Archive-semantic replay found no retained W/U/Z leaf explicitly testing the five architectures below.

---

## Z26 — fixed orbifold-cover / Lattès-Hurwitz classification

**Result: HARD generic / packet-sensitive refinement absorbed by Z5'.**

The active balanced e=2 factor map retained in H6 is

```text
psi:E -> P1,
deg psi = n = 28l,
```

ramified only over eight fixed target values, with simple ramification and aggregate data

```text
u_q + 2r_q = n,
sum_q u_q = 112l = 4n,
sum_q r_q = 56l = 2n.
```

A tempting theorem shape is to regard the eight target points as order-two orbifold points and hope that fixed orbifold branch support plus genus(E)=1 bounds `n`.

The orbifold Euler-characteristic gate is exactly saturated instead.

Target orbifold:

```text
(P1; 2,2,2,2,2,2,2,2)
chi_orb = 2 - 8(1-1/2) = -2.
```

At a ramified preimage, local degree 2 absorbs the target order. Each unramified preimage over an order-two target point must itself carry order two in the source orbifold. There are

```text
U = sum_q u_q = 4n
```

such points, so

```text
chi_orb(source)
= chi(E) - U(1-1/2)
= -2n
= n * chi_orb(target).
```

Thus orbifold Riemann-Hurwitz is an exact equality for every `l`; source orbifold complexity grows linearly with degree. The map is not a fixed parabolic `(2,2,2,2)` Lattès cover whose source has no growing orbifold marking.

More generally, fixed target branch support alone cannot bound degree for genus-one covers: isogeny followed by the quotient `E -> E/{±1} ~= P1` gives unbounded-degree covers with fixed four-point branch support. Therefore any successful cuboid refinement must use the exact eight-value passport/packet allocation, not generic Hurwitz/orbifold-cover theory.

Disposition:

```text
generic fixed-branch/orbifold classification = HARD
cuboid passport-sensitive refinement = Z5'
```

---

## Z27 — KSBA bounded stable-pair compactness after scaling the carrier

**Result: HARD.**

A different compactness idea is to encode a high-degree carrier as a stable pair with a small coefficient and invoke boundedness of stable pairs.

On the balanced canonical model the divisor class is numerically

```text
C_l ~= 7l K_X.
```

To keep the log canonical polarization/volume in a fixed numerical range one is forced to scale the coefficient like

```text
epsilon_l = 1/l,
K_X + epsilon_l C_l ~= 8K_X.
```

This defeats the standard bounded-pair architecture in two ways.

1. The coefficient set `{1/l}` has an infinite strictly decreasing sequence tending to zero, so it is not a fixed DCC coefficient set bounded away from zero.
2. If instead one fixes any positive coefficient `epsilon`, then
   `(K_X+epsilon C_l)^2` grows quadratically with `l`, so the pairs do not lie in one fixed-volume bounded moduli problem.

This is not a technical artifact: on any fixed polarized variety, divisors `C_l in |lL|` with coefficient `1/l` have bounded weighted numerical class while their unweighted degree is unbounded. Pair compactness at shrinking coefficient therefore cannot recover an upper bound for the degree of the support.

Disposition: `HARD`.

---

## Z28 — Cartan / Nevanlinna Second Main Theorem for canonical hyperplanes

**Result: HARD generic / any useful cuboid-specific enhancement folds into Z12.**

The normalization carries the seven canonical coordinate sections and hence a map to `P6`. A natural analytic/function-field route is Cartan's Second Main Theorem for hyperplanes.

For a linearly nondegenerate map to `P^N` and `q` hyperplanes in general position, the degree/characteristic term appears with coefficient

```text
q - N - 1.
```

The canonical coordinate package has

```text
N=6,
q=7,
q-N-1=0.
```

So the seven native coordinate hyperplanes sit exactly at the zero-coefficient threshold: generic Cartan SMT gives no positive global degree term to compare against branch/contact counting.

The four defining quadrics cannot be added as targets because the carrier lies in them identically. Any stronger application would need additional cuboid-specific divisors/hyperplanes in suitable subgeneral position together with a truncation/ramification estimate strong enough to beat the balanced contact mass. That is no longer generic SMT; it is effectively a special higher-jet/symmetric-differential construction and belongs to Z12.

Reference shape: classical Cartan SMT has coefficient `q-N-1` for hyperplanes in general position.

Disposition:

```text
generic canonical-hyperplane SMT = HARD
special extra-target/jet refinement = ABSORB INTO Z12
```

---

## Z29 — K-stability / valuative stability of the canonical model

**Result: HARD as an existence cutoff.**

The canonical model is the natural place to ask whether stability of the canonically polarized surface forbids very singular high pluricanonical low-genus divisors.

Canonically polarized varieties are K-stable, and modern valuative formulations even give uniform valuative stability under standard singularity hypotheses. But this is a stability statement about the polarized variety and its valuations/test configurations; it does not prohibit effective divisors in high multiples of the polarization.

The balanced hostile ray makes the mismatch exact:

```text
C_l ~= 7l K_X.
```

Any numerical slope/valuative test that sees only the divisor class therefore sees an ordinary sequence of positive multiples of `K_X`. High pluricanonical divisors are expected to exist and K-stability is compatible with them. To detect the normalization genus, the stability construction must be upgraded to a pair `(X,c_l C_l)` with singularity-sensitive coefficients; scaling `c_l` to keep the pair bounded returns to the Z27/Z25 coefficient/lct wall.

Reference shape: canonically polarized varieties are uniformly K/valuatively stable; this does not imply bounded degree of effective pluricanonical divisors.

Disposition: `HARD`.

---

## Z30 — Miyaoka aggregate counting of rational/elliptic canonical degree

**Result: HARD on the smooth resolution / PROMISING ONLY THROUGH THE SAME ORBIFOLD EXTENSION AS Z2.**

Miyaoka's 2009 aggregate theorem is unusually close to the desired population statement. For a smooth canonically embedded surface, put

```text
sigma = c2/K^2.
```

His Proposition B bounds weighted counts of rational curves of degree at most `N` under

```text
sigma < 1 + 4/N + 6/N^2,
```

and bounds the total canonical degree of elliptic curves when `sigma<1`.

### Smooth-resolution gate

For the cuboid resolution,

```text
K^2=16,
c2=80,
sigma=5.
```

The elliptic hypothesis `sigma<1` fails. For rational curves, `N=1` is allowed because `5<11`, but already

```text
N=2: 1+4/2+6/4 = 4.5 < 5,
```

so the theorem gives no unbounded-degree rational cutoff. Therefore the smooth theorem is HARD for 32-03.

### Orbifold diagnostic

For the singular canonical model retained in Z2,

```text
K_X^2=16,
c2_orb(X)=8,
sigma_orb=1/2.
```

If — and only if — one had a source-valid orbifold/klt analogue of Miyaoka Proposition B for the actual singular cuboid model and multibranch curves, the formal asymptotic constant would become

```text
((3 sigma_orb - 1)/(1 - sigma_orb)) K_X^2
= ((3/2 - 1)/(1/2))*16
= 16.
```

That would be far stronger than needed: it would give a fixed total canonical-degree budget for low-genus curves.

But substituting `c2_orb` into a theorem stated for smooth canonically embedded surfaces is not valid. Establishing precisely such an orbifold theorem and its curve adapter is the already-retained Z2 problem.

Reference: Yoichi Miyaoka, *Counting Lines and Conics on a Surface*, Publ. RIMS 45 (2009), Proposition B.

Disposition:

```text
smooth aggregate theorem = HARD
orbifold aggregate theorem shape = ABSORBED BY Z2
Z2 priority = materially strengthened
```

---

## Round-6 disposition

```text
Z26 HARD generic / packet refinement -> Z5'
Z27 HARD
Z28 HARD generic / special refinement -> Z12
Z29 HARD
Z30 HARD smooth / orbifold version -> Z2

new independent population-wide closer = none
planned breadth Z1-Z30 = COMPLETE
```

No route is deepened here.

## Firewalls

```text
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
finite_picard_enumeration_released=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
