# Stage13 — canonical working file

> **STATUS:** `STAGE13_3C_COMPLETE_13_3D_NEXT`
>
> **SCOPE:** primitive canonical face-ratio analysis
>
> **CANONICAL_WORKING_FILE:** `stages/stage13/main.md`

This file is the living mathematical source for Stage13.  The completed
Stage13-1 and Stage13-2 initial documents remain under `initial/` as provenance;
their active definitions and decomposition are consolidated here before the
Stage13-3 analysis.

## §1. Task 13-1 — definition of the observed ratio

For \(B\ge1\), consider positive integer quadruples

\[
(a,b,c,d)\in\mathbf Z_{>0}^4
\]

satisfying

\[
a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The strict order is the canonical representative under edge permutations, and
the gcd condition removes scaled copies.

Define

\[
Q_{ab}=a^2+b^2,\qquad Q_{ac}=a^2+c^2,\qquad Q_{bc}=b^2+c^2.
\]

The Stage13 one-face population consists of objects for which exactly one of
these three quantities is a positive integer square.  Its three categories are

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

The labels \(ab,ac,bc\) are **size positions after canonical ordering**, not
fixed coordinate-axis labels.

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
\mathbf P(100000)
=\frac{\mathbf N(100000)}{N_1(100000)}
\approx(0.50078,0.25698,0.24224).
\]

These values motivate the phrase “observed near \(2:1:1\)”.  Stage13 does not
assume that

\[
\mathbf P(B)\to(1/2,1/4,1/4),
\]

or even that this is the correct limiting vector.

Stage12 and Stage13 counts are not identified automatically.  Stage12 proves
an asymptotic for a primitive **oriented** count, while Stage13 uses primitive
canonical exactly-one-face objects.  Any bridge must account explicitly for
orientation, representation multiplicity, parity and canonical projection.

## §2. Task 13-2 — structural decomposition

Let

\[
\mathcal U(B)=
\left\{
(a,b,c,d):
a<b<c,\ \gcd(a,b,c)=1,\ a^2+b^2+c^2=d^2,\ d\le B
\right\}.
\]

No face condition is imposed in \(\mathcal U(B)\).  For
\(x\in\mathcal U(B)\), let

\[
I_{ab}(x)=\mathbf1_{Q_{ab}=\square},\quad
I_{ac}(x)=\mathbf1_{Q_{ac}=\square},\quad
I_{bc}(x)=\mathbf1_{Q_{bc}=\square}.
\]

Before the exactly-one sieve, define raw incidence counts

\[
A_{ab}=\sum_{x\in\mathcal U(B)}I_{ab}(x),\quad
A_{ac}=\sum_{x\in\mathcal U(B)}I_{ac}(x),\quad
A_{bc}=\sum_{x\in\mathcal U(B)}I_{bc}(x).
\]

Define the pair overlaps

\[
A_{ab,ac}=\sum I_{ab}I_{ac},\qquad
A_{ab,bc}=\sum I_{ab}I_{bc},\qquad
A_{ac,bc}=\sum I_{ac}I_{bc},
\]

and the three-face overlap

\[
A_3=\sum I_{ab}I_{ac}I_{bc}.
\]

Then inclusion-exclusion gives the exact identities

\[
\boxed{
N_{ab}=A_{ab}-A_{ab,ac}-A_{ab,bc}+A_3
}
\]

and cyclically,

\[
\boxed{
N_{ac}=A_{ac}-A_{ab,ac}-A_{ac,bc}+A_3,
}
\]

\[
\boxed{
N_{bc}=A_{bc}-A_{ab,bc}-A_{ac,bc}+A_3.
}
\]

Also

\[
N_1
=
A_{ab}+A_{ac}+A_{bc}
-2(A_{ab,ac}+A_{ab,bc}+A_{ac,bc})
+3A_3.
\]

This separates two logically different possibilities:

1. the near \(2:1:1\) shape is already present in the raw incidence vector
   \(\mathbf A(B)\); or
2. it is created or materially reshaped by the overlap correction.

The remaining structural layers to test are:

- canonical size-order chamber \(0<a<b<c\);
- primitive projection;
- parity, especially the \(2\)-adic branch;
- Stage12 representation/fiber multiplicity;
- odd-prime local density;
- cutoff and boundary effects.

