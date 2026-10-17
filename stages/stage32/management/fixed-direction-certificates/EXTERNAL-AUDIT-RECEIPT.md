# External hostile audit receipt — FIXED-DIRECTION-CERTIFICATES

```text
HOSTILE AUDIT: PASS
DATE: 2026-10-17
AUDITED HEAD: PR #1841, 6173ea54fbdcbfa6fa33e74cc66166c22839736d
REPRODUCTION: Python 3.12.14, gcc 13.3.0, OpenMP 8 threads; full verifier exit 0
  census prefixes 3,736,306,749; Hodge survivors 7,601,355,235; final survivors 727,865,116;
  per-row MIN with V51 726,240,487; all 530 strata equal RESULT.json
SCOPE: count of terminals passing the stated necessary-condition filter, and validity of the per-row MIN
NOT INCLUDED: curve existence or nonexistence, perfect-cuboid existence or nonexistence, MAIN promotion, merge permission
```

## Item verdicts

| # | Item | Verdict | Auditor's basis |
|---|---|---|---|
| 1 | Proof of the proposition | PASS* | Orthogonality holds for the intersection form: x*ᵀGy = tᵀQAy = 0. The inequality directions are correct. When c_D > 0 and lin_D < 0, s = −lin_D/c_D ≥ 0 is the minimiser. A kill needs the bound to be below L, so the strict `>` is right. *A general λ needs the c_D = 0 case too (see below). |
| 2 | Exact forms and integer scaling | PASS | Rebuilt in exact rationals; the Q denominator 456 and the forms hash match. An alternative formula that does not use the kernel N, BMB = P G⁻¹AᵀQAG⁻¹Pᵀ − PG⁻¹Pᵀ, reproduces LIN and all 24 c_D. The cross-multiplied test is correct. |
| 3 | Pruning in the C code | PASS | e − mass + support never increases as coordinates are added, so cutting a branch below the threshold is sound. The second support bound handles the step from value 0 to 1 correctly. x0 ≤ e/2 follows from x1 ≥ x0. The tie-break and parity rules are checked separately at the leaves. Prefix counts match on all 530 strata. |
| 4 | Overflow | PASS (for this input range) | e ≤ 72, x4 ≤ 672, and 64-bit inputs have absolute value at most 228,000,000. Every certificate product fits within 94 bits even under a conservative bound. 11,538 tasks against an allocation of 42,400. |
| 5 | Population and per-row MIN | PASS | Both counts rest on the same N220 unibranch census (same coordinate order, symmetry, parity and mass conditions). V51 is a refinement of it, so a per-row MIN is a valid upper bound. 726,240,487 is not a direct count of the joint survivor set. |
| 6 | Independent Python reference | PASS (limited independence) | It is a separate implementation, but it shares the form and strata construction and the same pruning idea. It covers the 40 smallest strata (8,859 prefixes) and is not a recount of the other 490 strata. |

The auditor's additional checks:
- A re-enumeration without the monotone pruning (choose the support positions, then take positive integer partitions) covered 80 strata and 58,852 prefixes. All three counts matched.
- The rational test and the integer test were compared on 120,000 cases. Equality does not reject.

## Requested fixes and their resolution

| Class | Finding | Resolution |
|---|---|---|
| must fix | A proof for a general λ must cover c_D = 0. | Added to `CONTRACT.md` step 9: if lin_D < 0, letting s → ∞ gives a contradiction. All 24 directions used here have c_D > 0, and the verifier requires it. |
| must fix | "Every multiplication is overflow-checked" is inaccurate. | `CONTRACT.md` corrected: only the certificate test is guarded; H and lin are covered by the input-range bound (≤ 94 bits). |
| minor | The Python reference is better described as recursive enumeration with integer-scaled exact tests. | `CONTRACT.md` corrected. The verifier docstring wording is marked as superseded; the code is unchanged. |

After the audited head, only documentation files in this leaf changed (`CONTRACT.md` and this receipt). `RESULT.json`, `count_fixed_direction_certificates.c`, `verify_fixed_direction_certificates.py` and `DIRECTIONS.json` are byte-identical to the audited head.
