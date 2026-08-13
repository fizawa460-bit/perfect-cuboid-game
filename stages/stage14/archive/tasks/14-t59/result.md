# Stage14-t59 — exact comparator rectangles for the fixed-U physical selector

## Purpose

Merged Stage14-t58 reduces the dominant fixed-`U` invisible packet to

\[
\sum_{p\ne q}
\left|
\sum_{\substack{\ell\delta\le Y_U\\
\ell\ \mathrm{canonical\ split\ prime}}}
\sum_{s\in C_U(\ell,\delta)}
 w_s K_{pq}(t_s,x_s)
\right|^2
\ll P^2 B^{o(1)}\sum_s|w_s|^2,
\tag{59.1}
\]

with the physical mask/lift coefficient energy already proved safe.  The remaining issue is that the actual selector is not one Cartesian product in the `(pi,V)` coordinates.

Stage14-t59 does not try to force a false tensor product.  Instead it uses two exact order relations already present in the physical reconstruction and decomposes the selector into only `B^{o(1)}` **families of pairwise-orthogonal Cartesian rectangles**, with a further aspect-ratio refinement that preserves the actual physical mass at the `L2` level.

This removes the arbitrary-selector ambiguity from the invisible fixed-`U` receiver.  The missing analytic theorem is now a same-modulus bilinear second moment on energy-balanced orthogonal rectangle families.

No global Stage14 power saving is claimed here.

---

## 1. Reciprocal quotient removes the second archimedean inequality

The t42 reciprocal quotient, used throughout t54--t58, chooses the representative

\[
0<x=\frac pq<1.
\]

The direction chart has

\[
0<t=\frac ab<1.
\]

The physical chamber is

\[
t<x<1/t.
\]

Since `x<1<1/t`, the upper inequality is automatic.  Therefore on the live reciprocal invisible packet

\[
\boxed{\mathbf 1_{\rm chamber}=\mathbf 1_{t<x}.}
\tag{59.2}
\]

This is stronger than the t58 statement `u>1, v<1`: after quotienting the reciprocal symmetry, the complete cross-angular selector is a single strict comparator between a direction-side scalar `t(pi)` and a cover-side scalar `x(V)`.

The frozen audit checks `p<q` for all 560 reciprocal states and verifies (59.2) on all of them.

```text
RECIPROCAL_QUOTIENT_X_LT_1=true
PHYSICAL_CHAMBER_REDUCES_TO_SINGLE_COMPARATOR=true
```

---

## 2. In the current super-square-root branch, invisibility has no residual cross mask

The current t route remains in the canonical super-square-root regime

\[
\ell^2>4B.
\tag{59.3}
\]

Merged t37 gives, from the exact physical budget,

\[
\frac{\varepsilon\ell m\delta}{2}\le B,
\qquad N(V)=n=k\delta,
\qquad k\le \varepsilon m,
\]

that

\[
\boxed{\ell>2\varepsilon m\delta\ge2N(V).}
\tag{59.4}
\]

Hence on the invisible branch

\[
\ell\nmid N(V)
\]

is automatic once the physical hyperbola is satisfied.  It is not an additional moving `(pi,V)` incidence in this regime.

Thus, after fixing primitive `U`, finite `epsilon`, divisor-fan `k`, and the invisible branch, the only genuinely cross-side support conditions are

\[
\boxed{t(\pi)<x(V)}
\tag{59.5}
\]

and

\[
\boxed{\ell(\pi)\le \frac{Y_U}{\delta(V)},
\qquad Y_U=\frac{2B}{\varepsilon N(U)}.}
\tag{59.6}
\]

All canonical/prime/orientation conditions restrict the `pi` side, while primitive-cover conditions restrict the `V` side.

The frozen audit reconstructs **every one of the 419 invisible reciprocal states exactly** from these two comparators inside the eight fixed `(U,epsilon,k)` packets; no extra cross-side condition is needed.

```text
SUPER_SQRT_INVISIBLE_COPRIMALITY_AUTOMATIC=true
FIXED_U_INVISIBLE_SUPPORT_EQUALS_TWO_COMPARATOR_INTERSECTION=true
```

---

## 3. Exact dyadic comparator lemma

Let `A,B` be finite sets and let

\[
L:A\to\mathbb R,
\qquad R:B\to\mathbb R.
\]

Consider the strict comparator support

\[
\mathcal S_{<}=\{(a,b):L(a)<R(b)\}.
\]

Rank the distinct scalar values in increasing order, obtaining leaf indices

