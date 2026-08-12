# Stage12-EX0 — Critical chain extraction

> **STATUS:** `STAGE12_EX0_CRITICAL_CHAIN_FIXED`
>
> **SCOPE:** frozen Stage12 R09 primitive oriented asymptotic only
>
> **R09_REOPEN_REQUIRED:** `false`
>
> **NEW_MATHEMATICS_ADDED:** `false`

## 0. Purpose and frozen source boundary

This document executes Stage12-EX0 from `stages/stage12-ex/roadmap.md`. It does not reopen Stage12 and does not replace any R09 argument. Its only job is to expose the active dependency chain of the frozen theorem, classify the proof nodes, and rank the highest-value targets for later independent human verification.

Frozen reading order:

```text
stages/stage12/final.md
stages/stage12/manifest-r09.md
review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html
```

Frozen theorem target:

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

The target is the R09-defined **primitive oriented count only**. No canonical-count, exact-one-face, perfect-cuboid existence, or Stage13 face-ratio claim is imported here.

## 1. Classification vocabulary

Every proof node below receives exactly one primary Stage12-EX classification.

```text
INTERNAL_EXACT
STANDARD_EXTERNAL_THEOREM
EXTERNAL_THEOREM_APPLICATION
COUNTING_INTERFACE
CONSTANT_NORMALIZATION
NUMERICAL_ONLY
```

`NUMERICAL_ONLY` is deliberately absent from the theorem dependency path. Finite partial products, CI, hashes, and numerical agreement remain diagnostics rather than proof nodes.

## 2. Active R09 dependency graph

```text
N00 FINAL ASYMPTOTIC
 |
 +-- N01 FINAL COMPOSITION
 |    |
 |    +-- N02 PRIMITIVE / ORIENTED COUNTING INTERFACE
 |    |    |
 |    |    +-- N03 PRIMITIVE-FIRST EXACT REINDEXING
 |    |         |
 |    |         +-- N04 FIXED-HEIGHT RESIDUE FORMULA
 |    |
 |    +-- N05 RADIAL HARMONIC MAIN TERM
 |    |    |
 |    |    +-- N06 PARITY-WEIGHTED COPRIME RECTANGLE ASYMPTOTIC
 |    |    |    |
 |    |    |    +-- N07 DIRICHLET-SERIES / EULER-PRODUCT CONSTRUCTION
 |    |    |    +-- N08 SINGULAR FACTORIZATION AT s=1
 |    |    |    +-- N09 EXACT SELBERG--DELANGE THEOREM
 |    |    |    +-- N10 SELBERG--DELANGE HYPOTHESIS MAP / APPLICATION
 |    |    |    +-- N11 COPRIME CROSS-CORRECTION WEIGHTED l1 TRANSFER
 |    |    |
 |    |    +-- N12 RADIAL STIELTJES TRANSFER AND LOG^3 EXTRACTION
 |    |    +-- N13 RECTANGLE / RADIAL LEADING CONSTANT
 |    |
 |    +-- N14 KAPPA / ETA NORMALIZATION
 |
 +-- N15 UNIFORMITY AND GLOBAL REMAINDER PASSAGE
```

The edges mean “the parent claim requires the child claim”. Historical arguments that R09 explicitly supersedes are not parallel children of this graph.

## 3. Node registry

### N00 — Frozen final asymptotic

**Class:** `INTERNAL_EXACT`

Claim:

\[
C_{\rm prim}(B)
\sim
\frac{\eta}{12\pi^2}B(\log B)^3
=
\frac{\kappa}{12\pi}B(\log B)^3.
\]

Active source: `stages/stage12/final.md`, final composition / final state.

Failure impact: theorem-level.

### N01 — Final composition

**Class:** `INTERNAL_EXACT`

The proof combines

```text
M(B) = (B/pi) H_lambda(B) + O(B(log B)^2),
H_lambda(B) = eta/(12*pi) (log B)^3 + o((log B)^3),
all nonresidue / endpoint terms = o(B(log B)^3).
```

This yields `eta/(12*pi^2)` and then uses `eta=pi*kappa`.

