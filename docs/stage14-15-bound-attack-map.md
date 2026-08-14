# Stage14/15 bound-attack map

`STATUS=AI_READABLE_DISCOVERY_INDEX`

This map inventories all **824** `result.md` files under Stage14 and Stage15. It is a discovery interface, not a replacement for the sources or audits.

## Purpose

Use this map before claiming a strongest bound, missing lower bound, new mechanism, or OPEN_GATE. Search the JSONL by population, target, method family, structural signature, failure reason, and missing input; then read every candidate source selected for reuse or rejection.

## Generated artifacts

- `docs/stage14-15-bound-attack-ledger/manifest.json` — shard manifest for the complete ledger.
- `docs/stage14-15-bound-attack-ledger/part-*.jsonl` — one record for every result file, split for GitHub/API readability.
- `docs/stage14-15-bound-coverage.json` — aggregate coverage and review queue counts.
- `scripts/build_stage14_15_attack_map.py` — deterministic regenerator.

## Coverage summary

- Stage14 records: 708
- Stage15 records: 116
- Records requiring targeted review: 380
- Records with a neighboring `audit.md`: 0

### Method families

| Family | Records |
|---|---:|
| `NEGATIVE_ROUTE_CERTIFICATE` | 745 |
| `DIVISOR_RECONSTRUCTION` | 656 |
| `LOCAL_CONGRUENCE_VALUATION` | 498 |
| `GAUSSIAN_SQUARECLASS` | 478 |
| `FINITE_CENSUS_REGRESSION` | 449 |
| `LITERATURE_ADAPTER` | 346 |
| `SIEVE_CHARACTER_SUM` | 337 |
| `PARAMETRIC_CONSTRUCTION` | 256 |
| `ELLIPTIC_GENUS_ONE` | 228 |
| `LATTICE_GEOMETRY` | 149 |
| `K3_SURFACE_COVER` | 60 |
| `INCIDENCE_GRAPH` | 21 |

### Structural signatures

| Signature | Records |
|---|---:|
| `INTEGRAL_SPACE_DIAGONAL` | 591 |
| `PAIRED_NORMS` | 512 |
| `DIRECTIONAL_CHAMBER` | 485 |
| `MOVING_MODULUS` | 242 |
| `PYTHAGOREAN_FACE` | 177 |
| `EXACTLY_TWO_FACES` | 158 |
| `OVERLAP_INTERSECTION` | 148 |
| `COMMON_CORE` | 92 |
| `UNCLASSIFIED` | 39 |
| `THREE_FACES_EULER` | 19 |

## Required consumer procedure

1. Filter the ledger for the target population and bound direction.
2. Search both direct terminology and structural signatures.
3. Inspect accepted candidates and every plausible rejected candidate in the source.
4. Check population, cutoff, multiplicity, measure, quantifier order, and audit status.
5. Review LOW/UNCLASSIFIED/PARTIAL/BLOCKED entries before asserting no compatible route exists.
6. Record accepted/rejected attack IDs in the Stage21–28 discovery ledger.

## Interpretation boundary

The ledger answers *what repository artifacts appear to have attacked which structures, and where they stopped*. It cannot prove that no genuinely new viewpoint exists. `UNCLASSIFIED` and `review_required=true` are explicit invitations for targeted AI reading.

## Reproduction

```bash
python3 scripts/build_stage14_15_attack_map.py --repo . --ref HEAD --out docs
```
