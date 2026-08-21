# Stage29 — Work-input suffix routing addendum

This addendum does not replace `stages/stage29/roadmap.md`. It records new candidate suffixes created by an independent Work literature audit after the audited Stage29-02 parent screening.

The suffixes are Stage29-native and must be audited independently before their results can influence `29-03 FOUNDATION_BACKFLOW_DECISION`.

## Recommended order

```text
29-02c-LG1  UNIBRANCH_LOW_GENUS_GLOBAL_DEGREE_LOCK
29-02c-LG2  PICARD_176_192_FINITE_ENUMERATION
29-02d      BEAUVILLE_IRREGULAR_COVER_DESCENT
29-02e      EXISTING_V4_CHARACTER_NEWFORM_ROUTE_CONTINUES
29-02f      TRANSCENDENTAL_BRAUER_AUDIT
29-02g      MODULI_M4_8_Q_DESCENT
```

## Why 02c is split

`29-02c-LG1` is a theorem/applicability lock: verify the published `d<=176+16g` theorem and all hypotheses on the exact endpoint surface.

`29-02c-LG2` is a separate finite computation/proof package: only after LG1 audits may the rank-64 Picard lattice be enumerated through `d<=176` for genus 0 and `d<=192` for genus 1. Multibranch-at-node curves remain a separate explicit residual receiver.

The two steps must not be collapsed, because an error in theorem applicability would invalidate the finite-enumeration range.

## Why 02d is separate

The Beauville surface is a distinct cover with `q=4` and an Albanese map; it is not the Stage29 joint V4 endpoint cover. Its arithmetic difficulty is Q-descent/twisting rather than the branch/canonical geometry of 29-02b.

## Why 02f is separate from 02e

29-02e studies the V4-character/cohomological decomposition and cross-quotient L-function adapter. Transcendental Brauer requires integral lattices, torsion and adelic evaluation. Rational L-function decomposition is input only and cannot self-close 02f.

## Why 02g is separate

The useful modular problem is the exact Q-descended `M(4,8)` conjugate-self-8-congruence receiver. Ordinary 8-congruence or generic `X(8)xX(8)` modularity is not enough.

## Anti-loop and backflow

```text
OLD_STAGE16_28_GATE_REPLAY=false
NEW_THEOREM_OR_NEW_GEOMETRIC_HOST_REQUIRED=true
BACKFLOW_TO_STAGE16_28=false_at_import
29_03_MUST_WAIT_FOR_RELEVANT_SUFFIX_AUDITS=true
```

This is a routing recommendation pending fresh audit of the Work import itself.
