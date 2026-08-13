# Stage16 final self-contained bundle — R01 candidate

```text
BUNDLE_ID=STAGE16-FINAL-SELF-CONTAINED-20260814-R01
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
STATUS=AUDITED_PASS_CLOSED
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

If `H_1(B)` counts the same primitive canonical `R<=B` population with at least one integral face, then
\[
\boxed{H_1(B)\asymp M_1(B)\asymp B^2\log B}.
\]
Thus the exactly-one mask does not change the proved power/log order relative to at-least-one. No leading asymptotic constant for `M_1(B)` is claimed.

## 2. Population and cutoff lock

- Canonical edges: `0<a<b<c`.
- Primitive means `gcd(a,b,c)=1`; scale copies are removed.
- Exactly-one means exactly one of the three face-square predicates is true.
- `R=sqrt(a^2+b^2+c^2)` is a real geometric height. Stage16 does not require `R` to be integral.
- On any later subpopulation with integral space diagonal `d`, one has `R=d` exactly, so `R<=B` and `d<=B` coincide.
- Finite Stage16-20 counts are diagnostic and are not used to prove the theorem.

## 3. Primitive Pythagorean faces

Let `P(X)` be the number of unordered primitive positive Pythagorean triangles with hypotenuse at most `X`.

### 3.1 Exhaustive and unique primitive Euclid parametrization

Take a primitive Pythagorean triple
\[
x^2+y^2=h^2,
\qquad \gcd(x,y)=1.
\]
Exactly one leg is even. After swapping the legs if needed, let `y` be even. Then `x,h` are odd. Put
\[
A=\frac{h+x}{2},\qquad C=\frac{h-x}{2}.
\]
We have
\[
AC=(y/2)^2.
\]
Also `gcd(A,C)=1`: a common divisor divides both `A+C=h` and `A-C=x`, hence divides `gcd(h,x)=1`. Since the coprime positive integers `A,C` have square product, each is a square. Thus
\[
A=m^2,\qquad C=n^2
\]
for unique positive integers `m>n`. Therefore
\[
h=m^2+n^2,\qquad x=m^2-n^2,\qquad y=2mn.
\]
The primitivity of the original triple gives `gcd(m,n)=1`; since `h` is odd, `m,n` have opposite parity. Conversely, any `m>n>=1` with `gcd(m,n)=1` and opposite parity gives a primitive Pythagorean triple by the displayed formulas. Uniqueness follows because
\[
m^2=(h+x)/2,\qquad n^2=(h-x)/2.
\]
After the fixed leg-order convention this gives a one-to-one parametrization of unordered primitive positive Pythagorean triangles.

### 3.2 Proof that `P(X) asymp X`

The condition `h=m^2+n^2<=X` places `(m,n)` in the sector
\[
0<n<m,\qquad m^2+n^2\le X.
\]
With `t=sqrt(X)`, this is a fixed planar sector dilated by `t`, so the total number of integer pairs is `O(t^2)=O(X)`. Hence `P(X)<<X`.

For the lower bound, choose a fixed polygonal region `Omega` of positive area whose closure lies strictly inside
\[
\{(u,v):0<v<u,\ u^2+v^2<1\}.
\]
Count pairs `(m,n)` in `t Omega` with `m` even, `n` odd, and `gcd(m,n)=1`. On the parity class `m` even, `n` odd, every common divisor is odd, so Möbius inversion gives
\[
N(t)=\sum_{\substack{d\ge1\\ d\ \mathrm{odd}}}\mu(d)N_d(t),
\]
where `N_d(t)` counts points of `t Omega` with `d|m`, `d|n`, `m` even, `n` odd`. This is a translate of a lattice of covolume `4d^2`, hence by the elementary area-plus-boundary estimate for a fixed polygon,
\[
N_d(t)=\frac{\operatorname{area}(\Omega)}{4d^2}t^2+O(t/d+1).
\]
Only `d=O(t)` can occur. Summing gives
\[
N(t)=\frac{\operatorname{area}(\Omega)}{4}t^2
\sum_{d\ \mathrm{odd}}\frac{\mu(d)}{d^2}
+O(t\log t).
\]
The Euler product
\[
\sum_{d\ \mathrm{odd}}\frac{\mu(d)}{d^2}
=\prod_{p\ \mathrm{odd}}(1-p^{-2})
\]
is positive. Therefore `N(t)>>t^2=X`. Every counted pair gives a distinct primitive Pythagorean triangle with hypotenuse `<X`. Hence
\[
\boxed{P(X)\asymp X}.
\]

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
There is no missing overlap factor because an exactly-one object has one and only one integral face. Thus
\[
\boxed{M_1(B)\ll B^2\log B}.
\]

