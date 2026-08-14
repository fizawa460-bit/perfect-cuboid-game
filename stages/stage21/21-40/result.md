# Stage21-40 — sharp upper-bound ledger and mechanism boundary

EVIDENCE_LEVEL=PROVED
CHECKPOINT=40
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## Sharp transition upper bound

Checkpoint30 proved the full asymptotic

\[
\frac{N_1(B)}{M_1(B)}\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

Therefore the strongest certified upper bound is already sharp at the same scale:

\[
\boxed{\frac{N_1(B)}{M_1(B)}\ll \frac{(\log B)^2}{B}},
\]

and in fact for every fixed chamber `q in {ab,ac,bc}`,

\[
\boxed{\frac{N_{1,q}(B)}{M_{1,q}(B)}\ll \frac{(\log B)^2}{B}}.
\]

No strictly smaller polynomial or logarithmic order can hold for these matched populations because checkpoint30 supplies a positive leading asymptotic constant.

## What pays for the bound

The matched source and target laws are

\[
M_1(B)\sim C_M B^2\log B,\qquad C_M=\frac{3}{4\pi^2},
\]

\[
N_1(B)\sim C_N B(\log B)^3,\qquad C_N=\frac{\kappa}{24\pi}.
\]

Thus the net cost decomposes at the level of proved exponents as

```text
POLYNOMIAL_LOSS = B^-1
LOGARITHMIC_GAIN = (log B)^2
```

The polynomial loss is consistent with Stage16S: imposing `a^2+b^2+c^2=d^2` on the ambient three-dimensional lattice population also costs one power of `B`.

The additional `(log B)^2` factor is therefore not the polynomial codimension cost itself. It is an arithmetic enhancement specific to conditioning on the exactly-one-face population.

## Structural mechanism currently certified

On the unique integral face, write

\[
x^2+y^2=p^2.
\]

The target adds exactly the second Pythagorean extension

\[
p^2+z^2=d^2.
\]

Hence the rigorous structural statement is:

```text
SOURCE_STRUCTURE = one primitive/canonical Pythagorean face plus free complementary edge
TARGET_STRUCTURE = nested/shared-hypotenuse Pythagorean extension p^2+z^2=d^2
AMBIENT_SPACE_CONDITION = primitive Pythagorean quadruple locus
```

The repo-wide structural search through Stage13/Stage17/Euler-side assets did not reveal an already-audited theorem that isolates the `(log B)^2` enhancement into a separate local-density, squareclass, valuation, or Euler-product factor. Existing theorems certify the total asymptotic, but not a unique finer causal factorization of the two logarithms.

Therefore checkpoint40 records the mechanism boundary rather than inventing a decomposition:

```text
SHARP_UPPER_SCALE=(log B)^2/B
SHARPNESS_PROVED=true
POLYNOMIAL_COST_MECHANISM=SPACE_QUADRATIC_CONSTRAINT / ONE_DIMENSION_LOSS
LOG_ENHANCEMENT_MECHANISM=ARITHMETICALLY_PRESENT_BUT_NOT_YET_FACTORIZED
LOCAL_FACTOR_PRODUCT_PROVED=false
SQUARECLASS_EXPLANATION_PROVED=false
VALUATION_EXPLANATION_PROVED=false
UNIQUE_CAUSAL_DECOMPOSITION_PROVED=false
OPEN_GATE=LOG_SQUARED_ENHANCEMENT_MECHANISM_UNRESOLVED
```

## Exploration consequence

Checkpoint40 does not weaken the Stage21 program. It identifies exactly what remains to investigate at checkpoints50-60: whether a constructive subfamily, local/squareclass analysis, or comparison with the Stage13 counting architecture can explain the two extra logarithms without double charging the already-certified `B^-1` space-diagonal cost.

No finite data are used as proof and no perfect-cuboid endpoint is invoked.

```text
UPSTREAM_PREMISE_CHECK=PASS
FINITE_DATA_USED_AS_PROOF=false
DOUBLE_CHARGE_CHECK=PASS
NEW_RESEARCH_JUSTIFIED=true
NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage21-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
