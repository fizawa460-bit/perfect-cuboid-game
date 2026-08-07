# Stage13 — canonical face-ratio structural analysis

> **CANONICAL_WORKING_FILE:** `stages/stage13/main.md`
>
> **CURRENT_TASK:** `Stage13-3a`
>
> **STATUS:** `RAW_INCIDENCE_FINITE_TEST_COMPLETE`
>
> **SCOPE:** canonical primitive cuboids with integer space diagonal, classified by integer-face position

Stage13 studies why the finite exact-one-face counts are close to a `2:1:1` directional ratio. It does **not** assume in advance that the limiting ratio exists or is exactly `2:1:1`.

The completed Stage13-1 and Stage13-2 content is integrated below. The files under `stages/stage13/initial/` remain historical sources after this canonical-file import.

---

## §1 — Task 13-1: definition

### 1.1 Base objects and canonical ordering

For `B>=1`, let

\[
\mathcal U(B)
=
\left\{
(a,b,c,d)\in\mathbf Z_{>0}^4:
 a<b<c,
 \gcd(a,b,c)=1,
 a^2+b^2+c^2=d^2,
 d\le B
\right\}.
\]

Thus Stage13 uses:

- primitive objects only;
- the strict canonical representative `a<b<c`;
- the space-diagonal cutoff `d<=B`;
- no scale multiplicity.

Set

\[
Q_{ab}=a^2+b^2,
\qquad
Q_{ac}=a^2+c^2,
\qquad
Q_{bc}=b^2+c^2.
\]

The three exact-one-face classes are

\[
\mathcal E_{ab}(B)
=
\{x\in\mathcal U(B):Q_{ab}=\square,\ Q_{ac},Q_{bc}\ne\square\},
\]

\[
\mathcal E_{ac}(B)
=
\{x\in\mathcal U(B):Q_{ac}=\square,\ Q_{ab},Q_{bc}\ne\square\},
\]

\[
\mathcal E_{bc}(B)
=
\{x\in\mathcal U(B):Q_{bc}=\square,\ Q_{ab},Q_{ac}\ne\square\}.
\]

Write

\[
N_{ab}=|\mathcal E_{ab}|,
\qquad
N_{ac}=|\mathcal E_{ac}|,
\qquad
N_{bc}=|\mathcal E_{bc}|,
\qquad
N_1=N_{ab}+N_{ac}+N_{bc}.
\]

Here `ab`, `ac`, `bc` are **size-order positions**, not fixed coordinate-axis labels:

- `ab`: smallest and middle edge;
- `ac`: smallest and largest edge;
- `bc`: middle and largest edge.

### 1.2 Finite observation motivating Stage13

The existing exact-one enumeration at `B=100000` gives

\[
(N_{ab},N_{ac},N_{bc})
=(84146,43180,40704),
\]

with

\[
N_1=168030.
\]

Normalizing by `N_bc` gives approximately

\[
2.0673:1.0608:1,
\]

and normalizing by the total gives approximately

\[
(0.50078,0.25698,0.24224).
\]

The idealized reference vector is

\[
\mathbf P_*=\left(\frac12,\frac14,\frac14\right),
\]

but Stage13 does not assume

\[
\mathbf P(B)\to\mathbf P_*.
\]

The existence and value of any limiting ratio, the finite-range deviation, and the mechanism generating the directional bias remain research questions.

### 1.3 Separation from Stage12

Stage12 proves an asymptotic for its primitive **oriented** count `C_prim(B)`. Stage13 counts canonical exact-one-face objects. Therefore no equality, constant-factor relation, or automatic projection between Stage12 and `N_ab,N_ac,N_bc,N_1` is assumed.

Any Stage12-to-Stage13 connection must explicitly audit orientation, representation multiplicity, parity, canonical projection, and boundary effects.

---

## §2 — Task 13-2: structural decomposition

### 2.1 Raw directional incidence

For `x in U(B)`, define

