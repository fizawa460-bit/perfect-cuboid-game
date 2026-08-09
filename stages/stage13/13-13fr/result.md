# Stage13-13fr — result

R07 Gate B closes the concrete fixed-S residue-model objection raised against R06.

The repair uses one explicit inert-prime model throughout:

```text
valuation strata: U, R_b, S_c
unit residue set: X^2+Y^2=1, Delta^2-Z^2=1
second-face test: W_p=1_{X^2+Z^2 in QR_0(F_p)}
```

A true second integral face gives the global square `x^2+z^2=w^2`, hence reduces directly to `W_p=1`. Positive-valuation states pass automatically, while the unit stratum has exact accepted cardinality `(p+1)^2/2`, giving

```text
alpha_p=(p+1)/(2(p-1))
lambda_p=(p+5)/(2(p+1)).
```

The same physical state model is then used for the finite Fourier expansion, effective-character quotient, five-slot pole signature, principal residue and fixed-S multiplier. Equivalent ambient characters agree on every actual coefficient state, so the reduced pole signature is representative-independent. The full principal sector contributes exactly `product lambda_p`; every nonprincipal class loses at least one pole termwise.

```text
STAGE13_13FR=COMPLETE_R07_CONCRETE_FIXED_S_RESIDUE_MODEL
R07_GATE_B=COMPLETE
R07_ACTUAL_RESIDUE_COORDINATES_EXPLICIT=true
R07_GLOBAL_SECOND_FACE_IMPLIES_LOCAL_TEST=true
R07_EFFECTIVE_QUOTIENT_WELL_DEFINED=true
R07_REDUCED_POLE_SIGNATURE_WELL_DEFINED=true
R07_PRINCIPAL_RESIDUE_RATIO_COMPUTED_IN_SAME_MODEL=true
R07_NONPRINCIPAL_TERM_WISE_POLE_LOSS=true
R07_TAGGED_SHARED_EDGE_INJECTION_FIXED_S_EXPLICIT=true
R07_REPAIR_BLOCKERS_OPEN=1
R07_BLOCKER_C_CURVED_REGION_SELF_CONTAINED_CLOSURE=true
R06_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fs
```

The remaining R07 theorem/proof-facing blocker is Gate C: promote the full curved-region uniform-error proof into the self-contained R07 review target.