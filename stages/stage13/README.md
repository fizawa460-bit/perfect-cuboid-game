# Stage13 — active structural analysis

Current state:

```text
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=ACTIVE
```

## Active organization

```text
stages/stage13/roadmap.md
stages/stage13/policy.md
stages/stage13/initial/definition.md
stages/stage13/initial/structural-decomposition.md
stages/stage13/main.md   # canonical mathematical working file once bootstrapped
```

Task 13-1 and 13-2 are completed initial sources. The next mathematical step is to bootstrap `main.md` by importing their active content as §1 and §2, then begin §3 (origin of the leading `2`).

## File rule

Stage13 uses one living mathematical source. Corrections go directly into `main.md`; Git/PR history records earlier versions.

Stage13-specific support assets should use the stage/task in the path, with short functional filenames:

```text
stages/stage13/scripts/13-3/<purpose>.py
stages/stage13/data/13-3/<purpose>.json
```

Do not repeat long `stage13_...` suffixes in filenames when the directory already supplies that context.

Generated external-review bundles are created only on demand.
