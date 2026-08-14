# Stage18 final self-contained interface bundle, R01 candidate

```text
BUNDLE_ID=STAGE18-FINAL-SELF-CONTAINED-20260814-R01
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
STATUS=CANDIDATE_PENDING_FRESH_STAGE18_AUDIT
STAGE=Stage18
POPULATION=primitive canonical cuboids with exactly two integral face diagonals
SPACE_DIAGONAL_INTEGRALITY=NOT_REQUIRED
COMMON_CUTOFF=R=sqrt(a^2+b^2+c^2)<=B
```

## 1. Executive theorem

Let
\[
\mathcal B_2(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly two face diagonals integral}\},
\]
where \(R=\sqrt{a^2+b^2+c^2}\), and let \(M_2(B)=\#\mathcal B_2(B)\). Then
\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5},\qquad C_{M_2}>0.
\]
For the matched ambient primitive/canonical population
\[
\mathcal U(B)=\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B\},\qquad U(B)=\#\mathcal U(B),
\]
one has
\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2),
\]
and therefore
\[
\boxed{\frac{M_2(B)}{U(B)}\sim\frac{36\zeta(3)C_{M_2}}{\pi}\frac{(\log B)^5}{B^2}\to0}.
\]
Consequently \(M_2(B)\asymp B(\log B)^5\), and the Stage18 population is infinite.

## 2. Population and cutoff lock

- Canonical physical object: one ordered representative `0<a<b<c`.
- Primitive: `gcd(a,b,c)=1`.
- Exactly-two: exactly two of `a^2+b^2`, `a^2+c^2`, `b^2+c^2` are perfect squares.
- No integral-space-diagonal condition is imposed.
- Cutoff: the geometric real length `R=sqrt(a^2+b^2+c^2)<=B`.
- Multiplicity: each primitive canonical physical cuboid is counted once.
- Stage18 finite tables are diagnostic and reproducibility evidence only.

## 3. Frozen upstream interface: Stage15 target theorem

```text
UPSTREAM_STAGE=Stage15
INTERFACE_OBJECT=STAGE18_TARGET
UPSTREAM_THEOREM=M_2(B) ~ C_M2 B(log B)^5 with C_M2>0 for primitive canonical exactly-two-face cuboids under R<=B and no space-diagonal requirement
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
ROLE=absolute Stage18 population law
```

The Stage18 checkpoint10 contract is literally the Stage15 ambient exactly-two population. There is no height substitution, orientation conversion, incidence-to-object conversion, measure conversion, or quantifier change.

## 4. Frozen upstream interface: Stage16 ambient law

```text
UPSTREAM_STAGE=Stage16
INTERFACE_OBJECT=STAGE18_AMBIENT_SOURCE
UPSTREAM_THEOREM=U(B)=pi/(36 zeta(3)) B^3+O(B^2) for primitive canonical positive cuboids under R<=B
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
ROLE=ambient denominator for Stage18 density
```

Here `POPULATION_MATCH=true` refers to the ambient source population used in the Stage18 ratio, not to the exactly-two target. The Stage18 target is a literal subset selected from this same physical source by the exactly-two predicate.

## 5. Internal implication chain

### 5.1 Absolute asymptotic

The first frozen interface applies directly to the Stage18 target, so
\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]
No finite census is used in this implication.

### 5.2 Ambient ratio

Divide the target asymptotic by
\[
U(B)=\frac{\pi}{36\zeta(3)}B^3\left(1+O(B^{-1})\right).
\]
Since the leading ambient constant is positive,
\[
\frac{M_2(B)}{U(B)}\sim\frac{36\zeta(3)C_{M_2}}{\pi}\frac{(\log B)^5}{B^2}.
\]
Thus Stage18 has zero ambient density and a certified net two-power polynomial thinning.

### 5.3 Upper and lower ledgers

Positivity of \(C_{M_2}\) implies, for sufficiently large \(B\), both
\[
M_2(B)\ll B(\log B)^5
\]
and
\[
M_2(B)\gg B(\log B)^5.
\]
These match in power and logarithmic order.

### 5.4 Infinitude