Active source: integrated proof §§4, 8–11 together with later R09 closures.

Failure impact: theorem-level.

### N02 — Primitive / oriented counting interface

**Class:** `COUNTING_INTERFACE`

The exact counted object is

\[
C_{\rm raw}(B)
=
\sum_{(h,r,s)\in\mathcal D_B}(G(hrs)-1),
\]

with `r<s`, the distinguished-face convention retained, and no canonical quotient. Global content gives the exact identity

\[
C_{\rm raw}(B)=\sum_{k\le B}C_{\rm prim}(\lfloor B/k\rfloor),
\]

hence Möbius inversion defines the primitive oriented count.

Active source: embedded Stage12-N1-3d definition sheet in `stages/stage12/final.md`.

Failure impact: fatal target mismatch even if all later analysis is correct.

### N03 — Primitive-first exact reindexing

**Class:** `COUNTING_INTERFACE`

For fixed coprime `(r,s)`, define

\[
A_{r,s}(m)
=
\sum_{k\mid m}\mu(k)\{G((m/k)rs)-1\}.
\]

Then exactly

\[
C_{\rm prim}(B)
=
\sum_{1\le r<s\atop(r,s)=1}
\sum_{m\le \lambda(r,s)B/(r^2+s^2)}
A_{r,s}(m),
\]

where `lambda=2` on odd–odd and `lambda=1` on opposite parity.

Active source: definition sheet §5 and integrated proof §2.

Failure impact: fatal; this is the bridge from object-level primitivity to the analytic sum.

### N04 — Fixed-height residue formula

**Class:** `INTERNAL_EXACT`

With the R09-defined multiplicative functions `beta`, `gamma`, and `g=pi*gamma=1*beta`,

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1+R_{r,s}(X),
\]

and the retained-region pointwise remainder satisfies

\[
R_{r,s}(X)
\ll G(rs)H_{\rm abs}(rs)X^{1/2}.
\]

This produces the residue main term and separates the fixed-height error budget.

Active source: definition sheet §§7–8, integrated proof §3, Stage12-N1-3b provenance embedded in R09.

Failure impact: fatal to the main analytic reduction.

### N05 — Radial harmonic main term

**Class:** `INTERNAL_EXACT`

After the fixed-height residue and the common-cutoff reduction,

\[
\mathcal M(B)
=
\frac B\pi\mathcal H_\lambda(B)
+O(B(\log B)^2),
\]

where

\[
\mathcal H_\lambda(B)
=
\sum_{r<s,(r,s)=1\atop r^2+s^2\le B}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}.
\]

The odd–odd annulus between cutoffs `B` and `2B` is lower order.

Active source: integrated proof §4.

Failure impact: fatal to the coefficient and the final scale.

### N06 — Parity-weighted coprime rectangle asymptotic

**Class:** `INTERNAL_EXACT`

For

\[
a_\lambda(r,s)=\lambda(r,s)g(r)g(s)\mathbf1_{(r,s)=1},
\]

and

\[
T_\lambda(R,S)=\sum_{r\le R}\sum_{s\le S}a_\lambda(r,s),
\]

R09 obtains a two-variable expansion with leading term

\[
C_\lambda^{(0)}RS\log R\log S
\]

plus lower rectangle polynomials and a uniform error containing the active tail exponent

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}.
\]

This is the widest internal bridge between the one-variable analytic inputs and the radial count. It simultaneously uses parity, coprimality, cross-correction coefficients, two one-variable asymptotics, and weighted coefficient-tail control.

Active source: integrated proof §6; Stage12-N1-3a, 3i, and 3j as embedded and superseded by R09 precedence.

Failure impact: fatal to the main term or to its uniformity.

### N07 — Dirichlet-series / Euler-product construction

**Class:** `INTERNAL_EXACT`

R09 derives prime by prime

\[
B_\beta(s)
:=
\sum_{n\ge1}\frac{\beta(n)}{n^s}
=
\zeta(s)L(s,\chi_4)J_\beta(s),
\]

