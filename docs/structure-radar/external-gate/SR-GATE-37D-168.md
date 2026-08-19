# StructureRadar parallel batch 37D — SR-STR-168 Möbius square-function envelope

BATCH_ID=SR-BATCH-PARALLEL-37D-168-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=D
STRUCTURE=SR-STR-168
MODE=ONE_PR_FOUR_LANES_DEEP_ATTACK
BASE_MAIN=9f70ff9c37c12981e197f0c213795fc7a906fc35
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 36D. The primitive physical representation weight has the exact internal Möbius expansion

```text
R_phys(n;P)=sum_{r^2|n} mu(r) R_{P,r}(n/r^2),
```

with the rescaled mask kept as `M_P(rz')`. The audit correctly forbids replacing the full common-quotient sum by a globally `B^o(1)`-sized family of frozen Möbius layers.

## 1. Global layer freezing is not needed for an upper bound

For each fixed positive `n`, Cauchy on the actual square-divisor layers gives

```text
|R_phys(n;P)|
 <= (# {r:r^2|n})^(1/2)
    (sum_{r^2|n} |R_{P,r}(n/r^2)|^2)^(1/2).
```

Since the pointwise layer count is at most `tau(n)=B^o(1)` on the current polynomial-height range, define the exact physical square function

```text
S_P(n)
 = (sum_{r^2|n} |R_{P,r}(n/r^2)|^2)^(1/2).
```

Then pointwise

```text
|R_phys(n;P)| <= B^o(1) S_P(n).
```

Applying this separately to `n=a m` and `n=b m`, and using the nonnegative common-quotient packet weight `w(m)`, gives the same-measure domination

```text
sum_m w(m) |R_phys(a m;P1) R_phys(b m;P2)|
 <= B^o(1) sum_m w(m) S_{P1}(a m) S_{P2}(b m).
```

All Möbius layers remain internal to the square functions. No globally frozen `(r1,r2)` family is created, and no cancellation in the Möbius signs is charged.

## 2. Smaller sufficient receiver

The previous exact layered twisted-divisor adapter remains one possible route, but it is stronger than necessary for an upper bound. It is enough to prove a fixed-power deficit directly for the physical square-function correlation, or to map that square-function receiver into a twisted-divisor/spectral theorem.

Thus the live sufficient target is

```text
FIRST_MISSING_LEMMA=SameMeasurePhysicalGaussianMobiusSquareFunctionCorrelationDeficit
```

A sufficient form is: uniformly in the retained coprime parameters `(a,b)` and physical packets, prove

```text
sum_m w(m) S_{P1}(a m) S_{P2}(b m)
 <= B^{-delta+o(1)} H_packet
```

for one fixed `delta>0`, preserving the common quotient, orientation/range/charged-once masks inside every `R_{P,r}`, and the original quantifier order. Alternatively, an exact same-measure adapter from these square functions to mod-4 twisted-divisor or spectral square functions is acceptable if coefficient energy is preserved.

The ambient identity `r_2=4(1*chi_4)` remains architecture only. Pointwise Gaussian multiplicity and pointwise Möbius-layer count remain `B^o(1)` facts only and are not charged as fixed-power density savings.

## 3. Firewalls

```text
PRIMITIVE_GCD_MOBIUS_PEEL_REUSED=true
GLOBAL_FROZEN_MOBIUS_LAYER_COUNT_SUBPOLYNOMIAL_PROVED=false
POINTWISE_MOBIUS_SQUARE_FUNCTION_DOMINATION=PROVED
RESCALED_PHYSICAL_MASK_RETAINED=true
MOBIUS_SIGN_CANCELLATION_CHARGED=false
AMBIENT_R2_REPLACEMENT_PROVED=false
PHYSICAL_SQUARE_FUNCTION_CORRELATION_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=SameMeasurePhysicalGaussianMobiusSquareFunctionCorrelationDeficit
SR_STR_168_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
