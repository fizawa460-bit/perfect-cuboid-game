# Stage15-2 — ambient exactly-two family: infinitude and polynomial growth exponent

Base: merged Stage15-0/1 (`PR #824`). The common height is

\[
R(a,b,c)=\sqrt{a^2+b^2+c^2},\qquad 0<a<b<c,\qquad \gcd(a,b,c)=1,
\]

and `M_2(B)` counts primitive canonical triples with exactly two integral face diagonals and `R<=B`, without requiring `R` to be integral.

## 1. Result

Stage15-2 proves

\[
B\ll M_2(B)\ll B^{1+o(1)}.
\]

Equivalently,

\[
M_2(B)=B^{1+o(1)}
\]

at the level of the polynomial exponent. Thus the ambient two-face family is infinite and has exact polynomial growth exponent one.

This does **not** determine the logarithmic factor. In particular, Stage15-2 does not claim `M_2(B) asymp B`, `M_2(B) asymp B(log B)^k`, or an asymptotic constant. The finite Stage15-1 counts look compatible with a substantial polylogarithmic factor, but that is diagnostic only.

```text
M2_INFINITE=true
M2_LINEAR_LOWER_BOUND=true
M2_UPPER_BOUND=B^(1+o(1))
M2_POLYNOMIAL_EXPONENT_ONE=true
M2_ASYMPTOTIC_PROVED=false
M2_LOG_POWER_PROVED=false
STAGE15_2_EXIT=M2_ONLY_PARTIAL_BOUNDS
```

## 2. Explicit two-parameter primitive exact-two family

Let `p,q` be coprime odd positive integers with `p<q<2p`. Set

\[
e=4pq,
\qquad x=4p^2-q^2,
\qquad y=4q^2-p^2.
\]

The two Euclid pairs

\[
(2p,q),\qquad (2q,p)
\]

are coprime and of opposite parity. Hence

\[
e^2+x^2=(4p^2+q^2)^2,
\qquad
e^2+y^2=(4q^2+p^2)^2.
\]

Both corresponding Pythagorean triangles are primitive. Therefore

\[
\gcd(e,x)=\gcd(e,y)=1,
\]

so the three-edge box is globally primitive.

Because `p,q` are odd, both `x` and `y` are odd. Hence

\[
x^2+y^2\equiv 2\pmod 4,
\]

which is not a square. Thus every member of this family has **exactly two**, not three, integral face diagonals.

A useful cancellation gives the exact geometric height identity

\[
R^2=e^2+x^2+y^2=17(p^4+q^4).
\]

### A canonical injective cone

Restrict further to

\[
1<q/p<11/10.
\]

Then

\[
x<y<e,
\]

so the canonical representative is exactly `(a,b,c)=(x,y,e)` and the two integral faces share the largest edge `c`.

The parameter pair is recoverable from the box because

\[
x+y=3(p^2+q^2),
\qquad y-x=5(q^2-p^2).
\]

Therefore distinct coprime odd pairs in this cone give distinct primitive canonical members of `B_2`.

Let

\[
C_0=\sqrt{17\left(1+(11/10)^4\right)}.
\]

If `p<=sqrt(B/C_0)`, then `R<=B`. By Möbius inversion, the number of coprime odd lattice pairs in any fixed positive-area cone is `c X^2+O(X log X)` for a positive constant `c`. Taking `X` proportional to `sqrt(B)` proves

\[
M_2(B)\gg B.
\]

The same construction in a cone above `(1+sqrt(2))/2` also supplies a linear-size family with the shared edge in the middle direction; the total lower bound needs only the largest-edge cone above.

## 3. Uniform divisor upper bound

Every exactly-two box has a unique shared edge `e`. Fix `e` and consider a possible other leg `x` satisfying

\[
e^2+x^2=h^2.
\]

Then

\[
(h-x)(h+x)=e^2.
\]

The positive factor pair `(h-x,h+x)` determines `x` uniquely. Therefore the number `r(e)` of possible Pythagorean completions through the leg `e` is at most

\[
r(e)\le \tau(e^2).
\]

For a box with `R<=B`, every edge is at most `B`. Ignoring the canonical, primitive, exactly-two, and geometric-pair restrictions can only enlarge the count, so

\[
M_2(B)
\le \sum_{e\le B}\binom{r(e)}2
\le \frac12\sum_{e\le B}\tau(e^2)^2.
\]

The standard uniform divisor bound gives

\[
\tau(n)=\exp\!\left(O\!\left(\frac{\log n}{\log\log n}\right)\right)=n^{o(1)}.
\]

Uniformly for `e<=B`, `tau(e^2)^2=B^{o(1)}`. Hence

\[
M_2(B)\ll B^{1+o(1)}.
\]

Together with the explicit linear lower family, this proves the polynomial exponent one statement.

## 4. Why this is not yet an asymptotic

The upper bound deliberately forgets most structure. It does not determine the average number of admissible pairs on a shared edge after:

- global primitivity;
- the exact `R<=B` ellipsoidal cutoff;
- the minimal shared-edge gluing relation;
- exclusion of the third square face;
- canonical directional chamber restrictions.

Consequently the gap between `B` and `B^{1+o(1)}` is entirely subpolynomial but can contain powers of `log B`. Stage15-1 finite data, for example, have `M_2(100000)=796698`; this is not promoted to a logarithmic law.

## 5. Focused literature gate

The Stage15-2 literature check found relevant parametrization and ambient rational-point machinery, but no directly matching theorem with all Stage15 hypotheses and the `R` height:

1. K. Ochieng, *Pythagorean Triples with Common Sides*, Journal of Mathematics (2019), DOI `10.1155/2019/4286517`: formulas and fixed-common-leg counts for primitive/nonprimitive Pythagorean triples. This supports the shared-leg divisor viewpoint but is not an `R<=B` asymptotic for primitive canonical exactly-two boxes.
2. R. Peschmann, *Exponent-one blockers and a Mordell-Weil construction of Euler bricks*, arXiv:2605.00573 (2026), and companion work arXiv:2604.09328: modern two-Pythagorean-pair parametrizations aimed at Euler/perfect bricks. Their theorem targets triple-face/perfect-brick structure, not `M_2(B)`.
3. V. Batyrev and Y. Tschinkel, *Manin's conjecture for toric varieties*, arXiv:alg-geom/9510014: a potential global counting framework after a correct compactification/height identification. No such adapter is asserted here.

The natural next analytic task is therefore to identify the exact rational surface/compactification for the two shared-face equations, prove that the Stage15 Euclidean height corresponds to the required adelic height up to controlled sector factors, remove accumulating boundary curves, and then determine whether an existing toric/del-Pezzo theorem yields the missing logarithmic exponent and leading constant.

```text
DIRECT_M2_R_HEIGHT_ASYMPTOTIC_FOUND=false
COMMON_LEG_PARAMETRIZATION_LITERATURE_FOUND=true
TORIC_DEL_PEZZO_ROUTE_REQUIRES_ADAPTER=true
NOVEL_ASYMPTOTIC_CLAIM=false
NEXT=Stage15-2a compactification/height/Picard-rank audit for the ambient two-face surface
```
