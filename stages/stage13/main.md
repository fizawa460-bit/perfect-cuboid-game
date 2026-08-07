# Stage13 — canonical working file

> **STATUS:** `STAGE13_3A_COMPLETE_13_3B_NEXT`
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