\[
0,1,\dots,M-1,
\]

and pad to the next power of two.  For one admissible pair with ranks `i<j`, let `b` be the highest binary bit on which `i` and `j` differ.  Then:

- the higher bits are a common prefix;
- the `b`-bit of `i` is `0`;
- the `b`-bit of `j` is `1`.

Therefore the pair belongs to the unique dyadic node whose left child contains `i` and right child contains `j` at their first differing bit.

This gives the exact disjoint decomposition

\[
\boxed{
\mathcal S_{<}
=\bigsqcup_{d}
\bigsqcup_{\nu\in\mathcal N_d}
A_{d,\nu}^{\rm L}\times B_{d,\nu}^{\rm R}.
}
\tag{59.7}
\]

For each fixed depth `d`, the left projections are pairwise disjoint and the right projections are pairwise disjoint.

For a non-strict relation `L(a)<=R(b)`, tag equal values by placing the left copy immediately before the right copy in the total order.  Then `<=` becomes a strict comparison of tagged ranks and the same lemma applies exactly.

If the input cardinalities are `B^{O(1)}`, the binary-tree depth is

\[
O(\log B).
\tag{59.8}
\]

No Fourier completion, Perron truncation, smoothing, or boundary error is involved.

```text
FINITE_COMPARATOR_EXACT_DYADIC_RECTANGLE_DECOMPOSITION_PROVED=true
COMPARATOR_RECTANGLE_DEPTH_COUNT=O(log_B)
SHARP_COMPARATOR_APPROXIMATION_ERROR=0
```

---

## 4. Apply the lemma to both physical comparators

For one fixed `(U,epsilon,k)` invisible packet, take the row variable to be the canonical direction/prime object `pi` and the column variable to be the primitive cover object `V`.

### Comparator A: physical chamber

Use

\[
L_1(\pi)=t(\pi),
\qquad R_1(V)=x(V),
\]

with the strict relation

\[
L_1<R_1.
\]

By (59.2), this is exactly the reciprocal physical chamber.

### Comparator B: sharp physical hyperbola

Use

\[
L_2(\pi)=\ell(\pi),
\qquad R_2(V)=\frac{Y_U}{\delta(V)},
\]

with

\[
L_2\le R_2.
\]

The tagged comparator convention includes exact boundary states with no half-weight and no error.

Each physical pair receives one dyadic node from comparator A and one from comparator B.  Fixing the two depths `(d_1,d_2)`, intersect the corresponding row and column child sets.  Since intersections of Cartesian products remain Cartesian,

\[
(A_1\times B_1)\cap(A_2\times B_2)
=(A_1\cap A_2)\times(B_1\cap B_2).
\]

Moreover, at fixed `(d_1,d_2)`, the nonempty intersections have pairwise-disjoint row projections and pairwise-disjoint column projections.

Therefore the complete physical selector is an exact disjoint union of only

\[
O((\log B)^2)
\]

**orthogonal rectangle families**.

```text
TWO_COMPARATOR_INTERSECTION_RECTANGULARIZES_EXACTLY=true
ORTHOGONAL_RECTANGLE_LEVEL_PAIR_COUNT=O((log_B)^2)
RECTANGLE_COUNT_ITSELF_NOT_CHARGED=true
```

The last line is important: there may be many rectangles, but they are not recombined by a Cauchy factor equal to their count.  At a fixed depth pair they form a block-diagonal support matrix with disjoint row and column projections.

---

## 5. Aspect-ratio refinement preserves the physical `L2` mass

Let one orthogonal rectangle family be

\[
\mathcal R=\{A_j\times B_j\}_j,
\]

with

\[
a_j=|A_j|,
\qquad b_j=|B_j|.
\]

Its physical mass is

\[
R_{\mathcal R}=\sum_j a_jb_j.
\tag{59.9}
\]

Partition the rectangles by the dyadic aspect ratio

\[
2^h\le \frac{a_j}{b_j}<2^{h+1}.
\tag{59.10}
\]

There are only `O(log B)` nonempty aspect bins.  Inside one bin,

\[
a_j^2\le 2^{h+1}a_jb_j,
\qquad
b_j^2\le 2^{-h}a_jb_j.
\]

Hence

\[
\boxed{
\left(\sum_j a_j^2\right)
\left(\sum_j b_j^2\right)
\le2R_{\mathcal R}^2.
}
\tag{59.11}
\]

Equivalently,

