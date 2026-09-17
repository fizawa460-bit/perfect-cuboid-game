# Stage32 MB104 — PR1819 retained search ledger — 2026-09-17

Status: **RESTART-SAFE SEARCH LEDGER / NO NEW MATHEMATICAL CREDIT**

This file is the compact successor ledger for the oversized historical research PR #1791. It exists so later `stage32mb-mainbatch` runs do not repeat searches already performed there.

## Historical source lock

```text
historical PR: #1791
historical branch: stage32mb-mainbatch-20260912
historical exact head at split: ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
new branch base: c6284abbb29930255892d56f800da0ea1e34734b
```

The historical PR remains the archive for detailed intermediate derivations. A closed PR is still a valid historical source; do not delete the historical branch while this ledger is active. No mathematical claim is imported merely because it existed in #1791.

## Retained current boundary

Current node: `MB104`.

Current unresolved packet is the genus-one span-5 balanced `000707000f0f` survivor, with `e=2` and `e=4` still open. The dangerous equality-packet core previously reduced to the `000707000f0f` family; no finite degree window, receiver credit, effectivity credit, theorem credit, endpoint credit, or Perfect-Cuboid claim was released.

For the `e=2` conductor problem, the canonical relative-sheet bit has already been identified:

```text
chi_ij := (r_i*r_j)/h,
chi_ij^2 = 1,
chi_ij=+1 <=> same residual lift <=> [lambda_(p;i,j)]=0,
chi_ij=-1 <=> deck-twisted lift <=> [lambda_(p;i,j)]=[gamma_Q].
```

The missing datum is not an absolute square-root sign. It is the actual conductor-pair transition, equivalently whether each conductor loop maps to `0` or `gamma_Q` in the retained ambient `Z/2` character.

The retained `e=2` Hodge target is

```text
sum_p sum_(i<j) I_ij*(1-chi_ij)/2 >= 84*l^2.
```

No strict upper bound below this threshold has been proved.

## Routes already searched: do not restart without a new enabling input

### A. Old R8/direct finite-window routes — dominated or wrong-side

- Pure local A1 landing data: arbitrarily many minimal branches can have distinct resolved landing parameters; no bounded multiplicity follows.
- Garcia-Fritz--Urzua symmetric differential degree: controls the wrong-side exceptional quantity and does not give the required `R8 < d/4 + O(1)` upper slope.
- Six rank-3 genus-5 fibrations with simple intersection: only `R8<=M<=6d`.
- All 28 fibrations with unit charging: at best a weak linear capacity; the retained slope test requires aggregate branch charge `q>112`, while one charge through all 28 maps gives only `q=28`.
- Fixed finite local jets / finite principal-part portfolios: saturated; repeated branches can share every bounded-depth local evaluation vector.
- Ordinary delta, Hodge projection, parity/transvection, mod-4 shell, determinant-bit, Bezout capacity, and formal allocation rearrangements did not close the balanced survivor.

Re-entry condition: a genuinely branch-sensitive global collision/conductor/intersection mechanism, an adaptive/unbounded-depth construction with controlled global dimension, or a new source-locked classification theorem strong enough at arbitrary degree.

### B. Ambient product / topology / Picard-torsion route — PAUSED AS PRIMARY

The `X_H=(C8 x C8)/H_diag` Armstrong route reached a finite abelianization computation with 128 representative fixed-element relations and a candidate unimodular-minor conclusion. The unresolved load-bearing point is source-completeness: whether those 128 representatives generate all fixed-point relations needed after abelianization.

Do not rerun another numerical rank computation first. Re-entry requires a proof of the torsion/fixed-point classification, reduction of conjugator choices to relative `H`-cosets, and exhaustiveness of the 128 relations. Even a successful `H_1(X_H,Z)=0` promotion would not automatically determine singular-carrier conductor gluing.

### C. Pointwise conductor residual-sheet recovery — PAUSED AS PRIMARY