with explicit local factors for `2`, primes `3 mod 4`, and primes `1 mod 4`. Since `g=1*beta`,

\[
G_g(s)
:=
\sum_{n\ge1}\frac{g(n)}{n^s}
=
\zeta(s)^2L(s,\chi_4)J_\beta(s).
\]

Active source: Stage12-N1-3i §1 and integrated proof §5.

Failure impact: fatal to the singular exponent and all Selberg–Delange outputs.

### N08 — Singular factorization near the dominant point

**Class:** `INTERNAL_EXACT`

The analytic factor is

\[
H_\beta(s)=L(s,\chi_4)J_\beta(s).
\]

R09 proves `J_beta` is locally uniformly absolutely convergent on every closed half-plane `Re(s)>=1/2+epsilon`, hence analytic there; `L(s,chi_4)` is analytic and nonzero at `s=1`; and therefore

```text
beta: B_beta(s) = zeta(s)^1 H_beta(s),
g:    G_g(s)    = zeta(s)^2 H_beta(s).
```

The dominant singular orders are therefore exactly `z=1` and `z=2`.

Active source: Stage12-N1-3i §§1, 3 and Stage12-N1-3j §3.

Failure impact: fatal to the main logarithmic degrees.

### N09 — Exact Selberg–Delange theorem invoked

**Class:** `STANDARD_EXTERNAL_THEOREM`

The sole theorem-level external analytic input intentionally retained by R09 is the finite-order Selberg–Delange theorem, locked to:

```text
Gérald Tenenbaum,
Introduction to Analytic and Probabilistic Number Theory,
3rd ed., Chapter II.5, Theorem II.5.2, p. 281.
```

R09 uses the finite-order expansion for `F(s)=zeta(s)^z H(s)` and does not require the older specific `3/5` zero-free-region remainder.

Active source: Stage12-N1-3d reference lock, completed by Stage12-N1-3i §3.

Failure impact: fatal if the quoted working form is not actually supplied by the cited theorem.

### N10 — Selberg–Delange hypothesis map and application

**Class:** `EXTERNAL_THEOREM_APPLICATION`

R09 maps the theorem to both `z=1` and `z=2` inputs:

```text
coefficient majorant:
  beta(n) <= tau(n),
  g(n) << tau_3(n)

analytic factor:
  H_beta = L(s,chi_4) J_beta

standard SD region:
  chosen inside the absolute-convergence region of J_beta

vertical growth:
  J_beta bounded by absolute convergence;
  L(s,chi_4) polynomial on fixed strips via its functional equation,
  Stirling, and Phragmen--Lindelof;
  therefore H_beta has polynomial growth

leading factor:
  H_beta(1)>0.
```

The active conclusions are, for every fixed `A>0`,

\[
\sum_{n\le x}\beta(n)
=
c_\beta x+O_A(x(\log(2x))^{-A}),
\]

and

\[
\sum_{n\le x}g(n)
=
x(c_g\log x+d_g)+O_A(x(\log(2x))^{-A}).
\]

Active source: Stage12-N1-3i §3, with the vertical-growth role separation finalized by Stage12-N1-3j §3.

Failure impact: fatal; even a correct external theorem does not help if the R09 hypotheses do not match it.

### N11 — Coprime cross-correction weighted `l1` transfer

**Class:** `INTERNAL_EXACT`

The two-variable coprime correction is expressed as

\[
C(s_1,s_2)=\prod_{q\equiv1(4)}C_q(s_1,s_2)
\]

with local

\[
C_q(s_1,s_2)=1-V_q(s_1)V_q(s_2).
\]

R09 proves the local weighted coefficient norm

\[
\|C_q-1\|_\delta\ll_\delta q^{-1-2\delta}
\]

and then, in 3j, proves weighted two-variable Dirichlet-convolution submultiplicativity plus a finite-product Cauchy argument, obtaining

\[
M_\delta
=
\sum_{a,b\ge1}
\frac{|c(a,b)|}{(ab)^{1/2+\delta}}
<\infty.
\]

This is what lets the one-variable Selberg–Delange expansions survive the coprime two-variable convolution uniformly.

