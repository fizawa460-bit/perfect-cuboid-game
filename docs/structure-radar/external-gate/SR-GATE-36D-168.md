# StructureRadar parallel batch 36D — SR-STR-168 primitive-mask Möbius peel

BATCH_ID=SR-BATCH-PARALLEL-36D-168-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=D
STRUCTURE=SR-STR-168
MODE=PARALLEL_DEEP_ATTACK
BASE_MAIN=8e7dd3e8410aad9d33734de2598bae25630901ce
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 35D. There the ambient identity `r_2=4(1*chi_4)` was retained only as architecture because the true object is the restricted physical representation weight `R_phys`, carrying primitive/orientation/range/charged-once masks.

## 1. Primitivity can be peeled exactly without replacing the physical mask

Write a physical representation as `z=x+iy`, `N(z)=n`, and let `M_P(z)` denote all retained non-primitivity masks for packet `P` (orientation, chamber/range, charged-once data, and any other representation-level physical condition). Then

```text
1_{gcd(x,y)=1} = sum_{r|x, r|y} mu(r).
```

Hence the exact primitive physical representation weight satisfies

```text
R_phys(n;P)
 = sum_{r^2|n} mu(r)
     sum_{N(z')=n/r^2} M_P(r z').
```

Define the rescaled-mask ambient representation weight

```text
R_{P,r}(m) = sum_{N(z')=m} M_P(r z').
```

Then exactly

```text
R_phys(n;P) = sum_{r^2|n} mu(r) R_{P,r}(n/r^2).
```

No invariance of the physical mask under scaling is assumed: the mask is explicitly evaluated at `r z'`. Thus orientation/range/charged-once conditions are preserved rather than silently replaced by ambient `r_2`.

The number of square-divisor roots `r` is at most `tau(n)=B^o(1)` on the current polynomial-height range. Therefore primitive Möbius peeling itself introduces only subpolynomial complexity and is not a separate fixed-power obstruction.

## 2. Consequence for the common-norm correlation

Applying the exact expansion to both `R_phys(a m;P_1)` and `R_phys(b m;P_2)` expresses the physical common-`m` correlation as a `B^o(1)`-complexity signed combination of correlations of rescaled-mask representation weights `R_{P_1,r_1}` and `R_{P_2,r_2}`. The common quotient, coprime `(a,b)` structure and all packet masks remain explicit.

The ambient twisted-divisor identity may be invoked only after an adapter handles these rescaled physical masks. The primitive gcd condition itself no longer needs to be bundled into that adapter.

## 3. New restart point

```text
FIRST_MISSING_LEMMA=SameMeasurePhysicalOrientationRangeMaskedGaussianToTwistedDivisorConvolutionAdapter
```

A sufficient form is:

> Uniformly over the `B^o(1)` Möbius square-divisor layers and retained coprime `(a,b)` packets, express the exact rescaled-mask representation correlations `R_{P_1,r_1}(a m/r_1^2) R_{P_2,r_2}(b m/r_2^2)` (with the divisibility layers written in their exact integral form) as a `B^o(1)`-complexity combination of mod-4 twisted-divisor or equivalent spectral terms, with coefficient norms controlled by the original physical energy and all orientation/range/charged-once masks and quantifier order preserved.

No claim is made that the remaining masks admit such an expansion. The reduction only removes primitivity as a separate algebraic obstruction.

## 4. Firewalls

```text
AMBIENT_R2_CHI4_ARCHITECTURE_REUSED=true
PRIMITIVE_GCD_MOBIUS_PEEL=PROVED
RESCALED_PHYSICAL_MASK_RETAINED=true
PRIMITIVITY_COMPLEXITY_SUBPOLYNOMIAL=PROVED
PHYSICAL_MASK_SCALE_INVARIANCE_ASSUMED=false
PHYSICAL_MASKED_TO_TWISTED_DIVISOR_ADAPTER_PROVED=false
FIRST_MISSING_LEMMA=SameMeasurePhysicalOrientationRangeMaskedGaussianToTwistedDivisorConvolutionAdapter
SR_STR_168_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
