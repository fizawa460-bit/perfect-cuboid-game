# Stage16-29 research overview — final closed-program state

Status: **Stage16-29 research program CLOSED; perfect-cuboid problem OPEN.**

This is the canonical human-readable overview of the completed Stage16-29 program. It answers three questions only: **what was done, what is closed at its stated scope, and what remains if research is restarted.** Detailed proof, audit and numerical provenance stays under `stages/`.

For reusable tools use [`arsenal/README.md`](arsenal/README.md). For the final Stage29 handoff use [`../stages/stage29/29-17/result.md`](../stages/stage29/29-17/result.md).

## 1. Population ladder and strongest certified state

Common physical convention:

```text
0 < a < b < c
gcd(a,b,c)=1
R=sqrt(a^2+b^2+c^2) <= B
```

- `M1`: exactly one integral face diagonal, no space condition.
- `N1`: exactly one integral face diagonal + integral space diagonal.
- `M2`: exactly two integral face diagonals, no space condition.
- `N2`: exactly two integral face diagonals + integral space diagonal.
- `M3`: all three face diagonals integral = primitive canonical Euler cuboids.
- `P`: all three face diagonals + integral space diagonal = perfect-cuboid endpoint.

| Population | Strongest certified global statement | Final status |
|---|---|---|
| `M1(B)` | `~ 3/(4*pi^2) B^2 log B` | asymptotic scale closed |
| `N1(B)` | `~ kappa/(24*pi) B(log B)^3`, `kappa>0` | asymptotic scale closed |
| `M2(B)` | `~ C_M2 B(log B)^5`, `C_M2>0` | asymptotic scale closed |
| `N2(B)` | `B^(1/4) << N2(B) <<_eps B^(1/2+eps)` | infinite, zero-density in `M2`; true exponent open |
| `M3(B)` | `liminf M3(B)/B^(1/3) >= 27/(40*pi^2)` and `M3(B) <<_eta B(log B)^(5-eta)` for fixed `eta<1/46` | infinite; true exponent/asymptotic open |
| `P(B)` | `P(B) <<_eps B^(1/2+eps)`; exact census zero through `B=10^9` | existence/nonexistence and `P/M3` open |

Main literal-survival facts:

```text
N1/M1 ~ (kappa*pi/18) (log B)^2/B -> 0

B^(-3/4)(log B)^(-5)
  << N2/M2
  <<_eps B^(-1/2+eps)(log B)^(-5)
  -> 0

M3/(M2+M3) -> 0

P/M3 = UNKNOWN
```

The earlier strata are therefore quantitatively thin. That does **not** imply endpoint emptiness.

## 2. What each Stage contributed

| Stage | Role | Durable result |
|---|---|---|
| **16** | `M1` baseline | one-face population `~ B^2 log B`; primitive/canonical physical contract frozen |
| **17** | `N1` baseline | exact `B(log B)^3` asymptotic; space condition zero-density after one face |
| **18** | `M2` baseline | exact `B(log B)^5` asymptotic |
| **19** | `N2` baseline | half-power upper, Gaussian/squareclass form, local zero-density mechanism |
| **20** | `M3` baseline | Euler K3 completion model, local blocker, log-saving upper |
| **21** | `16 -> 17` | intrinsic space cost `B^-1` with positive `(log B)^2` interaction after one face |
| **22** | `16 -> 18` | `M2/M1 ~ const*(log B)^4/B` |
| **23** | `17 -> 19` | second-face acquisition remains zero-density on already-space-integral host; no double charge |
| **24** | literal `18 -> 19` | `N2/M2 ->0` while `N2 -> infinity`; geometric/local/global mechanisms separated |
| **25** | combined `16 -> 19` | primitive `N2` lower families of order `B^(1/4)`; positive divergent face/space interaction |
| **26** | `18 -> 20` | Euler completion share tends to zero; two-parameter Saunderson raises lower scale to one-third |
| **27** | strict `N2` exponent reattack | current repo-native routes compressed; true exponent remains between quarter and half in power scale |
| **28** | `19` vs `20` bridge | common toric base/common physical polarization K3 comparison; branch and low-degree curve-spectrum differential isolated |
| **29** | direct endpoint synthesis | endpoint geometry, quotient/cover architecture, route portfolio, family exclusions, local/parametric/Brauer/modular attacks, final receiver compression |

