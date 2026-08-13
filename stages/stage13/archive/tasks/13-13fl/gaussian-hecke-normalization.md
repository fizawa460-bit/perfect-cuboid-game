# Stage13-13fl — Gaussian-Hecke primary-source normalization

> STATUS: `R06_GATE_B_GAUSSIAN_HECKE_NORMALIZATION`

This gate closes the R05 external-review objection concerning the exact Gaussian-Hecke character normalization and completed functional equation used by the nonzero angular modes.

## 1. Primary-source normalization actually used

Huang–Liu–Rudnick, §2.1, define for a nonzero Gaussian ideal `a=(alpha)`

\[
\Xi_k(\mathfrak a)=\left(\frac{\alpha}{\bar\alpha}\right)^{2k}=e^{i4k\theta_{\mathfrak a}},\qquad k\in\mathbf Z.
\]

For `k != 0` they state that `L(s,Xi_k)` is entire and that

\[
\xi(s,k)=\pi^{-(s+2|k|)}\Gamma(s+2|k|)L(s,\Xi_k)=\xi(1-s,k).
\]

Thus the gamma shift `2|k|` in R05 is correct **when `k` denotes the HLR Hecke-character index**.

## 2. Remove the R05 indexing ambiguity

The Stage13 Fourier analysis is naturally written in terms of an angular exponential

\[
e^{i m\theta}.
\]

The source character `Xi_k` produces angular exponent `m=4k`. Therefore the exact translation is

```text
HLR index k = m/4.
```

In particular, if the proof-facing retained mode is written as

\[
m=8\ell,\qquad \ell\ge1,
\]

then the corresponding source character is

\[
\boxed{k_{HLR}=2\ell},
\]

not `k_HLR=8 ell`. Any earlier phrase “Hecke k=8 ell” is therefore only safe if `k` meant the Fourier exponent rather than the HLR character index. R06 must use separate symbols and the exact map above.

For the retained family the completed factor is consequently

\[
\pi^{-(s+4\ell)}\Gamma(s+4\ell)L(s,\Xi_{2\ell}),
\]

and `L(s,Xi_{2 ell})` is entire for every `ell>=1`, hence has no pole at `s=1`.

## 3. What the proof consumes

The Stage13 harmonic estimate does not consume a numerical conductor exponent. It needs only:

1. entire continuation for every retained nonzero angular mode;
2. no pole at `s=1`;
3. a functional equation with an explicit gamma factor whose shift is linear in `ell`;
4. polynomial growth on any fixed vertical strip after applying Stirling and Phragmen–Lindelof;
5. the same conclusions after multiplying by one of finitely many fixed residue/ray-class twists.

Items 1–3 follow directly from the HLR normalization above for the untwisted angular family. Item 4 follows from the displayed functional equation, absolute convergence on a right boundary, Stirling for `Gamma(s+4 ell)`, and Phragmen–Lindelof; only existence of fixed exponents `C_H,D_H` is used.

For item 5, the finite residue conditions used in Stage13 range over a fixed finite set independent of `B` and `ell`. They correspond to fixed finite-order Hecke/ray-class characters. Multiplying such a character by `Xi_{2 ell}` leaves nonzero infinity type for `ell>=1`, so the resulting Hecke character is nontrivial and its L-function is holomorphic at `s=1`; its finite conductor is bounded inside the fixed twist family. The proof therefore requires no growing-modulus theorem.

## 4. Uniform proof-facing interface

For every retained `ell>=1` and every twist `omega` in the fixed finite twist set, the R06 interface is

\[
L(s,\Xi_{2\ell}\otimes\omega)
\]

with no pole at `s=1` and fixed-strip polynomial growth in `|t|+ell`. Hence the Riesz/Perron argument may retain the abstract bound

\[
S_\ell(X)\ll X^{1-\delta_H}(1+\ell)^{C_H}(\log(2X))^{D_H}
\]

for fixed positive `delta_H` and fixed finite exponents `C_H,D_H`; no numerical value of those exponents is part of the theorem contract.

## 5. Source lock

Primary normalization checked against:

- B. Huang, J. Liu, Z. Rudnick, *Gaussian primes in almost all narrow sectors*, §2.1: `Xi_k=(alpha/bar alpha)^{2k}=e^{i4k theta}`, entire continuation for `k!=0`, and completed equation `pi^{-(s+2|k|)} Gamma(s+2|k|) L(s,Xi_k)=xi(1-s,k)`.
- J. Merikoski, *On Gaussian primes in sparse sets*, §2.7, as an independent modern proof context using Hecke L-functions over `Q(i)`; no incompatible angular normalization is imported from it.

```text
STAGE13_13FL=COMPLETE_GAUSSIAN_HECKE_PRIMARY_SOURCE_NORMALIZATION
R06_GATE_B=COMPLETE
HLR_XI_K=(alpha/bar_alpha)^(2k)
HLR_ANGULAR_EXPONENT=4k
HLR_GAMMA_SHIFT=2*abs(k)
PROOF_FOURIER_EXPONENT=8*ell
PROOF_TO_HLR_INDEX=k_HLR=2*ell
RETAINED_ELL_MIN=1
NONZERO_ANGULAR_L_ENTIRE=true
NONZERO_ANGULAR_POLE_AT_1=false
FIXED_FINITE_TWISTS_ONLY=true
GROWING_MODULUS_THEOREM_USED=false
POLYNOMIAL_STRIP_GROWTH_SUFFICIENT=true
UNMAPPED_HECKE_ASSUMPTIONS=0
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
NEXT=13-13fm
```