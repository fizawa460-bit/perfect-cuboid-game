# Stage25-60 R504/R505/R506 hostile re-audit

Status: **FAIL — prior evidence blocker repaired, but checkpoint60 deep-stop remains blocked by normative-stop and R504 scope/proof issues**

## Scope

This re-audit reviews the hostile-FAIL repair on PR #990. It preserves the previous audit record `r505-r506-audit.md` and does not reopen the already accepted R505/R506 mathematics.

## A. Previous evidence blocker — REPAIRED

The repaired discovery ledger now materializes the required Stage16-28 handoff:

```text
REPO_REUSE_PREFLIGHT=PASS
REUSED_RESULTS=materialized
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=materialized
POPULATION_ADAPTERS_PROVED=materialized
```

The searched paths/terms/signatures and accepted/rejected candidates are also concrete. Therefore the previous reuse/discovery-field blocker is closed.

```text
REPO_REUSE_HANDOFF_COMPLETE=true
DISCOVERY_EVIDENCE_BLOCK_COMPLETE=true
```

## B. R505 / R506 — retained PASS

The previous hostile audit already accepted:

- R505 as the exact Stage19 target receiver `sf(A)=sf(B) iff A=kP^2, B=kQ^2`;
- R506 as the same receiver in rank-one/common-leg coordinates `u=mr, v=ns, w=ms, z=nr`, `uv=wz`;
- the Stage15 common-core reuse chain as relevant.

No new defect was found and no mathematical reopening is required.

```text
R505_EXACT_TARGET_RECEIVER_ACCEPTED=true
R506_TORIC_SUBSUMPTION_ACCEPTED=true
R505_STAGE15_REUSE_CHAIN_ACCEPTED=true
R505_MATHEMATICS_REOPEN_REQUIRED=false
R506_MATHEMATICS_REOPEN_REQUIRED=false
```

## C. R504 BC1 / BC2 — local no-rank-jump certificates accepted

The repair executes two concrete degree-two pullbacks.

For `k=u^2`, the genus-three cover `y^2=u^8+1` has three elliptic quotient factors with j-invariants `1728,8000,8000`. The extra factors have good reduction at `p=3` and point counts different from `E0:y^2=x^3-4x`, so they are not Q-isogenous to `E0`. The quotient differentials span the genus-three differential space, giving the required Jacobian isogeny decomposition. With the inherited section present, the pullback free rank remains one.

For `k=(u^2-1)/(2u)`, the analogous quotient factors have j-invariants `1728,10976,10976`; the complementary factors again have different good-prime trace at `p=3` from `E0`. The same conclusion follows.

```text
R504_BC1_NO_RANK_JUMP_ACCEPTED=true
R504_BC2_NO_RANK_JUMP_ACCEPTED=true
```

These are certificates for the two submitted candidates only; they do not classify all rational degree-two base changes.

## D. Exact Kummer label over Q — CORRECTION REQUIRED

The repair states

```text
R504_KUMMER_MODEL=Km(E0xE0)
```

as an exact Q-model. That is too strong in the submitted form.

Under the already audited identification `C ~= E0`, the deck involution is

\[
Q \mapsto T-Q,\qquad T=(0,0),
\]

not `Q -> -Q`. The hostile R504 audit also proved that `T` is not twice a Q-rational point. Therefore the involution `T-Q` cannot be conjugated to `-Q` by a Q-rational translation. Over an algebraic extension containing a half of `T` it becomes the standard product-Kummer involution, but over Q the safe statement is that the R504 surface is a **Q-form / twisted product-Kummer model** of `Km(E0 x E0)`, not literally the standard Q-Kummer quotient without an additional descent argument.

This does not invalidate BC1/BC2, which were checked directly on the pullback twist covers, but the route-boundary artifact must not use the stronger Q-isomorphism label.

```text
R504_STANDARD_Q_KUMMER_IDENTIFICATION_ACCEPTED=false
R504_SAFE_KUMMER_CLASS=Q_FORM_OR_TWIST_OF_PRODUCT_KUMMER
```

## E. Growing multiples — submitted upper needs the real-component parity lemma materialized

The physical-height identities

\[
(t/k)^2=(H_X-X)/(H_X+X),\qquad (kt)^2=(H_Y+Y)/(H_Y-Y)
\]

correctly imply `h(t) <= 0.5 log(2B)`. The Lattes degree `n^2` and canonical-height comparison then give the submitted `B^(1/n^2)` parameter bound for a fixed multiple.

However the claimed aggregate

\[
N_{R504,all\ multiples}(B) \ll B^{1/9}\sqrt{\log B}
\]

