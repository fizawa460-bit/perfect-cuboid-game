# Stage14-4ag — Kummer geometry and the active rank-jump graph

## Purpose

Stage14-4af reduced every physical raw pair to a non-torsion point on a positive-rank specialization of

\[
E_t:\quad Y^2=X(X-1)(X+t^2),
\]

with the actual first-face base parameter

\[
t=\frac{2r}{1-r^2},\qquad r=\frac{X_1}{H_1+S_1}\in\mathbf Q\cap(0,1).
\]

Stage14-4ag does two things:

1. identify the pulled-back K3 exactly with the classical level-4 elliptic modular / Kummer surface;
2. replace the vague phrase “rank-jump frequency” by an exact finite graph and prove that bounded multiplicity inside one elliptic fiber is only `B^{o(1)}`.

The result is a sharp reduction of the **power exponent** problem. It is not yet a proof of a `sqrt(B)` asymptotic.

---

## 1. Exact level-4 modular identification

Shimada's level-4 elliptic modular surface has Weierstrass model

\[
Y^2=X(X-1)\left(X-\left(\frac{\sigma+\sigma^{-1}}2\right)^2\right).
\]

On the Stage14 Pythagorean base put

\[
\boxed{\sigma=i\frac{1+r}{1-r}}.
\]

If `c=(1+r)/(1-r)`, then

\[
\frac{\sigma+\sigma^{-1}}2
=\frac{i(c-c^{-1})}{2}
=i\frac{2r}{1-r^2}
=it.
\]

Therefore Shimada's model becomes exactly

\[
Y^2=X(X-1)(X+t^2).
\]

Thus, after this explicit Möbius base change over `Q(i)`, the Stage14-4af K3 is the elliptic modular surface of level 4. The known six singular fibers are all `I4`; over `C` the surface is the Kummer surface associated with

\[
E_i\times E_i,
\qquad E_i=\mathbf C/(\mathbf Z+i\mathbf Z).
\]

This is an **EXACT_GEOMETRIC_COLLISION**. Stage14 makes no novelty claim for the K3/Kummer geometry itself.

Literature source:

- Ichiro Shimada, *The elliptic modular surface of level 4 and its reduction modulo 3*, arXiv:1806.05787 / Annali di Matematica (2020).

Important boundary: Shimada identifies the characteristic-3 reduction with the Fermat quartic. Stage14 does **not** identify the characteristic-zero surface with the Fermat quartic.

---

## 2. Symmetric Kummer double-cover equation

Use Euclidean parameters `r,s` for the two primitive oriented faces:

\[
\rho(r)=\frac{2r}{1+r^2},\qquad
\rho(s)=\frac{2s}{1+s^2}.
\]

The normalized space-diagonal square condition is

\[
z^2=1-(\rho(r)\rho(s))^2.
\]

With

\[
Z=z(1+r^2)(1+s^2),
\]

we get the exact symmetric model

\[
\boxed{
\mathcal K:\quad
Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.
}
\]

Writing

\[
M=r^2s^2+r^2+s^2+1,
\]

the branch polynomial factors over `Q` as

\[
\boxed{F=(M-4rs)(M+4rs)}
\]

and over `Q(i)` as four `(1,1)` factors:

\[
\boxed{
\begin{aligned}
F={}&(rs-ir-is+1)(rs-ir+is-1)\\
&\cdot(rs+ir-is-1)(rs+ir+is+1).
\end{aligned}}
\]

This is the global two-face Kummer presentation underlying the one-fiber elliptic model.

---

## 3. Active rank-jump graph

For `B>=1`, define a finite simple graph `G_B`.

A vertex is a primitive **oriented** Pythagorean face datum

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

that occurs as an endpoint of at least one raw Stage14 pair incidence of physical height `d<=B`.

An edge is one raw pair incidence. The Stage14-4ab parameter-fiber multiplicity-one theorem makes this a genuine simple edge ledger.

Let

\[
V(B)=|\mathcal V_B|,
\qquad E(B)=|\mathcal E_B|,
\qquad \bar d(B)=\frac1{V(B)}\sum_{F\in\mathcal V_B}\deg_B(F).
\]

Then, exactly,

