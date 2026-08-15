# Stage25-60 R503 — Yoshida varying-fiber route: generic-rank-zero obstruction and quantitative gate

STATUS=SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R503
ROLE=CHECKPOINT60_ITERATIVE_DEEP_ROUTE
TARGET=Stage19 primitive canonical exactly-two-face plus integral-space population

## 1. Result

The Yoshida route remains mathematically important, but its easiest hoped-for upgrade mechanism is now ruled out.

Yoshida studies

\[
E_{1,s}: y^2=x\bigl(x-(2s)^2\bigr)\bigl(x+(s^2-1)^2\bigr),
\qquad s\in\mathbb Q\setminus\{0,\pm1\}.
\]

Put

\[
a=2s,\qquad b=s^2-1,\qquad c=s^2+1.
\]

Then

\[
a^2+b^2=c^2,
\]

and Yoshida's family is exactly the Pythagorean/Frey family

\[
y^2=x(x-a^2)(x+b^2).
\]

Naskręcki, arXiv:1210.6933, records that this plus-sign Pythagorean family has geometric generic Mordell-Weil rank zero over the rational-function field. Therefore

\[
\boxed{\operatorname{rank}E_{1,s}(\overline{\mathbb Q}(s))=0.}
\]

In particular there is no non-torsion rational section on the original Yoshida elliptic surface, even after extending constants from `Q` to `Qbar`.

```text
R503_YOSHIDA_FAMILY_IDENTIFIED_WITH_PYTHAGOREAN_FREY_PLUS_FAMILY=true
R503_GENERIC_GEOMETRIC_MW_RANK=0
R503_NONTORSION_GENERIC_SECTION_EXISTS=false
R503_DIRECT_SECTION_BASED_POWER_COUNT_ROUTE=CLOSED
```

This does **not** say that positive-rank specializations are finite. Yoshida proves the opposite: infinitely many rational `s` have positive rank. The point is that those specializations are exceptional from the generic-section viewpoint.

## 2. Yoshida's explicit infinitude mechanism is one fixed-fiber orbit

Yoshida proves infinitude of rational face cuboids by starting with the fixed fiber

\[
s_0=5/3
\]

and a non-torsion point

\[
P=(-20/27,1120/243)\in E_{1,5/3}(\mathbb Q).
\]

Writing

\[
[n]P=(\alpha_n,\beta_n),
\]

Theorem 1.1 uses

\[
t=\frac{s\alpha-2s(s^2-1)}{\alpha+2s^2(s^2-1)}.
\]

At `s=5/3` this becomes the Möbius map

\[
\boxed{
t=\frac{15(9\alpha-32)}{81\alpha+800}
}
\]

with inverse

\[
\boxed{
\alpha=-\frac{160(5t+3)}{27(3t-5)}.
}
\]

Hence logarithmic heights satisfy

\[
h(t_n)=h(\alpha_n)+O(1).
\]

On the fixed elliptic curve, canonical height gives

\[
\hat h([n]P)=n^2\hat h(P),
\]

and the standard comparison between canonical height and `x`-coordinate height on a fixed elliptic curve yields

\[
h(\alpha_n)=2n^2\hat h(P)+O(1).
\]

Therefore

\[
\boxed{h(t_n)=\Theta(n^2).}
\]

## 3. Physical-height consequence for Yoshida's fixed-fiber cuboids

Yoshida's face cuboid attached to `(s,t)` has, in his notation,

\[
BF=2|t|,\qquad EF=|t^2-1|,
\]

so the scale-free edge ratio is

\[
\rho(t)=\frac{BF}{EF}=\frac{2t}{t^2-1}.
\]

This is a degree-two rational map on `P^1`, hence

\[
h(\rho(t))=2h(t)+O(1).
\]

For a primitive integer face cuboid of space height at most `B`, both edges in this ratio are at most `B`. After reducing the ratio to lowest terms,

\[
h(\rho)\le \log B+O(1).
\]

Consequently any member of Yoshida's fixed-fiber orbit whose primitive cuboid height is at most `B` must satisfy

\[
n^2\ll \log B.
\]

Thus the number of indices from this explicit orbit that can contribute below height `B` is at most

\[
\boxed{O(\sqrt{\log B}).}
\]

This is only an upper bound for this specific Yoshida orbit. It does not upper-bound all Stage19 objects or all positive-rank fibers.

```text
R503_YOSHIDA_FIXED_FIBER_ORBIT_HEIGHT=h(t_n)=Theta(n^2)
R503_YOSHIDA_FIXED_FIBER_ORBIT_COUNT_UPPER=O(sqrt(log B))
R503_YOSHIDA_FIXED_FIBER_ORBIT_BEATS_B_QUARTER=false
```

## 4. Yoshida's infinitely many positive-rank parameters are also height-sparse in the displayed construction

Yoshida obtains infinitely many positive-rank parameters by applying his diagrammatic transformation to the same points `[n]P`. The resulting `s`-coordinate is a Möbius function of `alpha_n`. At `s_0=5/3`, the displayed transformation specializes to

