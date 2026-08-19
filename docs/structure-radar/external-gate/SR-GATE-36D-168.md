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

Define

```text
R_{P,r}(m) = sum_{N(z')=m} M_P(r z').
```

Then exactly

```text
R_phys(n;P) = sum_{r^2|n} mu(r) R_{P,r}(n/r^2).
```

No scale invariance of the physical mask is assumed: the mask is explicitly evaluated at `r z'`. Thus orientation/range/charged-once conditions are preserved rather than silently replaced by ambient `r_2`.

For each fixed `n`, the number of admissible square-divisor roots `r` is at most `tau(n)=B^o(1)` on the current polynomial-height range. This is a pointwise complexity statement only.

## 2. Consequence for the common-norm correlation

Applying the exact expansion to both `R_phys(a m;P_1)` and `R_phys(b m;P_2)` gives the exact Möbius-layered correlation

```text
sum_m w(m)
  sum_{r1^2|a m} sum_{r2^2|b m}
    mu(r1)mu(r2)
    R_{P1,r1}(a m/r1^2)
    R_{P2,r2}(b m/r2^2).
```

The common quotient, coprime `(a,b)` structure and all packet masks remain explicit.

Audit firewall: the pointwise bound `#{r:r^2|n}=B^o(1)` does **not** by itself imply that, after summing over all `m`, the expression is a fixed `B^o(1)`-sized collection of globally frozen `(r1,r2)` correlations. The set of possible Möbius layers across the full `m`-range may be much larger. Therefore the `r1,r2` sums must remain inside the same-measure correlation unless a separate weighted layer-aggregation lemma is proved.

The ambient twisted-divisor identity may be invoked only after an adapter handles these rescaled physical masks together with the Möbius-layer dependence. The primitive gcd condition is algebraically exposed, but its layer aggregation cannot be dropped for free.

## 3. Repaired restart point

```text
FIRST_MISSING_LEMMA=SameMeasurePhysicalMobiusLayeredOrientationRangeMaskedGaussianToTwistedDivisorAdapter
```

A sufficient form is:

> Starting from the exact Möbius-layered common-`m` correlation above, transform or estimate the rescaled-mask representation weights by mod-4 twisted-divisor or equivalent spectral terms while preserving the internal square-divisor layer sums, original physical energy, orientation/range/charged-once masks, coprime `(a,b)` structure and quantifier order. Any externalization of `(r1,r2)` must be justified by a same-measure weighted layer-aggregation bound with at most `B^o(1)` total loss.

No claim is made that the remaining masks admit such an expansion. The exact Möbius identity is retained as progress; only the unjustified global `B^o(1)` layer-count claim is removed.

## 4. Firewalls

```text
AMBIENT_R2_CHI4_ARCHITECTURE_REUSED=true
PRIMITIVE_GCD_MOBIUS_PEEL=PROVED
RESCALED_PHYSICAL_MASK_RETAINED=true
POINTWISE_PRIMITIVE_LAYER_MULTIPLICITY_SUBPOLYNOMIAL=PROVED
GLOBAL_FROZEN_MOBIUS_LAYER_COUNT_SUBPOLYNOMIAL_PROVED=false
PHYSICAL_MASK_SCALE_INVARIANCE_ASSUMED=false
PHYSICAL_MASKED_TO_TWISTED_DIVISOR_ADAPTER_PROVED=false
FIRST_MISSING_LEMMA=SameMeasurePhysicalMobiusLayeredOrientationRangeMaskedGaussianToTwistedDivisorAdapter
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
