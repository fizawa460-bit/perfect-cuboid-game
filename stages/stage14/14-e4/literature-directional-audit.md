# Stage14-e4 — literature-first directional distribution audit

## Scope

Stage14-e4 asks for the directionwise asymptotic of the Stage14-e exactly-two ambient population

\[
E_a(B),\qquad E_b(B),\qquad E_c(B),
\]

where the two integral face diagonals share the edge `e`, `x<y`,

\[
e^2+x^2=\square,\qquad e^2+y^2=\square,
\qquad \gcd(e,x,y)=1,
\]

and the real Euclidean height is

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B,
\]

with no rational/integer requirement on `D_R`. The exactly-two condition is

\[
x^2+y^2\ne\square.
\]

The chambers are

```text
a: e<x<y
b: x<e<y
c: x<y<e
```

or, after normalization by `e`,

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1.
```

The literature gate remains:

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

## 1. Huang, toric adelic equidistribution — theorem-level input

Zhizhong Huang, *Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509. The current arXiv record used by this stage is v3, revised 17 July 2026.

Classification:

```text
REUSABLE_METHOD — THEOREM_LEVEL_INPUT
```

Huang proves the Manin--Peyre equidistribution principle for smooth proper split toric varieties over `Q`, with effective asymptotic formulas for rational points in arbitrary adelic neighbourhoods.

This is exactly the external theorem needed to turn the Stage14-e3 toric model into real-chamber asymptotics. Stage14-e4 does not claim adelic equidistribution as new; the repository-local work is the explicit computation of the archimedean Tamagawa density for the physical Euclidean height and its integration over the three cuboid chambers.

## 2. Browning--Loughran, thin sets under equidistribution — theorem-level input

Tim Browning and Daniel Loughran, *Sieving rational points on varieties*, Transactions of the American Mathematical Society 371 (2019), 5757--5785; preprint arXiv:1705.01999.

Classification:

```text
REUSABLE_METHOD — THEOREM_LEVEL_INPUT
```

Their Theorem 1.2 states that on an almost-Fano variety with equidistributed rational points on a dense open subset, a thin subset contributes zero percent of the bounded-height points.

For Stage14-e the third-face-square locus is the image of the generically degree-two cover

\[
w^2=t_1^2+t_2^2.
\]

Since `t1^2+t2^2` is not a square in the geometric function field, this is a genuine type-II thin cover after normalization/resolution. Hence Euler-brick points are `o(B(log B)^5)` and do not change any real-chamber leading coefficient.

This is stronger than the fixed `p=5` lower-bound neighbourhood used in e3: e4 can remove the whole third-face-square thin set at leading order.

## 3. Batyrev--Tschinkel, toric Manin asymptotics

Victor V. Batyrev and Yuri Tschinkel, *Manin's conjecture for toric varieties*, Journal of Algebraic Geometry 7 (1998), 15--53; arXiv:alg-geom/9510014, together with their height-zeta work arXiv:alg-geom/9606003.

Classification:

```text
REUSABLE_METHOD — THEOREM_LEVEL_INPUT
```

These remain the global height-counting input inherited from e3. The e4 novelty boundary is not the existence of a toric Manin asymptotic; it is the explicit identification of the three Stage14-e physical chambers inside the real torus and the resulting Tamagawa mass ratios.

## 4. Korolev--Ustinov, rational points on the unit circle

M. A. Korolev and A. V. Ustinov, *Distribution of rational points on the circle of unit radius*, Izvestiya: Mathematics 83:5 (2019), 1008--1049, DOI 10.1070/IM8839.

Classification:

```text
ADJACENT_RESULT + REUSABLE_CONTEXT
```

This studies fine distribution statistics of rational points on the unit circle, equivalently Pythagorean triples, under a one-circle denominator cutoff. It confirms that angular/shape distribution questions for Pythagorean points are classical and nontrivial.

It is not an exact collision with Stage14-e4: the present object is a pair of Pythagorean slopes coupled by the primitive shared-denominator/lcm height, compactified as the e3 toric surface, and split by the position of the shared edge.

## 5. Ochieng--Chikunji--Onyango-Otieno, common-side triples

Raymond Calvin Ochieng, Chiteng'a John Chikunji, Vitalis Onyango-Otieno, *Pythagorean Triples with Common Sides*, Journal of Mathematics (2019), Article ID 4286517, DOI 10.1155/2019/4286517.

Classification:

```text
ADJACENT_RESULT + REUSABLE_FIXED_LEG_ARITHMETIC
```

The paper gives formulas and multiplicities for Pythagorean triples with a fixed common leg. It is relevant arithmetic context but does not provide the Stage14-e anticanonical-height chamber distribution.

## 6. Current collision decision

The current search finds no direct source proving the precise Stage14-e4 statement

```text
primitive two-face common-edge ambient family
+ real Euclidean/anticanonical height
+ exactly-two thin-set removal
+ asymptotic split by e<x<y, x<e<y, x<y<e.
```

Accordingly:

```text
TORIC_ADELIC_EQUIDISTRIBUTION=REUSABLE_METHOD_THEOREM_INPUT
THIN_SET_ZERO_DENSITY=REUSABLE_METHOD_THEOREM_INPUT
ONE_CIRCLE_ANGULAR_DISTRIBUTION=ADJACENT_RESULT
COMMON_SIDE_FIXED_LEG_DISTRIBUTION=ADJACENT_RESULT
DIRECT_STAGE14_E4_DIRECTIONAL_THEOREM=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

The repository-local contribution in e4 is therefore narrowly stated: derive the physical archimedean density from the frozen e3 model, integrate it over the three real chambers, and transfer the raw chamber asymptotics to exactly-two by the established thin-set theorem.
