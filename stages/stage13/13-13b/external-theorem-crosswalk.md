# Stage13-13b — external theorem and hypothesis crosswalk

> STATUS: `STAGE13_13B_COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT`
>
> INPUT: merged `13-13a` claim/dependency ledger, immutable R03, `13-12ag` explicitness supplement, frozen Stage12 R09 theorem interface.
>
> PURPOSE: replace every generic phrase such as “standard Selberg--Delange/Hecke machinery” by an exact theorem boundary, verify the hypotheses actually used by Stage13, and eliminate external machinery that is stronger than necessary.

## 1. Decision

The audit finds **no failed external hypothesis** and no theorem-level change.

It also finds that the active R03 proof can be made cleaner than its current wording:

1. the quoted Gaussian-Hecke zero-free theorem is valid in the required polylogarithmic angular range, but it is not logically necessary for the nonzero-harmonic coefficient sum used by Stage13;
2. the zero-mode `zeta^1` and `zeta^2` summatory expansions do not require a black-box general Selberg--Delange theorem once the already-proved half-plane holomorphy of the residual factors is used with a finite-order Perron/residue contour;
3. fixed-prime residue transfer needs only finite character orthogonality/CRT plus the same meromorphic-continuation contour argument; no growing-conductor theorem is used;
4. the Selberg--Vaaler interval majorant/minorant is a genuine external approximation input and is now given an explicit primary citation;
5. coarea/Fubini, the weighted Wiener algebra, the Pythagorean parameterization used in Stage13, and infinitude of primes `3 mod 4` can all be discharged internally at the level needed here.

Therefore the final canonical proof may keep the historical Selberg--Delange and zero-free citations as context, but its **minimal logical external boundary** is smaller.

```text
UNMAPPED_EXTERNAL_INPUTS=0
FAILED_EXTERNAL_HYPOTHESES=0
THEOREM_CHANGED=false
STAGE12_R09_REOPENED=false
R03_MUTATED=false
```

---

## 2. Primary literature ledger

### E01 — Hecke analytic continuation and functional equation

**THEOREM USED**

For a nontrivial Hecke Grössencharacter, the associated Hecke `L`-function admits analytic continuation and a functional equation. For the Gaussian angular characters used by Stage13, one may write the completed function in the form

\[
\xi(s,k)=\pi^{-(s+2|k|)}\Gamma(s+2|k|)L(s,\Xi_k),
\qquad
\xi(s,k)=\xi(1-s,k),
\]

up to the fixed normalization convention for the angular index.

**PRIMARY SOURCE / MODERN PRIMARY RESTATEMENT**

- E. Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen*, Math. Z. 1 (1918), 357--376; II, Math. Z. 6 (1920), 11--51.
- B. Huang, J. Liu, Z. Rudnick, *Gaussian primes in almost all narrow sectors*, arXiv:1903.04005, §2.1, which explicitly defines the Gaussian angular characters and records the entire continuation for nonzero angular index and the completed functional equation.

**HYPOTHESES**

- fixed number field `Q(i)`;
- angular character index nonzero for the nonzero-harmonic channel;
- for fixed residue refinements, finite ray-class conductor is fixed before `B -> infinity`.

**WHERE VERIFIED IN STAGE13**

- `13-12aa`: `A_ell(s)=L(s,xi_{8ell})E_{h,ell}(s)` for `ell>=1`;
- `13-12ag` §3.5: no zeta pole in the scale factor;
- `13-12ae` §6: residue characters are imposed only at a fixed finite prime set.

**CONCLUSION IMPORTED**

Analytic continuation and polynomial vertical/conductor growth on every fixed strip used by the Perron contour. For `ell <= (log X)^4`, the archimedean conductor is only polylogarithmic in `X`.

**STATUS**: `APPLIES`.

### E02 — Gaussian-Hecke Landau--Page zero-free region

**THEOREM USED IN R03 WORDING**

For Gaussian angular Hecke characters with finite residue modulus `u`, the product `L_u(s,xi_k)` has at most one zero in a region

\[
\sigma>1-\frac{c}{\log(|u|(2+|t|)(2+|k|))},
\]

and if an exceptional zero exists then it is real, simple and has angular index `k=0`.

**PRIMARY SOURCE**

