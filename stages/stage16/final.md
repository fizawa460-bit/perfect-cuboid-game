# Stage16 final self-contained bundle — R01 candidate

```text
BUNDLE_ID=STAGE16-FINAL-SELF-CONTAINED-20260814-R01
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
STATUS=FRESH_AUDIT_CANDIDATE
STAGE=Stage16
POPULATION=primitive canonical cuboids with exactly one integral face diagonal
SPACE_DIAGONAL_INTEGRALITY=NOT_REQUIRED
COMMON_CUTOFF=R=sqrt(a^2+b^2+c^2)<=B
```

## 1. Executive theorem

Let
\[
\mathcal U(B)=\{0<a<b<c:\gcd(a,b,c)=1,\ a^2+b^2+c^2\le B^2\},
\qquad U(B)=\#\mathcal U(B),
\]
and let
\[
\mathcal B_1(B)=\{(a,b,c)\in\mathcal U(B):\text{exactly one of }a^2+b^2,a^2+c^2,b^2+c^2\text{ is a square}\},
\]
\[
M_1(B)=\#\mathcal B_1(B).
\]
Then
\[
\boxed{M_1(B)\asymp B^2\log B},
\]
while
\[
\boxed{U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2)}.
\]
Consequently
\[
\boxed{\frac{M_1(B)}{U(B)}\asymp\frac{\log B}{B}\to0}.
\]

If `H_1(B)` counts the same primitive canonical `R<=B` population with **at least one** integral face, then
\[
\boxed{H_1(B)\asymp M_1(B)\asymp B^2\log B}.
\]
Thus the exactly-one mask does not change the proved power/log order relative to at-least-one.

No leading asymptotic constant for `M_1(B)` is claimed.

## 2. Population and cutoff lock

- Canonical edges: `0<a<b<c`.
- Primitive means `gcd(a,b,c)=1`; scale copies are removed.
- Exactly-one means exactly one of the three face-square predicates is true.
- `R=sqrt(a^2+b^2+c^2)` is a real geometric height. Stage16 does **not** require `R` to be integral.
- On any later subpopulation with integral space diagonal `d`, one has `R=d` exactly, so `R<=B` and `d<=B` coincide without a loss factor.
- Finite Stage16-20 counts are diagnostic and are not used to prove the theorem.

## 3. Primitive Pythagorean face count

Let `P(X)` be the number of unordered primitive positive Pythagorean triangles with hypotenuse at most `X`.

Every such triangle has the unique primitive Euclid form, after the standard leg-order convention,
\[
x_0=m^2-n^2,\qquad y_0=2mn,\qquad h=m^2+n^2,
\]
with `m>n>=1`, `(m,n)=1`, and opposite parity.

The region `m^2+n^2<=X`, `0<n<m`, has area of order `X`, giving `P(X)<<X`. For the reverse inequality, restrict `(m,n)` to a fixed positive-area subregion strictly inside that sector. Coprime opposite-parity lattice pairs have positive density there by elementary Möbius inclusion-exclusion and the parity restriction. Hence
\[
\boxed{P(X)\asymp X}.
\]
Only this two-sided order is needed.

## 4. Upper bound for the exactly-one population

Every exactly-one object has a unique integral face. Write that face uniquely as
\[
(kx_0,ky_0,kh),
\]
where `(x_0,y_0,h)` is primitive Pythagorean and `k>=1` is the face scale. Let `z` be the third edge.

The cutoff implies `kh<=B` and `z<=B`. Dropping global primitivity, canonical ordering, and the exactly-one postfilter only enlarges the count, so
\[
M_1(B)
\le B\sum_{k\le B}P(B/k)
\ll B\sum_{k\le B}\frac{B}{k}
\ll B^2\log B.
\]
There is no missing overlap factor: an exactly-one object has one and only one marked integral face.

Therefore
\[
\boxed{M_1(B)\ll B^2\log B}.
\]

## 5. Sharp lower-bound construction

Fix a primitive Pythagorean face `(x_0,y_0,h)` and a scale `k` with
\[
kh\le B/4.
\]
Choose the third edge in
\[
B/3<z\le B/2,
\qquad (z,k)=1.
\]
Since `x_0,y_0<h`, both scaled face legs are below `B/4<z`; after sorting the two face legs, the edge triple is strict and canonical with `z` largest. Moreover
\[
R^2=(kh)^2+z^2\le B^2/16+B^2/4< B^2.
\]
Because `(x_0,y_0)=1`,
\[
\gcd(kx_0,ky_0,z)=\gcd(k,z)=1,
\]
so the triple is globally primitive.

For fixed `k`, inclusion-exclusion gives
\[
\#\{B/3<z\le B/2:(z,k)=1\}
=\frac{B}{6}\frac{\varphi(k)}{k}+O(\tau(k)).
\]

It remains to enforce exactly-one. For a fixed positive integer `X`, any accidental square
\[
X^2+z^2=w^2
\]
satisfies
\[
(w-z)(w+z)=X^2.
\]
Hence the number of such `z` is at most `\tau(X^2)`. Applying this to `X=kx_0` and `X=ky_0` removes all choices where either non-designated face becomes integral. Uniformly in the present range, the number removed per face shape is `B^{o(1)}`.

