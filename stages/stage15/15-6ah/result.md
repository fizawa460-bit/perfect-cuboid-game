# Stage15-6ah — full common-support CRT reduction and small-support boundary

Base: merged Stage15-6ag (`PR #839`, merge commit `fedb3c4`). Stage15-6ag proved a quantitative pair-energy bound when two retained low-core points share at least one sufficiently large good prime, but left pairs with only small or zero extra good overlap open.

Stage15-6ah sharpens that boundary. The correct quantity is not the largest shared prime, but the **full squarefree good common support**. Many individually small shared primes can combine into a large modulus and must be used together before declaring the pair low-overlap.

This stage does not open a genus-one, character, or large-sieve theorem. It exhausts the exact CRT/common-support reduction first.

## 1. Fixed low-core pair notation

Work inside one fixed charged Stage15 low-core physical fiber from 6ac--6ag. Thus

```text
outer pair (m,n)
common squareclass/core/orientations K_alpha,K_beta
cross-gcd labels h_alpha,h_beta
dyadic physical chamber
```

are fixed, with only `B^o(1)` legal decorations already charged.

For each retained primitive Gaussian parameter `z=a+ib`, write

\[
T(z)=h_\alpha\bigl(m^2Y(z)+i n^2X(z)\bigr)
     = C K_\beta w^2,
\qquad C:=mn h_\beta,
\]

where `K_alpha z^2=X+iY`, `N(K_beta)=k`, and 6ad proved that fixed `z` determines `w^2` and fixed `w` reconstructs `z` up to only a finite root/unit fiber.

For two retained points `z_1,z_2`, put

\[
L_+=a_1a_2+b_1b_2,
\qquad
L_-=a_1b_2-b_1a_2.
\]

Merged 6af gives

\[
\Delta_T=-2m^2n^2kL_+L_-.
\]

## 2. Full good common support

Let

\[
J=J(z_1,z_2)
\]

be the squarefree product of the rational norm primes `p` which

1. occur in both square factors `N(w_1)` and `N(w_2)`, and
2. are good for the 6af/6ag transfer, i.e. do not divide the fixed coefficient package or either primitive point norm.

Equivalently, `J` is the good squarefree part of

\[
\gcd(N(w_1),N(w_2)).
\]

The fixed core `K_beta` is **not** part of `J`; it was already charged in 6aa--6ac and AR-028 forbids recharging it.

For each `p|J`, the same-role/cross-role Gaussian orientation is one of finitely many choices. By 6af,

\[
p\mid L_+L_-.
\]

Moreover a good `p` cannot divide both `L_+` and `L_-`, because

\[
L_+^2+L_-^2=(a_1^2+b_1^2)(a_2^2+b_2^2)
\]

and good primes were defined to avoid both primitive point norms.

Hence the support splits uniquely after the finite orientation allocation:

\[
\boxed{J=J_+J_-,\qquad (J_+,J_-)=1,}
\]

with

\[
J_+\mid L_+,
\qquad
J_-\mid L_-.
\]

The number of orientation allocations is at most a fixed power of `2^{omega(J)}` and is therefore `B^o(1)`.

## 3. CRT compression to one primitive root-line

Fix the first point `z_1=(a_1,b_1)`, the modulus `J`, and the split `(J_+,J_-)`.

The second point satisfies

\[
a_1a_2+b_1b_2\equiv0\pmod{J_+},
\]

\[
a_1b_2-b_1a_2\equiv0\pmod{J_-}.
\]

Prime by prime, these are the orthogonal and parallel primitive lines from 6ag. Because `J_+` and `J_-` are coprime, CRT combines the local choices into one primitive rank-one residue line modulo `J`.

The coefficient matrix

\[
\begin{pmatrix}
a_1&b_1\\
-b_1&a_1
\end{pmatrix}
\]

has determinant `a_1^2+b_1^2`, a unit modulo `J` by goodness. Thus no hidden singular residue class is introduced.

