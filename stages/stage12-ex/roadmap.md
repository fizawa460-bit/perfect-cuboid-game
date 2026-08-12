# Stage12-EX — Human External Verification Roadmap

## Purpose

Stage12 is frozen at R09. Stage12-EX does **not** reopen or alter the Stage12 theorem by default.

The purpose of Stage12-EX is to convert the frozen Stage12 proof into small, human-verifiable mathematical units, obtain independent external human feedback where practical, record objections and confirmations precisely, and turn that feedback into a reusable review protocol for Stage13 and Stage14.

Primary frozen source:

```text
review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html
stages/stage12/final.md
stages/stage12/manifest-r09.md
```

Frozen Stage12 theorem target:

```text
C_prim(B) ~ kappa/(12*pi) * B(log B)^3
          = eta/(12*pi^2) * B(log B)^3
```

for the R09-defined primitive oriented distinguished-face population.

## Core policy

1. R09 remains immutable unless a concrete mathematical defect is independently reproduced.
2. Human review is evidence, not authority by itself. Every objection must be reconstructed against the frozen proof before acceptance.
3. One positive comment or answer does not close Stage12-EX.
4. Numerical agreement, CI, hashes, and AI review do not count as mathematical proof.
5. Math StackExchange questions must be focused, self-contained, answerable mathematical questions, not requests to review an entire project.
6. AI usage may be disclosed where relevant, but mathematical claims are presented on their own merits.
7. The goal is correctness verification first. Novelty, exposition, and publication strategy are separate questions.

## Stage12-EX0 — Critical-chain extraction

Build a dependency graph from the R09 theorem back to its essential inputs.

Rank proof nodes by failure impact. At minimum audit and classify:

- Dirichlet-series / Euler-product construction;
- singular factorization near the dominant point;
- exact Selberg–Delange theorem invoked;
- hypothesis mapping for Selberg–Delange;
- extraction of the `B(log B)^3` main term;
- derivation and normalization of `kappa` / `eta`;
- common-scale decomposition and Möbius inversion;
- primitive/oriented counting convention;
- any uniformity or remainder passage required by the final asymptotic.

Output:

```text
stages/stage12-ex/critical-chain.md
```

Every node must be labeled:

```text
INTERNAL_EXACT
STANDARD_EXTERNAL_THEOREM
EXTERNAL_THEOREM_APPLICATION
COUNTING_INTERFACE
CONSTANT_NORMALIZATION
NUMERICAL_ONLY
```

Exit condition:

```text
STAGE12_EX0_CRITICAL_CHAIN_FIXED=true
TOP_HUMAN_REVIEW_TARGETS_RANKED=true
```

## Stage12-EX1 — Core Verification Pack

Create the first human-review question around the single highest-value critical node.

The pack must be readable without the full repository and contain only:

- definitions required for the question;
- precise proposition/lemma being checked;
- all hypotheses;
- the proposed proof;
- any external theorem statement actually used;
- the exact point where verification is requested;
- consequences for the Stage12 theorem if the claim fails.

Do not ask “is my whole proof correct?”. Ask one concrete mathematical question.

Output:

```text
stages/stage12-ex/review-pack/core-question.md
```

Exit condition:

```text
CORE_QUESTION_SELF_CONTAINED=true
CORE_QUESTION_SINGLE_TARGET=true
```

## Stage12-EX2 — Selberg–Delange Verification Pack

Prepare a separate focused review package for the Selberg–Delange step.

It must explicitly show the chain

```text
counting function
-> Dirichlet series
-> Euler product / local factors
-> singular form
-> exact published Selberg–Delange statement
-> hypothesis map
-> main term and logarithmic exponent
-> constant
-> remainder needed by Stage12
```

The reviewer must not need to infer which version of Selberg–Delange is intended.

Output:

```text
stages/stage12-ex/review-pack/selberg-delange-question.md
```

Required checklist:

```text
EXACT_THEOREM_REFERENCE_PRESENT=true
THEOREM_HYPOTHESES_MAPPED=true
SINGULAR_EXPONENT_DERIVED=true
MAIN_CONSTANT_DERIVED=true
REMAINDER_REQUIREMENT_EXPLICIT=true
```

## Stage12-EX3 — Human-readable review document

Produce a compact human review document distinct from the full R09 bundle.

Suggested contents:

1. theorem statement;
2. object being counted;
3. notation table;
4. one-page dependency graph;
5. proof in theorem order;
6. external theorem contract table;
7. critical-risk annotations;
8. non-claims;
9. provenance link back to R09.

Do not include the historical Stage12 exploration unless required for a proof dependency.

Target path:

```text
stages/stage12-ex/stage12-human-review.md
```

Optional later rendering:

```text
review/STAGE12-HUMAN-REVIEW-<date>-R01.html
```

## Stage12-EX4 — Pre-publication adversarial audit

Before posting any question, audit it as a StackExchange question rather than as an internal research artifact.

Check:

- one principal mathematical question only;
- enough context to answer without opening GitHub;
- no giant proof dump;
- no request for general opinions;
- no dependence on AI verdicts;
- no unsupported claim of novelty;
- external theorem cited precisely;
- notation minimized;
- proof attempt shown;
- requested verification point explicit.

Classify readiness:

```text
READY_TO_POST
NEEDS_COMPRESSION
MISSING_HYPOTHESIS
TOO_BROAD
DEPENDENCY_NOT_SELF_CONTAINED
```

