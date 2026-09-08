# Hostile audit and merge-ready freshness

Purpose: define one repository-wide audit contract that separates research correctness from live Git merge readiness. This policy applies across all Stages. Stage-local controllers, states, and audit contracts may strengthen it, but they must not weaken, redefine, or replace it. Do not copy this policy body into Stage-local files; reference this path instead.

## 1. HOSTILE AUDIT

A hostile audit is an exact-head audit of the research claim, evidence, and authority boundary. It is not, by itself, a live-main merge-readiness test.

A hostile audit primarily checks:

- mathematics and logical validity;
- source locks and dependency identity;
- evidence and certificates;
- verifier correctness;
- required exact-head CI;
- authority provenance;
- research-credit boundaries;
- state, controller, and roadmap consistency;
- semantic adapters;
- claim-promotion firewalls.

If these checks pass for the audited exact head and evidence boundary, report:

```text
HOSTILE AUDIT: PASS
```

A defect in these research-integrity checks may produce `HOSTILE AUDIT: FAIL`. The result remains anchored to the exact audited head, claim/evidence boundary, and audit receipt. A later unrelated Git commit does not retroactively change what was audited.

The repository-wide research-credit policy remains cumulative: hostile-audit PASS does not itself grant a broader theorem, receiver, endpoint, existence/effectivity, or final-problem claim beyond the audited scope.

## 2. FRESHNESS / MERGE-READY is a separate gate

Current-main freshness is a separate operational gate. The following facts, by themselves, are not hostile-audit failures:

- current `main` advanced after the audited exact head was inspected;
- the PR is `behind > 0`;
- the intervening commit changes only an unrelated Stage;
- review of the intervening drift finds no semantic change to the audited mathematics, source/dependency boundary, authority, verifier, or shared contract used by the claim.

In that situation retain the hostile-audit result and report the merge gate separately, for example:

```text
HOSTILE AUDIT: PASS
MERGE-READY FRESHNESS: PENDING — unrelated main drift
```

The behind count is a freshness signal, not a research-correctness verdict.

## 3. Main drift that requires semantic-impact review

Main drift must be inspected for semantic impact when it touches any of the following:

- files in the audited Stage that are part of the audited claim/evidence boundary;
- a source-locked dependency;
- a shared theorem or Arsenal contract consumed by the audited claim;
- a Research OS policy that is load-bearing for the audit or promotion;
- a load-bearing rule in `AGENTS.md`;
- an authority dependency or promotion boundary;
- verifier or workflow semantics used by the audited claim;
- population, field, quotient, model, multiplicity, measure, mask, coordinate, or other load-bearing semantics;
- an actual merge conflict or semantic conflict.

If such drift changes the audited claim/evidence/authority boundary, or if its semantic impact cannot be excluded, re-run the relevant hostile audit on the resulting exact head before treating the prior PASS as sufficient for that changed boundary.

A commit confined to an independent Stage is not, solely by being newer than the audited head, a reason to change `HOSTILE AUDIT: PASS` into FAIL.

## 4. MERGE-READY FRESHNESS

Immediately before an intended merge, evaluate the live merge-ready gate separately. Record at minimum:

- current `main` exact SHA;
- PR ahead/behind counts;
- merge-base;
- relevant intervening drift and its semantic-impact classification;
- CI or replay required by the active Stage/PR contract after synchronization.

Possible reporting states include `CLEAR`, `PENDING`, or `BLOCKED`, with the reason stated explicitly. A PR may therefore be hostile-audit PASS while merge-ready freshness is still pending.

Hostile audit PASS is not merge authorization. A clear freshness gate is also not merge authorization unless the user or active repository contract separately authorizes merge.

## 5. Stage-local strengthening

Stage-local controller/state/audit contracts may impose additional checks, stricter replay requirements, extra source locks, or stronger promotion conditions. They may not:

- make unrelated `behind > 0` drift a repository-wide hostile-audit failure by definition;
- erase a hostile-audit PASS solely because independent main history advanced;
- collapse hostile audit and merge-ready freshness into one gate;
- weaken any repository-wide research-credit, audit, or semantic-adapter firewall.

If a Stage needs stronger rules, state only the additional Stage-local condition and reference this policy for the common definition.

## 6. Audit result, authority promotion, and merge are distinct

Keep these operations distinct:

```text
HOSTILE AUDIT
!= STAGE-LOCAL AUTHORITY / CLAIM SYNCHRONIZATION
!= MERGE-READY FRESHNESS
!= MERGE AUTHORIZATION
```

A Stage may require a separate synchronization or promotion gate before an audited result becomes consumable authority. Hostile-audit PASS does not bypass that gate. A known hostile-audit FAIL or revocation must still fail closed according to the active Stage contract and `research-credit-and-promotion-firewalls.md`.

This policy grants no mathematical theorem credit, no Stage advancement, no EX-to-MAIN promotion, no receiver or endpoint closure, no Perfect Cuboid existence/nonexistence claim, and no merge authorization.

## 7. Recommended audit report

For an audit where freshness is relevant, report the two outcomes independently:

```text
HOSTILE AUDIT: PASS | FAIL
AUDITED EXACT HEAD: <sha>
MERGE-READY FRESHNESS: CLEAR | PENDING | BLOCKED — <reason>
CURRENT MAIN: <sha>
```

When semantic main drift requires a new audit, say so explicitly rather than describing a pure freshness failure as a mathematical or research-integrity failure.
