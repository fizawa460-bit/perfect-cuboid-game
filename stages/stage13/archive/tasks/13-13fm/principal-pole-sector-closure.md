# Stage13-13fm — fixed-S principal-pole sector and pole-loss closure

> STATUS: `R06_GATE_C_PRINCIPAL_POLE_SECTOR_CLOSURE`
>
> PURPOSE: replace the R05 §14 intensional principal-sector description by an explicit fixed-`S` effective-character quotient, reduced pole-signature map, residue-functional argument, tagged upper-bound injection, and nonprincipal pole-loss proof.
>
> SCOPE: fixed finite sets of inert odd primes. No growing-modulus estimate is used.

Write

\[
D_q=\frac{\kappa I_q}{3\pi^3},\qquad
A_q(B)\sim D_qB(\log B)^3.
\]

For every fixed finite inert set `S` we prove

\[
\boxed{A^{\rm tag}_{q,S}(B)=2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)B(\log B)^3+o_S(B(\log B)^3)}
\]

with

\[
\lambda_p=\frac{p+5}{2(p+1)}.
\]

## 1. Explicit pole-producing slots

At zero Gaussian angular mode the pure odd-prime factors are

\[
A_0(s_h)=\zeta(s_h)L(s_h,\chi_4)E_{h,0}(s_h),
\]

\[
B_0(s_r)=\zeta(s_r)^2L(s_r,\chi_4)E_{r,0}(s_r),\qquad
B_0(s_s)=\zeta(s_s)^2L(s_s,\chi_4)E_{s,0}(s_s).
\]

Hence the unbounded principal-pole slots are exactly

\[
\boxed{\mathscr P=\{H,R_1,R_2,S_1,S_2\}.}
\]

`H` is the zeta factor in the `h` channel; `R_1,R_2` are the two zeta copies in the `r` channel; `S_1,S_2` are the two zeta copies in the `s` channel. `L(s,chi_4)`, finite 2-adic factors, inert residual factors and the mixed Wiener correction are holomorphic at the principal point and are not pole slots.

## 2. Actual constrained residue set and effective characters

Fix `p in S` and one admissible valuation stratum `U`, `R_b` or `S_c`. After the valuation choice, the square test depends on finitely many unit residues. Let `G_{p,nu}` be a finite abelian ambient product of unit groups used to encode them, and let

\[
\Omega_{p,\nu}\subseteq G_{p,\nu}
\]

be the actual finite set of admissible residue tuples satisfying the algebraic relations inherited from

\[
x^2+y^2=P^2,\qquad P^2+z^2=d^2.
\]

No group structure is asserted for `Omega_{p,nu}`.

Extend the accepted-state function by zero from `Omega_{p,nu}` to `G_{p,nu}` and Fourier-expand it in the ordinary character basis of the finite abelian group `G_{p,nu}`. Distinct ambient characters can agree on every point of `Omega_{p,nu}`. Put

\[
N_{p,\nu}:=\{\chi\in\widehat G_{p,\nu}:\chi(\omega)=1\text{ for every }\omega\in\Omega_{p,\nu}\}.
\]

`N_{p,nu}` is a subgroup of `widehat G_{p,nu}`. Two ambient characters act identically on the actual state set exactly when their quotient lies in `N_{p,nu}`. Define the effective character classes by

\[
\boxed{\mathscr X_{p,\nu}:=\widehat G_{p,\nu}/N_{p,\nu}.}
\]

Fourier coefficients of equivalent ambient characters are aggregated classwise. Thus algebraic aliasing is removed before pole classification; no independence of redundant auxiliary coordinates is assumed.

For fixed `S` and valuation profile `nu=(nu_p)`, CRT gives the product ambient group and product constrained set. The simultaneous square-test indicator has an exact finite character expansion, aggregated over

\[
\mathscr X_{S,\nu}=\prod_{p\in S}\mathscr X_{p,\nu}.
\]

All sums are finite because `S` is fixed before `B->infinity`.

## 3. Reduced pole-signature map

Each effective class `[chi] in X_{S,nu}` determines one multiplicative weight on the actual coefficient support. Pull that weight through the exact pure-factor decomposition and cancel any redundant auxiliary representation before classifying poles. The five induced fixed-conductor characters define

\[
\boxed{\rho_{S,\nu}([\chi])=(\chi_H,\chi_{R_1},\chi_{R_2},\chi_{S_1},\chi_{S_2}).}
\]

The map is well-defined on effective classes: representatives with the same action on every admissible residue state give the same weighted coefficient system, hence the same reduced pure-factor Dirichlet series.

Define

\[
\boxed{\mathcal K_{S,\nu}:=\ker\rho_{S,\nu}.}
\]

This is the principal pole sector. Membership means precisely that all five displayed induced pole-slot characters are principal. A class may remain nontrivial on a holomorphic mixed coordinate and still lie in `K_{S,nu}`; it is then correctly retained in the principal sector.

## 4. Principal-sector coefficient equals the local mean

For fixed `S`, let `Res_S(F)` denote the coefficient of the established zero-mode principal term `B(log B)^3` after inserting a finite residue function `F`, with the same real chamber and 2-adic branch. This is linear in `F`.

For an effective Fourier class `[chi]`, if `rho([chi])` is nonprincipal in at least one pole slot, its full principal residue is zero because a principal zeta slot is replaced by a fixed-conductor holomorphic `L`-factor. Therefore

\[
Res_S(W_{S,\nu})
=\sum_{[\chi]\in\mathcal K_{S,\nu}}\widehat W_{S,\nu}([\chi])Res_S([\chi]).
\]

