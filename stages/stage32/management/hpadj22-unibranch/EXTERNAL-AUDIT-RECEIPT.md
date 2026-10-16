# External hostile audit receipt — HPADJ22-UNIBRANCH

```text
HOSTILE AUDIT: PASS
DATE: 2026-10-16
AUDITED HEAD: PR #1840, 2dcb2258ec3ecb3909aa723c428a2a5bebbd2b8e (source-root 4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2)
REPRODUCTION: Python 3.12.14, verifier exit 0; 5,369,214,401 compressed terminals, 40 nonzero rows
SCOPE: exact count of compressed terminals passing the stated necessary-condition filter
NOT INCLUDED: nonexistence of curves, perfect-cuboid existence/nonexistence, MAIN promotion, merge permission
```

## Item verdicts

| # | Item | Verdict | Auditor's basis |
|---|---|---|---|
| 1 | Does `srem` bound hidden support? | PASS | It is derived from the N357 unit-capacity flow, with component bounds min(16,d), min(13,d-a,d-2a+4,h+5) and min(9,d-b-c,d-2b,d-2c+1). It is a support bound, not a mass bound. Independently matched against all 16 cuts on 75,950 cases. |
| 2 | Do `support` and ν use the same coordinates? | PASS | The assignment order is [95,99,103,102,49,97,94,101,93,98,96]. x4 (label 49) is excluded, which leaves exceptional labels 93..103 without 100. The groups a, b, c partition these 10 exactly. 38 exceptional coordinates remain hidden. |
| 3 | Is `req(e)` per e correct? | PASS | The verifier requires support + min(srem, e−M) ≥ max(K, ⌈(d+e)/2⌉−2g+2). The code's `need` test is equivalent, and its integer ceilings are correct. |
| 4 | Do the population, MIN and conjunction agree? | PASS | Both sides count the same (g,d,e,x0..x10) terminals, with the same symmetry, lexicographic and parity conditions. HPADJ adds refining conditions only (x4<4d and e≤3d imply x4≤19d−5e). Since srem≤38, the strengthened survivor set is contained in the V50 set, so a per-row MIN is valid. |
| 5 | Is removing the retained-value check justified? | PASS | That check compares against the HPADJ08 rejected mass for the original e-set, so it does not apply to a reduced e-set. The unmodified run executes it on all 42 rows. |

The auditor's independent checks:
- The two d=8 rows were reproduced by direct 11-coordinate enumeration: g0-d008 434,188 / 215,857 and g1-d008 383,258 / 283,419.
- The V50 counting part was recomputed independently and agreed: 511,353,002,049 in 40 rows.

## Requested fixes and their resolution

| Class | Finding | Resolution |
|---|---|---|
| must fix | The Drive copy of RESULT.json carried an added `_note`, which broke the canonical hash. | A byte-identical copy was uploaded as `32R-08_RESULT_exact_repo_copy.json` (sha256 `60eecb88…`). The old file is renamed `SUPERSEDED_…`, and the explanation moved to its description. The repository file was never affected. |
| minor | Name N357 as the direct source of `srem`. | Added in `CONTRACT.md`. |
| minor | "exactly the unibranch necessary condition" should be "a necessary-condition filter using an upper bound on ν". | Reworded in `CONTRACT.md`. |

Notes:
- The auditor did not rerun the known-curve check (SymPy was not installed).
- The geometric proposition of 32R-01 rests on its own existing audit.
- After the audited head, only documentation files in this leaf changed: `CONTRACT.md` and this receipt. `RESULT.json` and the verifier are byte-identical to the audited head.
