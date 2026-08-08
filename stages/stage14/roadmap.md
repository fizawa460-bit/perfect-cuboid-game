# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain the primitive canonical exactly-two-face population inside the integer-space-diagonal cuboid family.

The three canonical directions are indexed by their shared edge:

```text
a-direction = ab+ac only
b-direction = ab+bc only
c-direction = ac+bc only
```

## 14-1 — Definition and counting interface

Priority: required

```text
14-1a  lock ambient object, exactly-two categories, raw-pair/triple ledger   [complete]
14-1b  connect to the existing pair-overlap notation and inherited checks  [next]
14-1c  lock enumeration/output specification                               [planned]
```

Additional ordinary-letter substages are added only if a concrete interface issue appears.

## 14-2 — Complete finite enumeration

Priority: required

Enumerate

```text
O_ab_ac, O_ab_bc, O_ac_bc
T
N_a^(2), N_b^(2), N_c^(2)
N_2
```

at increasing `d<=B` cutoffs, with independent consistency checks where practical.

Status: not started.

## 14-3 — Finite directional-ratio evolution

Priority: required

Study

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}
\]

and normalized proportions over the audited cutoff range. Test whether the directions share one apparent growth scale or separate already at finite size.

Status: not started.

## 14-4 — True total growth order

Priority: major analytic task

Determine the correct asymptotic order of

\[
N_2(B).
\]

Stage13 proved only that the at-least-two-face population is lower order than `B(log B)^3`; Stage14 must determine the actual scale rather than presuppose one.

Fine-grained substages for this task may begin at `14-4aa`.

Status: not started.

## 14-5 — Directionwise asymptotic structure

Priority: major analytic task

After the total scale is understood, determine whether

\[
N_a^{(2)},\quad N_b^{(2)},\quad N_c^{(2)}
\]

share the same exponent/logarithmic scale, whether direction constants exist, and what geometric/arithmetic mechanism controls their ratios.

A later comparison with the face-diagonal-first / Euler-side two-face layer is natural, but equality of the two directional laws is not assumed.

Fine-grained substages for this task may begin at `14-5aa`.

Status: not started.

## Scope boundary

Stage14 does not assume perfect-cuboid nonexistence. The triple population `T(B)` is retained explicitly and removed from each raw pair count when forming the exactly-two populations.

No growth exponent, limiting directional ratio, monotonicity, or relation to the Euler-side two-face limit is assumed before it is proved or numerically diagnosed.
