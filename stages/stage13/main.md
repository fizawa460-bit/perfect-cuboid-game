# Stage13 — canonical working file

> **STATUS:** `STAGE13_3B_COMPLETE_13_3C_NEXT`
>
> **SCOPE:** primitive canonical face-ratio analysis
>
> **CANONICAL_WORKING_FILE:** `stages/stage13/main.md`

This file is the living mathematical source for Stage13. The completed Stage13-1 and Stage13-2 initial documents remain under `initial/` as provenance; their active definitions and decomposition are consolidated here before the Stage13-3 analysis.

## §1. Task 13-1 — definition of the observed ratio

For \(B\ge1\), consider positive integer quadruples

\[
(a,b,c,d)\in\mathbf Z_{>0}^4
\]

satisfying

\[
a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The strict order is the canonical representative under edge permutations, and the gcd condition removes scaled copies.

Define

\[
Q_{ab}=a^2+b^2,\qquad Q_{ac}=a^2+c^2,\qquad Q_{bc}=b^2+c^2.
\]

The Stage13 one-face population consists of objects for which exactly one of these three quantities is a positive integer square. Its three categories are

\[
\begin{aligned}
\mathcal E_{ab}(B)&=\{Q_{ab}=\square,\ Q_{ac},Q_{bc}\ne\square\},\\
\mathcal E_{ac}(B)&=\{Q_{ac}=\square,\ Q_{ab},Q_{bc}\ne\square\},\\
\mathcal E_{bc}(B)&=\{Q_{bc}=\square,\ Q_{ab},Q_{ac}\ne\square\},
\end{aligned}
\]

with counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B),
\]

and

\[
N_1(B)=N_{ab}(B)+N_{ac}(B)+N_{bc}(B).
\]

The labels \(ab,ac,bc\) are **size positions after canonical ordering**, not fixed coordinate-axis labels.

At the finite cutoff \(B=100000\), the locked Stage13-1 data are

\[
\mathbf N(100000)=(84146,43180,40704),
\]

hence

\[
N_{ab}:N_{ac}:N_{bc}\approx2.0673:1.0608:1
\]

when normalized by \(N_{bc}\), and

\[
\mathbf P(100000)=\frac{\mathbf N(100000)}{N_1(100000)}\approx(0.50078,0.25698,0.24224).
\]

These values motivate the phrase “observed near \(2:1:1\)”. Stage13 does not assume that

\[
\mathbf P(B)\to(1/2,1/4,1/4),
\]

or even that this is the correct limiting vector.

Stage12 and Stage13 counts are not identified automatically. Stage12 proves an asymptotic for a primitive **oriented** count, while Stage13 uses primitive canonical exactly-one-face objects. Any bridge must account explicitly for orientation, representation multiplicity, parity and canonical projection.

## §2. Task 13-2 — structural decomposition

Let

\[
\mathcal U(B)=\left\{(a,b,c,d):a<b<c,\ \gcd(a,b,c)=1,\ a^2+b^2+c^2=d^2,\ d\le B\right\}.
\]

No face condition is imposed in \(\mathcal U(B)\). For \(x\in\mathcal U(B)\), let

\[
I_{ab}(x)=\mathbf1_{Q_{ab}=\square},\quad I_{ac}(x)=\mathbf1_{Q_{ac}=\square},\quad I_{bc}(x)=\mathbf1_{Q_{bc}=\square}.
\]

Before the exactly-one sieve, define raw incidence counts

\[
A_{ab}=\sum_{x\in\mathcal U(B)}I_{ab}(x),\quad A_{ac}=\sum_{x\in\mathcal U(B)}I_{ac}(x),\quad A_{bc}=\sum_{x\in\mathcal U(B)}I_{bc}(x).
\]

Define the pair overlaps

\[
A_{ab,ac}=\sum I_{ab}I_{ac},\qquad A_{ab,bc}=\sum I_{ab}I_{bc},\qquad A_{ac,bc}=\sum I_{ac}I_{bc},
\]

and the three-face overlap

\[
A_3=\sum I_{ab}I_{ac}I_{bc}.
\]

Then inclusion-exclusion gives the exact identities

\[
\boxed{N_{ab}=A_{ab}-A_{ab,ac}-A_{ab,bc}+A_3}
\]

and cyclically,

\[
\boxed{N_{ac}=A_{ac}-A_{ab,ac}-A_{ac,bc}+A_3,}
\]

\[
\boxed{N_{bc}=A_{bc}-A_{ab,bc}-A_{ac,bc}+A_3.}
\]

Also

\[
N_1=A_{ab}+A_{ac}+A_{bc}-2(A_{ab,ac}+A_{ab,bc}+A_{ac,bc})+3A_3.
\]

