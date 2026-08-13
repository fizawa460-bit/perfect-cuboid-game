# Stage13 — canonical working file

> **STATUS:** `STAGE13_COMPLETE`
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

### §3.11 Stage13-3c question

Stage13-3b leaves a clean residual problem: why is the integer ratio flatter than the archimedean chamber ratio? The next discriminator is the prime \(2\):

> Does parity / \(2\)-adic structure supply a direction-dependent correction large enough to explain the flattening from the geometric ratio toward the observed raw ratio?

The support audit is

```text
stages/stage13/scripts/13-3/parity_2adic.py
stages/stage13/data/13-3/parity_2adic_report.json
```

and uses the same complete primitive canonical raw-incidence population as Stage13-3a.

### §3.12 Exact primitive parity structure

Let

\[
a^2+b^2+c^2=d^2,\qquad \gcd(a,b,c)=1.
\]

Modulo \(4\), a primitive solution has exactly one odd edge and \(d\) is odd. Write the two even edges as \(e_1,e_2\). Modulo \(8\), the space equation permits only

\[
v_2(e_1)=v_2(e_2)=1
\]

or

\[
v_2(e_1),v_2(e_2)\ge2;
\]

a mixed branch would give \(1+4+0\equiv5\pmod8\).

If at least one face diagonal is integral, the \(v_2(e_1)=v_2(e_2)=1\) branch is impossible: an odd-even face has square sum \(1+4\equiv5\pmod8\), while the even-even face has square sum \(4+4\equiv8\pmod{16}\). Therefore every primitive raw-incidence object satisfies

\[
\boxed{\text{one odd edge},\qquad d\text{ odd},\qquad 4\mid e_1,\quad4\mid e_2.}
\]

The finite audit confirms this for every audited object; at \(B=100000\) all \(168119\) distinct primitive canonical objects with at least one integral face lie in this branch.

### §3.13 Standalone prime-2 density is symmetric

The one-face varieties \(V_{ab},V_{ac},V_{bc}\) are carried into one another by coordinate permutations, and the primitive local condition is invariant under the same permutations. Hence a standalone \(p=2\) local density, before coupling to the real order chamber or representation fibers, is common to the three labels.

Thus the universal prime-2 admissibility sieve cannot by itself create a direction-dependent \(ab/ac/bc\) bias. Any visible prime-2 effect on canonical counts must come from coupling between the 2-adic type and another nonsymmetric layer.

### §3.14 Face-relative parity split

Split each raw incidence into:

- **OE:** the distinguished integral face contains the unique odd edge;
- **EE:** the distinguished integral face is the pair of even edges.

At \(B=100000\),

\[
\mathbf A^{OE}=(50320,24059,22386),
\]

\[
\mathbf A^{EE}=(33892,19177,18374),
\]

and \(\mathbf A=\mathbf A^{OE}+\mathbf A^{EE}\). Their \(bc\)-normalized ratios are

\[
\boxed{2.24783347:1.07473421:1}
\]

and

\[
\boxed{1.84456297:1.04370306:1}.
\]

The corresponding normalized proportion vectors are

\[
\mathbf P^{OE}\approx(0.520023,0.248633,0.231344),
\]

\[
\mathbf P^{EE}\approx(0.474392,0.268424,0.257184).
\]

The OE and EE shares of all raw incidences are about \(57.53\%\) and \(42.47\%\). Descriptively, a finite cancellation is visible: OE puts the \(ab\) share above one half while EE puts it below one half, and their mixture lands at the raw \(P_{ab}\approx0.500642\).

This is not a causal factorization of an asymptotic constant: each conditional vector still contains the real chamber, odd-prime arithmetic, representation multiplicity, and finite-boundary effects.

### §3.15 Finer 2-adic signatures

For OE incidences the audit records \((v_2(e_{\rm face}),v_2(e_{\rm remaining}))\); for EE incidences it records the two even-face valuations. Values \(4,5,\ldots\) are grouped as \(4+\) for the finite diagnostic.

At \(B=100000\), the total-variation distances between the resulting signature distributions are

\[
\begin{aligned}
d_{\rm TV}(ab,ac)&=0.04937\ldots,\\
d_{\rm TV}(ab,bc)&=0.04832\ldots,\\
d_{\rm TV}(ac,bc)&=0.03819\ldots.
\end{aligned}
\]

Thus detailed prime-2 signature mixes are not identical after canonical ordering, but the differences are only at the few-percent level in this finite diagnostic.

### §3.16 13-3c conclusion

Prime \(2\) matters strongly for admissibility: both even edges must be divisible by \(4\). But that universal local restriction is permutation-symmetric and therefore is not, by itself, the missing direction-dependent factor.

The finite OE/EE decomposition does reveal a real coupling between parity type and canonical size order, and the mixture visibly flattens the aggregate vector. Nevertheless both subpopulations retain a substantial \(ab\) excess, and the finer 2-adic signature differences are modest.

Accordingly,

\[
\boxed{\text{Stage13-3c does not identify prime }2\text{ as the complete correction from the geometric to the raw ratio.}}
\]

The next layer is Stage13-3d: test the Stage12 representation/fiber multiplicity after projection to the canonical size-ordered object, using the 13-3c parity signatures as controls.

No limiting \(2:1:1\) theorem, no global Euler product, and no asymptotic negligibility claim is made here.

