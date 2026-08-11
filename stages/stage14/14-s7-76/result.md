# Stage14-s7-76 — exact primitive-ray versus nonzero-determinant projective collision split

## Status

`COMPLETE_OFFDIAGONAL_PROJECTIVE_COLLISION_TO_REPEATED_PRIMITIVE_RAY_OR_NONZERO_DETERMINANT_MOVER_SPLIT`

Consumes batch-local `Stage14-s7-75`, merged `Stage14-4ek`, merged `Stage14-s7-70/71`, and latest merged main at batch start.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Primitive projective candidate vectors

Every live opposite-reciprocal candidate on the polynomial-core branch has

```text
v(z)=(X0(z),Y0(z)),
gcd(X0,Y0)=1,
gcd(C,X0Y0)=1.
```

For two candidates at the same exact modulus define the integer determinant

```text
Delta(z1,z2)=X1Y2-X2Y1.
```

The projective collision condition is exactly

```text
C | Delta(z1,z2).
```

## 2. Exact zero determinant means one primitive projective ray

If

```text
Delta(z1,z2)=0,
```

then the two primitive integer vectors are rationally proportional. Since both are primitive, they agree up to the finite sign/unit convention already included in the frozen physical orientation labels.

Thus zero-determinant off-diagonal collisions are precisely repeated occurrences of one primitive projective ray.

```text
ZERO_DETERMINANT_COLLISION_IFF_SAME_PRIMITIVE_PROJECTIVE_RAY=true
FINITE_SIGN_UNIT_LABEL_COST=O1
```

No reverse-fiber bound from a projective ray to canonical allocation witnesses is assumed here.

## 3. Exact ray/mover decomposition

For one exact polynomial modulus `C`, let `m_C(r)` be the charged-once unit-incidence multiplicity of primitive ray `r`. Define

```text
K_ray(C)=sum_r m_C(r)(m_C(r)-1),
```

and

```text
K_mov(C)
 = # {(z1,z2):
      z1!=z2,
      Delta(z1,z2)!=0,
      C|Delta(z1,z2)}.
```

Then exactly

```text
K_off(C)=K_ray(C)+K_mov(C).
```

On the mover part one may write

```text
Delta(z1,z2)=k C,
k in Z\{0}.
```

The quotient `k` is not yet known to be short or sparse and is not charged as a new saving coordinate.

```text
OFFDIAGONAL_COLLISION_RAY_MOVER_DECOMPOSITION_EXACT=true
NONZERO_DETERMINANT_MOVER_EQUATION=Delta_equals_kC
MOVER_QUOTIENT_FIXED_POWER_SAVING_PROVED=false
```

## 4. Why repeated rays cannot be discarded a priori

Candidate multiplicity is only known to be `B^o(1)` after fixing one canonical allocation slope/witness. It does not imply that the same primitive reciprocal ray cannot be produced by polynomially many distinct physical backgrounds.

Therefore the repeated-ray term `K_ray(C)` is a genuine possible concentration mechanism and cannot be absorbed into the diagonal or finite-fiber bookkeeping without a new reverse-incidence argument.

```text
GLOBAL_PRIMITIVE_RAY_MULTIPLICITY_BOUND=UNPROVED
REPEATED_RAY_RECHARGED_AS_FINITE_FIBER=false
```

## 5. Receiver and next

Stage14-s7-75 forces

```text
K_off(C)=M_C^2 B^(-o(1))
```

on a concentrated saturating exact-modulus sequence. By the exact split above, at least one of repeated-ray mass or genuine mover mass must itself remain exponent-zero on the pair-density scale.

The next stage makes this dichotomy quantitative through the maximum primitive-ray multiplicity.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_76_NEW_AUXILIARY_H_NEEDED=false
```

## Boundary

```text
STAGE14_S7_76=COMPLETE_OFFDIAGONAL_PROJECTIVE_COLLISION_TO_REPEATED_PRIMITIVE_RAY_OR_NONZERO_DETERMINANT_MOVER_SPLIT
ZERO_DETERMINANT_COLLISION_IFF_SAME_PRIMITIVE_PROJECTIVE_RAY=true
OFFDIAGONAL_COLLISION_RAY_MOVER_DECOMPOSITION_EXACT=true
NONZERO_DETERMINANT_MOVER_EQUATION=Delta_equals_kC
GLOBAL_PRIMITIVE_RAY_MULTIPLICITY_BOUND=UNPROVED
MOVER_QUOTIENT_FIXED_POWER_SAVING_PROVED=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_76_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-77
```
