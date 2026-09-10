# Stage32 Arsenal Harvest 4 — discovery ledger

Status: **DISCOVERY COMPLETE / ABSTRACTION, HOSTILE DEDUP, IMPLEMENTATION NOT PERFORMED**.

This file is a discovery ledger only. It does not register Arsenal weapons/workflows, assign stable IDs, mutate Stage32 authority, or grant mathematical credit.

## Frozen discovery range

Harvest 3 is PR #1668. Its frozen upper bound was:

`714bd143f0c20082edcbb81c3905a86b1a56b4bf`.

Harvest 4 starts from that exact boundary rather than from the later #1668 merge commit, so material between the frozen Harvest 3 ceiling and its implementation merge cannot be silently skipped.

Merged Stage32 source is frozen at discovery-start `main`:

`bf2890ec0b8168f70db803de876024aa6b6d1f6d`

which includes merged Stage32EX5 PR #1742.

The current unmerged Stage32 retained chain is included only as a separate snapshot source:

- PR #1753
- branch `stage32-main-final-chain-reentry`
- exact snapshot head `1b171f5f45ded8937f51a666e606d88b26a96402`
- snapshot status: **source only, not repository-main authority**.

Later movement of `main` or #1753 does not widen this discovery automatically.

## Discovery result

Exactly **23 raw candidates** are recorded in `stage32-harvest4-discovery.json`.

No candidate has yet been classified as NEW_WEAPON, EXTEND_EXISTING, NEW_WORKFLOW, HISTORICAL_OR_NEGATIVE, STAGE32_SPECIFIC, or REJECT_DUPLICATE. Those decisions belong to the next abstraction + hostile-dedup phase.

### A — FULL178 exact finite-population / lattice / indexing candidates

1. `DISC-S32-H4-A01` — prefix exceptional-support capacity necessary cut (N220). Audited zero-loss cut; about 49.7089% of the post-node-mass indexed terminals are rejected without Picard64 completion.
2. `DISC-S32-H4-A02` — secondary filtered-rank random access preserving the old canonical completeness rank (N230). Hostile-audited.
3. `DISC-S32-H4-A03` — fail-closed filtered execution/completeness adapter (N240 V2). Repairs manifest-membership and fake-completion acceptance defects; re-audit still required.
4. `DISC-S32-H4-A04` — exact post-N220 survivor exceptional-block priority census (N250). Finds four one-block e=48 strata without adding pruning credit.
5. `DISC-S32-H4-A05` — mass/support saturation rigidity (N260). In four e=K=48 strata, all 48 exceptional coordinates are forced to one and only x4 remains free. Audit required.
6. `DISC-S32-H4-A06` — all48+x4 HNF negative weapon check (N270). Exact dominated result: 0/12952 terminals rejected.
7. `DISC-S32-H4-A07` — normal-mass augmented 50-functional integer-lattice obstruction (N280). Provisionally rejects 6438/12952 terminals and empties two of the four N260 strata; audit required.
8. `DISC-S32-H4-A08` — dependent first-normal-half functional extraction (N290). Produces an exact forced quantity for a stronger future nonnegativity cut but adds no direct HNF rejection.
9. `DISC-S32-H4-A09` — symbolic free-axis block exact UNSAT partition (EX5 BC2). The local `(g1-d008,e=4)` ranks `0..398` are retained exact UNSAT in three 133-rank blocks while x4 is kept symbolic.

### B — geometry / topology / cover / marking candidates

