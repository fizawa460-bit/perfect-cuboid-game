# Stage13-13ff — exact external theorem contracts for R05

> STATUS: `STAGE13_13FF_EXTERNAL_THEOREM_CONTRACTS`
>
> PURPOSE: expose the complete proof-facing external boundary used by the repaired Stage13 proof. No phrase such as “standard Hecke theory” or “controlled Vaaler coefficients” is accepted as a proof step after this gate.
>
> INPUTS: Stage13-13b hypothesis crosswalk, Gate D harmonic-conductor ledger, Gate E Stage12 counting interface.
>
> SCOPE: external analytic continuation / functional equations for the relevant Dirichlet and Gaussian-Hecke L-functions, and Vaaler’s periodic sawtooth approximation. The Perron/Riesz conversion and the interval-polynomial construction are written internally below.

---

## 1. Source ledger and normalization

The proof uses the following primary sources.

1. **Hecke, 1918/1920.** E. Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen*, Math. Z. 1 (1918), 357–376; II, Math. Z. 6 (1920), 11–51.
2. **Modern Gaussian restatement.** B. Huang, J. Liu, Z. Rudnick, *Gaussian primes in almost all narrow sectors*, arXiv:1903.04005, §2.1. For the Gaussian characters
   \[
   \Xi_k(\mathfrak a)=e^{i4k\theta_{\mathfrak a}},
   \]
   they record for `k != 0` entire continuation and the completed functional equation
   \[
   \xi(s,k)=\pi^{-(s+2|k|)}\Gamma(s+2|k|)L(s,\Xi_k)=\xi(1-s,k).
   \]
3. **Finite Gaussian residue twists.** J. Merikoski, *On Gaussian primes in sparse sets*, Compositio Math. 161 (2025), 181–243, §2.7. For a Gaussian residue character `chi` modulo `u`, the paper defines
   \[
   L(s,\xi_k\chi)
   =\sum_{(\mathfrak a,2)=1}
   \frac{\xi_k(\mathfrak a)\chi(\mathfrak a)}{(N\mathfrak a)^s}.
   \]
   Stage13 uses only **fixed** finite residue conductor in the overlap transfer. No theorem uniform in a modulus growing with `B` is imported.
4. **Vaaler.** J. D. Vaaler, *Some extremal functions in Fourier analysis*, Bull. Amer. Math. Soc. 12 (1985), 183–216. We import the finite-degree sawtooth approximation stated below and derive the interval majorants/minorants ourselves.

The historical Gaussian zero-free citation (Merikoski Lemma 2.13 / Coleman) is valid but is not a logical input to the final nonzero-harmonic contour, because that contour contains `L` itself rather than `1/L` or `L'/L`.

---

## 2. Contract H1 — nonzero Gaussian angular Hecke L-functions

Let `k` be a nonzero integer. For the Gaussian angular character `Xi_k` on ideals of `Z[i]`, define for `Re s>1`

\[
L(s,\Xi_k)=\sum_{\mathfrak a\neq0}\frac{\Xi_k(\mathfrak a)}{(N\mathfrak a)^s}.
\]

### Imported statement

For `k != 0`:

1. `L(s,Xi_k)` continues holomorphically to all `s in C`;
2. the completed function
   \[
   \xi(s,k)=\pi^{-(s+2|k|)}\Gamma(s+2|k|)L(s,\Xi_k)
   \]
   satisfies
   \[
   \xi(s,k)=\xi(1-s,k);
   \]
3. hence `L(s,Xi_k)` has **no pole at `s=1`**.

Stage13 uses angular indices `k=8 ell`, `ell>=1`; therefore every retained nonzero harmonic is in the holomorphic case.

```text
HECKE_NONZERO_ENTIRE=true
HECKE_NONZERO_FUNCTIONAL_EQUATION=true
HECKE_NONZERO_POLE_AT_1=false
ANGULAR_INDEX=k=8*ell
```

---

## 3. Contract H2 — fixed finite residue twists