## 5. Sharp lower-bound construction

Fix a primitive Pythagorean face `(x_0,y_0,h)` and a scale `k` with
\[
kh\le B/4.
\]
Choose
\[
B/3<z\le B/2,
\qquad (z,k)=1.
\]
Since `x_0,y_0<h`, both scaled face legs are below `B/4<z`; after sorting the two face legs, the edge triple is strict and canonical with `z` largest. Moreover
\[
R^2=(kh)^2+z^2\le B^2/16+B^2/4<B^2.
\]
Because `gcd(x_0,y_0)=1`,
\[
\gcd(kx_0,ky_0,z)=\gcd(k,z)=1,
\]
so the triple is globally primitive.

### 5.1 Coprime third-edge count

By inclusion-exclusion,
\[
\#\{B/3<z\le B/2:(z,k)=1\}
=\sum_{d\mid k}\mu(d)
\left(\left\lfloor\frac{B}{2d}\right\rfloor-
\left\lfloor\frac{B}{3d}\right\rfloor\right).
\]
Therefore
\[
\#\{B/3<z\le B/2:(z,k)=1\}
=\frac{B}{6}\sum_{d\mid k}\frac{\mu(d)}d+O(\tau(k))
=\frac{B}{6}\frac{\varphi(k)}k+O(\tau(k)).
\]

### 5.2 Accidental-square deletion and uniform divisor bound

For fixed positive `X`, if
\[
X^2+z^2=w^2,
\]
then
\[
(w-z)(w+z)=X^2.
\]
Each solution gives a factor pair of `X^2`, so the number of possible `z` is at most `tau(X^2)`.

We now prove the uniform estimate used here. For every `epsilon>0` there is a constant `C_epsilon` such that
\[
\tau(n)\le C_\epsilon n^\epsilon
\]
for all positive integers `n`. Write `n=prod p^a`. For primes `p>=2^{1/epsilon}`, one has
\[
a+1\le2^a\le p^{\epsilon a}.
\]
There are only finitely many smaller primes, and for each such prime
\[
\sup_{a\ge0}\frac{a+1}{p^{\epsilon a}}<\infty.
\]
Multiplying these finitely many constants proves the bound. Applying it with exponent `epsilon/2` to `n=X^2` gives
\[
\tau(X^2)\ll_\epsilon X^\epsilon.
\]
Since in the construction `X<=B/4`, this is uniform and may be written `B^{o(1)}`.

Applying the factorization bound to `X=kx_0` and `X=ky_0` removes all choices where either nondesignated face becomes integral. Thus exactly-one is enforced after deleting at most `B^{o(1)}` third edges per face-shape/scale pair.

The construction is injective after deletion: the unique integral face recovers its primitive Euclid shape and scale, and the remaining edge recovers `z`.

### 5.3 Main term and error sums

For `k` with `B/(4k)` above a fixed threshold, Section 3 gives
\[
P(B/(4k))\gg B/k.
\]
Hence the main candidate count is
\[
\gg B^2\sum_{k\le cB}\frac{\varphi(k)}{k^2}.
\]
Using
\[
\frac{\varphi(k)}k=\sum_{d\mid k}\frac{\mu(d)}d
\]
and writing `k=dm`,
\[
\sum_{k\le X}\frac{\varphi(k)}{k^2}
=\sum_{d\le X}\frac{\mu(d)}{d^2}
\sum_{m\le X/d}\frac1m.
\]
Since
\[
\sum_{m\le Y}\frac1m=\log Y+\gamma+O(1/Y),
\]
while `sum |mu(d)| log d/d^2` converges, we get
\[
\sum_{k\le X}\frac{\varphi(k)}{k^2}
=\left(\sum_{d=1}^\infty\frac{\mu(d)}{d^2}\right)\log X+O(1)
=\frac1{\zeta(2)}\log X+O(1).
\]