10. `DISC-S32-H4-B01` — finite stabilizer capacity + parity branch forcing from EX1-05C/05D.
11. `DISC-S32-H4-B02` — normalization conductor/discriminant even-correction coupling `Disc=Br+2A` from EX1-05H.
12. `DISC-S32-H4-B03` — cellular Smith-cokernel assembly obstruction from EX1-05AF. The retained terminal has `6144 x 4 = 24576` actual classes, zero trivial classes, and every class of order two; this is load-bearing in the audited V6 genus-1 exclusion.
13. `DISC-S32-H4-B04` — audited cover-geometry exclusion + separately audited cross-population identity adapter from EX3.
14. `DISC-S32-H4-B05` — finite marking-torsor ambiguity certificate from EX4: 24 projective identifications, transitive S3 action, and 8/8/8 line counts prove the frozen package cannot select an absolute W-line.
15. `DISC-S32-H4-B06` — branch-labelled H1/J2 to P/Q structural marking adapter; exact finite phase ambiguity retained instead of silently choosing a label.
16. `DISC-S32-H4-B07` — weighted local tensor pole-debt accounting from EX6, including residual nonnode minimum `(1116+8E)k` after the known f-divisor contribution.
17. `DISC-S32-H4-B08` — exact product-cover nonnode ramification split `8*eta + 8*rho` and proof that total-degree RH is duplicate of the retained two-factor slack.
18. `DISC-S32-H4-B09` — canonical 48-node / Aut(1536) / order-64 sign-kernel / full-S4 quotient / nonsplit-extension package from the AM-BJ consolidation.
19. `DISC-S32-H4-B10` — exact complex-conjugation class separation: `cc(V6)` is outside the retained Aut orbit of V6.

### C/D — source/runtime adapters, research-ops, breadth and section reconstruction

20. `DISC-S32-H4-C01` — runtime exceptional index -> exact object -> canonical projective fingerprint -> retained node bridge. The child-lane work explicitly demonstrates why incidental runtime enumeration order must not be treated as mathematical identity.
21. `DISC-S32-H4-C02` — exact BTVA 48-node reconstruction and BTVA-to-Stoll coordinate-rename/model adapter.
22. `DISC-S32-H4-C03` — fail-closed claim-DAG / cross-scope authority and promotion contract introduced by Stage32 management PRs #1706/#1708. This is a research-ops candidate only at discovery time.
23. `DISC-S32-H4-D01` / `D02` / `D03` are represented in the machine ledger as bounded breadth anti-loop, valuation-separated finite-section reconstruction, and symmetric-differential labelled-node support/span infrastructure respectively; the machine ledger remains authoritative for the exact 23-entry inventory and source locks.

## Carry-forward from Harvest 3

Two Harvest 3 promotion-blocked items are not counted as new Harvest 4 discoveries:

- PR #1570 — orbit-sum stabilizer / blow-down quotient noninvariance / equivariant pullback / commutator lineage. Harvest 3 retained it as provenance because its exact final V2 hostile-re-audit receipt was not recoverable from the frozen surface inspected there.
- PR #1643 — source-bound H-character probe `chi_u -> {0,infinity} -> delta_0inf`. Harvest 3 retained it as provenance because the frozen authority surface did not yet support promotion.

Their maturity/provenance may be rechecked during the next abstraction/dedup phase, but their presence here does not expand the new-candidate count.

## Important boundaries observed during discovery

- N220 and N230 are already hostile-audited exact sources.
- N240 is a hostile-FAIL repair awaiting fresh re-audit.
- N260 and N280 are audit-required and therefore remain provisional source candidates.
- N270 and N290 are valuable negative/dependence results but do not add pruning credit by themselves.
- EX5 ranks `0..398` are local exact UNSAT only; no whole-stratum or FULL178 claim follows.
- The EX1-05AF terminal is audited, but Harvest 4 must still abstract the reusable cellular/Smith hypotheses instead of importing the V6 conclusion as a generic weapon.
- EX4 and EX6 negative walls are bounded anti-loop knowledge, not global impossibility results.
- Runtime node canonicalization must preserve projective-scale/enumeration-order invariance while treating geometric/Galois actions equivariantly; quotienting by the full geometric action would destroy 48-object identity.

## What has deliberately not been done

- no hostile dedup against existing Arsenal cards;
- no comparison assigning A01/A07/etc. to existing Stage32 PW IDs;
- no stable Arsenal ID creation;
- no `docs/arsenal/index.json` changes;
- no generated card/catalog changes;
- no Stage32 MAIN/EX state changes;
- no heavy workflow reruns;
- no hostile-audit self-credit;
- no merge.

## Next phase

`STAGE32_HARVEST4_ABSTRACTION_THEN_HOSTILE_DEDUP`

The next phase should abstract the reusable hypotheses/output contract of each raw candidate, then compare them aggressively against existing Arsenal weapons/workflows and the Harvest 3 carry-forward items before any implementation PR or stable-ID assignment.
