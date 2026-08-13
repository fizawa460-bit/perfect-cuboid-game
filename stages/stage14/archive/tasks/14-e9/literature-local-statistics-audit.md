# Stage14-e9 — literature refresh for gcd/lcm and local-statistics control

Search date: 2026-08-09.

## Scope

Stage14-e9 studies the primitive shared-edge two-face ambient family under the physical real Euclidean height

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B
\]

and asks how the two reduced primitive Pythagorean faces decompose through

\[
g=\gcd(S_1,S_2),\qquad e=\operatorname{lcm}(S_1,S_2),
\]

including prime-by-prime support states and their relation to third-face-square/Euler-brick completion.

Classification vocabulary:

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```

Absence from the current search is not a novelty certificate.

## 1. Ochieng–Chikunji–Onyango-Otieno — common-side Pythagorean triples

Reference: *Pythagorean Triples with Common Sides*, Journal of Mathematics (2019), Article ID 4286517, DOI 10.1155/2019/4286517.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

This work studies pairs of Pythagorean triples sharing a side and develops divisor-based formulas for primitive and nonprimitive common-side configurations. It is directly relevant arithmetic context for the Stage14 shared-edge geometry.

The present search did not find the exact Stage14-e population counted simultaneously with the primitive three-edge condition, real Euclidean height, exactly-two filter, direction chambers, and the physical `(g,u,v)` ledger used here.

## 2. Huang — toric adelic equidistribution

Reference: Zhizhong Huang, *Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509.

Classification:

```text
REUSABLE_METHOD — ADELIC_LOCAL_DISTRIBUTION
```

Stage14-e3/e4/e6 already uses the split-toric Manin–Peyre framework. Huang's adelic equidistribution machinery is the natural theorem-level input if a later refinement computes limiting masses for explicit local valuation strata.

E9 deliberately does not identify its six states

```text
none, G, U, V, GU, GV
```

with normalized Tamagawa probabilities. That would require an additional local-coordinate calculation for the exact physical height. Therefore the present six-state tables remain deterministic finite statistics, except for the elementary congruence blockers proved directly in e9.

## 3. Peschmann — coprime Pythagorean-pair Euler-brick geometry

References:

- René Peschmann, *Quartic reductions and elliptic obstructions for perfect Euler bricks*, arXiv:2604.09328.
- René Peschmann, *A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers*, arXiv:2604.28072.
- René Peschmann, *Exponent-one blockers and a Mordell-Weil construction of Euler bricks*, arXiv:2605.00573.

Classification:

```text
ADJACENT_RESULT + REUSABLE_PARAMETER_CONTEXT
```

These papers use coprime Pythagorean-pair structures and quartic/elliptic reductions for Euler-brick and perfect-cuboid constraints. They are close to the arithmetic language of Stage14 but retain stronger completion conditions than the e9 ambient population.

The current search did not locate the Stage14-e real-height gcd/lcm distribution or its six physical support-state ledger in these works.

## 4. E9 exact inverse

The frozen e1 bijection writes

\[
e=g\alpha\beta,
\qquad x=\beta X_1,
\qquad y=\alpha X_2,
\]

where

\[
g=\gcd(S_1,S_2),\qquad
\alpha=S_1/g,
\qquad
\beta=S_2/g.
\]

E9 recovers the same data directly from the physical tuple:

\[
u=\gcd(e,x)=\beta,
\qquad
v=\gcd(e,y)=\alpha,
\]

then

\[
g=e/(uv),
\qquad S_1=gv,
\qquad S_2=gu,
\qquad \operatorname{lcm}(S_1,S_2)=e.
\]

This is an elementary consequence of the already-locked primitive gluing and is not advertised as a new general theorem about Pythagorean triples.

## 5. E9 mod-2 and mod-3 blockers

The two new completion exclusions used by e9 are elementary congruence consequences of the exact local state coordinates.

For `p=2`, state `G` means

```text
2|g, 2∤u, 2∤v.
```

Then `e` is even while `x,y` are odd, so

\[
x^2+y^2\equiv2\pmod4,
\]

which cannot be a square.

For `p=3`, state `G` means

```text
3|g, 3∤u, 3∤v.
```

Then `3|e` while `3∤xy`, so

\[
x^2+y^2\equiv2\pmod3,
\]

again impossible for a square.

These blockers are repository-local deductions from the e9 coordinates. They are not presented as novel modular facts.

## 6. Relation to Stage14-e8

E8 supplies an independent `B^{1+o(1)}` upper envelope for Euler bricks and records the large gap between that envelope, the ambient two-face population, and the observed completion count. E9 attacks part of that gap at the local arithmetic level.

The `p=2,G` and `p=3,G` exclusions remove a large fixed portion of the finite raw population, but by themselves they do not improve the global asymptotic exponent and do not establish a new fixed relative saving beyond the already-proved e4 thin-set theorem.

## 7. Search boundary

Current classification:

```text
OCHIENG_ET_AL_COMMON_SIDE_FORMULAS=ADJACENT_RESULT_PLUS_REUSABLE_METHOD
HUANG_TORIC_ADELIC_EQUIDISTRIBUTION=REUSABLE_METHOD
PESCHMANN_COPRIME_PYTHAGOREAN_PAIR_GEOMETRY=ADJACENT_RESULT
DIRECT_STAGE14_E9_GCD_LCM_REAL_HEIGHT_DISTRIBUTION=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
DIRECT_STAGE14_E9_SIX_STATE_LOCAL_TABLE=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

No asymptotic gcd/lcm law, prime-state independence, or novelty claim is inferred from the finite audit or from search absence.