```text
STAGE13_3A=COMPLETE
STAGE13_3B=COMPLETE
STAGE13_3C=COMPLETE
PRIMITIVE_RAW_PARITY=one_odd_two_multiples_of_4
STANDALONE_P2_LOCAL_FACTOR_DIRECTION_BIAS=false
FINITE_OE_BC_NORMALIZED=2.2478334673:1.0747342089:1
FINITE_EE_BC_NORMALIZED=1.8445629694:1.0437030587:1
P2_ORDER_COUPLING_VISIBLE=true
P2_LAYER_COMPLETE_EXPLANATION=false
ASYMPTOTIC_CLAIM=false
NEXT=Stage13-3d representation / fiber multiplicity
```

### §3.17 Stage13-3d question

Stage13-3c leaves representation/fiber multiplicity as the next possible source of the missing arithmetic correction. The question is:

> Does the Stage12 weight \(G(p)-1\), after projection to a canonical size-ordered object with a distinguished integral face, become a direction-dependent or otherwise variable fiber multiplicity capable of changing the \(ab:ac:bc\) ratio?

The support audit is

```text
stages/stage13/scripts/13-3/representation_fiber.py
stages/stage13/data/13-3/representation_fiber_report.json
```

It independently reconstructs the Stage12 ordered distinguished-face records and projects them to the same primitive canonical raw incidences used in Stage13-3a.

### §3.18 What \(G(p)-1\) counts

Recall

\[
G(p)=\prod_{q\mid p,\ q\equiv1\pmod4}(2v_q(p)+1).
\]

The standard sum-of-two-squares formula gives

\[
r_2(p^2)=4G(p),
\]

where \(r_2\) counts signed ordered integer pairs \((x,y)\) with \(x^2+y^2=p^2\). Exactly four of these are the axis solutions

\[
(\pm p,0),\qquad(0,\pm p).
\]

After removing them and dividing by the four independent sign choices of a positive ordered pair,

\[
\boxed{
G(p)-1
=
\#\{(x,y)\in\mathbf Z_{>0}^2:x^2+y^2=p^2\}.
}
\]

Thus Stage12's variable-looking weight does not assign \(G(p)-1\) copies to one fixed face. It enumerates all **different ordered positive face representations** sharing the same diagonal \(p\).

For a fixed unordered positive face \(\{x,y\}\), \(x=y\) is impossible in an integer right triangle, so exactly two of those ordered representations correspond to that face:

\[
(x,y),\qquad(y,x).
\]

### §3.19 Uniqueness of the complementary Stage12 parameter

Fix a Stage13 raw incidence: a primitive canonical object together with one distinguished integral face. Let \(p\) be that face diagonal and \(z\) the complementary edge, so

\[
p^2+z^2=d^2.
\]

Set

\[
u=d-z,\qquad v=d+z.
\]

Then \(uv=p^2\). With

\[
h=\gcd(u,v),
\]

the coprime integers \(u/h\) and \(v/h\) have square product, hence each is a square. Therefore uniquely

\[
u=hr^2,\qquad v=hs^2,\qquad r<s,\qquad(r,s)=1,
\]

and

\[
p=hrs,\qquad z=\frac{h(s^2-r^2)}2,\qquad d=\frac{h(r^2+s^2)}2.
\]

So once the distinguished face and its ordered legs are fixed, there is exactly one Stage12 \((h,r,s)\) record. There is no additional hidden multiplicity in the second Pythagorean triangle.

### §3.20 Exact fiber bridge

Let \(\Pi_{12}\) be the Stage13-2 bridge map from primitive Stage12 oriented records to

\[
(\text{canonical object},\text{distinguished canonical face},\sigma),
\]

where \(\sigma\in S_3\) retains the Stage12 edge orientation.

For each canonical raw face incidence:

1. exactly two orientations \(\sigma\) are supported, obtained by swapping the two distinguished face legs while keeping the complementary edge in the Stage12 third position;
2. for each supported \(\sigma\),
   \[
   \boxed{m_{12}(x,f,\sigma)=1;}
   \]
3. after forgetting \(\sigma\), the total projection multiplicity is exactly
   \[
   \boxed{2.}
   \]

Consequently, if \(C^{\rm proj}_{\rm prim,uv}(B)\) denotes the Stage12 primitive oriented records whose canonical distinguished face lands in category \(uv\), then for every \(B\)

\[
\boxed{C^{\rm proj}_{\rm prim,ab}(B)=2A_{ab}(B),}
\]

\[
\boxed{C^{\rm proj}_{\rm prim,ac}(B)=2A_{ac}(B),}
\]

\[
\boxed{C^{\rm proj}_{\rm prim,bc}(B)=2A_{bc}(B).}
\]

Summing the three directions gives the exact bridge

\[
\boxed{
C_{\rm prim}(B)
=2\bigl(A_{ab}(B)+A_{ac}(B)+A_{bc}(B)\bigr).
}
\]

This remains exact for multi-face objects because the distinguished face is retained: a two-face object contributes two raw incidences and four Stage12 oriented records; a hypothetical three-face object would contribute three incidences and six records.

The same factor \(2\) holds separately in the OE and EE strata from Stage13-3c, so there is no hidden parity-dependent fiber correction.

### §3.21 Finite audit

The independent finite audit reproduces both the Stage13-3a directional raw counts and the historical Stage12 raw-oriented locks. For the primitive bridge it gives:

| \(B\) | \(A_{ab}+A_{ac}+A_{bc}\) | Stage12 primitive oriented | ratio |
|---:|---:|---:|---:|
| 1,000 | 604 | 1,208 | 2 |
| 2,000 | 1,444 | 2,888 | 2 |
| 5,000 | 4,515 | 9,030 | 2 |
| 10,000 | 10,680 | 21,360 | 2 |
| 20,000 | 24,796 | 49,592 | 2 |
| 50,000 | 73,999 | 147,998 | 2 |
| 100,000 | 168,208 | 336,416 | 2 |