So the complete kernel contribution, not one raw auxiliary tuple, is exactly the principal leading coefficient.

Evaluate the same linear functional directly in physical local variables. For one inert prime,

\[
L_{p,0}=\frac{p+1}{p-1},\qquad
L^W_{p,0}=\frac{p+5}{2(p-1)},
\]

hence

\[
\frac{L^W_{p,0}}{L_{p,0}}=\lambda_p=\frac{p+5}{2(p+1)}.
\]

CRT makes the fixed local insertion a tensor product, so

\[
\boxed{\frac{Res_S(W_S)}{Res_S(1)}=\prod_{p\in S}\lambda_p.}
\]

The two evaluations of the same principal-residue functional prove that the **entire** principal sector reproduces exactly `product_{p in S} lambda_p`, including every harmless auxiliary alias.

## 5. Tagged factor two cannot undercount

For a raw canonical `q`-incidence `X`, tag either of the two edge legs of the distinguished face. The ambient tagged set is

\[
\mathcal T_q(B)=\{(X,t):X\in A_q(B),\ t\text{ is one of the two }q\text{-face legs}\}.
\]

Thus, as an exact finite identity,

\[
\boxed{|\mathcal T_q(B)|=2A_q(B).}
\]

Fix `r != q`. The two faces `q` and `r` share exactly one edge. Every object in `O_{qr}(B)` is sent to the tagged `q`-incidence whose tag is that unique shared edge. The second integral face gives the integer square condition for that tag, so it passes every local test `W_p`. This map is injective. Triple-face objects cause no ambiguity: for a fixed ordered pair `(q,r)` there is still exactly one shared edge.

Hence for every finite `B` and fixed `S`,

\[
\boxed{O_{qr}(B)\le A^{\rm tag}_{q,S}(B).}
\]

The factor `2` is therefore the exact unconstrained tagged multiplicity. It may overcount accepted tags, but it cannot undercount a true pair overlap.

## 6. Outside the kernel, at least one pole is genuinely lost

Take `[chi] notin K_{S,nu}`. By definition of the reduced signature, at least one of

\[
\chi_H,\chi_{R_1},\chi_{R_2},\chi_{S_1},\chi_{S_2}
\]

is nonprincipal. Equality on the algebraically constrained state set has already been quotiented out, so there is no remaining auxiliary-character cancellation to invoke.

At that pole slot, the principal zeta factor is replaced by a fixed-conductor nonprincipal Dirichlet or nonzero-infinity-type Gaussian/ray-class Hecke `L`-factor. By `13-13fl` it is holomorphic at `s=1` with the fixed-strip polynomial growth required by the Riesz/Perron step.

The split-prime mixed correction remains absolutely convergent in the same weighted Wiener algebra after fixed unit-modulus twists. It is holomorphic and cannot restore a lost pole.

Relative to the established `B(log B)^3` zero-mode residue polynomial, at least one pole slot is lost, so the log degree drops by at least one. The same finite-order Riesz/Perron, curved-region, boundary and harmonic estimates therefore give

\[
O_S(B(\log B)^2)=o(B(\log B)^3)
\]

for each fixed effective class. There are only finitely many classes and valuation profiles for fixed `S`, hence

\[
\boxed{\text{all nonprincipal sectors}=o_S(B(\log B)^3).}
\]

## 7. Fixed-S asymptotic and squeeze

The unconstrained tagged population has leading coefficient `2D_q`. Sections 4 and 6 give

\[
\boxed{A^{\rm tag}_{q,S}(B)=2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)B(\log B)^3+o_S(B(\log B)^3).}
\]

For inert `p>=7`, `lambda_p<=3/4`. Choose `k` distinct inert primes `p_i>=7`, fix `S_k`, then let `B->infinity`:

\[
\limsup_{B\to\infty}\frac{O_{qr}(B)}{B(\log B)^3}
\le2D_q\prod_{p\in S_k}\lambda_p
\le2D_q(3/4)^k.
\]

Only after that limit let `k->infinity`. Therefore

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)},\qquad
\boxed{T(B)=o(B(\log B)^3)}.
\]

The order of limits is

```text
fix S -> B -> infinity -> enlarge S.
```

No growing-modulus theorem and no perfect-cuboid nonexistence assumption are used.

## 8. Gate C locks

```text
STAGE13_13FM=COMPLETE_FIXED_S_PRINCIPAL_POLE_SECTOR_CLOSURE
R06_GATE_C=COMPLETE
POLE_CHANNELS=H,R1,R2,S1,S2
ACTUAL_CONSTRAINED_RESIDUE_SET_USED=true
AUXILIARY_CHARACTER_ALIASING_QUOTIENTED_BEFORE_POLE_CLASSIFICATION=true
PRINCIPAL_POLE_SECTOR=KER_REDUCED_POLE_SIGNATURE_MAP
PRINCIPAL_SECTOR_RESIDUE_FUNCTIONAL_PROOF_COMPLETE=true
PRINCIPAL_POLE_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p
TAGGED_AMBIENT_CARDINALITY=2*A_q(B)
TAGGED_FACTOR_TWO_UPPER_BOUND_PROVED=true
NONPRINCIPAL_POLE_LOSS_PROVED=true
MIXED_CORRECTION_CANNOT_RESTORE_POLE=true
NONPRINCIPAL_TOTAL=o_S(B(log B)^3)
LIMIT_ORDER=FIX_S_THEN_B_TO_INFINITY_THEN_ENLARGE_S
GROWING_MODULUS_THEOREM_USED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fn
```