## 3. Main condition-interaction picture

The conditions do not behave as independent random filters.

- One face -> space: polynomial cost `B^-1`, enhanced by `(log B)^2`.
- One face -> two faces: polynomial cost `B^-1`, compensated by `(log B)^4`.
- Two faces -> space: zero-density but infinite; two-face conditioning positively enhances space survival relative to ambient and one-face baselines.
- Two faces -> Euler: Euler share in the legal at-least-two-face host tends to zero.
- Stage19 vs Stage20: they are different degree-two K3 completions of the same two-face geometry, not a literal subset pair.

Stage28 put both K3s over

```text
Y = Bl_4(P1 x P1),  L=-K_Y,
M_sp^2=M_face^2=8.
```

with the first certified geometric differential

```text
Stage19 space cover      : 4 genus-0 branch components
Stage20 third-face cover : 2 genus-1 branch components
```

and the fixed-curve spectrum distinction

```text
Stage19 physical M-degree 4 rational curves : absent
Stage20 Saunderson physical M-degree         : 6
Stage19 physical M-degree 6 absence          : not proved
```

These are causal/geometric differences, not a proof ordering the full populations.

## 4. Stage29 endpoint synthesis

Stage29 organized the endpoint simultaneously through:

- the full four-quadric cuboid surface;
- the residual joint `V4` completion over the two-face base;
- the degree-64 seven-line sign/Kummer cover of `P2` with deck group `(Z/2)^6`;
- seven coordinate-sign K3 quotients;
- Campedelli quotient compression;
- the Beauville irregular cover;
- modular `M(4,8)` / `X(8)` descriptions with field-of-definition firewalls;
- endpoint L-function / K3-character decomposition;
- parametric/Master-Hit coverage and local squareclass views.

Durable Stage29 closures include exact crosswalks between these models, the physical population/subcover incidence dictionary, Stage20/Testa-Stoll K3 identification, global Master-Hit coverage of primitive Euler bricks/endpoints, endpoint avoidance of the F7 branch lines and Q-liftable permutation fixed loci, and complete degree-`<=6` integral curve-carrier classification in the audited scope.

Stage29-13 also discharged the nondegenerate Saunderson family and the explicit

```text
B(q)=(4q,q^2-4,2(q^2-1))
```

family against perfect completion. Consequently

```text
liminf (M3(B)-P(B))/B^(1/3) >= 27/(40*pi^2) > 0,
```

but this does **not** imply `P/M3 -> 0`.

## 5. Final Stage29 close state

Stage29 closed at `29-17` as an endpoint-synthesis phase. The perfect-cuboid problem did not close.

Final triage:

```text
SOURCE_FRONTIER_COUNT=46
CLOSED_CLASS1_COUNT=6
ACTIVE_CLASS2_COUNT=13
ACTIVE_CLASS3_COUNT=11
DORMANT_CLASS4_COUNT=16
FINAL_ACTIVE_KERNEL_COUNT=13
FINAL_CLASS2_KERNEL_COUNT=4
FINAL_CLASS3_KERNEL_COUNT=9
HIDDEN_CLASS1_PENDING_COUNT=0
```

The historical 11-route surface is frozen as provenance:

```text
G10-FULL-ENDPOINT       = AMBER
G10-LOWGENUS-PICARD     = AMBER
G10-K3-SIGN             = AMBER
Q11-CAMPEDELLI          = AMBER
Q11-BEAUVILLE           = AMBER
Q11-MODULAR             = AMBER
Q11-BRAUER              = AMBER
J12-JOINT-V4            = AMBER
J12-LOCAL-SQUARECLASS   = AMBER
J12-PARAMETRIC          = AMBER
J12-POP-INTERACTION     = GREEN
```