At \(B=100000\), the directional projection is exactly

\[
(168424,86472,81520)
=2(84212,43236,40760).
\]

All \(336416\) supported full-orientation fibers in the audit have size \(1\), and all \(168208\) canonical face incidences have exactly two supported orientations. The audit also checks the \(G(p)-1\) representation identity and the unique hyperbola reconstruction on every generated value needed at each cutoff.

Thus the finite data agree with the exact combinatorial proof without exception.

### §3.22 A theorem-level transfer from Stage12

The exact bridge now permits one immediate transfer of the frozen Stage12 theorem. Since

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3,
\]

we obtain for the **total primitive canonical raw incidence**

\[
\boxed{
A_{ab}(B)+A_{ac}(B)+A_{bc}(B)
\sim
\frac{\kappa}{24\pi}B(\log B)^3.
}
\]

Equivalently, using \(\eta=\pi\kappa\), the constant is \(\eta/(24\pi^2)\).

This is a theorem about the sum of the three raw incidence counts. It does not separate the three directional constants and therefore does not prove a limiting \(2:1:1\) ratio.

Combining the bridge with the exact inclusion-exclusion identity from §2 also gives

\[
\boxed{
N_1(B)
=
\frac12C_{\rm prim}(B)
-2\bigl(A_{ab,ac}+A_{ab,bc}+A_{ac,bc}\bigr)
+3A_3.
}
\]

Therefore an exactly-one asymptotic with the same half-Stage12 main term would follow if the overlap correction were proved lower order. Stage13-3a supplies strong finite evidence for that statement but **not** its asymptotic proof.

### §3.23 13-3d conclusion

Stage13-3d resolves the representation/fiber ambiguity exactly:

\[
\boxed{\text{Stage12 representation/fiber multiplicity is not a direction-dependent correction.}}
\]

The variable quantity \(G(p)-1\) counts different ordered positive faces sharing \(p\); it is not a variable weight attached repeatedly to one fixed Stage13 incidence. Once a particular canonical incidence is fixed, the only projection multiplicity is the universal two-fold swap of its face legs.

Hence this layer cannot explain why the archimedean chamber prediction

\[
2.4317:1.1158:1
\]

is flatter in the actual integer data. What can still matter is the **arithmetic distribution of representation-rich values of \(p\)** across the canonical chamber: different \(p\)'s genuinely produce different incidences. That is an odd-prime / representation-density question rather than a fiber-multiplicity question.

The next step is Stage13-3e.

```text
STAGE13_3A=COMPLETE
STAGE13_3B=COMPLETE
STAGE13_3C=COMPLETE
STAGE13_3D=COMPLETE
SUPPORTED_FULL_ORIENTATION_FIBER_SIZE=1
SUPPORTED_ORIENTATIONS_PER_CANONICAL_INCIDENCE=2
CANONICAL_PROJECTION_MULTIPLICITY=2
C_PRIM_EQUALS_2_RAW_INCIDENCE_TOTAL=true
RAW_INCIDENCE_TOTAL_ASYMPTOTIC=kappa/(24*pi)*B*(log B)^3
REPRESENTATION_FIBER_DIRECTION_BIAS=false
EXACT_ONE_ASYMPTOTIC_REQUIRES_OVERLAP_CONTROL=true
NEXT=Stage13-3e odd-prime / representation-density correction
```

## §4. Task 13-4 — origin of the two near-1 components

Stage13-4 asked why the finite \(ac\) and \(bc\) populations are close without assuming an exact \(ac\leftrightarrow bc\) symmetry.

At \(B=100000\), the locked finite ratios are

\[
\frac{A_{ac}}{A_{bc}}=1.060745829\ldots,
\qquad
\frac{N_{ac}}{N_{bc}}=1.060829403\ldots.
\]

The closeness is already present before the exactly-one sieve and survives the largest audited cutoff band, so it is not created by overlap removal or by the outer cutoff boundary.

The pure-\(G\) diagnostic nearly equalizes the two directions in aggregate, but the equality is a cancellation rather than a symmetry. At \(B=100000\), the OE and EE pure-\(G\) components tilt in opposite directions, approximately

\[
(ac/bc)_{OE}\approx0.95422,
\qquad
(ac/bc)_{EE}\approx1.04547.
\]

Primitive-support reweighting then supplies much of the residual positive \(ac-bc\) tilt visible in the actual finite data. Thus the two near-1 components arise from a finite arithmetic/geometric cancellation, not from an exact involution exchanging the two categories.

```text
STAGE13_4=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
EXACT_AC_BC_SYMMETRY=false
PURE_G_AC_BC_NEAR_EQUALITY_IS_CANCELLATION=true
OVERLAP_CREATES_AC_BC_CLOSENESS=false
LARGEST_CUTOFF_BOUNDARY_CREATES_AC_BC_CLOSENESS=false
```

## §5. Task 13-5 — deviation coordinates

Define the normalized exactly-one vector

\[
P(B)=\frac1{N_1(B)}\bigl(N_{ab}(B),N_{ac}(B),N_{bc}(B)\bigr)
\]

and the finite \(2:1:1\) baseline

\[
P_0=\left(\frac12,\frac14,\frac14\right).
\]

Set

\[
\Delta(B)=P(B)-P_0,
\]

with coordinates

\[
\alpha(B)=P_{ab}(B)-\frac12,
\qquad
\beta(B)=\frac{P_{ac}(B)-P_{bc}(B)}2.
\]

Then

\[
\Delta(B)=\bigl(\alpha(B),-\alpha(B)/2+\beta(B),-\alpha(B)/2-\beta(B)\bigr).
\]

