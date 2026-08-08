# Stage13 — Structural Origin of the 2:1:1 Ratio

## Goal

Stage13 studies the directional asymptotic law for primitive canonical exactly-one-face cuboids with integer space diagonal, using Stage12 R09 as a frozen prior theorem-level input.

## External-review repair history

```text
R01: OPEN
  - circular raw direction-neutrality
  - under-derived fixed-modulus overlap transfer

13-12aa: non-circular common-factor architecture
13-12ab: fixed-local overlap architecture
13-12ac: neutral R02 bundle

R02 Grok:   OPEN
R02 Claude: REPAIRABLE
R02 Qwen:   REPAIRABLE

13-12ad: quantitative j=0 Wiener / curved / harmonic closure
13-12ae: exact inert p-adic / local-state closure
13-12af: R03 proof resynthesis and single-file review bundle
```

Current state:

```text
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE
STAGE13_12AE=COMPLETE_EXACT_PADIC_LOCAL_CLOSURE
STAGE13_12AF=COMPLETE_R03_REVIEW_RESYNTHESIS
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=R03_CANDIDATE
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
NEXT=EXTERNAL_R03_REVIEW
```

No internal label self-declares Stage13 externally `CLOSED`.

---

## Original phases

```text
13-1   definition / counting convention                     [complete]
13-2   structural decomposition                             [complete]
13-3   chamber geometry / finite diagnostics                [complete]
13-4   ac-bc finite mechanism                               [complete diagnostic]
13-5   deviation coordinates                                [complete]
13-6   finite deviation classification                      [complete]
13-7   original asymptotic chain                            [historical; disputed steps superseded]
13-8   Stage12 factor-2 bridge                               [complete]
13-9   historical structural theorem statement              [historical]
13-10  historical final explanation                         [historical]
13-11  R01 Stage13-only review bundle                       [complete]
```

The exact finite bridge remains

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B).
\]

---

## 13-12 repair sequence

### 13-12aa — non-circular raw common factor [complete]

Derives the form

\[
A_q(B)\sim\Theta J_qB(\log B)^3
\]

with one unknown common `Theta` before using Stage12 total calibration.

### 13-12ab — fixed-local overlap architecture [complete structurally]

Uses fixed finite prime sets and the order

```text
fix S_k
B -> infinity
k -> infinity
```

rather than any growing-modulus assertion.

### 13-12ac — R02 bundle [complete, immutable]

Historical reviewed target:

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html
```

R02 is frozen after review.

### 13-12ad — quantitative `j=0` analytic closure [complete]

Uniform mixed correction:

\[
\boxed{\|C_{\ell,p}-1\|_{5/8}\le529p^{-5/4}}
\]

for split `p>=13`, uniformly in retained angular phase.

Fixed budget:

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
finite-order A = 48
```

and all small-height / wing / mesh / Vaaler / harmonic contributions are `o(B(log B)^3)`.

The logarithmic-moment estimate also controls convolution-induced shifts and shows that only the direction-neutral value `C_0(1,1,1)` can enter the leading degree-three coefficient.

### 13-12ae — exact inert p-adic/local-state closure [complete]

For inert `p=3 mod 4`:

```text
v_p(h)=0 by primitivity
allowed valuations = U, R_b, S_c only
```

and

\[
L_{p,0}(1,1,1)=\frac{p+1}{p-1},
\qquad
\frac{T_p^+}{L_{p,0}(1,1,1)}=\frac{2}{p+1}\le\frac2p.
\]

Thus

\[
\boxed{C_0=2}.
\]

The exact constrained local multiplier is

\[
\boxed{\lambda_p=\frac{p+5}{2(p+1)}}.
\]

Hence `lambda_p<=3/4` for every inert `p>=7`, and the fixed-set squeeze gives pair/triple overlap lower order.

### 13-12af — R03 resynthesis [complete]

Authoritative current proof:

```text
stages/stage13/13-12af/current-proof.md
```

Physical single-file target:

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260809-R03.html
```

R03 adds four explicit clarifications requested by Qwen R02:

```text
1. tag factor 2 = safe upper multiplicity only
2. pre-calibration Stage12 use = error majorant only
3. OE/EE = branchwise finite 2-adic variants
4. J_q = 2 I_q / pi = analytic change-of-variables identity
```

R03 proof precedence:

```text
13-12af/current-proof.md
-> 13-12ad/result.md
-> 13-12ae/result.md
-> 13-12aa/result.md
-> 13-12ab/result.md
-> 13-12ac/current-proof.md
-> historical support
```

---

## R03 theorem candidate

\[
\boxed{
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3
}
\]

for `q in {ab,ac,bc}`, and

\[
\boxed{N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.}
\]

Normalized candidate vector:

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

---

## Dependency graph

```text
Stage12 R09 frozen total
        |
        +--------------------+
        |                    |
        v                    v
13-3d factor-2 bridge   chamber I_q
        |                    |
        |              analytic J_q=2I_q/pi
        +---------+----------+
                  v
            13-12aa
       common Theta form
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
 exact inert local overlap
                  |
                  v
      EXACT-ONE R03 CANDIDATE
                  |
                  v
            13-12af R03
                  |
                  v
         EXTERNAL R03 REVIEW
```

## Current status

```text
RAW_DIRECTIONAL_ANALYTIC_CORE=RESTORED_WITH_EXPLICIT_ERROR_BUDGET
P_ADIC_POSITIVE_VALUATION_TAIL=REPAIRED_EXACTLY
LOCAL_STATE_REFINEMENT_COMPLETENESS=REPAIRED
EXACT_ONE_THEOREM_EXTERNAL_STATUS=PENDING_R03_REVIEW
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
NEXT=EXTERNAL_R03_REVIEW
```
