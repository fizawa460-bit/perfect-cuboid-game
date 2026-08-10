# Stage14-tH13 — sparse many-conductor quadratic large-sieve / dispersion adapter

## Purpose

Stage14-t45 certified, for fixed twist `tau` and fixed partner `y`, the genuine one-dimensional prime character

\[
\chi_{\ell_x}(\tau F_y)=\chi_{D_{\tau,y}}(\ell_x),
\qquad
D_{\tau,y}=\operatorname{funddisc}(\operatorname{sqf}(\tau F_y)).
\]

The obstruction is that `y` moves.  In each of the eight frozen top-heavy twists t45 sees exactly `544` distinct partner conductors, so the live object is

\[
\mathcal B_\tau=\sum_{x,y}a_xb_y\,\chi_{D_{\tau,y}}(\ell_x),
\]

with canonical-prime selector weights and all tH12/t44 routing retained.

This stage builds the reusable analytic adapter only.  It **does not** assume, import, or prove a t45 power saving.

---

## 1. Mandatory common refinement and exact selector preservation

Fix a tH12 common disjoint refinement block `R`, a twist `tau`, a dyadic canonical-prime scale

\[
L<\ell_x\le 2L,
\]

and, when needed, a dyadic nonprincipal conductor shell

\[
Q<|D_{\tau,y}|\le 2Q.
\]

All finite 2-adic / sign / reciprocity classes are also refined before applying a large sieve.  No estimate from an incompatible partition may be combined with this block.

Let `w_R(x)` be the **actual canonical-prime selector weight** inherited from the physical family.  It is absorbed into the coefficient, not discarded:

\[
A_\ell
 :=
 \sum_{\substack{x\in R\\ \ell_x=\ell}}
 a_x w_R(x).
\tag{H13.1}
\]

Likewise, after all partner-side block weights are included, collapse equal conductors exactly:

\[
B_D
 :=
 \sum_{\substack{y\in R\\D_{\tau,y}=D}}b_y v_R(y).
\tag{H13.2}
\]

Define

\[
E_\ell(R)=\sum_\ell |A_\ell|^2,
\qquad
E_D(R;Q)=\sum_{Q<|D|\le2Q}|B_D|^2,
\tag{H13.3}
\]

and support cardinalities

\[
P_R=\#\{\ell:A_\ell\ne0\},
\qquad
K_R(Q)=\#\{D:Q<|D|\le2Q,\ B_D\ne0\}.
\tag{H13.4}
\]

Thus the selector survives **exactly** in `A_ell`.  Large-sieve zero extension occurs only after this exact coefficient formation.

For unit positive partner weights, `E_D=sum_D m_D^2` is the same-modulus collision energy, not merely the number of distinct conductors.  Hence `544 distinct conductors` by itself is not an energy bound.

---

## 2. t44 routing: remove the large cross-bad canonical primes first

For fixed `tau`, t44 gives

\[
\mathcal S_\tau
 :=\{p>2\sqrt B:p\mid\tau\},
\qquad
|\mathcal S_\tau|\le16+o(1).
\tag{H13.5}
\]

If a distinct foreign canonical prime is cross-bad, t44 forces that prime into `tau`.  Therefore the many-conductor large-sieve block is defined only after routing

```text
same canonical prime                  -> exceptional same-ell slice
ell_x in S_tau                        -> t44 twist-supported bad-prime slice
generic distinct-prime cross-good     -> tH13 many-conductor adapter
```

For the routed bad-prime slice one has only the energy-safe estimate

\[
|\mathcal B_{\rm bad}|
\le
|\mathcal S_\tau|^{1/2}E_{\ell,{\rm bad}}^{1/2}
\,K_R^{1/2}E_D^{1/2},
\tag{H13.6}
\]

up to the inherited coefficient normalizations.  The `O(1)` number of exposed primes does **not** itself imply a power saving; a mass bound for those slices is still required.

---

## 3. Principal conductor is a separate slice

The principal conductor `D=1` must never be placed inside a nonprincipal large-sieve average.  After the exact collapse (H13.2),

\[
\boxed{
\mathcal B_{\rm pr}
 = B_1\sum_\ell A_\ell .
}
\tag{H13.7}
\]

