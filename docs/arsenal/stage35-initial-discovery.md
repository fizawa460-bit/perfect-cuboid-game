# Stage35 / Stage35-EX Arsenal initial harvest discovery ledger

Status: `DISCOVERY_ONLY_NOT_ARSENAL_PROMOTION`

Human-readable Harvest 1 discovery ledger plus Harvest 2 mathematical abstraction. Machine-readable files:

- `docs/arsenal/stage35-initial-discovery.json` — full Harvest 1 discovery/provenance ledger, now pointing to the H2 companion;
- `docs/arsenal/stage35-initial-abstraction.json` — all 36 Harvest 2 abstraction sheets.

## Frozen harvest boundary

There was no pre-existing Stage35 Arsenal checkpoint, so the lower bounds were reconstructed from authoritative Git/main history, not from a working-branch `SOURCE_HEAD`.

- Stage35 canonical inception: `43b5cc4a655cf68e9bdefad22800071d6f8d9fa0` (PR `#1506` merge).
- Stage35-EX canonical inception: `7423eab4f153df7e58c3c9aa7ef3ecdf3f53c4f8` (`stage35-ex: add bounded startup charter`).
- Harvest upper bound/current main at Harvest 1 start: `9184c7ab694415592cc428a675c0ebed27cac510`.
- Scope remains Stage35 inception -> frozen upper bound union Stage35-EX inception -> frozen upper bound.
- Later `main` movement does not widen Harvest 1 or Harvest 2.

## Firewalls

This PR does not modify `docs/arsenal/index.json`, generated cards, catalog, Stage35 MAIN state, or Stage35-EX authority. It assigns no stable IDs and grants no theorem, receiver, endpoint, E1, R29/FIB2/J12, Stage35, or perfect-cuboid credit. Negative routes are not mathematical weapons. No merge is authorized.

## Arsenal lookup discipline

The required order was followed: `docs/arsenal/index.json` first, then only semantic near-neighbor cards. H2 comparison neighbors are `S34-W01`, `S34-W03`, `S34-WF01`, `S33-PW04`, `S33-PW07`, and `S31-W01`; `S30-WF03` is retained for Harvest 3 workflow/source-marking comparison.

## Harvest 1 discovery totals

| Class | Count |
|---|---:|
| A probable `NEW_WEAPON` | 11 |
| B probable `EXTEND_EXISTING` | 7 |
| C probable `NEW_WORKFLOW` | 6 |
| D `STAGE35_SPECIFIC` | 3 |
| E `HISTORICAL_OR_NEGATIVE` | 6 |
| F unresolved | 3 |
| **Total** | **36** |

The full H1 per-candidate source PR/head/certificate/verifier/blob/audit fields remain in `stage35-initial-discovery.json`; H2 does not rewrite those discovery claims.

# Harvest 2 — Mathematical Abstraction

- `DISCOVERY + ABSTRACTION COMPLETE`
- `HOSTILE DEDUP NOT YET COMPLETE`
- `ARSENAL PROMOTION NOT PERFORMED`

All 36 H1 candidates have an abstraction sheet containing object type, exact hypotheses, transformation, output, failure contract, marking/source-lock requirement, reusability test, and source locator. Stage35 symbols are stripped only where the exact hypotheses survive; a concrete Stage35 calculation is never widened into an unstated theorem.

## H2 reclassification

| Class | Count | IDs |
|---|---:|---|
| `ABSTRACTABLE` | 7 | `A02,A03,A05,A09,A10,B01,B05` |
| `PARTIALLY_ABSTRACTABLE` | 14 | `A01,A04,A06,A07,A08,A11,B02,B03,B04,B06,B07,F01,F02,F03` |
| `STAGE35_SPECIFIC` | 3 | `D01,D02,D03` |
| `NEGATIVE_ONLY` | 6 | `E01-E06` |
| `WORKFLOW_ONLY` | 6 | `C01-C06` |
| **Total** | **36** | |

## Product-square chain: split contracts

Do not merge the original Stage35 chain into one weapon.

1. The source-specific primitive normalization and two-Pythagorean branch extraction remain upstream marked payload.
2. `A01` retains the reusable **coprime product rectangle** core: from `RS=UV`, `gcd(R,S)=gcd(U,V)=1`, allocate prime powers into four pairwise-coprime cells to reconstruct the four factors.
3. `B01` is separate: an exact square ratio with four factored terms gives a **product-square** condition only.
4. `A02` is the subsequent dynamic gcd-reservoir support method.
5. `A03` is the subsequent squareclass compatibility-graph method.

