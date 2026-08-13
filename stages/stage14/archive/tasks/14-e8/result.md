# Stage14-e8 — quantitative Euler-brick thin-set count

> STATUS: `STAGE14_E8_COMPLETE_K3_AND_SUBPOWER_MULTIPLICITY_ENVELOPE`
>
> INPUT: frozen e4 thin-set theorem, e7 exact Euclidean-height census, standard Pythagorean parametrization and divisor-function maximal order.
>
> RESULT: the third-face-square population is identified with a K3 height problem and admits an independent unconditional envelope
>
> \[
> R_{\rm EB}(B)
> \ll
> B\log B\exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right)
> =B^{1+o(1)}.
> \]
>
> This does **not** prove a fixed power saving or a logarithmic saving relative to the e4 ambient main term.

## 1. Population and ledger normalization

Let

\[
R_{\rm EB}(B)
\]

denote the number of primitive **unordered** Euler bricks

\[
0<a<b<c,
\qquad
\gcd(a,b,c)=1,
\]

with

\[
a^2+b^2=\square,
\qquad
a^2+c^2=\square,
\qquad b^2+c^2=\square,
\]

and the same Stage14-e physical height

\[
D_{\mathbf R}=\sqrt{a^2+b^2+c^2}\le B.
\]

There is no integer-space-diagonal condition.

Stage14-e stores raw two-face objects as a choice of shared edge.  Every Euler brick has three choices of shared edge, hence exactly

\[
\boxed{
E_{\rm raw}(B)-E_2(B)=3R_{\rm EB}(B).
}
\]

The e7 exact census verifies this identity at all 17 frozen cutoffs through `B=10^6`.

At the ceiling,

\[
R_{\rm EB}(10^6)=219,
\]

so the raw incidence difference is

\[
3\cdot219=657.
\]

## 2. The Euler-brick projective surface

Choose one edge as `E` and call the other two `X,Y`.  Introduce the three face diagonals `U,V,Z`.  The Euler-brick equations are

\[
\boxed{
U^2=E^2+X^2,
\qquad
V^2=E^2+Y^2,
\qquad
Z^2=X^2+Y^2.
}
\]

Homogenously these define an intersection of three quadrics in

\[
\mathbf P^5_{[E:X:Y:U:V:Z]}.
\]

Thus the natural projective Euler-brick surface is a `(2,2,2)` complete-intersection model.

On the physical positive locus all six coordinates are nonzero and the Jacobian has full rank.  Stage14-e8 needs only this physical smooth locus plus the compactified double-cover description below; it does not claim that every boundary chart of the displayed projective model is already a nonsingular minimal model.

## 3. Agreement with the e4 double cover and the K3 canonical class

Stage14-e4 starts from

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad
L=-K_Y
=2H_1+2H_2-\sum_{j=1}^{4}E_j,
\]

and removes the third-face-square locus

\[
t_1^2+t_2^2=w^2.
\]

To understand that locus quantitatively, keep the double cover rather than discarding it.

On `P1 x P1`, write

\[
t_i=\frac{u_i^2-v_i^2}{2u_iv_i}.
\]

After clearing denominators, the zero divisor of `t1^2+t2^2` has bidegree `(4,4)`.  At each of the four torus-fixed corners it has multiplicity two.  Therefore its strict transform on `Y` has class

\[
4H_1+4H_2-2\sum E_j
=2L
=-2K_Y.
\]

Over `Q(i)` the numerator factors into the two `(2,2)` components corresponding to `t1+i t2` and `t1-i t2`; each strict transform has class `L`.  The pole orders are even, so the branch divisor of the quadratic extension is exactly the odd zero divisor of total class

\[
D\sim2L=-2K_Y.
\]

For the normalization of the double cover

\[
\pi:Z\to Y,
\]

the double-cover adjunction formula gives

\[
K_Z
=\pi^*\!\left(K_Y+\frac12D\right)
=\pi^*(K_Y-K_Y)
=0.
\]

After resolving any boundary rational double points, the compactified Euler-brick surface is therefore a K3 surface.

This is the geometric reason that the e4 `thin type II` statement should not be confused with an automatic fixed power saving: the thin cover itself carries a rich two-dimensional K3 rational-point problem.

## 4. Physical Euclidean height versus projective height

For a primitive physical integral point, let

\[
H_{\max}=\max(E,X,Y,U,V,Z).
\]

Since

\[
U^2=E^2+X^2,
\quad
V^2=E^2+Y^2,
\quad
Z^2=X^2+Y^2,
\]

all three face diagonals satisfy

\[
U,V,Z\le D_{\mathbf R}.
\]

