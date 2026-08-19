# StructureRadar parallel batch 36A — SR-STR-169 TT* Gram reduction

BATCH_ID=SR-BATCH-PARALLEL-36A-169-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=A
STRUCTURE=SR-STR-169
MODE=PARALLEL_DEEP_ATTACK
BASE_MAIN=8e7dd3e8410aad9d33734de2598bae25630901ce
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 35A. There the remaining task was reduced to a same-`H_phys^MAIN` operator-norm deficit for the primitive completed inverse-frequency family, with the original batch34 Fourier `L2` energy retained and the gcd-descent factor kept inside the kernel.

## 1. Exact TT* reduction

For one retained gcd stratum `d`, write the completed operator as

```text
(T_d c)(x) = sum_{b:d|b} K_d(x,b)c_b,
```

where `x` denotes the exact remaining MAIN physical variables and the `L2` norm in `x` is taken against the original charged `H_phys^MAIN` packet measure. Define the Gram kernel

```text
G_d(b,b') = <K_d(.,b), K_d(.,b')>_{H_phys^MAIN}.
```

Then, exactly,

```text
||T_d||_{2->2}^2 = ||T_d^* T_d||_{2->2},
(T_d^*T_d)(b,b') = G_d(b,b').
```

No new Fourier normalization is introduced. The coefficient vector remains the original restricted `c_b=W_hat(b)/q` from batch34/35A.

For the finite Hermitian Gram matrix, Schur gives the sufficient bound

```text
||T_d||_{2->2}^2
 <= sup_b sum_{b':d|b'} |G_d(b,b')|.
```

Thus a published operator theorem is not logically required as a black box. It is enough to prove a fixed-power deficit for the exact same-measure two-copy Gram correlations.

## 2. Diagonal/off-diagonal split

The row sum decomposes exactly as

```text
G_d(b,b) + sum_{b'!=b, d|b'} |G_d(b,b')|.
```

The diagonal is the same-packet kernel energy and the off-diagonal term is a genuine two-frequency physical correlation. No cancellation between the two is assumed. A successful closure must bound both at the required scale, or show that the diagonal is already below the target envelope and place the fixed-power work entirely in the off-diagonal branch.

This converts the abstract operator adapter into a scalar/two-copy correlation target on the original MAIN measure.

## 3. New restart point

```text
FIRST_MISSING_LEMMA=MAINWallPrimitiveInverseFrequencyTTStarGramRowDeficit
```

A sufficient form is:

> Uniformly over all retained MAIN wall packets and gcd strata, prove
> `sup_b sum_{b':d|b'} |G_d(b,b')| <= B^{-2delta+o(1)} E_packet`
> for one fixed `delta>0`, with `E_packet` normalized to the exact batch34/35A kernel-energy scale. Preserve the correlated modulus, common-parent weights, gcd-descent factor, primitive/chamber/parity masks, and quantifier order. Packet summation may lose only `B^o(1)`.

A Kuznetsov/large-sieve/Kloosterman-fraction theorem may discharge this after exact range matching, but theorem applicability is not claimed here.

## 4. Firewalls

```text
SAME_MEASURE_OPERATOR_REDUCTION_REUSED=true
TTSTAR_GRAM_REDUCTION=PROVED
FRESH_DESCENDED_PARSEVAL_IDENTITY_CLAIMED=false
GCD_DESCENT_FACTOR_RETAINED=true
GRAM_DIAGONAL_AUTOMATICALLY_SMALL=false
PUBLISHED_SPECTRAL_THEOREM_APPLICABILITY_PROVED=false
FIRST_MISSING_LEMMA=MAINWallPrimitiveInverseFrequencyTTStarGramRowDeficit
SR_STR_169_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```

WORK_DELEGATION_RECOMMENDED=true
WORK_TARGET=SR-STR-169 / MAINWallPrimitiveInverseFrequencyTTStarGramRowDeficit
