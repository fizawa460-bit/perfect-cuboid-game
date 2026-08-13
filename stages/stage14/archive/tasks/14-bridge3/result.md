# Stage14-bridge3 — residual direction-drift control gate and bridge closure

## Purpose

Bridge3 executes the final predeclared bridge task from `stages/stage14/archive/docs/operations/stage14-bridge-num-to-proof-roadmap.md`:

```text
raw direction shift
- explained local/arithmetic mixtures
- known cluster/family effects
= residual structured shift
```

The question is not whether the frozen exactly-two direction vector visibly moves between shells. It does. The question is whether the residual movement survives the already-merged control stack strongly enough to justify inventing a new proof-side mechanism.

Authoritative merged inputs are:

```text
Stage14-num-alpha11-diag4  PR #310  arithmetic/local partitions
Stage14-num-alpha11-diag5  PR #312  same-d and face-graph dependence controls
Stage14-num-alpha11-diag10 PR #334  finite-count shell heterogeneity calibration
Stage14-bridge2            PR #337  p=7 local-row packet translation
```

No new census is started.

---

## 1. Arithmetic mixtures leave a large descriptive residual

Diag4 froze the late-shell movement

```text
(300m,400m] -> (400m,500m]
observed direction-shift L2 = 0.12232012942880242.
```

Across all 22 predeclared arithmetic/congruence partitions, the best mixture-only reconstruction was

```text
best partition = p19_nonshared_zero_count
explained fraction L2 = 0.0342814300399743.
```

Therefore the tested arithmetic-class composition explains only about 3.4% of the observed late-shell vector movement under that same-data descriptive decomposition.

This is a negative mechanism test, not evidence that the remaining 96.6% is itself arithmetic structure.

---

## 2. Same-diagonal and face-graph dependence do not attenuate the shift

Diag5 tested the two strongest predeclared dependence proxies available in the frozen B500m population.

Equal weighting per represented space diagonal gives

```text
shift ratio relative to raw = 1.0133921901483236.
```

Equal weighting per primitive-face graph connected component gives

```text
shift ratio relative to raw = 1.09250237451836.
```

Thus neither control shrinks the late shift. The graph-component correction actually makes it slightly larger.

This closes two obvious family/multiplicity explanations, but again does not prove that the residual is a new coherent arithmetic family.

---

## 3. Shell-size calibration blocks promotion of the residual

Diag10 then asks the key promotion-gate question on the merged B<=1m shell panel.

Under the conditional common-direction permutation calibration:

```text
Pearson p                  = 0.4389912201755965
G-test p                   = 0.3382732345353093
max shell pair-L1 p        = 0.14199716005679885
survival-shape RMS p       = 0.49387012259754803.
```

The source-adjusted plug-in survival calibration gives a similarly nonexceptional RMS p-value.

Therefore

```text
FINITE_COUNT_SAMPLING_NOISE_SUFFICIENT_EXPLANATION_AT_CURRENT_B1M_PANEL=true
ARITHMETIC_SHELL_HETEROGENEITY_DETECTED=false.
```

This changes the bridge3 conclusion decisively: after the control stack, the residual shell movement does **not** pass the bridge evidence ladder's L2 promotion gate.

The correct output is not a speculative new invariant. It is a durable `NO_NEW_MECHANISM_YET` closure.

---

## 4. What remains real and already has an owner

Two direction-dependent finite signals remain useful, but neither is a new bridge3 residual.

### 4.1 Cumulative second-face survival ordering

Merged diag7/diag8 show persistent cumulative

```text
S_ab < S_ac < S_bc
```

through all listed checkpoints to B=1m.

Bridge1 already translated this to a chamber-resolved local-density question in Stage14-4. Bridge3 does not duplicate it.

### 4.2 p=7 shared-edge signature

Diag4/diag5 found a control-surviving finite p=7 direction association. Bridge2 translated it exactly into ordered `good/S/X` local-row packets on the two primitive faces.