`GREEN` records theorem-level progress, not endpoint resolution.

### Final Class-2 computational/model kernels

```text
K16-C2-LOWGENUS-PICARD-PRODUCTION
K16-C2-MODULAR-S4-ACTION
K16-C2-BRAUER-EXPLICIT-CHAIN
K16-C2-EXT-E-INTEGRAL-CERTIFICATION
```

### Final Class-3 theorem kernels

```text
K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT
K16-C3-CAMPEDELLI-UNIFORM-TORSOR
K16-C3-BEAUVILLE-ONE-STEP-DESCENT
K16-C3-QWEB-CLIFFORD-OBSTRUCTION
K16-C3-M3-LOCAL-TO-GLOBAL
K16-C3-PESCH-EXPONENT-ONE
K16-C3-MOVING-FIBER-ARITHMETIC
K16-C3-EXT-C-PRIMITIVE-DIVISOR
K16-C3-TERMINAL-P-OVER-M3
```

`K16-C3-PESCH-EXPONENT-ONE` is conjectural. If the exact receiver `R29-PESCH-E1` were proved, the audited dependency chain would imply perfect-cuboid nonexistence; that theorem is **not currently proved**.

Future work should start from these 13 kernels rather than replay Stage29's 46-entry triage.

## 6. Exact finite evidence

The exact matched Stage29 census reaches `B=10^9`:

```text
M2(10^9) = 51,379,127,865
N2(10^9) = 4,566
M3(10^9) = 4,362
P(10^9)  = 0
```

Firewall:

```text
P(B)=0 for B<=10^9  !=  P(B)=0 for all B.
```

Finite data are regression/evidence only; no true exponent, eventual ordering, or global nonexistence theorem is inferred from them.

## 7. What is closed and should not be casually reopened

At their exact audited scopes, treat these as stable inputs:

1. primitive/canonical physical population and cutoff conventions;
2. `M1`, `N1`, `M2` asymptotic scales;
3. `N2` infinitude + zero density + quarter/half exponent corridor;
4. `M3` infinitude + explicit one-third liminf lower + log-saving upper;
5. Stage16-28 interaction/no-double-charge interfaces;
6. Stage19/20 common-base K3 bridge and physical polarization;
7. explicitly audited Stage29 endpoint/sign/K3/Campedelli/Beauville/modular structural maps;
8. Master-Hit global Euler/endpoint-candidate coverage;
9. Saunderson and explicit `B(q)` endpoint exclusions;
10. degree-`<=6` carrier classification in its stated scope;
11. exact finite census through `R<=10^9`;
12. Stage29 final triage into 13 active kernels plus 16 dormant Class-4 receivers.

“Closed” means closed at the theorem/adapter/family scope stated in the source. It does not mean the perfect-cuboid problem is solved.

## 8. Final frontier

```text
Stage16-29 research program             : CLOSED
Perfect cuboid existence/nonexistence   : OPEN
P(B)/M3(B)                              : OPEN
true N2 exponent                        : OPEN
true M3 exponent/asymptotic             : OPEN
historical endpoint route portfolio     : 1 GREEN / 10 AMBER
active restart kernels                  : 13
hidden immediately executable Class-1  : 0
finite exact endpoint search            : zero hits through R<=10^9
```

Authoritative final handoff:

- [`Stage29-17 result`](../stages/stage29/29-17/result.md)
- [`Stage29-17 final-handoff.json`](../stages/stage29/29-17/final-handoff.json)
- [`Stage29-17 audit`](../stages/stage29/29-17/audit.md)
- [`Stage29 numerical ledger`](../stages/stage29/numerical-ledger.md)

This file, not an archived CURRENT/status/roadmap document, is the canonical high-level state of the completed Stage16-29 program.
