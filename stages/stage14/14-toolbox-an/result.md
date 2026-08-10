# Stage14-toolbox-an — barrier / obstruction atlas and next-receiver selector

Toolbox-an reorganizes only merged Stage14 results. It owns no new theorem and no new power saving.

Current checkpoint:

```text
V(B) << B^(7/8+o(1))
CURRENT_REMAINING_GAP_TO_SQRT=3/8
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=17/168
```

Current critical geometry:

```text
P,Q ~ B^(1/2)
a,b ~ B^(3/8)
x,y ~ B^(1/16)
xi=ab ~ B^(3/4)
```

Merged 4cb / s7-14 freezes the exact shared-label minimax

```text
E_support(gamma)=1/2+gamma/2
E_2cell(gamma)=1-gamma/6
E(gamma)=min(E_support,E_2cell)
gamma_critical=3/4
E_critical=7/8
```

The current direct theorem targets are:

1. off-diagonal joint-label collision saving
   `sum r_B(xi,k)(r_B(xi,k)-1) << B^(7/8-delta+o(1))` with `delta>0`;
2. physically realized `xi` sparsity with fixed `delta>0`, giving `E_delta=1-1/(8-12delta)`;
3. genuinely transverse coefficient gain `C^(-1/3-eta)` with `eta>0`, giving `E_eta=(7+3eta)/(8+6eta)`.

Merged t50 closes the auxiliary bad-prime aggregate and isolates the selector-sensitive two-modulus second moment as an open support theorem. For main/s it remains a bridge target until an exact operator/quantifier bridge to the live direct receiver is proved.

Merged t50 also records `TH14_NEEDED=true`. Stage14-tH14 should build the selector-sensitive two-auxiliary Gaussian second-moment receiver/certificate while retaining the physical selector and signed common-refinement structure.

Deliverables:

- `docs/stage14-toolbox/barrier-obstruction-atlas.md`
- `docs/stage14-toolbox/next-receiver-selector.md`
- 11 new canonical cards
- toolbox-am forward-compatible regression
- dedicated toolbox-an audit / CI

```text
STAGE14_TOOLBOX_AN=COMPLETE_BARRIER_OBSTRUCTION_ATLAS_AND_NEXT_RECEIVER_SELECTOR
CANONICAL_NEW_CARD_COUNT=11
CANONICAL_TOTAL_CARD_COUNT=109
ATLAS_STATUS_CLASS_COUNT=8
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
CURRENT_REMAINING_GAP_TO_SQRT=3/8
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=17/168
CURRENT_CRITICAL_SHARED_LABEL_EXPONENT=3/4
CURRENT_CRITICAL_SELECTED_COEFFICIENT_EXPONENT=3/8
CURRENT_CRITICAL_SQUAREPART_ROOT_EXPONENT=1/16
SHARED_LABEL_SUPPORT_PLUS_ONE_TWO_CELL_ARCHITECTURE_BARRIER=7/8
PRIMARY_DIRECT_OBSTRUCTION=OFF_DIAGONAL_XI_K_COLLISION_ENERGY
REALIZED_XI_SPARSITY_IS_DIRECT_GO=true
TRANSVERSE_COEFFICIENT_GAIN_IS_DIRECT_GO=true
SELECTOR_SENSITIVE_TWO_MODULUS_IS_MAIN_BRIDGE_GO=true
T_TWO_MODULUS_TO_MAIN_XI_K_OPERATOR_BRIDGE_PROVED=false
OFF_DIAGONAL_XI_K_COLLISION_POWER_SAVING_PROVED=false
REALIZED_LABEL_SPARSITY_POWER_SAVING_PROVED=false
TRANSVERSE_COEFFICIENT_GAIN_PROVED=false
EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED=true
SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false
COMPLETE_T32_BOUND_PROMOTED_TO_SPARSE_SELECTOR=false
PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_ALLOWED=false
TH14_NEEDED=true
CURRENT_7_8_LEDGER_SUPERSEDED=false
T51_OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_AN_OWNS_NEW_POWER_SAVING=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-ao critical-shell collision and second-moment interface contracts
```
