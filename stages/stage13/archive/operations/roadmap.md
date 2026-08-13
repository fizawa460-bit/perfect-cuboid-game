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

R03 Grok: CLOSED
R03 Qwen: CLOSED
R03 Claude: not recorded at this checkpoint

13-12ag: post-R03 proof-explicitness supplement
```

Current state:

```text
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE
STAGE13_12AE=COMPLETE_EXACT_PADIC_LOCAL_CLOSURE
STAGE13_12AF=COMPLETE_R03_REVIEW_RESYNTHESIS
STAGE13_12AG=COMPLETE_PROOF_EXPLICITNESS_SUPPLEMENT

R03_GROK_VERDICT=CLOSED
R03_QWEN_VERDICT=CLOSED
R03_CLAUDE_VERDICT=NOT_RECORDED

EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=R03_CANDIDATE_WITH_POST_REVIEW_SUPPLEMENT
STAGE13_GLOBAL_REVIEW_STATUS=TWO_R03_CLOSED_VERDICTS_RECORDED_PENDING_FINAL_FREEZE
NEXT=FINAL_EXTERNAL_REVIEW_FREEZE_OR_NEW_R04_ONLY_IF_REQUESTED
```

No internal label self-declares Stage13 externally `CLOSED`. The two `CLOSED` labels above are recorded external reviewer outcomes.

Downstream Stage14 may use the R03 theorem candidate as an explicit upstream dependency while final Stage13 freeze bookkeeping remains pending.

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

## 13-12 repair and review sequence

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

### 13-12af — R03 resynthesis [complete, reviewed artifact frozen]

Authoritative R03 proof:

```text
stages/stage13/13-12af/current-proof.md
```

Physical reviewed target:

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260809-R03.html
```

R03 adds the requested tag-factor, Stage12-majorant, OE/EE and analytic `J_q=2I_q/pi` clarifications. Grok and Qwen subsequently returned `CLOSED` on the supplied R03 review.

R03 is immutable after those reviews. Stage13-12ag must not regenerate it.

### 13-12ag — post-R03 proof explicitness [complete in this stage]

This step strengthens presentation without changing the theorem.

#### Full coarea/Fubini chain

For each face `q={i,j}`, use `q`-adapted spherical coordinates

\[
x_i=\sin\theta\cos\alpha,
\quad
x_j=\sin\theta\sin\alpha,
\quad
x_k=\cos\theta.
\]

Then

\[
w_q=\frac1{\sin\theta},
\qquad
d\omega=\sin\theta d\theta d\alpha,
\]

so

\[
\boxed{w_qd\omega=d\theta d\alpha}.
\]

Writing `psi=pi/2-theta` and letting `ell_q(psi)` be the canonical inner-angle slice length gives by Fubini

\[
I_q=\int\ell_q(\psi)d\psi.
\]

The outer parameterization gives

\[
\psi=2\phi-\frac\pi2,
\qquad
k_q(\phi)=\frac4\pi\ell_q(\psi),
\]

and hence

\[
\boxed{J_q=\frac2\pi I_q}.
\]

#### Exact inert unit character sum

For `p=3 mod 4`, with `chi` the quadratic character, Stage13-12ag expands

\[
S=S_0+S_1+S_2+S_3
\]

and proves

\[
S_0=0,
\quad
S_1=p-1,
\quad
S_2=p+1,
\quad
S_3=-2.
\]

Thus

\[
S=2(p-1).
\]

Since the total unit population is `T=p^2-1` and exactly four states have `X^2+Z^2=0`,

\[
\boxed{
N_{\rm acc}=\frac{T+S+4}{2}=\frac{(p+1)^2}{2}
}.
\]

Therefore

\[
\boxed{\alpha_p=\frac{p+1}{2(p-1)}}
\]

has an explicit symbolic Legendre/Jacobi-sum proof.

#### Selberg--Delange hypothesis crosswalk

The zero-mode one-variable factors are recorded in theorem-ready form

\[
A_0(s)=\zeta(s)^1G_h(s),
\qquad
B_0(s)=\zeta(s)^2G_b(s),
\]

with residual Euler quotients `1+O(p^{-2sigma})` for `sigma>1/2`, hence holomorphic arithmetic factors near `s=1` after finite local factors are separated. Stage13-12ad's weighted-Wiener estimate supplies all fixed logarithmic moments needed by the mixed convolution.

For nonzero harmonics,

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s)
\]

has no zeta pole, and the retained range `ell<=log^4 B` lies inside the already declared polylog-uniform Gaussian-Hecke zero-free input.

The repository therefore clearly separates what Stage13 proves internally from the finite-order Selberg--Delange/Tauberian and Hecke zero-free results taken as standard external analytic inputs.

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
        |            coarea/Fubini + J_q=2I_q/pi
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
          Grok/Qwen CLOSED
                  |
                  v
            13-12ag
 explicitness supplement
                  |
                  v
       FINAL FREEZE DECISION
```

## Current status

```text
RAW_DIRECTIONAL_ANALYTIC_CORE=RESTORED_WITH_EXPLICIT_ERROR_BUDGET
P_ADIC_POSITIVE_VALUATION_TAIL=REPAIRED_EXACTLY
LOCAL_STATE_REFINEMENT_COMPLETENESS=REPAIRED
COAREA_IQ_TO_INTERVAL_LENGTH=PROVED_EXPLICITLY
INERT_UNIT_CHARACTER_SUM=PROVED_SYMBOLICALLY
SELBERG_DELANGE_HYPOTHESIS_CROSSWALK=RECORDED
R03_GROK_VERDICT=CLOSED
R03_QWEN_VERDICT=CLOSED
EXACT_ONE_THEOREM_EXTERNAL_STATUS=TWO_R03_CLOSED_VERDICTS_RECORDED
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_FINAL_FREEZE_BOOKKEEPING
NEXT=FINAL_EXTERNAL_REVIEW_FREEZE_OR_NEW_R04_ONLY_IF_REQUESTED
```