This separates two logically different possibilities: the near \(2:1:1\) shape is already present in the raw incidence vector \(\mathbf A(B)\), or it is created/materially reshaped by the overlap correction.

The remaining structural layers to test are canonical size-order chamber \(0<a<b<c\), primitive projection, parity (especially the 2-adic branch), Stage12 representation/fiber multiplicity, odd-prime local density, and cutoff/boundary effects.

A full \(S_3\) orientation lift by itself cannot create the leading \(2\): for an object with one distinguished unordered face, its six edge permutations place that face on each fixed coordinate plane exactly twice, so the axis-labelled multiplicity is \(2:2:2=1:1:1\).

No Euler-product factorization, constant bridge to Stage12, or limiting \(2:1:1\) theorem is asserted at this point.

## §3. Task 13-3 — origin of the leading 2

### §3.1 Stage13-3a question

The first discriminator is deliberately cheap and decisive:

> Is the leading near-\(2\) already visible in \(\mathbf A(B)=(A_{ab},A_{ac},A_{bc})\) before the exactly-one sieve?

If yes, overlap cannot be the mechanism that *creates* the leading \(2\). If no, the pair/triple-overlap layer would require detailed analysis first.

### §3.2 Complete finite enumeration used for 13-3a

The audit script is

```text
stages/stage13/scripts/13-3/raw_incidence.py
```

and writes

```text
stages/stage13/data/13-3/raw_incidence_report.json
```

For a bound \(B\), it generates every positive integer Pythagorean triple with hypotenuse at most \(B\), including nonprimitive scalings. It builds two indexes:

\[
x^2+y^2=p^2
\]

for face representations with hypotenuse \(p\), and

\[
p^2+z^2=d^2,\qquad d\le B
\]

for extensions having \(p\) as a leg.

Gluing on the common \(p\) gives

\[
x^2+y^2+z^2=d^2
\]

with at least one integral face diagonal. Conversely, every object in \(\mathcal U(B)\) having at least one integral face can be obtained in this way by choosing one of its integral faces and denoting that face diagonal by \(p\). Thus this is complete for the raw-incidence population, although a multi-face object can be generated more than once.

The script sorts the three edges and requires \(a<b<c\), imposes \(\gcd(a,b,c)=1\), deduplicates by \((a,b,c,d)\), recomputes all three square conditions directly, checks the inclusion-exclusion identities, and at \(B=100000\) independently reproduces the locked Stage13-1 exactly-one vector \((84146,43180,40704)\).

The last check is important: 13-3a is not obtained merely by adding old reported overlap counts back by hand.

### §3.3 Finite results

The multi-bound audit gives:

| \(B\) | raw \(A_{ab}\) | raw \(A_{ac}\) | raw \(A_{bc}\) | raw ratio normalized by \(bc\) | exactly-two objects |
|---:|---:|---:|---:|---|---:|
| 1,000 | 306 | 160 | 138 | 2.2174 : 1.1594 : 1 | 2 |
| 2,000 | 702 | 372 | 370 | 1.8973 : 1.0054 : 1 | 5 |
| 5,000 | 2,300 | 1,138 | 1,077 | 2.1356 : 1.0566 : 1 | 15 |
| 10,000 | 5,281 | 2,740 | 2,659 | 1.9861 : 1.0305 : 1 | 25 |
| 20,000 | 12,407 | 6,284 | 6,105 | 2.0323 : 1.0293 : 1 | 42 |
| 50,000 | 37,014 | 19,080 | 17,905 | 2.0672 : 1.0656 : 1 | 62 |
| 100,000 | 84,212 | 43,236 | 40,760 | 2.0660 : 1.0607 : 1 | 89 |

At \(B=100000\),

\[
\boxed{\mathbf A=(84212,43236,40760)}
\]

with raw proportions

\[
\frac{\mathbf A}{A_{ab}+A_{ac}+A_{bc}}\approx(0.5006421,0.2570389,0.2423190).
\]

The overlap counts are

\[
A_{ab,ac}=33,\qquad A_{ab,bc}=33,\qquad A_{ac,bc}=23,\qquad A_3=0.
\]

Therefore

\[
\begin{aligned}
N_{ab}&=84212-33-33=84146,\\
N_{ac}&=43236-33-23=43180,\\
N_{bc}&=40760-33-23=40704,
\end{aligned}
\]

exactly reproducing the Stage13-1 locked data.

The exactly-one sieve removes only

\[
(66,56,56)
\]

incidences, i.e. approximately

\[
(0.0784\%,\,0.1295\%,\,0.1374\%)
\]

of the three raw components respectively. The \(L^\infty\) change in the normalized proportion vector is only

\[
1.3756\times10^{-4}.
\]

