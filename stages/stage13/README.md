# Stage13 — active structural analysis

Current state:

```text
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=ACTIVE
STAGE13_3A=COMPLETE
STAGE13_3B=COMPLETE
NEXT=Stage13-3c
```

## Active organization

```text
stages/stage13/roadmap.md
stages/stage13/policy.md
stages/stage13/initial/definition.md
stages/stage13/initial/structural-decomposition.md
stages/stage13/main.md
stages/stage13/scripts/13-3/raw_incidence.py
stages/stage13/scripts/13-3/geometric_chamber.py
stages/stage13/data/13-3/raw_incidence_report.json
stages/stage13/data/13-3/geometric_chamber_report.json
```

`main.md` is the canonical living mathematical source. The completed Stage13-1/2 initial files remain as provenance; active mathematics is edited in `main.md`.

Stage13-3a established, by complete finite enumeration through the audited cutoffs, that the near `2:1:1` shape is already present in the raw face incidences before the exactly-one overlap sieve. The overlap correction is tiny at `B=100000`; this is a finite result, not an asymptotic theorem.

Stage13-3b then isolated the canonical size-order / archimedean mechanism. Pure relabelling or full positive-octant symmetry gives `1:1:1`, but on the chamber `0<a<b<c` the exact one-face Gelfand--Leray weights satisfy `w_ab>w_ac>w_bc`. Their chamber integrals give a `bc`-normalized geometric ratio approximately `2.4317:1.1158:1`, which captures most of the finite departure from `1:1:1` but overstates the observed raw ratio `2.0660:1.0607:1`. Thus geometry is a strong leading mechanism, not yet the complete arithmetic explanation.

The next mathematical step is Stage13-3c: split raw incidence by parity / 2-adic class and test whether this arithmetic layer flattens the geometric ratio toward the observed one.

## File rule

Stage13 uses one living mathematical source. Corrections go directly into `main.md`; Git/PR history records earlier versions.

Stage13-specific support assets should use the stage/task in the path, with short functional filenames:

```text
stages/stage13/scripts/13-3/<purpose>.py
stages/stage13/data/13-3/<purpose>.json
```

Do not repeat long `stage13_...` suffixes in filenames when the directory already supplies that context.

Generated external-review bundles are created only on demand.
