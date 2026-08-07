# Stage12-N1-2 repaired proof review manifest R02

> **BUNDLE_ID:** `PC-N1-2-REPAIRED-PROOF-20260807-R02`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3d`
>
> **SOURCE_SNAPSHOT_COMMIT:** `08a3bc0b8428f9c620269da9b488e8b849cf909c`
>
> **SOURCE_LEDGER_SHA256:** `26528cd336fe4b6ce5bc70bdca368ad605f29f711bec71e34a6427d98b3560dc`
>
> **LAST_SOURCE_DOCUMENT:** `docs/stage12-n1-2-final-r02.md`
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT`
>
> **REVIEW_PAGE:** `review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html`

## Mandatory handshake

Before mathematical review, reproduce exactly:

```text
BUNDLE_ID=PC-N1-2-REPAIRED-PROOF-20260807-R02
COMPLETED_THROUGH=Stage12-N1-3d
SOURCE_SNAPSHOT_COMMIT=08a3bc0b8428f9c620269da9b488e8b849cf909c
SOURCE_LEDGER_SHA256=26528cd336fe4b6ce5bc70bdca368ad605f29f711bec71e34a6427d98b3560dc
LAST_SOURCE_DOCUMENT=docs/stage12-n1-2-final-r02.md
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT
END_OF_BUNDLE=PC-N1-2-REPAIRED-PROOF-20260807-R02
```

If any value differs, return `STALE_SOURCE`.

## Review target

Review only the theorem candidate for the definition-sheet primitive oriented count:

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3.
\]

Do not infer a perfect-cuboid existence claim, canonical count, or exact-one-face asymptotic.

## Immutable source ledger

The source snapshot contains the following four documents.

| path | Git blob SHA |
|---|---|
| `docs/stage12-n1-3d-definition-sheet.md` | `b44f76a890363708d6274d14b7f7154894debc7b` |
| `docs/stage12-n1-3d-constant-sheet.md` | `3428f220c35c3625589dc44abf55819b48109631` |
| `docs/stage12-n1-3d-selberg-delange-reference-lock.md` | `23f887107b0babaadfcf6d6dc2e4255921c3651d` |
| `docs/stage12-n1-2-final-r02.md` | `e343182e82d9ecacf844fa7e508662749d43b55b` |

Pinned links:

1. `https://github.com/fizawa460-bit/perfect-cuboid-game/blob/08a3bc0b8428f9c620269da9b488e8b849cf909c/docs/stage12-n1-3d-definition-sheet.md`
2. `https://github.com/fizawa460-bit/perfect-cuboid-game/blob/08a3bc0b8428f9c620269da9b488e8b849cf909c/docs/stage12-n1-3d-constant-sheet.md`
3. `https://github.com/fizawa460-bit/perfect-cuboid-game/blob/08a3bc0b8428f9c620269da9b488e8b849cf909c/docs/stage12-n1-3d-selberg-delange-reference-lock.md`
4. `https://github.com/fizawa460-bit/perfect-cuboid-game/blob/08a3bc0b8428f9c620269da9b488e8b849cf909c/docs/stage12-n1-2-final-r02.md`

The physical HTML repeats all definitions, constants, reference assumptions, and the repaired proof chain, so the pinned links are integrity references rather than prerequisites for reading.

## Repairs represented

```text
MAJOR_01=CLOSED_BY_STAGE12_N1_3A
MAJOR_02=CLOSED_BY_STAGE12_N1_3B
MAJOR_03=CLOSED_BY_STAGE12_N1_3C_G
MAJOR_04=CLOSED_BY_STAGE12_N1_3D
CLARIFICATION_01=CLOSED_BY_STAGE12_N1_3D_REFERENCE_LOCK
MINOR_01=CORRECTED
MINOR_02=CLOSED_BY_SELF_CONTAINED_R02
```

## Required adversarial questions

1. Does the definition sheet unambiguously define raw, primitive, oriented, parity, height, and multiplicity conventions?
2. Is the Möbius relation an exact object-level identity and is the primitive-first formula endpoint-correct?
3. Does Stage12-N1-3b's `X^(1/2)` pointwise remainder yield the stated retained-region averaged saving?
4. Do the `z=1` and `z=2` instances satisfy the locked Selberg--Delange hypotheses and is arbitrary fixed log-power saving sufficient after all box losses?
5. Is the parity-weighted coprime rectangle factorization exact, including the 2-adic local factor?
6. Is `C_lambda^(0)=8 eta/pi^2` correct prime by prime?
7. Does the radial Stieltjes calculation retain the kernel, orientation, parity, arc, and lower-log boundary terms and produce exactly `1/12`?
8. Are `kappa`, `eta`, and `eta=pi*kappa` independently recomputable from the constant sheet?
9. Are all `-1`, floor, shallow, annulus, diagonal, and fixed-height remainder terms `o(B(log B)^3)`?
10. Is any unproved fixed-`(b,c)` anisotropic kernel lemma still used? The intended answer is no: it is superseded, not assumed.

## Review output

Return one of:

- `CLOSED`: no material gap remains and theorem hypotheses are itemized.
- `REPAIRABLE`: explicit local gap with a stated repair lemma.
- `OPEN`: central unsupported or false implication.
- `STALE_SOURCE`: handshake mismatch.
- `UNREADABLE_SOURCE`: physical bundle truncation or missing end marker.

A generic plausibility statement is not a completed review.