# Stage28-60-r3 — low-degree lattice receiver

```text
ROUTE=R23_LOW_DEGREE_LATTICE_RECEIVER
STATUS=RESEARCH_REQUEST_READY_FINITE_COMPUTATION_GATE
```

The fixed-curve spectrum comparison leaves one bounded repo-native finite question before no further Stage60 progress can reasonably be expected from low-degree geometry.

## Stage19 exact finite receiver

Use the Stage14-4ak Shimada embedding of the physical Kummer surface with fixed

```text
GramS0
M
physical deck involution delta
physical fiber/corner labels
AutX0f-equivalence
Galmu/Q-descent data
Wout0 chamber data
```

and enumerate irreducible rational root classes `C` satisfying

\[
C^2=-2,
\qquad 0<M\cdot C\le 6.
\]

The audited degree-four result must be reproduced as a regression:

```text
physical Q-rational classes with M.C=4 = 0.
```

The new output should classify `M.C=5` and `M.C=6` after effectivity, M-null-boundary removal, Q-descent, automorphism quotient and physical-open filtering.

## Stage20 comparison receiver

The target already has a degree-six rational witness from the generalized Saunderson map.  For an exact spectrum comparison, classify whether the Stage20 third-face K3 has physical rational curves of degree `<6` under its matched physical quasi-polarization, and count its degree-six classes up to the same physical-equivalence semantics.

## Why this is only an intermediate gate

If the source has an `M.C=5` rational curve, a single fixed curve can contribute at exponent `2/5`, larger than the Saunderson `1/3` exponent.  If degree five is absent and degree six is the next possible source degree, then the two fixed-curve spectra are tied at polynomial exponent `1/3` at worst.

Neither outcome determines the whole-population bridge.  Stage14-4al shows that the Stage19 count may be produced by a moving first-hit/rank-jump mechanism rather than a finite accumulating set.  Therefore a global complement bound is mandatory before fixed-curve spectra can be promoted to `J_28` or `M3/N2` asymptotics.

```text
FINITE_LATTICE_RECEIVER=PhysicalLowDegreeRootSpectrumM5M6
SOURCE_SURFACE=Stage19 space Kummer
TARGET_SURFACE=Stage20 third-face K3
HEIGHT=physical quasi-polarization under R<=B
SOURCE_M4_REGRESSION=EMPTY
TARGET_M6_WITNESS=SAUNDERSON
GLOBAL_COUNT_CONCLUSION_FROM_SPECTRUM_ALONE=FORBIDDEN
ENDPOINT_COUNT_FORBIDDEN=true
```