Also `E,X,Y<=D_R`, hence

\[
\boxed{H_{\max}\le D_{\mathbf R}.}
\]

Conversely

\[
D_{\mathbf R}
=\sqrt{E^2+X^2+Y^2}
\le\sqrt3\,H_{\max}.
\]

Therefore

\[
\boxed{
H_{\max}\le D_{\mathbf R}\le\sqrt3 H_{\max}.
}
\]

So the Stage14-e physical ordering is a genuine bounded-height ordering on this K3; no hidden exponential height change is present.

## 5. Elementary quantitative projection

The K3 description explains the difficulty, but an unconditional quantitative envelope can be obtained without solving K3 point counting.

Take a primitive unordered Euler brick

\[
a<b<c.
\]

The two largest edges satisfy

\[
b^2+c^2=z^2
\]

for an integer face diagonal `z`.  Since

\[
z^2=b^2+c^2\le a^2+b^2+c^2\le B^2,
\]

we have

\[
z\le B.
\]

Thus every brick projects to an ordinary positive integer Pythagorean triple

\[
(b,c,z),
\qquad z\le B.
\]

Let `P(B)` denote the number of unordered positive Pythagorean triples with hypotenuse at most `B`, including nonprimitive multiples.

By the Euclid parametrization every such triple is

\[
k(m^2-n^2),
\qquad 2kmn,
\qquad k(m^2+n^2),
\]

with the usual primitive/parity conditions on `(m,n)`.  Dropping those restrictions only enlarges the count, and therefore

\[
P(B)
\le
\sum_{m\le\sqrt B}
\sum_{n<m}
\frac{B}{m^2+n^2}.
\]

For fixed `m`,

\[
\sum_{n<m}\frac1{m^2+n^2}
\le\frac{m}{m^2}
=\frac1m.
\]

Hence

\[
\boxed{P(B)\ll B\log B.}
\]

This part is completely elementary.

## 6. Fixed Pythagorean projection: divisor bound for the remaining edge

Fix the projected pair `(b,c)`.  A possible remaining edge `a` must in particular satisfy

\[
a^2+b^2=u^2
\]

for an integer `u`.

Factor:

\[
(u-a)(u+a)=b^2.
\]

Thus every candidate `a` determines a factor pair of `b^2`.  Parity, positivity, the inequality `a<b`, the second face equation `a^2+c^2=\square`, and primitivity only remove candidates.

Therefore the number of completions above a fixed projected Pythagorean pair is at most

\[
\boxed{\tau(b^2)}
\]

(and in fact at most half this many if one records unordered factor pairs).

Consequently

\[
R_{\rm EB}(B)
\le
P(B)\max_{n\le B}\tau(n^2).
\]

The standard maximal-order divisor bound gives

\[
\max_{n\le B}\tau(n^2)
=
\exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right).
\]

Combining with `P(B)<<B log B`, Stage14-e8 obtains

\[
\boxed{
R_{\rm EB}(B)
\ll
B\log B
\exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right).
}
\]

Equivalently,

\[
\boxed{R_{\rm EB}(B)=B^{1+o(1)}\quad\text{as an upper envelope}.}
\]

In epsilon notation, for every fixed `epsilon>0`,

\[
\boxed{
R_{\rm EB}(B)=O_{\epsilon}(B^{1+\epsilon}).
}
\]

This theorem is independent of the e4 thin-set zero-density theorem.

## 7. What this bound does and does not improve

Stage14-e4 already proves, by a general thin-set theorem plus toric equidistribution,

\[
R_{\rm EB}(B)=o\!\left(B(\log B)^5\right).
\]

Stage14-e8 now has the second, independent statement

\[
R_{\rm EB}(B)
\ll
B\log B\exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right).
\]

These estimates control different aspects:

- e4 proves genuine zero density relative to the ambient main term;
- e8 proves that the Euler-brick population has polynomial upper exponent at most `1`, up to a subpower multiplicity factor.

However, the e8 divisor envelope does **not** imply

\[
R_{\rm EB}(B)\ll B(\log B)^A
\qquad(A<5),
\]

and does not imply

\[
R_{\rm EB}(B)\ll B^{1-\delta}
\]

for a fixed `delta>0`.

So the planned phrase “quantitative saving beyond e4” cannot honestly be locked in the strong relative sense.

The correct lock is:

```text
INDEPENDENT_QUANTITATIVE_ENVELOPE_PROVED=true
QUANTITATIVE_RELATIVE_SAVING_PROVED=false
```

## 8. Exact finite census under the physical height

