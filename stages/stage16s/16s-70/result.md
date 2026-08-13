# Stage16S-70 — bounded maximal synthesis / closeout verdict

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage16S has fresh-audited checkpoints 10 through 60. Checkpoint 70 performs only the bounded synthesis allowed by `docs/stage16-28-stage70-policy.md`.

## Intrinsic-status verdict

For the ambient primitive/canonical population

\[
U(B)=\#\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B\},
\]

audited Stage16 gives

\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2).
\]

For Stage16S,

\[
N_S^{all}(B)\sim\frac{B^2}{32G},\qquad
N_S^0(B)\sim\frac{B^2}{32G},
\]

where `G` is Catalan's constant. Hence

\[
\boxed{\frac{N_S^{all}(B)}{U(B)}\sim
\frac{9\zeta(3)}{8\pi G}\frac1B},
\]

and the same leading law holds for `N_S^0(B)/U(B)`.

Therefore:

```text
TRUE_ORDER_SPACE_AT_LEAST=B^2_WITH_LEADING_CONSTANT_1/(32G)
TRUE_ORDER_SPACE_ONLY=B^2_WITH_LEADING_CONSTANT_1/(32G)
INTRINSIC_SPACE_DIAGONAL_POLYNOMIAL_COST=ONE_POWER_OF_B
SPACE_ONLY_FRACTION_WITHIN_SPACE_AT_LEAST -> 1
```

The intrinsic ambient `B^-1` thinning is fully certified. This is not merely a best-known upper exponent.

## Face-condition verdict inside Stage16S

Let

\[
C_F(B)=N_S^{all}(B)-N_S^0(B)
\]

count Stage16S objects with at least one integral face. Audited Stage16S-30 proves, for every `epsilon>0`,

\[
C_F(B)=O_\varepsilon(B^{1+\varepsilon}).
\]

Thus

\[
\frac{C_F(B)}{N_S^{all}(B)}=O_\varepsilon(B^{-1+\varepsilon})\to0,
\qquad
\frac{N_S^0(B)}{N_S^{all}(B)}\to1.
\]

So excluding every integral-face case is asymptotically negligible at the Stage16S quadratic main-term level. The current `C_F` upper bound is not asserted sharp.

## Comparison to Stage17

Stage17 has the audited conditional law

\[
\frac{N_1(B)}{M_1(B)}\asymp\frac{(\log B)^2}{B}.
\]

Stage16S has the ambient control law

\[
\frac{N_S^{all}(B)}{U(B)}\sim C_S/B,
\qquad C_S=\frac{9\zeta(3)}{8\pi G}>0.
\]

Therefore the one-power polynomial loss is already intrinsic to space-diagonal integrality before any face condition. The extra logarithmic profile in Stage17 is a real comparison signal, but Stage16S does not classify it as independence, positive correlation, negative correlation, or a factorization law. That final interaction question belongs to Stage21.

## Bounded StageX-70 synthesis