A full \(S_3\) orientation lift by itself cannot create the leading \(2\):
for an object with one distinguished unordered face, its six edge
permutations place that face on each fixed coordinate plane exactly twice, so
the axis-labelled multiplicity is \(2:2:2=1:1:1\).

No Euler-product factorization, constant bridge to Stage12, or limiting
\(2:1:1\) theorem is asserted at this point.

## §3. Task 13-3 — origin of the leading 2

### §3.1 Stage13-3a question

The first discriminator is deliberately cheap and decisive:

> Is the leading near-\(2\) already visible in
> \(\mathbf A(B)=(A_{ab},A_{ac},A_{bc})\) before the exactly-one sieve?

If yes, overlap cannot be the mechanism that *creates* the leading \(2\).
If no, the pair/triple-overlap layer would require detailed analysis first.

### §3.2 Complete finite enumeration used for 13-3a

The audit script is

```text
stages/stage13/scripts/13-3/raw_incidence.py
```

and writes

```text
stages/stage13/data/13-3/raw_incidence_report.json
```

For a bound \(B\), it generates every positive integer Pythagorean triple
with hypotenuse at most \(B\), including nonprimitive scalings.  It builds two
indexes:

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

with at least one integral face diagonal.  Conversely, every object in
\(\mathcal U(B)\) having at least one integral face can be obtained in this
way by choosing one of its integral faces and denoting that face diagonal by
\(p\).  Thus this is complete for the raw-incidence population, although a
multi-face object can be generated more than once.

The script then:

1. sorts the three edges and requires \(a<b<c\);
2. imposes \(\gcd(a,b,c)=1\);
3. deduplicates by the canonical tuple \((a,b,c,d)\);
4. recomputes all three square conditions directly from the deduplicated
   tuple rather than trusting the distinguished generating face;
5. checks the inclusion-exclusion identities;
6. at \(B=100000\), independently reproduces the locked Stage13-1
   exactly-one vector \((84146,43180,40704)\).

The last check is important: 13-3a is not obtained merely by adding old
reported overlap counts back by hand.

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
\boxed{
\mathbf A=(84212,43236,40760)
}
\]

with raw proportions

\[
\frac{\mathbf A}{A_{ab}+A_{ac}+A_{bc}}
\approx
(0.5006421,0.2570389,0.2423190).
\]

The overlap counts are

\[
A_{ab,ac}=33,\qquad
A_{ab,bc}=33,\qquad
A_{ac,bc}=23,\qquad
A_3=0.
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

of the three raw components respectively.  The \(L^\infty\) change in the
normalized proportion vector is only

\[
1.3756\times10^{-4}.
\]

### §3.4 13-3a conclusion

The finite computation decisively answers the discriminator posed in §3.1:

\[
\boxed{\text{the near }2:1:1\text{ shape is already present before the exactly-one sieve.}}
\]

Thus the pair-overlap / exact-one correction does **not** generate the leading
\(2\) at the audited cutoffs.  It produces only a small perturbation.

This is a finite enumerative result.  It does **not** prove that overlaps are
asymptotically negligible, nor does it prove a limiting \(2:1:1\) ratio.

The leading candidate mechanism therefore moves one layer earlier: the next
test is the **canonical size-order / geometric chamber effect**.  This is
Stage13-3b.

```text
STAGE13_3A=COMPLETE
RAW_INCIDENCE_ALREADY_NEAR_2_1_1=true
OVERLAP_GENERATES_LEADING_2=false_at_audited_finite_bounds
ASYMPTOTIC_CLAIM=false
NEXT=Stage13-3b canonical size-order / geometric density
```

### §3.5 Stage13-3b — canonical chamber / archimedean density

The Stage13-3b discriminator was:

> Does the interaction between the canonical size-order chamber and the real one-face density create an \(ab\) excess of approximately the observed size?

For a distinguished integral \(ab\) face introduce its diagonal \(p\):
\[
a^2+b^2=p^2,\qquad p^2+c^2=d^2.
\]
The Gelfand--Leray Jacobian in \((p,d)\) is \(4pd\), so after radial
normalization \((a,b,c)=d(x,y,z)\) the angular weight is, up to a common
constant,
\[
w_{ab}=\frac1{\sqrt{x^2+y^2}}.
\]
Cyclically,
\[
w_{ac}=\frac1{\sqrt{x^2+z^2}},\qquad
w_{bc}=\frac1{\sqrt{y^2+z^2}}.
\]

On the canonical chamber
\[
R=\{(x,y,z)\in S^2:0<x<y<z\},
\]
one has pointwise
\[
\boxed{w_{ab}>w_{ac}>w_{bc}.}
\]
Pure canonical relabelling with uniform weight still gives \(1:1:1\), and
integrating over the full positive octant also gives \(1:1:1\) by coordinate
symmetry.  Thus the asymmetry is specifically
\[
\boxed{\text{canonical size-order chamber}\times\text{one-face real density}.}
\]

The support audit
```text
stages/stage13/scripts/13-3/geometric_chamber.py
stages/stage13/data/13-3/geometric_chamber_report.json
```
gives
\[
\begin{aligned}
I_{ab}&=0.659705248705705\ldots,\\
I_{ac}&=0.302699752672608\ldots,\\
I_{bc}&=0.271295548757857\ldots,
\end{aligned}
\]
with the exact check
\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}.
\]
The \(bc\)-normalized geometric ratio is therefore
\[
\boxed{2.4316847502:1.1157564290:1}.
\]

