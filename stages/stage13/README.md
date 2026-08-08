# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

and explains both the finite near-`2:1:1` observation and its asymptotic behaviour.

## Current state

```text
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=COMPLETE_AT_STRUCTURAL_DIAGNOSTIC_LEVEL
STAGE13_3A=COMPLETE
STAGE13_3B=COMPLETE
STAGE13_3C=COMPLETE
STAGE13_3D=COMPLETE
STAGE13_3E=COMPLETE
STAGE13_3F=COMPLETE
STAGE13_4=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
STAGE13_4A=COMPLETE
STAGE13_4B=COMPLETE
STAGE13_4C=COMPLETE
STAGE13_5=COMPLETE
STAGE13_6=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
STAGE13_7=COMPLETE_AT_UNCONDITIONAL_EXACT_ONE_DIRECTIONAL_ASYMPTOTIC_LEVEL
NEXT=Stage13-8
```

The active roadmap is

```text
stages/stage13/roadmap.md
```

and the Stage13 working-file policy is

```text
stages/stage13/policy.md
```

The policy designates

```text
stages/stage13/main.md
```

as the canonical living mathematical source. Stage13-8 is now expected to consolidate the already-proved Stage12-to-Stage13 bridge into that canonical exposition.

## Stage13-7 final result

Stage13-7 resolves the asymptotic behaviour of the exact-one directional vector. With the Stage13-3b chamber integrals

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
I_ab+I_ac+I_bc = pi^2/8
```

the three category counts satisfy

\[
N_q(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
\]

and

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

Therefore

```text
P_inf = (0.5347369332313988,
         0.24535917783225203,
         0.21990388893634913)

N_ab:N_ac:N_bc
 -> 2.431684750178191 : 1.115756428951881 : 1
```

so the proved limiting ratio is **not** `2:1:1`.

For the Stage13-5 deviation coordinates,

```text
alpha -> 0.034736933231398814
beta  -> 0.01272764444795145
```

and

```text
Delta_inf = ( 0.034736933231398814,
             -0.004640822167747971,
             -0.03009611106365087 )
```

is nonzero.

At `B=100000`, by contrast, exact-one has approximately

```text
alpha = 0.0007796226864250431
beta  = 0.007367731952627507
```

so the observed near-`2:1:1` vector is strongly pre-asymptotically flattened.

No monotone convergence or explicit secondary convergence rate is claimed.

## Stage13-7 theorem chain

The final chain is:

```text
13-7j
  individual primitive pure-G category asymptotics
  G_q ~ K_q B(log B)^(1/3)
  normalized limit = Stage13-3b chamber vector

13-7ja
  preprimitive m1 asymptotics
  M_q ~ C_q B log B
  primitive support changes exponent 1 -> 1/3
  leading normalized vector unchanged

13-7jb
  restore supported-shell richness
  A_q ~ [kappa I_q/(3 pi^3)] B(log B)^3
  raw normalized limit = chamber vector

13-7jc
  exact inclusion-exclusion
  pair-overlap problem reduced to F(B)=o(B(log B)^3)

13-7jd
  unconditional face-cuboid bound B*exp(C log B/loglog B)
  useful intermediate bound, insufficient by itself for exactly-one

13-7je
  exact Kummer / congruent-number-twist / coupled-height reduction
  structural intermediate route

13-7jf
  fixed-prime quadratic-residue sieve
  pair overlaps = o(B(log B)^3)
  triple overlap = o(B(log B)^3)
  exact-one category asymptotics and directional limit proved

13-7jg
  constant/dependency/tagged-orientation/order-of-limits audit
  Stage13-7 completion decision
```

The shortest final overlap proof is the 13-7jf fixed-prime sieve. The essential order of limits is

```text
fix finitely many sieve primes
-> B -> infinity
-> increase the number of fixed primes
```

so no uniform theorem for a modulus growing with `B` is required.

No perfect-cuboid nonexistence assumption is used.

## Scale ladder

The absolute scales change dramatically, but the leading normalized chamber vector survives every layer:

| observable | scale | normalized limit |
|---|---|---|
| preprimitive `m1` | `B log B` | Stage13-3b chamber |
| primitive pure-`G` | `B(log B)^(1/3)` | Stage13-3b chamber |
| primitive raw incidence | `B(log B)^3` | Stage13-3b chamber |
| primitive exactly-one | `B(log B)^3` | Stage13-3b chamber |

The common primitive-support survival constant is diagnostically

```text
Lambda ~= 0.7516555708217902
```

and the common scaled pure-`G` to raw amplification is diagnostically

```text
Omega ~= 0.0010287940977836043.
```

The numerical `kappa`, `K_q`, `D_q`, `Lambda`, and `Omega` values based on truncated prime products are diagnostics, not certified enclosures. The symbolic theorem constants are authoritative.

## Stage13-7 final audit assets

```text
stages/stage13/scripts/13-7/consolidation_audit.py
stages/stage13/data/13-7/consolidation_audit_report.json
stages/stage13/archive/stage13-7-final.md
```

Historical 13-7jc/7jd/7je conditional status flags remain in their own reports as provenance. The 13-7jg supersession ledger records that their open overlap condition is discharged by 13-7jf.

## Earlier structural synthesis

Stages13-3 through 13-6 remain important because they explain the finite regime rather than merely the limit.

- Canonical archimedean geometry creates the directional ordering `ab>ac>bc` and the chamber vector that ultimately becomes the asymptotic limit.
- At accessible cutoffs, representation-rich supported shells strongly flatten the `ab` excess.
- Pure-`G` OE/EE and geometric subregions have opposite `ac-bc` gaps and can cancel strongly.
- Primitive support materially changes the finite residual `ac-bc` tilt.
- The exactly-one overlap sieve is already tiny at finite audited bounds and is now proved lower order asymptotically.
- The universal Stage12 projection multiplicity `2` is a normalized directional null.

Thus the finite near-`2:1:1` observation is not the limiting law: it is a pre-asymptotic cancellation/flattening regime sitting in front of the stronger chamber limit.

## Next — Stage13-8

Stage13-8 was originally planned to construct the rigorous Stage12-to-Stage13 bridge. Much of that bridge has now been proved ahead of schedule:

```text
13-3d  oriented -> canonical raw multiplicity 2
13-3d  Stage12 total -> raw total
13-7jb raw total -> individual raw category constants
13-7jf raw -> exactly-one after lower-order overlap removal
13-7jg constants/orientation/order-of-limits audit
```

Stage13-8 should therefore primarily consolidate these pieces into the canonical Stage13 exposition, unify notation/local factors, and identify only genuinely missing bridge lemmas before Stage13-9 states the main structural theorem.

## File rule

Stage13 mathematical corrections normally go directly into the canonical `main.md`; Git/PR history records prior versions. Support assets use task-first paths such as

```text
stages/stage13/scripts/13-<task>/<purpose>.py
stages/stage13/data/13-<task>/<purpose>.json
```

Frozen task-end snapshots under `stages/stage13/archive/` are provenance, not replacements for the living canonical file.