Active source: Stage12-N1-3i §2, Stage12-N1-3j §§1–2.

Failure impact: fatal to the stated rectangle error and therefore potentially to the final asymptotic.

### N12 — Radial Stieltjes transfer and extraction of `(log B)^3`

**Class:** `INTERNAL_EXACT`

The full-quadrant harmonic sum is written as the Stieltjes integral

\[
\widetilde{\mathcal H}_\lambda(B)
=
\iint_{x^2+y^2\le B}
\frac{1}{x^2+y^2}\,dT_\lambda(x,y).
\]

The mixed derivative of the leading rectangle term contributes

\[
C_\lambda^{(0)}(\log x+1)(\log y+1)\,dx\,dy.
\]

The cubic part is governed by

\[
I(B)
=
\int_{x,y\ge1\atop x^2+y^2\le B}
\frac{\log x\log y}{x^2+y^2}\,dx\,dy
=
\frac\pi{48}(\log B)^3+O((\log B)^2).
\]

Symmetry and `r<s` then contribute the orientation factor `1/2`.

Active source: constant sheet §§6–8, integrated proof §8, with radial lower-limit details closed by Stage12-N1-3h.

Failure impact: fatal to the claimed logarithmic main term or its factor `1/12`.

### N13 — Rectangle / radial leading constant

**Class:** `CONSTANT_NORMALIZATION`

The parity-weighted coprime rectangle coefficient is

\[
C_\lambda^{(0)}=\frac8{\pi^2}\eta.
\]

Combined with the full-quadrant radial integral `pi/48`, orientation `1/2`, and the fixed-height front factor `B/pi`, this gives

\[
\frac B\pi
\cdot
\frac12
\cdot
\frac\pi{48}
\cdot
\frac{8\eta}{\pi^2}
=
\frac{\eta}{12\pi^2}B.
\]

Active source: constant sheet §§4–8 and integrated proof §§7–8.

Failure impact: major theorem-constant failure; the scale may survive while the stated constant does not.

### N14 — `kappa` / `eta` normalization

**Class:** `CONSTANT_NORMALIZATION`

R09 defines the three-variable Euler product `kappa` and two-variable residue constant `eta` explicitly. Prime-by-prime comparison gives

\[
\frac{\eta}{\kappa}
=
\frac8\pi
\prod_{\ell\ {m odd}}(1-\ell^{-2})^{-1}
=
\pi,
\]

hence

\[
\eta=\pi\kappa.
\]

This is an exact Euler-factor identity, not a numerical observation.

Active source: constant sheet §§1–3 and integrated proof §7.

Failure impact: major failure of the equivalence between the two published constant forms.

### N15 — Uniformity and global remainder passage

**Class:** `INTERNAL_EXACT`

The final asymptotic requires all local approximations to survive summation over the moving radial domain. R09's active error architecture includes:

- fixed-height retained remainder averaged to `o(B(log B)^(-A))`;
- rectangle tail exponent `R^(3/4+epsilon)S + R S^(3/4+epsilon)`;
- arbitrary fixed log-power Selberg–Delange remainder, with the expansion order chosen large enough before summing boxes;
- radial core defined by `R,S>=S0`;
- separate small-coordinate wings from Stage12-N1-3f;
- fixed-height shallow sector from Stage12-N1-3g;
- radial lower-limit and vertical details from Stage12-N1-3h;
- radial arc, Stieltjes boundary, lower rectangle polynomials, floor replacement, `-1` terms, and odd–odd annulus all lower order.

The active conclusion is that every omitted term is `o(B(log B)^3)`.

Active source: integrated proof §§3, 9–10 together with Stage12-N1-3f, 3g, 3h, 3i, 3j precedence.

Failure impact: fatal to theorem status. A correct formal main term without this passage is not an asymptotic proof.

## 4. Critical-path compression

For human review, the sixteen-node graph can be compressed into seven independently meaningful audit targets:

