# Stage16S-30 — ratio / thinning law

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Population lock

Stage16S keeps the audited checkpoint-10 contract unchanged:

- positive integer edges with `0<a<b<c`;
- `gcd(a,b,c)=1`;
- geometric height `R=sqrt(a^2+b^2+c^2)<=B`;
- `SPACE_AT_LEAST`: `R` integral, with no face-diagonal restriction;
- `SPACE_ONLY`: `SPACE_AT_LEAST` with zero integral face diagonals.

Write

\[
N_S^{\mathrm{all}}(B)=\#\mathcal S_{\mathrm{all}}(B),\qquad
N_S^0(B)=\#\mathcal S_0(B).
\]

The ambient primitive/canonical source count from Stage16-30 is

\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2).
\]

Checkpoint 30 asks for genuine asymptotic ratios, not a fit to the Stage16S-20 finite table.

## Literature input: primitive Pythagorean quadruples

Werner Hürlimann, *Exact and Asymptotic Evaluation of the Number of Distinct Primitive Cuboids*, Journal of Integer Sequences 18 (2015), Article 15.2.5, studies positive primitive solutions of

\[
x^2+y^2+z^2=t^2
\]

modulo permutation. His Theorem 7 gives, for the cumulative count of distinct primitive nonzero cuboids with odd diagonal `t<=x`, the leading asymptotic

\[
N_3^{H}(x)\sim \frac{x^2}{32G},
\]

where

\[
G=L(2,\chi_4)
\]

is Catalan's constant. The paper also isolates the repeated-edge subpopulation through its cumulative `N_2(x;2)` term, with

\[
N_2(x;2)\sim \frac{\sqrt2}{2\pi}x.
\]

Only the leading quadratic term and the fact that the repeated-edge correction is `O(x)` are needed here.

## Exact adapter to the Stage16S contract

Three compatibility checks are required before importing the literature asymptotic.

### 1. Primitive Stage16S objects have odd space diagonal

On the target population the positive space diagonal is `d=R`. If `d` were even, then

\[
a^2+b^2+c^2\equiv0\pmod4.
\]

Since a square is `0` or `1 mod 4`, the sum of three squares can be `0 mod 4` only when all three squares are `0 mod 4`. Thus `a,b,c` would all be even, contradicting `gcd(a,b,c)=1`.

Therefore every primitive Stage16S object has odd `d`. Hürlimann's odd-diagonal cumulative theorem misses no Stage16S object.

### 2. The primitivity conventions agree

Hürlimann uses

\[
\gcd(a,b,c,d)=1.
\]

Stage16S uses `gcd(a,b,c)=1`. If a positive integer divides all three edges, then the equation

\[
d^2=a^2+b^2+c^2
\]

forces that divisor to divide `d` as well. Hence the two primitivity conventions are equivalent on integral-space-diagonal objects.

### 3. Strict canonical ordering only removes a linear-size equality family

Hürlimann's distinct count permits repeated positive edges. Stage16S requires strict `a<b<c`.

An all-equal positive solution is impossible because `3a^2=d^2` has no nonzero integer solution. Thus every repeated-edge object has exactly two equal edges and, after permutation, is represented by

\[
x^2+2y^2=d^2.
\]

This is precisely the `N_2(B;2)` equality term separated in the literature count. Consequently the project adapter is exact:

\[
\boxed{
N_S^{\mathrm{all}}(B)=N_3^{H}(B)-N_2(B;2).
}
\]

Because `N_2(B;2)=O(B)`, the strict-order correction is lower order. Therefore

\[
\boxed{
N_S^{\mathrm{all}}(B)\sim \frac{B^2}{32G}.
}
\]

The Stage16S-20 finite census is compatible with this leading constant. For example, at `B=2000`,

\[
\frac{N_S^{\mathrm{all}}(2000)}{2000^2}
=\frac{136060}{4000000}\approx0.034015,
\]

while

\[
\frac1{32G}\approx0.034116.
\]

This numerical agreement is diagnostic only and is not used in the proof.

## Ambient thinning law for SPACE_AT_LEAST

Combining the Stage16 ambient theorem with the adapted literature asymptotic gives

\[
\frac{N_S^{\mathrm{all}}(B)}{U(B)}
\sim
\frac{9\zeta(3)}{8\pi G}\frac1B.
\]

Hence

\[
\boxed{
\frac{N_S^{\mathrm{all}}(B)}{U(B)}
\sim
\frac{9\zeta(3)}{8\pi G}\,B^{-1}
\to0.
}
\]

Numerically the leading ratio constant is approximately `0.4699466`.

Thus requiring an integral space diagonal is a polynomial `1/B` thinning of the ambient primitive/canonical cuboid population under the common `R<=B` cutoff.

## Excluding all integer-face cases is asymptotically negligible inside Stage16S

Let

\[
C_F(B)=N_S^{\mathrm{all}}(B)-N_S^0(B)
\]

be the number of Stage16S objects having at least one integral face diagonal.

For an upper bound, mark one integral face, say

\[
a^2+b^2=e^2,
\]

and use the space-diagonal equation to obtain the nested Pythagorean system

