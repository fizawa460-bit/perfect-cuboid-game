# StageA2 independent audit — A2-3

```text
AUDIT_VERDICT=PASS
AUDITED_TASK=STAGEA2-A2-3-R01
AUDITED_SUBMISSION_HEAD=c44a35c99015e476a486d6f61af6f681a4215b29
BASE_MAIN_AUDIT=PASS
BASE_MAIN=d031c6a7fd2d8f3fcdc6a5667bf6f6cbba75ea6e
BASE_MAIN_IS_A1_CLOSURE_MERGE=PASS
SOURCE_PDF_AUDIT=PASS
SOURCE_PDF_LOCATOR=arXiv:2604.05459v1_PDF_p13_equation_6
SOURCE_PRECEDING_PQ_MINUS18_AUDIT=PASS
PUBLISHED_ANCHOR_COEFFICIENT_AUDIT=PASS_MINUS18
EQUATION6_TRANSCRIPTION_AUDIT=PASS
SANITY_POINT_AUDIT=PASS_(3,1,7,1)
SANITY_POINT_8_OF_8_SQUARES_AUDIT=PASS
MINUS8_NEGATIVE_CONTROL_AUDIT=PASS_1_OF_8
RECIPROCAL_QUADRATIC_AUDIT=PASS
D18_EXPANSION_AUDIT=PASS
D18_DISCRIMINANT_AUDIT=PASS_MINUS_2^80_3^3_5^2
GENUS3_SMOOTHNESS_AUDIT=PASS
RECIPROCAL_QUOTIENT_AUDIT=PASS
Q18=z^4-40z^2+256z-112
Q18_DISCRIMINANT_AUDIT=PASS_MINUS_2^32_3_5
GENUS1_SMOOTHNESS_AUDIT=PASS
K1_EXCLUDED_WALL_AUDIT=PASS_z2_Yplusminus16
RECONSTRUCTION_THREE_SQUARE_COVERS_AUDIT=PASS
A1_MINUS8_IMPORT_FIREWALL_AUDIT=PASS
GENERAL_COVERAGE_PROVED=false
NEW_ARBITRARY_CUBE_CONSTRAINT=false
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
EXACT_HEAD_STAGEA2_CI=NOT_CONFIGURED
AUDIT_REPAIR_PERFORMED=false
REPAIR_REQUIRED=false
READY_TRANSITION=AUTHORIZED_AFTER_AUDIT
NEXT_TARGET=A2-4_PUBLISHED_MINUS18_QUARTIC_AND_EXACT_COVERS
NEXT_EXPECTED_COMMAND=StageA2-main-batch
```

## Independent source check

The audit did not rely on the StageA1 transcription. The arXiv v1 PDF was inspected directly. PDF p.13 equation (6) contains the factor `c^8-18c^4d^4+d^8` twice in the `a0` square factor. PDF p.12 also contains the same `-18` coefficient in the immediately preceding `(P,Q)` formula. This independently confirms that the StageA2 source lock is correct.

The exact equation-(6) formulas were then evaluated independently at `(c,d,G,H)=(3,1,7,1)`. The submitted tuple and all eight square roots reproduce exactly. Replacing only `-18` by `-8` leaves exactly one of the eight subset sums square, reproducing the negative control.

## Independent algebra check

Starting from the published `F18`, normalization with `x=c/d`, `r=G/H`, `k=x^2`, `u=r-1/r` gives

`4k(k-1)u^2-(k^4-18k^2+1)u-16k^2(k-1)=0`.

Its discriminant in `u` is exactly

`D18(k)=k^8-36k^6+256k^5-186k^4+256k^3-36k^2+1`,

with polynomial discriminant `-2^80*3^3*5^2`. The reciprocal quotient with `z=k+1/k` is exactly

`Y^2=z^4-40z^2+256z-112`,

whose polynomial discriminant is `-2^32*3*5`.

## New audit observation for A2-4

The correct published-minus18 polynomials have extra exact factorization structure:

`D18(k)=(k^4-8k^3+30k^2-8k+1)(k^4+8k^3-2k^2+8k+1)`

and

`z^4-40z^2+256z-112=(z^2-8z+28)(z^2+8z-4)`.

This does not invalidate A2-3. It is a useful fresh structural input for A2-4 and should be analyzed before importing any generic elliptic-curve machinery.

No StageA2-specific pull-request workflow run exists on the submitted head or the audited post-audit branch head, so CI is recorded as not configured rather than inferred from unrelated workflows.