Bridge2 explicitly did **not** prove that packet composition explains the full direction bias. That falsifiable receiving test remains owned by Stage14-4.

Bridge3 therefore does not reinterpret p=7 as the cause of the late shell movement.

---

## 5. Relation to the current post-local proof route

The proof tracks have now moved beyond the old local-only bottleneck:

```text
Stage14-s5u closes the s5 local method at physical exponent 41/42.
Stage14-4 / s6 are moving to direct post-local global-small-point witness counting.
```

If a future merged numerical result produces a genuinely control-surviving direction anomaly, the natural proof-side refinement is a chamber-conditioned version of that witness count, schematically

```text
J_C,q(B)
```

for `q in {a,b,c}`, optionally conditioned on a frozen local row packet such as the bridge2 p=7 state.

But bridge3 does **not** create that theorem task now, because the present residual shell drift did not survive the finite-count promotion gate.

This preserves the bridge rule:

```text
no stable mechanism -> no manufactured proof obstruction.
```

---

## 6. Reopen trigger

The bridge route is parked after bridge3. A bridge4 should be opened only if a newly merged result supplies at least one of:

```text
NEW_EXACT_IDENTITY
REPRODUCIBLE_LOCAL_SIGNATURE not already owned by bridge1/2
REPRODUCIBLE_FAMILY_OR_SQUARECLASS_SIGNATURE
CONTROL_SURVIVING_DIRECTIONAL_ANOMALY after finite-count calibration
NEW_THEOREM_LEVEL_QUESTION_FROM_FINITE_DATA
```

A particularly clean trigger would be an independent/higher-count shell panel that rejects the common-direction/common-survival finite-count null after multiplicity correction, or a receiver-side bridge1/2 calculation that leaves a reproducible chamber residual.

Until then:

```text
NEXT_BRIDGE_STAGE=NONE.
```

---

## Evidence ladder

```text
L1  exact late-shell vector movement                              yes
L2  survives arithmetic-mixture controls                         descriptively yes
L2  survives same-d / graph reweighting                           yes
L2  exceeds finite-count shell noise                              no
L3  new exact residual invariant                                  no
L4  new receiver dictionary beyond bridge1/2                      no
L5  new proof handoff                                             no
```

The correct scientific classification is therefore a controlled closure, not a failed stage.

```text
STAGE14_BRIDGE3=COMPLETE_RESIDUAL_DIRECTION_DRIFT_CONTROL_GATE_AND_BRIDGE_CLOSURE
RAW_LATE_SHIFT_EXACT_FINITE=true
KNOWN_ARITHMETIC_MIXTURE_EXPLAINS_LATE_SHIFT=false
SAME_DIAGONAL_DEPENDENCE_EXPLAINS_LATE_SHIFT=false
GRAPH_COMPONENT_DEPENDENCE_EXPLAINS_LATE_SHIFT=false
RESIDUAL_SHELL_DRIFT_EXCEEDS_FINITE_COUNT_NOISE_AT_5PCT=false
RESIDUAL_SHELL_DRIFT_PROMOTED_TO_L2=false
NEW_EXACT_PARAMETER_INVARIANT_ISOLATED=false
NEW_PROOF_RECEIVER_REQUIRED=false
BRIDGE1_CUMULATIVE_SURVIVAL_HANDOFF_REMAINS_ACTIVE=true
BRIDGE2_P7_ROW_PACKET_HANDOFF_REMAINS_ACTIVE=true
DURABLE_NO_NEW_MECHANISM_YET_CLOSURE=true
BRIDGE_SEQUENCE_PARKED=true
BRIDGE4_PREEMPTIVELY_CREATED=false
ASYMPTOTIC_DIRECTION_CLAIM=false
FINITE_ZERO_NONEXISTENCE_CLAIM=false
NEXT=NONE_UNTIL_NEW_MERGED_CONTROL_SURVIVING_DIRECTIONAL_OR_FAMILY_TRIGGER
```
