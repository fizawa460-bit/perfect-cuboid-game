# Stage14-4ghH primary-source applicability matrix

Frozen source:

```text
SOURCE_SNAPSHOT_SHA=79393f83b1110b7e66b41a23c51596a10bc6c7ef
TARGET_FILE=stages/stage14/14-4gh/h-target.md
SEARCH_DATE=2026-08-12
```

Only primary papers and preprints are used.  The exact frozen weight is the
nested quadratic divisor-root sum derived in `result.md`, not a generic divisor
function.

## Sources checked

1. Lasse Grimmelt and Jori Merikoski, *The divisor function along arithmetic
   progressions and binary cubic polynomials*, arXiv:2508.17979 (2025).
   - Covers ordinary divisor equidistribution for moduli with two small factors,
     with an almost-all moduli application and a binary-cubic application.
   - Does not state an every-principal-cell theorem for two divisors of `uv`, a
     divisor of their product, and two moving quadratic root congruences.
   - Verdict: near input only; direct transfer not certified.

2. A. J. Irving, *The divisor function in arithmetic progressions to smooth
   moduli*, arXiv:1403.8031 (2014).
   - Covers one ordinary divisor function in one progression with suitable
     modulus factorisation.
   - The exact Stage14 weight is not reduced to this geometry.
   - Verdict: direct transfer not certified.

3. David T. Nguyen, *Generalized divisor functions in arithmetic progressions:
   I*, arXiv:2308.06839 (2023), and *II*, arXiv:2302.12815 (2023).
   - Part I uses constrained/averaged moduli; Part II treats a modified shifted
     convolution second moment.
   - Neither statement supplies the frozen uniform nested first moment.  The
     merged pointwise multiplicity bound also makes a second moment unnecessary
     for support transfer.
   - Verdict: architecture only; direct transfer not certified.

4. Mingxuan Zhong and Tianping Zhang, *A new result on the divisor problem in
   arithmetic progressions modulo a prime power*, arXiv:2505.10341 (2025).
   - Gives an ordinary-divisor asymptotic for prime-power moduli.
   - The Stage14 modulus is not restricted to a prime power and the nested
     quadratic divisor-root coupling is absent.
   - Verdict: direct transfer not certified.

5. Christopher Frei and Efthymios Sofos, *Generalised divisor sums of binary
   forms over number fields*, arXiv:1609.04002 (2016).
   - Gives asymptotics/lower bounds for specified generalized divisor-sum
     weights over binary-form values.
   - No exact identity places the Stage14 nested CRT weight in the covered class.
   - Verdict: structural lead only; direct transfer not certified.

6. Sandro Bettin, *Linear correlations of the divisor function*,
   arXiv:1701.06608 (2017).
   - Treats divisor products constrained by a fixed nontrivial linear equation.
   - The Stage14 active relation is nested multiplicative/quadratic, not a fixed
     linear correlation.
   - Verdict: structural comparator only; direct transfer not certified.

7. Kevin Ford, *The distribution of integers with a divisor in a given
   interval*, arXiv:math/0401223 (2004).
   - Supplies a genuine single-divisor support theorem.
   - It does not retain the two divisor layers or the simultaneous root CRT.
   - Verdict: support template only; direct transfer not certified.

## Applicability boundary

```text
DIRECT_FULL_TARGET_THEOREM_COUNT=0
OFF_THE_SHELF_THEOREM_APPLICABLE=false
DIRECT_TRANSFER_PROVED=false
EVERY_PRINCIPAL_CELL_UNIFORMITY_SUPPLIED=false
EXACT_TWO_CRT_CONGRUENCES_RETAINED_IN_ANY_CANDIDATE=false
FIRST_MOMENT_FULL_EXPONENT_PROVED=false
FIRST_MOMENT_FIXED_POWER_DEFICIT_PROVED=false
PARAMETER_DICHOTOMY_PROVED=false
```