For the interval-count error, use `P(B/(4k))<<B/k` and
\[
\sum_{k\le B}\frac{\tau(k)}k
=\sum_{ab\le B}\frac1{ab}
\le\left(\sum_{a\le B}\frac1a\right)
\left(\sum_{b\le B}\frac1b\right)
\ll(\log B)^2.
\]
Therefore
\[
\sum_{k\le B}P(B/(4k))\tau(k)
\ll B(\log B)^2.
\]
The accidental-square deletion contributes at most
\[
B^{o(1)}\sum_{k\le B}P(B/(4k))
\ll B^{1+o(1)}\log B.
\]
Both errors are `o(B^2 log B)`. Consequently
\[
\boxed{M_1(B)\gg B^2\log B}.
\]
Together with Section 4,
\[
\boxed{M_1(B)\asymp B^2\log B}.
\]

## 6. Common source universe

### 6.1 Positive-octant lattice count

Let
\[
N_3(B)=\#\{v\in\mathbb Z^3:\|v\|_2\le B\}.
\]
Attach to each lattice point its unit cube centered at that point. The union of cubes centered at points of the radius-`B` ball is contained in the radius-`B+sqrt(3)/2` ball, while the radius-`B-sqrt(3)/2` ball is contained in the union. Hence
\[
\frac{4\pi}{3}(B-\sqrt3/2)^3
\le N_3(B)
\le\frac{4\pi}{3}(B+\sqrt3/2)^3,
\]
so
\[
N_3(B)=\frac{4\pi}{3}B^3+O(B^2).
\]
Points with at least one zero coordinate lie on three coordinate planes and contribute only `O(B^2)`. The remaining points split equally among the eight open octants by sign symmetry. Therefore the number of positive ordered triples is
\[
\boxed{\frac\pi6B^3+O(B^2)}.
\]

### 6.2 Primitive and canonical count

Möbius inversion over the common gcd gives
\[
\sum_{d\le B}\mu(d)
\left(\frac\pi6(B/d)^3+O((B/d)^2)\right).
\]
The error is
\[
O\left(B^2\sum_{d\le B}d^{-2}\right)=O(B^2).
\]
Also
\[
\sum_{d\le B}\frac{\mu(d)}{d^3}
=\frac1{\zeta(3)}+O(B^{-2}),
\]
so the primitive positive ordered count is
\[
\frac{\pi}{6\zeta(3)}B^3+O(B^2).
\]
Triples with two equal coordinates contribute `O(B^2)`: for each of the three equality choices there are only `O(B^2)` integer pairs inside the ball. Every remaining primitive ordered triple has six permutations, exactly one satisfying `0<a<b<c`. Hence
\[
\boxed{U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2)}.
\]
Therefore
\[
\boxed{M_1(B)/U(B)\asymp\log(B)/B\to0}.
\]

## 7. Causal decomposition

An unrestricted ordered two-edge pair has order `B^2`. Requiring that pair to form an integral face replaces it by scaled primitive Pythagorean faces:
\[
\sum_{k\le B}P(B/k)
\asymp B\sum_{k\le B}\frac1k
\asymp B\log B.
\]
The third edge remains free at order `B`, so the Stage16 host has order
\[
(B\log B)\,B=B^2\log B.
\]
Thus the power drop is caused by the one-face Pythagorean restriction and the logarithm by the harmonic face-scale sum. Primitivity changes density/weights but not the proved power/log order; canonicalization changes multiplicity but not that order.

Let `H_1(B)` count primitive canonical triples under the same cutoff with at least one integral face. A union bound over the three face choices gives
\[
H_1(B)\ll B^2\log B.
\]
Since
\[
M_1(B)\le H_1(B)
\]
and Section 5 gives `M_1(B)>>B^2 log B`,
\[
\boxed{H_1(B)\asymp M_1(B)\asymp B^2\log B}.
\]
This does not prove `H_1(B)-M_1(B)=o(B^2 log B)` or a limiting value of `M_1(B)/H_1(B)`.

## 8. AR-039 compatibility interface

AR-039 supplies a narrower exactly-one family that additionally has integral space diagonal. It is not load-bearing for the Stage16 asymptotic theorem. On that family the geometric height satisfies `R=d` exactly, so the historical cutoff `d<=B` equals the Stage16 cutoff `R<=B`. Its weaker `B^(1/2)` lower bound is retained only as a Stage17/21 regression interface and is never used to infer the ambient Stage16 exponent.

## 9. Finite computation

Stage16-20 produced a deterministic finite baseline. Representative values are

```text
B=50   M_1(B)=490
B=100  M_1(B)=2620
B=200  M_1(B)=12664
```

Independent direct canonical-triple checks agreed at these cutoffs. The finite table is diagnostic only.

## 10. Intrinsic status and negative knowledge

