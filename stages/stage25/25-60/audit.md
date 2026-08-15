# Stage25 checkpoint60 hostile fresh audit

Status: **FAIL — core mathematics accepted; R502 route-boundary repair required**

## Scope

This audit independently attacked the three theorem-level additions in PR #985 and the checkpoint60 exploration/continuation contract:

1. exact causal cross-ratio and corrected product identity;
2. R501 exact primitive-gcd / height-rigidity theorem;
3. R504 generic non-torsion moving section and explicit `3P` section;
4. strongest-known / no-upgrade route classification and checkpoint60 stop discipline.

## Core mathematics — accepted

### Causal cross-ratio

With

\[
F=M_2/M_1,\quad S=N_1/M_1,\quad A=N_2/M_2,\quad T=N_2/N_1,
\]

the identity

\[
I=A/S=T/F=N_2M_1/(M_2N_1)
\]

is exact, and therefore

\[
N_2/M_1=FA=ST=FSI.
\]

Using the audited checkpoint50 backflow gives

\[
I(B)\gg B^{1/4}(\log B)^{-7}\to\infty.
\]

The population-ratio interaction classification `POSITIVE_DIVERGENT` is accepted. No probabilistic-independence or literal-subset inference is introduced.

### R501 primitive-height rigidity

For coprime positive `m,n` in the fixed physical cone, the proof that no prime `>3` divides the primitive gcd is correct, and the 2-adic/3-adic cases give

\[
g=2^{7[m,n\text{ both odd}]}3^{4[3\mid m]}\le10368.
\]

Hence primitive height differs from the raw degree-eight space height by only a bounded factor. Combined with the already-audited R501 lower and the reverse parameter count, the family-specific theorem

\[
N_{R501}(B)=\Theta(B^{1/4})
\]

is accepted. This is not a global ceiling for `N2`.

### R504 generic non-torsion section

The quartic-to-elliptic map is algebraically correct. The section

\[
P(k)=(-4k^2,4k(k^4-1))
\]

specializes at the good fiber `k=2` to the already-audited infinite-order point `(-16,120)`, which rules out generic torsion. The displayed `3P` formulas satisfy the quartic identity and agree with the elliptic group law. The structural claim

```text
R504_GENERIC_NONTORSION_SECTION_PROVED=true
```

is accepted. No stronger global lower is accepted from R504.

## FAIL finding — R502 was dropped from the live set without a no-upgrade certificate

Checkpoint50 explicitly left the Meskhishvili third parametrization as an open fallback route:

```text
R502_MESKHISHVILI_THIRD_FAMILY=OPEN_FALLBACK_SAME_EXPONENT
```

Checkpoint60 now classifies R502 as `SAME_EXPONENT_FALLBACK` and removes it from

```text
live_routes_after_current_audit
LIVE_HIGH_VALUE_ROUTES
NEXT_AFTER_AUDITED_MERGE
```

without proving the analogue of the new R501 rigidity theorem.

The stated reason is only that the third parametrization has maximal homogeneous degree eight. That is not sufficient to certify a primitive physical-height exponent of eight. The entire purpose of R507 was to exclude the possibility that primitive gcd growth or another height collapse changes the effective exponent of a degree-eight family. Applying the stricter R507 standard to R501 but not to R502 is an unsupported asymmetry.

This also conflicts with the checkpoint60 stop rule, which says every assigned route R502-R506 must eventually be `CLOSED_PROVED`, `CLOSED_NO_UPGRADE_WITH_CERTIFICATE`, or `EXTERNAL_THEOREM_GATE` before Stage70. `SAME_EXPONENT_FALLBACK` is not such a certificate.

### Required narrow repair

One of the following is sufficient:

1. **Reopen R502**: put R502 back in the live checkpoint60 route set and continuation handoff; do not claim it is closed/no-upgrade yet; or
2. **Certify R502**: provide source-level formulas plus a primitive-height/multiplicity/exactly-two analysis strong enough to prove that this route cannot exceed exponent `1/4` under the exact Stage19 measure.

No R501, R504, causal-interaction, count, or upstream theorem needs to be reopened for this repair.

## CI status

The submitted head has successful Stage25-10/20/30/40/50/60 deterministic workflows. Those checks support the algebraic identities and regressions, but the current checkpoint60 verifier does not test the R502 live/closed asymmetry above; therefore CI success does not discharge this audit finding.

## Verdict

```text
AUDIT_VERDICT=FAIL
DISCOVERY_AUDIT_VERDICT=FAIL
HOSTILE_AUDIT=true
CORE_MATHEMATICS_VERDICT=PASS
CAUSAL_CROSS_RATIO_ACCEPTED=true
INTERACTION_SIGN_ACCEPTED=POSITIVE_DIVERGENT
R501_EXACT_FAMILY_GROWTH_ACCEPTED=Theta(B^(1/4))
R501_GCD_BOUND_ACCEPTED=10368
R504_GENERIC_NONTORSION_SECTION_ACCEPTED=true
R502_ROUTE_BOUNDARY_ACCEPTED=false
R502_PREMATURELY_REMOVED_FROM_LIVE_SET=true
REPAIR_SCOPE=R502_LIVE_RESTORE_OR_PRIMITIVE_HEIGHT_NO_UPGRADE_CERTIFICATE
COUNTS_RECOMPUTE_REQUIRED=false
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
STAGE70_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=Stage25-main-batch
```