For Gate G, fix once and for all a finite set of inert primes `S`, and let `u` be the resulting finite Gaussian residue modulus. Let `chi` range over the finite character group attached to that fixed modulus.

The product `xi_k chi` is a Hecke character of `Q(i)`. We import the classical Hecke continuation/functional-equation theorem in the following proof-facing form:

- if `xi_k chi` is nontrivial, `L(s,xi_k chi)` is holomorphic at `s=1` and admits analytic continuation and a Hecke functional equation;
- the only possible pole at `s=1` belongs to the trivial Hecke character;
- because `S` is fixed before `B -> infinity`, every finite conductor parameter occurring here is a fixed constant for that limiting problem.

The exact root number and the exact conductor normalization are not used by Stage13. Only continuation, pole/no-pole status, and fixed-strip polynomial growth are used.

```text
FIXED_RESIDUE_CONDUCTOR=true
NONTRIVIAL_HECKE_TWIST_HOLOMORPHIC_AT_1=true
ONLY_TRIVIAL_HECKE_CHARACTER_HAS_POLE_AT_1=true
GROWING_MODULUS_THEOREM_USED=false
```

Merikoski §2.7 supplies the exact Gaussian residue-character model used by the repository; its Landau–Page lemma is not needed for the final contour.

---

## 4. Contract D1 — the Dirichlet factor `L(s,chi_4)`

The zero-mode factors contain the primitive nonprincipal Dirichlet character modulo `4`,

\[
\chi_4(n)=
\begin{cases}
0,&2\mid n,\\
1,&n\equiv1\pmod4,\\
-1,&n\equiv3\pmod4.
\end{cases}
\]

We import the classical Dirichlet-L theorem in exactly the form needed here:

- `L(s,chi_4)` is holomorphic at `s=1` and continues holomorphically to `C`;
- its completed L-function satisfies the standard functional equation;
- on every fixed vertical strip it has polynomial growth.

No zero-free region and no prime-number theorem in arithmetic progressions is required for Stage13.

```text
CHI4_NONPRINCIPAL=true
L_CHI4_HOLOMORPHIC_AT_1=true
DIRICHLET_AP_THEOREM_REQUIRED=false
```

---

## 5. Internal consequence — polynomial strip/angular growth

DeepSeek’s R04 objection correctly asked what “polynomial strip/conductor growth” actually means in the proof. We now make the logical interface explicit.

Fix a strip

\[
\sigma_-\le \Re s\le\sigma_+,
\qquad \sigma_-<1<\sigma_+,
\]

with Stage13 ultimately taking `sigma_-=3/4` after the residual Euler factor has been separated.

For the untwisted nonzero angular family, absolute convergence gives a uniform bound on the right boundary `Re s=sigma_+>1`. On the reflected left boundary, the functional equation expresses `L(s,Xi_k)` as a ratio of gamma factors times `L(1-s,Xi_k)`. Stirling’s formula on a fixed strip gives a bound by a fixed power of

\[
2+|t|+|k|.
\]

Phragmén–Lindelöf across the fixed strip therefore yields constants `C_strip,D_strip` depending only on the chosen strip such that

\[
\boxed{
|L(\sigma+it,\Xi_k)|
\ll
(2+|t|+|k|)^{C_{\rm strip}}
}
\]

for all `k!=0` and all `sigma` in the strip. Fixed finite residue twists satisfy the same type of statement with an additional fixed conductor factor; because `S` is fixed, that factor is absorbed into the implied constant.

The residual Euler/Wiener factor `E_{h,ell}(s)` from Gate B is holomorphic and phase-uniform on the required half-plane. Hence

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s)
\]

has polynomial growth in `|t|+ell` on `Re s>=3/4`.

This section is an internal deduction from H1/H2/D1 plus Stirling and Phragmén–Lindelöf; it is not a new number-theoretic black box.