\[
\boxed{
\sqrt{\sum_j a_j^2}
\sqrt{\sum_j b_j^2}
\le\sqrt2\,R_{\mathcal R}.}
\tag{59.12}
\]

This is the exact energy ledger needed for a bilinear second-moment theorem: after balancing, the product of the two one-side `L2` size budgets is controlled by the **actual selected physical mass**, not by the ambient Cartesian product size.

Combining two comparator depths with one aspect bucket gives only

\[
\boxed{O((\log B)^3)=B^{o(1)}}
\tag{59.13}
\]

energy-balanced orthogonal rectangle families.

```text
ASPECT_RATIO_REFINEMENT_COUNT=O(log_B)
BALANCED_RECTANGLE_ENERGY_PRODUCT_LE_2_R2=true
AMBIENT_CARTESIAN_MASS_SUBSTITUTED_FOR_PHYSICAL_MASS=false
```

---

## 6. Frozen exact-support audit

On the merged frozen reciprocal family:

```text
reciprocal states                  560
invisible states                   419
fixed (U,epsilon,k) packets          8
sum row objects across packets     222
sum cover objects across packets    33
exact intersection rectangles      127
energy-balanced rectangle families 109
max comparator tree depth            7
max rectangles in one family         4
support reconstruction failures      0
rectangle Cartesian failures         0
orthogonality failures                0
energy-balance failures               0
```

Per packet:

```text
U=(-1,0), eps=2, k=1:   states 131, rows 75, cols 7, rectangles 27, families 25
U=(-1,0), eps=2, k=2:   states  86, rows 52, cols 6, rectangles 33, families 26
U=(-1,-1),eps=1, k=1:   states  96, rows 39, cols 7, rectangles 29, families 23
U=(-1,-1),eps=1, k=2:   states  64, rows 29, cols 6, rectangles 21, families 19
U=(-2,1), eps=2, k=5:   states  13, rows  8, cols 2, rectangles  6, families  5
U=(-2,-1),eps=2, k=5:   states  20, rows 12, cols 2, rectangles  6, families  6
U=(-2,-1),eps=2, k=10:  states   7, rows  5, cols 2, rectangles  4, families  4
U=(-2,1), eps=2, k=10:  states   2, rows  2, cols 1, rectangles  1, families  1
```

These are finite diagnostics.  The asymptotic theorem is the exact comparator decomposition plus the logarithmic depth bound and (59.11).

---

## 7. Interaction with the t57 Kummer/Mellin packet

On one Cartesian rectangle `A_j x B_j`, the t57 local mode

\[
(\xi\eta^{-1})(t)\,(\eta\xi)(x)
\tag{59.14}
\]

separates exactly between the direction and cover coordinates:

\[
\sum_{\pi\in A_j}\alpha(t(\pi))
\quad\times\quad
\sum_{V\in B_j}\beta(x(V)).
\tag{59.15}
\]

Thus after t59 the physical support no longer enters the analytic theorem as an arbitrary two-dimensional subset.  It enters as a `B^{o(1)}` collection of energy-balanced **block-diagonal bilinear packets**, while the common auxiliary modulus from tH3/tH4 remains common.

This does not license the forbidden operation

```text
same shared modulus
 -> independent modulus on pi side
 -> independent modulus on V side.
```

The two sides are separated only in coefficient support.  The auxiliary `(p,q)` index remains the same on both sides.

```text
RECTANGLE_LOCAL_MELLIN_MODE_FACTORIZATION_PROVED=true
SHARED_AUXILIARY_MODULUS_PRESERVED=true
INDEPENDENT_PI_V_MODULUS_TENSORIZATION_ALLOWED=false
```

---

## 8. New minimal analytic receiver

Define

```text
SharedUEnergyBalancedOrthogonalRectangleSecondMoment
```

as follows.

For every fixed primitive `U`, finite `epsilon`, divisor-fan `k`, invisible branch, and every t59 rectangle family

\[
\mathcal R=\{A_j\times B_j\}_j
\]

with disjoint row/column projections and one dyadic aspect-ratio bin, prove uniformly

\[
\boxed{
\sum_{p\ne q}
\left|
\sum_j
\sum_{\pi\in A_j}
\sum_{V\in B_j}
K_{pq}(t(\pi),x(V))
\right|^2
\ll
P^2
\left(\sum_j|A_j||B_j|\right)
B^{o(1)}.
}
\tag{59.16}
\]

The theorem may retain all t57 spectral coefficients and all tH3/tH4 conductor labels.  It must not pay for the number of rectangles; the only legal size budget is the physical mass plus `B^{o(1)}` roadworks factors.