### §3.4 13-3a conclusion

The finite computation decisively answers the discriminator posed in §3.1:

\[
\boxed{\text{the near }2:1:1\text{ shape is already present before the exactly-one sieve.}}
\]

Thus the pair-overlap / exact-one correction does **not** generate the leading \(2\) at the audited cutoffs. It produces only a small perturbation.

This is a finite enumerative result. It does **not** prove that overlaps are asymptotically negligible, nor does it prove a limiting \(2:1:1\) ratio.

The leading candidate mechanism therefore moves one layer earlier: the next test is the **canonical size-order / geometric chamber effect**. This is Stage13-3b.

```text
STAGE13_3A=COMPLETE
RAW_INCIDENCE_ALREADY_NEAR_2_1_1=true
OVERLAP_GENERATES_LEADING_2=false_at_audited_finite_bounds
ASYMPTOTIC_CLAIM=false
NEXT=Stage13-3b canonical size-order / geometric density
```

### §3.5 Stage13-3b question

The next discriminator is more precise than “does sorting create the bias?” Pure relabelling cannot: if all three faces carried the same density, restricting to the same chamber \(0<a<b<c\) would still give \(1:1:1\). The question is instead:

> Does the interaction between the canonical size-order chamber and the real one-face density naturally create an \(ab\) excess of approximately the observed size?

The support script and report are

```text
stages/stage13/scripts/13-3/geometric_chamber.py
stages/stage13/data/13-3/geometric_chamber_report.json
```

### §3.6 Exact archimedean directional weight

Consider first a distinguished integral \(ab\) face. Introduce its face diagonal \(p\) and write the real one-face variety locally as

\[
F_1=a^2+b^2-p^2=0,\qquad F_2=p^2+c^2-d^2=0.
\]

Using \((a,b,c)\) as free coordinates and solving for \((p,d)\),

\[
\left|\det\frac{\partial(F_1,F_2)}{\partial(p,d)}\right|=4pd.
\]

Thus, up to a common constant, the Gelfand--Leray density is

\[
\frac{da\,db\,dc}{4pd}.
\]

Put

\[
(a,b,c)=r(x,y,z),\qquad x^2+y^2+z^2=1,\qquad r=d.
\]

Then \(p=r\sqrt{x^2+y^2}\) and

\[
da\,db\,dc=r^2\,dr\,d\omega.
\]

The factors of \(r\) cancel, leaving the angular weight

\[
\boxed{w_{ab}(x,y,z)=\frac1{\sqrt{x^2+y^2}}.}
\]

The same calculation gives

\[
\boxed{w_{ac}=\frac1{\sqrt{x^2+z^2}},\qquad w_{bc}=\frac1{\sqrt{y^2+z^2}}.}
\]

This is an exact statement about the real local density on the three one-face varieties. It is **not** yet a theorem that the global integer counts have these archimedean constants without additional arithmetic factors.

### §3.7 What canonical ordering changes

Normalize by \(d\) and let

\[
R=\{(x,y,z)\in S^2:0<x<y<z\}.
\]

Inside \(R\),

\[
x^2+y^2<x^2+z^2<y^2+z^2,
\]

so pointwise

\[
\boxed{w_{ab}>w_{ac}>w_{bc}.}
\]

Thus the canonical chamber places the smallest two edges on the face with the largest real-density weight. This is the first mechanism tested so far that produces the observed direction of the bias before any parity or odd-prime correction is introduced.

Two controls are important.

First, with a uniform angular weight, every direction sees the same chamber area

\[
\operatorname{area}(R)=\frac{\pi}{12},
\]

so **canonical relabelling alone gives \(1:1:1\)**.

Second, on the full positive octant \(S^2_+\), coordinate symmetry gives equal directional integrals. For example

\[
J=\int_{S^2_+}\frac{d\omega}{\sqrt{x^2+y^2}}=\frac{\pi^2}{4},
\]

and the same value holds for \(ac\) and \(bc\). Therefore removing the size-order chamber restores the symmetric ratio \(1:1:1\).

The asymmetry is specifically the interaction

\[
\boxed{\text{canonical chamber}\;\times\;\text{one-face }1/p\text{ real-density weight}.}
\]

### §3.8 Ordered-chamber integrals

Use spherical coordinates

\[
x=\sin\theta\cos\varphi,\qquad y=\sin\theta\sin\varphi,\qquad z=\cos\theta.
\]

The chamber is

\[
\frac\pi4<\varphi<\frac\pi2,\qquad 0<\theta<\arctan(\csc\varphi).
\]

Define

\[
I_{uv}=\int_R w_{uv}\,d\omega.
\]

The audit independently reproduces

