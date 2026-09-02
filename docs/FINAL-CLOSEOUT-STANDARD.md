# Final closeout standard

This document is a **closeout-only** standard. It is not part of normal Stage startup, MAIN batch, controller replay, or routine audit reading. Read it only when creating or auditing a Stage-root `final.md` intended to be a permanent mathematical closeout document.

## Core rule

A Stage-root `final.md` must be self-contained at the Stage27/28/34 level:

> If every other file in this repository were unavailable, a mathematically competent reader must still be able to identify and verify the Stage's theorem, proof reductions, finite classifications, exceptional cases, and exact conclusion from `final.md` itself, using external mathematical literature where explicitly cited.

Repository-internal certificates, source locks, manifests, hashes, CI runs, audit reviews, scripts, and earlier Stage files may appear as **provenance and reproducibility records only**. They must not substitute for a mathematical step omitted from `final.md`.

## Required proof surface

A self-contained `final.md` must state, as applicable:

1. **Exact theorem and population.** Define the complete population being quantified over and justify completeness: generators/bases, torsion translates, signs, symmetry reductions, excluded boundary classes, and any other reason a displayed parametrization covers the entire claimed population.
2. **Exact algebraic reduction.** Give the equations and derivations that connect the Stage input to the object actually classified. Do not replace a derivation with an internal artifact name.
3. **Finite funnel.** If an infinite problem is reduced to finitely many squareclasses, branches, orbits, quotient species, models, residue classes, etc., define those objects mathematically and explain why the finite list is exhaustive.
4. **Every load-bearing transition.** For each transition in a finite closure chain, identify the input class, the concrete curve/quotient/local condition or other test used, the completeness theorem or finite exhaustion that makes the test decisive, and why exactly the stated class is removed. Internal labels such as `Candidate A`, model numbers, branch IDs, or job names are insufficient unless their mathematical meaning is also stated.
5. **Terminal representatives.** Any direct representatives used with symmetry/sign transfer must be identifiable in the text by enough mathematical data to reconstruct the argument (for example parameters, squareclass tuple, quotient/triple, and model/equation where load-bearing). Internal hashes are not required.
6. **Exceptional and boundary cases.** Poles, torsion, projective points, cusps, zero factors, compactification boundaries, denominator-zero cases, map exceptions, and similar cases must be classified explicitly whenever they could affect the claimed population.
7. **Final implication and firewalls.** State the exact contradiction/implication from the completed classification to the Stage theorem, and separately state what is *not* proved. A receiver-restricted theorem must not silently become a parent-route or perfect-cuboid theorem.
8. **Provenance last.** Repository paths, blob hashes, run/job IDs, review IDs, certificates, and replay instructions belong after the mathematical proof surface. A reader may use them to reproduce the computation, but must not need them to understand what was proved or why each closure step is valid.

## Finite-computation rule

It is not necessary to print every member of a large finite set when doing so adds no mathematical information. Compression is allowed only when the compressed group is mathematically identifiable from the text.

For example, a statement such as `92 -> 76 by rank-zero quotients` is not sufficient by itself. The document must specify which branch group is meant, which quotient(s) decide it, why the rational point set or residue test is complete, and why the pullback leaves no admissible point. Conversely, 92 nearly identical branch IDs need not be printed when a mathematical grouping plus representative data and an exhaustive rule uniquely determine them.

## External references

External literature may be cited for standard or explicitly imported theorems. The closeout document need not reproduce an external paper. It must, however, state clearly which theorem/result is being used and verify the Stage-specific hypotheses needed to apply it.

## Self-contained audit gate

Before declaring `SELF-CONTAINED: PASS`, audit the document under the destructive thought experiment:

```text
Keep only this Stage's final.md.
Delete or hide every other repository file.
Allow access to explicitly cited external literature.
Can the claimed Stage theorem still be followed and checked without guessing what an internal label, certificate, or computation did?
```

If the answer is no at any load-bearing step, the document is not yet self-contained.

A closeout may therefore be mathematically correct and audit-PASS at the Stage level while still failing this separate self-contained-document standard.

## Operational rule

Do **not** add this file to the mandatory read set for ordinary Stage work. Invoke it explicitly only for final closeout creation or self-contained-final audit.

Recommended instruction:

```text
Read docs/FINAL-CLOSEOUT-STANDARD.md and create/audit this Stage's root final.md to that standard.
```

Stage27, Stage28, and the self-contained Stage34 closeout are precedent for the intended level. Their internal files are not normative dependencies; this document is the standard.