Firewall: `product-square != each factor square`.

## Squareclass abstraction

`A02` converts exact pairwise gcd identities into a bounded reservoir incidence table while preserving live parameter-dependent primes and separate 2-adic bookkeeping. `A03` converts complete pair-product squareclass relations into an edge-labelled compatibility graph and solves vertex squareclasses in independent reservoirs. Both are transportable methods, but neither proves the fixed finite exhaustive branch family required by `S34-W01`.

## Gaussian abstraction

`D03` is demoted to `STAGE35_SPECIFIC`: the concrete Gaussian factorizations are source formulas and the generic factorization is classical. `A04` survives partially only at the **joint-orientation** level: two genuinely distinct source-locked norm orientations, after exact unit/conjugation control, may yield a new squareclass compatibility condition. A symmetry-mirrored orientation is not a new receiver.

Firewall: `Gaussian factorization != new obstruction` and `necessary local/norm condition != global contradiction`.

## Elliptic / Kummer abstraction

The four Kummer leaves remain separate because their contracts differ:

- `A05`: involution quotient + fixed/boundary accounting + exact converse;
- `A06`: rational-source lift predicate + source-faithful Kummer normal form;
- `A07`: internalization of remaining source square(s) into a complete finite Kummer receiver;
- `A08`: reciprocal common-factor compression of an already complete receiver.

`B07` is only partially abstractable: sign involutions on a diagonal high-genus family can produce elliptic quotient inventories, but the quotient data do not classify the source curve or specialization-new points. Exact genus-one quartic -> elliptic birational transport remains the separate `S31-W01` contract.

Firewalls: `finite quotient != rational point classification`; `genus-one/elliptic model != MW closure`; `generic function-field information != all-specialization theorem`.

## Picard / Brauer abstraction

`B03`/`B04` are only partially abstractable because a full source-marked Picard G-module is load-bearing; they strongly overlap `S33-PW04`/`S33-PW07`. `D02` is the object-specific Stage35 proper result and remains Stage35-specific. `F01` is an incomplete but meaningful open-boundary adapter schema: boundary divisor module -> map into proper Picard -> `Pic(Ubar)`/localization/Brauer data. Proper `H^1(G,Pic)` or `Br_1` cannot be relabelled as an open result. `F03` likewise cannot become a Brauer obstruction without one exact global unramified class and its source-bound local evaluations.

Firewalls: `Brauer candidate != Brauer obstruction`; `proper Brauer != open Brauer`.

## Other high-value reusable contracts

- `A09`: primitive three-variable pair-gcd skeleton `A=xy*a`, `B=xz*b`, `C=yz*c`, transporting only the coprimalities actually forced.
- `A10`: finite exceptional-prime classification by exact small-prime census plus bounded-genus auxiliary-curve/Weil completion for all sufficiently large primes.
- `B05`: finite forced-prime support assignments followed by symmetry/Burnside orbit compression; finite routing receiver only, not global squareclass exhaustion.
- `A11`: p-adic valuation-cone and signed-gap coupling remains only partially abstractable because the retained theorem is prime/residue-pattern specific.

## Marking / source-lock result

Source marking remains essential for `A04`, `A06-A08`, `B03`, `B06`, `F01`, and `F03`. The core methods in `A01` (rectangle core), `A02`, `A03`, `A05`, `A09`, and `A10` can be stated without Stage35 variable names once their exact hypotheses are retained.

## Harvest 3 exact handoff

Keep the upper bound frozen at `9184c7ab694415592cc428a675c0ebed27cac510`. Hostile-dedup the 21 mathematical candidates `A01-A11`, `B01-B07`, `F01-F03`; separately dedup workflow candidates `C01-C06`; do not promote `D01-D03` or `E01-E06` as mathematical weapons.

Comparison cards: `S34-W01`, `S34-W03`, `S34-WF01`, `S33-PW04`, `S33-PW07`, `S31-W01`, `S30-WF03`. For every retained candidate compare object type, field, quantifiers, markedness, hypotheses, transformation, output, and failure contract. Compare `A01` only at the rectangle core; `A02/A03` only as pre-enumeration support/graph contracts; `A04` only at joint-orientation level; keep `A05-A08` separate unless hostile comparison proves semantic identity; compare `B03/B06` to `S33-PW04` and `B04/F03` to `S33-PW07`; preserve proper/open separation; dedup `C01-C06` against Arsenal workflows and Research OS; retain `E01-E06` only as negative/history assets.

No stable ID assignment, `index.json`/card/catalog modification, Stage authority change, or merge is authorized by Harvest 2.