There is no character cancellation in (H13.7).  Its admissible default bound is

\[
|\mathcal B_{\rm pr}|
\le |B_1|\,\|A\|_1,
\tag{H13.8}
\]

or a stronger bound supplied by an independent principal-slice theorem.  tH13 supplies no such theorem.

---

## 4. Rational quadratic large-sieve receiver

After the preceding routing, the generic nonprincipal shell is exactly

\[
\mathcal B_R(Q)
 =
 \sum_{Q<|D|\le2Q}B_D
 \sum_{L<\ell\le2L}A_\ell\chi_D(\ell),
\tag{H13.9}
\]

where the inner support consists of odd primes and therefore of squarefree integers.

Heath-Brown's quadratic large sieve, after splitting the finitely many fundamental-discriminant 2-adic classes, gives

\[
\sum_{Q<|D|\le2Q}^{\rm fund}
\left|\sum_{L<\ell\le2L}A_\ell\chi_D(\ell)\right|^2
\ll_\varepsilon
(LQ)^\varepsilon(L+Q)E_\ell(R).
\tag{H13.10}
\]

Cauchy in `D` therefore yields the primary reusable receiver

\[
\boxed{
|\mathcal B_R(Q)|
\ll_\varepsilon
(LQ)^\varepsilon
(L+Q)^{1/2}
E_\ell(R)^{1/2}E_D(R;Q)^{1/2}.
}
\tag{H13.11}
\]

This is the correct quadratic `L+Q` cost.  The ordinary all-character large sieve has a `Q^2+L` scale, but that is **not** the quadratic-character receiver used here.

### Conductor-energy form

Let

\[
\mathfrak W_D(R;L)
 :=
 \sum_{D\ne1}(L+|D|)|B_D|^2.
\tag{H13.12}
\]

Summing dyadic conductor shells and absorbing the logarithmic number of shells into `B^{o(1)}` gives

\[
\boxed{
|\mathcal B_R^{\rm np}|
\ll
B^{o(1)}E_\ell(R)^{1/2}
\mathfrak W_D(R;L)^{1/2}.
}
\tag{H13.13}
\]

This is a genuine improvement over using only `Q_max` whenever the **coefficient energy is concentrated at small conductors**.  Thus tH13 answers the conductor-energy question positively: max conductor is not the only reusable input.

The same statement may be retained shell-by-shell when that is sharper:

\[
|\mathcal B_R^{\rm np}|
\ll
B^{o(1)}E_\ell(R)^{1/2}
\sum_Q(L+Q)^{1/2}E_D(R;Q)^{1/2}.
\tag{H13.14}
\]

---

## 5. Sparse cardinality: what is and is not available

A purely finite-dimensional Hilbert-Schmidt bound gives

\[
\boxed{
|\mathcal B_R(Q)|
\le
(P_RK_R(Q))^{1/2}
E_\ell(R)^{1/2}E_D(R;Q)^{1/2}.
}
\tag{H13.15}
\]

Hence the unconditional same-block adapter may take

\[
\boxed{
|\mathcal B_R(Q)|
\ll B^{o(1)}E_\ell^{1/2}E_D(Q)^{1/2}
\min\!\left\{(L+Q)^{1/2},\ (P_RK_R(Q))^{1/2}\right\}.
}
\tag{H13.16}
\]

But (H13.15) contains **no character cancellation**.  It is only the matrix-dimension bound.

### Cardinality-only sparse large sieve is false in general

There is no universal replacement of the conductor range `Q` by the number `K` of distinct conductors without extra distribution information.

Take any finite set `P` of odd test primes and put

\[
M=8\prod_{p\in P}p.
\]

By Dirichlet's theorem choose arbitrarily many distinct primes

\[
q_j\equiv1\pmod M.
\]

Then each `D_j=q_j` is a positive fundamental discriminant and

\[
\chi_{D_j}(p)=1
\qquad(p\in P)
\]

for every `j`.  The resulting `K x P` character matrix is the all-ones matrix, whose squared operator norm is `KP`.  Therefore a hypothetical sparse quadratic large sieve with cost `K+P` (or any comparable cardinality-only substitute for the conductor scale) fails when `K,P` grow together.

