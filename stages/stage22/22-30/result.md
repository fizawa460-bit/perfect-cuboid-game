# Stage22-30 — matched one-face / two-face population ratio

EVIDENCE_LEVEL=PROVED
CHECKPOINT=30
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## 1. Question and semantic lock

Stage22 compares the primitive canonical exactly-one-face and exactly-two-face strata under the same physical cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B.
\]

Write

\[
M_1(B)=\#\{\text{primitive canonical exactly-one-face cuboids with }R\le B\},
\]

\[
M_2(B)=\#\{\text{primitive canonical exactly-two-face cuboids with }R\le B\}.
\]

These strata are disjoint. Therefore `M2/M1` is a matched adjacent-stratum population-size ratio, not a literal subset-survival probability.

## 2. Strongest compatible upstream interfaces

The stronger source interface recovered and fresh-audited in Stage21 is

\[
\boxed{M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.}
\]

The audited Stage15/Stage18 target interface is

\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.}
\]

Stage15-2b explicitly records that `C_M2` is a positive toric/Tamagawa chamber constant but is not evaluated numerically. The repository search found no audited stronger compatible target interface giving a closed numerical value for `C_M2`. Thus the strongest presently portable checkpoint30 theorem keeps `C_M2` symbolic.

The source and target populations use the same canonical convention `0<a<b<c`, primitive convention `gcd(a,b,c)=1`, physical multiplicity one, and the exact same `R<=B` cutoff. No measure or quantifier adapter is required.

## 3. Leading population-size ratio

Direct division of the two audited asymptotics gives

\[
\frac{M_2(B)}{M_1(B)}
\sim
\frac{C_{M_2}B(\log B)^5}{(3/(4\pi^2))B^2\log B}
=
\boxed{\frac{4\pi^2C_{M_2}}{3}\frac{(\log B)^4}{B}}.
\]

Hence

\[
\boxed{\frac{M_2(B)}{M_1(B)}\longrightarrow0.}
\]

The exact polynomial thinning power between the adjacent strata is `B^-1`, with logarithmic compensation `(log B)^4` and positive leading constant `4*pi^2*C_M2/3`.

Equivalently,

\[
M_2(B)=o(M_1(B)).
\]

This statement is theorem-level and uses no finite-data slope.

## 4. Relation to checkpoint20

Checkpoint20 found the finite ratios

```text
B=50    M2/M1=0.0326530612
B=100   M2/M1=0.0213740458
B=200   M2/M1=0.0135818067
B=400   M2/M1=0.0082922073
B=800   M2/M1=0.0049178353
B=1200  M2/M1=0.0035487426
B=1600  M2/M1=0.0028392751
B=2000  M2/M1=0.0024085735
```

Their monotone decrease is compatible with the proved limiting law, but it is not used to derive the exponent, logarithmic power, constant, or limit.

## 5. What the law does and does not mean

The result rigorously quantifies how much smaller the exactly-two stratum is than the exactly-one stratum under a common ambient geometric scale:

```text
POLYNOMIAL_RATIO_POWER=-1
LOG_RATIO_POWER=4
LEADING_RATIO_CONSTANT=4*pi^2*C_M2/3
LEADING_RATIO_CONSTANT_POSITIVE=true
RATIO_LIMIT=0
M2_LITTLE_O_M1=true
```

It does not assert that a particular exactly-one cuboid acquires a second face with this probability. No objectwise transition map from the exactly-one set to the exactly-two set is being claimed.

The result also does not identify the arithmetic mechanism responsible for the full `B^-1 (log B)^4` change. Checkpoints40-60 remain responsible for upper/lower ledgers and causal decomposition, including separating dimension/height effects from the coupled shared-edge Pythagorean structure.

## 6. Reuse-search verdict

The checkpoint10 preflight requirement has been discharged at theorem level:

```text
SEARCH_REQUIRED_BEFORE_NEW_THEOREM=true
SEARCH_SCOPE=ARSENAL+NUM_INDEX+STAGES+SUPPLEMENTS+ARCHIVE+PRS
SEARCH_MODES=direct terms;synonyms/notation;structural signatures;dependency neighbors
STRONGEST_KNOWN_CHECK=PASS
STRONGER_SOURCE_RESULT_FOUND=true
SOURCE_INTERFACE=E-1e as audited through Stage21: M1(B)~3/(4*pi^2) B^2 log B
TARGET_CONSTANT_SEARCH=PASS
TARGET_INTERFACE=Stage15-2b / Stage18: M2(B)~C_M2 B(log B)^5, C_M2>0
TARGET_CONSTANT_EXPLICIT_NUMERIC=false
NEW_THEOREM_REQUIRED=false
```

The ratio law is therefore an exact synthesis of already-audited compatible interfaces rather than a new external counting theorem.

## 7. Exit

```text
UPSTREAM_PREMISE_CHECK=PASS
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
FALSE_SUBSET_INTERPRETATION_BLOCKED=true
FINITE_DATA_USED_AS_PROOF=false
DOUBLE_CHARGE_CHECK=PASS
NEXT_CHECKPOINT=40
NEXT_EXPECTED_COMMAND=Stage22-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
