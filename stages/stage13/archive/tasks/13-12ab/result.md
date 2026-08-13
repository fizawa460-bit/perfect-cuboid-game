# Stage13-12ab — fixed-local overlap repair

> STATUS: `STAGE13_12AB_COMPLETE_FIXED_LOCAL_OVERLAP_REPAIR`
>
> PREVIOUS: Stage13-12aa restored the raw directional theorem non-circularly.
>
> REVIEW TARGET: Claude R01 MAJOR on the old fixed-modulus overlap transfer.
>
> GLOBAL REVIEW STATE: `PENDING_EXTERNAL_R02`

The old Stage13-7jf fixed-prime idea is retained, but its missing global step is replaced here by an explicit finite-local-factor lemma inside the Stage13-12aa `j=0` Euler-product framework.

## 1. Tagged pair-overlap test

For one tagged raw incidence write

\[
x^2+y^2=P^2,\qquad P^2+z^2=d^2.
\]

If a second integral face shares the tagged leg `x`, then

\[
x^2+z^2=w^2.
\]

Hence for every odd prime `p`, `x^2+z^2` is a quadratic residue or zero modulo `p`.

For inert primes `p=3 mod 4`, define

\[
W_p=1_{x^2+z^2\in QR_0(F_p)}.
\]

A genuine pair-overlap point passes every chosen `W_p`. Each canonical raw incidence has two tags; for a fixed pair type choose the tag on its shared edge. Thus the pair overlap injects into a tagged raw population satisfying the chosen local tests.

## 2. Fixed-local-factor lemma

Stage13-12aa gives, after OE/EE splitting and Gaussian angular Fourier decomposition, a three-variable Euler product

\[
\mathcal D_\ell(\mathbf s)=\prod_l L_{l,\ell}(\mathbf s),
\qquad \mathbf s=(s_h,s_r,s_s).
\]

At one fixed prime `p`, refine the local state by adjoining the finitely many unit residues modulo `p` needed to recover `(x,y,P,z,d) mod p`. This is only a finite refinement of the existing valuation state. By CRT, states at distinct primes remain tensor factors.

For a bounded local weight `W_p`, replace

\[
L_{p,\ell}(\mathbf s)
\quad\hbox{by}\quad
L^W_{p,\ell}(\mathbf s).
\]

For a fixed finite set `S`, the constrained series is identically

\[
\boxed{
\mathcal D_{\ell,S}(\mathbf s)
=\mathcal D_\ell(\mathbf s)
\prod_{p\in S}\frac{L^W_{p,\ell}(\mathbf s)}{L_{p,\ell}(\mathbf s)}.
}
\]

Because `S` is fixed before `B -> infinity`, this changes only finitely many local factors. Therefore:

- zero-mode zeta pole orders are unchanged;
- the Stage13-12aa weighted-l1 mixed correction remains valid;
- the real curved region and category kernel `J_q` are unchanged;
- nonzero Gaussian harmonics acquire only a bounded finite Euler-factor multiplier and no new zeta pole;
- the Selberg/Vaaler plus polylog-uniform Hecke remainder remains lower order, with constants allowed to depend on fixed `S`.

Let

\[
\lambda_p=\frac{L^W_{p,0}(1,1,1)}{L_{p,0}(1,1,1)}.
\]

Then the tagged constrained raw count satisfies

\[
\boxed{
A^{tag}_{q,S}(B)
\sim 2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)B(\log B)^3,
}
\]

where the factor 2 is the two-tag lift and

\[
D_q=\frac{\kappa I_q}{3\pi^3}
\]

is the non-circular Stage13-12aa constant. The factor `lambda_p` is category-independent: the category enters only through the real zero-mode kernel, whereas `W_p` is purely local on the tagged oriented variables.

This is the fixed-modulus transfer that was not written out in Stage13-7jf.

## 3. Inert-prime acceptance is bounded away from one

On the unit-hypotenuse stratum `P in Z_p^*`, normalize `P=1`. For `p=3 mod 4`,

\[
x^2+y^2=1
\]

has `p+1` points and

