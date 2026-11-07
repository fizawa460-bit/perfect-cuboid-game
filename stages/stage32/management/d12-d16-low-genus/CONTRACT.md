# Stage32 D12-D16-LOW-GENUS — no curves of degree 12, 14 (all classes) or 16 (unibranch-compatible classes) and geometric genus ≤ 1 (proof + computation, research cycles 32R-38..80)

```text
CLAIM: Let S̃ be the minimal resolution of the cuboid surface S and d = K·C.
       (a) d = 12: every integral curve C on S̃ has geometric genus >= 2 (all 2029 class representatives).
       (b) d = 14: the same (all 1487 class representatives).
       (c) d = 16: the same for every class of the 71,697 unibranch-compatible representatives (of 1,737,363).
STATUS: Reading (paper) audit, five rounds. Round 1 (8 audits): PAPER AUDIT FAIL; rounds 2-4: HOLD; round 5 (reading
        audit of R2, 2026-11-06): PASS (conditional), four should-fix items, all wording, answered in PAPER-R2.md §R.6.
        Under the owner's audit standard (MAIN-START-HERE, #1851: a reading audit that finds nothing wrong is enough;
        re-execution optional) this is a PASS. Zero credit; no credit flag is changed.
SCOPE: A geometric fact about the d = 12, 14, 16 strata. MAIN authority and all formal counts are unchanged.
NOT CLAIMED: d = 16 multibranch-only classes (1,665,666 representatives). They belong to 32-03 / the unrestricted
        programme and are being judged separately (not part of this leaf).
BUILDS ON: d8-low-genus (#1844) and d10-low-genus (#1845), both audited; route-E E02/E04 (merged, executing audit PASS);
        route-E E03 (1), reproduced with proof in PAPER-R2.md Appendix K and audited with this package.
```

## Files
| path | content |
|---|---|
| `PAPER-R2.md` | the audited package (verbatim copy of `AUDIT-PACKAGE-32-02-D12-D16-R2.md`). Single source for the claim, the tools (Lemma G, T1-T7), the case analysis, the audit responses (§R) and the proofs (Appendices A-D, J, K). |
| `logs/` | research logs 32R-38..80 cited by the package (Appendix I). |
| `code/` | source snapshot (`*.py`, `*.sh`, `*.c`, Singular tail templates) of the directories named in Appendix I, with the paths of the local workspace (`code/split/` = `stage32_research/split/`, `code/<dir>/` = `stage32_research/stoll/<dir>/`). Some files in `code/split/` are later tools (d = 18 / 20, all-class runs) that this leaf does not use. |
| `RESULT.json` | counts and status. |
| `MANIFEST-sha256.txt` | sha256 of every file of this leaf. |

## What is not in the repository
The generated data (enumeration shards about 2.8 GB, Singular inputs/outputs of the h0, pencil and net stages) stay in
the owner's local workspace (`claudework/stage32_research/`). Under the audit standard the computations need not be
re-executed; the package states what each computation decides (PAPER-R2.md §2-§4, Appendices E-G).

## Points the audits checked (PAPER-R2.md §7, §R)
- exact y-stage of the split enumeration (`split/splitenum9x.c`, `gen_exact.py`);
- T1 (does the ideal compute |x|), Lemma G (App. A), genus additivity and pieces (App. B-D);
- the char-p formulation of pencils and nets (§2.5), including δ <= μ in char p (§2.5(i));
- the non-reduced members and the 2Γ-families (§4.5-§4.7);
- the μ filter for the 13 nets of μ = 16 (App. J) and route-E E03 (1) (App. K).
