# Stage32 Arsenal Harvest 4 — discovery ledger

Status: **DISCOVERY COMPLETE / ABSTRACTION, HOSTILE DEDUP, IMPLEMENTATION NOT PERFORMED**.

This is a discovery ledger only. It does not register Arsenal weapons/workflows, assign stable IDs, mutate Stage32 authority, or grant mathematical credit.

## Frozen range

Harvest 3 is PR #1668. Harvest 4 starts from its frozen discovery upper bound, not from the later implementation merge:

- previous frozen upper bound: `714bd143f0c20082edcbb81c3905a86b1a56b4bf`
- Harvest 3 merge: `9184c7ab694415592cc428a675c0ebed27cac510`
- Harvest 4 merged-source upper bound at discovery start: `bf2890ec0b8168f70db803de876024aa6b6d1f6d`

The unmerged Stage32 retained line is included only as a separate frozen source snapshot:

- PR #1753
- branch `stage32-main-final-chain-reentry`
- exact head `1b171f5f45ded8937f51a666e606d88b26a96402`
- status: `SNAPSHOT_SOURCE_ONLY_NOT_MAIN_AUTHORITY`

Later movement of main or #1753 does not widen this discovery automatically.

## Result

The machine ledger `stage32-harvest4-discovery.json` records exactly **25 raw candidates**. No NEW_WEAPON / EXTEND_EXISTING / NEW_WORKFLOW / HISTORICAL_OR_NEGATIVE / STAGE32_SPECIFIC / REJECT_DUPLICATE decision has been made yet.

### A — FULL178 exact finite-population / lattice / indexing

1. `A01` N220 prefix exceptional-support capacity necessary cut. Audited zero-loss cut; ~49.7089% of the post-node-mass indexed population is rejected without Picard64 completion.
2. `A02` N230 filtered-rank random access preserving the old canonical completeness rank. Hostile-audited.
3. `A03` N240 fail-closed filtered execution/completeness adapter. Manifest membership and fake-completion defects repaired; re-audit required.
4. `A04` N250 exact post-N220 block-priority census. Finds four one-block e=48 strata.
5. `A05` N260 mass/support saturation rigidity. In four e=K=48 strata all 48 exceptional coordinates are forced to one and only x4 remains free. Audit required.
6. `A06` N270 exact negative HNF check: `[1]^48+x4` rejects 0/12952 terminals.
7. `A07` N280 50-functional normal-mass augmented HNF obstruction. Provisionally rejects 6438/12952 terminals and empties two of four N260 strata. Audit required.
8. `A08` N290 dependent half-mass extraction. Gives an exact derived quantity for a stronger nonnegativity cut but no direct new rejection.
9. `A09` EX5 symbolic-free-axis exact UNSAT partition. Local `(g1-d008,e=4)` ranks `0..398` are retained UNSAT in three 133-rank blocks while x4 stays symbolic.

### B — geometry / topology / cover / marking

10. `B01` finite stabilizer-capacity + parity branch forcing from EX1-05C/05D.
11. `B02` normalization conductor/discriminant even-correction coupling `Disc=Br+2A` from EX1-05H.
12. `B03` cellular Smith-cokernel assembly obstruction from EX1-05AF: `6144 x 4 = 24576` actual classes, zero trivial classes, every class order two; load-bearing in the audited V6 genus-1 exclusion.
13. `B04` audited EX3 cover-geometry exclusion plus separately audited population-identity adapter before MAIN consumption.
14. `B05` audited finite marking-torsor ambiguity certificate: 24 projective identifications, transitive S3, and 8/8/8 W-line counts prove the frozen package cannot choose an absolute W-line.
15. `B06` branch-labelled H1/J2 to P/Q structural marking adapter with the absolute cyclic phase left explicitly unresolved.
16. `B07` EX6 weighted tensor pole-debt accounting, including residual nonnode minimum `(1116+8E)k` after subtracting the known f-divisor contribution.
17. `B08` exact product-cover nonnode ramification split `8*eta+8*rho`; also proves total-degree RH is duplicate of the previous two-factor slack.
18. `B09` AM-BJ canonical 48-node / Aut(1536) / order-64 sign-kernel / full-S4 / nonsplit-extension package.
19. `B10` AM-BJ Galois/orbit separation: `cc(V6)` lies outside the retained Aut orbit of V6.

### C — source/runtime and research-ops adapters

20. `C01` runtime exceptional index -> exact object -> canonical projective fingerprint -> retained node identity bridge. Runtime enumeration order is explicitly not mathematical identity.
21. `C02` exact BTVA 48-node reconstruction and BTVA-to-Stoll coordinate-rename/model adapter.
22. `C03` Stage32 fail-closed claim-DAG / cross-scope authority and promotion contract from #1706/#1708. Research-ops candidate only at discovery time.

### D — breadth / section / theorem-interface candidates

23. `D01` audited bounded EX5 route-family exhaustion anti-loop: `5 BLOCKED + 1 INAPPLICABLE + 1 DUPLICATE + 0 QUALIFIED`, with typed re-entry blockers.
24. `D02` EX2 valuation-separated finite section-subspace reconstruction: a 2D divisor-theoretic subspace plus a third independent section line, without claiming full H0 or a member.
25. `D03` audited symmetric-differential labelled-node support/span infrastructure with a separate exceptional-pairing bridge and runtime-identity gate.

## Carry-forward watchlist from Harvest 3

Not counted among the 25 new discoveries:

- PR #1570 — orbit-sum stabilizer / blow-down quotient noninvariance / equivariant pullback / commutator lineage. Harvest 3 left it promotion-blocked on provenance/audit-receipt recovery.
- PR #1643 — source-bound H-character probe `chi_u -> {0,infinity} -> delta_0inf`. Harvest 3 left it promotion-blocked on the then-frozen authority surface.

Their maturity/provenance can be rechecked during abstraction/dedup; they are not silently rediscovered as new items.

## Discovery boundaries

- N220 and N230 are hostile-audited exact sources.
- N240 is a hostile-FAIL repair awaiting re-audit.
- N260 and N280 remain audit-required; their numerical exclusions are not authority yet.
- N270 and N290 are retained negative/dependence results, not new pruning credit.
- EX5 ranks `0..398` are local exact UNSAT only, not whole-stratum or FULL178 closure.
- EX1-05AF is audited, but a generic Arsenal weapon must abstract the cellular/assembly hypotheses rather than inherit a V6 conclusion.
- EX4/EX6 negative walls remain bounded anti-loop knowledge, not global impossibility claims.
- Runtime node canonicalization preserves projective-scale and enumeration-order independence while treating geometric/Galois actions equivariantly; quotienting by the full geometric action would destroy the 48-object identity.

## Deliberately not performed

- hostile dedup against existing Arsenal cards;
- stable Arsenal ID assignment;
- `docs/arsenal/index.json` edits;
- generated card/catalog edits;
- Stage32 MAIN/EX state edits;
- heavy workflow reruns;
- hostile-audit self-credit;
- merge.

## Next phase

`STAGE32_HARVEST4_ABSTRACTION_THEN_HOSTILE_DEDUP`

That phase should abstract each candidate's hypotheses/output contract first, then aggressively compare against existing Arsenal weapons/workflows and the Harvest 3 carry-forward watchlist before any implementation or stable-ID assignment.