\[
a^2+b^2=e^2,\qquad e^2+c^2=d^2,\qquad d\le B.
\]

Dropping primitivity and canonical restrictions can only enlarge the count. For fixed `d`, the number of positive pairs `(e,c)` with `e^2+c^2=d^2` is at most

\[
r_2(d^2)\le4\tau(d^2).
\]

For each such `e`, the number of positive pairs `(a,b)` with `a^2+b^2=e^2` is at most

\[
r_2(e^2)\le4\tau(e^2).
\]

Using the standard divisor bound `tau(n)<<_eps n^eps`, for every `eps>0` the number of objects with this marked integral face is

\[
O_\varepsilon(B^{1+\varepsilon}).
\]

There are only three possible faces, so the union bound gives

\[
\boxed{
C_F(B)=O_\varepsilon(B^{1+\varepsilon})
\qquad(\forall\varepsilon>0).
}
\]

Since `N_S^{all}(B)~B^2/(32G)`, this is lower order. Therefore

\[
N_S^0(B)
=N_S^{\mathrm{all}}(B)-C_F(B)
\sim \frac{B^2}{32G},
\]

and

\[
\boxed{
\frac{N_S^0(B)}{N_S^{\mathrm{all}}(B)}
=1-O_\varepsilon(B^{-1+\varepsilon})
\to1.
}
\]

Equivalently, among primitive canonical integral-space-diagonal cuboids, the subpopulation having **any** integral face diagonal has zero density. Removing every face-integral case does not change the leading `B^2/(32G)` population law.

Combining with the ambient denominator also gives

\[
\boxed{
\frac{N_S^0(B)}{U(B)}
\sim
\frac{9\zeta(3)}{8\pi G}\frac1B.
}
\]

At `B=2000`, the finite diagnostic ratio is

\[
\frac{N_S^0}{N_S^{\mathrm{all}}}
=\frac{134621}{136060}\approx0.989424.
\]

Again, the finite value is not used to infer the limit.

## Exact claim boundary

Checkpoint 30 does **not** claim:

- probabilistic independence between the space-diagonal and face-diagonal conditions;
- that the `O_epsilon(B^{1+epsilon})` faceful upper bound is sharp;
- an asymptotic constant for the faceful complement `C_F(B)`;
- a causal explanation for why the nested Pythagorean conditions are sparse;
- any perfect-cuboid existence or nonexistence conclusion.

The true leading law for `SPACE_AT_LEAST` and `SPACE_ONLY`, and the three ratio limits above, are certified. The sharper structure and best upper/lower ledgers remain checkpoint-40/50 work.

## Dependency ledger

```text
SOURCE_POPULATION=U(B): primitive canonical positive triples under R<=B
TARGET_POPULATION_1=SPACE_AT_LEAST
TARGET_POPULATION_2=SPACE_ONLY
COMMON_CUTOFF=R<=B; on target d=R exactly
LITERATURE_INPUT=Hurlimann 2015 JIS 18 Article 15.2.5 Theorem 7 plus repeated-edge N2(x;2) term
LITERATURE_ADAPTER=odd diagonal automatic by primitivity; gcd conventions equivalent; strict-order correction equals repeated-edge N2(B;2)
SPACE_AT_LEAST_ASYMPTOTIC=N_S^all(B) ~ B^2/(32G)
SPACE_ONLY_ASYMPTOTIC=N_S^0(B) ~ B^2/(32G)
AMBIENT_RATIO_ALL=N_S^all(B)/U(B) ~ [9 zeta(3)/(8 pi G)]/B
AMBIENT_RATIO_ONLY=N_S^0(B)/U(B) ~ [9 zeta(3)/(8 pi G)]/B
INTERNAL_ZERO_FACE_RATIO=N_S^0(B)/N_S^all(B) -> 1
FACEFUL_COMPLEMENT=C_F(B)=O_epsilon(B^(1+epsilon))
RATIO_LIMIT_STATUS=PROVED
EVIDENCE_LEVEL=LITERATURE_ADAPTED_WITH_PROVED_PROJECT_ADAPTER
FINITE_DATA_USED_AS_PROOF=false
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=YES_AND_CERTIFIED
```

This checkpoint is load-bearing for Stage16S-40 and for later Stage21 intrinsic-versus-interaction comparisons. Under the safe-batching rule, the main lane stops here for fresh `Stage16S-audit` rather than self-certifying the upper/lower/causal ledgers.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16S
CURRENT_CHECKPOINT=30
CHECKPOINTS_ATTEMPTED=30
CHECKPOINTS_SUBMITTED=30
NEW_CLAIMS=N_S^all(B) ~ B^2/(32G); N_S^0(B) ~ B^2/(32G); both ambient ratios ~ [9 zeta(3)/(8 pi G)]/B; N_S^0/N_S^all -> 1 with faceful complement O_epsilon(B^(1+epsilon))
REUSED_WEAPONS=Stage16-30 ambient U(B),Stage16S-10,Stage16S-20
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 30 is a compact literature-adaptation and divisor-bound proof; no repository-heavy implementation is required.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16S-audit
```