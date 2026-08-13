# Self-contained mathematical review standard

```text
STANDARD_ID=SELF_CONTAINED_REVIEW_STANDARD_V1
STATUS=ACTIVE
PRECEDENTS=Stage12_R09,Stage13_R07,Stage14_R06
DEFAULT_LABEL=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
SUMMARY_ONLY_IS_SELF_CONTAINED=false
TOP_LEVEL_REVIEW_ROOT=ACTIVE_RENDERED_REVIEW_ARTIFACTS_ONLY
```

## 1. Purpose

This document fixes the project-wide meaning of a **self-contained mathematical review** so that later stages do not silently weaken the standard.

The precedents are the active Stage12 R09, Stage13 R07, and Stage14 R06 review bundles. Stage14 is especially important: external hostile review found that several already-proved internal steps had been compressed to citations or short assertions, and the bundle was repaired by transcribing those proofs without changing the theorem. That repair pattern is the default rule for future stages.

A self-contained review is not merely an executive summary with repository paths. It is a proof-facing artifact that a fresh mathematical reviewer can audit without browsing the repository, except for theorem-level external literature explicitly declared as an external input.

## 2. Canonical boundary

The default project status is

`SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS`.

This means:

1. **Internal load-bearing mathematics is physically present.** Every project-internal lemma, adapter, normalization, multiplicity statement, measure transfer, cutoff identification, local-density computation, or quantifier step needed for the final implication chain is stated and proved, or transcribed in proof-complete form, inside the review artifact.
2. **Published external theorems may remain external.** Their full proofs need not be reproduced. The review must state the exact working form used, list the hypotheses that matter, map those hypotheses to the current object, and state all uniformity/quantifier limitations.
3. **A completed earlier Stage may be a frozen interface.** Its theorem need not be re-proved if the current Stage uses exactly the same statement, population, cutoff, and multiplicity convention. The interface statement must nevertheless be printed exactly enough to audit the transfer. If the new Stage changes the measure, height, population, orientation, multiplicity, or quantifier order, the required adapter is internal and must be proved in the current review.
4. **Repository paths are provenance, not proof.** A sentence of the form “Stage X proved Y; see path” is insufficient when Y is load-bearing inside the current Stage.
5. **Finite computation is separate from theorem proof.** Reproducibility checks and finite data may be included, but they cannot replace a mathematical implication.
6. **No hidden asset dependency.** A rendered HTML review intended to be standalone must not require remote CSS, JavaScript, fonts, images, MathJax, CDN assets, or live repository access to understand the proof chain.

## 3. What must be embedded

Embed the proof, not merely the conclusion, whenever a step answers any of these questions:

- Why is the counted population the intended physical population?
- Why is the cutoff/height exactly the same, or what is the exact adapter?
- Why is a parametrization exhaustive and what is its multiplicity?
- Why does a compactification/resolution have the claimed geometry or Picard rank?
- Why may an external theorem be applied to this object and this measure?
- Why is a thin or exceptional locus negligible?
- Why is an arithmetic normal form equivalent in both directions?
- Why does a local density have the printed value?
- Why do local conditions tensor, and in what order may limits be taken?
- Why is an averaged/fixed-modulus theorem being used at the legally matching level?
- Why is a saving not double charged or cross-promoted from another population?
- Why does the final theorem follow from the preceding chain?

Non-load-bearing historical discussion, route archaeology, abandoned candidates, and diagnostic detail may be summarized with provenance links.

## 4. External theorem contract

For each external published theorem, print a compact contract with these fields:

```text
THEOREM=<author/result>
WORKING_FORM=<exact statement used>
OBJECT=<variety/measure/family to which it is applied>
HYPOTHESES_CHECKED=<list>
HEIGHT_OR_MEASURE_MATCH=<exact equality or proved adapter>
LOCAL_OR_ARCHIMEDEAN_RESTRICTIONS=<what is allowed>
QUANTIFIERS=<fixed parameters before the main limit>
UNIFORMITY_NOT_CLAIMED=<explicit limitations>
ROLE=<main term / equidistribution / thin-set removal / etc.>
```

Do not write “standard theorem applies” when any hypothesis, measure, height, exceptional set, or uniformity statement is load-bearing.

## 5. Frozen earlier-stage interface contract

A prior completed stage can be imported without reproducing its full proof only when all of the following are explicit:

