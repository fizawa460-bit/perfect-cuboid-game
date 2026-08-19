# StructureRadar parallel batch 33B — SR-STR-170 squareclass divisor-window reduction

BATCH_ID=SR-BATCH-PARALLEL-33B-170-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=B
STRUCTURE=SR-STR-170
MODE=PARALLEL_DEEP_ATTACK
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from the merged Stage14 q14 reciprocal-divisor-window radar and the normalized SR-STR-170 gate. The old wording asked for a transfer from ordinary divisor-window results to the reciprocal squareclass divisor window with all physical masks retained.

The present lane separates the deterministic squareclass algebra from the genuinely analytic physical-measure transfer.

## 1. Exact squareclass parameterization

On the Stage14 heavy reciprocal packet the admissible divisor has the recorded form

```text
L = J a^2
```

with the squareclass `J` frozen on the packet. Equivalently, for squarefree `J`,

```text
sqf(L)=J.
```

If `L | M`, then necessarily `J | M` and

```text
a^2 | M/J.
```

Conversely, whenever `a^2 | M/J`, the divisor `L=J a^2` divides `M` and has the required squareclass. Thus squareclass-divisor existence is exactly square-divisor existence in the quotient `M/J`; no probabilistic transfer is needed for this algebraic step.

## 2. Reciprocal windows become square-divisor windows

If the physical reciprocal window is

```text
L_- <= L <= L_+,
```

then the parameter `a` lies in the exact interval

```text
sqrt(L_-/J) <= a <= sqrt(L_+/J).
```

Its multiplicative width is the square root of the original `L`-window width. The complementary cofactor is still

```text
E = M/L = M/(J a^2),
```

so the canonical/reverse masks attached to `E` remain part of the charged physical packet and are not discarded by this reparameterization.

Hence the live arithmetic object is not a generic ordinary divisor in a short interval. It is a square divisor `a^2 | M/J` in a corresponding square-root interval, coupled to the exact complementary physical cofactor.

## 3. Ordinary-divisor shadow: one-sided inclusion only

There is an exact set inclusion

```text
{exists admissible squareclass divisor L in the physical window}
  subseteq
{exists ordinary divisor d of M in the same L-window}.
```

Therefore any *upper* bound for ordinary-divisor-window support that is already stated in the same underlying `M`-measure and at the actual physical window width automatically upper-bounds the squareclass support with distortion 1.

What does not follow is a relative-density equivalence, lower bound, or transfer of an ordinary-divisor theorem whose averaging measure/window hypotheses differ from the frozen physical packet. In particular the squareclass/canonical cofactor masks cannot be removed merely because ordinary divisor support is larger.

## 4. Smaller missing lemma

The old `Q14_FORD_SQUARECLASS_WINDOW_TRANSFER_TEST` bundled two issues: squareclass algebra and physical theorem compatibility. The first issue is now discharged exactly. The remaining bridge is

```text
FIRST_MISSING_LEMMA=PhysicalSquareDivisorWindowOrdinaryShadowMeasureCompatibility
```

A sufficient form is:

> On every retained fixed-E / fixed-ray Stage14 packet feeding the Stage27-19 boundary receiver, place the actual radial integer `M` and its physical reciprocal window inside a published ordinary-divisor-window upper-support theorem with a fixed-power relative deficit, without changing the charged physical measure. Verify the theorem at the actual window width after the `L=J a^2` square-root reparameterization, retain the complementary `E=M/(J a^2)` masks, and lose at most `B^o(1)` in all packet summations.

If such an ordinary-divisor upper theorem applies on the correct physical measure, the squareclass restriction needs no further density penalty: the exact subset relation is enough for the upper lane.

## 5. Verdict / firewalls

```text
SQUARECLASS_DIVISOR_TO_SQUARE_DIVISOR_PARAMETERIZATION=PROVED
RECIPROCAL_WINDOW_SQUARE_ROOT_REPARAMETERIZATION=PROVED
SQUARECLASS_SUPPORT_SUBSET_OF_ORDINARY_DIVISOR_SUPPORT=PROVED
ORDINARY_DIVISOR_THEOREM_PHYSICAL_MEASURE_COMPATIBILITY_PROVED=false
COMPLEMENTARY_PHYSICAL_COFACTOR_MASK_REMOVABLE=false
FIRST_MISSING_LEMMA=PhysicalSquareDivisorWindowOrdinaryShadowMeasureCompatibility
SR_STR_170_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
