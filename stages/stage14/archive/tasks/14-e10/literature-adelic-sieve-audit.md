# Stage14-e10 — literature audit for adelic state laws and completion sieves

Search date: 2026-08-09.

## Scope

Stage14-e10 upgrades the finite six-state ledger of e9 to an adelic limiting law and strengthens the Euler-brick thin-set estimate.  The ambient base is the split toric surface

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad -K_Y=L,\qquad \rho(Y)=6,
\]

with the physical Euclidean height coming from the e6 adelic metric.  The six e9 support states at a prime are

```text
none, G, U, V, GU, GV.
```

The completion locus is the rational image of the degree-two Euler-brick/K3 cover of this toric surface.

Classification vocabulary remains

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```

Absence from the current search is not a novelty certificate.

## 1. Huang v3 — effective adelic equidistribution

Zhizhong Huang, *Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509v3, revised 17 July 2026.

Classification:

```text
HUANG_V3_FIXED_ADELIC_EQUIDISTRIBUTION=THEOREM_LEVEL_INPUT
```

Theorem 1.4 gives an asymptotic formula, with an effective error term and explicit dependence on the finite adelic neighbourhood, for rational points of bounded canonical toric anticanonical height lying in a standard adelic set.  The finite part may be open-closed.  The main theorem also establishes Manin--Peyre equidistribution for smooth proper split toric varieties whose anticanonical line bundle is globally generated.

For e10 this is used only after the e6 local metric calculation.  A fixed finite collection of valuation-state conditions is first truncated at bounded valuation, hence is a finite union of open-closed p-adic sets.  The omitted valuation tail has arbitrarily small local Tamagawa mass.  Passing the truncation bound to infinity gives the exact six-state masses.  Conditions at distinct fixed primes have product Tamagawa mass.  Combining them with one of the e4 real direction chambers shows that the same finite-place law holds in each direction.

The physical adelic norm is not silently identified with Huang's canonical toric norm.  The already-used Manin--Peyre metric invariance for a fixed anticanonical line bundle and the explicit e6 physical local densities provide the metric crosswalk.

## 2. Huang v3 — generically finite fibration image

Same source, Theorem 1.6(1).

Classification:

```text
HUANG_V3_GENERIC_FINITE_LOG_SAVING=THEOREM_LEVEL_INPUT
```

Let `f:Z->Y` be a dominant proper morphism to the above toric base, with `Z` proper, smooth and geometrically integral.  Huang proves that if `f` is generically finite of degree greater than one then the number of toric rational points of height at most `B` lying in the adelic image `f(Z(A_Q))` is

\[
O\!\left(B(\log B)^{\rho(Y)-1-\iota_f}\right)
\]

for a constant `0<iota_f<1` depending on `f`.

The e8 Euler-brick compactification supplies exactly the required map after normalization/minimal resolution:

```text
Z = smooth proper geometrically integral K3 resolution
f: Z -> Y
geometric generic degree = 2
```

Every rational Euler-brick point maps into `f(Z(Q))`, hence into the larger adelic image `f(Z(A_Q))`.  Therefore Huang's upper bound applies to the Euler-brick projection.  Since `rho(Y)=6`, e10 obtains

\[
R_{\rm EB}(B)\ll B(\log B)^{5-\eta_{\rm EB}}
\]

for some `eta_EB in (0,1)`.  The physical and canonical toric heights are fixed multiplicatively comparable, so the logarithmic saving is unchanged by switching to the physical Euclidean cutoff.

Stage14-e10 does **not** evaluate Huang's numerical constant `iota_f` for this cover; that is deliberately left open.

## 3. Batyrev--Tschinkel — toric main term

Victor V. Batyrev and Yuri Tschinkel, *Manin's conjecture for toric varieties*, J. Algebraic Geom. 7 (1998), 15--53; arXiv:alg-geom/9510014.

Classification:

```text
BATYREV_TSCHINKEL_TORIC_MAIN_TERM=REUSABLE_METHOD_PLUS_UPSTREAM_INPUT
```

This is the theorem-level background for the anticanonical `B(log B)^(rho-1)` scale already used in e3/e4/e6.  E10 does not re-prove or re-normalize the global leading constant.

## 4. Browning--Loughran — equidistribution and rational-point sieves

Tim Browning and Daniel Loughran, *Sieving rational points on varieties*, arXiv:1705.01999.

Classification:

```text
BROWNING_LOUGHRAN_RATIONAL_POINT_SIEVE=ADJACENT_RESULT_PLUS_REUSABLE_METHOD
```

Their general framework explains the local-to-global sieve principle: equidistribution lets one impose any fixed finite set of local conditions with Tamagawa-product density, while without stronger uniformity the generic conclusion is qualitative `o(1)` rather than a sharp growing-prime upper bound.  This is exactly the proof boundary retained by the elementary e10 residue sieve.

E10 does not import a quadric-specific Selberg-sieve bound into the present toric/K3 setting.

## 5. Mertens prime product

For the classical prime product theorem we use the standard Mertens formula; a convenient self-contained reference is Mark B. Villarino, *Mertens' Proof of Mertens' Theorem*, arXiv:math/0504289.  Jared Duker Lichtman, *Mertens' prime product formula, dissected*, arXiv:2002.03361, is additional modern context.

Classification:

```text
MERTENS_PRIME_PRODUCT=REUSABLE_METHOD
```

Since e10 proves

\[
\delta_p=\frac2p+O(p^{-2}),
\]

Mertens' theorem gives

\[
\prod_{p\le z}(1-\delta_p)
\sim\frac{C_{\rm sieve}}{(\log z)^2}
\]

for some positive constant `C_sieve`.  No numerical value of this constant is promoted to a theorem in e10.

## 6. Finite-field character identity

For odd `p`, the e10 blocker uses only the elementary quadratic-character identity

\[
\sum_{r\in\mathbf F_p}\chi(r^2+1)=-1.
\]

After removing `r=0` and the possible two roots of `r^2=-1`, the number of nonzero `r` for which `r^2+1` is a nonsquare is

\[
\frac{p-\chi_4(p)}2.
\]

This is proved directly in the e10 result and deterministically checked for every odd prime through `199`; it is not treated as a novelty claim.

## 7. Collision boundary

The general toric equidistribution theorem, the fibration-image logarithmic saving, rational-point sieve philosophy and Mertens product are all existing literature.  The repository-specific work is the crosswalk from the e9 `(g,u,v)` states to the e6 physical p-adic height shells, the resulting closed six-state probabilities, and the explicit residue blocker mass

\[
\delta_p=\frac{2(p-\chi_4(p))}{p^2+6p+1}.
\]

The current search did not locate this exact Stage14 physical-height six-state law or blocker product as a pre-existing cuboid counting statement.  This absence is not used as a novelty certificate.

```text
DIRECT_STAGE14_E10_SIX_STATE_LAW=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
DIRECT_STAGE14_E10_RESIDUE_BLOCKER_PRODUCT=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```
