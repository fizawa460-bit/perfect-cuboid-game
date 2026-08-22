# Stage25 reentry campaign roadmap

```text
STATUS=NORMATIVE_FUTURE_CAMPAIGN
OWNER_STAGE=Stage25
CAMPAIGN=Stage25-reentry
STARTS_AFTER=Stage25 checkpoint70 audited closeout merged
PRECEDES=Stage26
```

## Purpose

Stage16–20 established population baselines, while Stage21–25 exposed interactions and produced stronger weapons. In particular, Stage25 improved the Stage19 lower bound and already forced backflow into Stages23 and24. A closed stage therefore means that its stated theorem interface is accepted; it does not mean every later-compatible research route has been exhausted.

This campaign performs one bounded reentry pass before Stage26. It strengthens the interfaces most relevant to the third-face problem, propagates material discoveries across affected stages, and then hands a synchronized weapon set to Stages26–28.

Stage25 itself must finish first. This roadmap does not relax the current checkpoint60 deep-stop rule, does not bypass checkpoint70, and does not authorize work while a Stage25 repair remains unresolved.

## Order

| Phase | Task ID | Target | Required output |
|---|---|---|---|
| `25-reentry-10` | `Stage25-um-r001a` | Stage16–25 synchronization | Freeze strongest audited interfaces, unresolved gates, and weapon dependencies |
| `25-reentry-20` | `Stage25-u24-r002a` | Stage24 reattack | Reassess `M2 -> N2` using final Stage25 lower/upper/causal weapons; attack the true target exponent and space-after-two-faces mechanism |
| `25-reentry-30` | `Stage25-u23-r003a` | Stage23 reattack | Reassess `N1 -> N2`, directional channels, second-face-under-space interaction, and any Stage24-derived receiver |
| `25-reentry-40` | `Stage25-u22-r004a` | Stage22 reattack | Strengthen the two-face/no-space source: explicit constant/directional interfaces, `log^4` mechanism, and third-face-ready toric receivers |
| `25-reentry-50` | `Stage25-u21-r005a` | Stage21 reattack | Refine the one-face/space `log^2` mechanism and isolate reusable shared-P/local factors without reopening the proved ratio law unnecessarily |
| `25-reentry-60` | `Stage25-u20-r006a` | Stage20 deep reentry | Use all strengthened weapons for a serious Euler-cuboid baseline attack; freeze the strongest Stage26-ready `M2 -> M3` interface |
| `25-reentry-70` | `Stage25-um-r007a` | propagation synthesis | Resolve derived-route queue, synchronize backflow, audit readiness, and hand off to Stage26 |

The order `24 -> 23 -> 22 -> 21 -> 20` is deliberate. Stage24 and Stage23 directly consume the final Stage25 `N2` work. Stage22 then strengthens the two-face source needed by Stage20/26. Stage21 supplies the comparison for space-diagonal interactions. Stage20 is attacked last, after those weapons are available, rather than being treated as already exhausted by its earlier baseline pass.

## Phase contract

Every phase must perform:

1. repository-wide reuse preflight, including the Stage14/15 attack ledger and deep-review queue;
2. source-level read of the affected stage's final bundle, controller, discovery ledgers, and later backflow artifacts;
3. at least one fresh compatible receiver mutation or an explicit proof that no repo-native mutation remains;
4. population/cutoff/multiplicity/measure/quantifier compatibility checks;
5. a result, discovery ledger, weapon delta, propagation proposal ledger, verifier, and fresh audit;
6. no asymptotic promotion from finite data.

An earlier theorem may remain closed while its mechanism is refined. Use separate fields:

```text
THEOREM_INTERFACE_VALID=true|false
REENTRY_RESEARCH_COMPLETE=true|false
STRONGER_RESULT_PROVED=true|false
NEW_REUSABLE_WEAPON_PROVED=true|false
```

## Derived-discovery propagation

Each phase writes `backflow-proposals.json`. Every proposal contains:

```text
PROPOSAL_ID=
ORIGIN_TASK=
AFFECTED_STAGES=
CLAIM_OR_WEAPON=
POPULATION_MATCH=
CUTOFF_MATCH=
MULTIPLICITY_MATCH=
MEASURE_MATCH=
QUANTIFIER_MATCH=
NOVELTY_CLASS=NEW|STRENGTHENING|SUPERSESSION|NEGATIVE_CERTIFICATE
ACTION=APPLY_NOW|QUEUE_DERIVED_ROUTE|DEFER_TO_STAGE26_28|NO_ACTION
AUDIT_REQUIRED=true|false
```

Rules:

- A theorem-changing backflow is applied only after fresh audit PASS.
- A new mathematically distinct route receives the next unused Stage25 pre-stage serial, beginning with `Stage25-um-r008a`.
- A refinement keeps its existing route ID; IDs are never recycled.
- At most three derived routes may be `ACTIVE` simultaneously. Additional proposals remain queued.
- A derived route cannot recursively launch another route before its own parent phase is audited.
- A proposal affecting multiple stages must name every affected stage and perform the complete compatibility map for each.
- Negative results require a source-level certificate; `no result found` is not closure.

## Stop and handoff

Stage26 becomes allowed only when:

```text
STAGE25_MAIN_CLOSED=true
ALL_REENTRY_PHASES_AUDITED=true
DERIVED_ROUTE_QUEUE_HAS_UNRESOLVED_INTERNAL_ROUTE=false
STAGE20_STAGE26_READY_INTERFACE=true
BACKFLOW_SYNCHRONIZED=true
STAGE26_ALLOWED=true
```

Queued items may remain only when classified as `EXTERNAL_THEOREM_GATE` or explicitly deferred to a named Stage26–28 receiver. Repetition of an exhausted Stage14/15 route without a new equation, height relation, same-measure estimate, or external theorem does not block handoff.

## Commands

```text
Stage25-reentry-main-batch
Stage25-reentry-audit
```

One main-batch command executes only the current phase and any already-authorized child work. It does not silently run all seven phases or merge a PR. The final response must state the next phase, live derived routes, queued proposals, and whether a human decision is required.
