# Stage14-bridge1 — conditional second-face survival -> chamber local-density handoff

## Purpose

Translate the merged numerical second-face survival signal into the smallest proof-side task that can explain or falsify it, without promoting finite data to an asymptotic theorem.

Authoritative numerical sources:

```text
Stage14-num-alpha11-diag7  PR #320  merge eb43ba338e3b377242000cbdee0a5ffcf4522317
Stage14-num-alpha11-diag8  PR #324  merge 3f98deb3f6fb043cca2a63dfcd98645235b9fd67
frozen diag8 summary blob  52a1b180987d378684d4c87361935ded41f7fd24
```

The proof-side receiver is merged `Stage14-4bd`, whose nonconstant reciprocal/local Fourier error is now power-saving while the constant/diagonal local-density term `D_loc` remains open.  Its prescribed next task is `Stage14-4be evaluate D_loc/A_W`.

No new numerical census and no external theorem are used here.

---

## 1. Exact finite algebra

Use the exactly-two shared-edge chamber counts

```text
a = #(ab & ac),
b = #(ab & bc),
c = #(ac & bc).
```

For the raw one-face denominators

```text
A_ab, A_ac, A_bc,
```

the endpoint loads are exactly

```text
E_ab = a+b,
E_ac = a+c,
E_bc = b+c.
```

At every merged diag8 checkpoint through `B=1,000,000`, the frozen census verifies

```text
A_q - N1_q = E_q
```

and `T(B)=0`, so the finite conditional second-face survival rates are exactly

```text
S_ab = (a+b)/A_ab,
S_ac = (a+c)/A_ac,
S_bc = (b+c)/A_bc.
```

This is an identity of the finite census; it does not assume a limiting pair law.

---

## 2. The signal survives the first bridge controls

Merged diag8 evaluates the same canonical observable at

```text
B = 100k, 200k, 300k, 400k, 500k, 750k, 1m.
```

Relative to `S_bc=1`,

```text
100k : 0.570448 : 0.942733 : 1
200k : 0.597980 : 0.833559 : 1
300k : 0.599843 : 0.827653 : 1
400k : 0.594434 : 0.853837 : 1
500k : 0.601907 : 0.869959 : 1
750k : 0.597434 : 0.871081 : 1
1m   : 0.604399 : 0.908758 : 1
```

Hence the ordering

```text
S_ab < S_ac < S_bc
```

holds at every frozen checkpoint in this range.

What survives is the **directional ordering**, not a fitted limiting vector.  The profile is not monotone toward the diagnostic target derived from a hypothetical `2:2:1` exactly-two law.

Bridge evidence therefore advances from `L1` to `L2`, but no convergence claim is made.

---

## 3. Exact algebraic bridge from pair chambers to survival

Let a hypothetical asymptotic exactly-two chamber vector be

```text
(C_a,C_b,C_c)
```

and let the corresponding raw-face denominator constants be

```text
(P_ab,P_ac,P_bc).
```

If both scales exist, the induced endpoint vector is algebraically

```text
(C_a+C_b, C_a+C_c, C_b+C_c),
```

so the relative survival constants must be proportional to

```text
(C_a+C_b)/P_ab,
(C_a+C_c)/P_ac,
(C_b+C_c)/P_bc.
```

This implication is purely algebraic conditional on existence of the two asymptotic scales.  It does not assert that those scales have been proved.

For the diagnostic specialization

```text
(C_a:C_b:C_c) = 2:2:1
```

the endpoint law is exactly

```text
4:3:3.
```

Combining this with the proved Stage13 limiting face vector recorded by diag8,

```text
(P_ab,P_ac,P_bc)
 = (0.5347369332, 0.2453591778, 0.2199038889),
```

gives the normalized diagnostic survival profile

```text
0.54831669 : 0.89625296 : 1.
```

This reproduces the diag7/diag8 bridge target, but `2:2:1` remains a diagnostic assumption only.

Bridge evidence reaches `L3`: the finite phenomenon has an exact pair-chamber / endpoint / denominator reformulation.

---

## 4. Why the live receiver is 14-4be, not another character-sum stage

Merged `Stage14-s5r` closes the actual finite local 2-descent character polynomial with a power-saving average.  Merged `Stage14-4bd` imports that closure and proves

```text
E_rec(M) << M^(2-1/200+o(1)),
E_rec(B) << B^(399/400+o(1)).
```

The main-track local decomposition is still

```text
S_W <= D_loc + E_rec.
```

Here `E_rec` contains the nonconstant reciprocal/local Fourier modes.  The explicitly unresolved term is

```text
D_loc / A_W,
```

the constant/diagonal local-density contribution.

Therefore a persistent **leading directional density difference**, if it is already visible at the local-solubility layer, should be looked for first in the chamber-resolved constant/diagonal term rather than by reopening the now-closed reciprocal-error machinery.

This is not a theorem that the numerical bias is local.  It is a falsifiable routing statement:

- if the correctly normalized chamberwise `D_loc/A_W` values differ, they provide a proof-side mechanism candidate for part of the observed survival bias;
- if they are equal after the exact chamber normalization, the current local constant mode cannot explain the directional ordering, and the bridge must move the mechanism search to the remaining global-solubility / physical-height / archimedean layer.

