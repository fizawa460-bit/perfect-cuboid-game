# Stage14-e7 — literature-first audit for secondary asymptotics

## Scope

Stage14-e7 asks why the exact Stage14-e census through `B=10^6` looks almost proportional to

\[
B(\log B)^3
\]

even though Stage14-e3/e6 prove

\[
E_2(B)\sim C_E B(\log B)^5,
\qquad
1.47953102009666\times10^{-6}<C_E<1.47956061101297\times10^{-6}.
\]

The literature gate remains

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

The key distinction in e7 is between:

1. the **local Laurent expansion** of the height zeta function at `s=1`;
2. a **global effective contour shift / Tauberian theorem** strong enough to turn several Laurent coefficients into a proved counting polynomial;
3. a finite-data crossover diagnostic.

These are not interchangeable.

## 1. Batyrev--Tschinkel — pole structure and leading term

Victor V. Batyrev and Yuri Tschinkel, *Height Zeta Functions of Toric Varieties*, arXiv:alg-geom/9606003.

Classification:

```text
REUSABLE_METHOD — LOCAL_POLE_STRUCTURE_AND_LEADING_TERM
```

Their Theorems 1.1 and 1.4 give, in the toric setting, a representation of the form

\[
Z(s)=\frac{g(s)}{(s-a)^b}+h(s)
\]

with `g,h` holomorphic on the closed leading half-plane and `g(a) != 0`.  In the Stage14-e anticanonical case,

```text
a=1
b=rho(Y)=6.
```

This justifies a pole of order six and hence the `B(log B)^5` leading order.  The Tauberian statement quoted in that paper extracts the leading term only.

Therefore Batyrev--Tschinkel alone does **not** justify promoting a five-term polynomial

\[
B(c_5\log^5 B+c_4\log^4 B+c_3\log^3 B+\cdots)
\]

with an effective remainder for the physical Stage14-e height.

## 2. Chambert-Loir--Tschinkel — effective toric error machinery

Antoine Chambert-Loir and Yuri Tschinkel, *Fonctions zeta des hauteurs des espaces fibres*, arXiv:math/0003013; Progress in Mathematics 199 (2001), 71--115.

Classification:

```text
REUSABLE_METHOD — EFFECTIVE_TAUBERIAN_TEMPLATE
```

The paper explicitly improves the error term for toric varieties.  Its Appendix A gives a Tauberian theorem of the following shape: if the height zeta function has meromorphic continuation into a half-plane left of the leading pole, has a unique pole there of multiplicity `b`, and satisfies polynomial vertical growth, then

\[
N(B)=B^a P(\log B)+O(B^{a-\delta})
\]

for a polynomial `P` of degree `b-1`.

For Stage14-e this is exactly the template that would turn a sixfold pole into a degree-five logarithmic polynomial.

However, e7 does not simply quote this conclusion for the physical Euclidean metric.  The repository must still verify, for that exact metric:

```text
PHYSICAL_METRIC_LEFT_HALF_PLANE_CONTINUATION
PHYSICAL_METRIC_VERTICAL_GROWTH_BOUND
NO_EXTRA_POLES_IN_THE_SHIFTED_STRIP
```

The e6 leading-constant calculation does not prove those effective analytic properties.

## 3. Formal Laurent-to-polynomial dictionary

Suppose, in addition to the already-proved leading pole, one has enough continuation and growth to justify the Chambert-Loir--Tschinkel contour shift.  Write near `s=1`

\[
Z(s)=\sum_{j=1}^{6}\frac{A_{-j}}{(s-1)^j}+O(1).
\]

The residue of

\[
Z(s)\frac{B^s}{s}
\]

at `s=1` gives

\[
B\{c_5L^5+c_4L^4+c_3L^3+c_2L^2+c_1L+c_0\},
\qquad L=\log B,
\]

with in particular

\[
\boxed{c_5=\frac{A_{-6}}{5!}},
\]

\[
\boxed{c_4=\frac{A_{-5}-A_{-6}}{4!}},
\]

\[
\boxed{c_3=\frac{A_{-4}-A_{-5}+A_{-6}}{3!}}.
\]

Stage14-e6 evaluates `c5=C_E`.  It does not evaluate `A_-5` or `A_-4`.

This dictionary is recorded because it identifies the exact analytic objects required for a future genuine secondary-term theorem.  It is not itself a proof that the physical counting function has the full polynomial expansion.

## 4. Finite-crossover analysis is diagnostic, not a Laurent computation

Stage14-e7 extends the exact census to a denser grid of cutoffs through `10^6`.  It then studies

\[
R_3(B)=\frac{E_2(B)}{B(\log B)^3}.
\]

If a three-term polynomial model were already numerically dominant, then

\[
R_3(B)\approx c_5(\log B)^2+c_4\log B+c_3.
\]

The e7 regression **fixes** `c5` to the e6 theorem value and estimates only effective finite-range `c4,c3`.  These fitted coefficients are explicitly labeled

```text
FINITE_EFFECTIVE_COEFFICIENTS_ONLY
```

because they drift as the lower edge of the fit window is moved.  They are not identified with the true Laurent coefficients.

## 5. Collision status

The current primary-source search finds the general toric pole theorem and an effective Tauberian/toric error-term framework, but no source computing the secondary coefficients for the specific Stage14-e physical Euclidean metric and bad `p=2` normalization.

```text
DIRECT_STAGE14_E7_SECONDARY_COEFFICIENTS=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

This is not a novelty certificate.
