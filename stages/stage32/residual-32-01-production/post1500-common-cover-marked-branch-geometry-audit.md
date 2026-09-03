# Post-1500 common-cover / marked-branch geometry audit

## Scope

This is a negative closed-world audit under the Stage32 authority inherited from PR #1500. It does **not** assert that no geometric theorem exists. It records only that the presently admitted repository evidence does not derive the required strict Rosati improvement.

## Authority and target

- authority checkpoint: `O211`
- current bound: `sigma(Gamma) <= 1204`
- current extremal value: `Q = 602`
- required improvement: `sigma(Gamma) < 1204`, equivalently `Q < 602`
- `O212+` remains prohibited unless that strict improvement is certified

## Admitted input

- `stages/stage32/controller.json`
- `stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md`

The post-1500 source note already certifies that the current D4/PSD constraints, the repaired exact pair-operator upper bound (`376`, from degrees `105` and `81`), and the Weierstrass estimate (`W=128`, hence `p>=32`) are all compatible with `Q=602`. Re-running those inequalities is therefore outside this lane.

## Geometry-lane audit

The admitted material identifies the only relevant next mechanism: the two pair-maps originate from the same cover and carry marked branch/ramification structure. However, the admitted input contains no theorem, local intersection table, ramification-multiplicity computation, or contribution-identification rule that maps those shared geometric data to a strict decrease of a Rosati off-diagonal contribution.

Consequently, the implication

`shared cover + marked branch/ramification => Q < 602`

is **not derivable from the current closed-world premises**. This is an evidence gap, not a proof that such an implication is false.

## Result

`AUDITED_NEGATIVE`

- no certified strict `sigma` improvement
- `sigma(Gamma)` authority remains `1204`
- `Q` remains `602`
- `O212+` remains unauthorized

## Re-entry condition

This lane may be reopened only when at least one newly admitted artifact supplies one of the following:

1. a shared-cover / branch / ramification -> Rosati-entry coupling theorem or exact certificate;
2. a local intersection / multiplicity / ramification calculation forcing a strict loss in at least one off-diagonal contribution; or
3. a certified identification or collision among contributions previously counted independently.

Absent one of these, repeating D4/PSD/operator/Weierstrass arithmetic is an anti-loop violation. This audit does not authorize broader retained-asset research or resumption of `O212+`.
