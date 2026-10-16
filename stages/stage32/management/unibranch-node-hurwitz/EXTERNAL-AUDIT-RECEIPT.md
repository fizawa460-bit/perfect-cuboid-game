# External hostile audit receipt — UNIBRANCH-NODE-HURWITZ

```text
HOSTILE AUDIT: PASS
DATE: 2026-10-16
AUDITED OBJECT: self-contained review bundle "32R-01" (proposition, known-curve check, census filter) at main 29e1c1067d2814128c8b4f7eee44d3f1e58e14cc
SCOPE: unibranch necessary condition 2*nu >= e+d-4g+4 and its filter on the compressed N220/N354 census
NOT INCLUDED: nonexistence of curves, perfect-cuboid existence/nonexistence, MAIN consumption permission
REPO EXACT-HEAD AUDIT OF THIS LEAF: PENDING
```

## Auditor findings (summary)

The auditor checked five items:

| Item | Verdict | Note |
|---|---|---|
| 1. `B = nu` | PASS | Holds under bijective normalization of the image on the singular surface. Smoothness of the resolved curve alone would not suffice. |
| 2. `R_i >= e - B + q_i` | PASS | Includes tangency, high multiplicity and exceptional/boundary intersection points. Fibres of different maps are counted in separate `R_1`, `R_2`. |
| 3. Fibre-component exclusion | PASS | Non-special fibres are smooth `X(8)`. The only special-fibre components are the 12 boundary elliptic curves and the 48 exceptional curves; Stoll--Testa v3 §5 agrees. |
| 4. Required-threshold replacement | PASS (as a compressed census) | `nu <= U = S_10 + min(38, e - M_10)` is a valid upper bound, so rejecting `U < max(K, L)` is correct. The `x4` factorization is preserved. |
| 5. Unibranch-only scope | PASS | An explicit multibranch configuration shows why `B = nu` fails outside the scope. |

Other findings:

- All 10 dependency blobs matched at the audited commit.
- **Reproduction** (Python 3.12.14, SymPy 1.14.0, python-flint 0.9.0, z3-solver 4.15.4.0):
  - the 80 covered known curves all hold with equality, with 0 violations;
  - N354 baseline `[17128, 38560956534397137634780102]`;
  - new count `[530, 511353002049]`, with all 40 per-row entries matching;
  - the N354 verifier itself passed.
- **Independent extra checks:**
  - direct enumeration of visible exceptional mass 0..10 against the N220 DP;
  - 42,340 cases (e = 0..729, thresholds -2..55) of `rejected_fast` against direct support counts;
  - local multiplicities `a, b <= 1000` with 0 violations;
  - boundary strata g0-d044/e48 (597) and g1-d048/e48 (673).

## Requested fixes and their resolution

| Class | Finding | Resolution in this leaf |
|---|---|---|
| must fix | Counts are compressed terminals (prefixes), not Picard classes or curves | Stated in `CONTRACT.md`, `RESULT.json` (`count_semantics`) and the verifier output |
| must fix | Make the local resolution `z = x*u^2` and the "no other special fibres" argument self-contained | `CONTRACT.md` proof step 2 |
| minor | The loop checks the 92 non-exceptional known curves (80 covered), not "all 140" | Corrected wording |
| minor | Equality holds for the 80 covered curves, not for the boundary 12 | Corrected wording |
| recommended | Regression test on the full 40-row output | The verifier compares all per-row data with `RESULT.json` |

The auditor did not verify a Python 3.10 environment; the author's WSL Python 3.10.6 replay passed.
