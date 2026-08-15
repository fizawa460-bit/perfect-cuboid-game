# Stage25-40 fresh audit

Status: **PASS**

## Scope

Fresh audit of checkpoint40 upper-bound provenance, the no-fake-product firewall, discovery/reuse evidence, controller-history preservation, and the localized fixed-finite-curve deduction.

## Accepted mathematics

The source and target interfaces are already audited:

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Hence

\[
\boxed{
\frac{N_2(B)}{M_1(B)}
\ll_\varepsilon
B^{-3/2+\varepsilon}(\log B)^{-1}
}.
\]

This agrees with both exact count-cancellation paths

\[
\frac{N_2}{M_1}=\frac{M_2}{M_1}\frac{N_2}{M_2}
\]

and

\[
\frac{N_2}{M_1}=\frac{N_1}{M_1}\frac{N_2}{N_1}.
\]

No independence statement is used.

The Stage24 thin-cover theorem `N2=o(B(log B)^5)` and the fixed-prime squareclass zero-density route each imply only the weaker qualitative endpoint statement

\[
N_2/M_1=o(B^{-1}(\log B)^4).
\]

They are correctly treated as alternative sparsity proofs and are not multiplied onto the inherited half-power upper.

## Fixed-finite-curve refinement

Stage24-40 proves every fixed physical rational curve has degree at least five with respect to the physical height polarization, hence each fixed curve contributes `O(B^(2/5+o(1)))`; the same polynomial scale is valid for any genuinely fixed finite collection.

Dividing by the Stage25 source asymptotic gives

\[
\boxed{
\frac{N_{2,\mathrm{fixed\ finite}}(B)}{M_1(B)}
=O(B^{-8/5+o(1)}(\log B)^{-1}).
}
\]

The submission correctly does **not** extend this to a `B`-dependent moving family. No uniform implied constant or uniform `o(1)` across such a family has been proved.

## No-fake-product audit

PASS. In particular:

- `(N1/M1)(M2/M1)` is not identified with `N2/M1`;
- Path A and Path B are not multiplied together;
- the local-sieve and thin-cover zero-density mechanisms are not multiplied with the half-power theorem;
- Stage21's log-squared interaction is not charged a second time;
- checkpoint30's missing order-chamber/shared-edge directional adapter remains open and no directional endpoint ratio theorem is reintroduced.

## Discovery/reuse audit

PASS. The checkpoint40 discovery ledger records searched paths, structural signatures, candidates found, accepted candidates, rejected candidates with reasons, population adapters, sublane decisions, and NUM reuse status. No finite computation is used as an asymptotic proof.

The decision not to open a new Stage25-specific upper sublane is acceptable at checkpoint40 because the imported comparison lattice contains no distinct receiver beyond the already-audited Stage24 target-side moving-family obstruction. This is a bounded scope statement, not a global no-known-theorem claim.

## CI and verifier interpretation

The checkpoint40 provenance verifier checks the exponent arithmetic, required firewalls, discovery markers, and preservation of prior checkpoint audit provenance. The earlier checkpoint30 verifier failure on first cp40 submission was a stale `CURRENT_CHECKPOINT==30` assertion; it was correctly made future-checkpoint aware without changing checkpoint30 mathematics.

Current-head deterministic checks before this audit commit:

- Stage25-10 contract audit: SUCCESS;
- Stage25-20 matched-grid replay: SUCCESS;
- Stage25-30 ratio consistency audit: SUCCESS;
- Stage25-40 upper provenance audit: SUCCESS.

CI is supporting evidence for arithmetic/state consistency, not a substitute for the mathematical audit above.

## Non-claims preserved

```text
STRICT_GLOBAL_UPPER_UPGRADE_PROVED=false
HALF_POWER_INTRINSIC_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
DIRECTIONAL_SOURCE_CHANNEL_ADAPTER_PROVED=false
DIRECTIONAL_ENDPOINT_UPPER_REFINEMENT=OPEN_GATE_ADAPTER_REQUIRED
FINITE_DATA_USED_AS_PROOF=false
PERFECT_CUBOID_CONCLUSION=false
```

## Verdict

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
UPPER_BOUND_PROVENANCE_CHECK=PASS
DIRECT_UPPER_CHECK=PASS
PATH_A_UPPER_CHECK=PASS
PATH_B_UPPER_CHECK=PASS
THREE_WAY_UPPER_CONSISTENCY=PASS
NO_FAKE_PRODUCT_SAVING_CHECK=PASS
FIXED_FINITE_CURVE_REFINEMENT_ACCEPTED=true
STRICT_GLOBAL_UPPER_UPGRADE_PROVED=false
DIRECTIONAL_OVERCLAIM_REINTRODUCED=false
CONTROLLER_HISTORY_PRESERVATION=PASS
FINITE_DATA_USED_AS_PROOF=false
COUNTS_RECOMPUTE_REQUIRED=false
MATHEMATICS_REOPEN_REQUIRED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=50
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #983; then Stage25-main-batch
```