\[
I_{ab}(x)=\mathbf1_{Q_{ab}=\square},
\qquad
I_{ac}(x)=\mathbf1_{Q_{ac}=\square},
\qquad
I_{bc}(x)=\mathbf1_{Q_{bc}=\square}.
\]

Before imposing the exact-one sieve, define

\[
A_{ab}=\sum_{x\in\mathcal U(B)} I_{ab}(x),
\qquad
A_{ac}=\sum_{x\in\mathcal U(B)} I_{ac}(x),
\qquad
A_{bc}=\sum_{x\in\mathcal U(B)} I_{bc}(x).
\]

Define pair overlaps

\[
A_{ab,ac}=\sum I_{ab}I_{ac},
\qquad
A_{ab,bc}=\sum I_{ab}I_{bc},
\qquad
A_{ac,bc}=\sum I_{ac}I_{bc},
\]

and triple overlap

\[
A_3=\sum I_{ab}I_{ac}I_{bc}.
\]

The exact indicator identities are

\[
\boxed{
N_{ab}=A_{ab}-A_{ab,ac}-A_{ab,bc}+A_3,
}
\]

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

Consequently

\[
\boxed{
N_1
=A_{ab}+A_{ac}+A_{bc}
-2(A_{ab,ac}+A_{ab,bc}+A_{ac,bc})
+3A_3.
}
\]

This separates a directional pattern already present in the raw incidence vector

\[
\mathbf A=(A_{ab},A_{ac},A_{bc})
\]

from any pattern generated or modified by the exact-one overlap correction.

### 2.2 Canonical size-order layer

Because `a<b<c`, the three face positions are not geometrically identical inside the canonical chamber

\[
0<a<b<c.
\]

The three incidences can therefore have different parameter ranges, cutoff geometry, arithmetic weights, or boundary behavior even when the underlying unlabeled equations are symmetric.

### 2.3 Full-orientation check

A strict canonical object has six edge-label permutations. If an exactly-one object has one distinguished unordered integer face, then under all six equally weighted permutations that face appears on each fixed coordinate plane exactly twice. Hence full `S_3` orientation alone gives

\[
2:2:2=1:1:1.
\]

Therefore the canonical near-`2:1:1` pattern cannot be explained solely by uniformly restoring all orientations.

### 2.4 Layers kept logically separate

The remaining mechanisms are audited separately:

- primitive projection;
- parity, especially the `p=2` / 2-adic layer;
- representation and fiber multiplicity;
- odd-prime local density;
- cutoff and boundary effects;
- exact-one overlaps.

For a future Stage12 bridge, a map

\[
\Pi_{12}:\mathcal R_{12}(B)
\longrightarrow
\mathcal U(B)\times\{ab,ac,bc\}\times S_3
\]

may be introduced, with fiber multiplicity `m_12`. No constant-fiber assumption is made before that map is audited.

Likewise, no Euler-product factorization of Stage13 directional constants and no claim that odd-prime local factors are independent or common has yet been made.

---

## §3 — Task 13-3: origin of the leading 2

### 3.1 Stage13-3a question

The first discriminator is deliberately simple:

> Is the near-`2:1:1` pattern already present in raw incidence
> \(A_{ab}:A_{ac}:A_{bc}\) before the exact-one sieve?

If yes, overlap correction is not required to generate the leading finite-range pattern. If no, overlap becomes a primary candidate mechanism.

### 3.2 Exact finite enumeration method

The support script is

```text
stages/stage13/scripts/13-3/raw_incidence.py
```

and the checked-in report is

```text
stages/stage13/data/13-3/raw_incidence.json
```

The enumeration uses the fact that every raw incidence with an integer face diagonal `p` and integer space diagonal `d` can be written as two nested integer right triangles:

\[
x^2+y^2=p^2,
\qquad
p^2+t^2=d^2.
\]

All positive integer Pythagorean triples with hypotenuse at most the requested cutoff are generated by the standard primitive Euclid parameterization followed by positive scaling. For every outer triple, either leg is tested as the candidate face diagonal `p`; every inner representation of that `p` is then joined to the remaining edge `t`.

