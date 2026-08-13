# Stage13-13fu — R07 canonical synthesis result

> STATUS: `COMPLETE_R07_CANONICAL_PROOF_SYNTHESIS`

The R07 repairs are integrated into one canonical proof entrypoint:

```text
stages/stage13/13-13fu/stage13-r07-canonical-proof.md
```

The synthesis keeps the Stage13 theorem and constants unchanged while incorporating the full R07 repair chain:

1. fixed finite Gaussian-Hecke/ray-class twists are identified at the exact HLR/Merikoski angular normalization and proved holomorphic at `s=1` with common fixed-strip polynomial growth for fixed `S`;
2. the fixed-S overlap argument is instantiated on the explicit `U/R_b/S_c` residue model with the actual second-face square test, exact `lambda_p`, well-defined effective quotient and pole signature, principal multiplier, nonprincipal pole loss, and fixed-S tagged injection;
3. Vaaler angular approximation is separated from the physical curved cutoff, and the full `Lambda^27` box / boundary shell / mesh / harmonic error ledger is integrated;
4. exact integer Wiener inequalities, retained-`ell` uniform logarithmic moments, the epsilon-form overlap squeeze, and the Stage12 oriented-record factor-two statement are integrated.

```text
STAGE13_13FU=COMPLETE_R07_CANONICAL_PROOF_SYNTHESIS
R07_CANONICAL_PROOF=stages/stage13/13-13fu/stage13-r07-canonical-proof.md
R07_CANONICAL_PROOF_SINGLE_ENTRYPOINT=true
R07_GATES_A_B_C_D_COMPLETE=true
R07_REPAIR_BLOCKERS_OPEN=0
R07_HARDENING_OBLIGATIONS_OPEN=0
R07_FIXED_TWIST_CONTRACT_INTEGRATED=true
R07_CONCRETE_FIXED_S_MODEL_INTEGRATED=true
R07_CURVED_REGION_CLOSURE_INTEGRATED=true
R07_EXACT_ARITHMETIC_QUANTIFIERS_INTEGRATED=true
SUM_IQ_ANALYTIC_PROOF_COMPLETE=true
FINITE_DATA_USED_AS_PROOF=false
HECKE_PROOF_FOURIER_EXPONENT=8*ell
HECKE_HLR_INDEX=2*ell
HECKE_MERIKOSKI_INDEX=8*ell
HECKE_GAMMA_SHIFT=4*ell
GLOBAL_SECOND_FACE_IMPLIES_LOCAL_TEST=true
PRINCIPAL_RESIDUE_RATIO=product(lambda_p)
LAMBDA_P=(p+5)/(2(p+1))
LAMBDA_3=1
INERT_CONTRACTION_STARTS_AT_P_GE_7=true
MESH_PER_COORD=O(log(2B)/eta)=O((log B)^9)
BOX_COUNT=O((log B)^27)
ALL_BOX_FINITE_REMAINDER=O(B(log B)^-35)
CURVED_BOUNDARY=O(B(log B)^-5)
MESH_ERROR=O(B(log B)^-5)
HARMONIC_POLYLOG_EXPONENT=4*C_H+D_H+6
WIENER_529_INTEGER_INEQUALITY=true
WIENER_P5_INTEGER_INEQUALITY=true
WIENER_LOG_MOMENTS_UNIFORM_IN_ELL=true
OVERLAP_SQUEEZE_EPSILON_FORM=true
STAGE12_PROJECTION_FIBER_OBJECT=ORIENTED_DISTINGUISHED_FACE_RECORDS
R07_BUNDLE_CREATED=false
R07_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R06_IMMUTABLE=true
R06_VERDICTS_CARRY_FORWARD_TO_R07=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fv
```

`13-13fv` is reserved for building the immutable R07 self-contained review bundle from a fixed merged source snapshot. R07 external review counts must restart from zero.
