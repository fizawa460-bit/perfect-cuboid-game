# Stage13-13fq — R07 fixed finite Hecke/ray-class twist contract

> STATUS: `R07_GATE_A_FIXED_TWIST_HECKE_CONTRACT`
>
> PURPOSE: close the R06 review objection that the finite residue twists were asserted to inherit the untwisted Gaussian-Hecke analytic properties without an equally explicit proof-facing contract.
>
> SCOPE: the nonzero angular factors arising after a fixed finite inert-prime set `S` is chosen. No estimate uniform in a modulus growing with `B` is used or needed.

## 1. Exact source-family identification

Two source normalizations occur in the Stage13 proof.

Huang--Liu--Rudnick §2.1 uses

\[
\Xi_k(\mathfrak a)
=\left(\frac{\alpha}{\bar\alpha}\right)^{2k}
=e^{i4k\theta_{\mathfrak a}},
\]

and for `k != 0`

\[
\pi^{-(s+2|k|)}\Gamma(s+2|k|)L(s,\Xi_k)
\]

is entire and satisfies the `s <-> 1-s` functional equation.

Stage13 retains Fourier exponent

\[
m=8\ell,\qquad \ell\ge1,
\]

so the HLR index is

\[
\boxed{k_{\rm HLR}=2\ell}
\]

and the archimedean gamma shift is

\[
\boxed{2|k_{\rm HLR}|=4\ell}.
\]

Merikoski §2.7 uses primary Gaussian generators and writes

\[
\xi_j(z)=\left(\frac z{|z|}\right)^j=e^{ij\arg z}.
\]

Thus on the retained family

\[
\boxed{\Xi_{2\ell}=\xi_{8\ell}}.
\]

This translation is important: the Merikoski twisted family corresponding to the Stage13 retained harmonic is exactly

\[
L(s,\xi_{8\ell}\chi)
=L(s,\Xi_{2\ell}\chi).
\]

Merikoski defines this Hecke `L`-function for every finite Gaussian residue character

\[
\chi\in\widehat{(\mathbf Z[i]/u\mathbf Z[i])^\times}.
\]

## 2. The actual finite family needed after fixing S

Fix a finite inert-prime set

\[
S=\{p_1,\dots,p_r\}
\]

before `B -> infinity`. Put `M_S=product_{p in S} p`.

The fixed-S acceptance predicate depends on finitely many residue coordinates modulo the primes in `S`, together with the already-fixed 2-adic parity branch. Choose one Gaussian modulus `u_S` divisible by `M_S` and by the fixed 2-adic normalization modulus required to encode those residue coordinates. The exact minimal modulus is irrelevant to the analytic argument; what matters is

```text
u_S depends only on fixed S and the fixed parity branch,
not on B and not on ell.
```

Let

\[
\mathcal X_S^{\rm Gau}
:=\widehat{(\mathbf Z[i]/u_S\mathbf Z[i])^\times}.
\]

The actual Gaussian characters with nonzero coefficients in the finite Fourier expansion form a subset of this finite group. We prove the analytic contract for the entire ambient group `X_S^Gau`, which is stronger and avoids any dependence on the later R07-B explicit residue-coordinate calculation.

For each retained `ell>=1` and each `omega in X_S^Gau`, define

\[
\Psi_{\ell,\omega}=\Xi_{2\ell}\,\omega
=\xi_{8\ell}\,\omega.
\]

The ordinary rational-unit characters appearing in the same fixed-S Fourier expansion are finite Dirichlet characters and are handled by the classical Dirichlet `L`-function contract; the only issue repaired here is the Gaussian/ray-class factor.

## 3. Why the product is again a Hecke character

`omega` is finite order and therefore has trivial archimedean type. `Xi_{2ell}` is a Hecke character whose archimedean component has nonzero angular type `8ell` in Merikoski notation. Their product is therefore another Hecke/ray-class character of `Q(i)`.

Its finite conductor divides a modulus determined by `u_S` and the fixed base normalization of `Xi`; hence the set

