# Stage13-9 final — frozen main-structural-theorem snapshot

> **STATUS:** `STAGE13_9_COMPLETE_MAIN_STRUCTURAL_THEOREM`
>
> **SCOPE:** frozen task-end provenance snapshot; canonical living mathematics remains `stages/stage13/main.md`

## Main theorem

For the primitive canonical exactly-one directional count vector

\[
\mathbf N(B)=(N_{ab}(B),N_{ac}(B),N_{bc}(B)),
\]

with integral space diagonal `d<=B`, define the canonical chamber integrals

\[
I_{ab}=\int_R\frac{d\omega}{\sqrt{x^2+y^2}},\quad
I_{ac}=\int_R\frac{d\omega}{\sqrt{x^2+z^2}},\quad
I_{bc}=\int_R\frac{d\omega}{\sqrt{y^2+z^2}},
\]

where `R={0<x<y<z}` on the positive unit sphere. Then

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}
\]

and

\[
\boxed{
\mathbf N(B)
=
\frac{\kappa}{3\pi^3}(I_{ab},I_{ac},I_{bc})B(\log B)^3
+o(B(\log B)^3).
}
\]

Hence

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3
\]

and

\[
\frac{\mathbf N(B)}{N_1(B)}
\to
\frac8{\pi^2}(I_{ab},I_{ac},I_{bc}).
\]

Numerically,

```text
P_inf = (0.5347369332313988,
         0.24535917783225203,
         0.21990388893634913)

ab:ac:bc
 -> 2.431684750178191 : 1.115756428951881 : 1
```

Thus the limiting law is not `2:1:1`.

## Stage12 bridge

For each canonical category `q`,

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)
\]

exactly, and the pair/triple overlap population is lower order. Therefore

\[
N_q(B)=\frac12C^{\rm proj}_{\rm prim,q}(B)+o(B(\log B)^3),
\]

\[
N_1(B)=\frac12C_{\rm prim}(B)+o(B(\log B)^3).
\]

No perfect-cuboid nonexistence assumption is used.

## Deviation corollary

Relative to `(1/2,1/4,1/4)`,

```text
Delta_inf = ( 0.034736933231398814,
             -0.004640822167747971,
             -0.03009611106365087 )
alpha_inf = 0.034736933231398814
beta_inf  = 0.01272764444795145
```

At `B=100000`, the much smaller `alpha` and finite `beta` record a strongly pre-asymptotic flattened regime.

## Structural content

The theorem packages three layers:

1. canonical archimedean chamber geometry determines the unequal normalized directional vector;
2. primitive/arithmetic representation factors determine the common leading population scale;
3. multi-face overlaps are lower order and therefore do not alter the leading exactly-one vector.

The detailed finite-mechanism narrative is reserved for Stage13-10.

## Scope boundary

```text
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
PERFECT_CUBOID_EXISTENCE_DECIDED=false
EXPLICIT_CONVERGENCE_RATE_PROVED=false
EFFECTIVE_THRESHOLD_PROVED=false
MONOTONICITY_PROVED=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false
NEW_ANALYTIC_THEOREM_INTRODUCED_IN_13_9=false
```

The main theorem is a synthesis of established Stage13-7 and Stage13-8 results at the existing project theorem standard.

## Audit assets

```text
stages/stage13/scripts/13-9/main_structural_theorem_audit.py
stages/stage13/data/13-9/main_structural_theorem_audit_report.json
```

The audit classification is `PASS`.

```text
STAGE13_9=COMPLETE_MAIN_STRUCTURAL_THEOREM
NEXT=Stage13-10 final explanation
```