The resulting edge triple `(x,y,t)` is sorted to `a<b<c`, repeated-edge cases are removed, and

\[
\gcd(a,b,c)=1
\]

is enforced. The distinguished face is then classified as `ab`, `ac`, or `bc` by its position after sorting.

For a fixed canonical object `(a,b,c,d)`, face bits are unioned rather than deduplicating the object before incidence counting. Thus an object with two integer faces contributes once to each appropriate raw incidence, exactly as the definitions of `A_uv` require.

This procedure is complete for raw incidence: any object counted by some `A_uv` supplies the inner right triangle formed by that face and its integer diagonal, and the outer right triangle formed by that face diagonal, the remaining edge, and `d`; conversely every retained nested pair satisfies the Stage13 base equations and the selected face condition.

### 3.3 Finite results

The raw counts are:

| `B` | `A_ab` | `A_ac` | `A_bc` | `bc`-normalized raw ratio |
|---:|---:|---:|---:|---:|
| 1,000 | 306 | 160 | 138 | `2.217391 : 1.159420 : 1` |
| 3,000 | 1,198 | 613 | 591 | `2.027073 : 1.037225 : 1` |
| 10,000 | 5,281 | 2,740 | 2,659 | `1.986085 : 1.030463 : 1` |
| 30,000 | 19,999 | 10,436 | 9,784 | `2.044052 : 1.066639 : 1` |
| 100,000 | 84,212 | 43,236 | 40,760 | `2.066045 : 1.060746 : 1` |

At `B=100000`, the raw proportion vector is

\[
\frac{1}{168208}(84212,43236,40760)
\approx
(0.500642,0.257039,0.242319).
\]

This is already extremely close to the observed exact-one proportion vector

\[
(0.50078,0.25698,0.24224).
\]

### 3.4 Validation against the existing exact-one data

The same face-bit ledger gives, at `B=100000`, pair overlaps

\[
(A_{ab,ac},A_{ab,bc},A_{ac,bc})=(33,33,23)
\]

and

\[
A_3=0.
\]

Applying the exact identities from §2 yields

\[
N_{ab}=84212-33-33=84146,
\]

\[
N_{ac}=43236-33-23=43180,
\]

\[
N_{bc}=40760-33-23=40704,
\]

which exactly reproduces the Stage13-1 finite dataset. This is an internal consistency check of the enumeration and classification logic. A dedicated analysis of overlap size and its scaling is deferred to Stage13-3b rather than inferred from one cutoff.

### 3.5 Stage13-3a conclusion

The finite computation answers the Stage13-3a discriminator:

\[
\boxed{
\text{The near-}2:1:1\text{ directional pattern is already present in raw incidence.}
}
\]

At every reported checkpoint from `B=3000` through `B=100000`, `A_ab/A_bc` is close to `2`, while `A_ac/A_bc` is close to `1`. At `B=100000`, passing from raw incidence to exact-one changes

\[
2.066045:1.060746:1
\]

to

\[
2.067266:1.060829:1.
\]

Therefore the exact-one overlap sieve is **not needed to generate the observed leading finite-range 2**. This sharply lowers overlap as the primary explanation for that feature and moves the mechanism search upstream, toward canonical size-order geometry, parity, representation multiplicity, and local arithmetic.

This is **not** an asymptotic theorem. The data do not yet prove that

\[
A_{ab}:A_{ac}:A_{bc}\to2:1:1
\]

or that overlaps are asymptotically negligible. Those are separate claims requiring separate bounds or asymptotics.

### 3.6 State after 13-3a

```text
STAGE13_3A=COMPLETE
RAW_NEAR_2_1_1_PRESENT_BEFORE_EXACT_ONE=true_at_tested_cutoffs
OVERLAP_REQUIRED_TO_GENERATE_FINITE_LEADING_2=false_at_tested_cutoffs
ASYMPTOTIC_RAW_RATIO=UNPROVEN
ASYMPTOTIC_OVERLAP_SIZE=UNPROVEN
NEXT=Stage13-3b_overlap_quantification
```
