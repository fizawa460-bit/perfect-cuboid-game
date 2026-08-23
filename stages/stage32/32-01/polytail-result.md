# Stage32-01-POLYTAIL — result

```text
STATUS=SUBMITTED_FOR_AUDIT
LEAF=L32-01-POLYTAIL
CLASS=2
```

The audited preflight exposed a 64-variable/140-halfspace homogeneous tail-cone computation that timed out under PyNormaliz.  The wall is removed algebraically rather than by extending runtime.

The source-locked Picard core satisfies the exact integer identity

```text
19*(H.x)
 = sum_{92 known nonexceptional curves D} (D.x)
 + 5*sum_{48 exceptional curves E} (E.x).
```

All coefficients on the right are strictly positive.  The verifier also checks that 64 of these intersection forms are the upstream primitive Picard basis Gram rows and have determinant `-2^28`, hence span the full dual space.

Therefore a class satisfying all 140 nonnegative-intersection inequalities and `H.x=0` has all 140 intersections zero and hence is the zero class.  Every positive fixed-degree slice is consequently bounded.  For degree `d` the exact coordinate bounds include

```text
0 <= D.x <= 19*d
0 <= E.x <= floor(19*d/5).
```

Submitted consequence:

```text
L32_01_POLYTAIL=CLOSED_EXACT_POSITIVE_DUAL_CERTIFICATE_PENDING_AUDIT
NORMALIZ_TAIL_CONE_REQUIRED=false
RAW_63D_CVP_REQUIRED=false
NEXT_RESIDUAL=32-01-GRADED-SLICE-INTEGER-ORBIT-ENUMERATOR
```

No census/effectivity/receiver credit is claimed:

```text
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
