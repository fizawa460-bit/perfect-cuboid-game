# StructureRadar parallel batch 33D — SR-STR-168 common-norm-quotient reduction

BATCH_ID=SR-BATCH-PARALLEL-33D-168-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=D
STRUCTURE=SR-STR-168
MODE=PARALLEL_DEEP_ATTACK
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from Stage14 q12 and the normalized SR-STR-168 gate. The old obstruction was a same-measure weighted Gaussian norm-ratio collision

```text
x2 * N(z1) = x1 * N(z2)
```

with physical masks and a concern that no polynomial-length Gaussian modulus/sample family had been exposed for a large-sieve argument.

The present lane gives an exact arithmetic contraction of the collision equation before any large-sieve or pair-correlation input is considered.

## 1. Remove the common gcd of the scalar coordinates

Write

```text
g = gcd(x1,x2),
x1 = g a,
x2 = g b,
gcd(a,b)=1.
```

Then the collision equation is equivalent to

```text
b * N(z1) = a * N(z2).
```

Since `(a,b)=1`, Euclid's lemma gives

```text
a | N(z1),
b | N(z2).
```

Hence there is an integer `m>=0` such that

```text
N(z1) = a m,
N(z2) = b m.
```

Conversely any pair satisfying these two equations satisfies the original norm-ratio collision. Thus, after peeling `g`, the norm-ratio equation is exactly a common-norm-quotient incidence.

## 2. Collision energy becomes a common-quotient representation correlation

Ignoring no physical masks, one may regroup a weighted collision sum by `(g,a,b,m)`:

```text
sum_{g,a,b: (a,b)=1} sum_m
    W(g,a,b,m; physical data)
    R_phys(a m; packet_1)
    R_phys(b m; packet_2),
```

where `R_phys(n;packet)` denotes the number/weight of Gaussian representations of norm `n` surviving the exact frozen physical conditions in that copy.

This is only a change of variables. It does not assert factorization of `W`, independence of the two representation weights, or a power saving.

The standard pointwise representation bound `r_2(n) <= 4 tau(n)` shows that unconstrained representation multiplicity is `B^o(1)` on polynomial-size integers, but that controls only multiplicity at fixed `(a,b,m)`. It does not make the *support in m* fixed-power sparse and therefore cannot close the Stage27 receiver by itself.

## 3. Consequence for the old polynomial-family wording

A polynomial-length family of Gaussian moduli is not logically required merely to normalize the collision equation. The exact common quotient `m` is the natural averaging coordinate. A Gaussian large sieve may still become useful after the physical representation weights are separated, but the first missing issue is now same-measure correlation along this common quotient rather than the existence of a generic modulus family.

The smaller missing lemma is

```text
FIRST_MISSING_LEMMA=SameMeasurePhysicalCommonNormQuotientCorrelationDeficit
```

A sufficient form is:

> On every retained MAIN/Stage14 packet relevant to the norm-ratio branch, bound the off-diagonal common-quotient correlation in `m` with one uniform fixed positive power after peeling `g=gcd(x1,x2)`, while retaining primitive/gcd/range/orientation/charged-once masks and the actual coefficient energy. Any character or Gaussian-large-sieve separation must be proved from the exact physical weights rather than replacing them by an ambient representation function.

A weaker but still useful intermediate statement would show that all diagonal/proportional configurations in `(a,b,z1,z2)` contribute only the already-charged principal mass, leaving a genuinely oscillatory off-diagonal common-quotient sum.

## 4. Relation to SR-STR-169

The SR-STR-169 lane attacks a quadratic additive-frequency kernel in the Stage27 MAIN wall receiver. SR-STR-168 instead contracts the Gaussian norm-ratio collision branch. They may eventually meet after a selector decomposition, but no saving from one lane is multiplied into the other without an exact common-measure adapter.

## 5. Verdict / firewalls

```text
NORM_RATIO_TO_COMMON_NORM_QUOTIENT_REDUCTION=PROVED
COMMON_GCD_PEEL=PROVED
FIXED_COMMON_QUOTIENT_REPRESENTATION_MULTIPLICITY_SUBPOLYNOMIAL=true
COMMON_QUOTIENT_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
PHYSICAL_WEIGHT_FACTORISATION_PROVED=false
POLYNOMIAL_GAUSSIAN_MODULUS_FAMILY_REQUIRED_FOR_NORMALIZATION=false
FIRST_MISSING_LEMMA=SameMeasurePhysicalCommonNormQuotientCorrelationDeficit
SR_STR_168_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
