# Stage25-reentry-60 weapon delta

STATUS=SUBMITTED_PENDING_FRESH_AUDIT
TASK_ID=Stage25-u20-r006a

## Candidate weapon S25-W05 — raw-pair Euler completion adapter

```text
WEAPON_ID=S25-W05
NAME=RAW_PAIR_EULER_COMPLETION_ADAPTER
TYPE=exact_adapter+theorem_candidate
SOURCE=Stage25-reentry-60
HOST=primitive canonical no-space shared-edge raw pair incidences under R<=B
EXACT_IDENTITIES=P_j=M2,j+M3; P=M2+3M3
DIRECTIONAL_RATE=Theta_j=M3/P_j
TOTAL_RATE=Theta=3M3/P
```

If fresh audit passes, the adapter carries the audited Stage18/20 bounds into the literal completion measure:

\[
B^{-5/6}(\log B)^{-5}\ll_j\Theta_j
\ll_{j,\eta}(\log B)^{-\eta},
\]

\[
B^{-5/6}(\log B)^{-5}\ll\Theta
\ll_\eta(\log B)^{-\eta},
\qquad \eta<1/46,
\]

and supplies

\[
\Theta_j/\Theta_k\to C_k/C_j.
\]

## Why this is reusable

The adapter solves a recurring bookkeeping problem: `M3/M2` compares disjoint object strata and is not literally a survival probability, whereas `Theta_j` and `Theta` are same-measure raw-incidence completion rates. Stage26 can therefore attack the third-face condition directly without inventing a population or multiplicity conversion.

## Inputs retained separately

- S20-W01 remains the quantitative thin-cover upper theorem.
- S20-W02 remains the explicit target lower family.
- S20-W03 remains the local causal blocker law.
- r010a remains the raw-pair denominator identity.
- r011a remains a source-side geometric invariant ledger and is not applied to the K3 target as a fake Picard-rank law.

No savings are multiplied as independent factors.

```text
NEW_REUSABLE_WEAPON_CANDIDATE=true
NEW_REUSABLE_WEAPON_PROVED=false
WEAPON_ID=S25-W05
PRIMARY_RECEIVER=Stage26
SECONDARY_RECEIVERS=Stage27,Stage28
AUDIT_STATUS=PENDING
```