```text
POLYNOMIAL_STRIP_GROWTH_DERIVED=true
POLYNOMIAL_ANGULAR_GROWTH_DERIVED=true
FIXED_STRIP_LEFT=3/4
```

---

## 6. Internal consequence — why the Gate D summatory power saving follows

A bare phrase “shift Perron” is too terse when only polynomial vertical growth is known. We therefore state the smoothing step that makes the implication rigorous.

Let

\[
F_\ell(s)=\sum_{n\ge1}a_\ell(n)n^{-s}
\]

be holomorphic on `Re s>=sigma_0` for a fixed `sigma_0<1`, and suppose on that half-plane it has polynomial growth in `|t|+ell`. Gate B supplies the required uniform coefficient majorants for the residual convolution.

Choose an integer `m` larger than the fixed vertical-growth exponent and use the `m`-fold Riesz/Perron kernel

\[
\frac{X^s}{s(s+1)\cdots(s+m)}.
\]

The denominator kills the polynomial vertical growth, so the contour can be shifted from `Re s>1` to `Re s=sigma_0` without crossing a pole for `ell>=1`. This gives a smoothed bound

\[
R_{m,\ell}(X)
\ll
X^{\sigma_0}(1+\ell)^C(\log 2X)^D.
\]

Finite differencing with a step `H=X^{1-eta}` converts the Riesz sum to the ordinary partial sum. The short transition interval is bounded by the coefficient majorant. Since `sigma_0<1`, choose fixed `eta>0` small enough to leave a positive power gap. Consequently there exist fixed

\[
\delta_H>0,\qquad C_H,D_H\ge0
\]

such that

\[
\boxed{
S_\ell(X)=\sum_{n\le X}a_\ell(n)
\ll X^{1-\delta_H}(1+\ell)^{C_H}(\log 2X)^{D_H}
}
\]

uniformly for all `X>=2`, `ell>=1`.

This is exactly the Gate D interface. No numerical value of `delta_H,C_H,D_H` is required, because Gate D keeps their polynomial loss visible and absorbs it by the stretched exponential from `H_0`.

```text
HECKE_FAMILY_SUMMATORY_INTERFACE_DERIVED=true
UNSMOOTHED_PERRON_SHORTCUT_USED=false
RIESZ_PERRON_SMOOTHING_EXPLICIT=true
FIXED_A48_REQUIRED=false
```

---

## 7. Contract V1 — Vaaler sawtooth approximation

Let

\[
e(x)=e^{2\pi i x},
\qquad
\psi(x)=\{x\}-\frac12
\]

away from integers, with the conventional midpoint value at discontinuities. For every integer `L>=1`, Vaaler’s finite Fourier approximation gives a trigonometric polynomial

\[
\psi_L(x)
=
\sum_{1\le |h|\le L}
\frac{a_h}{-2\pi i h}e(hx),
\qquad 0\le a_h\le1,
\]

and the pointwise error bound

\[
\boxed{
|\psi(x)-\psi_L(x)|
\le
E_L(x)
:=
\frac1{2L+2}
\sum_{|h|\le L}
\left(1-\frac{|h|}{L+1}\right)e(hx).
}
\]

The right side is a nonnegative Fejér-kernel multiple.

This sawtooth statement is the only Vaaler result imported as a black box.

---

## 8. Internal derivation — interval majorant/minorant and exact coefficients

Let `I=(alpha,beta]` be an interval on `R/Z`, with length `|I|` interpreted modulo one. Away from endpoints,

\[
1_I(x)
=|I|+\psi(\alpha-x)+\psi(x-\beta).
\]

Define

\[
P_{I,L}^{\pm}(x)
=|I|
+\psi_L(\alpha-x)+\psi_L(x-\beta)
\pm E_L(\alpha-x)\pm E_L(x-\beta).
\]

Then pointwise (with the usual endpoint convention)

\[
\boxed{
P_{I,L}^-(x)\le1_I(x)\le P_{I,L}^+(x).
}
\]

Both polynomials have degree at most `L`.