At \(B=100000\),

\[
\alpha(B)\approx0.0007796226864250431,
\qquad
\beta(B)\approx0.007367731952627507.
\]

So the accessible finite deviation is strongly \(\beta\)-dominated even though the eventual asymptotic regime is not.

```text
STAGE13_5=COMPLETE
DEVIATION_BASELINE=(1/2,1/4,1/4)
ALPHA=P_ab-1/2
BETA=(P_ac-P_bc)/2
```

## §6. Task 13-6 — finite deviation classification

Stage13-6 classified the finite near-\(2:1:1\) distortion rather than treating it as a candidate limit theorem.

The main finite flattening of \(\alpha\) is associated with supported-shell richness: at accessible cutoffs, the \(ab\) incidences lie on systematically poorer primitive representation shells than \(ac\) and \(bc\), depressing the geometric \(ab\) advantage. Equalizing supported-shell weight moves the finite vector substantially back toward the archimedean chamber vector.

The finite \(\beta\) component is produced by a combination of opposite-signed parity/geometric contributions, pure-\(G\) cancellation and primitive-support coupling. No single exact \(ac\leftrightarrow bc\) symmetry exists.

These statements are finite structural diagnostics. They explain why accessible data look unusually close to \(2:1:1\), but they do not determine the limiting vector; that is settled in §7.

```text
STAGE13_6=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
FINITE_ALPHA_FLATTENING=supported_shell_richness_dominant
FINITE_BETA_STRUCTURE=multi_layer_cancellation_and_primitive_support
FINITE_NEAR_2_1_1_IS_NOT_ASSUMED_AS_LIMIT=true
```

## §7. Task 13-7 — asymptotic behaviour

Stage13-7 resolves the asymptotic directional problem at the existing project theorem standard. Its final audit is

```text
stages/stage13/data/13-7/consolidation_audit_report.json
```

with provenance snapshot

```text
stages/stage13/archive/stage13-7-final.md
```

### §7.1 Directional raw incidence theorem

For \(q\in\{ab,ac,bc\}\), Stage13-7jb proves

\[
\boxed{
A_q(B)\sim D_q B(\log B)^3,
\qquad
D_q=\frac{\kappa I_q}{3\pi^3}.
}
\]

Because

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8},
\]

these constants sum to the Stage12-transferred total

\[
\sum_qD_q=\frac{\kappa}{24\pi}.
\]

Thus the normalized raw incidence vector tends to

\[
\boxed{
P_\infty=
\left(
\frac{8I_{ab}}{\pi^2},
\frac{8I_{ac}}{\pi^2},
\frac{8I_{bc}}{\pi^2}
\right).
}
\]

Numerically,

\[
P_\infty\approx(0.5347369332313988,0.24535917783225203,0.21990388893634913),
\]

or, normalized by \(bc\),

\[
\boxed{2.431684750178191:1.115756428951881:1.}
\]

The primitive-support and supported-shell arithmetic change the absolute logarithmic scale but not this leading normalized chamber vector.

### §7.2 Overlap theorem and exactly-one transfer

Write

\[
O_{ab,ac}=A_{ab,ac},\qquad O_{ab,bc}=A_{ab,bc},\qquad O_{ac,bc}=A_{ac,bc},\qquad T=A_3.
\]

Stage13-7jf applies a fixed-prime quadratic-residue sieve inside the already-counted raw incidence populations. For each fixed finite set of sufficiently large inert primes \(p\equiv3\pmod4\), the congruence-refined raw theorem has the same \(B(\log B)^3\) pole order with a product of local acceptance factors, and each such factor is eventually at most \(3/4\).

The order of limits is essential:

```text
fix k primes
-> B -> infinity
-> only then k -> infinity
```

so no growing-modulus theorem is used. Consequently,

\[
\boxed{
O_{ab,ac},O_{ab,bc},O_{ac,bc}=o(B(\log B)^3),
\qquad
T=o(B(\log B)^3).
}
\]

No perfect-cuboid nonexistence assumption is used. A perfect cuboid, if one exists, lies inside the lower-order triple-overlap population but cannot change the leading one-face asymptotic.

Substituting these bounds into the exact inclusion-exclusion identities from §2 yields

\[
\boxed{
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

Summing,

\[
\boxed{
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
}
\]

Hence the exactly-one normalized vector has the same chamber limit as the raw incidence vector.

### §7.3 Limiting deviation

Relative to \(P_0=(1/2,1/4,1/4)\),

\[
\alpha(B)\to0.034736933231398814,
\qquad
\beta(B)\to0.01272764444795145,
\]

and

\[
\boxed{
\Delta_\infty=
(0.034736933231398814,
-0.004640822167747971,
-0.03009611106365087).
}
\]

Thus

\[
\boxed{P_\infty\ne(1/2,1/4,1/4),}
\]

so the observed near-\(2:1:1\) finite vector is a strongly pre-asymptotically flattened regime rather than the true limit.

No monotone convergence theorem or explicit secondary convergence rate is claimed. The fixed-modulus refinement and the rest of the asymptotic chain are accepted at the same standard-theorem-application level as the frozen Stage12 argument; independent publication-grade review has not yet been completed.

```text
STAGE13_7=COMPLETE_AT_UNCONDITIONAL_EXACT_ONE_DIRECTIONAL_ASYMPTOTIC_LEVEL
EXACT_ONE_DIRECTIONAL_LIMIT_UNCONDITIONAL=true
LIMIT_EQUALS_2_1_1=false
PAIR_OVERLAP_LOWER_ORDER_PROVED=true
TRIPLE_OVERLAP_LOWER_ORDER_PROVED=true
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
EXPLICIT_CONVERGENCE_RATE_PROVED=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false
```

## §8. Task 13-8 — rigorous Stage12-to-Stage13 connection

Stage13-8 consolidates the bridge from the frozen Stage12 primitive oriented theorem to the Stage13 primitive canonical exactly-one directional theorem. The interface audit is recorded in

```text
stages/stage13/scripts/13-8/bridge_ledger.py
stages/stage13/data/13-8/bridge_ledger_report.json
```

Stage13-8a found no new mathematical bridge gap. This section is the canonical theorem integration of that audit.

### §8.1 Frozen Stage12 input

Stage12 remains frozen at R09. Its counting target is the primitive oriented count \(C_{\rm prim}(B)\), with theorem

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3,
}
\]

