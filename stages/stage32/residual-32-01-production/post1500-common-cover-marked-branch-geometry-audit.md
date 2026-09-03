# Post-1500 common-cover / marked-branch geometry audit

## Scope

This is a negative closed-world audit under the Stage32 O210 authority inherited from merged PR #1500. It does **not** assert that no geometric theorem exists. It records only that the presently admitted repository evidence does not derive a new common-cover / marked-branch / ramification constraint that excludes the required Rosati value.

## Authority and target

- active fixed overlap: `O210`
- exact repaired value: `sigma(Gamma) = 1204`
- exact repaired Rosati lattice value: `Q(T) = 602`
- `O210` remains OPEN at the audited nonexclusion boundary
- `O212+` remains blocked behind `O210`
- this lane asks only whether the already-admitted common-cover / marked-branch / ramification information itself forces a strict Rosati loss or otherwise excludes `sigma(Gamma)=1204 / Q(T)=602`

No `O211` authority is created by this audit.

## Admitted input and source lock

1. live authority: `stages/stage32/controller.json`; its relevant content is read and checked by the dedicated verifier;
2. immutable repaired mathematical source: `stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md`, Git blob SHA-1 `b0ea281eae453929c292059a919bc1f68b3080b3`.

The repaired source-note certifies the facts used by this lane:

- `Gamma^2 = 15806`;
- `sigma(Gamma) = 1204`;
- `Q(T) = 602`;
- the retained positive-definite `D4 direct-sum D4` trace lattice represents `Q=602`;
- the retained operator constraint is `T^dagger*T <= 8505`, and it does not exclude `Q=602`;
- the retained O210 Weierstrass collision estimate is only `delta_Gamma >= 1924`, while the corrected required value is `7984`, so it also does not exclude the carrier.

This audit does **not** use the unsupported `376` pair-operator value or `W=128 -> p>=32` statement from the failed #1501 head.

## Geometry-lane audit

The admitted repaired authority identifies the remaining mechanism only at the level of a search target: a genuinely geometric property of a correspondence arising from the common-cover / marked-branch geometry would have to force `sigma(Gamma)=0` or otherwise exclude the exact required value `sigma(Gamma)=1204 / Q(T)=602`.

The admitted material contains no source-locked theorem, local intersection table, ramification-multiplicity computation, or contribution-identification rule that turns the shared-cover / marked-branch / ramification data into such an exclusion. In particular, the implication

`shared cover + marked branch/ramification => strict Rosati loss`

is not derivable from the currently admitted closed-world premises.

This is an evidence gap, not a proof that the implication is false.

## Result

`AUDITED_NEGATIVE`

- no new geometric exclusion of `sigma(Gamma)=1204 / Q(T)=602` is certified;
- the authority remains at `O210`;
- `O210` remains open;
- `O212+` remains unauthorized;
- no effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows.

## Re-entry condition

This lane may be reopened only when at least one newly admitted, source-locked artifact supplies one of the following:

1. a common-cover / branch / ramification to Rosati-entry coupling theorem or exact certificate;
2. a local intersection / multiplicity / ramification calculation forcing a strict Rosati loss; or
3. a certified identification or collision among contributions previously counted independently that excludes the required value.

Absent one of these, repeating the bounded D4/operator/Weierstrass nonexclusion checks or merely restating that the pair-maps share a cover is an anti-loop violation. This audit does not authorize broader retained-asset research or resumption of `O212+`.