The exact relative receiver `chi_ij` is retained, but invariant downstairs A1 branch data, `eta=0`, common-cover existence, current `E[2]` compression, and the existing product/Jacobian package do not select the conductor gluing bit. The repository does not currently materialize the normalization-preimage transition data needed to evaluate every pair.

Do not return to absolute `tau`-odd sheet labels or pointwise `r_z/r_w` comparisons unless a new source-locked local modular/product-cover adapter appears.

### D. Cusp-width shortcut — CLOSED pending exact support equality

The shortcut requires the exact source-locked equality

```text
f1^{-1}(Cusps) = f2^{-1}(Cusps).
```

Current divisor-class/product information does not establish equality of these effective supports. Do not reuse the cusp-width obstruction without this equality.

### E. Product correspondence / common etale cover — REJECT AS PRIMARY

The previous `1024 -> 128` reduction counted Picard labels rather than divisors. Each surviving class still has a large moving section space `h0(A box B)=(28l-4)^2`. This route does not by itself eliminate the balanced packet.

### F. Correlated 28-fibration support/multiplicity passport — REJECT AS NEXT DEEP ROUTE

The shallow leverage test did not find a coupled inequality beating the already-failed summed-RH/unit-charging capacity. The retained free first jet can generically avoid every finite critical-slope condition, and the aggregate charge is far below the `q>112` threshold.

### G. Global curve / Mori classification — HOLD

Current test curves leave an unbounded balanced ray. Re-entry requires a genuinely new full Mori/effective-cone input or an arbitrary-class low-genus classification; current bounded-degree/low-span results are insufficient.

### H. Picard/effectivity/irreducibility — HOLD, one cheap preflight allowed

Fixed-component, conic, zero-quartic, Riemann--Roch, local-jet, and purely numerical Picard routes are exhausted for this purpose. The only currently justified cheap continuation is a global equality-packet/equisingular codimension preflight, not naive independent-jet counting.

Numerical leverage target:

```text
dim |lA| approximately 168*l^2 - 56*l + 7,
required delta/equality defect = 168*l^2 + 56*l,
nominal deficit approximately 112*l - 7.
```

Test small `l` first (`l=1,2,3`) only if an exact source-locked global evaluation model exists. Continue deeper only if the exact global codimension shows the needed linear-growth deficit and survives known superabundance. Otherwise mark the route HOLD/REJECT and rotate to another `32-03`-level mechanism.

## Detailed historical artifacts worth consulting before reopening a route

At historical exact head `ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11`, the following files are the first lookup points:

```text
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/R8-BOUND-ROUTE-LEDGER.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GLOBAL-CLASSIFICATION-CHECKPOINT.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESEARCH-CHECKPOINT-20260917.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-CONDUCTOR-PAIR-INVOLUTION-QUOTIENT.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INVARIANT-NODE-BRANCH-NORMALIZATION.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/ARMSTRONG-FIBER-PRODUCT-H1-SOURCE-NOTE.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MULTIFIBRATION-RH-CAPACITY-WALL.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MULTIFIBRATION-LOCAL-JET-WALL.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FINITE-JET-MULTIPLICITY-SATURATION-WALL.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-13FORM-PORTFOLIO-PREFLIGHT.md
```

Search those historical paths before opening a new route with the same mathematical shape.

## Next research rule

Work one level above the individual conductor sign. Prefer a shared MB104 obstruction capable of eliminating an entire packet or forcing a finite window. The first permitted cheap probe is the equality-packet/equisingular global codimension test above. If it fails, rotate to another `32-03`-level global mechanism rather than descending again into the parked topology or pointwise-sign tunnels.

## Firewalls

- `e=2`: OPEN.
- `e=4`: OPEN.
- `000707000f0f`: OPEN.
- No conductor pair is assigned `chi=+1` or `chi=-1` by this ledger.
- No `H_1(X_H,Z)=0` promotion is made here.
- No finite degree window is proved.
- No receiver/effectivity/final-milestone/theorem/endpoint/Perfect-Cuboid credit.
- No heavy compute authorization.
- No merge/rebase authorization.
