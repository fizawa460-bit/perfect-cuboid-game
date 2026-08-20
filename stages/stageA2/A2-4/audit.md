# StageA2 independent audit — A2-4

```text
AUDIT_VERDICT=PASS_WITH_ELEMENTARY_STRENGTHENING_AND_LANDMARK_REPAIR
AUDITED_TASK=STAGEA2-A2-4-R01
AUDITED_SUBMISSION_HEAD=de59f9bedd396afabef097270b856dcb13e9a6aa
BASE_MAIN_AUDIT=PASS
BASE_MAIN=231eff9bbf0a1c45f60f0ec04057f00ec8777f6b
BASE_MAIN_IS_A2_3_MERGE=PASS
SOURCE_MINUS18_FIREWALL_AUDIT=PASS
Q18_FACTOR_AUDIT=PASS
FIRST_GCD_BOUND_AUDIT=PASS
FIRST_SPLIT_PARITY_STRENGTHENING=PASS_DELTA1_ONLY
FIRST_DELTA2_Q5_AUDIT=PASS_BUT_REDUNDANT
CONIC_PARAMETERIZATION_AUDIT=PASS
SECOND_FACTOR_IDENTITY_AUDIT=PASS
SECOND_GCD_BOUND_AUDIT=PASS
SECOND_SPLIT_PARITY_STRENGTHENING=PASS_DELTA_PLUSMINUS1_ONLY
SECOND_PLUSMINUS2_Q5_AUDIT=PASS_BUT_REDUNDANT
CPLUS_CMINUS_RECEIVER_AUDIT=PASS
FIRST_RECONSTRUCTION_T_COVER_AUDIT=PASS
T_INFINITY_LANDMARK_AUDIT=FAIL_THEN_REPAIRED
T_INFINITY_BRANCH=Cplus
T_INFINITY_IMAGE=z=2,U=-4_EXCLUDED_K1_WALL
COMPLETE_E18_RATIONAL_POINT_CLOSURE=false
GENERAL_COVERAGE_PROVED=false
NEW_ARBITRARY_CUBE_CONSTRAINT=false
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
EXACT_HEAD_STAGEA2_CI=NOT_CONFIGURED
AUDIT_REPAIR_PERFORMED=true
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
NEXT_TARGET=A2-5_PUBLISHED_MINUS18_TWO_COVER_RATIONAL_POINT_CLOSURE
NEXT_EXPECTED_COMMAND=StageA2-main-batch
```

## Independent algebra audit

The audit recomputed the factorization

`Q18=(z^2-8z+28)(z^2+8z-4)`

and the two exact parameter identities

`z=(2t^2-8t-6)/(t^2-1)`

and

`z^2-4=-16(2t+1)(t^2-2t-2)/(t^2-1)^2`.

All reproduce exactly. The submitted mod-5 eliminations are also correct, but the audit found stronger elementary parity statements that make those local eliminations unnecessary.

For reduced `z=a/b`, put

`F1=a^2-8ab+28b^2`, `F2=a^2+8ab-4b^2`.

The submitted proof gives `gcd(F1,F2)|2^8`, so all odd prime valuations in each factor are even once `F1F2` is a square. At `2`, primitiveness gives:

- if `a` is odd or `b` is even, both factors are odd;
- if `a=2m`, `b` odd and `m` even, both have `v2=2`;
- if `a=2m`, `b` odd and `m` odd, both have `v2=4` (the residual brackets are `4 mod 8`).

Hence `v2(F1)` and `v2(F2)` are always even. Since both factors are positive on a rational `E18` point, each is itself a square. Thus the exact first split is already `delta=1`; the submitted `delta=2` branch is a harmless over-approximation and its `Q_5` emptiness check is correct but redundant.

For reduced `t=a/b`, put

`A=a^2-5ab-5b^2`, `B=a^2-ab-b^2`.

The submitted argument gives `gcd(A,B)|4`. But for primitive `(a,b)`, both `A` and `B` are always odd, so the gcd is odd and therefore equals `1`. Since `AB` is a square, `A` and `B` have the same sign and their absolute values are individually squares. Thus the exact second split is directly `delta=+1` or `delta=-1`; the submitted `+/-2` branches are again harmless over-approximations, and the `Q_5` checks are correct but redundant.

Therefore the surviving receiver `Cplus/Cminus` is unchanged and is certified by a stronger elementary argument than the submission used.

## Landmark repair

The submitted landmark list omitted the projective parameter `t=infinity`. Homogenizing the `Cplus` equations gives at `W=0`

`R^2=T^2`, `S^2=T^2`,

so there are rational `Cplus` points at `t=infinity`. Under the conic parameterization,

`z -> 2`, `U -> -4`,

so these map to the same excluded `k=1` wall (`z=2`, `Y=+/-16`) already known from A2-3. They must not be treated as nondegenerate candidates in A2-5.

This omission does not change the finite two-cover descent or any exclusion. The machine-readable report/controller and verifier are repaired to record it.

No StageA2-specific workflow run exists on the exact submitted head, so CI is recorded as not configured rather than inferred from unrelated workflows.
