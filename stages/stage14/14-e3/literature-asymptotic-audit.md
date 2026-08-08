# Stage14-e3 — literature-first asymptotic collision audit

## Scope

Stage14-e3 asks for the true order of the primitive exactly-two ambient count

\[
E_2(B),
\]

where

\[
e^2+x^2=\square,\qquad e^2+y^2=\square,
\qquad \gcd(e,x,y)=1,\qquad x<y,
\]

and

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B,
\]

with no rationality or integrality condition on `D_R`, while `x^2+y^2` is required to be nonsquare.

The e2 finite data suggested `B(log B)^3`. This stage does not treat that fit as evidence of a theorem; it first searches for an established height-counting framework.

Classification vocabulary remains

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```

and

```text
NOVELTY_BY_SEARCH_ABSENCE=false
```

## 1. Ochieng–Chikunji–Onyango-Otieno (2019): common-side Pythagorean triples

Bibliography:

Raymond Calvin Ochieng, Chiteng'a John Chikunji, Vitalis Onyango-Otieno,
*Pythagorean Triples with Common Sides*, Journal of Mathematics (2019), Article ID 4286517, DOI 10.1155/2019/4286517.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

This paper gives formulas for primitive and nonprimitive Pythagorean triples sharing a fixed leg and is directly relevant to the arithmetic multiplicity attached to the Stage14-e shared edge. It does not, in the present search, count the two-face ambient population under the projective/Euclidean height used here.

Therefore it is useful local/fixed-leg structure, not the e3 total-height theorem.

## 2. Batyrev–Tschinkel: Manin's conjecture for toric varieties

Bibliography:

Victor V. Batyrev and Yuri Tschinkel,
*Manin's conjecture for toric varieties*, Journal of Algebraic Geometry 7 (1998), 15–53; preprint arXiv:alg-geom/9510014.

Classification:

```text
REUSABLE_METHOD — THEOREM-LEVEL INPUT
```

Batyrev–Tschinkel prove the Manin asymptotic for rational points of bounded anticanonical height on arbitrary smooth projective toric varieties over number fields.

Stage14-e3 does **not** claim this theorem as new. The repository-local work is the explicit identification of the Stage14-e two-face ambient family with a real chamber of the rational torus on a specific smooth toric surface, and the verification that the physical height comes from its anticanonical line bundle up to bounded metric comparison.

The resulting toric surface is the blow-up of `P^1 x P^1` at its four torus-fixed corners and has Picard rank six. Consequently the anticanonical toric count has logarithmic exponent

\[
\rho-1=5.
\]

## 3. Huang: adelic equidistribution and geometric sieve for toric varieties

Bibliography:

Zhizhong Huang,
*Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509.

Classification:

```text
REUSABLE_METHOD — THEOREM-LEVEL INPUT
```

Huang proves the Manin–Peyre equidistribution principle for smooth projective split toric varieties over `Q`, including asymptotic formulas in arbitrary adelic neighbourhoods.

Stage14-e3 needs this refinement twice:

1. to restrict the toric count to a positive real chamber corresponding to `q_1>1`, `q_2>1`, `t_1<t_2`;
2. to impose a fixed 5-adic congruence neighbourhood that forces the third face `x^2+y^2` to be nonsquare.

This prevents the exactly-two lower bound from relying on any unproved assertion that Euler bricks are density zero.

## 4. The explicit 5-adic blocker

For one Pythagorean slope write

\[
h^2-t^2=1,
\qquad q=h+t,
\qquad q^{-1}=h-t,
\]

so

\[
t=\frac{q-q^{-1}}2.
\]

At `p=5`, impose the open unit conditions

\[
q_1\equiv2\pmod5,
\qquad q_2\equiv3\pmod5.
\]

Since `2^{-1}=3` and `3^{-1}=2` modulo 5,

\[
t_1\equiv\frac{2-3}{2}\equiv2\pmod5,
\qquad
t_2\equiv\frac{3-2}{2}\equiv3\pmod5.
\]

Each individual Pythagorean condition is locally valid:

\[
1+t_1^2\equiv1+4\equiv0\pmod5,
\qquad
1+t_2^2\equiv1+9\equiv0\pmod5.
\]

But

\[
t_1^2+t_2^2\equiv4+9\equiv3\pmod5,
\]

and `3` is a nonsquare unit modulo 5. Hence `t_1^2+t_2^2` cannot be a square in `Q_5`, therefore cannot be a square in `Q`.

Since

\[
x^2+y^2=e^2(t_1^2+t_2^2),
\]

all rational points in this fixed 5-adic neighbourhood are automatically in the exactly-two ambient population.

The neighbourhood is nonempty and has positive local measure. Together with any nonempty real open chamber inside `q_1>1, q_2>1, t_1<t_2`, Huang's theorem supplies a positive-order lower-bound family.

## 5. Collision decision

No source found in the current search states the precise Stage14-e result in its cuboid language:

```text
primitive shared-edge two-face ambient objects
+ real Euclidean projective height
+ exactly-two third-face exclusion
+ shared-edge chambers
```

However, after the repository-local toric identification, the **total growth mechanism is not a new analytic theorem**. It is an application of established toric height-counting and equidistribution theorems.

Current classification:

```text
COMMON_SIDE_FIXED_LEG_FORMULAS=ADJACENT_RESULT_PLUS_REUSABLE_METHOD
TORIC_MANIN_HEIGHT_COUNT=REUSABLE_METHOD_THEOREM_INPUT
TORIC_ADELIC_EQUIDISTRIBUTION=REUSABLE_METHOD_THEOREM_INPUT
DIRECT_CUBOID_LANGUAGE_E3_THEOREM=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

## 6. Consequence for the e2 finite fit

The toric Picard rank calculation predicts logarithmic exponent five, not three. Therefore the e2 observation

\[
E_2(B)/(B(\log B)^3)\approx0.0052
\]

through `B=10^6` is retained only as a pre-asymptotic diagnostic.

Stage14-e3 must not tune a proof to the finite `log^3` fit. The theorem-level target is the order

\[
B(\log B)^5.
\]

No leading constant for the exactly-two subset is asserted at this stage.
