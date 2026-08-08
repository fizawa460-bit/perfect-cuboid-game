# Stage13 — Structural Origin of the 2:1:1 Ratio

## Goal

Stage13 explains the finite primitive canonical near-`2:1:1` one-face ratio,
its geometric/arithmetic mechanisms, and the justified directional asymptotic
law, using the frozen Stage12 R09 primitive oriented theorem as a prior input.

## Review precedence after R01

The original Stage13-1 through Stage13-10 chain was completed and packaged as a
single-file R01 review bundle. One external review returned `OPEN` with two
substantive objections:

1. the old 7jb direction-neutral raw `j=0` constant check was circular;
2. the 7jf fixed-modulus transfer in the pair-overlap sieve needs an independent
   theorem-level audit.

The old `STAGE13=COMPLETE` flags are therefore historical until the 13-12
repair sequence is closed.

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_1_THROUGH_10=HISTORICALLY_COMPLETE
STAGE13_EXTERNAL_REVIEW_R01=OPEN
STAGE13_GLOBAL_REVIEW_STATUS=OPEN
```

---

## Phase 1 — Define and decompose

### 13-1 Definition — complete

Primitive canonical object, space-diagonal cutoff, exactly-one condition and
`ab/ac/bc` directional labels.

### 13-2 Structural decomposition — complete

Raw incidence, overlap correction, chamber, orientation, primitive, parity,
representation multiplicity, local density and boundary layers.

---

## Phase 2 — Explain the finite directional shape

### 13-3 Leading-2 finite mechanism — complete at finite diagnostic level

Canonical archimedean geometry creates the `ab` excess; supported-shell
richness materially flattens it at accessible cutoffs.

### 13-4 Two-near-1 finite mechanism — complete at finite diagnostic level

No exact `ac<->bc` symmetry; finite parity, pure-`G` and primitive-support
contributions partially cancel.

---

## Phase 3 — Original asymptotic chain

### 13-5 Deviation definition — complete

### 13-6 Finite deviation classification — complete

### 13-7 Original asymptotic chain — reopened by external review

The historical 13-7 theorem claimed

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

The raw direction-neutrality proof and overlap transfer are now being audited
separately under 13-12.

### 13-8 Stage12 bridge — historical complete

The exact finite projection identity

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)
\]

remains active.

### 13-9 Main structural theorem — historical, pending reclosure

### 13-10 Final explanation — historical, pending reclosure

---

## Phase 4 — External-review repair sequence

### 13-11 Single-file review bundle — complete

R01 packaged Stage13 for external review.

### 13-12aa Non-circular `j=0` common factor — complete

Status:

```text
STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
CLAUDE_FATAL_DIRECTION_NEUTRALITY=REPAIRED
RAW_DIRECTIONAL_ASYMPTOTIC=RESTORED_NON_CIRCULARLY
```

Instead of seeding categorywise constants, 13-12aa first proves

\[
A_q(B)\sim\Theta J_q B(\log B)^3
\]

with one unknown common \(\Theta\), using an explicit `j=0` local kernel,
three-variable weighted-`l1` factorization and nonzero-harmonic cancellation.
Only afterwards is the Stage12 total used to obtain

\[
\Theta=\frac{\kappa}{6\pi^2},
\qquad
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

Assets:

```text
stages/stage13/13-12aa/result.md
stages/stage13/scripts/13-12aa/j0_common_factor_audit.py
stages/stage13/data/13-12aa/j0_common_factor_audit_report.json
```

### 13-12ab Fixed-modulus overlap transfer — NEXT

Independently prove or reject the step

```text
fixed finite local sieve conditions
=> same B(log B)^3 degree with main constant multiplied by fixed local factors
```

inside the tagged raw-incidence population. This audit must not assume the old
7jf conclusion merely because the finite-field local ratio is correct.

Target decision:

```text
PAIR_OVERLAP_LOWER_ORDER=PROVED_OR_RETRACTED
TRIPLE_OVERLAP_LOWER_ORDER=PROVED_OR_RETRACTED
EXACT_ONE_TRANSFER=PROVED_OR_RETRACTED
```

### 13-12ac Re-synthesis / R02 review bundle — only if needed

If 13-12ab closes, integrate the repairs, regenerate a clean Stage13-only R02
review bundle and request a new zero-base external review. If 13-12ab finds a
new gap, continue the repair sequence instead.

---

## Current dependency graph

```text
Stage12 R09 frozen total theorem
        |
        +---------------------------+
        |                           |
        v                           v
13-3d exact factor-2 bridge   13-3b chamber I_q
        |                           |
        +------------+--------------+
                     v
              13-12aa j=0 repair
                     |
                     v
          RAW DIRECTIONAL THEOREM
                     |
                     v
        13-12ab overlap transfer audit
                     |
          +----------+----------+
          |                     |
        closes                 fails
          |                     |
          v                     v
 exact-one theorem          further repair
          |
          v
 13-12ac R02 re-review
```

## Current status

```text
RAW_DIRECTIONAL_THEOREM=ACTIVE_AFTER_13_12AA
EXACT_ONE_DIRECTIONAL_THEOREM=PENDING_13_12AB
STAGE13_GLOBAL_REVIEW_STATUS=OPEN
NEXT=Stage13-12ab
```
