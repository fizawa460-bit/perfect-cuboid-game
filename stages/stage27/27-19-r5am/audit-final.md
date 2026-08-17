# Stage27-19-r5am-r5an — final fresh audit registration

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
R5AM_MATHEMATICAL_AUDIT=PASS
R5AN_MATHEMATICAL_AUDIT=PASS
CI_AUDIT=PASS
LIFECYCLE_AUDIT=PASS
PR=1061
PR_STATE=MERGED
PR_HEAD=1a4fdafb576374c7aff560d70ca9afe9a1b21095
MERGE_COMMIT=366548fbc2d41536cd0d0e285784e932ec27bad7
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_CLOSE_R5AM_R5AN=true
NEXT_DERIVED_ROUTE=27-19-r5ao
```

The initial r5am draft had an insufficiently justified conductor-prime step in the Pell count. The final PR head repairs this by passing to the maximal order of the real quadratic field and counting integral ideal divisors of the principal norm ideal. The required uniform subpower bound is accepted.

The initial r5an wording also overstated the ambient unit-slope universe as uniformly `asymp kappa^2`. The final PR head corrects this to the exact ambient count `phi(kappa)^2` with `phi(kappa)^2=kappa^(2-o(1))`. The core residue receiver remains valid: `4^omega(kappa)=kappa^o(1)` occupied paired slope classes.

Dedicated `Stage27-19-r5al-r5an Pell and kappa receiver` CI is SUCCESS on the final PR head.

No exponent promotion is authorized. Checkpoint 40 remains active.