where the frozen constant ledger gives

\[
\boxed{\eta=\pi\kappa.}
\]

Stage13 does not reinterpret this theorem as a canonical or exactly-one count without an explicit projection.

### §8.2 Object, cutoff and primitivity compatibility

The Stage12 parameterization has

\[
d=\frac{h(r^2+s^2)}2,
\qquad d\le B,
\]

so its height cutoff is exactly the Stage13 space-diagonal cutoff.

Stage12 primitivity is obtained by Möbius inversion with respect to the common integer scale of the three cuboid edges. After canonical sorting this is precisely

\[
\gcd(a,b,c)=1.
\]

Sorting the edges and swapping the two legs of a distinguished face preserve this gcd. The frozen Stage12 definition sheet also records zero repeated-side contribution, so the strict canonical chamber \(a<b<c\) introduces no missing tie-boundary main term.

Thus the two stages use compatible height and primitive conventions; only orientation and distinguished-face bookkeeping remain to be quotiented.

### §8.3 Exact directional projection

For \(q\in\{ab,ac,bc\}\), define \(C^{\rm proj}_{\rm prim,q}(B)\) to be the Stage12 primitive oriented records whose distinguished integral face becomes canonical direction \(q\) after sorting the three edges.

The exact fiber result from §3.20 gives

\[
\boxed{
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)
}
\]

for every \(B\), and therefore

\[
\boxed{
C_{\rm prim}(B)=2(A_{ab}+A_{ac}+A_{bc}).
}
\]

The factor \(2\) is exactly the two orders of the two positive legs of the distinguished face. There is no additional multiplicity from the complementary Pythagorean extension. The identity also remains exact for multi-face objects because raw incidence retains the distinguished face: an exactly-two-face cuboid contributes two incidences and four Stage12 records, while an exactly-three-face cuboid contributes three incidences and six records.

The factor \(2\) holds separately in the OE and EE parity strata, so canonical projection introduces no hidden direction-dependent 2-adic coefficient.

### §8.4 Directional constant bridge

Put

\[
P_q=\frac{8I_q}{\pi^2}.
\]

The Stage13-7 directional refinement of the Stage12-oriented population can be written

\[
C^{\rm proj}_{\rm prim,q}(B)
\sim
\frac{\kappa}{12\pi}P_qB(\log B)^3
=
\frac{2\kappa I_q}{3\pi^3}B(\log B)^3.
\]

Dividing by the exact projection multiplicity gives

