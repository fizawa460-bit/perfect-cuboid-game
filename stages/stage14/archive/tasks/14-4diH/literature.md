# Stage14-4diH literature / applicability matrix

Frozen source:

```text
SOURCE_SNAPSHOT_SHA=0a2d313b4bd1baf8fad29cda70cc0f8a44e1b153
TARGET_FILE=stages/stage14/14-4di/h-target.md
```

This file records theorem applicability only for that immutable receiver.

## Sources audited

1. Anji Dong, Nicolas Robles, Dirk Zeindler, **Bilinear forms with Kloosterman fractions and applications**, arXiv:2601.00292 (2026).
   - Main geometry: bilinear Kloosterman fractions with arbitrary coefficient sequences.
   - Frozen 4di mismatch: the physical phase has a fixed modulus `q` and a coupled physical product coefficient `P_-`; no exact denominator-varying bilinear-fraction reduction with all physical masks retained is present.
   - Verdict: direct transfer not certified.

2. Valentin Blomer, Alexandru Pascadi, **Bilinear forms with Kloosterman sums via quadratic characters**, arXiv:2607.24311 (2026).
   - Theorem 1.1 gives strong bilinear bounds for complete Kloosterman sums for arbitrary moduli and a fixed-power saving in the critical square-root range.
   - Frozen 4di mismatch: no legal completion/decoupling has converted the physical incomplete phase and its three-weight packet into an independent-coefficient complete Kloosterman bilinear form.
   - Even a successful oscillatory transfer would not remove the principal term.
   - Verdict: direct whole-family transfer not certified.

3. Djordje Milićević, Xinhua Qin, Xiaosheng Wu, **Bilinear forms with Kloosterman sums and moments of twisted L-functions**, arXiv:2511.07550 (2025).
   - General power-saving bilinear estimates modulo arbitrary moduli.
   - Frozen 4di mismatch: no theorem-ready complete-sum coefficient geometry has been derived, and the theorem does not by itself control the positive physical principal density.
   - Verdict: direct transfer not certified.

4. Bryce Kerr, Igor E. Shparlinski, Xiaosheng Wu, Ping Xi, **Bounds on bilinear forms with Kloosterman sums**, arXiv:2204.05038 (2022).
   - Type-II and incomplete Kloosterman bilinear technology.
   - Frozen 4di mismatch: the physical modulus/root/product/factorization coupling is not reduced to the theorem's bilinear coefficient packet with all masks retained; the principal term is outside the oscillatory bound.
   - Verdict: direct whole-family transfer not certified.

5. Thomas Wright, **Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions**, arXiv:2604.25177 (2026).
   - Partially fixed-modulus trilinear Kloosterman fraction technology and dispersion applications. The distribution application requires suitable equidistribution of one coefficient sequence in small moduli.
   - Frozen 4di mismatch: no such small-modulus equidistribution theorem is available for the balanced squarefree/reciprocal/X15 physical coefficient sequence, and the full conductor is itself coupled to the physical packet.
   - Verdict: direct transfer not certified.

## Cross-cutting theorem boundary

The frozen target is not merely

```text
bound a centered oscillatory sum.
```

It asks for a bound on the full positive physical saturation count. The exact decomposition still contains

```text
principal zero mode,
three X15 pairwise covariance terms,
one X15 triple covariance term.
```

None of the audited theorems supplies, for the frozen coefficient packet,

```text
PRINCIPAL_DENSITY_FIXED_POWER_LOSS,
MAIN_TERM_SCALE_SIGNED_ANTICORRELATION,
or FULL_THREE_WEIGHT_COVARIANCE_CONTROL.
```

Hence no current off-the-shelf theorem is directly sufficient for the requested whole-family power saving.

```text
OFF_THE_SHELF_THEOREM_APPLICABLE=false
OSCILLATORY_ERROR_POWER_SAVING_CERTIFIED=false
PRINCIPAL_DENSITY_FIXED_POWER_LOSS_CERTIFIED=false
MAIN_TERM_SCALE_SIGNED_ANTICORRELATION_CERTIFIED=false
X15_ALL_COVARIANCE_TERMS_CONTROLLED=false
FIXED_POWER_SAVING_PROVED=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
```