### Zero mode

Each `E_L` has constant coefficient `1/(2L+2)`, so

\[
\boxed{
\widehat P_{I,L}^{\pm}(0)
=|I|\pm\frac1{L+1}.
}
\]

Thus the bracket excess is exactly `1/(L+1)=O(1/L)`.

### Nonzero coefficients

For `1<=|h|<=L`, the two sawtooth terms together contribute at most

\[
\frac1{\pi |h|}
\]

in absolute value, and the two error kernels contribute at most

\[
\frac1{L+1}.
\]

Therefore

\[
\boxed{
|\widehat P_{I,L}^{\pm}(h)|
\le
\frac1{\pi|h|}+\frac1{L+1}<1
\qquad(1\le|h|\le L).
}
\]

This is stronger than Gate D needs: the Vaaler coefficient contributes **no positive power of the harmonic index**.

A union of a bounded number of intervals is handled by summing the corresponding polynomials; all constants are multiplied only by that fixed endpoint-complexity bound.

```text
VAALER_IMPORTED_OBJECT=SAWTOOTH_APPROXIMATION
VAALER_INTERVAL_MAJORANT_DERIVED_INTERNALLY=true
VAALER_ZERO_MODE_EXCESS=1/(L+1)
VAALER_NONZERO_COEFFICIENT_BOUND_LT=1
VAALER_POSITIVE_ELL_POWER=0
```

---

## 9. Application to the Stage13 harmonic ledger

Take

\[
L=\lfloor(\log B)^4\rfloor.
\]

The interval zero-mode excess is `O(1/L)`. Multiplying by the positive raw total mass `O(B(log B)^3)` gives

\[
O\!\left(B(\log B)^{-1}\right).
\]

For the nonzero modes, the coefficient bound `<1` combines with Gate D’s family estimate and gives

\[
\mathcal E_{\rm harm,core}
\ll
B(\log B)^{4C_H+D_H+6}
\exp\{-\delta_H(\log B)^{1/4}\},
\]

which is smaller than every fixed negative logarithmic power.

Thus the external input and the internal bookkeeping now meet without an unspecified coefficient constant or an unexplained conductor exponent.

---

## 10. What is explicitly *not* imported

The final R05 route does **not** require:

- a Gaussian-Hecke zero-free region;
- a zero-density theorem;
- a general Selberg–Delange black box;
- a theorem uniform in a residue modulus growing with `B`;
- Dirichlet’s theorem on primes in arithmetic progressions;
- an external Wiener lemma.

The zero mode uses the internal pole-order Perron/Riesz argument with `zeta(s)` and `zeta(s)^2`; the nonzero angular mode uses H1 plus the internal smoothed contour argument above.

---

## 11. Gate F locks

```text
STAGE13_13FF=COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS
HECKE_NONZERO_ENTIRE=true
HECKE_NONZERO_FUNCTIONAL_EQUATION=true
HECKE_NONZERO_POLE_AT_1=false
FIXED_RESIDUE_CONDUCTOR=true
NONTRIVIAL_HECKE_TWIST_HOLOMORPHIC_AT_1=true
L_CHI4_HOLOMORPHIC_AT_1=true
POLYNOMIAL_STRIP_GROWTH_DERIVED=true
POLYNOMIAL_ANGULAR_GROWTH_DERIVED=true
RIESZ_PERRON_SMOOTHING_EXPLICIT=true
HECKE_FAMILY_SUMMATORY_INTERFACE_DERIVED=true
VAALER_IMPORTED_OBJECT=SAWTOOTH_APPROXIMATION
VAALER_INTERVAL_MAJORANT_DERIVED_INTERNALLY=true
VAALER_ZERO_MODE_EXCESS=1/(L+1)
VAALER_NONZERO_COEFFICIENT_BOUND_LT=1
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
GENERAL_SELBERG_DELANGE_REQUIRED=false
GROWING_MODULUS_THEOREM_USED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13fg
```