No external post is authorized unless `READY_TO_POST`.

## Stage12-EX5 — First Math StackExchange verification

Post the EX1 question only after EX4 readiness.

Record exactly:

- final posted question text;
- URL;
- date;
- edits made after comments;
- every substantive mathematical objection;
- every substantive confirmation;
- whether a response addresses the whole requested claim or only part.

Classify each external response as:

```text
HUMAN_CONFIRMATION
HUMAN_OBJECTION
PARTIAL_CHECK
CLARIFICATION_ONLY
NO_MATHEMATICAL_VERDICT
```

Do not classify by reputation score alone.

Target ledger:

```text
stages/stage12-ex/human-review-ledger.md
```

## Stage12-EX6 — Objection reproduction and repair gate

For every `HUMAN_OBJECTION`:

1. restate it mathematically without rhetoric;
2. locate the exact R09 claim it targets;
3. independently reproduce or refute it;
4. determine theorem impact;
5. classify severity.

Severity:

```text
FATAL
MAJOR
MINOR
NOTE
NOT_REPRODUCED
```

If a real theorem-level defect is reproduced, do not rewrite R09 in place.

Create a repair track and a new candidate review version.

```text
R09_REOPEN_REQUIRED=true/false
```

## Stage12-EX7 — Selberg–Delange external verification

Only after the first question format has proved workable, submit the focused EX2 question.

The goal is to obtain independent scrutiny of the theorem application, not merely recognition that Selberg–Delange exists.

Required review targets:

- exact singular exponent;
- analytic factor regularity;
- theorem-version compatibility;
- uniformity actually needed;
- constant extraction;
- Möbius / primitive transfer interaction if relevant.

Again, all responses enter the human review ledger and pass through EX6 before changing mathematical status.

## Stage12-EX8 — Human Review Ledger closure

Maintain a compact status table for the frozen theorem chain.

Minimum rows:

```text
DIRICHLET_SERIES_AND_EULER_PRODUCT=
SELBERG_DELANGUE_HYPOTHESIS_MAP=
LOG_POWER_3=
MAIN_CONSTANT_KAPPA=
PRIMITIVE_MOBIUS_TRANSFER=
ORIENTED_COUNT_CONVENTION=
FINAL_ASYMPTOTIC_COMPOSITION=
```

Allowed states:

```text
HUMAN_CHECKED_NO_OBJECTION
HUMAN_CHECKED_PARTIAL
OPEN_OBJECTION
AI_ONLY_CHECKED
NOT_EXTERNALLY_CHECKED
NOT_APPLICABLE
```

Stage12-EX is **not** closed merely because one reviewer says the theorem looks correct.

Suggested closure condition:

```text
OPEN_THEOREM_LEVEL_HUMAN_OBJECTIONS=0
CRITICAL_CHAIN_UNEXAMINED_BY_HUMAN=0 or explicitly waived with rationale
R09_REOPEN_REQUIRED=false
```

If full human coverage cannot be obtained, record the exact remaining unchecked nodes instead of declaring success.

## Stage12-EX9 — Transfer protocol to Stage13 and Stage14

Once Stage12-EX has a stable workflow, extract a reusable external-human-verification protocol.

The reusable protocol must specify:

- how to choose critical nodes;
- how to reduce a large proof to answerable questions;
- how to separate theorem correctness from novelty;
- how to ingest human objections;
- how to avoid authority-based acceptance;
- how to version repaired review bundles;
- how to maintain provenance.

Apply next to Stage13 before asking a human to audit the full Stage14 theorem chain, unless a suitable expert independently volunteers to inspect Stage14 first.

Target:

```text
stages/stage12-ex/external-human-review-protocol.md
```

## Stop / split rule

Stage12-EX is a verification program, not a new mathematics campaign.

Split only when the critical chain contains genuinely independent expert domains, for example:

```text
analytic-number-theory / Selberg–Delange
versus
combinatorial primitive/orientation counting interface
```

Do not create many parallel routes merely to obtain more verdicts.

If a review uncovers a new mathematical problem rather than a verification issue, stop Stage12-EX at that gate and open an explicitly named Stage12 repair track.

## External-review ethics and presentation

When interacting with human reviewers:

- do not claim peer review before actual peer review;
- do not present AI consensus as validation;
- do not conceal dependencies needed to check the claim;
- do not pressure an answerer into reviewing unrelated later stages;
- acknowledge useful criticism;
- distinguish the author's responsibility from AI assistance;
- follow the rules of the external venue.

## Final Stage12-EX report

At completion report:

```text
STAGE12_EX_STATUS=
HUMAN_REVIEW_QUESTIONS_POSTED=
SUBSTANTIVE_HUMAN_RESPONSES=
HUMAN_CONFIRMATIONS=
HUMAN_OBJECTIONS=
REPRODUCED_MAJOR_OR_FATAL_OBJECTIONS=
OPEN_THEOREM_LEVEL_HUMAN_OBJECTIONS=
R09_REOPEN_REQUIRED=
STAGE13_EX_PROTOCOL_READY=
STAGE14_HUMAN_REVIEW_PREPARATION_READY=
```

The strongest acceptable conclusion without formal publication peer review is a precise statement of what independent human readers checked and what remains unchecked. Do not upgrade Stage12-EX completion into a claim of journal-level validation.