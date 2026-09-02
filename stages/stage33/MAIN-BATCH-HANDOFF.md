# Stage33 MAIN batch handoff

status: UNPROMOTED_DELTA_ORDER4_PULLBACK_GAP_BLOCKED_ON_TWO_ROWS
base_merge: #1483
pr: #1485
branch: stage33-post1483-order4-pullback-two-row-extraction
merge: FORBIDDEN
heavy_compute: FORBIDDEN

MAIN-STATE remains V11. No mathematical state promotion occurred after the V11 sync, so the mandatory EMPTY reset law has not fired.

## Current unpromoted delta

The semantic J2 order-4 route requires BigK pullback rows `[2,4,9,10,20,35,39,47,49,67]`.

Row `39` is already recovered exactly by retained symmetry transport:
- certificate: `stages/stage33/33-12/j2-order4-row39-retained-symmetry-transport-v11.json`
- canonical SHA256: `a83d558fc96822d9b8a01512e7d1afa3cf9db0958718325a27fddb32ba753604`
- mechanism: pinned BigK `35 -> 39` under upstream `sign_a3`, matched by retained Stage32 generator-6 full-surface class transport `53 -> 57`; certified row35 is class53, hence row39 is class57.

Successor exact row availability leaves exactly `[20,67]` unresolved:
- certificate: `stages/stage33/33-12/j2-order4-retained-pullback-row-availability-v12.json`
- canonical SHA256: `61a8523c8ca788c58aa0c3732694406230e4fd11afbe67a2d63d5543b0dda9ec`

## New #1485 static geometric-route audit

A genuinely new static source-locked route was checked without executing Magma and without target-compatibility inference:
- certificate: `stages/stage33/33-12/j2-order4-row20-row67-static-geometric-route-audit-v15.json`
- canonical SHA256: `dfb7176cc59272896971a3f06964ddd9456db7935e0dc0a71213f7767664feb3`
- source head audited: `65a9f472c7db174330fa628b107a2510dbc39c95`

Exact narrowing:
- BigK row `20` is `C1sK[20]`, the last of the eight branch conics (BigK rows `13..20`). The explicit sign/coordinate symmetries keep this separate eight-element branch-conic orbit closed.
- retained six-support exact pullbacks are BigK rows `[26,35,42,47,49,52]`, so the row20 branch-conic orbit has no retained six-support anchor. The row39-style anchor transport therefore does not close row20.
- the pinned full-surface source has the matching branch-conic formula, but a complete pullback also includes exceptional-divisor terms over flattened singular points; the exact retained indices of those terms require the runtime singular-point ordering/incidence data.
- BigK uses known curves first and then the 12 exceptional divisors represented by `ptsK`; hence row `67` is the fifth exceptional coordinate, `ptsK[5]`.
- `ptsK` itself is constructed as `Points(SingularSubscheme(K))`, and the exceptional part of `permsK` uses runtime `Position(..., ptsK, ...)`. The pinned source does not statically serialize which geometric singular point occupies `ptsK[5]`.
- narrow repository searches found no distinct retained point-order/incidence serialization under the new `SingularSubscheme(S)` / `flattened` route identifiers.

Consequently rows `[20,67]` are still unresolved, but the static symmetry/geometric route is now exhausted to a sharper blocker: missing runtime singular-point ordering/incidence data. No named J2 order-4 source coordinate is materialized. Kummer standard columns remain `0`; Stage33 progress remains `6/11`; Stage33-12 remains OPEN. Keep `NO_INFERENCE`.

## Anti-repeat locks — do not redo these searches unchanged

1. Retained Stage32 origin artifact was already audited as a possible hidden pullback source.
   - certificate: `stages/stage33/33-12/j2-order4-retained-stage32-pullback-source-audit-v13.json`
   - canonical SHA256: `1cc6639578e8f054e90f42297a2e364a56c87363dfa0aa2c18d45d7341685ff2`
   - immutable Actions artifact: `9588229672`; observed ZIP SHA256 exactly matched retained lock `6e4e6e5350717296f0e76e5c972e945b72a61d32e039718a535e245826b5b159`.
   - artifact contains only `d16-aut-action.json`, `d16-aut-prefix256-bundle.txt`, `d16-exact`, `d16-hperp.txt`, `packet-manifest.json`.
   - raw-byte scan found zero occurrences of `BigK`, `MatBigKtoBig`, `preimages`, `ptsK`, `C1sK`, or `projection`.
   - consequence: this retained artifact does not serialize ordered Big/BigK pullback rows 20 or 67.
   - reopen only if new independent evidence identifies a concrete encoded incidence/pullback table inside or derived from this artifact.

2. The pinned upstream exact source itself was already inspected for retained row serialization.
   - source: `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd:Cuboids/cuboids.magma`
   - source blob SHA1: `0422b69847f2afb97cb7b3ed02ebef91279f61b1`
   - raw SHA256: `5dc3ae961d872ff96420385880edf0f4225a12d3f906c614e1ccd2220399ce89`
   - certificate: `stages/stage33/33-12/j2-order4-pinned-upstream-pullback-row-serialization-audit-v14.json`
   - canonical SHA256: `aabdfd71306de99cae202d838be20144a0a001743d79fb5d1608ce91afc43562`
   - exact source constructs `preimages` and `MatBigKtoBig` at runtime and checks `Matrix(PicbasrepsK)*MatBigKtoBig*MatqPic eq MatKtoS`.
   - rows 20/67 are not retained there as literal/serialized exact vectors; narrow repo/history searches under these known identifiers found no alternate retained serialization.
   - this is an evidence-availability negative result, not a theorem that no serialization can exist elsewhere.
   - reopen the same search only if a new concrete source/path/identifier is supplied; otherwise do not repeat it.

Do not reopen qPic, Smith, sign census, S3 candidate enumeration, the Stage32 retained-marking origin artifact, or infer rows 20/67 from target compatibility merely because the next batch lacks context. Their current premises have not changed.

## Next exact action

The remaining direct route is now explicit: obtain a genuinely new retained artifact that locks the missing singular-point ordering/incidences, or obtain explicit authorization for a narrow execution of the pinned upstream source solely to emit `MatBigKtoBig` rows `[20,67]`. Do not launch that execution under the current `heavy_compute: FORBIDDEN` boundary. Until one of those premises changes, stop at this exact blocker rather than repeating the negative/static searches above.
