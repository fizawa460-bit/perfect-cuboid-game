# Stage21-60 — causal decomposition of the Stage16 -> Stage17 interaction

EVIDENCE_LEVEL=PROVED
CHECKPOINT=60
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## 1. Audited transition theorem

Checkpoint30 proved the matched conditional survival law

\[
\frac{N_1(B)}{M_1(B)}\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

Stage16S supplies the intrinsic ambient space-diagonal baseline

\[
\frac{N_S^{all}(B)}{U(B)}\sim
\frac{9\zeta(3)}{8\pi G}\frac1B.
\]

Thus the polynomial space cost is the same `B^{-1}`, while exactly-one-face conditioning creates an additional positive logarithmic enhancement of exact order `(log B)^2`.

## 2. Structural source of the new Diophantine condition

For the unique integral face write

\[
x^2+y^2=P^2.
\]

The Stage17 space-diagonal condition is exactly

\[
P^2+z^2=d^2.
\]

Hence Stage16 -> Stage17 is a nested Pythagorean extension sharing the intermediate hypotenuse/leg `P`. This is not a heuristic model: it is the exact algebraic bridge used in Stage11, Stage13 and Stage17.

AR-038 freezes the corresponding exact raw representation convolution. If `H(P)` denotes positive unordered representations with `P` as a hypotenuse and `L_B(P)` representations with the same `P` as a leg extending to `d<=B`, then

\[
C_{raw}(B)=2\sum_{P\le B}H(P)L_B(P).
\]

After primitive/canonical projection,

\[
C_{prim}(B)=2N_1(B)+4N_{exact2}(B)+6N_3(B).
\]

This exact identity establishes that the target bulk is assembled from shared-`P` representation multiplicities; it is not a union of isolated one-parameter examples.

## 3. Stage13 bulk analytic mechanism

The audited Stage13 R07 proof resolves the nested Pythagorean system through the outer parametrization

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\qquad (r,s)=1.
\]

Its proof-facing Dirichlet architecture has five unbounded pole-producing pure channels

```text
H, R1, R2, S1, S2.
```

For every fixed finite inert-prime set `S`, the full principal sector is defined by all five induced pole-slot characters being principal. R07 proves:

1. the complete principal sector carries the full leading residue;
2. accepted fixed-`S` local conditions multiply that principal residue by the physical local average `prod_{p in S} lambda_p`;
3. every nonprincipal effective class loses at least one pole termwise;
4. a finite sum of such lower-pole terms cannot recreate the missing higher pole;
5. consequently nonprincipal sectors are `o_S(B(log B)^3)`.

Thus the Stage17 main term

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3
\]

is a **bulk principal-sector phenomenon** of the multiplicative shared-`P` parameter system. It is not produced by a finite exceptional residue class or by a thin explicit construction.

## 4. What is eliminated as the source of the enhancement

### 4.1 Canonical directional geometry is not the net log² source

Stage13's ordered-chamber Gelfand--Leray factors `I_q` produce real directional bias. But Stage21-30 proves that the same `I_q` occurs in source and target directional asymptotics and cancels:

\[
\frac{N_{1,q}(B)}{M_{1,q}(B)}\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}
\]

for all `q=ab,ac,bc`. Therefore canonical chamber bias affects directional constants but not the net Stage21 `(log B)^2` enhancement.

### 4.2 Exactly-one overlap subtraction is not the main source

Stage13 proves every pair overlap and the triple overlap are

\[
o(B(\log B)^3).
\]

Hence deleting multi-face objects does not create the target `B(log B)^3` main term or its two extra logarithms relative to the Stage16 source.

### 4.3 The known explicit survivor family is not the main source

Checkpoint50 repaired and proved for the entire AR-039 family

\[
N_{AR039}(B)=\Theta(B^{1/2})=o(N_1(B)).
\]

Thus AR-039 is genuinely negligible in the full Stage17 population and cannot explain the enhancement.

