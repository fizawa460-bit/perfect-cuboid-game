# Research credit and promotion firewalls

Purpose: prevent local computations, partial models, bounded evidence, or intermediate proofs from being promoted beyond the scope they actually establish.

This policy is **repository-wide and mandatory**. It consolidates recurring safety rules that appeared independently across Stage16-29 and then reappeared in Stage32-33 controllers and hostile audits. Stage-local controllers may add stricter conditions, but must not weaken these rules.

## 1. Audit gate before promotion

No new mathematical, computational, receiver, theorem, endpoint, or downstream dependency credit is authoritative merely because a computation finished, a proof draft exists, CI is green, or a PR is ready.

Promotion requires the audit state demanded by the active Stage contract. Where a hostile/fresh audit is required, the pre-audit result remains provisional.

`PASS`, `COMPLETE`, `READY`, `CI_SUCCESS`, and similar operational labels must not be treated as interchangeable with audited mathematical closure.

## 2. Keep credit layers separate

Never collapse distinct credit layers.

```text
COMPUTATIONAL_EVIDENCE
!= NUMERICAL_CREDIT
!= RECEIVER_DISCHARGE
!= THEOREM_CREDIT
!= EFFECTIVITY_OR_EXISTENCE_CREDIT
!= ENDPOINT_OR_FINAL_PROBLEM_CREDIT
```

A lower layer may support a higher layer only through an explicit audited adapter or proof.

In particular:

- a successful finite computation does not by itself prove a theorem;
- discharging one receiver does not discharge its parent route unless the dependency contract says so;
- theorem credit does not imply a final perfect-cuboid existence/nonexistence conclusion unless the endpoint adapter is proved.

## 3. Finite, bounded, sampled, or empirical evidence is not a global theorem

Finite census results, bounded exhaustive searches, finite zero hits, fitted exponents, monotone trends on a grid, numerical slopes, representative shards, and finite regression panels must not be promoted to:

- asymptotic laws;
- global nonexistence;
- true growth exponents;
- limiting ratios;
- complete classification outside the certified bound;
- impossibility of an unresolved route.

A bounded result is authoritative only on its certified bounded domain unless a separate proof extends it.

## 4. Do not infer the true exponent or asymptotic from unmatched bounds

Upper and lower bounds, even when both strong, do not identify the true exponent or leading asymptotic unless they match at the required scale or an independent theorem proves the identification.

Finite effective exponents or regression fits do not close an exponent gap.

Never convert:

```text
lower exponent <= true exponent <= upper exponent
```

into a claimed equality without proof.

## 5. Preserve semantic contracts; transfers require adapters

Population, object, measure, cutoff, multiplicity, primitivity, ordering, field, height, quotient, coordinate, and mask semantics are load-bearing.

Never automatically transfer a result between two objects merely because they are closely related.

Examples requiring an explicit audited adapter when relevant include:

- matched population-size ratio vs literal objectwise survival probability;
- exactly-k stratum vs at-least-k host;
- raw incidence count vs canonical object count;
- one height/cutoff vs another;
- primitive vs nonprimitive populations;
- ordered/canonical vs unordered objects;
- a subfamily vs the ambient family;
- local/fixed-packet/fixed-height claims vs a whole-family claim;
- one geometric polarization/model vs another.

If no adapter is proved, retain the result only in its original semantic scope.

## 6. No automatic transfer from quotient, finite group, geometric closure, or extension field to the original global object

A theorem proved after simplifying the arithmetic/geometric object must stay at that level until descent/lift/inflation is proved.

In particular, do not automatically promote:

- finite-group or finite-quotient cohomology to absolute-Galois closure;
- a statement over `Qbar` to `Q`;
- a statement over `Q(i)` or another extension field to `Q`;
- a quotient/K3/cover result to the original surface;
- geometric existence of a lift to arithmetic existence of a rational lift.

Field-of-definition and descent are explicit firewalls, not bookkeeping details.

