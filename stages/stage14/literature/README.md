# Stage14 literature radar

This directory is a cross-track theorem/reference radar for Stage14. It is not a new proof track and has no stage-number progression of its own.

## Mission

Continuously read the current Stage14 frontiers (`14-4`, `14-s`, `14-t`, and when relevant `14-e`) and collect external literature that could shorten, close, or redirect one of those exact proof gaps.

The radar must follow the repository's current mathematics, not a fixed literature roadmap. When a track moves, its literature page should be updated to the new frontier.

## Directory contract

```text
stages/stage14/literature/
  README.md          rules and current routing
  14-4.md            Kummer/K3/low-degree-curve/height references
  14-s.md            elliptic-family/Selmer/rank/regulator/small-point references
  14-t.md            triple/Humbert-Edge/thin-cover/uniformity references
  cross-track.md     results genuinely useful to 2+ tracks
```

Do not create one file per paper. Each track gets one short, scan-friendly ledger.

## Entry format

Every reference entry must contain only the information needed by the working track:

```text
### Short citation
- Link: stable paper/preprint/publisher URL
- Theorem: exact theorem/proposition/corollary number when available
- Gives: one-sentence mathematical payload
- Stage14 hook: exact current lemma/equation/obstruction it could address
- Fit: DIRECT / NEAR / BLOCKED / BACKGROUND
- Missing: if not DIRECT, the precise hypothesis or translation still missing
- Checked: YYYY-MM-DD
```

A bare link without a theorem-level note is allowed only in an `INBOX` subsection and must eventually be promoted or deleted.

## Readability rules

1. **Track-first, not bibliography-first.** A `14-s` worker should be able to open `14-s.md` and ignore the rest.
2. **Current frontier first.** Put references closest to the current `NEXT=` target at the top.
3. **No paper summaries.** Record the theorem that might be used, not an abstract rewrite.
4. **No citation inflation.** Ten weakly related papers are worse than one theorem with a verified hypothesis map.
5. **Negative results are valuable.** If a famous theorem does not apply, keep it as `BLOCKED` and state the exact failed hypothesis so later agents do not rediscover the same dead end.
6. **Distinguish arithmetic height from physical height.** Never claim applicability until the paper's height is translated to the Stage14 physical cutoff `d<=B` or the relevant `M`/canonical height.
7. **Distinguish fixed fiber from moving family.** A theorem uniform on one curve is not automatically uniform in the Stage14 parameter.
8. **No conjecture laundering.** BSD, Lang/Vojta, uniformity conjectures, perfect-cuboid nonexistence, etc. must be labelled explicitly as conditional.
9. **Prefer primary sources.** Original paper/preprint or authoritative monograph; secondary notes only for orientation.
10. **Stable links only.** Prefer DOI, arXiv, journal, author/institution repository. Avoid search-result URLs.

## Cross-track routing

A paper belongs in `cross-track.md` only if the same theorem has a concrete hook in at least two active tracks. Otherwise duplicate a short pointer such as `See cross-track: <citation>` rather than copying the full note.

Current routing priorities:

```text
14-4  -> Q-rational M-degree-4 bisections; rational curves on Kummer/K3; big-and-nef height
14-s  -> first-small-point/generator height; regulator; rank jumps in elliptic families
14-t  -> WAITING on concrete 14-4 bisections; meanwhile third-square double covers, Humbert-Edge quotients, uniform rational-point bounds
14-e  -> low priority unless a new ambient theorem directly sharpens a Stage14 comparison
```

## What the radar must not do

- Do not change Stage14 theorem statements merely because a paper looks relevant.
- Do not open a new mathematical lane without identifying which existing obstruction it removes.
- Do not rerun finite experiments already owned by another track.
- Do not treat a literature claim as imported until hypotheses have been checked against repository notation.
- Do not count `NEAR`, `BLOCKED`, or `BACKGROUND` as mathematical progress.

## Promotion rule

When an entry becomes `DIRECT`, the literature radar should point the owning track to it. The owning track, not this directory, performs the proof import and changes theorem status.

The radar can therefore stay active while `14-t` itself is waiting.