At \(B=100000\), Stage13-3a gives the raw ratio
\[
2.0660451423:1.0607458292:1.
\]
Hence the real chamber gets the direction and approximate scale of the
leading \(ab\) excess right but overstates it.  In normalized-proportion
\(L^1\) distance it removes about \(79.6\%\) of the finite discrepancy from
the symmetric \(1:1:1\) baseline at \(B=100000\); across the seven audited
cutoffs the analogous descriptive fraction is about \(68.2\%\) to \(85.6\%\).

This is not a global asymptotic theorem.  In particular, no equality between
the chamber integrals and the true arithmetic leading constants is asserted.

```text
STAGE13_3B=COMPLETE
ARCHIMEDEAN_CHAMBER_DIRECTION_ORDER=ab>ac>bc
CANONICAL_RELABELING_ALONE_GENERATES_BIAS=false
GEOMETRIC_MODEL_BC_NORMALIZED=2.4316847502:1.1157564290:1
RAW_B100000_BC_NORMALIZED=2.0660451423:1.0607458292:1
GEOMETRIC_MODEL_IS_GLOBAL_ASYMPTOTIC_THEOREM=false
NEXT=Stage13-3c parity / 2-adic correction
```

### §3.6 Stage13-3c question

Stage13-3b leaves a clean residual problem: why is the integer ratio flatter
than the archimedean chamber ratio?

The next discriminator is the prime \(2\):

> Does parity / \(2\)-adic structure supply a direction-dependent correction
> large enough to explain the flattening from the geometric ratio toward the
> observed raw ratio?

The support audit is
```text
stages/stage13/scripts/13-3/parity_2adic.py
stages/stage13/data/13-3/parity_2adic_report.json
```
and uses exactly the same complete primitive canonical raw-incidence
enumeration as Stage13-3a.

### §3.7 Exact primitive parity structure

Let
\[
a^2+b^2+c^2=d^2,\qquad \gcd(a,b,c)=1.
\]
Modulo \(4\), a primitive solution cannot have zero, two, or three odd edge
lengths.  Thus it has exactly one odd edge and \(d\) is odd.

Write the two even edges as \(e_1,e_2\).  Modulo \(8\), the space-diagonal
equation permits only two coarse branches:
\[
v_2(e_1)=v_2(e_2)=1,
\]
or
\[
v_2(e_1),v_2(e_2)\ge2.
\]
A mixed branch would give \(1+4+0\equiv5\pmod8\), impossible for \(d^2\).

Now impose that at least one face diagonal is integral.  The branch
\(v_2(e_1)=v_2(e_2)=1\) is impossible:

- an odd-even face has square sum \(1+4\equiv5\pmod8\);
- the even-even face has square sum \(4+4\equiv8\pmod{16}\).

Neither is a square.  Therefore every primitive raw-incidence object satisfies
\[
\boxed{\text{one odd edge},\qquad d\text{ odd},\qquad 4\mid e_1,\ 4\mid e_2.}
\]

The finite enumeration confirms this for every audited object; at
\(B=100000\) all \(168119\) distinct primitive canonical objects with at
least one integral face lie in this branch.

### §3.8 Standalone \(2\)-adic density is category-symmetric

