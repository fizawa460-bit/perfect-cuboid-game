# Stage20-70 audit

Status: PASS

This fresh re-audit follows the prior committed `FAIL_REPAIR_REQUIRED` verdict. The prior mathematical synthesis was already accepted substantively; the only failures were the self-contained-review boundary in `stages/stage20/final.md`.

The bounded repair is now complete and satisfies `SELF_CONTAINED_REVIEW_STANDARD_V1`.

## Repair verification 1: current-Stage load-bearing proof is embedded

The final bundle now transcribes the complete Stage20-50a Saunderson construction in dependency order. For every even integer `m>=10`, with

```text
u=m^2-1,
v=2m,
w=m^2+1,
A=u|4v^2-w^2|,
B1=v|4u^2-w^2|,
C=4uvw,
```

the bundle proves internally:

- `u^2+v^2=w^2` and pairwise coprimality of `u,v,w`;
- all three face-square identities;
- `gcd(A,B1,C)=1` by the prime-divisor argument;
- strict canonical order `0<B1<C<A` for `m>=10`;
- injectivity because `A(m)` is strictly increasing;
- the exact common-cutoff estimate `R<31m^6`.

Hence it proves inside the final artifact

\[
M_3(B)\ge \left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4
\]

for all sufficiently large `B`, and therefore

\[
M_3(B)\gg B^{1/6}.
\]

No repository lookup is needed to audit this current-Stage lower theorem.

## Repair verification 2: frozen upstream interfaces are explicit

The final bundle now prints frozen-interface contracts for Stage14-e8, Stage14-e10 and Stage14-e11 with the required fields:

```text
UPSTREAM_STAGE
UPSTREAM_THEOREM
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

The contracts identify `R_EB(B)=M_3(B)` object-for-object under the same primitive/canonical Euclidean cutoff and one-object multiplicity. Quantifier boundaries are explicit: e10 fixed-prime two-limit logic is not promoted to growing primes, and e11 fixes `eta<1/46` before `B->infinity`; endpoint `eta=1/46` is not claimed.

## Mathematical closeout

The strongest certified same-population upper theorem remains the frozen Stage14-e11 interface:

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}
\qquad(\text{every fixed }\eta<1/46),
\]

with the concrete safe choice

\[
M_3(B)\ll B(\log B)^{5-1/50}.
\]

Together with the internal lower theorem,

\[
\boxed{B^{1/6}\ll M_3(B)\ll B(\log B)^{5-1/50}.}
\]

The true exponent, matching lower bound, asymptotic formula/constant and square-root finite signal remain OPEN_GATES. The local blocker law, K3/thin-cover theorem, divisor envelope and explicit family are not double charged. `Stage18->Stage20` conditional thinning and independence/correlation remain owned by Stage26. No integral-space-diagonal condition or perfect-cuboid conclusion is introduced.

The repository-wide reuse preflight and strongest-known check are retained as PASS. No new theorem or computation was required by the repair. Stage70 bounded synthesis stop rule is satisfied.

```text
CHECKPOINT_STATUS=PROVED_AUDITED_PASS
MATHEMATICAL_SYNTHESIS_STATUS=PASS
SELF_CONTAINED_REVIEW_GATE=PASS
SELF_CONTAINED_BUNDLE_AUDIT=PASS
INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
UPSTREAM_INTERFACES_EXACT=true
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
EVIDENCE_LEVELS_COMPLETE=YES
DEPENDENCY_LEDGER_COMPLETE=YES
OPEN_GATE_REENTRY_JUSTIFIED=NO
ARSENAL_SUPERSESSION_CHECK=PASS
ARSENAL_PROMOTION_AUDIT=PASS
DOUBLE_CHARGE_CHECK=PASS
SYNTHESIS_STOP_RULE_SATISFIED=YES
REPO_REUSE_PREFLIGHT=PASS
STRONGEST_KNOWN_CHECK=PASS
PERFECT_CUBOID_CONCLUSION=NONE

PREVIOUS_AUDIT_VERDICT=FAIL_REPAIR_REQUIRED
PREVIOUS_AUDIT_PERSISTENCE_STATUS=COMMITTED
CURRENT_AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=PENDING_STATUS_SYNC
UNSYNCED_AUDIT_STATE=final.md,manifest-r01.md,20-controller.json,docs/00_CURRENT_RESEARCH_STATUS.md,20-70/result.md,docs/stage20-arsenal.md
ADVANCE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=
NEXT_STAGE=Stage21
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=false
```
