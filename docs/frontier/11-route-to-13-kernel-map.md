# Stage29 historical routes ↔ frozen active kernels

Status: **Stage29 CLOSED; route colors frozen as provenance.**

This sheet answers one question: **which of the 13 frozen restart kernels now owns the surviving work of each of the 11 historical Stage29 routes?**

Authority:
- `stages/stage29/29-16/route-portfolio.json`
- `stages/stage29/29-16/active-kernel-ledger.json`
- `stages/stage29/29-16/audit.md`
- `stages/stage29/29-17/final-handoff.json`

Important: 11 route labels are mathematical/provenance surfaces. After compression they are **not 11 independent execution owners**. There are 9 current scheduling-owner routes because `G10-K3-SIGN` and `J12-JOINT-V4` are merged-support routes.

## One-sheet map

| Historical route | Frozen color | Portfolio role after 29-16 | Active kernel(s) | Meaning |
|---|---|---|---|---|
| `G10-FULL-ENDPOINT` | AMBER | active independent | `K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT` | full physical endpoint needs an effective rational-point theorem; another sparsity bound is insufficient |
| `G10-LOWGENUS-PICARD` | AMBER | active support | `K16-C2-LOWGENUS-PICARD-PRODUCTION` | finite carrier production remains; lacks all-rational-point coverage theorem |
| `G10-K3-SIGN` | AMBER | **merged support**; execution owner `Q11-BRAUER` | `K16-C2-BRAUER-EXPLICIT-CHAIN` | live K3 work is the `K_c` two-primary Brauer presentation/lift adapter; K3 quotient emptiness is not standalone |
| `Q11-CAMPEDELLI` | AMBER | active independent + shared Brauer support | `K16-C3-CAMPEDELLI-UNIFORM-TORSOR`; `K16-C2-BRAUER-EXPLICIT-CHAIN` | torsor theorem is independent; `CAMP4` lives inside shared Brauer DAG |
| `Q11-BEAUVILLE` | AMBER | active independent, compressed to one-step descent | `K16-C3-BEAUVILLE-ONE-STEP-DESCENT` | second/iterated descent is not a separate stronger route; open-twist one-step arithmetic remains |
| `Q11-MODULAR` | AMBER | active support | `K16-C2-MODULAR-S4-ACTION` | `MOD1C/MOD1D` closed; only exact action/cocycle adapter remains active |
| `Q11-BRAUER` | AMBER | active independent; primary computation owner | `K16-C2-BRAUER-EXPLICIT-CHAIN`; `K16-C3-QWEB-CLIFFORD-OBSTRUCTION` | physical-open/two-primary explicit computation + independent Clifford theorem possibility |
| `J12-JOINT-V4` | AMBER | **merged support**, no unique active kernel | `K16-C3-TERMINAL-P-OVER-M3` | exact V4 structure retained; bounded ADE child dormant; no separate actionable residual survives |
| `J12-LOCAL-SQUARECLASS` | AMBER | active independent | `K16-C3-M3-LOCAL-TO-GLOBAL` | local data are explicit; only load-bearing wall is transfer to exact `M3` physical measure |
| `J12-PARAMETRIC` | AMBER | active independent, multi-kernel | `K16-C3-PESCH-EXPONENT-ONE`; `K16-C3-MOVING-FIBER-ARITHMETIC`; `K16-C3-EXT-C-PRIMITIVE-DIVISOR`; `K16-C2-EXT-E-INTEGRAL-CERTIFICATION` | Pesch E1 is the primary narrow global-coverage theorem target; others are alternate moving/thin-family tracks |
| `J12-POP-INTERACTION` | GREEN | certified theorem progress + terminal frontier | `K16-C3-TERMINAL-P-OVER-M3` | GREEN credits exact survival theorems only; literal `P/M3` remains unknown |

## Kernel-centric reverse map

```text
K16-C2-LOWGENUS-PICARD-PRODUCTION
  <- G10-LOWGENUS-PICARD

K16-C2-MODULAR-S4-ACTION
  <- Q11-MODULAR

K16-C2-BRAUER-EXPLICIT-CHAIN
  <- Q11-BRAUER [execution owner]
  <- G10-K3-SIGN [merged support]
  <- Q11-CAMPEDELLI [shared CAMP4 support]

K16-C2-EXT-E-INTEGRAL-CERTIFICATION
  <- J12-PARAMETRIC

K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT
  <- G10-FULL-ENDPOINT

K16-C3-CAMPEDELLI-UNIFORM-TORSOR
  <- Q11-CAMPEDELLI

K16-C3-BEAUVILLE-ONE-STEP-DESCENT
  <- Q11-BEAUVILLE

K16-C3-QWEB-CLIFFORD-OBSTRUCTION
  <- Q11-BRAUER

K16-C3-M3-LOCAL-TO-GLOBAL
  <- J12-LOCAL-SQUARECLASS

K16-C3-PESCH-EXPONENT-ONE
  <- J12-PARAMETRIC

K16-C3-MOVING-FIBER-ARITHMETIC
  <- J12-PARAMETRIC

K16-C3-EXT-C-PRIMITIVE-DIVISOR
  <- J12-PARAMETRIC

K16-C3-TERMINAL-P-OVER-M3
  <- J12-POP-INTERACTION
  <- J12-JOINT-V4 [merged support]
```

## Compression accounting

```text
historical route labels         = 11
frozen colors                   = 1 GREEN / 10 AMBER / 0 RED
current scheduling-owner routes = 9
merged-support routes           = 2
active source receivers         = 24
compressed active kernels       = 13
  Class 2 kernels               = 4
  Class 3 kernels               = 9
```

The two support merges are scheduling compression only. They do not delete routes, change route colors, or assert mathematical/statistical independence among the remaining nine owners.

## Unique-route reactivation note

`J12-JOINT-V4` regains its own unique active kernel only if a genuinely joint third-face/space theorem appears that is not equivalent to the existing local-transfer or terminal `P/M3` frontier.

`G10-K3-SIGN` regains a separate execution owner only if a K3-specific arithmetic mechanism appears that is not already part of the physical-open/two-primary Brauer DAG.