Since \(C_{M_2}>0\) and \(B(\log B)^5\to\infty\), the asymptotic gives \(M_2(B)\to\infty\). Hence infinitely many primitive canonical exactly-two-face cuboids exist in the Stage18 population.

### 5.5 Causal normal form

Two distinct faces of a cuboid share exactly one edge. If the two integral faces are the successful faces, call their shared edge \(s\) and their other edges \(x,y\). Their integrality is equivalent to integers \(p,q\) satisfying
\[
s^2+x^2=p^2,\qquad s^2+y^2=q^2.
\]
The remaining face has sides \(x,y\). Because the Stage18 mask is exactly-two, that remaining face must fail:
\[
x^2+y^2\notin\square.
\]
Conversely, these three conditions give exactly two integral face diagonals. Thus the normal form is equivalent in both directions.

This structure is coupled through the common edge \(s\). Nothing in the proof identifies the two square conditions with independent probability factors.

## 6. Finite computation

The audited deterministic Stage18 census is

```text
B:   50  100  200  400  800  1200  1600  2000
M2:  16   56  172  494  1347 2350  3536  4812
CSV_SHA256=7873368267bbc21e5fd9ec6437d30e84a646ec4ddb14a50746575f59ac932e5a
```

At `B=200`, the shared-edge enumerator and an independent direct canonical brute-force enumeration agree as sets with 172 objects. These checks are `COMPUTED`; they do not prove the asymptotic theorem.

## 7. Causal boundaries and non-claims

Stage18 certifies the net ambient law for the complete exactly-two predicate. It does not certify a factorization of that net cost into separate contributions from the first face, second face, and third-face exclusion.

- The effect of adding the second face to the Stage16 one-face population is Stage22.
- The effect of adding a third face to Stage18 is Stage26.
- Comparison of exactly-two with at-least-two awaits Stage20/26 input.
- Imposing an integral space diagonal creates Stage19 and later Stage24 questions.
- No independence statement is made.
- No conclusion about existence or nonexistence of a perfect cuboid is made.

Canonical ordering, primitivity, `R<=B`, and physical-object counting are common to the ambient source and are not newly charged causal mechanisms.

## 8. Stage70 bounded synthesis verdict

The absolute Stage18 theorem is settled at its certified asymptotic resolution: polynomial exponent `1`, logarithmic power `5`, positive leading constant `C_M2`, and ambient zero density of exact order `(log B)^5/B^2` up to the printed constant.

Further decomposition of the cost requires a new comparison theorem or another roadmap stage. Therefore Stage18 stops rather than importing Stage22 or Stage26 into its own closeout.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=stable interface for Stage19, Stage22, Stage26 and Stage28 with subtle net-versus-incremental causal boundaries
ARSENAL_PROMOTION_REQUIRED=NO
ARSENAL_CANDIDATES=NONE
SYNTHESIS_STOP_RULE_SATISFIED=YES
```

## 9. Provenance ledger

```text
POPULATION_CONTRACT=stages/stage18/18-10/result.md
FINITE_BASELINE=stages/stage18/18-20/result.md
FINITE_COUNTS=stages/stage18/18-20/counts.csv
RATIO=stages/stage18/18-30/result.md
UPPER=stages/stage18/18-40/result.md
LOWER=stages/stage18/18-50/result.md
CAUSAL=stages/stage18/18-60/result.md
SYNTHESIS=stages/stage18/18-70/result.md
STAGE15_INTERFACE=stages/stage15/final.md
STAGE16_INTERFACE=stages/stage16/final.md
```

## 10. Machine-readable lock

```text
BUNDLE_ID=STAGE18-FINAL-SELF-CONTAINED-20260814-R01
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
STATUS=CANDIDATE_PENDING_FRESH_STAGE18_AUDIT
UPSTREAM_INTERFACES_EXACT=true
INTERNAL_CAUSAL_NORMAL_FORM_EMBEDDED=true
POPULATION_AND_CUTOFF_AUDITED=true
MULTIPLICITY_AUDITED=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
FINITE_DATA_PROMOTED_TO_THEOREM=false
INDEPENDENCE_CLAIM=false
SPACE_DIAGONAL_CLAIM=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_STAGE_AFTER_PASS=Stage19
CODEX_REQUIRED=false
AUDIT_REQUIRED=true
```