\[
\begin{aligned}
I_{ab}&=0.659705248705705\ldots,\\
I_{ac}&=0.302699752672608\ldots,\\
I_{bc}&=0.271295548757857\ldots.
\end{aligned}
\]

The strict order \(I_{ab}>I_{ac}>I_{bc}\) follows already from the pointwise inequality. The numerical ratios are

\[
I_{ab}:I_{ac}:I_{bc}=2.1794046506:1:0.8962529581
\]

when normalized by \(I_{ac}\), or

\[
\boxed{2.4316847502:1.1157564290:1}
\]

when normalized by \(I_{bc}\).

There is also the exact sum identity

\[
\boxed{I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}.}
\]

Indeed, \(w_{ab}+w_{ac}+w_{bc}\) is permutation-symmetric, so its integral is the same on all six order chambers. Since each individual weight integrates to \(J=\pi^2/4\) over the full positive octant,

\[
6(I_{ab}+I_{ac}+I_{bc})=3J=\frac{3\pi^2}{4}.
\]

The corresponding geometric proportion vector is

\[
\boxed{\mathbf P_{\rm geom}\approx(0.53473693,0.24535918,0.21990389).}
\]

### §3.9 Comparison with the raw incidence data

At \(B=100000\), Stage13-3a gave

\[
\mathbf P_{\rm raw}\approx(0.50064206,0.25703890,0.24231903)
\]

and raw \(bc\)-normalized ratio

\[
2.06604514:1.06074583:1.
\]

The chamber model predicts

\[
2.43168475:1.11575643:1.
\]

Thus it gets the ordering and the scale of the leading \(ab\) excess right, but it **overstates** the bias: relative to the observed \(bc\)-normalized ratios, the geometric \(ab\) component is about \(17.7\%\) high and the \(ac\) component about \(5.2\%\) high.

A descriptive comparison makes the size of the effect clearer. At \(B=100000\), the \(L^1\) distance of the raw proportion vector from the symmetric baseline \((1/3,1/3,1/3)\) is

\[
0.33461746,
\]

whereas its distance from \(\mathbf P_{\rm geom}\) is only

\[
0.06818974.
\]

Thus this chamber model removes about \(79.6\%\) of the finite \(L^1\) discrepancy from \(1:1:1\). Across the seven audited cutoffs \(1000\le B\le100000\), the same descriptive fraction ranges from about \(68.2\%\) to \(85.6\%\).

This percentage is a diagnostic, not a theorem or a statistical confidence statement. It only quantifies how much closer the observed finite vector lies to the archimedean chamber model than to the fully symmetric baseline.

### §3.10 13-3b conclusion

Stage13-3b gives a strong structural answer but not the final arithmetic constant.

\[
\boxed{\text{canonical ordering plus the }1/p\text{ archimedean density is a dominant mechanism for the leading }2.}
\]

More precisely:

1. full orientation / full positive-octant symmetry gives \(1:1:1\);
2. canonical relabelling with uniform weight still gives \(1:1:1\);
3. after imposing \(0<a<b<c\), the exact one-face real-density weights satisfy \(w_{ab}>w_{ac}>w_{bc}\);
4. their chamber integrals produce an \(ab\)-enhanced ratio of the correct qualitative and approximate quantitative scale;
5. the model is not complete, because it predicts a stronger bias than the raw integer data.

Therefore the leading \(2\) no longer looks mysterious at the archimedean level: the shortest-pair face has the smallest face diagonal and hence the largest real-density weight throughout the canonical chamber. The remaining problem is to explain why arithmetic effects flatten

\[
2.4317:1.1158:1
\]

toward the observed

\[
2.0660:1.0607:1.
\]

The next inexpensive discriminator is the parity / \(2\)-adic layer. Stage13-3c will split the raw incidence vector by edge parity and face direction before moving to representation multiplicity or odd-prime local factors.

No limiting \(2:1:1\) ratio, no global Euler product, and no equality between these chamber integrals and the true asymptotic constants is claimed here.

```text
STAGE13_3A=COMPLETE
STAGE13_3B=COMPLETE
ARCHIMEDEAN_CHAMBER_DIRECTION_ORDER=ab>ac>bc
CANONICAL_RELABELING_ALONE_GENERATES_BIAS=false
CANONICAL_CHAMBER_TIMES_REAL_DENSITY_GENERATES_BIAS=true
GEOMETRIC_MODEL_BC_NORMALIZED=2.4316847502:1.1157564290:1
RAW_B100000_BC_NORMALIZED=2.0660451423:1.0607458292:1
GEOMETRIC_MODEL_IS_COMPLETE_ARITHMETIC_EXPLANATION=false
ASYMPTOTIC_CLAIM=false
NEXT=Stage13-3c parity / 2-adic correction
```