```text
KNOWN_RESULTS=population contract fixed; deterministic census through B=2000; N_S^all(B) ~ B^2/(32G); N_S^0(B) ~ B^2/(32G); N_S^all/U ~ [9 zeta(3)/(8 pi G)]/B; N_S^0/N_S^all -> 1; C_F(B) <<_epsilon B^(1+epsilon); upper/lower ledgers match at B^2 order; causal intrinsic one-power loss audited
ADDITIONAL_DEDUCTIONS=SPACE_AT_LEAST and SPACE_ONLY have identical leading asymptotic; zero-face exclusion is main-term neutral; the intrinsic space-diagonal polynomial cost matches Stage17's polynomial B^-1 cost while logarithmic profiles differ
CAUSAL_SYNTHESIS=the equation a^2+b^2+c^2=d^2 places ambient triples on the primitive Pythagorean-quadruple locus, reducing cubic ambient order to quadratic; integral-face cases form a lower-order nested-Pythagorean subset and do not generate the Stage16S main term
LOWER_STAGE_REINTERPRETATIONS=Stage16S-20 finite ratios are diagnostics for the later proved asymptotic only; Stage16S-40/50 are direct ledgers from audited Stage16S-30; Stage17's one-power loss is no longer evidence that the polynomial cost is created only by the prior face condition
REFINEMENT_CANDIDATES=effective error term for Hurlimann adapter; sharper asymptotic/order for C_F(B); decomposition of face1/face2/face3 components; quantitative explanation of the Stage17 logarithmic enhancement
NEW_HEURISTICS=NONE
OPEN_GATES=sharp order/asymptotic for C_F(B) remains open; Stage21 owns independence/correlation/interaction classification; no perfect-cuboid endpoint claim
NEXT_STAGE_QUESTIONS=Stage21 should compare Stage16->17 against the audited Stage16S baseline and determine what the logarithmic enhancement means without double charging the intrinsic B^-1 cost
SYNTHESIS_STOP_REASON=further refinement requires a new theorem, sharper divisor/lattice analysis, new literature work, or Stage21 transition analysis outside the Stage16S population-baseline question
SYNTHESIS_STOP_RULE_SATISFIED=YES
```

No earlier checkpoint is reopened. No population, cutoff, primitivity, or canonicalization rule was invalidated.

## Checkpoint classification

```text
CHECKPOINT_10=PROVED_AUDIT_PASS
CHECKPOINT_20=COMPUTED_AUDIT_PASS
CHECKPOINT_30=LITERATURE_ADAPTED_AUDIT_PASS
CHECKPOINT_40=PROVED_LEDGER_AUDIT_PASS
CHECKPOINT_50=PROVED_LEDGER_AUDIT_PASS
CHECKPOINT_60=PROVED_SYNTHESIS_AUDIT_PASS
CHECKPOINT_70=PROVED_CANDIDATE_PENDING_FRESH_AUDIT
POPULATION_CONTRACT_CHANGED=NO
EVIDENCE_LEVELS_COMPLETE=YES
DEPENDENCY_LEDGER_COMPLETE=YES
DOUBLE_CHARGE_CHECK=PASS
```

## Stage-end artifact decisions

Stage16S contains a sharp asymptotic with an external-theorem adapter, a lower-order faceful-complement proof, and a causal interface expected to be used by Stage21. Reconstructing those adapters from scattered checkpoint files would be unsafe. A self-contained interface bundle is therefore included as `stages/stage16s/final.md` with manifest `stages/stage16s/manifest-r01.md`.

No arsenal promotion is proposed. Stage21 can consume the stable audited Stage16S final interface directly, avoiding duplicate sources of truth.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=Stage21 needs a stable proof-facing intrinsic space-diagonal baseline including the Hurlimann adapter and faceful-complement proof.
ARSENAL_PROMOTION_REQUIRED=NO
ARSENAL_CANDIDATES=NONE
```

## Proposed closeout

Stage16S is an auxiliary parallel lane, so closing it does not select or advance the numbered parent stage. After fresh audit PASS:

```text
STAGE_STATUS=CLOSED
ADVANCE_ALLOWED=true
NEXT_STAGE=
STAGE21_BASELINE_READY=true
PARALLEL_LANE=true
```

Until that audit passes, Stage16S remains open at checkpoint 70.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16S
CURRENT_CHECKPOINT=70
CHECKPOINTS_ATTEMPTED=70
CHECKPOINTS_SUBMITTED=70
NEW_CLAIMS=bounded closeout synthesis and Stage21-ready intrinsic-status interface; no stronger asymptotic theorem than audited checkpoints 30-60
REUSED_WEAPONS=Stage16-30,Stage16S-30,Stage16S-40,Stage16S-50,Stage16S-60,Stage17-30,Stage17-60,Hurlimann-2015-after-audited-adapter
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 70 is bounded mathematical synthesis and interface-bundle assembly.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16S-audit
MERGE_ALLOWED=false
```