The construction is injective after this deletion: the unique integral face recovers its scale-times-primitive decomposition, and the remaining edge recovers `z`.

For `k` with `B/(4k)` above a fixed threshold, `P(B/(4k))>>B/k`. Thus the main candidate count is
\[
\gg B^2\sum_{k\le cB}\frac{\varphi(k)}{k^2}.
\]
Using
\[
\frac{\varphi(k)}{k}=\sum_{d\mid k}\frac{\mu(d)}{d}
\]
and reversing the finite sum gives
\[
\sum_{k\le X}\frac{\varphi(k)}{k^2}
=\frac{1}{\zeta(2)}\log X+O(1).
\]
The interval-count error is
\[
\ll \sum_{k\le B}P(B/(4k))\tau(k)
\ll B\sum_{k\le B}\frac{\tau(k)}{k}
\ll B(\log B)^2,
\]
and the accidental-square deletion contributes at most
\[
B^{o(1)}\sum_{k\le B}P(B/(4k))
\ll B^{1+o(1)}\log B.
\]
Both are `o(B^2 log B)`. Therefore
\[
\boxed{M_1(B)\gg B^2\log B}.
\]
Combined with the upper bound,
\[
\boxed{M_1(B)\asymp B^2\log B}.
\]

## 6. Common source universe

The number of positive ordered integer triples in the Euclidean ball
\[
a^2+b^2+c^2\le B^2
\]
is
\[
\frac{\pi}{6}B^3+O(B^2).
\]
Möbius inversion over the common gcd gives
\[
\sum_{d\le B}\mu(d)\left(\frac{\pi}{6}(B/d)^3+O((B/d)^2)\right)
=\frac{\pi}{6\zeta(3)}B^3+O(B^2).
\]
Triples with equal coordinates contribute only `O(B^2)`. Every remaining primitive ordered triple has six permutations, exactly one of which satisfies `0<a<b<c`. Hence
\[
\boxed{U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2)}.
\]
Therefore
\[
\boxed{M_1(B)/U(B)\asymp \log(B)/B\to0}.
\]

## 7. Causal decomposition

An unrestricted ordered two-edge pair has order `B^2`. Requiring that pair to form an integral face replaces it by scaled primitive Pythagorean faces:
\[
\sum_{k\le B}P(B/k)
\asymp B\sum_{k\le B}\frac1k
\asymp B\log B.
\]
The third edge remains free at order `B`. Therefore the Stage16 host is of order
\[
(B\log B)\cdot B=B^2\log B.
\]

At the proved resolution:

- the **power drop** from cubic order is caused by the one-face Pythagorean restriction;
- the **logarithm** is caused by the harmonic face-scale sum;
- the third edge supplies the remaining `B` factor;
- primitivity changes density/weights but not the power/log order;
- canonicalization changes multiplicity but not the power/log order;
- exactly-one is order-neutral relative to at-least-one;
- space-diagonal arithmetic is not part of Stage16 and is not charged to this exponent.

To justify the exactly-one statement, let `H_1(B)` count primitive canonical triples under the same cutoff with at least one integral face. A union bound over the three possible faces gives
\[
H_1(B)\ll B^2\log B.
\]
Since `M_1(B)<=H_1(B)` and the proved lower bound gives `M_1(B)>>B^2 log B`, one obtains
\[
\boxed{H_1(B)\asymp M_1(B)\asymp B^2\log B}.
\]
This does **not** prove
\[
H_1(B)-M_1(B)=o(B^2\log B)
\]
or a limiting value of `M_1(B)/H_1(B)`.

## 8. AR-039 compatibility interface

AR-039 supplies a narrower two-parameter family with integral space diagonal and exactly one integral face. For coprime
\[
m>n\ge1,\qquad m\equiv2\pmod{14},\quad n\equiv1\pmod{14},
\]
set
\[
x=m^2-n^2,\quad y=2mn,\quad p=m^2+n^2,
\]
\[
c=(p^2-1)/2,\qquad d=(p^2+1)/2.
\]
The canonical triple `(min(x,y),max(x,y),c)` is primitive, has exactly the `xy` face integral, and has integral space diagonal `d`; the mod-7 certificate excludes the other two face squares.

This family is a valid Stage16 subset because Stage16 does not forbid integral space diagonal. On the family
\[
R=d
\]
exactly, so `d<=B` and the Stage16 cutoff `R<=B` agree. The inherited lower bound `>>B^{1/2}` is therefore a legal regression lower bound inside Stage16, but it is much weaker than the sharp ambient `B^2 log B` law and is never used to infer the Stage16 exponent.

## 9. Finite computation

Stage16-20 produced a deterministic finite baseline using primitive Euclid face generation plus exhaustive third-edge completion and exact postfilters. Representative values are

```text
B=50   M_1(B)=490
B=100  M_1(B)=2620
B=200  M_1(B)=12664
```

