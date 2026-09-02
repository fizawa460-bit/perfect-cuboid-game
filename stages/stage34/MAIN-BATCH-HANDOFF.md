# Stage34 MAIN batch handoff

```text
STATUS=PR1489_Q8413_TORSION_PARENT_CLASSIFICATION_PREAUDIT_READY
PR=#1489 OPEN
BRANCH=stage34-main/q8413-torsion-parent-classification
BASE_MAIN=97f3da5dfad72630aaf0f3b8088c85b7a285b01b
MATHEMATICAL_EVIDENCE_FROZEN_HEAD=94fb93eec0e92a006f94721aa90082fc9aa0e9f8
AUTHORITATIVE_REMAINING=4
AUTHORITATIVE_SIGN_ORBITS=2
Q8413_REPRESENTATIVE_CLOSURE_CANDIDATES=2
Q8413_SIGN_TRANSFER_CANDIDATES=2
HOSTILE_AUDIT_PASSED=false
D2_ALL_FACTOR_BRANCHES_CLOSED=false
R29_EXT_CHANG_C_CLOSED=false
MERGE_ALLOWED=false
```

Transient PREAUDIT delta only. `MAIN-STATE.json` remains the promoted machine authority and is intentionally unchanged until hostile audit authorizes promotion.

## Exact q=84/13 result frozen on this PR

Source:

- `stages/stage34/34-02/prove_d2_stageA2_q8413_torsion_parent_classification.py`
- `stages/stage34/34-02/d2-stageA2-q8413-torsion-parent-classification-certificate.json`

For both rank-zero Q(i) elliptic quotients, good reduction at the Gaussian primes above 29 and 37 gives exact group orders:

- model 38: `28, 40`, gcd `4`;
- model 165: `28, 48`, gcd `4`.

Each quotient already has full rational 2-torsion `C2 x C2`, so its complete Q(i)-torsion subgroup has order exactly 4. Since the retained PREAUDIT Mordell-Weil rank is zero, these are all quotient points.

Rational quotient-X and inverse genus-two reconstruction are therefore complete:

- model 38 / `40dc8f63e92a8a3a65e8`: rational X `{0,89531}` gives x `{-1,1,-7/6,6/7}`. The only full-parent lift is x=`-7/6`, with `A=0`; every reconstructed point is receiver-degenerate. Nondegenerate full-parent lifts: `0`.
- model 165 / `7a7ef1a67e794fe1651f`: rational X `{-1157016,0}` gives x `{-13,1/13,-1,1}`. The only full-parent lift is x=`-13`, with `B=0`; every reconstructed point is receiver-degenerate. Nondegenerate full-parent lifts: `0`.
- quotient infinity is the already source-locked exceptional x=0/infinity receiver-degenerate locus.

Direct representative closure candidates:

- `40dc8f63e92a8a3a65e8`
- `7a7ef1a67e794fe1651f`

Exact sign-transfer candidates, not yet promoted:

- `8a374a057daf5f92a87e`
- `98b42307b3aa398f1e0c`

## Next exact gate

Independent hostile audit of the exact PR #1489 evidence. The audit must independently verify good reduction/torsion injection, both finite-field point counts, completeness of the rational-X torsion list, inverse reconstruction, U/V/A/B square tests, exceptional infinity, and applicability of the already-audited sign involution. Only a PASS may promote authority `4 branches / 2 sign orbits -> 0 / 0`.

Do not infer before that audit:

- authoritative q=84/13 branch closure;
- `D2_all_factor_branches_closed`;
- all-multiples closure;
- `R29_EXT_CHANG_C_closed`;
- parent-route closure;
- any perfect-cuboid existence/nonexistence claim.

Do not merge in this MAIN batch.
