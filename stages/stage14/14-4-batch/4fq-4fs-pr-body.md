## Stage14-main-batch — 4fq through 4fs

Starts from and publication-rechecks merged main `3af02c764300db002cce3e3bdf7da1236548ecbd`.

### Results
- `4fq`: on fixed `E=E0`, separates physical outer support from the bare short-unitary shadow. If `S_bare=B^(sigma+o(1))`, `S_phys=B^(tau+o(1))`, and `delta_c=sigma-tau`, survival requires exactly `sigma-delta_c=tau>=mu`; exponent-zero conditional completion density is not forced.
- `4fr`: performs the same split on polynomial `E`, consuming merged s7-98 without recharge. The `m=B^o(1)` branch has one-dimensional outer coordinate `E`; polynomial `m` retains `(E,m)`.
- `4fs`: unifies all heavy complementary-dilation branches into a nested-support budget and separates two noninterchangeable saving mechanisms: bare short-unitary shadow sparsity versus conditional canonical/reverse completion deficit.

The heavy receiver materially changes to

`ComplementaryDilationBareShortUnitaryShadowExponentVersusConditionalCanonicalReverseCompletionDeficitBudget`.

q14/Ford can only be compared to the bare fixed-E mechanism and still provides no branch-exact fixed-power Stage14 bound. It does not address the physical-completion deficit. No new heavy main H is opened.

```text
BATCH_START_MAIN_SHA=3af02c764300db002cce3e3bdf7da1236548ecbd
BATCH_PUBLICATION_MAIN_SHA=3af02c764300db002cce3e3bdf7da1236548ecbd
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4ft
```

Includes deterministic nested-support/unitary-divisor audit, regressions for merged 4fn..4fp, s7-96..98 and Work-buX33, publication lock, and path-scoped CI.