\[
\boxed{
A_q(B)
\sim
\frac{\kappa}{24\pi}P_qB(\log B)^3
=
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

Equivalently, using \(\eta=\pi\kappa\),

\[
A_q(B)\sim\frac{\eta I_q}{3\pi^4}B(\log B)^3.
\]

Summing \(P_q=1\) recovers the frozen Stage12 total after the universal factor \(1/2\).

### §8.5 Direct Stage12-to-exactly-one bridge

By §2,

\[
N_{ab}=A_{ab}-O_{ab,ac}-O_{ab,bc}+T
\]

and cyclically. By §7.2 every overlap term on the right is lower order. Combining this with the exact projection gives the direct categorywise bridge

\[
\boxed{
N_q(B)
=
\frac12C^{\rm proj}_{\rm prim,q}(B)
+o(B(\log B)^3).
}
\]

Summing the three categories gives

\[
\boxed{
N_1(B)
=
\frac12C_{\rm prim}(B)
+o(B(\log B)^3).
}
\]

This formula is the concise Stage12-to-Stage13 theorem interface. It uses no perfect-cuboid nonexistence assumption.

At the exact finite level the total relation remains

\[
N_1(B)
=
\frac12C_{\rm prim}(B)
-2(O_{ab,ac}+O_{ab,bc}+O_{ac,bc})
+3T.
\]

### §8.6 End-to-end finite checksum

At \(B=100000\), the locked values are

\[
C_{\rm prim}=336416,
\qquad
A_{\rm total}=168208,
\qquad
O_{ab,ac}+O_{ab,bc}+O_{ac,bc}=89,
\qquad
T=0,
\]

so exactly

\[
336416=2\cdot168208
\]

and

\[
168030=336416/2-2\cdot89+3\cdot0.
\]

Directionally,

\[
(C^{\rm proj}_{\rm prim,ab},C^{\rm proj}_{\rm prim,ac},C^{\rm proj}_{\rm prim,bc})
=(168424,86472,81520),
\]

\[
(A_{ab},A_{ac},A_{bc})=(84212,43236,40760),
\]

\[
(N_{ab},N_{ac},N_{bc})=(84146,43180,40704).
\]

Thus the finite enumeration, exact projection, overlap accounting and asymptotic constants use one consistent object convention from Stage12 through Stage13.

### §8.7 Scope and dependency boundary

The bridge does **not** reopen Stage12. Frozen Stage12 supplies:

- the definition and theorem for \(C_{\rm prim}\);
- the primitive/oriented convention;
- \(\kappa\), \(\eta\), their local-factor ledger and \(\eta=\pi\kappa\).

Stage13 supplies:

- the exact factor-2 projection (§3.20);
- the directional chamber constants and raw asymptotics (§7.1);
- the fixed-prime overlap theorem (§7.2);
- the exactly-one transfer (§7.2 and §8.5).

The fixed-modulus congruence refinement used in the overlap proof is a Stage13 extension at the same accepted theorem-application level; it is not retroactively inserted into the frozen Stage12 theorem statement.

No additional bridge lemma is required between the two stages.

```text
STAGE13_8A=COMPLETE
STAGE13_8B=COMPLETE_CANONICAL_BRIDGE_INTEGRATION
STAGE13_8C=COMPLETE_FINAL_AUDIT
STAGE13_8=COMPLETE
NEW_MATHEMATICAL_BRIDGE_GAP_FOUND=false
STAGE12_REOPENED=false
OBJECT_MAP=CLOSED
CUTOFF_MATCHING=CLOSED
PRIMITIVE_DEFINITION_MATCHING=CLOSED
ORIENTATION_FIBER=CLOSED
CANONICAL_DIRECTION_PARTITION=CLOSED
PARITY_PROJECTION=CLOSED
DIRECTIONAL_RAW_CONSTANTS=CLOSED_BY_STAGE13_7
OVERLAP_TO_EXACT_ONE=CLOSED_BY_STAGE13_7
NEXT=Stage13-9 main structural theorem
```

## §9. Task 13-9 — main structural theorem

Stage13-9 introduces no new analytic input. It packages the completed Stage13-7 asymptotic theorem and the completed Stage13-8 counting bridge into the principal theorem of Stage13.

The consistency audit is

```text
stages/stage13/scripts/13-9/main_structural_theorem_audit.py
stages/stage13/data/13-9/main_structural_theorem_audit_report.json
```

### §9.1 Main structural theorem

Let

\[
\mathbf N(B)=\bigl(N_{ab}(B),N_{ac}(B),N_{bc}(B)\bigr)
\]

for primitive canonical cuboids

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B,
\]

having exactly one integral face diagonal, with the category determined by which canonical face is integral.

Let

\[
R=\{(x,y,z)\in S^2:0<x<y<z\}
\]

and

\[
I_{ab}=\int_R\frac{d\omega}{\sqrt{x^2+y^2}},\qquad
I_{ac}=\int_R\frac{d\omega}{\sqrt{x^2+z^2}},\qquad
I_{bc}=\int_R\frac{d\omega}{\sqrt{y^2+z^2}}.
\]

Then

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8},
\]

and, as \(B\to\infty\),

\[
\boxed{
\mathbf N(B)
=
\frac{\kappa}{3\pi^3}
\bigl(I_{ab},I_{ac},I_{bc}\bigr)
B(\log B)^3
+o\!\bigl(B(\log B)^3\bigr),
}
\]

where the vector \(o\)-term is componentwise (equivalently in any fixed norm on \(\mathbf R^3\)). Thus, for each \(q\in\{ab,ac,bc\}\),

\[
\boxed{
N_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

Summing the three components gives

\[
\boxed{
N_1(B)
\sim
\frac{\kappa}{24\pi}B(\log B)^3.
}
\]

### §9.2 Normalized directional law

Dividing the vector theorem by its total gives

\[
\boxed{
\frac{\mathbf N(B)}{N_1(B)}
\longrightarrow
\frac8{\pi^2}
\bigl(I_{ab},I_{ac},I_{bc}\bigr).
}
\]

Numerically,

\[
\boxed{
P_\infty
=
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913).
}
\]

Equivalently,

\[
\boxed{
N_{ab}:N_{ac}:N_{bc}
\longrightarrow
2.431684750178191:1.115756428951881:1.
}
\]

In particular,

\[
\boxed{P_\infty\ne(1/2,1/4,1/4),}
\]

so the finite near-\(2:1:1\) pattern is not the limiting law.

### §9.3 Stage12 bridge form

Let \(C^{\rm proj}_{\rm prim,q}(B)\) be the frozen-Stage12 primitive oriented records whose distinguished integral face projects to canonical category \(q\). The exact projection theorem gives

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)
\]

for every \(B\), while Stage13-7 proves that all pair overlaps and the triple overlap are lower order. Therefore the main theorem is equivalently connected to Stage12 by

\[
\boxed{
N_q(B)
=
\frac12 C^{\rm proj}_{\rm prim,q}(B)
+o(B(\log B)^3),
}
\]

and

\[
\boxed{
N_1(B)
=
\frac12 C_{\rm prim}(B)
+o(B(\log B)^3).
}
\]

The common factor \(1/2\) is purely the quotient by the two orders of the distinguished face legs and has no directional effect.

### §9.4 Structural content of the theorem

The theorem separates the asymptotic directional law into three layers.

1. **Archimedean chamber geometry.** The canonical order chamber \(0<a<b<c\), coupled with the one-face Gelfand--Leray density, supplies the three unequal weights \(I_{ab}>I_{ac}>I_{bc}\).
2. **Arithmetic population scale.** Primitive support, representation richness and the Stage12 local-factor constant \(\kappa\) determine the absolute \(B(\log B)^3\) scale. At leading normalized order they contribute a common factor across the three categories.
3. **Exactly-one sieve.** Pair and triple face overlaps are \(o(B(\log B)^3)\), so removing multi-face objects does not alter the leading directional vector.

