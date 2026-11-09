# Stage32 D16-ALL-CLASSES — no curve of degree 16 and geometric genus ≤ 1, all classes (multibranch-only included)

```text
CLAIM: Let S̃ be the minimal resolution of the cuboid surface S and d = K·C. Every integral non-exceptional curve C on
       S̃ with d = 16 has geometric genus >= 2. (R2 = management/d12-d16-low-genus proved this for the classes of the
       71,697 unibranch-compatible representatives; this leaf treats the other 1,665,666.)
       With R2 (d = 12, 14), d8 (#1844) and d10 (#1845): no integral curve of degree <= 16 and geometric genus <= 1
       except the known ones.
STATUS: reading (hostile) audit, three rounds: round 1 HOLD (a821e14f), round 2 HOLD narrow (4349cac6), round 3 PASS
        (6e22aef1), PAPER.md §7. Under the owner's audit standard (#1851) this is a PASS. Zero credit; no credit flag
        changed.
SCOPE: A geometric fact about the d = 16 stratum. MAIN authority, STATE files and all formal counts are unchanged.
BUILDS ON: R2 (#1852: T1-T7, Lemma G, §2.5, §4.5, the analyzer), E05.1 (μ filter, audited), the split enumeration.
NEW HERE: Lemma K (support on known curves), Lemma P (exact genus from all plane singular points); PAPER.md §2.
```

## Files
| path | content |
|---|---|
| `PAPER.md` | claim, pipeline, counts, the two new lemmas, audit points |
| `AUDIT-REQUEST.md` | reading-audit request |
| `logs/` | 32R-97 (this result), 32R-91 (chain context) |
| `code/` | scripts with workspace paths (`code/<dir>/` = `stage32_research/stoll/<dir>/`, `code/split/` = `stage32_research/split/`); they call R2 code (`fasth0/`, `gfast/`, `p16/`, `m16/`, `cnc/`, `fix0/`) as in R2's `code/` |
| `results/` | tallies and small result files (all counts quoted in PAPER.md) |
| `RESULT.json` | counts and status |
| `MANIFEST-sha256.txt` | sha256 of every file of this leaf |

Generated data (all-rep shards, Singular inputs/outputs) stay local (`claudework/stage32_research/`).
