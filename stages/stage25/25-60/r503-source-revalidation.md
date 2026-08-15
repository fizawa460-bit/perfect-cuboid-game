# Stage25-60 R503 primary-source revalidation

STATUS=COMPLETE
ROUTE=R503

## Primary source A — Yoshida

Takumi Yoshida, *The relationship between face cuboids and elliptic curves*, arXiv:2407.09825.

Reused facts:

- the elliptic family
  \[
  E_{1,s}:y^2=x(x-(2s)^2)(x+(s^2-1)^2);
  \]
- the map
  \[
  t=\frac{s\alpha-2s(s^2-1)}{\alpha+2s^2(s^2-1)};
  \]
- rational face-cuboid data with `BF=2|t|`, `EF=|t^2-1|`, and `HF=sqrt(gamma)`;
- the surjective elliptic-data-to-face-cuboid map has finite multiplicity `32:1`;
- the explicit fixed fiber `s=5/3` contains the non-torsion point `(-20/27,1120/243)`;
- the infinitude proof uses multiples `[n]P` on that fixed fiber;
- the proof of infinitely many positive-rank `s` applies the displayed rational transformation to those same multiples.

No quantitative polynomial lower count in the physical cuboid height is imported from the paper.

## Primary source B — Naskręcki

Bartosz Naskręcki, *Mordell-Weil ranks of families of elliptic curves associated to Pythagorean triples*, arXiv:1210.6933.

The paper distinguishes the plus-sign Pythagorean/Frey family

\[
y^2=x(x-a^2)(x+b^2),\qquad a^2+b^2=c^2,
\]

and records that the corresponding generic geometric Mordell-Weil rank is zero.

The adapter to Yoshida is exact:

\[
a=2s,\qquad b=s^2-1,\qquad c=s^2+1,
\]

because

\[
(2s)^2+(s^2-1)^2=(s^2+1)^2.
\]

Thus no change of population, cutoff, or heuristic identification is involved in the generic-rank statement; it is the same elliptic surface family up to notation/scaling.

## Nearby height/specialization sources reviewed but not promoted

- Joseph H. Silverman, arXiv:2402.14771: a function-field Lehmer-type canonical-height lower bound. Useful background, but it does not count rational specializations of positive rank with small points in the exact Yoshida family.
- Wei Pin Wong, arXiv:1409.3255: specialization-height/injectivity results for families over higher-dimensional projective bases. It does not provide the required one-parameter polynomial lower count of bounded-height positive-rank fibers for R503.

## Later exact-face-cuboid recheck

A bounded arXiv search for later work using the exact rational face-cuboid / Yoshida setup did not identify a subsequent primary paper proving the missing polynomial small-point count across varying `s`.

This is not recorded as an exhaustive literature nonexistence theorem.

```text
R503_PRIMARY_SOURCE_REVALIDATION=PASS
R503_YOSHIDA_SOURCE=arXiv:2407.09825
R503_GENERIC_RANK_ZERO_SOURCE=arXiv:1210.6933
R503_FAMILY_ADAPTER=EXACT
R503_NEARBY_HEIGHT_THEOREMS_REVIEWED=true
R503_DIRECTLY_APPLICABLE_UNIFORM_SMALL_POINT_COUNT_FOUND=false
R503_EXHAUSTIVE_LITERATURE_NONEXISTENCE_CLAIM=false
```
