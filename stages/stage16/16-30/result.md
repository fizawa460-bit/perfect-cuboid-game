# Stage16-30 — ratio / thinning law

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Question

Stage16-20 established a finite census for the frozen population

\[
\mathcal B_1(B)=\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B,\ \text{exactly one face diagonal integral}\},
\qquad M_1(B)=\#\mathcal B_1(B),
\]

with

\[
R=\sqrt{a^2+b^2+c^2}.
\]

Checkpoint 30 asks for a genuine ratio / thinning law rather than a fit to the finite table.

Define the Stage16 source universe

\[
\mathcal U(B)=\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B\},
\qquad U(B)=\#\mathcal U(B).
\]

No face-square or space-diagonal condition is imposed in \(\mathcal U(B)\).

## Theorem 16-30.1 — exact order of the Stage16 population

There are constants \(0<c<C<\infty\) such that, for all sufficiently large \(B\),

\[
cB^2\log B\le M_1(B)\le CB^2\log B.
\]

Equivalently,

\[
\boxed{M_1(B)\asymp B^2\log B.}
\]

The source universe satisfies

\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2).
\]

Hence

\[
\boxed{\frac{M_1(B)}{U(B)}\asymp\frac{\log B}{B}\to0.}
\]

Thus exactly one integral face diagonal is abundant in absolute terms, of order \(B^2\log B\), but is zero-density inside all primitive canonical cuboids under the same geometric cutoff.

This theorem does **not** claim an asymptotic constant for \(M_1(B)\).

## Proof

### 1. Primitive Pythagorean face shapes have linear counting order

Let \(P(X)\) be the number of unordered primitive positive Pythagorean triangles with hypotenuse at most \(X\).

By the primitive Euclid parametrization (AR-002), every such shape is represented uniquely by

\[
x_0=m^2-n^2,\qquad y_0=2mn,\qquad h=m^2+n^2,
\]

with \(m>n\ge1\), \((m,n)=1\), and opposite parity, after fixing the usual leg-order convention.

The region \(m^2+n^2\le X\) has area \(\asymp X\), so trivially \(P(X)\ll X\). For the reverse bound, restrict \((m,n)\) to any fixed positive-area box lying strictly inside

\[
0<n<m,\qquad m^2+n^2\le X.
\]

Möbius inclusion-exclusion for coprimality, together with the opposite-parity condition, leaves a positive density of the lattice points in that box. Therefore

\[
P(X)\gg X
\]

for sufficiently large \(X\). Hence

\[
P(X)\asymp X.
\]

Only this two-sided order is used below; no exact constant for \(P(X)\) is required.

### 2. Upper bound for \(M_1(B)\)

An exactly-one object has a unique integral face. Write that face as

\[
(kx_0,ky_0,kh),
\]

where \((x_0,y_0,h)\) is primitive Pythagorean and \(k\ge1\) is its unique scale. If the third edge is \(z\), then

\[
R^2=(kh)^2+z^2\le B^2.
\]

For an upper bound we may drop the global primitivity, canonical-order, and exact-one postfilters and simply use \(z\le B\). Therefore

\[
M_1(B)
\le B\sum_{k\le B}P(B/k)
\ll B\sum_{k\le B}\frac{B}{k}
\ll B^2\log B.
\]

No overlap factor is missing: an exactly-one object has exactly one integral face, so it has one marked face in this parametrization.

### 3. A large exactly-one subfamily for the lower bound

Fix a primitive Pythagorean face \((x_0,y_0,h)\) and a scale \(k\) satisfying

\[
kh\le B/4.
\]

Choose the third edge in the interval

\[
B/3<z\le B/2,
\]

subject to

\[
(z,k)=1.
\]

Because \(x_0,y_0<h\), both scaled face legs are less than \(B/4<z\). Thus the resulting edge triple is already strict after sorting the two face legs, and

\[
R^2=(kh)^2+z^2\le B^2/16+B^2/4=5B^2/16<B^2.
\]

Since \((x_0,y_0)=1\),

\[
\gcd(kx_0,ky_0,z)=\gcd(k,z)=1.
\]

So every retained triple is globally primitive and satisfies the Stage16 cutoff.

For fixed \(k\), inclusion-exclusion gives

\[
\#\{B/3<z\le B/2:(z,k)=1\}
=\frac{B}{6}\frac{\varphi(k)}{k}+O(\tau(k)).
\]

It remains only to remove choices for which a second face accidentally becomes integral. For a fixed positive integer \(X\), solutions of

\[
X^2+z^2=w^2
\]

satisfy

\[
(w-z)(w+z)=X^2.
\]

Hence the number of such \(z\) is at most \(\tau(X^2)\). For the two non-designated faces, each scaled face contributes at most

\[
\tau((kx_0)^2)+\tau((ky_0)^2)=B^{o(1)}
\]

