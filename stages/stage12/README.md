# Stage12 — frozen at R09

Stage12-N1-2 is complete and frozen at the R09 self-contained proof bundle.

## Active Stage12 files

```text
stages/stage12/final.md
stages/stage12/manifest-r09.md
review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html
```

- `final.md` is the canonical technical proof text for normal reading.
- `manifest-r09.md` records the frozen bundle identity, hashes, theorem scope, and provenance.
- the R09 HTML remains at top-level `review/` because it is the single Stage12 page intended for direct external distribution.

The frozen theorem scope is the bundle-defined primitive oriented count only:

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

This does not assert perfect-cuboid existence/nonexistence, a canonical-count asymptotic, an exact-one-face asymptotic, or a final `2:1:1` ratio.

Selberg--Delange remains an external published theorem-level input.

## Archive

Everything that is not part of the three active entry points is historical provenance:

```text
stages/stage12/archive/docs/
stages/stage12/archive/scripts/
stages/stage12/archive/data/
stages/stage12/archive/review/
stages/stage12/archive/workflows/
```

See `archive/INDEX.md` for the task-to-script/data map.

Historical scripts and workflows are preserved for provenance. They were written against the repository layout that existed at the time, so their internal path strings are not automatically rewritten during this organizational move. For exact historical reproduction, use the recorded freeze/provenance commits. If Stage12 is deliberately reopened, restore only the required workflow/script and update paths deliberately.

## Freeze policy

Stage12 is not reopened for routine Stage13 work or repeated AI review. Reopen only for a concrete mathematical error, explicit counterexample, genuine Stage13 dependency conflict, or publication editing need.