The e7 exact ledger already supplies 17 cutoffs.  Representative unique-brick counts are

| `B` | `R_EB(B)` | `R_EB/sqrt(B)` | third-square raw incidence fraction |
|---:|---:|---:|---:|
| 2,000 | 7 | 0.156525 | 4.3451e-3 |
| 10,000 | 18 | 0.180000 | 1.2943e-3 |
| 50,000 | 42 | 0.187830 | 3.7968e-4 |
| 200,000 | 82 | 0.183358 | 1.29695e-4 |
| 1,000,000 | 219 | 0.219000 | 4.75454e-5 |

At `B=10^6`,

\[
\boxed{R_{\rm EB}=219}
\]

and

\[
\boxed{
\frac{3R_{\rm EB}}{E_{\rm raw}}
=4.75453638494\times10^{-5}.
}
\]

The finite `R_EB/sqrt(B)` statistic remains strikingly small and slowly varying, but Stage14-e8 does not promote it to a theorem.

## 9. Effective power fits are diagnostic only

A log--log fit

\[
R_{\rm EB}(B)\approx C B^{\alpha}
\]

over all 17 e7 cutoffs gives

\[
\alpha_{B\ge2000}=0.5475214\ldots.
\]

Nested-window fits give approximately

```text
min B       fitted alpha
2,000       0.5475
10,000      0.5404
50,000      0.5571
100,000     0.5827
200,000     0.6306
```

The drift is substantial.  Therefore neither

\[
R_{\rm EB}(B)\asymp\sqrt B
\]

nor even a stable empirical power exponent is frozen.

The finite statement is only

```text
SQRT_B_FINITE_CANDIDATE_ONLY=true
```

## 10. Finite audit of the divisor envelope

At `B=10^6`, the audit finds

\[
P(10^6)=1,980,642
\]

integer Pythagorean triples with hypotenuse at most `10^6`.

Also

\[
\max_{n\le10^6}\tau(n^2)=3645,
\]

first attained at

\[
n=720720.
\]

Thus the most naive finite realization of the proof gives the enormous ceiling

\[
\frac12 P(10^6)\max\tau(n^2)
=3,609,720,045,
\]

versus the actual `219` bricks.

This gap is informative: the theorem loses almost everything in the completion multiplicity.  A future improvement must exploit **simultaneous** completion of both projected legs, not merely one divisor equation.

That identifies a concrete arithmetic bottleneck for any attempt to turn the observed square-root signal into a theorem.

## 11. Literature boundary

The literature refresh is recorded in

```text
stages/stage14/14-e8/literature-euler-brick-count-audit.md
```

The key current facts are:

- Rathbun gives very large exhaustive cuboid tables under different ordering conventions;
- Himane studies primitive Euler-brick generation;
- Peschmann 2026 supplies a structural theorem that every primitive Euler brick comes from a unique master tuple after the odd-edge/labelling convention;
- no primary source found in the current search gives the present Euclidean-height `R_EB(B)` asymptotic or a fixed `B^(1-delta)` / `B log^A, A<5` upper bound.

Hence

```text
DIRECT_STAGE14_E8_EUCLIDEAN_COUNT=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

is retained.

## 12. Locked conclusion

```text
STAGE14_E8=COMPLETE_K3_AND_SUBPOWER_MULTIPLICITY_ENVELOPE
EULER_BRICK_K3_MODEL_LOCKED=true
EULER_BRICK_PROJECTIVE_MODEL=THREE_QUADRICS_IN_P5
EULER_BRICK_DOUBLE_COVER_BRANCH_CLASS=-2K_Y
PHYSICAL_HEIGHT_PROJECTIVE_COMPARISON_LOCKED=true

E4_ZERO_DENSITY_RETAINED=true
E8_INDEPENDENT_QUANTITATIVE_ENVELOPE_PROVED=true
EULER_BRICK_POWER_EXPONENT_UPPER_ENVELOPE=1+o(1)
QUANTITATIVE_RELATIVE_SAVING_PROVED=false
FIXED_POWER_SAVING_PROVED=false
LOG_POWER_SAVING_BELOW_5_PROVED=false

MAX_EXACT_CENSUS_B=1000000
EULER_BRICKS_AT_B1E6=219
SQRT_B_FINITE_CANDIDATE_ONLY=true
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false

NEXT_E_SUPPLEMENT=Stage14-e9 gcd/lcm and local-statistics decomposition
```

Stage14-e9 can now use this K3/divisor bottleneck as a control target: the hope is that gcd/lcm and finite-local statistics explain why simultaneous completion is vastly rarer than the one-leg divisor envelope permits.
