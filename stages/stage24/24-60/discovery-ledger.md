# Stage24-60 — discovery ledger

CHECKPOINT=60
ROLE=CAUSAL_INTERACTION_DISCOVERY
SEARCH_STATUS=COMPLETE_FOR_CHECKPOINT60

## 1. Required policy gates

Checkpoint60 requires:

- intrinsic baseline comparison with Stage16S and Stage21;
- alternate-path comparison with Stage22 and Stage23;
- independence/correlation classification;
- explicit double-charge check;
- recognition that the Stage19 squareclass condition is genuinely new on Stage24;
- prohibition on attributing the inherited half-power rate to the local sieve without proof.

All six gates were executed.

## 2. Source clusters opened

| ID | Source | Role | Outcome |
|---|---|---|---|
| D60-01 | Stage16S final | ambient integral-space control | exact intrinsic space cost `~c/B` |
| D60-02 | Stage21 controller/final | exactly-one-face space interaction | positive `(log B)^2` enhancement over ambient baseline |
| D60-03 | Stage22 closeout | no-space second-face comparison | sharp `M2/M1 ~ const*(log B)^4/B` |
| D60-04 | Stage23-60 + post-Stage24-50 supersession | second face after space already paid | qualitative zero density; old odd/odd death narrowed; new `N2>>sqrt(log B)` inherited |
| D60-05 | Stage24-30 | Stage24 zero-density mechanisms | quotient upper, fixed-prime squareclass sieve, independent thin cover |
| D60-06 | Stage24-40 | half-power causal-boundary audit | local tensor not fixed-power capable; half-power mechanism remains unassigned |
| D60-07 | Stage24-50 | new lower theorem | infinite primitive Stage19 family and `N2>>sqrt(log B)` |

No finite numerical trend is used as theorem input.

## 3. New deductions at checkpoint60

### D60-N1 — Stage24 lower survivor-ratio bound

From

`N2(B)>>sqrt(log B)` and `M2(B)~C_M2 B(log B)^5`,

\[
N_2/M_2\gg B^{-1}(\log B)^{-9/2}.
\]

Together with the inherited upper this gives the first two-sided asymptotic-scale bracket for the literal Stage24 survivor ratio, though the powers do not match.

### D60-N2 — Stage23 lower comparison after supersession

From the same lower theorem and `N1(B)~cB(log B)^3`,

\[
N_2/N_1\gg B^{-1}(\log B)^{-5/2}.
\]

This updates the Stage23 comparison after its historical checkpoint60 closeout without revoking its audit.

### D60-N3 — ambient-relative Stage24 interaction bracket

For

\[
\mathcal J_2=(N_2/M_2)/(N_S^{all}/U),
\]

\[
(\log B)^{-9/2}\ll \mathcal J_2
\ll_\varepsilon B^{1/2+\varepsilon}(\log B)^{-5}.
\]

The bounds contain `1`, so the global interaction sign cannot currently be classified.

### D60-N4 — second-order cross-ratio bracket

Define

\[
\mathcal I
=(N_2/M_2)/(N_1/M_1)
=(N_2/N_1)/(M_2/M_1).
\]

Then

\[
(\log B)^{-13/2}\ll \mathcal I
\ll_\varepsilon B^{1/2+\varepsilon}(\log B)^{-7}.
\]

This is the natural algebraic face/space interaction observable across the four-count square. Its sign relative to `1` is unresolved.

### D60-N5 — thin but infinite

Checkpoint30 gives `N2/M2->0`; checkpoint50 gives `N2->infinity`. Hence the exact Stage24 target is now rigorously

```text
ZERO_DENSITY_AND_INFINITE
```

rather than merely nonempty finite evidence.

### D60-N6 — explicit arithmetic-stratum heterogeneity

The historical Stage15 algebraic formulas have:

- coprime odd/odd slice: identically zero space survivors by mod 16;
- mixed-parity `C17` slice: infinitely many space survivors.

Thus a natural two-face construction is not filtered uniformly by the space predicate. This does not settle the global interaction sign.

## 4. Independence/correlation classification

The exact conclusions are deliberately asymmetric:

```text
STAGE21_ONE_FACE_VS_SPACE=POSITIVE_LOGARITHMIC_INTERACTION_PROVED
STAGE24_TWO_FACE_VS_SPACE=GLOBAL_SIGN_UNRESOLVED
STAGE24_GLOBAL_RATIO_INDEPENDENCE_PROVED=false
STAGE24_GLOBAL_RATIO_INDEPENDENCE_DISPROVED=false
EXPLICIT_ARITHMETIC_STRATUM_HETEROGENEITY=PROVED
```

A structural dependence inside one explicit family is not promoted to a global stochastic correlation theorem.

## 5. Double-charge search

Potential illegal combinations were checked explicitly:

1. ambient `B^-1` baseline times inherited half-power saving;
2. Stage21 `(log B)^2` factor imported to the two-face host;
3. Stage23 charging space squareclass after space is already in the source;
4. Stage22/23 adjacent-stratum ratios narrated as conditional probabilities;
5. fixed-prime sieve saving multiplied onto Stage14 upper;
6. thin-cover zero-density saving multiplied with local sieve or half-power upper;
7. checkpoint50 lower family treated as bulk density.

All are rejected. The legal charge map is materialized in `double-charge-audit.md`.

## 6. Half-power attribution search

Checkpoint40 remains controlling:

- fixed `M.C=4` rational-curve square-root mechanism is eliminated;
- fixed-power occupancy-deficit strata are strict sub-square-root;
- the split-prime local tensor is logarithmic even under hypothetical polynomial windows;
- moving-family / first-small-point / transverse-incidence control remains open.

Therefore checkpoint60 does not assign the inherited `1/2` upper exponent to the squareclass condition, local sieve, thin cover, or any single causal factor.

## 7. Numerical reuse preflight

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,24-14num-r201,24-14num-r202
NUM_POPULATION_MATCH=EXACT
NUM_EVIDENCE_LEVEL=EXACT_FINITE_ORACLE_PLUS_AUDITED_THEOREM_INTERFACES
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED_AT_CAUSAL_SYNTHESIS
```

Finite counts remain regression/diagnostic evidence only.

## 8. Exit

```text
DISCOVERY_CHECKPOINT=60
SOURCE_CLUSTERS_OPENED=7
NEW_DEDUCTIONS=6
INTRINSIC_BASELINE_COMPARISON=COMPLETE
ALTERNATE_PATH_COMPARISON=COMPLETE
INDEPENDENCE_CORRELATION_CLASSIFICATION=COMPLETE_WITH_GLOBAL_SIGN_OPEN
DOUBLE_CHARGE_CHECK=PASS
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage24-audit
```