\[
\boxed{
s'_n=\frac{4(27\alpha_n+40)}{27\alpha_n-640}.
}
\]

This map also has a rational inverse, so

\[
h(s'_n)=h(\alpha_n)+O(1)=\Theta(n^2).
\]

Therefore Yoshida's explicit proof of infinitely many positive-rank `s` supplies only

\[
O(\sqrt{\log X})
\]

such displayed parameters of rational height at most `X`.

This does not rule out many other positive-rank specializations. It shows only that the particular infinitude construction in the paper is height-sparse and cannot itself supply the polynomial-sized varying-fiber population needed to improve Stage25.

```text
R503_YOSHIDA_POSITIVE_RANK_S_SEQUENCE_HEIGHT=Theta(n^2)
R503_YOSHIDA_DISPLAYED_S_SEQUENCE_COUNT_UPPER=O(sqrt(log X))
R503_POSITIVE_RANK_INFINITUDE_IMPLIES_POWER_COUNT=false
```

## 5. The 32:1 theorem solves multiplicity, not population growth

Yoshida proves a `32:1` surjection from elliptic data `(s,alpha,beta)` to rational face-cuboid similarity classes. This is extremely useful once one has many bounded-height elliptic data, because it gives finite multiplicity.

But `32:1` does not create a new parameter dimension. To beat the audited Stage25 lower

\[
N_2(B)\gg B^{1/4},
\]

R503 still needs a polynomial-sized supply of non-torsion data whose resulting cuboid height is polynomially controlled.

The generic-rank-zero theorem proves that such a supply cannot come from a non-torsion section of the original `s`-surface.

## 6. Exact remaining theorem gate

R503 is therefore not marked `CLOSED_NO_UPGRADE`. Instead it is reduced to a more precise external/base-change gate.

A future successful R503 upgrade must provide at least one of the following:

1. **low-degree base change / multisection:** an algebraic cover `s=f(u)` on which the pulled-back Yoshida surface has a non-torsion section, together with a rational-parameter count, physical-height control, bounded multiplicity, primitive reduction and exactly-two exceptions;
2. **quantitative exceptional-fiber theorem:** a theorem giving polynomially many rational parameters `s` of bounded height for which `E_{1,s}` has a non-torsion point of uniformly polynomially controlled height;
3. **average small-point theorem in this exact family:** enough bounded-height elliptic data across varying fibers to overcome the `B^(1/4)` R501/R502 lower after all Stage19 adapters.

Positive-rank infinitude alone is insufficient. A specialization injectivity theorem alone is insufficient. A lower bound for canonical height on each individual fiber is insufficient unless accompanied by a polynomial lower count of fibers carrying suitably small points.

```text
R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE
R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED_BY_GEOMETRIC_RANK_ZERO
R503_LOW_DEGREE_BASE_CHANGE_MULTISECTION=OPEN_GATE
R503_QUANTITATIVE_POSITIVE_RANK_FIBER_COUNT=OPEN_GATE
R503_UNIFORM_SMALL_POINT_COUNT=OPEN_GATE
R503_GLOBAL_LOWER_EXPONENT_UPGRADE_PROVED=false
R503_MATCHING_HALF_POWER_LOWER_PROVED=false
```

## 7. Primary-source recheck

Load-bearing primary sources reviewed:

- Takumi Yoshida, *The relationship between face cuboids and elliptic curves*, arXiv:2407.09825. Used for `E_{1,s}`, the `32:1` map, the fixed `s=5/3` non-torsion orbit, and the construction of infinitely many positive-rank `s`.
- Bartosz Naskręcki, *Mordell-Weil ranks of families of elliptic curves associated to Pythagorean triples*, arXiv:1210.6933. Used for the geometric generic-rank-zero statement for `y^2=x(x-a^2)(x+b^2)` with `a^2+b^2=c^2`.
- Joseph H. Silverman, *A Lehmer-Type Lower Bound for the Canonical Height on Elliptic Curves Over Function Fields*, arXiv:2402.14771, reviewed as a nearby height input. It is not a polynomial lower-count theorem for rational positive-rank specializations and is not promoted into the Stage25 proof.
- Wei Pin Wong, *Heights and the Specialization Map for Families of Elliptic Curves over P^n*, arXiv:1409.3255, reviewed as a nearby specialization result. It does not supply the required one-parameter bounded-height positive-rank population for R503.

A bounded arXiv recheck also found no later exact face-cuboid paper supplying the missing quantitative varying-fiber small-point theorem. This is a bounded search result, not an exhaustive nonexistence claim.

```text
PRIMARY_SOURCE_RECHECK=PASS
GENERIC_RANK_ZERO_SOURCE_BOUND=PASS
YOSHIDA_SOURCE_BOUND=PASS
NO_EXHAUSTIVE_LITERATURE_NONEXISTENCE_CLAIM=true
FINITE_DATA_USED_AS_PROOF=false
FRESH_AUDIT_REQUIRED=true
```