Consequently the same primitive root-line lattice estimate underlying AR-009 applies to the full composite modulus. For a dyadic primitive `z_2` rectangle of area scale

\[
W=A_0B_0,
\]

one obtains, after the `B^o(1)` orientation charge,

\[
\boxed{
\#\{z_2:\ J(z_1,z_2)=J\}
\ll B^{o(1)}\left(1+\frac{W}{J}\right).
}
\]

All original physical masks only delete candidates.

## 4. Fixed anchor has only B^o(1) candidate J

For fixed `z_1`, 6ad fixes `w_1` up to `O(1)` roots/units. Every admissible common support `J` divides the squarefree kernel of the polynomially bounded integer `N(w_1)` after removing bad/fixed-core primes.

Therefore

\[
\#\{J\text{ possible for fixed }z_1\}
\le \tau(\operatorname{rad}N(w_1))
=B^{o(1)}.
\]

This is AR-016 divisor accounting only.

Let `E_{J>=L}` count nondegenerate ordered pairs whose full good common support is at least `L`. Summing the composite-modulus root-line bound gives

\[
\boxed{
E_{J\ge L}
\ll \#Z\,B^{o(1)}\left(1+\frac{W}{L}\right).
}
\]

This strictly sharpens the bookkeeping boundary from 6ag: a pair with no large individual shared prime is still controlled if the product of its small shared primes is large.

```text
STAGE15_6AH_FULL_COMMON_SUPPORT_MODULUS=true
STAGE15_6AH_COMPOSITE_SUPPORT_CRT_ROOTLINE=true
STAGE15_6AH_LARGE_TOTAL_SUPPORT_ENERGY_BOUND=true
STAGE15_6AH_LARGE_TOTAL_SUPPORT_BOUND=N*B^o(1)*(1+W/L)
```

## 5. What remains after using the full support

The genuinely unresolved population is now

\[
\boxed{J<L,}
\]

including `J=1`.

This is stronger and cleaner than the 6ag phrase "small-or-zero overlap": all large products of small primes have been removed already.

For fixed anchor `z_1`, fixing a small `J` and its orientation split does not reconstruct `z_2`. It only places `z_2` on an index-`J` primitive residue line. When `J` is small compared with the dyadic area scale, the line bound is of ambient order.

In particular the zero-support branch `J=1` supplies no congruence restriction at all.

```text
STAGE15_6AH_SMALL_TOTAL_SUPPORT_RECONSTRUCTION=false
STAGE15_6AH_ZERO_SUPPORT_CONGRUENCE_RESTRICTION=false
```

## 6. The pair square identity is exact but tautological

Because both points lie in the same fixed square target,

\[
T(z_j)=C K_\beta w_j^2,
\]

we have the exact pair identity

\[
\boxed{
T(z_1)\overline{T(z_2)}
=C^2 k\,(w_1\overline{w_2})^2.
}
\]

Thus after division by the fixed scalar `C^2 k`, the cross-product of the two transfer values is a Gaussian square even when `J=1`.

However this does **not** create a new independent saving. Put

\[
\xi=w_1\overline{w_2}.
\]

For fixed `z_1`, the first point fixes `w_1` up to `O(1)`. Varying `w_2` varies `xi` by a fixed invertible Gaussian multiplication. Conversely fixed `xi` determines `w_2`, and 6ad then reconstructs `z_2` up to only `O(1)`.

Therefore

```text
z_2 <-> w_2 <-> xi
```

is an exponent-preserving finite-fiber reparameterization. The pair square identity is a useful exact normal form, but it is not a new modulus, dimension drop, or density saving.

This is the Stage15 realization of the AR-010/AR-016 reconstruction firewall: renaming the free second point by `xi` cannot be charged as a second theorem.

```text
STAGE15_6AH_PAIR_SQUARE_IDENTITY=true
STAGE15_6AH_PAIR_SQUARE_IDENTITY_INDEPENDENT_SAVING=false
```

## 7. Arsenal accounting