The upper and lower bounds meet, so
\[
M_1(B)=\Theta(B^2\log B).
\]
At this resolution the polynomial exponent `2` and the single logarithmic factor are intrinsic, not merely current upper/lower exponents.

Still unknown or deliberately unclaimed:

- a leading asymptotic constant for `M_1(B)`;
- a full asymptotic formula with error term;
- a directional limiting vector for which canonical face is integral;
- `H_1(B)-M_1(B)=o(B^2 log B)`;
- a limiting ratio `M_1(B)/H_1(B)`;
- the Stage16-to-Stage17 survival ratio after imposing integral space diagonal;
- any conclusion about existence or nonexistence of perfect cuboids.

## 11. Self-containedness and external-input boundary

All load-bearing mathematics used for the Stage16 theorem is embedded above, including:

- primitive Euclid parametrization, exhaustiveness, and uniqueness;
- the positive-density proof of `P(X) asymp X`;
- the uniform divisor bound giving `tau(X^2)=B^{o(1)}`;
- `sum_{k<=B} tau(k)/k << (log B)^2`;
- the positive-octant lattice count `pi B^3/6+O(B^2)` and its boundary error;
- the Möbius step giving the primitive source-universe constant.

No published external theorem is load-bearing for the Stage16 conclusion. The harmonic-sum identities and Euler products used above are explicitly derived to the level needed here. AR-039 is a non-load-bearing frozen regression interface only.

```text
INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
EXTERNAL_THEOREM_DEPENDENCIES=NONE
UPSTREAM_LOAD_BEARING_THEOREM_DEPENDENCIES=NONE
AR039_LOAD_BEARING=false
```

## 12. Stage-end artifact decision

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=Stage16 proves a new sharp population law and causal decomposition that Stage17 and Stage21 are expected to cite repeatedly; reconstructing the proof from checkpoints would be unsafe.
ARSENAL_PROMOTION_REQUIRED=NO
ARSENAL_CANDIDATES=NONE
ARSENAL_REASON=The portable ingredients are already covered by AR-002 primitive Euclid decomposition, AR-001 population conventions, and AR-039 regression construction. The new B^2 log B synthesis is primarily a Stage16 population theorem rather than a distinct cross-stage weapon.
```

## 13. Safety ledger

```text
CHECKPOINT_10=PROVED
CHECKPOINT_20=COMPUTED
CHECKPOINT_30=PROVED
CHECKPOINT_40=PROVED
CHECKPOINT_50=PROVED
CHECKPOINT_60=PROVED
CHECKPOINT_70=PROVED_AUDITED_PASS
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
EVIDENCE_LEVELS_COMPLETE=YES
DEPENDENCY_LEDGER_COMPLETE=YES
OPEN_GATE_REENTRY_JUSTIFIED=NOT_APPLICABLE
ARSENAL_SUPERSESSION_CHECK=NOT_APPLICABLE
DOUBLE_CHARGE_CHECK=PASS
```

## 14. Provenance

Canonical Stage16 sources include `stages/stage16/16-10/result.md`, `16-20`, `16-30`, `16-40`, `16-50`, `16-60`, `16-70`, the Stage16 controller, and the Stage16-28 roadmap/policies. Repository paths are provenance only; no path substitutes for a load-bearing proof above.

## 15. Fresh hostile-review checklist

A fresh Stage16 audit must check at least:

1. population/cutoff/primitivity/canonical conventions;
2. Euclid parametrization exhaustiveness and uniqueness;
3. the positive-density proof of `P(X) asymp X`;
4. injectivity, primitivity, cutoff, and accidental-square deletion in the lower family;
5. the uniform divisor bound and summed error estimates;
6. the positive-octant lattice count and primitive source-universe constant;
7. the `H_1(B)` comparison without silently claiming overlap little-o;
8. AR-039 only as a non-load-bearing regression subset with exact `R=d` adapter;
9. intrinsic-status and non-claim boundaries;
10. controller/current-status/manifest consistency.

## 16. Machine-readable lock

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
INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
EXTERNAL_THEOREM_DEPENDENCIES=NONE
FRESH_AUDIT_REQUIRED=false
NEXT_STAGE_AFTER_PASS=Stage17
```


## Certified closeout status

This artifact was submitted as an audit candidate and was subsequently certified by [stages/stage16/16-70/audit.md](../stage16/16-70/audit.md) in PR #901. Current canonical status: `AUDITED_PASS_CLOSED`. Frozen mathematical claims and nonclaims are unchanged.