uses `n>=3`, i.e. it requires that every nondegenerate physical quartic point comes from an odd multiple. The repair says "odd physical multiples" but does not prove that this exhausts all physical multiples.

The missing lemma is available but must be made explicit: for `F=k^4+1>0`, quartic images satisfy

\[
X=-\frac{4Ft^2}{t^4+1}\in[-2F,0],
\]

which is the bounded/non-identity real component of

\[
E_F:y^2=x(x-2F)(x+2F).
\]

The generator `P` lies on that non-identity component. Since `E_F(R)/E_F(R)^0 ~= Z/2`, odd multiples remain on the bounded component and even multiples lie on the identity component `x>=2F`; hence even multiples cannot be real quartic images. This is the needed reason that the first possible nondegenerate physical multiple is `n=3`.

Until this parity lemma is materialized in the route certificate/verifier, the exact all-multiples `O(B^(1/9)sqrt(log B))` theorem is not accepted as submitted.

```text
R504_GROWING_MULTIPLE_HEIGHT_ARGUMENT_CORE_ACCEPTED=true
R504_ALL_PHYSICAL_MULTIPLES_ODD_LEMMA_MATERIALIZED=false
R504_ALL_MULTIPLES_COUNT_UPPER_ACCEPTED=false
```

This is a narrow repair; it does not require new input.

## F. Normative checkpoint60 stop rule — SELF-RELAXATION REJECTED

The current `main` version of `continuation-policy.md` is marked `STATUS=NORMATIVE_FOR_STAGE25_60_CONTINUATION` and requires, for deep stop:

- every assigned route to be `CLOSED_PROVED`, `CLOSED_NO_UPGRADE_WITH_CERTIFICATE`, or `EXTERNAL_THEOREM_GATE`;
- no compatible repo-native attack remains live;
- remaining open items require genuinely new **external mathematics**, not another unexecuted repo-native mutation.

PR #990 modifies this same normative policy while submitting itself for closure, changing the final condition to allow "genuinely new parametric input" and narrowing the prohibition to mutations "of an existing normal form". This is a material relaxation of the acceptance criterion and cannot be used by the same submission to certify its own deep stop.

The repaired R504 residual is currently

```text
EXTERNAL_OR_NEW_EXPLICIT_CURVE_GATE
```

and explicitly asks for an exceptional rational base change/multisection `phi` with an extra `E0` factor in `J(C_phi)`. That is a precise and useful research gate, but it is not the existing normative `EXTERNAL_THEOREM_GATE`, and an explicit `phi` is potentially repo-native/new-parametric work rather than external mathematics.

Therefore checkpoint60 must continue under the unmodified normative stop rule unless a separately audited policy change is made outside the closing submission.

```text
CONTINUATION_POLICY_SELF_RELAXATION_ACCEPTED=false
R504_RESIDUAL_DEEP_STOP_CLASS_ACCEPTED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

## Verdict

The repair materially improved R504 and fixed the mandatory evidence handoff, but it does not yet satisfy checkpoint60 closure.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
AUDIT_VERDICT=FAIL
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
REPO_REUSE_HANDOFF_COMPLETE=true
DISCOVERY_EVIDENCE_BLOCK_COMPLETE=true
R505_EXACT_TARGET_RECEIVER_ACCEPTED=true
R506_TORIC_SUBSUMPTION_ACCEPTED=true
R504_BC1_NO_RANK_JUMP_ACCEPTED=true
R504_BC2_NO_RANK_JUMP_ACCEPTED=true
R504_STANDARD_Q_KUMMER_IDENTIFICATION_ACCEPTED=false
R504_SAFE_KUMMER_CLASS=Q_FORM_OR_TWIST_OF_PRODUCT_KUMMER
R504_ALL_PHYSICAL_MULTIPLES_ODD_LEMMA_MATERIALIZED=false
R504_ALL_MULTIPLES_COUNT_UPPER_ACCEPTED=false
CONTINUATION_POLICY_SELF_RELAXATION_ACCEPTED=false
R504_RESIDUAL_DEEP_STOP_CLASS_ACCEPTED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
R505_MATHEMATICS_REOPEN_REQUIRED=false
R506_MATHEMATICS_REOPEN_REQUIRED=false
REPAIR_SCOPE=RESTORE_NORMATIVE_STOP_RULE;CORRECT_Q_KUMMER_LABEL;MATERIALIZE_REAL_COMPONENT_PARITY_LEMMA;KEEP_R504_RESIDUAL_LIVE_OR_SEPARATELY_JUSTIFY_POLICY_CHANGE
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=Stage25-main-batch
```