```text
AR-017=FULL_SHARED_SUPPORT_TO_CROSS_RESULTANT_ADAPTER_ACTIVE
AR-009=COMPOSITE_CRT_PRIMITIVE_ROOTLINE_AFTER_SHARED_SUPPORT_FIXED
AR-016=DIRECT_REUSE_FOR_J_DIVISORS_AND_ORIENTATIONS
AR-010=RECONSTRUCTION_FIREWALL_PAIR_SQUARE_REPARAMETERIZATION
AR-028=NO_FIXED_CORE_OR_PRIVATE_ROOT_RECHARGE_PASS
AR-023/024=PHYSICAL_MEASURE_FIREWALL_PASS
AR-012=NOT_TRIGGERED
AR-013=NOT_TRIGGERED
AR-014=NOT_NEEDED
```

Targeted Stage14 comparison: t70 already records the same general lesson that full common support must be used before declaring a small-overlap branch, and that the `J=1` algebraic branch cannot be closed by generic common-support reconstruction alone. This is **negative/structural guidance only**; its fixed-U measure and exponents are not imported.

```text
STAGE14_T70_DIRECT_REUSE=false
STAGE14_T70_STRUCTURAL_ANALOGY=USE_FULL_COMMON_SUPPORT_THEN_SMALL_J_REMAINS
```

## 8. Counting boundary

Stage15-6ah has now exhausted the pair-overlap information available from AR-017 without recharging old support:

```text
degenerate parallel/orthogonal pairs
  -> O(N)                    [6ag]

full good common support J >= L
  -> N*B^o(1)*(1+W/L)       [6ah]

small total common support 1 <= J < L
  -> open

zero common support J=1
  -> open, no congruence modulus
```

The small-total-support branch cannot be made finite by exact reconstruction from the current data. The remaining arithmetic is again the one-point fixed-outer anisotropic Gaussian-square transfer receiver from 6ae, now with the additional information that pairwise common square-factor support is small.

A future theorem may exploit this small-support/coprimality condition, but Stage15-6ah does not open or assume such a theorem.

## 9. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ah
STAGE15_6AH_STARTING_GATE=SMALL_OR_ZERO_EXTRA_OVERLAP
STAGE15_6AH_FULL_COMMON_SUPPORT_MODULUS=true
STAGE15_6AH_COMPOSITE_SUPPORT_CRT_ROOTLINE=true
STAGE15_6AH_FIXED_ANCHOR_J_CHOICES=B^o(1)
STAGE15_6AH_LARGE_TOTAL_SUPPORT_ENERGY_BOUND=true
STAGE15_6AH_LARGE_TOTAL_SUPPORT_BOUND=N*B^o(1)*(1+W/L)
STAGE15_6AH_SMALL_TOTAL_SUPPORT_OPEN=true
STAGE15_6AH_ZERO_SUPPORT_OPEN=true
STAGE15_6AH_PAIR_SQUARE_IDENTITY=true
STAGE15_6AH_PAIR_SQUARE_IDENTITY_INDEPENDENT_SAVING=false
STAGE15_6AH_SMALL_TOTAL_SUPPORT_RECONSTRUCTION=false
STAGE15_6AH_GLOBAL_PAIR_ENERGY_SAVING_PROVED=false
STAGE15_6AH_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AH_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AH_EXIT=FULL_COMMON_SUPPORT_EXHAUSTED_SMALL_TOTAL_SUPPORT_ONE_POINT_GATE_READY
```

## 10. Next narrow gate

Stage15-6ai should return to the surviving **one-point** receiver, now on the small-total-common-support population, and determine its uniform algebraic model before any external theorem search. The natural audit is whether the coupled real quadrics define a uniformly nonsingular genus-one/conic-degenerate family after the already-fixed outer data, with the physical height and coefficient measure written explicitly.

Do not infer a genus-one counting theorem merely from the quartic norm projection; first classify the exact projective model and singular/degenerate coefficient loci.
