# CHECK-12 — degree-5 slack-0 maps: all 6090 built and checked (2026-11-15)

Scope: `route_F_compute_request_12_20261115.md` (build all degree-5 slack-0 maps with critical
values in B = {0, oo, +-1, +-i}). Done on the local PC; no upper-model use.
Result files are in `f02/`. Numerical search plus independent checks — this is not a proof of completeness.
Completeness is witnessed by the Hurwitz counts in `hurwitz5.json`.

## Provenance

- `f02/build_maps5.py` was written by an **external free AI (ChatGPT)** at the user's request.
  Claude read the whole file before running it: no network access and no subprocess calls.
  The original is kept as `f02/maps5work/build_maps5.orig.py` (local only, not committed);
  sha256 of the original is `10dbca94301c7b1e3cae99be7604d5885055effd4e565b7a396d6340ef372fa2`.
- Claude patched two places (both marked in the source):
  1. **Bug fix (`signature_set`)**: the duplicate-prefilter key sorted mp coordinates directly.
     On maps with symmetry, ties that are exact in theory are perturbed at 1e-100, so the sort
     order flipped and equivalent maps got different keys. The prefilter then never called the
     exact test, so duplicates were accepted as new maps. The builder reported "complete" while
     maps were still missing. The fix sorts by coordinates rounded to 7 digits.
  2. State precision: P and Q are now written with 60 digits (was 40).
- New scripts by Claude: `f02/refine5.py` (re-refine to dps 110), `f02/expand5.py`
  (orbit expansion and checks) and `f02/compare_maps.py` (independent bijection check).

## Method

1. **Octahedral reduction.** The 24 rotations h of the octahedron permute B, so h∘p is a
   slack-0 map of the permuted type. The 90 types fall into 7 orbits. Only these
   representatives were searched: 002222, 020222, 011222, 021122, 021212, 111122, 111212
   (6 + 6 + 40 + 40 + 40 + 240 + 240 = 612 maps).
2. **Search** (`build_maps5.py`, 10 workers): random starts, damped Newton, mpmath refinement.
   - Run 1: about 3 h, with the bug.
   - Run 2: about 26 min, after the fix. The start-up dedupe removed 2 duplicates in 111122 and
     6 in 111212; the search then found the 8 missing maps.
3. **Refinement** (`refine5.py`): Newton at dps 110 from the stored values.
   - Worst residual 1.2e-108.
   - Worst Jacobian condition number 3.8e8. This is why 40-digit storage was marginal against
     the 1e-32 identity test.
4. **Expansion** (`expand5.py`): all 24·612 = 14688 images h∘p were made and deduplicated
   within each type (signature prefilter plus exact coefficient identity after a source Möbius
   map). Every unique map was rechecked: Wronskian roots equal the critical points, and the
   values are the prescribed points of B.

## Results

| Check | Result |
|---|---|
| Per-type count vs `hurwitz5.json` | **90/90 types match, total 6090/6090** (`f02/expand5.report.json`) |
| Worst critical-point/value residual | 4.1e-93 |
| Independent recount (`compare_maps.py`, critical data recomputed from P,Q in `maps5.json`) | 6090 distinct, 0 duplicates, 0 differences |
| Degree-4 reproduction (fixed builder dedupe vs existing `maps4.json`) | see below |

Degree 4:
- The existing `f02/maps4.json` has 680 maps with 0 internal duplicates.
- A full rebuild with `build_maps5.py 4` (unpatched signature, about 34 min) reported 680/680.
- The rebuild actually contained 3 hidden duplicates, so it had only 677 distinct maps.
- All 677 match maps in `maps4.json`. The 3 missing maps are one each in 111102, 111120 and
  111210.
- This confirms the bug independently, and confirms `maps4.json` (earlier work) is sound.

Degree 3 (60) was not re-run separately.

## Files committed

- `f02/maps5.json`: flat list `[{datum,P,Q}]`, 6090 maps, 40 digits, same shape as `maps4.json`.
  sha256 `6ca6653fa04a29a9ee4f8b30f98e4e62e4222aeea5f83ba7d9eb8c145a55acdf`.
- `f02/expand5.report.json`
- Not committed because `f02/.gitignore` excludes `*.jsonl`, as with `maps4.jsonl`. These
  files stay local in `f02/`:
  - `maps5.jsonl`, the maps grouped by type;
  - `maps5reps.state.jsonl`, the 612 representatives with critical data at 100 digits.
    Running `expand5.py` on it regenerates everything.
  - Critical data can also be recomputed from `maps5.json` alone; `compare_maps.py` does this.
- `f02/maps5logs/`: build runs 1 and 2, the expansion log, and the degree-4 rebuild log.
- Scripts: `build_maps5.py` (patched), `refine5.py`, `expand5.py`, `compare_maps.py`.

## Not done

- **Monodromy check.** The maps were not matched one-to-one to the monodromy classes; the
  counts per type were used instead. This was optional in request 12.
- **Next step.** Use `maps5.json` to extend the problem-window census (`checks9/census9.py`)
  and the band data to degree 5.