## 7. No double charge, fake product saving, or unsupported independence

A saving, sparsity factor, probability loss, interaction factor, local condition, squareclass restriction, or structural deficit may be charged at most once unless an audited argument proves a genuinely independent second factor.

Do not multiply together bounds merely because they arise from differently named routes.

Do not infer independence or correlation signs from:

- path-factor identities;
- separate upper bounds;
- separate positive invariants;
- local products;
- two descriptions of the same physical restriction.

Every product saving must identify distinct sources of saving and prove that both remain available under the same measure, weights, masks, and quantifiers.

## 8. Effectivity/existence is separate from lattice, class, orbit, or cohomological enumeration

Enumerating an admissible class, Picard vector, orbit, cohomology class, formal carrier, divisor class, or numerical candidate does not by itself prove that an effective geometric or arithmetic object exists.

Where the research question needs an actual curve, rational point, divisor, family, or physical cuboid, effectivity/existence must receive its own proof or explicit receiver credit.

Numerical orbit census is not curve classification unless effectivity and carrier conditions are independently closed.

## 9. Only closed dependencies release downstream credit

A downstream unit may consume an upstream result as authoritative only when the upstream dependency is in the closure state required by the active controller.

Default Research OS rule:

```text
DOWNSTREAM_RELEASE_REQUIRES_AUDITED_CLOSED_DEPENDENCY=true
```

`RUNNING`, `READY`, `PENDING_AUDIT`, `BLOCKED`, provisional `PASS`, or merely successful Actions do not release mathematical credit downstream.

A Stage may define a narrower explicit exception, but it must name the exact provisional interface and prohibit theorem/endpoint promotion from that provisional input.

## 10. Hostile audit may revoke, downgrade, supersede, or reopen prior credit

Historical PASS/CLOSED status is not protected against a later audit that discovers a broken assumption, scope regression, invalid transfer, missing adapter, or stronger new input.

When a later audit materially invalidates an earlier promoted claim:

- do not preserve the old credit for convenience;
- record the exact reason;
- downgrade or reopen the affected unit;
- block downstream release that depended on the invalidated claim;
- retain unaffected historical results explicitly rather than rewriting history.

A later stronger theorem may supersede an older bound without declaring the older proof false. Distinguish `SUPERSEDED` from `REVOKED`.

## 11. Finite failure or a blocked route is not impossibility

A finite search yielding zero survivors, one parameter family failing, one model being blocked, one theorem window missing, or one candidate route closing does not establish nonexistence of the target or exhaustion of all mathematically distinct routes.

Use the Cycle Exploration Safety Protocol before parking a receiver or claiming that no route remains.

## 12. Final-problem claims require explicit endpoint authorization

No intermediate Stage may infer either existence or nonexistence of a perfect cuboid merely because a population is sparse, a finite endpoint census is zero, a Brauer/K3/Picard component is closed, or a strong upper/lower bound is proved.

A final-problem claim requires an explicit audited endpoint theorem/adapter whose scope is the full physical problem.

Unless such a certificate exists, keep both flags false:

```text
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Required use in future controllers

New Stage controllers should inherit this policy rather than restating all generic rules. Recommended field:

```text
"research_credit_firewalls": {
  "policy": "docs/research-os/policies/research-credit-and-promotion-firewalls.md",
  "inherited": true,
  "stage_local_overrides_may_weaken": false
}
```

Stage-local controller fields remain authoritative for the current numerical values, statuses, exact dependencies, and any stricter specialized firewalls.

## Relationship to other Research OS policies

This policy governs **credit and promotion scope**.

- `cycle-exploration-safety-protocol.md` governs breadth, route preservation, no-recharge, and parking.
- `actions-storage-and-evidence-safety.md` governs compute/storage/concurrency/evidence safety.
- `self-contained-review-standard.md` governs review completeness.
- `codex-task-scope-stop-policy.md` governs bounded execution scope.

These policies are cumulative. Passing one does not waive another.
