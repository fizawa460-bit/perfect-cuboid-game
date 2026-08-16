# Stage27-20 — finite diagnostics for the true N2 exponent attack

```text
TASK_ID=Stage27-20
CHECKPOINT=20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=DERIVED_EXACT_FINITE
```

Stage27 keeps the exact Stage18->Stage19 population contract from checkpoint10: primitive canonical exactly-two-face cuboids, target additionally requiring integral space diagonal, with the same Euclidean cutoff `R<=B`.

## Exact finite sources

The exact Stage19/Stage15 matched census supplies

`(B,N2)=(1000,2),(2000,5),(5000,15),(10000,25),(20000,42),(50000,62),(100000,89)`.

The later Stage24 numerical lane is an exact same-population ladder and supplies

`(200000,116),(500000,188),(1000000,255)`.

The frozen Stage19 numerical observatory additionally certifies

`N2(500000000)=3495`, with directional endpoint `(N2,a,N2,b,N2,c)=(1374,1371,750)`.

No interpolation is inserted between one million and five hundred million.

## Derived diagnostics

For two sampled cutoffs `B1<B2`, define the finite effective exponent

\[
\alpha_{\rm eff}(B_1,B_2)=\frac{\log(N_2(B_2)/N_2(B_1))}{\log(B_2/B_1)}.
\]

The broad-window value from `1,000,000` to `500,000,000` is

\[
\boxed{\alpha_{\rm eff}=0.421237360\ldots}.
\]

At the same endpoints,

\[
N_2(B)/\sqrt B: 0.255000000\to0.156301152,
\]
while

\[
N_2(B)/B^{1/4}: 8.063808033\to23.372473659.
\]

Thus the available finite window is compatible with growth strictly between the currently proved quarter-power lower and half-power upper. It does not identify an asymptotic exponent.

Directionally, comparing the exact one-million vector `(98,101,56)` with the exact 500-million vector `(1374,1371,750)` gives broad-window effective exponents approximately

```text
a: 0.424888256
b: 0.419684576
c: 0.417519733
```

These three values are close on this finite window, but no common directional exponent or limiting directional proportion is claimed.

## Research consequence

The finite evidence raises the priority of the strict sub-square-root upper lane: the half-power normalization decreases substantially over the largest validated window. The lower-family lane remains equally open because the quarter-power normalization grows strongly. Neither observation is theorem evidence.

Checkpoint30 may use this panel only as a hypothesis-selection aid. Checkpoints40/50 must obtain new proof input before changing any exponent.

```text
EXACT_FINITE_PANEL_MATERIALIZED=true
BROAD_WINDOW_ALPHA_EFF_1M_TO_500M=0.421237360
SQRT_NORMALIZATION_1M=0.255000000
SQRT_NORMALIZATION_500M=0.156301152
QUARTER_NORMALIZATION_1M=8.063808033
QUARTER_NORMALIZATION_500M=23.372473659
DIRECTIONAL_ALPHA_EFF_A=0.424888256
DIRECTIONAL_ALPHA_EFF_B=0.419684576
DIRECTIONAL_ALPHA_EFF_C=0.417519733
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
TRUE_N2_EXPONENT_IDENTIFIED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=30
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage27-audit
```