```text
T1  parity-weighted coprime rectangle asymptotic
T2  exact Selberg--Delange theorem + R09 hypothesis/application map
T3  primitive/oriented/common-scale counting interface
T4  radial Stieltjes transfer and the 1/12 factor
T5  uniformity / remainder passage across all regions
T6  Dirichlet-series, Euler-product, and dominant singular factorization
T7  eta / kappa and rectangle-leading-constant normalization
```

These are not seven new proofs. They are review surfaces cut through the frozen R09 proof.

## 5. Ranked human-review targets

Ranking rule: first by theorem-level failure impact, then by number of independent mechanisms coupled inside the node, then by how hard the node is to validate from purely local algebra. The ranking is for **verification priority**, not a claim that lower-ranked nodes are less necessary.

| rank | target | primary nodes | failure impact | why it ranks here |
|---:|---|---|---|---|
| 1 | parity-weighted coprime rectangle asymptotic | N06, N11 | FATAL | widest internal bridge; combines coprimality, parity, two SD expansions, weighted coefficient convolution, and the active `3/4+epsilon` tails |
| 2 | Selberg–Delange theorem/application contract | N09, N10, N08 | FATAL | sole theorem-level external analytic input; exact theorem version and every hypothesis must match the R09 use |
| 3 | primitive/oriented/common-scale interface | N02, N03 | FATAL | determines what is actually being counted; an error here proves an asymptotic for the wrong population |
| 4 | uniformity and remainder passage | N15 | FATAL | converts formal/local main terms into a global asymptotic over the moving radial region |
| 5 | radial Stieltjes transfer and `1/12` | N12, N13 | MAJOR/FATAL | supplies the cubic log and the archimedean/orientation factor; a defect changes the main term |
| 6 | Dirichlet/Euler construction and singular orders | N07, N08 | FATAL | fixes the `z=1` and `z=2` singular structure feeding all SD expansions, but is relatively local to audit |
| 7 | `eta`, `kappa`, and local constant normalization | N13, N14 | MAJOR | exact constant identity; important but more algebraically isolated than the preceding bridges |

### First review-pack implication

Under the Stage12-EX roadmap, the highest-ranked non-duplicative first core question is therefore the **parity-weighted coprime rectangle asymptotic** (`T1`). The roadmap already reserves a separate dedicated Selberg–Delange pack, so `T2` remains independently mandatory rather than being absorbed into `T1`.

This sentence fixes only the EX0 ranking. It does not post a question, choose a venue-specific wording, or begin EX1.

## 6. Known supersession hazards for reviewers

A human reviewer must not reconstruct the proof from an older Stage12 file without applying R09 precedence. In particular:

```text
old R^(1/2+delta) rectangle strengthening = inactive
active rectangle tail = R^(3/4+epsilon)S + R S^(3/4+epsilon)

old retained => min(R,S)>=S0 implication = inactive
active radial decomposition = core + explicit small-coordinate wings

old shallow-sector assertion = inactive
active shallow estimate = Stage12-N1-3g

old specific 3/5 zero-free remainder = not required
active SD remainder = arbitrary fixed log-power from finite-order expansion

old Stage12-N1-2p references for beta bound / cross norm = provenance only
active direct closure = Stage12-N1-3i

global weighted l1 Euler-product step = explicitly expanded by Stage12-N1-3j

J_beta functional equation = never assumed
functional equation is used only for L(s,chi_4)
```

Any external review pack must quote the active form, not a superseded historical statement embedded for provenance.

## 7. EX0 exit state

```text
STAGE12_EX0_CRITICAL_CHAIN_FIXED=true
TOP_HUMAN_REVIEW_TARGETS_RANKED=true
R09_REOPEN_REQUIRED=false
R09_MUTATED=false
EXTERNAL_HUMAN_REVIEW_PERFORMED=false
NUMERICAL_EVIDENCE_USED_AS_PROOF=false
NEXT_STAGE12_EX_TARGET=Stage12-EX1
EX1_PRIMARY_TARGET=PARITY_WEIGHTED_COPRIME_RECTANGLE_ASYMPTOTIC
EX2_RESERVED_TARGET=SELBERG_DELANGE_APPLICATION
```