**Failure boundary:** sparse conductor cardinality alone does not prevent arbitrarily coherent character rows.  Any improvement beyond (H13.16) must use conductor size, spacing/distribution, residue-class exclusion, product-kernel energy, or an equivalent correlation certificate.

The frozen t45 fact `K=544` is therefore useful census data but is not an asymptotic cancellation theorem.  Even treating `544=B^{o(1)}` would require a uniform theorem that t45 does not provide.

---

## 6. Reciprocity / duality

Canonical rational primes are split Gaussian primes, hence `ell ≡ 1 (mod 4)`.  After splitting the finite `D` 2-part and `ell mod 8` classes, quadratic reciprocity converts

\[
\chi_D(\ell)
\]

into the dual Jacobi/Kronecker symbol with `ell` as the character modulus, up to a fixed local sign on the refined block.

Consequences:

1. the tH13 matrix is genuinely dual in the `ell` and squarefree-conductor variables after finite local refinement;
2. one may Cauchy on either side and invoke the quadratic large sieve in the more convenient orientation;
3. duality does **not** turn sparse conductor cardinality into conductor range — it preserves the same `L+Q` barrier.

This is also why selector weights are harmless analytically once they have been formed exactly into `A_ell`: the quadratic large sieve accepts arbitrary complex coefficients.

---

## 7. Norm-induced Gaussian-Hecke comparison

For a primary Gaussian prime `varpi` above the canonical rational prime,

\[
N\varpi=\ell,
\qquad
\eta_D(\varpi):=\chi_D(N\varpi)=\chi_D(\ell).
\tag{H13.17}
\]

Goldmakher-Louvel's quadratic large sieve over number fields gives an `(M+N)(MN)^epsilon` receiver for a certified quadratic Hecke family of squarefree ideals.  Thus the tH12 norm-induced Hecke formulation remains a valid interface when the coefficient/selector genuinely depends on the Gaussian ideal or orientation.

For the t45 phase itself, however, (H13.17) depends only on the rational norm.  Collapsing to `ell` and using (H13.10) is the cleaner route and avoids any possible loss from measuring a base-changed character by an ideal conductor.  The Gaussian-Hecke theorem supplies **no automatic sparse-cardinality gain** over the rational receiver.

Comparison:

```text
rational quadratic LS       preferred for t45 norm-only phase; exact L+Q envelope
Gaussian-Hecke quadratic LS valid if ideal/orientation data must remain; no K-for-Q miracle
reciprocity / duality        changes orientation, not the conductor-range barrier
same-modulus dispersion      only route here that can exploit extra pair-correlation structure
```

---

## 8. Same-modulus collapse and dispersion receiver

The equal-conductor part must first be collapsed by (H13.2).  After Cauchy in the canonical-prime coefficients,

\[
|\mathcal B_R^{\rm np}|^2
\le
E_\ell(R)
\sum_{\ell\in\operatorname{supp}A}
\left|\sum_{D\ne1}B_D\chi_D(\ell)\right|^2.
\tag{H13.18}
\]

Expanding the square gives

\[
|\mathcal B_R^{\rm np}|^2
\le
E_\ell(R)
\left(
P_RE_D(R)+\Delta_R
\right),
\tag{H13.19}
\]

where the first term is the exact same-modulus diagonal and the off-diagonal is organized by the product squareclass