The one-face varieties
\[
V_{ab},\qquad V_{ac},\qquad V_{bc}
\]
are carried into one another by permutations of \(a,b,c\).  The primitive
local condition is invariant under the same permutations.  Consequently a
standalone \(p=2\) local density, before coupling it to the real order chamber
or to representation fibers, is common to the three face labels.

Thus
\[
\boxed{\text{the universal prime-2 admissibility sieve cannot by itself create a directional }ab/ac/bc\text{ bias}.}
\]

Any visible prime-\(2\) effect on the canonical counts must come from coupling
between the \(2\)-adic type and another nonsymmetric layer, such as the real
order chamber or the representation/canonical-projection fibers.

### §3.9 Face-relative parity split

Each raw face incidence is split into two exact types.

- **OE:** the distinguished integral face contains the unique odd edge.
- **EE:** the distinguished integral face is the pair of even edges.

At \(B=100000\),
\[
\mathbf A^{OE}=(50320,24059,22386),
\]
and
\[
\mathbf A^{EE}=(33892,19177,18374),
\]
with
\[
\mathbf A=\mathbf A^{OE}+\mathbf A^{EE}=(84212,43236,40760).
\]

The corresponding \(bc\)-normalized ratios are
\[
\boxed{\mathbf A^{OE}: 2.24783347:1.07473421:1}
\]
and
\[
\boxed{\mathbf A^{EE}: 1.84456297:1.04370306:1.}
\]

Their normalized proportion vectors are
\[
\mathbf P^{OE}\approx(0.520023,0.248633,0.231344),
\]
\[
\mathbf P^{EE}\approx(0.474392,0.268424,0.257184).
\]

Thus a real finite cancellation is visible: the OE subpopulation puts the
\(ab\) share above one half, while the EE subpopulation puts it below one
half.  Their incidence shares at \(B=100000\) are approximately
\[
57.53\%\quad\text{and}\quad42.47\%,
\]
and the mixture lands at the raw
\[
P_{ab}\approx0.500642.
\]

This is a useful structural observation, but it is not yet a causal
factorization of the asymptotic constant.  The two conditional vectors
already contain the real chamber, all odd-prime arithmetic, and
representation multiplicity.

### §3.10 Finer \(2\)-adic signatures

For OE incidences the audit records
\[
\bigl(v_2(e_{\rm face}),v_2(e_{\rm remaining})\bigr),
\]
and for EE incidences it records the two even-face valuations.  For a compact
finite table, valuations \(4,5,\ldots\) are grouped as \(4+\).

At \(B=100000\), the total-variation distances between the resulting
signature distributions are
\[
\begin{aligned}
d_{\rm TV}(ab,ac)&=0.04937\ldots,\\
d_{\rm TV}(ab,bc)&=0.04832\ldots,\\
d_{\rm TV}(ac,bc)&=0.03819\ldots.
\end{aligned}
\]

So the detailed prime-\(2\) signature mix is not identical after canonical
ordering, but the differences are modest.  This is consistent with a visible
finite coupling without making prime \(2\) the entire explanation of the
geometric-to-arithmetic flattening.

### §3.11 13-3c conclusion

Stage13-3c separates two statements that should not be conflated.

First, the prime-\(2\) admissibility condition is extremely strong:
\[
\boxed{4\mid e_1,\ 4\mid e_2}
\]
for every primitive object in the raw one-face population.

Second, this universal condition is permutation-symmetric across the three
one-face varieties.  Therefore it is not, by itself, a direction-dependent
local factor that can turn the geometric vector into the observed one.

The finite OE/EE decomposition does reveal a nontrivial coupling between
parity type and canonical size order, and that coupling visibly flattens the
aggregate vector.  But both subpopulations still carry a substantial
\(ab\) excess, and the finer \(2\)-adic signature distributions differ only
at the few-percent total-variation level.

Accordingly,
\[
\boxed{\text{prime }2\text{ matters, but Stage13-3c does not identify it as the complete missing correction.}}
\]

The next layer is Stage13-3d: test the Stage12 representation/fiber
multiplicity after projection to the canonical size-ordered object.  That is
the next plausible source of a category-dependent weight large enough to
bridge the remaining gap.

No limiting \(2:1:1\) theorem, no global Euler product, and no asymptotic
negligibility claim is made here.

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