\[
\{\mathfrak f_{\ell,\omega}:\omega\in\mathcal X_S^{\rm Gau}\}
\]

is finite and, in fact, independent of both `B` and `ell` at the finite places. We denote this finite conductor set by `F_S`.

The infinity type cannot become trivial: multiplying by a finite-order character changes only the finite component. Thus for every retained `ell>=1`,

\[
\boxed{\Psi_{\ell,\omega}\text{ has nonzero infinity type}.}
\]

In particular `Psi_{ell,omega}` is never the trivial Hecke character.

## 4. Primitive reduction and holomorphy at s=1

A residue character `omega` may be imprimitive. Replace it by its primitive inducing character `omega^*`. Then

\[
L(s,\Psi_{\ell,\omega})
=L(s,\Psi_{\ell,\omega^*})\,E_{S,\omega}(s),
\]

where `E_{S,omega}` is a finite Euler polynomial coming only from primes dividing the fixed modulus. It is entire and bounded polynomially on every fixed strip.

Classical Hecke theory applies to the primitive nontrivial character `Psi_{ell,omega^*}`. Because its infinity type is nonzero, its Hecke `L`-function is entire; in particular

\[
\boxed{L(s,\Psi_{\ell,\omega})\text{ is holomorphic at }s=1}
\]

for every `ell>=1` and every fixed residue twist `omega`.

This is also structurally consistent with Merikoski's §2.7 Landau--Page statement: any possible exceptional near-one zero in the family `L(s,xi_j chi)` must have `j=0`, while the retained Stage13 family has `j=8ell != 0`. Stage13 does not use that zero-free region; it is only an independent check that the retained family lies in the nonzero-angular sector.

## 5. Exact completed shape for primitive twists

For a primitive twist let `f_omega` denote its finite conductor and put `Q_omega=N(f_omega)`. The finite twist does not alter the archimedean type, so the completed function has the same gamma shift `4ell` as the HLR untwisted family:

\[
\Lambda(s,\Psi_{\ell,\omega})
=Q_\omega^{s/2}
\pi^{-(s+4\ell)}
\Gamma(s+4\ell)
L(s,\Psi_{\ell,\omega}).
\]

Up to the standard unit-modulus root number it satisfies

\[
\Lambda(s,\Psi_{\ell,\omega})
=\varepsilon_{\ell,\omega}
\Lambda(1-s,\overline{\Psi}_{\ell,\omega}),
\qquad |\varepsilon_{\ell,\omega}|=1.
\]

The exact root number is not used anywhere in Stage13. The only proof-facing facts consumed later are:

1. the gamma shift is `4ell`;
2. `Q_omega` belongs to a finite set depending only on fixed `S`;
3. the function is entire for `ell>=1`;
4. the functional equation reflects one fixed vertical strip to another.

## 6. Common fixed-strip polynomial growth

Choose one fixed `epsilon_0>0`, for example `epsilon_0=1/4`, and work on

\[
-\epsilon_0\le\sigma\le1+\epsilon_0.
\]

On the right boundary `sigma=1+epsilon_0`, absolute convergence gives a bound uniform in `ell` and in every `omega in X_S^Gau`.

On the left boundary, the functional equation reflects to the absolutely convergent right boundary. The conductor factor is bounded by a constant depending only on fixed `S`. Stirling's formula on a fixed strip gives

\[
\left|
\frac{\Gamma(1-s+4\ell)}{\Gamma(s+4\ell)}
\right|
\ll
(2+|t|+\ell)^{C_0}
\]

with one exponent `C_0` depending only on the strip, not on `ell` and not on the finite twist.

Phragmen--Lindelof therefore gives constants `C_S>=0` and `A_S>0` such that, simultaneously for every `omega in X_S^Gau`, every `ell>=1`, and every point of the fixed strip,

\[
\boxed{
|L(\sigma+it,\Psi_{\ell,\omega})|
\le A_S(2+|t|+\ell)^{C_S}.
}
\]

Because `X_S^Gau` and the conductor set are finite, the common constants are simply the maxima over finitely many primitive finite parts. No constant depends on `B`.