\[
\kappa(D,D')
=
\operatorname{funddisc}(\operatorname{sqf}(DD')).
\tag{H13.20}
\]

Define

\[
\Gamma_R(\kappa)
=
\sum_{\substack{D\ne D'\\\kappa(D,D')=\kappa}}
B_D\overline{B_{D'}},
\qquad
S_R(\kappa)
=
\sum_{\ell\in\operatorname{supp}A}\chi_\kappa(\ell).
\tag{H13.21}
\]

Then, on the cross-good coprime slice,

\[
\Delta_R
=
\sum_{\kappa\ne1}\Gamma_R(\kappa)S_R(\kappa).
\tag{H13.22}
\]

Equations (H13.19)-(H13.22) are the **same-modulus dispersion receiver**.  They expose exactly what t46 may try to improve:

- product-kernel support cardinality;
- product-kernel coefficient energy `sum_kappa |Gamma_R(kappa)|^2`;
- cancellation in the prime sums `S_R(kappa)`;
- or structural exclusion forcing many off-diagonal kernels away.

A second quadratic large sieve may be applied to the `kappa` family if its conductor/energy ledger is favorable, but this is not automatically an improvement: `kappa(D,D')` can have conductor on a product scale comparable to `Q^2`.

Therefore tH13 records (H13.22) as a conditional receiver, not a power-saving theorem.

---

## 9. Critical `sqrt(ell)` strip exponent ledger

Write the critical canonical-prime scale as

\[
L=B^{1/2+o(1)}.
\]

For one common-refinement / conductor shell let

\[
P_R=B^{p+o(1)},\quad
K_R(Q)=B^{k+o(1)},\quad
Q=B^{q+o(1)},
\]

and

\[
E_\ell(R)=B^{e_\ell+o(1)},
\qquad
E_D(R;Q)=B^{e_D+o(1)}.
\]

Then (H13.11) gives

\[
\boxed{
\operatorname{exp}_{\rm QLS}
=
\frac{e_\ell+e_D+\max(1/2,q)}{2}.
}
\tag{H13.23}
\]

The cardinality/Hilbert-Schmidt receiver gives

\[
\boxed{
\operatorname{exp}_{\rm HS}
=
\frac{e_\ell+e_D+p+k}{2}.
}
\tag{H13.24}
\]

Thus the reusable shell ledger is

\[
\boxed{
\operatorname{exp}_{\rm tH13}
=
\frac{e_\ell+e_D+
\min\{\max(1/2,q),\ p+k\}}{2}.
}
\tag{H13.25}
\]

For unit collapsed coefficients (`e_ell=p`, `e_D=k`), the raw pair-count exponent is `p+k`.  The possible QLS gain is

\[
\boxed{
\delta_{\rm QLS}
=
\max\left\{0,
\frac{p+k-\max(1/2,q)}{2}
\right\}.
}
\tag{H13.26}
\]

This immediately gives the critical failure boundary.  Even if one were allowed to treat the conductor family as genuinely sparse with `k=0` and the prime support fills the critical strip with `p=1/2`,

\[
\delta_{\rm QLS}
=
\max\{0,(1/2-\max(1/2,q))/2\}=0.
\tag{H13.27}
\]

So **sparse cardinality alone cannot produce a fixed power saving in the critical strip**.  A fixed saving requires at least one additional input:

```text
(A) conductor-energy compression below the max-Q envelope,
(B) a shell with p+k > max(1/2,q),
(C) product-kernel / same-modulus dispersion saving,
(D) extra cancellation in the canonical-prime selector sum,
(E) a structural theorem eliminating the high-conductor energy.
```

The crude predecessor bounds are intentionally not promoted to a sharp conductor theorem: t44 has `tau <= 2^16 B^8` and t40 has `|F_y| <= 256 B^4`, so a naive max-range estimate for `D_{tau,y}` can be as poor as `B^{12+o(1)}`.  This makes the max-conductor form of (H13.11) useless in the critical strip and is exactly why (H13.12)-(H13.14) and (H13.22) are retained.

No global Stage14 exponent is claimed from this local ledger because t46 still has to supply the block energies and the common-refinement aggregation ledger.

---

## 10. tH12 coefficient-energy aggregation contract

All tH13 estimates are **per common disjoint refinement block**.  To aggregate them:

1. form the exact physical coefficients first;
2. split principal / t44-bad / generic nonprincipal slices;
3. refine simultaneously by the tH12 common core, canonical-prime selector cell, finite reciprocity class, and dyadic conductor shell;
4. record `E_ell`, `E_D`, and any block replication factor in the tH12 coefficient-energy ledger;
5. take `min(QLS, HS, dispersion)` only inside the **same** refined block;
6. aggregate disjoint blocks by Cauchy/energy summation, never by multiplying local `O(1)` statements by an unrecorded number of blocks.

This preserves the tH12 quantifier guard exactly.

---

## 11. Frozen audit facts inherited from t45

The deterministic t45 census used by this adapter is

```text
states                                      560
common-core blocks                           37
canonical-prime blocks                       87
joint core/prime blocks                     530
generic distinct-prime cross-good pairs 305,334

top heavy tau: 91,209,286,34034,41,329,4641,11
for every one of those tau:
    distinct fixed-partner conductors        544
    max candidate-pairs sharing one D       1114
```

The `1114` multiplicity warning is precisely why same-modulus energy is kept separate from distinct-conductor cardinality.

---

## 12. Receiver handed to Stage14-t46

For every certified tH12 common-refinement block `R` and fixed `tau`, t46 may invoke:

### Generic nonprincipal shell theorem

\[
\boxed{
|\mathcal B_R(Q)|
\ll B^{o(1)}E_\ell(R)^{1/2}E_D(R;Q)^{1/2}
\min\{(L+Q)^{1/2},(P_RK_R(Q))^{1/2}\}.
}
\tag{H13.28}
\]

### Conductor-energy theorem

\[
\boxed{
|\mathcal B_R^{\rm np}|
\ll B^{o(1)}E_\ell(R)^{1/2}
\left(\sum_{D\ne1}(L+|D|)|B_D|^2\right)^{1/2}.
}
\tag{H13.29}
\]

### Same-modulus dispersion identity

\[
\boxed{
|\mathcal B_R^{\rm np}|^2
\le
E_\ell(R)
\left(P_RE_D(R)+
\sum_{\kappa\ne1}\Gamma_R(\kappa)S_R(\kappa)
\right),
}
\tag{H13.30}
\]

with absolute value inserted on the off-diagonal term when used as a one-sided bound.

### Separate receivers

```text
D=1 principal                 -> (H13.7)-(H13.8), no LS cancellation
t44 large cross-bad primes    -> (H13.5)-(H13.6), O(1) slices only
same-ell exceptional slice    -> outside this adapter
```

### What t46 must prove to get a new power saving

At least one of the following must be certified uniformly, not just on the frozen sample:

- favorable dyadic conductor-energy moment `W_D(R;L)`;
- conductor shell exponents satisfying the positive-gain condition in (H13.26);
- a product-kernel energy / correlation estimate improving (H13.30);
- a selector-sensitive prime-character cancellation theorem;
- or a separate power-saving estimate for principal / same-ell / t44-bad slices sufficient for global aggregation.

---

## 13. Locked boundary

```text
STAGE14_TH13=COMPLETE_SPARSE_MANY_CONDUCTOR_LARGE_SIEVE_DISPERSION_ADAPTER
T45_FIXED_PARTNER_CHARACTER_USED=true
T45_POWER_SAVING_ASSUMED=false
CANONICAL_PRIME_SELECTOR_WEIGHT_PRESERVED=true
TH12_COMMON_DISJOINT_REFINEMENT_REQUIRED=true
TH12_COEFFICIENT_ENERGY_LEDGER_REQUIRED=true
T44_LARGE_BAD_CANONICAL_PRIME_ROUTING_INCLUDED=true
PRINCIPAL_CONDUCTOR_SEPARATE=true
RATIONAL_QUADRATIC_LARGE_SIEVE_RECEIVER_PROVED=true
RECIPROCITY_DUAL_RECEIVER_PROVED=true
NORM_INDUCED_GAUSSIAN_HECKE_INTERFACE_RECORDED=true
SAME_MODULUS_DISPERSION_RECEIVER_PROVED=true
CONDUCTOR_ENERGY_REFINEMENT_AVAILABLE=true
SPARSE_CARDINALITY_REPLACES_CONDUCTOR_RANGE=false
SPARSE_CARDINALITY_COUNTERMODEL_RECORDED=true
CRITICAL_SQRT_ELL_EXPONENT_LEDGER_PROVED=true
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
GENERIC_CROSS_GOOD_GLOBAL_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t46 plug actual block/cardinality/conductor-energy/product-kernel ledgers into H13.28-H13.30 and test the positive-gain inequalities; do not infer saving from 544 alone
```

---

## References used by the adapter

- D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995), 235-275.  Quadratic large sieve in the `(M+N)(MN)^epsilon` form for odd squarefree variables.
- L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, Math. Proc. Cambridge Philos. Soc. 154 (2013), 193-212, Theorem 1.1.  Number-field quadratic Hecke-family analogue with the same `(M+N)(MN)^epsilon` shape.

These are analytic receivers only; neither reference supplies the missing Stage14-specific coefficient-energy or dispersion estimate.