Bridge evidence reaches `L4` because the finite observable now has a live proof-side receiver and a precise negative outcome.

---

## 5. Receiver dictionary

The required dictionary is

```text
NUM a = #(ab&ac)  <-> Stage14 exactly-two shared-edge chamber a
NUM b = #(ab&bc)  <-> Stage14 exactly-two shared-edge chamber b
NUM c = #(ac&bc)  <-> Stage14 exactly-two shared-edge chamber c

NUM A_ab,A_ac,A_bc <-> Stage13/raw distinguished-face chamber denominators
NUM endpoint E_q   <-> incidence of exactly-two chambers at source face q
NUM S_q=E_q/A_q    <-> conditional source-face survival observable

proof A_W^(j)       <-> ambient weight/count in 14-4 chamber j
proof D_loc^(j)     <-> constant/diagonal locally-soluble contribution in chamber j
proof E_rec^(j)     <-> nonconstant reciprocal error, already power-saving in 14-4bd
```

The shared-edge chamber index `j` is `a,b,c`.  If `14-4be`'s exact local bookkeeping is naturally source->destination directed rather than symmetric in the shared-edge chamber, it should retain the six directed cells before summing:

```text
ab->ac, ab->bc,
ac->ab, ac->bc,
bc->ab, bc->ac.
```

Their pairwise sums must reproduce the three source-face endpoint loads above.

---

## 6. Smallest falsifiable receiving task — handoff to Stage14-4be

`Stage14-4be` should augment its already-prescribed `D_loc/A_W` evaluation with a **chamber-resolved ledger**.

### Test A — freeze the diagonal constants by chamber

Compute, with the exact same local states and `Q_2` branches already owned by 14-4,

```text
rho_diag,a = D_loc^(a) / A_W^(a),
rho_diag,b = D_loc^(b) / A_W^(b),
rho_diag,c = D_loc^(c) / A_W^(c).
```

Do not average the three chambers before this comparison.

### Test B — decide whether local density can carry a directional mechanism

Record exactly one of

```text
CHAMBER_DIAGONAL_LOCAL_DENSITIES_EQUAL_AFTER_NORMALIZATION=true
```

or

```text
CHAMBER_DIAGONAL_LOCAL_DENSITIES_EQUAL_AFTER_NORMALIZATION=false.
```

If equal, bridge1's local-density mechanism candidate is falsified and the observed survival ordering must be sought beyond the local constant mode.

If unequal, retain the exact chamber vector and assemble the induced endpoint/source-face vector before any numerical comparison.

### Test C — compare only structural predictions

The first comparison with diag8 is limited to:

1. whether the induced source-face ordering predicts `S_ab<S_ac<S_bc`;
2. whether the induced endpoint asymmetry has the same sign pattern as the frozen data;
3. whether any claimed normalization is exact from the proof definitions.

Do **not** fit the finite `B<=1m` ratios to choose local constants, and do not declare a limit from numerical agreement.

This is the `L5` handoff.

---

## 7. What bridge1 does not claim

Bridge1 does not prove:

```text
S_ab:S_ac:S_bc has a limit;
(a:b:c) -> 2:2:1;
D_loc/A_W equals the physical second-face survival probability;
local solubility equals global solubility;
the finite survival ordering persists asymptotically;
T(B)=0 for all B.
```

The local character system is a proof-side majorant/interface.  Global solubility and the physical small-point/height filter can still change the final physical directional constants.

---

## Handoff / boundary

```text
STAGE14_BRIDGE1=COMPLETE_CONDITIONAL_SECOND_FACE_SURVIVAL_TO_LOCAL_DENSITY_HANDOFF
SOURCE_NUM_STAGE=Stage14-num-alpha11-diag7+diag8
SOURCE_NUM_PR=320+324
SOURCE_NUM_MERGE_SHA=eb43ba338e3b377242000cbdee0a5ffcf4522317+3f98deb3f6fb043cca2a63dfcd98645235b9fd67
SOURCE_DATA_BLOB_SHA=52a1b180987d378684d4c87361935ded41f7fd24
OBSERVABLE=conditional_second_face_survival_by_source_face
FINITE_SCOPE=B<=1000000
CONTROLS_PASSED=exact_recomposition+seven_cumulative_checkpoints+fixed_canonicalization
SURVIVAL_ORDERING_PERSISTENT_ON_FROZEN_CHECKPOINTS=true
SURVIVAL_PROFILE_MONOTONE_LIMIT_CLAIM=false
EXACT_ENDPOINT_ALGEBRAIZATION=true
RECEIVER_ROUTE=Stage14-4
RECEIVER_STAGE_OR_FILE=Stage14-4be_after_merged_14-4bd
RECEIVER_OBJECT=chamber_resolved_D_loc_over_A_W
E_REC_REOPEN_REQUIRED=false
HANDOFF_TEST=compute_chamberwise_D_loc_over_A_W_and_test_equal_vs_directional_local_density
EVIDENCE_LEVEL_BEFORE=L1
EVIDENCE_LEVEL_AFTER=L5
ASYMPTOTIC_CLAIM=false
FINITE_ZERO_NONEXISTENCE_CLAIM=false
NEXT=Stage14-bridge2 p=7 local-signature translator after bridge1 merge
```