```text
UPSTREAM_STAGE=<stage>
UPSTREAM_THEOREM=<exact theorem statement>
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

If any field is false, the current review must supply the missing adapter proof. This is the Stage12→13 and Stage14→15 style boundary: the upstream theorem can be frozen, but the new-stage interface cannot be hand-waved.

## 6. Required review structure

The default template is:

1. **Bundle identity / immutable snapshot**
   - bundle ID, source snapshot, theorem status, review status.
2. **Executive theorem statement**
   - strongest proved claims and theorem species.
3. **Scope, definitions, population, cutoff**
   - primitive/canonical/orientation conventions and non-claims.
4. **Frozen upstream interfaces**
   - exact statements imported from completed stages.
5. **Internal proof chain in dependency order**
   - theorem/lemma/proposition statements and proof-complete derivations.
6. **External theorem contracts and hypothesis maps**
   - exact working interfaces only; no need to reproduce published proofs.
7. **Exceptional/thin/boundary/measure audit**
   - no silent population changes.
8. **Quantifier and uniformity audit**
   - especially fixed versus growing moduli/prime sets.
9. **Finite computation / deterministic verification**
   - explicitly diagnostic or reproducibility-only unless mathematically proved otherwise.
10. **Negative knowledge and non-claims**
    - matching lower bounds, existence questions, effective rates, etc.
11. **Provenance/source ledger**
    - paths and immutable identifiers.
12. **Fresh hostile-review checklist**
    - every load-bearing implication can be checked from the artifact.
13. **Machine-readable lock**
    - theorem scope, external-input boundary, self-containment status, audit requirement.

The order may change for readability, but none of the load-bearing categories may disappear.

## 7. HTML construction template

A standalone HTML review should include:

```html
<header>
  bundle identity / theorem status / review status
</header>
<nav>
  internal fragment links only
</nav>
<main>
  theorem and scope
  exact definitions and interfaces
  internal proof chain
  external theorem contracts
  audits, non-claims, provenance
  machine-readable lock
</main>
```

Default asset policy:

```text
INLINE_CSS=true
REMOTE_JAVASCRIPT=false
REMOTE_STYLESHEET=false
REMOTE_FONT=false
REMOTE_IMAGE=false
MATHJAX_OR_CDN_REQUIRED=false
LIVE_REPOSITORY_ACCESS_REQUIRED_FOR_PROOF=false
INTERNAL_FRAGMENT_NAVIGATION_ONLY=true
```

Mathematics may be rendered with plain Unicode, HTML, MathML, or another fully embedded representation. Readability is secondary to preserving the exact mathematical content.

## 8. Review-root placement policy

The top-level `review/` directory is reserved for **active rendered review artifacts**. Do not place the standard/template document there, because that would mix operating policy with review targets and would undo the Stage12-style final/manifest/archive layout.

This standard therefore lives at:

`docs/self-contained-review-standard.md`

The documentation index must link to it. Each new stage that creates a final self-contained review should also reference this standard from its controller, manifest, or build/audit contract.

## 9. Build and audit gates

Before a self-contained review may be frozen:

```text
INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
EXTERNAL_THEOREM_WORKING_FORMS_STATED=true
EXTERNAL_HYPOTHESES_MAPPED=true
UPSTREAM_INTERFACES_EXACT=true
POPULATION_AND_CUTOFF_AUDITED=true
MULTIPLICITY_AUDITED=true
MEASURE_AND_EXCEPTIONAL_SETS_AUDITED=true
QUANTIFIERS_AND_UNIFORMITY_AUDITED=true
FINITE_DATA_PROMOTED_TO_THEOREM=false
REMOTE_REQUIRED_ASSETS=false
FRESH_HOSTILE_REVIEW=PASS
```

A deterministic verifier may check structure, markers, hashes, offline assets, and selected algebraic identities. It does not replace the fresh mathematical review.

## 10. Failure modes

The following are automatically **not self-contained** until repaired:

- a load-bearing assertion is supported only by a repository path;
- an internal proof is replaced by “proved in Stage X” when Stage X is part of the current bundle rather than a frozen upstream theorem interface;
- an external theorem is named without the working form or hypothesis map;
- a comparable height is silently treated as the exact physical cutoff;
- an almost-all/average result is charged to every fixed packet without an exceptional-set bridge;
- a local density is printed without its population/measure computation;
- a fixed finite-modulus theorem is silently used with a modulus growing with the main parameter;
- a parametrization is used without exhaustiveness/multiplicity control;
- a thin or excluded population is simply dropped without a theorem;
- an offline artifact requires live links or remote runtime assets for mathematical comprehension.

## 11. Change discipline

Changing this definition is a project-level policy change, not a stage-local editorial change.

Any future relaxation or strengthening must:

1. modify this file explicitly;
2. explain why Stage12 R09 / Stage13 R07 / Stage14 R06 precedent is being changed;
3. update affected controllers/verifiers;
4. receive a fresh audit.

Absent such a deliberate change, this V1 standard is authoritative.