If (59.16) holds, then summing the `O((log B)^3)` t59 families by Cauchy costs only `B^{o(1)}` and proves the t58 receiver

```text
SharedUCanonicalPrimeDeltaToroidalSecondMoment.
```

Consequently t57, t56 and tH15 then close the dominant invisible fixed-`U` squareclass energy.

This receiver is strictly narrower than t58:

- arbitrary two-dimensional selector: removed;
- sharp chamber approximation: removed;
- sharp hyperbola approximation: removed;
- support-energy transfer: already closed by t58;
- remaining issue: same-modulus bilinear cancellation on orthogonal Cartesian blocks.

```text
SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
```

---

## 9. Why the previous 3-of-4 rectangle witness is no longer a blocker

The t58 witness

```text
1 1
1 0
```

correctly disproves a **single** Cartesian-product selector.  It does not contradict t59.

A triangular/order selector is expected to contain such `3/4` minors.  The comparator lemma decomposes it by the first binary scale at which the row and column ranks separate.  The support is therefore not rank one, but it has a polylogarithmic number of orthogonal **levels**, and each physical pair is assigned exactly once.

Thus the t58 guard remains valid while its obstruction is sharpened from

```text
non-Cartesian selector
```

to

```text
energy-balanced orthogonal-rectangle bilinear second moment.
```

No contradiction or stale boundary remains.

---

## 10. tH decision

`tH16` remains needed; no `tH17` is created.

The t58 request asked tH16 to analyze the broad

```text
SharedUCanonicalPrimeDeltaToroidalSecondMoment.
```

Stage14-t59 supplies a strictly sharper theorem shape.  The tH16 task should now be interpreted as:

```text
attack SharedUEnergyBalancedOrthogonalRectangleSecondMoment;
keep the common auxiliary modulus common;
use the exact t57 rank-one Kummer/Mellin packet on each rectangle;
exploit disjoint row/column projections and the balance identity
sqrt(sum |A_j|^2 * sum |B_j|^2) <= sqrt(2) * physical_mass;
do not pay a factor equal to the number of rectangles;
do not collapse state pairs to squareclass/E4 coefficients.
```

Possible analytic routes remain same-modulus trace/bilinear large sieve, reciprocity, or a hybrid fourth-moment estimate, but t59 does not claim any of them already proves (59.16).

The t route is not blocked waiting for tH16.

```text
TH16_NEEDED=true
TH16_REQUESTED_OBJECT=SharedUEnergyBalancedOrthogonalRectangleSecondMoment
TH17_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH16=false
```

---

## Locked boundary

```text
STAGE14_T59=COMPLETE_EXACT_TWO_COMPARATOR_ORTHOGONAL_RECTANGLE_REDUCTION
MERGED_T58_IMPORTED=true
RECIPROCAL_QUOTIENT_X_LT_1=true
PHYSICAL_CHAMBER_REDUCES_TO_SINGLE_COMPARATOR=true
SUPER_SQRT_INVISIBLE_COPRIMALITY_AUTOMATIC=true
FIXED_U_INVISIBLE_SUPPORT_EQUALS_TWO_COMPARATOR_INTERSECTION=true
FINITE_COMPARATOR_EXACT_DYADIC_RECTANGLE_DECOMPOSITION_PROVED=true
TWO_COMPARATOR_INTERSECTION_RECTANGULARIZES_EXACTLY=true
ORTHOGONAL_RECTANGLE_LEVEL_PAIR_COUNT=O((log_B)^2)
ASPECT_RATIO_REFINEMENT_COUNT=O(log_B)
BALANCED_RECTANGLE_ENERGY_PRODUCT_LE_2_R2=true
TOTAL_ENERGY_BALANCED_RECTANGLE_FAMILY_COUNT=O((log_B)^3)
RECTANGLE_LOCAL_MELLIN_MODE_FACTORIZATION_PROVED=true
SHARED_AUXILIARY_MODULUS_PRESERVED=true
INDEPENDENT_PI_V_MODULUS_TENSORIZATION_ALLOWED=false
SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false
SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH16_NEEDED=true
TH16_REQUESTED_OBJECT=SharedUEnergyBalancedOrthogonalRectangleSecondMoment
TH17_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH16=false
NEXT=Stage14-t60 attack SharedUEnergyBalancedOrthogonalRectangleSecondMoment directly; consume tH16 if available and test same-modulus bilinear/fourth-moment estimates on the exact orthogonal rectangle packet
```