The same argument applies to the finitely many nonprincipal rational Dirichlet characters on the rational pole channels. Principal rational characters are deliberately not put in this holomorphic class; those are exactly the channels that retain zeta poles.

## 7. Riesz/Perron interface

The Stage13 contour uses `L` itself, not `1/L` or `L'/L`, so no zero-free region is required.

Take a Riesz order larger than the common vertical-growth exponent. Shift the smoothed contour to the fixed line used by Stage13 (in particular the `sigma=3/4` line lies inside the strip), and then recover a sharp summatory bound by finite differencing and the existing positive coefficient majorant.

Thus, for each fixed `S`, there exist

\[
\delta_S>0,\qquad C_{H,S},D_{H,S}\ge0
\]

such that the full fixed-twist retained family satisfies

\[
\boxed{
S_{\ell,\omega}(X)
\ll_S
X^{1-\delta_S}
(1+\ell)^{C_{H,S}}
(\log(2X))^{D_{H,S}}
}
\]

uniformly for

```text
X >= 2,
ell >= 1,
omega in X_S^Gau.
```

The proof only takes `B -> infinity` with `S` fixed, so dependence of the implied constant and polynomial exponents on `S` is harmless. No `S=S(B)` occurs.

## 8. Source ledger

Primary proof-facing sources:

1. E. Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen*, Math. Z. 1 (1918), 357--376; II, Math. Z. 6 (1920), 11--51 — general Hecke-character continuation and functional equation.
2. B. Huang, J. Liu, Z. Rudnick, *Gaussian primes in almost all narrow sectors*, arXiv:1903.04005, §2.1 — exact untwisted Gaussian normalization `Xi_k=e^{i4k theta}`, entire continuation for `k!=0`, and completion `pi^{-(s+2|k|)} Gamma(s+2|k|)`.
3. J. Merikoski, *On Gaussian primes in sparse sets*, Compositio Math. 161 (2025), §2.7 — exact finite residue-twist family `L(s,xi_j chi)` for `chi` on `(Z[i]/uZ[i])^x`, and the nonzero-angular separation in the zero-free statement.

Aggarwal's treatment of positive-weight Hecke characters over imaginary quadratic fields is consistent with the same continuation/functional-equation plus Phragmen--Lindelof convexity mechanism, but the three items above are sufficient for the Stage13 contract.

## 9. Gate closure

```text
STAGE13_13FQ=COMPLETE_R07_FIXED_TWIST_HECKE_CONTRACT
R07_GATE_A=COMPLETE
R07_FIXED_TWIST_FAMILY_EXPLICIT=true
R07_FIXED_TWIST_AMBIENT_FAMILY=dual((Z[i]/u_S Z[i])^x)
R07_HLR_TO_MERIKOSKI_TRANSLATION=Xi_{2ell}=xi_{8ell}
R07_FIXED_TWIST_PRIMARY_CONTRACT_VERIFIED=true
R07_TWIST_CONDUCTOR_INDEPENDENT_OF_B=true
R07_TWIST_FINITE_CONDUCTOR_SET_FOR_FIXED_S=true
R07_TWIST_INFINITY_TYPE_NONZERO_FOR_ELL_GE_1=true
R07_TWIST_HOLOMORPHIC_AT_S1=true
R07_TWIST_GAMMA_SHIFT=4*ell
R07_COMMON_STRIP_GROWTH_EXPONENTS_EXIST=true
R07_COMMON_STRIP_GROWTH_UNIFORM_IN_ELL=true
R07_COMMON_STRIP_GROWTH_UNIFORM_OVER_FIXED_TWIST_FAMILY=true
R07_GROWING_MODULUS_THEOREM_USED=false
R07_ZERO_FREE_REGION_REQUIRED=false
R07_REPAIR_BLOCKERS_OPEN=2
R07_BLOCKER_B_CONCRETE_FIXED_S_RESIDUE_MODEL=true
R07_BLOCKER_C_CURVED_REGION_SELF_CONTAINED_CLOSURE=true
R06_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fr
```
