# Stage29 frozen frontier — 13 active kernels

Status: **Stage29 CLOSED; perfect-cuboid problem OPEN.**

This is the human-readable restart ledger for the 13 active kernels frozen by Stage29-17. It is a projection of the audited Stage29-16/17 records, not a new mathematical claim.

Authority:
- `stages/stage29/29-16/active-kernel-ledger.json`
- `stages/stage29/29-16/decision-frontier.md`
- `stages/stage29/29-17/final-handoff.json`
- `stages/stage29/29-17/post-stage29-research-os.md`

## Execution classes

- **Class 2 / ②** = current-tool-limit executed. No new theorem is logically required at the first wall; restart by decomposing into exact code/CAS/model/certificate leaves.
- **Class 3 / ③** = new theorem required. Do not replay generic searches. Restart only when a theorem candidate, genuinely new proof mechanism, or a special-structure reduction changes the exact wall.

Generic anti-loop rule:

```text
chosen kernel
  -> dependency DAG
  -> bounded work packages
  -> leaf-level Class 1/2/3/4 reclassification
```

## Master list

| Kernel | Class | Source receiver(s) | Exact wall | Known audited input | Restart condition | Endpoint consequence |
|---|---:|---|---|---|---|---|
| `K16-C2-LOWGENUS-PICARD-PRODUCTION` | ② | `LG2`, `LG2-EFF`, `LG2-MB` | symmetry-reduced, effectivity-aware, multibranch Picard-lattice enumeration to audited `d<=176/192` bounds | degree `<=6` carrier classification; finite Picard reduction; rank-44 close-vector feasibility analysis | **NOW if chosen**: implement a production symmetry/orbit + effectivity + multibranch enumerator with reproducible certificate | complete bounded low-genus census only; not decisive without rational-point coverage |
| `K16-C2-MODULAR-S4-ACTION` | ② | `KUM5` | arrangement-to-modular `S4` action identification compatible with audited `Q/Q(i)` descent cocycles | abstract `S4` groups/field scopes known; `MOD1C` closed with trivial sigma action and 8 marked defects; `MOD1D` physical noncusp stabilizer-free | **NOW if chosen**: materialize the action/cocycle-level identification; abstract group isomorphism is insufficient | maps the 8 defects to the exact arrangement action; does not eliminate a defect by itself |
| `K16-C2-BRAUER-EXPLICIT-CHAIN` | ② | `CAMP4`, `K3-RULED2`, `BR0A/B/G`, `BR2A/B`, `NF-PHYS2` | source-locked integral boundary/Picard matrices + saturation; absolute-Galois `UPic/Gersten`; Creutz–Viray relation/symbol matrix; `Q`-descent; explicit 2-primary classes; local evaluation | 72-component physical boundary; Div→Pic preflight; Ford seven-line geometric `Br[2]` precursor dimension 9; explicit `K_c` ruled `(4,4)` model; simple branch; geometric `dim_F2 Br(K_c_Qbar)[2]=2` | **NOW if chosen**: start at `BR0A` matrix/saturation and follow the audited dependency DAG; no new theorem prerequisite at the first wall | decision-capable if the completed physical Brauer/étale-Brauer set is certified empty; completion alone may return nonempty |
| `K16-C2-EXT-E-INTEGRAL-CERTIFICATION` | ② | `EXT-CHANG-E` | integrality-preserving quartic→elliptic birational maps plus source-locked complete `IntegralPoints`/elliptic-log certificate | 29-13 certification attempt isolated the missing integrality/reconstruction certificate; sampled height constant alone rejected | **NOW if chosen** when the maps/certificate can be constructed or source-locked and independently checked | closes/rejects one thin Sophie-Germain-prime family only |
| `K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT` | ③ | `PI1-OPEN` | effective cuboid-specific higher-dimensional/nonabelian rational-point theorem on physical `U`, or another theorem directly classifying/emptying `U(Q)` | endpoint four-quadric/open geometry, physical exclusions, quotient maps and low-degree carrier work audited; global upper `P(B)<<_eps B^(1/2+eps)` | reactivate only for a theorem/proof mechanism that actually classifies or empties physical `U(Q)`, or reduces it to exact finite work | directly decision-capable |
| `K16-C3-CAMPEDELLI-UNIFORM-TORSOR` | ③ | `CAMP2` | uniform ramification support + finite Selmer-style control for relevant `H`-torsors, or replacement theorem proving `C_H(Q)=empty` | audited `Q`-defined Campedelli quotients; every endpoint `Q`-point pushes to each audited quotient; geometric quotient work already done | reactivate on an individual-uniform torsor/Selmer theorem or quotient-specific emptiness theorem with exact `Q` adapter | one audited quotient with empty `Q`-points would be decisive |
| `K16-C3-BEAUVILLE-ONE-STEP-DESCENT` | ③ | `BEAU1C`, `BEAU2`, `BEAU3` | make physically occurring open twists finite, or uniformly control every locally soluble Beauville/Bolza twist enough to compute one-step descent/étale-Brauer | exact pointwise squareclass `delta(P)=F_cub(P)`; codim-1 parity; swap-stable `V4` kernel; ordinary descent = étale-Brauer on physical open; iterated descent adds no stronger obstruction | reactivate on a theorem giving finite physical twist support, uniform all-twist arithmetic, or a special reduction to finite exact computation | decision-capable if the exact one-step set is empty |
| `K16-C3-QWEB-CLIFFORD-OBSTRUCTION` | ③ | `QWEB-CLIFFORD` | rank-7 Clifford/isotropy theorem strong enough for the exact endpoint quadratic web, with physical adapter | exact endpoint quadratic-web receiver fixed; proper algebraic and odd-primary Brauer avenues already separated/exhausted | reactivate only on a theorem/proof that matches rank, field and physical isotropy hypotheses exactly | decision-capable if it yields a genuine endpoint obstruction |
| `K16-C3-M3-LOCAL-TO-GLOBAL` | ③ | `KUM-LOC3` | uniform local-to-global/equidistribution/sieve transfer for the correlated seven squareclasses on exact primitive canonical `M3` under `R<=B` | odd-prime laws + real place + exact `Delta_2=1/53760`; exact seven-squareclass local object known | reactivate on a **same-physical-measure** theorem; ambient `P2`/toric density is not sufficient | closes a legal `M3`-host density/survival statement; not nonexistence by itself |
| `K16-C3-PESCH-EXPONENT-ONE` | ③ | `PESCH-E1` | prove universal exponent-one blocker, or replacement theorem with the same global Master-Hit consequence | Master-Hit global coverage of every primitive Euler brick / endpoint candidate audited; conditional implication audited | reactivate on a proof of E1, a theorem implying E1, or an exact replacement preserving global coverage | **if proved as stated ⇒ perfect-cuboid nonexistence**; currently conjectural |
| `K16-C3-MOVING-FIBER-ARITHMETIC` | ③ | `FIB2` | uniform arithmetic/specialization over moving genus-3/genus-5 family, or globally exhaustive finite reduction with exact lift reconstruction | fibration architecture and field ledgers exist; individual-fiber Chabauty/MW methods known to fail the uniform quantifier | reactivate on a uniform family theorem or a proof that a finite fiber list is globally exhaustive | decision-capable if all fibers are covered and lifts reconstructed exactly |
| `K16-C3-EXT-C-PRIMITIVE-DIVISOR` | ③ | `EXT-CHANG-C` | effective odd-multiplicity primitive-divisor theorem upgrading audited finite windows to all multiples | finite rank-1/rank-2 windows already executed/audited; residual all-multiples step isolated | reactivate on the required primitive-divisor theorem or a family-specific proof replacing it | closes one special moving/thin family, not the global endpoint |
| `K16-C3-TERMINAL-P-OVER-M3` | ③ | `TERMINAL-P-OVER-M3` | direct endpoint-vs-Euler interaction theorem giving a nontrivial scale for `P(B)/M3(B)`, or endpoint emptiness | `M3` lower/upper corridor; global `P` upper; exact nested-host survival theorems; exact census has zero endpoint hits through `10^9` | reactivate on a direct same-host `P/M3` theorem, a new endpoint-vs-Euler correlation mechanism, or endpoint emptiness theorem | closes literal final survival scale; even `P/M3->0` alone would not prove `P=0` |

## Decision-value split

Directly or conditionally endpoint-decision-capable:

```text
K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT
K16-C3-CAMPEDELLI-UNIFORM-TORSOR
K16-C3-BEAUVILLE-ONE-STEP-DESCENT
K16-C2-BRAUER-EXPLICIT-CHAIN
K16-C3-QWEB-CLIFFORD-OBSTRUCTION
K16-C3-PESCH-EXPONENT-ONE
K16-C3-MOVING-FIBER-ARITHMETIC
```

Supporting / scale-only when closed in isolation:

```text
K16-C2-LOWGENUS-PICARD-PRODUCTION
K16-C2-MODULAR-S4-ACTION
K16-C2-EXT-E-INTEGRAL-CERTIFICATION
K16-C3-M3-LOCAL-TO-GLOBAL
K16-C3-EXT-C-PRIMITIVE-DIVISOR
K16-C3-TERMINAL-P-OVER-M3
```

No priority ranking is implied by this document.