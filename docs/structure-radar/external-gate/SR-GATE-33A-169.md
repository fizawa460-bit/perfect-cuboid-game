# StructureRadar parallel batch 33A — SR-STR-169 quadratic-completion reduction

BATCH_ID=SR-BATCH-PARALLEL-33A-169-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=A
STRUCTURE=SR-STR-169
MODE=PARALLEL_DEEP_ATTACK
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from merged batch30 together with the selector/q17 normalizations in merged batches31-32. Batch30 reduced the Stage27-20 receiver to the exact nonzero-frequency two-copy covariance in `H_phys^MAIN`; the remaining generic wording was `MAINWallPhysicalCenteredFrequencyToKloostermanFractionTransfer`.

The present lane proves the algebraic quadratic-completion kernel that sits inside that transfer and isolates a smaller physical Fourier-norm bridge.

## 1. Exact Fourier completion of the physical f-weight

Fix one retained MAIN packet after the merged CRT normalization, with modulus

```text
q = 2UV/gcd(U,V)
```

and congruence phase

```text
f^2 - C = 0 (mod q),
C = G_- + lambda_h N.
```

Let `W(f)` denote the exact remaining physical coefficient on residues `f mod q` after all other frozen packet data have been retained. Define the finite Fourier transform

```text
W_hat(b) = sum_{f mod q} W(f) e_q(-bf).
```

Fourier inversion gives the exact identity, for every `a mod q`,

```text
sum_{f mod q} W(f) e_q(a f^2)
 = (1/q) sum_{b mod q} W_hat(b) G_q(a,b),

G_q(a,b) = sum_{r mod q} e_q(a r^2 + b r).
```

No estimate or change of measure has occurred here.

## 2. The inverse-frequency phase is already present in the complete Gauss kernel

On the odd part of `q`, whenever `(2a,q)=1`, completing the square gives

```text
G_q(a,b)
 = G_q(a,0) e_q(-b^2 * inverse(4a) mod q).
```

Thus the complete quadratic kernel produces an inverse-`a` phase exactly. This is the projective/Kloosterman-fraction geometry that batch30 was trying to reach.

For general composite/even `q`, Chinese remainder factorization separates the odd and 2-primary local Gauss factors. Non-coprime `(a,q)>1` strata are not discarded; they must be retained and controlled separately. The present reduction therefore proves only the algebraic emergence of inverse-frequency geometry, not a power saving.

## 3. What is still missing

The obstruction is no longer the existence of a formal transform from `f^2` to inverse fractions. That transform is exact after finite Fourier completion. The genuinely physical issue is whether the exact MAIN coefficient can be completed with acceptable Fourier energy and whether the bad-gcd/even local strata can be summed without losing the fixed power.

The smaller missing lemma is

```text
FIRST_MISSING_LEMMA=MAINWallPhysicalResidueFourierCompletionNormAndBadGCDControl
```

A sufficient form is:

> On every retained Stage27 MAIN wall block, for the exact residue coefficient `W(f)` arising from the centered/two-copy `H_phys^MAIN` survivor weight, prove an `L1/L2` Fourier bound strong enough that the completed Gauss kernels may be decomposed into `B^o(1)` inverse-frequency bilinear/trilinear pieces, while preserving all physical masks, correlated `q=2UV/gcd(U,V)`, nested common-parent weights, quantifier order, and one uniform positive power. Control the 2-primary and `(a,q)>1` strata in the same measure rather than deleting them.

Once this is available, Dong--Robles--Zeindler remains the first published bilinear Kloosterman-fraction theorem to test on the coprime odd pieces. Wright remains secondary if an actual modulus average and the required coefficient factorization emerge. No applicability claim is made before this physical Fourier bridge is proved.

## 4. Relation to batches31-32

Merged batch31 says the full physical selector need not admit a global Hecke factorization; it should first be transported into canonical charged-once correlation branches. Merged batch32 similarly isolates the q17 branch as a nonnegative witness-incidence component. Those transports remain separate prerequisites where they are used.

The present lane concerns the analytic quadratic kernel after a MAIN-native branch has been exposed. It does not bypass `SR-STR-167` or `SR-STR-174`, and their hypothetical savings are not multiplied with this lane.

## 5. Verdict / firewalls

```text
QUADRATIC_RESIDUE_FOURIER_COMPLETION_IDENTITY=PROVED
COPRIME_ODD_GAUSS_INVERSE_FREQUENCY_PHASE=PROVED
FULL_MAIN_PHYSICAL_FOURIER_NORM_CONTROL_PROVED=false
BAD_GCD_AND_TWO_PRIMARY_MAIN_CONTROL_PROVED=false
DIRECT_KLOOSTERMAN_THEOREM_APPLICABILITY_PROVED=false
FIRST_MISSING_LEMMA=MAINWallPhysicalResidueFourierCompletionNormAndBadGCDControl
SR_STR_169_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