\[
d^2-z^2=1
\]

has `p-1` points. Thus the unrestricted normalized count is `p^2-1`.

The quadratic-character calculation checked independently by the audit gives the exact accepted count

\[
\frac{(p+1)^2}{2}.
\]

Therefore the unit-stratum acceptance is

\[
\boxed{
\lambda_p^\times=\frac{p+1}{2(p-1)}
=\frac12+\frac1{p-1}.
}
\]

The full local factor also contains states with `p|P`. For inert `p`, the equation `x^2+y^2=P^2` forces `p|x,y`; primitivity then forces `z` to be a unit. In the explicit 12aa local coefficient system these are positive-valuation terms. The coefficients have a fixed-degree divisor majorant and every such term contains at least one factor `p^{-1}` at `(1,1,1)`. Hence, with one absolute constant `C0`,

\[
\frac{\text{positive-valuation local mass}}{L_{p,0}(1,1,1)}
\le \frac{C_0}{p}.
\]

Using the trivial acceptance bound 1 on that tail,

\[
\boxed{
\lambda_p\le \frac12+\frac1{p-1}+\frac{C_0}{p}
=\frac12+O(1/p),
}
\]

with an absolute implied constant. Thus there is an absolute `p0` such that every inert prime `p>p0` satisfies

\[
\boxed{\lambda_p\le 3/4.}
\]

Dirichlet's theorem supplies infinitely many primes `3 mod 4` above `p0`.

As a stronger finite-field diagnostic, the complete primitive affine mod-p ratio is

\[
\frac{p^2+2p+5}{2(p^2+1)},
\]

which is `<2/3` for inert primes `p>=11`. This finite-field identity is diagnostic; the theorem uses the explicit positive-valuation tail estimate above.

## 4. Order-of-limits squeeze

Fix `k`. Choose distinct inert primes

\[
S_k=\{p_1,\ldots,p_k\},\qquad p_i>p0,
\]

and hold `S_k` fixed. For every pair overlap `O_qr(B)`,

\[
O_{qr}(B)\le A^{tag}_{q,S_k}(B).
\]

Therefore

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le 2D_q\prod_{p\in S_k}\lambda_p
\le 2D_q(3/4)^k.
\]

Now let `k -> infinity` only after the `B -> infinity` limsup. Hence

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}
\]

for all three pair overlaps. No modulus depending on `B` occurs anywhere.

The triple overlap `T(B)` is a subset of every pair overlap, so

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

No perfect-cuboid nonexistence assumption is used.

## 5. Exactly-one theorem restored

The exact identities are

\[
N_{ab}=A_{ab}-O_{ab,ac}-O_{ab,bc}+T,
\]

and cyclically. Stage13-12aa gives

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

The pair/triple terms are now lower order, therefore

\[
\boxed{
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3
}
\]

and

\[
\boxed{N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.}
\]

The normalized limit is restored:

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

## 6. Supersession and review state

The old Stage13-7jf files remain provenance, but the sentence “fixed congruence restrictions are handled by the same machinery” is no longer an active proof step. The active chain is

```text
13-12aa explicit j=0 Euler-factor framework
  -> 13-12ab finite local-state refinement
  -> finite Euler-factor replacement
  -> lambda_p <= 1/2 + O(1/p)
  -> fixed-S squeeze
  -> pair/triple lower order
  -> exact-one transfer
```

Status:

```text
CLAUDE_FATAL_DIRECTION_NEUTRALITY=REPAIRED_BY_13_12AA
CLAUDE_MAJOR_FIXED_MODULUS_TRANSFER=REPAIRED_BY_13_12AB
RAW_DIRECTIONAL_ASYMPTOTIC=RESTORED
PAIR_OVERLAP_LOWER_ORDER=RESTORED
TRIPLE_OVERLAP_LOWER_ORDER=RESTORED
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=RESTORED
STAGE13_REPAIR_CHAIN=COMPLETE
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
NEXT=regenerate Stage13-only review bundle and request fresh R02 review
```

Stage13 is not self-declared externally CLOSED here; the repaired bundle should be reviewed again independently.