Thus the asymptotic normalized direction is the archimedean chamber vector, even though finite arithmetic reweighting strongly flattens that vector over the accessible numerical range.

This structural interpretation is a theorem-level synthesis of the earlier results; the detailed narrative explaining the finite flattening is reserved for Stage13-10.

### §9.5 Deviation corollary

Relative to

\[
P_0=(1/2,1/4,1/4),
\]

the deviation vector satisfies

\[
\boxed{
\Delta(B)=P(B)-P_0\longrightarrow
\Delta_\infty
}
\]

with

\[
\boxed{
\Delta_\infty=
(0.034736933231398814,
-0.004640822167747971,
-0.03009611106365087).
}
\]

Equivalently,

\[
\alpha(B)\to0.034736933231398814,
\qquad
\beta(B)\to0.01272764444795145.
\]

At \(B=100000\), however,

\[
\alpha\approx0.0007796226864250431,
\qquad
\beta\approx0.007367731952627507,
\]

which records how strongly pre-asymptotic the observed near-\(2:1:1\) regime still is.

### §9.6 Logical scope

The theorem does **not** assume that perfect cuboids do not exist. If a perfect cuboid exists, it belongs to the triple-overlap population; Stage13 proves only that this population is lower order relative to the one-face main term. Thus the theorem neither proves nor disproves existence of a perfect cuboid.

The theorem also does not provide:

- an explicit numerical convergence rate for \(P(B)\to P_\infty\);
- an effective threshold beyond which a prescribed error bound holds;
- monotonicity of any directional ratio;
- an independent publication-grade verification of the fixed-modulus analytic input.

Accordingly, one must not infer quantitative closeness to the limit at a specified enormous finite value of \(B\) without an additional effective error term.

### §9.7 Proof dependency summary

The main theorem depends on the following established chain:

```text
Stage12 R09
  primitive oriented total theorem
        |
        v
Stage13-3b
  exact canonical chamber integrals I_ab,I_ac,I_bc
        |
        v
Stage13-3d
  exact projection multiplicity 2
        |
        v
Stage13-7jb
  categorywise raw incidence asymptotics
        |
        v
Stage13-7jf
  pair/triple overlaps are lower order
        |
        v
Stage13-8
  object/cutoff/primitivity/constant bridge closed
        |
        v
Stage13-9
  main structural theorem
```

No additional lemma is introduced between Stage13-8 and this theorem statement.

```text
STAGE13_9=COMPLETE_MAIN_STRUCTURAL_THEOREM
MAIN_VECTOR_ASYMPTOTIC_PROVED=true
NORMALIZED_DIRECTIONAL_LIMIT_PROVED=true
LIMIT_EQUALS_2_1_1=false
STAGE12_TO_MAIN_THEOREM_BRIDGE_CLOSED=true
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
EXPLICIT_CONVERGENCE_RATE_PROVED=false
MONOTONICITY_PROVED=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false
NEXT=Stage13-10 final explanation
```

## §10. Task 13-10 — final explanation

Stage13-10 introduces no new analytic theorem. It answers the original structural question by separating the **finite observed regime** from the **asymptotic leading law** and identifying which layers control each.

### §10.1 The apparent paradox

At the locked finite cutoff \(B=100000\),

\[
N_{ab}:N_{ac}:N_{bc}\approx2.0673:1.0608:1,
\]

which is visually close to \(2:1:1\). But the proved normalized limit is

\[
\boxed{
2.431684750178191:1.115756428951881:1.
}
\]

There is no contradiction. The first vector is a finite population after substantial arithmetic reweighting; the second is the coefficient vector of the leading \(B(\log B)^3\) asymptotic.

### §10.2 The geometric backbone

The persistent directional asymmetry begins at the real place. On the canonical chamber

\[
0<a<b<c,
\]

the one-face Gelfand--Leray weights satisfy pointwise

\[
w_{ab}>w_{ac}>w_{bc}.
\]

The shortest-pair face has the smallest face diagonal and hence the largest \(1/p\) density weight. Integrating these weights over the canonical chamber produces

\[
I_{ab}>I_{ac}>I_{bc}
\]

and exactly the limiting directional vector.

Two controls show what the mechanism is **not**. Pure canonical relabelling with a uniform weight gives \(1:1:1\), and removing the order chamber restores full coordinate symmetry. Thus the asymmetry comes from

\[
\boxed{\text{canonical size order}\times\text{one-face real density},}
\]

not from the labels \(ab,ac,bc\) by themselves.

### §10.3 Why the finite vector is much flatter

Accessible integer populations do not sample the chamber with the leading asymptotic weight already fully stabilized.

The dominant finite flattening of the \(ab\) excess is associated with **supported-shell richness**. At audited finite cutoffs, the \(ab\) incidences lie on systematically poorer primitive representation shells than the \(ac\) and \(bc\) incidences. This depresses the large geometric \(ab\) advantage and moves the observed vector toward the near-\(2:1:1\) shape.

The smaller \(ac-bc\) separation is also not an exact symmetry. Finite OE/EE parity strata and pure-\(G\) components carry opposite-signed \(ac-bc\) tilts, which cancel strongly in aggregate, while primitive-support reweighting supplies much of the residual positive \(ac-bc\) gap. These are genuine finite arithmetic/geometric couplings.

The exactly-one sieve is not the source of the flattening. At \(B=100000\), the raw vector is already

\[
(84212,43236,40760)
\]

before overlap removal, and the exactly-one vector is

\[
(84146,43180,40704).
\]

The change is tiny compared with the directional bias already present.

Accordingly, the finite observation is best described as