J. Merikoski, *On Gaussian primes in sparse sets*, Compositio Math. 161 (2025), 181--243, Lemma 2.13, DOI `10.1112/S0010437X24007632`, arXiv:2302.11331.

A broader classical source is M. D. Coleman, *A zero-free region for the Hecke L-functions*, Mathematika 37 (1990), 287--304, DOI `10.1112/S0025579300013000`.

**HYPOTHESES**

- `u` fixed for each Stage13 fixed-local problem;
- `k=8ell`, `ell>=1` for nonzero harmonics;
- `ell <= (log B)^4`.

**WHERE VERIFIED**

`13-12ad` §10 and `13-12ag` §3.5.

**CONCLUSION**

The citation in R03 is correct: the possible exceptional zero is excluded for nonzero angular frequency, and the logarithmic denominator is only `O(log log B)` in the retained range.

**AUDIT REFINEMENT**

Stage13 does **not need** this zero-free region to prove the required coefficient-sum cancellation, because `A_ell(s)` contains `L(s,xi_{8ell})` itself, not its reciprocal, logarithmic derivative, or a fractional power. Zeros do not obstruct the contour shift. E01 plus the already-proved residual holomorphy suffices.

**STATUS**: `VALID_BUT_LOGICALLY_REDUNDANT_FOR_FINAL_PROOF`.

### E03 — classical Selberg--Delange framework

**THEOREM REFERENCED HISTORICALLY**

If a Dirichlet series factors as

\[
F(s)=\zeta(s)^\rho G(s)
\]

with the appropriate analytic regularity of `G`, the Selberg--Delange method supplies finite-order asymptotic expansions of the summatory coefficients.

**PRIMARY SOURCES**

- H. Delange, *Généralisation du théorème de Ikehara*, Ann. Sci. Éc. Norm. Sup. 71 (1954), 213--242, DOI `10.24033/asens.1023`.
- R. de la Bretèche, G. Tenenbaum, *Remarks on the Selberg--Delange method*, Acta Arith. 200 (2021), 349--369, DOI `10.4064/aa201024-26-5`, arXiv:2010.12929.

**STAGE13 HYPOTHESES**

For the zero mode,

\[
A_0(s)=\zeta(s)G_h(s),
\qquad
B_0(s)=\zeta(s)^2G_b(s),
\]

where

\[
G_h(s)=L(s,\chi_4)E_{h,0}(s),
\qquad
G_b(s)=L(s,\chi_4)E_{b,0}(s).
\]

`13-12ag` proves that the residual Euler quotients are `1+O(p^{-2sigma})`, hence the `E` factors converge absolutely and locally uniformly for every

\[
\sigma\ge\frac12+\delta.
\]

Thus `G_h,G_b` are holomorphic in a fixed half-plane containing `s=1`; the pole exponents are the integers `1` and `2`.

**AUDIT REFINEMENT**

For the exact Stage13 need, invoking a general Selberg--Delange theorem is optional. A finite Perron contour shifted to a fixed line `sigma_0` with `5/8<sigma_0<1` crosses only the pole at `s=1`. The residue gives

