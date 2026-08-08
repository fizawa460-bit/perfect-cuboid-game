# Stage13 — Structural Origin of the 2:1:1 Ratio

## Goal

Stage13 explains the finite primitive canonical near-`2:1:1` one-face ratio,
its geometric/arithmetic mechanisms and the directional asymptotic law, using
Stage12 R09 as a frozen prior input.

## Review precedence after R01

The original Stage13-1 through Stage13-10 chain was completed and packaged as a
single-file R01 bundle. External review returned `OPEN` with two substantive
proof objections:

1. old 7jb raw `j=0` direction-neutrality was circular;
2. old 7jf fixed-modulus overlap transfer was insufficiently derived.

The 13-12 repair sequence now addresses both and Stage13-12ac has packaged a
fresh R02 candidate. Historical `STAGE13=COMPLETE` flags do not override the
current external-review state.

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_1_THROUGH_10=HISTORICALLY_COMPLETE
STAGE13_EXTERNAL_REVIEW_R01=OPEN
STAGE13_REPAIR_CHAIN=COMPLETE
STAGE13_12AC=COMPLETE_R02_REVIEW_RESYNTHESIS
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
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
13-7   original asymptotic chain                            [historical; repaired by 13-12]
13-8   Stage12 bridge                                       [historical complete]
13-9   main structural theorem                              [historical statement]
13-10  final explanation                                    [historical statement]
13-11  Stage13-only single-file review bundle               [complete R01]
```

The exact finite bridge from 13-3d remains active:

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B).
\]

---

## External-review repair sequence

### 13-12aa — non-circular raw `j=0` common factor [complete]

Old 7jb seeded the desired categorywise constants and then checked a common
ratio. 13-12aa replaces that with the independent theorem shape

\[
A_q(B)\sim\Theta J_q B(\log B)^3
\]

with one unknown `Theta`. Only afterwards is the Stage12 total theorem used to
calibrate

\[
\Theta=\frac{\kappa}{6\pi^2},
\qquad
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

```text
STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
CLAUDE_FATAL_DIRECTION_NEUTRALITY=REPAIRED
RAW_DIRECTIONAL_ASYMPTOTIC=RESTORED_NON_CIRCULARLY
```

Assets:

```text
stages/stage13/13-12aa/result.md
stages/stage13/scripts/13-12aa/j0_common_factor_audit.py
stages/stage13/data/13-12aa/j0_common_factor_audit_report.json
```

### 13-12ab — fixed-local overlap transfer [complete]

A fixed local condition refines only one prime's finite local state. For fixed
`S`, the constrained Fourier-channel Euler product is

\[
\mathcal D_{\ell,S}
=\mathcal D_\ell
\prod_{p\in S}\frac{L^W_{p,\ell}}{L_{p,\ell}}.
\]

For inert primes `p=3 mod 4`, the second-face necessary condition has unit-layer
acceptance

\[
\frac{p+1}{2(p-1)}=\frac12+\frac1{p-1},
\]

with positive-valuation tail `O(1/p)`. Hence all sufficiently large inert
primes have `lambda_p<=3/4`.

Fix `k` such primes, take `B->infinity`, then let `k->infinity`. This proves

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3).
\]

Therefore the exactly-one theorem is restored from the 13-12aa raw theorem.

```text
STAGE13_12AB=COMPLETE_FIXED_LOCAL_OVERLAP_REPAIR
CLAUDE_MAJOR_FIXED_MODULUS_TRANSFER=REPAIRED
PAIR_OVERLAP_LOWER_ORDER=RESTORED
TRIPLE_OVERLAP_LOWER_ORDER=RESTORED
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=RESTORED
STAGE13_REPAIR_CHAIN=COMPLETE
```

Assets:

```text
stages/stage13/13-12ab/result.md
stages/stage13/scripts/13-12ab/fixed_local_overlap_audit.py
stages/stage13/data/13-12ab/fixed_local_overlap_audit_report.json
```

### 13-12ac — R02 re-synthesis / external re-review [complete]

Stage13-12ac creates a fresh review entrypoint and a new physical R02 bundle.
R01 is not mutated.

Authoritative R02 entrypoint:

```text
stages/stage13/13-12ac/current-proof.md
```

Physical review bundle:

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html
```

Machine-readable manifest:

```text
stages/stage13/data/13-12ac/review_bundle_manifest.json
```

R02 explicitly neutralizes internal status pressure:

```text
PREVIOUS_R01_VERDICT_BINDING=false
INTERNAL_PASS_FLAGS_ARE_EVIDENCE=false
INTERNAL_COMPLETE_FLAGS_ARE_EVIDENCE=false
GIT_HASHES_ARE_MATHEMATICAL_EVIDENCE=false
CI_SUCCESS_IS_MATHEMATICAL_EVIDENCE=false
NEGATIVE_VERDICT_REQUIRES_EXTRA_BURDEN=false
```

The target external verdict remains one of

```text
CLOSED
REPAIRABLE
OPEN
UNREADABLE_SOURCE
```

with no preferred outcome.

No internal status may substitute for the independent R02 verdict.

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
       13-12ab fixed-local overlap
                     |
                     v
          PAIR/TRIPLE LOWER ORDER
                     |
                     v
         EXACT-ONE THEOREM RESTORED
                     |
                     v
         13-12ac R02 BUNDLE
                     |
                     v
            EXTERNAL R02 REVIEW
```

## Current status

```text
RAW_DIRECTIONAL_THEOREM=RESTORED_BY_13_12AA
EXACT_ONE_DIRECTIONAL_THEOREM=RESTORED_BY_13_12AB
STAGE13_REPAIR_CHAIN=COMPLETE
STAGE13_12AC=COMPLETE_R02_REVIEW_RESYNTHESIS
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
NEXT=EXTERNAL_STAGE13_R02_REVIEW
```
