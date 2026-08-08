# Stage13 — Structural Origin of the 2:1:1 Ratio

## Goal

Stage13 explains the finite primitive canonical near-`2:1:1` one-face ratio,
its geometric/arithmetic mechanisms and the directional asymptotic law, using
Stage12 R09 as a frozen prior input.

## External-review repair history

```text
R01: OPEN
  - circular raw direction-neutrality
  - under-derived fixed-modulus overlap transfer

13-12aa: structural non-circular common-factor repair
13-12ab: structural fixed-local overlap repair
13-12ac: neutral R02 single-file review bundle

R02 Grok:   OPEN
R02 Claude: REPAIRABLE
```

The R02 reviewers agree that the R01 circularity was genuinely repaired. Their
common remaining objection is quantitative analytic closure of the new `j=0`
route; Grok also keeps two p-adic overlap-side details open.

Current status:

```text
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE
STAGE13_GLOBAL_REVIEW_STATUS=OPEN
NEXT=Stage13-12ae
```

---

## Original phases

```text
13-1   definition / counting convention                     [complete]
13-2   structural decomposition                             [complete]
13-3   leading-2 finite mechanism                           [complete finite diagnostic]
13-4   two-near-1 finite mechanism                          [complete finite diagnostic]
13-5   deviation coordinates                                [complete]
13-6   finite deviation classification                      [complete]
13-7   original asymptotic chain                            [historical; superseded in disputed parts]
13-8   Stage12 bridge                                       [historical complete]
13-9   main structural theorem                              [historical statement]
13-10  final explanation                                    [historical statement]
13-11  Stage13-only R01 bundle                              [complete]
```

The exact finite projection bridge remains active:

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B).
\]

---

## 13-12 external-review repair sequence

### 13-12aa — non-circular raw common factor [complete]

Proves the theorem shape

\[
A_q(B)\sim\Theta J_qB(\log B)^3
\]

before Stage12 calibration. This repairs the R01 circular definition of the
directional constants.

```text
STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
R01_DIRECTION_NEUTRALITY_CIRCULARITY=REPAIRED_STRUCTURALLY
```

### 13-12ab — fixed-local overlap transfer [complete structurally]

Replaces the old “same machinery” sentence with a finite Euler-factor
replacement identity for fixed local conditions, followed by the fixed-`k`,
`B->infinity`, then `k->infinity` squeeze.

R02 accepted the direction of this repair but Grok requested a stronger
all-valuation p-adic derivation.

### 13-12ac — R02 re-synthesis [complete]

Published

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html
```

with neutral verdict instructions and explicit supersession of old 7jb/7jf.
The R02 snapshot is not mutated after review.

### 13-12ad — quantitative `j=0` analytic closure [complete]

Targets the common R02 analytic objections.

#### Uniform Wiener bound

Fix

\[
\delta=1/8,\qquad\sigma=5/8.
\]

The coefficientwise proof gives, uniformly for every split `q>=13` and every
angular phase,

\[
\boxed{\|C_{\ell,q}-1\|_{5/8}\le529q^{-5/4}.}
\]

The finite split prime `q=5` is separated. Hence the global mixed correction is
weighted-`l1` uniformly over the retained harmonic family.

#### Curved/harmonic error budget

Use

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
finite-order A = 48
```

Then

```text
small height                 O(B (log B)^(9/4))
small coordinate             O(B (log B)^(5/2))
mixed log shifts             O(B (log B)^2)
rectangle power tails        B (log B)^C exp(-c (log B)^(1/4))
curved boundary / mesh       O(B (log B)^(-5))
Vaaler excess                O(B (log B)^(-1))
retained harmonics on core   O(B (log B)^(-6))
```

Every term is lower order than `B(log B)^3`.

The Gaussian-Hecke input is now stated with explicit angular-conductor
dependence and concrete `K,A`; it is no longer referenced only as “same
machinery”.

Assets:

```text
stages/stage13/13-12ad/result.md
stages/stage13/scripts/13-12ad/j0_quantitative_closure_audit.py
stages/stage13/data/13-12ad/j0_quantitative_closure_audit_report.json
```

Status:

```text
CLAUDE_R02_WEIGHTED_L1_UNIFORMITY=REPAIRED
CLAUDE_R02_NONZERO_HARMONIC_LOWER_ORDER=REPAIRED
GROK_R02_ZERO_MODE_CURVED_TRANSFER=REPAIRED
RAW_DIRECTIONAL_ANALYTIC_CORE=RESTORED_WITH_EXPLICIT_ERROR_BUDGET
```

### 13-12ae — exact p-adic overlap/local-state closure [NEXT]

This step must address only the remaining Grok R02 overlap objections.

Required outputs:

```text
1. Explicit local state table for every inert-prime valuation stratum relevant
   to the tagged raw coefficient system, including primitivity and OE/EE
   compatibility.

2. Exact or explicitly majorized positive-valuation local mass giving
      tail / L_{p,0}(1,1,1) <= C0/p
   with a concrete absolute C0.

3. A concrete p0 for which every inert p>p0 satisfies lambda_p<=3/4.

4. Direct verification that every genuine pair overlap maps into the constrained
   tagged local population on every state used by the Euler factor.
```

No R03 bundle should be produced until this is complete.

### 13-12af — R03 re-review [blocked]

Only after 13-12ae closes the p-adic/local-state issues:

```text
regenerate current proof
publish neutral Stage13-only R03 HTML
request fresh independent review
```

---

## Current dependency graph

```text
Stage12 R09 frozen total
        |
        +--------------------+
        |                    |
        v                    v
13-3d factor-2 bridge   chamber I_q / J_q
        |                    |
        +---------+----------+
                  v
            13-12aa
     non-circular common form
                  |
                  v
            13-12ad
 quantitative j=0 closure
                  |
                  v
        RAW DIRECTIONAL CORE
                  |
                  v
            13-12ae
  exact p-adic overlap closure
                  |
                  v
      EXACT-ONE THEOREM CANDIDATE
                  |
                  v
            13-12af R03
```

## Current status

```text
RAW_DIRECTIONAL_ANALYTIC_CORE=RESTORED_WITH_EXPLICIT_ERROR_BUDGET
P_ADIC_POSITIVE_VALUATION_TAIL=PENDING_13_12AE
LOCAL_STATE_REFINEMENT_COMPLETENESS=PENDING_13_12AE
EXACT_ONE_THEOREM_EXTERNAL_STATUS=OPEN
STAGE13_GLOBAL_REVIEW_STATUS=OPEN
NEXT=Stage13-12ae
```
