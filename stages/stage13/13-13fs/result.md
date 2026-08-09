# Stage13-13fs — result

R07 Gate C closes the final theorem-level blocker remaining after `13-13fq` and `13-13fr`.

The new proof-facing lemma is

```text
stages/stage13/13-13fs/curved-region-self-contained-closure.md
```

and makes the full rectangle-to-curved-region route self-contained, including the point most vulnerable to misreading: Vaaler approximates only the one-dimensional inner-angle chamber indicator; the physical height cutoff is never Fourier-approximated and is instead handled by the multiplicative mesh and thin-shell argument.

```text
STAGE13_13FS=COMPLETE_R07_CURVED_REGION_SELF_CONTAINED_CLOSURE
R07_GATE_C=COMPLETE
R07_CURVED_REGION_FULL_LEMMA_IN_REVIEW_TARGET=true
R07_PER_BOX_UNIFORMITY_EXPLICIT=true
R07_BOUNDARY_MESH_DERIVATION_EXPLICIT=true
R07_VAALER_TO_CURVED_REGION_ROUTE_EXPLICIT=true
R07_VAALER_APPLIES_ONLY_TO_INNER_ANGLE_INTERVALS=true
R07_PHYSICAL_CUTOFF_HANDLED_BY_MULTIPLICATIVE_SHELL=true
R07_VAALER_ENDPOINT_DISCRETE_CONVENTION_EXPLICIT=true
R07_PHYSICAL_EQUALITY_POINTS_RETAINED=true
MESH_PER_COORD=O(log(2B)/eta)=O((log B)^9)
BOX_COUNT=O((log B)^27)
PER_BOX_FINITE_REMAINDER=O(B(log B)^-62)
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
POWER_TAIL_SAVING=exp(-(3/16)(log B)^(1/4))
CURVED_BOUNDARY_MAIN_MASS=O(B(log B)^-5)
MESH_ERROR=O(B(log B)^-5)
MIXED_LOG_SHIFT_BOUND=O(B(log B)^2)
RETAINED_HARMONIC_POLYLOG=4*C_H+D_H+6
R07_REPAIR_BLOCKERS_OPEN=0
R07_GATES_A_B_C_COMPLETE=true
R07_GATE_D_HARDENING_REMAINS=true
R06_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13ft
```

`13-13ft` is the non-theorem-changing R07 Gate D hardening pass (exact rational inequalities, uniform logarithmic moments, epsilon-form fixed-S squeeze, and oriented-fiber wording) before canonical R07 synthesis.