excluded third edges, uniformly in the present range. Removing these values leaves an exactly-one object.

The construction is injective: the unique integral face recovers its scaled primitive Pythagorean decomposition and the remaining edge is \(z\).

### 4. Summing the lower-bound family

For all \(k\) with \(B/(4k)\) above a fixed absolute threshold, Step 1 gives

\[
P(B/(4k))\gg B/k.
\]

The main candidate contribution is therefore

\[
\gg B^2\sum_{k\le cB}\frac{\varphi(k)}{k^2}.
\]

The elementary identity

\[
\frac{\varphi(k)}{k}=\sum_{d\mid k}\frac{\mu(d)}{d}
\]

implies, after reversing the finite sum,

\[
\sum_{k\le X}\frac{\varphi(k)}{k^2}
=\frac{1}{\zeta(2)}\log X+O(1).
\]

Thus the main contribution is \(\gg B^2\log B\).

The interval-count error contributes

\[
\ll B\sum_{k\le B}\frac{\tau(k)}{k}
\ll B(\log B)^2,
\]

and the accidental-second-face exclusions contribute

\[
B^{o(1)}\sum_{k\le B}P(B/(4k))
\ll B^{1+o(1)}\log B.
\]

Both are \(o(B^2\log B)\). Therefore

\[
M_1(B)\gg B^2\log B.
\]

Combining with Step 2 proves \(M_1(B)\asymp B^2\log B\).

### 5. Size of the common source universe

The number of positive ordered integer triples in the Euclidean ball

\[
a^2+b^2+c^2\le B^2
\]

is

\[
\frac{\pi}{6}B^3+O(B^2).
\]

Möbius inversion on the common gcd, valid because the Euclidean cutoff is homogeneous, gives the primitive ordered count

\[
\frac{\pi}{6\zeta(3)}B^3+O(B^2).
\]

Triples with two equal coordinates contribute only \(O(B^2)\). Dividing the remaining distinct ordered triples by the six edge permutations yields

\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2).
\]

Therefore

\[
\frac{M_1(B)}{U(B)}\asymp\frac{\log B}{B}\to0.
\]

This is on exactly the same primitive/canonical `R<=B` physical measure fixed at Stage16-10.

## Relation to Stage16-20 finite data

The finite table is diagnostic only. For example,

\[
\frac{M_1(B)}{B^2\log B}
\]

is approximately `0.0569, 0.0598, 0.0621, 0.0640, 0.0649, 0.0654, 0.0657` at `B=100,200,400,800,1200,1600,2000` respectively. This is compatible with the proved order but is **not** used to infer a limiting constant.

## Arsenal / provenance audit

- **AR-001**: direct reuse for primitive/canonical projection and exact-one separation.
- **AR-002**: direct reuse for the unique primitive Euclid face decomposition.
- **AR-032**: method-level reuse after an explicit adapter; the common-gcd Möbius step is applied only to the homogeneous source-universe cutoff. No Stage12 coefficient asymptotic is imported.
- **AR-039**: not charged. Its `N_1(B)>>B^(1/2)` integral-space-diagonal family is much thinner and belongs to the later Stage16-50 historical lower-bound ledger, not to this ambient proof.

No Stage14/15 space-diagonal-only counting theorem is promoted to the Stage16 ambient measure.

## Checkpoint classification

```text
EVIDENCE_LEVEL=PROVED
DEPENDS_ON=Stage16-10,Stage16-20,arsenal:AR-001,arsenal:AR-002,arsenal:AR-032
SOURCE_POPULATION=U(B): primitive canonical positive edge triples under R<=B with no face condition
TARGET_POPULATION=M_1(B): primitive canonical exactly-one-face triples under the same R<=B cutoff
SURVIVOR_RATIO=M_1(B)/U(B) ASYM log(B)/B
RATIO_LIMIT_STATUS=ZERO_DENSITY_PROVED
TRUE_ORDER_OF_M1=B^2 log B up to positive constants
EXACT_M1_ASYMPTOTIC_CONSTANT=NOT_CLAIMED
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
FINITE_DATA_USED_AS_PROOF=false
```

This new theorem is load-bearing for checkpoints 40 and 50. In accordance with the safe-batching rule, the main lane stops here for a fresh Stage16 audit instead of self-certifying the later ledgers.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16
CURRENT_CHECKPOINT=30
CHECKPOINTS_ATTEMPTED=30
CHECKPOINTS_SUBMITTED=30
NEW_CLAIMS=M_1(B) ASYM B^2 log B; U(B)=pi/(36 zeta(3)) B^3+O(B^2); M_1(B)/U(B) ASYM log B/B -> 0
REUSED_WEAPONS=AR-001,AR-002,AR-032(method-level after adapter)
CODEX_REQUIRED=false
CODEX_REASON=The checkpoint is a compact mathematical counting argument; no repository-heavy implementation or external execution is required.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16-audit
```