Independent direct canonical-triple checks agreed at these cutoffs. The finite table is compatible with the theorem but is not proof input and is not used to infer a leading constant or directional law.

## 10. Intrinsic status and negative knowledge

The upper and lower bounds meet. Therefore the true order of `M_1(B)` is identified up to positive multiplicative constants:
\[
M_1(B)=\Theta(B^2\log B).
\]
At this resolution, the polynomial exponent `2` and the single logarithmic factor are intrinsic, not merely current upper/lower exponents.

Still unknown or deliberately unclaimed:

- a leading asymptotic constant for `M_1(B)`;
- a full asymptotic formula with error term;
- a directional limiting vector for which canonical face is integral;
- `H_1(B)-M_1(B)=o(B^2 log B)`;
- a limiting ratio `M_1(B)/H_1(B)`;
- any Stage16-to-Stage17 survival ratio after imposing integral space diagonal;
- any conclusion about existence or nonexistence of perfect cuboids.

## 11. Stage-end artifact decision

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=Stage16 proves a new sharp population law and causal decomposition that Stage17 and Stage21 are expected to cite repeatedly; reconstructing the proof from checkpoints would be unsafe.
ARSENAL_PROMOTION_REQUIRED=NO
ARSENAL_CANDIDATES=NONE
ARSENAL_REASON=The portable ingredients are already covered by AR-002 primitive Euclid decomposition, AR-001 population conventions, and AR-039 regression construction. The new B^2 log B synthesis is primarily a Stage16 population theorem rather than a distinct cross-stage weapon.
```

## 12. Safety ledger

```text
CHECKPOINT_10=PROVED
CHECKPOINT_20=COMPUTED
CHECKPOINT_30=PROVED
CHECKPOINT_40=PROVED
CHECKPOINT_50=PROVED
CHECKPOINT_60=PROVED
CHECKPOINT_70=PROVED_CANDIDATE_PENDING_FRESH_AUDIT
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
EVIDENCE_LEVELS_COMPLETE=YES
DEPENDENCY_LEDGER_COMPLETE=YES
OPEN_GATE_REENTRY_JUSTIFIED=NOT_APPLICABLE
ARSENAL_SUPERSESSION_CHECK=NOT_APPLICABLE
DOUBLE_CHARGE_CHECK=PASS
```

## 13. Provenance

Canonical Stage16 sources:

- `stages/stage16/16-10/result.md`
- `stages/stage16/16-20/result.md`
- `stages/stage16/16-20/counts.csv`
- `stages/stage16/16-30/result.md`
- `stages/stage16/16-30/audit.md`
- `stages/stage16/16-40/result.md`
- `stages/stage16/16-40/audit.md`
- `stages/stage16/16-50/result.md`
- `stages/stage16/16-50/audit.md`
- `stages/stage16/16-60/result.md`
- `stages/stage16/16-60/audit.md`
- `stages/stage16/16-70/result.md`
- `stages/stage16/16-controller.json`
- `docs/stage16-28-population-roadmap.md`

No repository path substitutes for a load-bearing proof above; the paths are provenance only.

## 14. Fresh hostile-review checklist

A fresh Stage16 audit must check at least:

1. population/cutoff/primitivity/canonical conventions;
2. uniqueness and completeness of the Pythagorean-face upper-bound decomposition;
3. injectivity, primitivity, cutoff, and accidental-square deletion in the lower family;
4. summed error sizes versus `B^2 log B`;
5. the primitive source-universe constant `pi/(36 zeta(3))`;
6. the `H_1(B)` at-least-one comparison without silently claiming overlap little-o;
7. AR-039 only as a narrower regression subset with exact `R=d` adapter;
8. intrinsic-status and non-claim boundaries;
9. bundle and arsenal decisions;
10. controller/current-status/manifest consistency.

## 15. Machine-readable lock

```text
STAGE16_FINAL_THEOREM=M_1(B) ASYM B^2 log B
SOURCE_UNIVERSE=U(B)=pi/(36 zeta(3)) B^3+O(B^2)
STAGE16_THINNING=M_1(B)/U(B) ASYM log(B)/B -> 0
AT_LEAST_ONE_HOST=H_1(B) ASYM B^2 log B
TRUE_ORDER_IDENTIFIED=true
POLYNOMIAL_EXPONENT=2
LOG_POWER=1
LEADING_CONSTANT_PROVED=false
PRIMARY_CAUSE=ONE_FACE_PYTHAGOREAN_DIMENSION_DROP
LOG_SOURCE=HARMONIC_FACE_SCALE_SUM
GLOBAL_OVERLAP_LITTLE_O_PROVED=false
DIRECTIONAL_LAW_PROVED=false
SPACE_DIAGONAL_CHARGED=false
PERFECT_CUBOID_CONCLUSION=NONE
SELF_CONTAINED_STATUS=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
EXTERNAL_THEOREM_DEPENDENCIES=NONE_LOAD_BEARING_BEYOND_ELEMENTARY_STANDARD_FACTS_EXPLICITLY_USED_ABOVE
FRESH_AUDIT_REQUIRED=true
NEXT_STAGE_AFTER_PASS=Stage17
```