\[
\boxed{
\text{chamber bias}
\;\text{strongly flattened by finite arithmetic reweighting},
}
\]

with a small additional exactly-one correction.

### §10.4 Why the chamber vector returns asymptotically

The decisive asymptotic fact is that the categorywise raw incidence constants factor as

\[
A_q(B)\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

All of the primitive/arithmetic population growth that survives in the leading term appears through the **same scalar factor** \(\kappa/(3\pi^3)\) for the three directions. The direction dependence of the leading coefficient is therefore entirely contained in \(I_q\).

So the finite shell, parity and primitive-support couplings can strongly distort moderate cutoffs without supplying a distinct direction-dependent coefficient in the leading normalized asymptotic. After normalization by the total population, the common arithmetic scale cancels and the chamber vector remains:

\[
\frac{\mathbf A(B)}{A_{ab}+A_{ac}+A_{bc}}
\longrightarrow
\frac8{\pi^2}(I_{ab},I_{ac},I_{bc}).
\]

Finally, pair and triple overlaps satisfy

\[
O_{ij}=o(B(\log B)^3),\qquad T=o(B(\log B)^3),
\]

so passing from raw incidence to exactly-one cannot change that leading normalized vector.

This is the resolution of the finite/asymptotic tension:

\[
\boxed{
\begin{array}{c}
\text{finite: direction-dependent arithmetic reweighting is still visible},\\[2mm]
\text{leading asymptotic: that directional reweighting is lower-order,}\\
\text{the common arithmetic scale cancels, and chamber geometry remains.}
\end{array}
}
\]

### §10.5 Why near-2:1:1 can persist for a long range

An asymptotic theorem does not say that convergence must be fast or monotone. Stage13 proves only

\[
P(B)=P_\infty+o(1).
\]

It does not prove an explicit error such as \(O(1/\log B)\), nor an effective threshold \(B_0(\varepsilon)\). Therefore the finite near-\(2:1:1\) regime may persist over a very long numerical range without contradicting the theorem.

For the same reason, Stage13 does not justify saying that a specified enormous finite value of \(B\)—even one described by a famous huge-number notation—must already be quantitatively close to the limiting ratio. Such a statement would require an effective convergence bound not presently proved.

### §10.6 What the result says about multi-face and perfect cuboids

Stage13 proves that the population with at least two integral faces is lower order relative to the one-face \(B(\log B)^3\) main population, and the triple-overlap population is lower order as well.

This explains why multi-face objects are asymptotically negligible for the directional one-face law. It does **not** imply that the triple-overlap population is empty. A single perfect cuboid, finitely many perfect cuboids, or a sufficiently sparse infinite family are all compatible with a lower-order estimate.

Thus Stage13 maps the one-face landscape and isolates the multi-face region, but it neither proves nor disproves the existence of a perfect cuboid.

### §10.7 Final answer to the Stage13 question

The original near-\(2:1:1\) observation is not an accidental numerical coincidence, but neither is it the true limiting law.

Its explanation has two scales:

1. **Why there is an \(ab\) excess at all:** canonical chamber geometry coupled to the one-face real density favors the shortest-pair face.
2. **Why finite counts look much closer to \(2:1:1\) than the limiting chamber ratio:** supported-shell richness and other finite primitive/parity arithmetic couplings flatten the chamber bias and partly cancel the \(ac-bc\) gap.
3. **Why the limit nevertheless returns to the chamber vector:** the surviving arithmetic main factor is common to all three directions, while pair/triple overlaps are lower order.

Hence

\[
\boxed{
\text{finite near-}2:1:1
=\text{a long pre-asymptotic flattening of a stronger chamber bias},
}
\]

where the equality sign is explanatory shorthand rather than an exact algebraic decomposition.

The true normalized limiting law is

\[
\boxed{
P_\infty
=(0.5347369332313988,
  0.24535917783225203,
  0.21990388893634913),
}
\]

or

\[
\boxed{
N_{ab}:N_{ac}:N_{bc}
\longrightarrow
2.431684750178191:1.115756428951881:1.
}
\]

### §10.8 Stage13 completion boundary

Stage13 is complete at the current project theorem standard. It has:

- defined the primitive canonical exactly-one directional population;
- isolated raw incidence and overlap contributions;
- identified the canonical chamber mechanism behind the directional bias;
- classified the main finite flattening/cancellation mechanisms;
- proved the unconditional categorywise asymptotic law at the accepted Stage12 theorem-application standard;
- proved pair/triple overlaps are lower order;
- closed the Stage12-to-Stage13 counting bridge;
- stated the main structural theorem; and
- given the final finite-versus-asymptotic explanation.

Open questions outside the completed Stage13 scope include the true growth law of the two-face population, an effective convergence rate for the directional vector, independent publication-grade verification, and the existence or nonexistence of a perfect cuboid.

```text
STAGE13_10=COMPLETE_FINAL_EXPLANATION
STAGE13=COMPLETE
FINITE_NEAR_2_1_1_EXPLAINED=true
FINITE_REGIME_IS_PREASYMPTOTIC=true
ASYMPTOTIC_DIRECTION_IS_ARCHIMEDEAN_CHAMBER_VECTOR=true
FINITE_ARITHMETIC_FLATTENING_IS_LEADING_NORMALIZED_CONSTANT=false
PAIR_OVERLAP_LOWER_ORDER=true
TRIPLE_OVERLAP_LOWER_ORDER=true
PERFECT_CUBOID_EXISTENCE_RESOLVED=false
EXPLICIT_CONVERGENCE_RATE_PROVED=false
MONOTONICITY_PROVED=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false
NEXT_STAGE13_TASK=NONE
```