\[
\boxed{E(B)=O_{\rm pair}^{raw}(B)=N_2(B)+3T(B)}
\]

and the handshake lemma gives

\[
\boxed{E(B)=\frac12V(B)\bar d(B)}.
\]

Therefore

\[
\boxed{
N_2(B)=\frac12V(B)\bar d(B)-3T(B).
}
\]

This identity isolates the three independent ingredients of the exactly-two count:

1. **active positive-rank base frequency** `V(B)`;
2. **partner multiplicity per active fiber** `bar d(B)`;
3. **triple subtraction** `3T(B)`.

A triple object contributes three raw pair edges; its endpoint orientation states need not form a triangle in this graph.

---

## 4. First-hit height and positive-rank specialization

For a primitive oriented first face `F`, define the first-hit height

\[
\mu(F)=\min\{d:\ F\text{ occurs in a physical raw pair of space diagonal }d\},
\]

with `mu(F)=infinity` if no partner exists.

Then

\[
\boxed{V(B)=\#\{F:\mu(F)\le B\}.}
\]

Stage14-4af proves `mu(F)<infinity => rank E_F(Q)>0` because every physical point is non-torsion.

Conversely, if a genuine Pythagorean specialization has positive rank, it has infinitely many non-torsion rational points. The rational function `q` has finite fibers; after avoiding its finite boundary locus and using the quartic symmetries `q -> -q` and `q -> 1/q`, one obtains a rational point with `0<q<1`. This reconstructs a primitive rational Pythagorean second face. The minimal Stage14 gluing is primitive, its `d^2` is an integer, and the elliptic square condition makes `d` rational; hence `d` is an integer. Avoiding the finite equality boundary gives a canonical raw pair.

Thus

\[
\boxed{
\mu(F)<\infty
\iff
\operatorname{rank}E_F(\mathbf Q)>0
}
\]

for genuine Pythagorean first-face specializations. `V(B)` is therefore the positive-rank specialization count ordered by the **first physical small-point height**, not merely by the base height.

---

## 5. Uniform per-fiber multiplicity is `B^{o(1)}`

Marta Dujella proves a uniform theorem: over a fixed number field, an elliptic curve carrying a rational point of exact prime order has at most

\[
\exp\left(C\frac{\log H}{\log\log H}\right)
\]

rational points of exponential height at most `H`, with `C` depending only on the number field.

Every Stage14 fiber has rational 2-torsion, so the theorem applies with `k=Q` and `ell=2`.

For a physical pair with `d<=B`:

- `H_1<d<=B`, hence the rational base `t=X_1/S_1` has polynomial height in `B`;
- Stage14-4ae gives `H(q)<=O(sqrt(B))` uniformly because `g<=S_1`;
- the quartic-to-elliptic map is a fixed bounded-degree rational map in `t,q` and the square-root coordinate.

Elementary Weil-height inequalities therefore give an absolute `C0` such that every physical partner point lies in elliptic exponential height at most `B^C0`.

Consequently, uniformly in the active vertex `F`,

\[
\boxed{
\deg_B(F)
\le
\exp\left(C\frac{\log B}{\log\log B}\right)
=B^{o(1)}.
}
\]

Let

\[
\Delta(B)=\max_F\deg_B(F).
\]

Since every active vertex has degree at least one,

\[
\boxed{
\frac12V(B)\le E(B)\le\frac12V(B)\Delta(B)
=V(B)B^{o(1)}.
}
\]

Therefore the raw-pair edge count and the active rank-jump vertex count have the same polynomial growth exponent:

\[
\boxed{
\limsup_{B\to\infty}\frac{\log E(B)}{\log B}
=
\limsup_{B\to\infty}\frac{\log V(B)}{\log B},
}
\]

and likewise for `liminf`.

This is the main quantitative theorem of 14-4ag. A positive power of `B` cannot be manufactured by one prolific elliptic fiber; the power exponent lives in the frequency of **new active rank-jump fibers**.

Literature source:

- Marta Dujella, *Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves*, arXiv:2312.03655; Acta Arithmetica 217 (2025), 309–332.

---

## 6. Exact finite graph census through two million

The Stage14 exact Pythagorean-gluing census was augmented to retain the oriented endpoint graph. All 11 frozen cutoffs reproduce the existing raw-pair / exactly-two ledger, with `T=0`.

| B | E raw edges | V active vertices | average degree | max degree | V/sqrt(B) |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 2 | 3 | 1.3333 | 2 | 0.09487 |
| 2,000 | 5 | 7 | 1.4286 | 2 | 0.15652 |
| 5,000 | 15 | 25 | 1.2000 | 2 | 0.35355 |
| 10,000 | 25 | 39 | 1.2821 | 3 | 0.39000 |
| 20,000 | 42 | 54 | 1.5556 | 6 | 0.38184 |
| 50,000 | 62 | 80 | 1.5500 | 6 | 0.35777 |
| 100,000 | 89 | 117 | 1.5214 | 6 | 0.36999 |
| 200,000 | 116 | 155 | 1.4968 | 6 | 0.34659 |
| 500,000 | 188 | 254 | 1.4803 | 8 | 0.35921 |
| 1,000,000 | 255 | 347 | 1.4697 | 8 | 0.34700 |
| 2,000,000 | 356 | 490 | 1.4531 | 9 | 0.34648 |

On the full decade `200,000 -> 2,000,000`, the effective exponents are

\[
\boxed{\alpha_V=0.4998643818582221}
\]

for active vertices and

\[
\alpha_E=0.4869920087459567
\]

for raw edges.

At the four late cutoffs `200k,500k,1m,2m`,

\[
\operatorname{mean}(V(B)/\sqrt B)=0.3498207760,
\]

with coefficient of variation about `1.55%`.

This is finite evidence only. It does **not** prove `V(B)~c sqrt(B)` or even `V(B)=B^{1/2+o(1)}`. It does, however, locate the observed square-root signal much more precisely: in the audited range it is primarily a signal in the **number of active rank-jump base states**, not in per-fiber multiplicity.

---

## 7. Kummer-height literature boundary

McKinnon computed bounded-height rational-point behavior for Kummer surfaces associated with products of elliptic curves and showed that a finite union of accumulating curves can dominate the count outside the first arithmetic stratum.

Because the Stage14 K3 is the self-product Kummer `Km(E_i x E_i)` over `C`, this is a directly relevant structural method. It is **not yet imported as a Stage14 counting theorem**, because the Stage14 primitive/lcm physical height and rational field of definition must first be matched to the height/divisor used in the Kummer counting theorem.

Literature source:

- David McKinnon, *Counting Rational Points on K3 Surfaces*, J. Number Theory 84 (2000), arXiv:math/9903013.

This is the natural target of Stage14-4ah.

---

## 8. Triple gate remains independent

Stage14-4af proved that, for a fixed active first face, the triple/perfect-cuboid condition is a genus-5 curve. That gives fiberwise finiteness, but no uniform moving-base estimate.

The exact identity remains

\[
N_2(B)=E(B)-3T(B).
\]

Therefore 14-4ag does **not** transfer a hypothetical raw-pair `sqrt(B)` law to exactly-two. A theorem such as

\[
T(B)=o(\sqrt B)
\]

or an appropriately stronger relative thin-set estimate is still required.

---

## 9. Decision

```text
STAGE14_4AG=COMPLETE

LEVEL4_MODULAR_K3_IDENTIFIED_OVER_QI=true
KUMMER_EI_SELF_PRODUCT_GEOMETRY_IMPORTED=true
GLOBAL_KUMMER_DOUBLE_COVER_LOCKED=true

RANK_JUMP_GRAPH_IDENTITY_LOCKED=true
ACTIVE_VERTEX_IS_SMALL_POINT_POSITIVE_RANK_COUNT=true
DUJELLA_SUBPOLYNOMIAL_DEGREE_BOUND=true
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true

FINITE_ACTIVE_VERTEX_SQRTB_SIGNAL=true
FINITE_VERTEX_EXPONENT_200K_TO_2M=0.4998643818582221
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false

TRIPLE_FIXED_BASE_GENUS=5
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false

NEXT=Stage14-4ah Kummer height/accumulating-multisection and relative triple-thin analysis
```

The power-law mystery is now narrower: **how many new positive-rank Kummer fibers acquire their first physical point by height `B`?** The number of partners already living inside one active fiber is subpolynomial and cannot change the power exponent.