\[
\sum_{h\le X}a_0(h)=\alpha X+O(X^{1-\delta'}),
\]

and

\[
\sum_{r\le X}b_0(r)
=X(\beta_1\log X+\beta_0)+O(X^{1-\delta'}),
\]

for some fixed `delta'>0`, after the standard truncated-contour estimates. This is more than sufficient for the logarithmic error budget used in `13-12ad`. No fractional zeta power occurs, so there is no branch issue.

**STATUS**: `CLASSICAL_ROUTE_APPLIES; BLACK_BOX_NOT_REQUIRED_AFTER_HYPOTHESIS_AUDIT`.

### E04 — Selberg--Vaaler interval majorant/minorant

**THEOREM USED**

A periodic interval indicator admits pointwise trigonometric majorants/minorants of degree at most `L` whose zero Fourier coefficients differ from the interval length by `O(1/L)`, with controlled nonzero Fourier coefficients.

**PRIMARY SOURCE**

J. D. Vaaler, *Some extremal functions in Fourier analysis*, Bull. Amer. Math. Soc. 12 (1985), 183--216, DOI `10.1090/S0273-0979-1985-15349-2`.

**HYPOTHESES**

- bounded interval indicator on the circle;
- integer trigonometric degree `L>=1`.

**WHERE VERIFIED IN STAGE13**

- the category sets at fixed outer angle are intervals/unions with bounded endpoint complexity;
- `L=(log B)^4` is made integral by harmless flooring;
- the total positive raw mass is `O(B(log B)^3)` by the exact Stage12/Stage13 factor-two bridge plus frozen Stage12 R09.

**CONCLUSION IMPORTED**

The constant-term bracket excess contributes

\[
O\!\left(\frac{B(\log B)^3}{L}\right)
=O(B(\log B)^{-1}),
\]

and the retained Fourier range is `|ell|<=L`.

**STATUS**: `APPLIES`.

---

## 3. Internal discharge of previously ambiguous external steps

### I01 — special Perron/residue pole-order lemma

The final proof only needs the following special case. Suppose

\[
F(s)=\zeta(s)^mH(s),\qquad m\in\{0,1,2\},
\]

where `H` is holomorphic on `sigma>=sigma_0` for some fixed `sigma_0<1`, has polynomial vertical growth there, and the Dirichlet coefficients have polynomial growth. A truncated Perron formula with a rectangular contour gives the pole-order consequences required by Stage13:

- `m=0`: no pole and a power-saving summatory bound;
- `m=1`: one residue proportional to `X`;
- `m=2`: a residue `X(c_1 log X+c_0)`;

with a fixed power-saving remainder after choosing contour height as a suitable fixed power of `X`.

For Stage13 choose any `sigma_0>5/8`. The residual factors are holomorphic there, and the Hecke/Dirichlet factors have polynomial strip growth. Polylogarithmic angular conductor is absorbed by the power saving.

This special contour calculation will be written directly in `13-13c`.

```text
PERRON_SPECIAL_CASE_HYPOTHESES_VERIFIED=true
GENERAL_SELBURG_DELANGE_REQUIRED=false
```

### I02 — nonzero Gaussian harmonic cancellation

For `ell>=1`,

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s)
\]

has no pole. By E01 and the residual Euler-product bound, I01 applies uniformly for

\[
1\le\ell\le(\log X)^4.
\]

Thus for some fixed `delta'>0` and fixed `C`,

\[
\sum_{h\le X}a_\ell(h)
\ll X^{1-\delta'}(1+\ell)^C.
\]

On the retained polylogarithmic range this is stronger than any fixed logarithmic saving required by the `A=48` budget. Zeros of `L(s,xi_{8ell})` do not obstruct this argument.

```text
NONZERO_HARMONIC_CANCELLATION_HYPOTHESES_VERIFIED=true
ZERO_FREE_REGION_NEEDED_FOR_THIS_STEP=false
```

### I03 — fixed-prime residue transfer

For a fixed prime set `S`, all congruence predicates are finite functions on finite residue groups. Character orthogonality gives an exact finite decomposition, and CRT tensors the local groups.

For the principal character tuple, the same zeta poles remain and the leading local factor is multiplied by the exact acceptance product. For every nonprincipal tuple, at least one principal zeta factor is replaced by a nonprincipal Dirichlet/Hecke factor holomorphic at `s=1`; I01 lowers its order. The conductors are fixed because `S` is frozen before `B->infinity`.

No theorem uniform in a modulus growing with `B` is used.

```text
CHARACTER_ORTHOGONALITY=FINITE_GROUP_IDENTITY
CRT=FINITE_RING_IDENTITY
FIXED_S_THEN_B_LIMIT=true
GROWING_MODULUS_THEOREM_USED=false
```

### I04 — coarea/Fubini step

The actual Stage13 coordinate calculation gives

\[
w_q\,d\omega=d\theta\,d\alpha.
\]

The integrand is nonnegative, so Tonelli applies before finiteness is known. The resulting angular domain has finite measure, proving finiteness and then ordinary Fubini. Therefore

\[
I_q=\int\ell_q(\psi)\,d\psi
\]

has no hidden regularity hypothesis.

```text
COAREA_FUBINI_HIDDEN_HYPOTHESIS=false
```

### I05 — weighted Wiener algebra

The norm

\[
\|F\|_\rho=\sum|f_{a,b,c}|\rho^{a+b+c}
\]

is submultiplicative directly from the Cauchy product and Tonelli for nonnegative absolute values. `13-12ad` proves explicit inverse bounds and

\[
\|C_{\ell,p}-1\|_{5/8}\le529p^{-5/4}.
\]

No external Wiener lemma is needed.

```text
EXTERNAL_WIENER_THEOREM_REQUIRED=false
```

### I06 — Pythagorean parameterization / parity branches

Stage13 uses the already-locked primitive outer formulas

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\qquad(r,s)=1,
\]

with OE/EE parity variants. These are algebraic identities and the 2-adic branch distinction is finite. Stage13 needs no separate external asymptotic counting theorem for Pythagorean triples; the asymptotic total mass is imported only through frozen Stage12 R09.

```text
ADDITIONAL_EXTERNAL_PYTHAGOREAN_COUNTING_THEOREM_REQUIRED=false
```

### I07 — infinitely many inert primes

The fixed-set squeeze only needs arbitrarily many primes `p=3 mod 4`. Dirichlet's theorem on primes in arithmetic progressions is unnecessary: if `p_1,...,p_k` were all such primes, then

\[
N=4p_1\cdots p_k-1\equiv3\pmod4
\]

has a prime divisor `q=3 mod4` not among the `p_i`. Thus `13-13c` should use this elementary argument.

```text
DIRICHLET_AP_THEOREM_REQUIRED=false
```

---

## 4. Claim-by-claim mapping back to 13-13a

| Claim | External issue in 13-13a | 13-13b disposition |
|---|---|---|
| C05 | coarea/Fubini | discharged by I04 |
| C06 | Selberg--Delange + Hecke | E01 + I01/I02; hypotheses verified |
| C10 | finite-order analytic inputs + Vaaler | I01/I02 + E04 |
| C11 | parity branch uniformity | finite local factor; no new theorem |
| C19 | fixed-conductor transfer | I03; no growing modulus |
| C20 | infinitely many inert primes | I07; no Dirichlet AP theorem needed |
| C26 | general Selberg--Delange | E03 valid; replace by special Perron I01 |
| C27 | Gaussian-Hecke cancellation | E01 + I02; Merikoski E02 valid but redundant |
| C28 | CRT/characters | I03, finite algebra plus E01 for nonprincipal `L` factors |

No other claim in the 30-claim ledger carries an unresolved external analytic dependency.

---

## 5. Minimal external theorem boundary for 13-13c

```text
FROZEN_UPSTREAM:
  Stage12 R09 total primitive-oriented asymptotic

EXTERNAL_ANALYTIC_INPUTS:
  Hecke/Dirichlet L-function analytic continuation, functional equation,
  and polynomial strip/conductor growth for the fixed field Q(i) and fixed residue conductors

EXTERNAL_APPROXIMATION_INPUT:
  Vaaler 1985 periodic interval trigonometric majorant/minorant

INTERNALIZED_IN_STAGE13:
  special Perron/residue pole-order lemma
  nonzero-harmonic contour cancellation
  fixed-character orthogonality and CRT
  coarea/Tonelli/Fubini check
  weighted Wiener norm algebra
  Pythagorean algebra/parity bookkeeping
  infinitude of primes 3 mod 4
```

The historically cited Selberg--Delange and Merikoski/Coleman zero-free results remain mathematically compatible with the proof, but neither is necessary as an additional logical gate once the special contour argument is written explicitly.

---

## 6. Final lock

No contradiction with the 13-13a frozen theorem was found.

```text
STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
UNMAPPED_EXTERNAL_INPUTS=0
FAILED_EXTERNAL_HYPOTHESES=0
MINIMAL_EXTERNAL_BOUNDARY_LOCKED=true
HECKE_ANALYTIC_CONTINUATION_FUNCTIONAL_EQUATION_REQUIRED=true
VAALER_INTERVAL_MAJORANT_REQUIRED=true
GENERAL_SELBURG_DELANGE_BLACK_BOX_REQUIRED=false
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED_FOR_FINAL_PROOF=false
MERIKOSKI_ZERO_FREE_CITATION_VALID=true
GROWING_MODULUS_INPUT_USED=false
DIRICHLET_AP_THEOREM_REQUIRED=false
THEOREM_CHANGED=false
R03_MUTATED=false
STAGE12_R09_REOPENED=false
NEXT=13-13c
```