### 4.4 Cutoff, canonicalization and primitivity are not newly charged

The Stage16 and Stage17 populations use the same primitive canonical convention and the same physical cutoff, with `d=R` exactly on target objects. These are interface conditions, not new thinning/enhancement mechanisms.

## 5. Causal synthesis

The strongest rigorous Stage21 causal statement is therefore:

```text
POLYNOMIAL_LOSS=B^-1
POLYNOMIAL_LOSS_CAUSE=intrinsic space-diagonal quadratic/Pythagorean constraint
LOG_ENHANCEMENT=(log B)^2
LOG_ENHANCEMENT_LOCATION=bulk multiplicative shared-P nested-Pythagorean principal sector
SHARED_P_CONVOLUTION=EXACT_AR038
STAGE13_PRINCIPAL_SECTOR_DOMINATES=true
NONPRINCIPAL_SECTORS_LOWER_ORDER=true
CANONICAL_DIRECTIONAL_GEOMETRY_IS_NET_LOG_SOURCE=false
EXACTLY_ONE_OVERLAP_IS_MAIN_LOG_SOURCE=false
AR039_IS_MAIN_LOG_SOURCE=false
CUTOFF_OR_MULTIPLICITY_ARTIFACT=false
DOUBLE_CHARGE_CHECK=PASS
```

In words: imposing an integral space diagonal costs one intrinsic polynomial dimension, but inside the already-one-face population the shared intermediate diagonal has sufficiently rich multiplicative representation structure that the surviving bulk receives a logarithmic compensation of order `(log B)^2` relative to the ambient intrinsic baseline.

This is a theorem-level causal localization. It is stronger than merely observing the quotient and stronger than attributing the effect to a special family.

## 6. Remaining fine-mechanism open gate

The repository still does **not** contain an audited canonical decomposition of the two extra logarithms into two individually named local factors or a proof of a statement such as

```text
first extra log = pole slot X
second extra log = pole slot Y
```

The R07 proof has five principal pole-producing channels and a coupled curved-region summation. Although this architecture produces the full `B(log B)^3` main term and rigorously localizes the enhancement to the principal multiplicative bulk, no frozen theorem uniquely assigns the net two-log difference against the Stage16 `B^2 log B` law to two independent channels.

Therefore that finer decomposition remains open:

```text
OPEN_GATE=LOG_SQUARED_FINE_POLE_OR_LOCAL_FACTOR_DECOMPOSITION_UNRESOLVED
INDEPENDENT_LOG_FACTOR_CLAIM=false
LOCAL_PROBABILITY_PRODUCT_CLAIM=false
FIVE_POLE_SLOTS_TO_TWO_NET_LOGS_CANONICAL_MAP_PROVED=false
```

This open gate does not weaken the exact transition theorem or the causal localization above.

## 7. Evidence and provenance boundary

Reused theorem-level inputs:

- Stage21-30 audited transition and Stage16S comparison;
- Stage21-40 mechanism boundary;
- Stage21-50 audited AR-039 exclusion;
- AR-038 exact shared-hypotenuse convolution from Stage11;
- Stage13 R07 fixed-twist/residue/pole-sector/curved-region proof, especially `13-13fr` and `13-13fs`;
- Stage13 overlap little-o theorem;
- Stage13/Stage21 directional `I_q` cancellation.

No finite fit is promoted. No new growing-modulus theorem, local independence assumption, or product of heuristic factors is used.

```text
UPSTREAM_PREMISE_CHECK=PASS
FINITE_DATA_USED_AS_PROOF=false
NEW_COMPUTATION_REQUIRED=false
NEW_RESEARCH_RESULT=bulk-principal-sector causal localization with competing mechanisms rigorously excluded
FINE_MECHANISM_OPEN=true
NEXT_CHECKPOINT=70
NEXT_EXPECTED_COMMAND=Stage21-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
