# Stage13-13fm — fixed-S principal-pole sector and pole-loss closure

> STATUS: `R06_GATE_C_PRINCIPAL_POLE_SECTOR_CLOSURE`
>
> PURPOSE: replace the R05 §14 intensional principal-sector description by an explicit fixed-`S` character quotient, pole-signature map, residue-functional argument, tagged upper-bound injection, and nonprincipal pole-loss proof.
>
> INPUTS: merged `13-13fk` and `13-13fl`; the exact inert local mass from `13-13fg`; the zero-mode pure factorization from `13-13fh`; fixed-conductor Dirichlet/Gaussian-Hecke holomorphy from `13-13fl`.
>
> SCOPE: fixed finite sets of inert odd primes. No growing-modulus estimate is used.

Write

\[
D_q=\frac{\kappa I_q}{3\pi^3},\qquad
A_q(B)\sim D_qB(\log B)^3.
\]

We prove, for every fixed finite inert set `S`,

\[
\boxed{
A^{\rm tag}_{q,S}(B)
=2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)B(\log B)^3
+o_S(B(\log B)^3),
}
\]

where

\[
\lambda_p=\frac{p+5}{2(p+1)}.
\]

The proof below is deliberately formulated on the **actual constrained residue state space** rather than on a redundant tuple of auxiliary characters.

---

## 1. The unbounded pole-producing slots are explicit

At zero Gaussian angular mode, the pure odd-prime factorization used in Stage13 is

\[
A_0(s_h)=\zeta(s_h)L(s_h,\chi_4)E_{h,0}(s_h),
\]

and

\[
B_0(s_r)=\zeta(s_r)^2L(s_r,\chi_4)E_{r,0}(s_r),
\qquad
B_0(s_s)=\zeta(s_s)^2L(s_s,\chi_4)E_{s,0}(s_s).
\]

Thus the only unbounded principal-pole slots are the five displayed zeta copies

\[
\boxed{
\mathscr P=\{H,R_1,R_2,S_1,S_2\}.
}
\]

Here `H` is the zeta factor in the `h` channel, `R_1,R_2` are the two zeta copies in the `r` base channel, and `S_1,S_2` are the two zeta copies in the `s` base channel. The factors `L(s,chi_4)`, the finite 2-adic factors, inert residual factors, and the split-prime mixed Wiener correction are holomorphic at the principal point and are **not** pole-producing slots.

This is the exact meaning of “channel” in the R06 overlap proof.

---

## 2. Actual constrained local state space and removal of auxiliary aliasing

Fix a finite inert set

\[
S=\{p_1,\ldots,p_k\}.
\]

At each `p in S`, first fix one of the admissible valuation strata

```text
U, R_b, S_c.
```

After that valuation choice, all remaining local information used by the square test is unit residue information modulo `p`. Let `G_{p,nu}` be any convenient ambient product of unit groups used to parameterize those residues, and let

\[
H_{p,\nu}\subseteq G_{p,\nu}
\]

be the **actual image** of admissible residues satisfying all algebraic relations inherited from

\[
x^2+y^2=P^2,\qquad P^2+z^2=d^2.
\]

Only the restriction of a character to `H_{p,nu}` has mathematical meaning. Consequently two ambient auxiliary characters which agree on `H_{p,nu}` are identified. Equivalently,

\[
\widehat H_{p,\nu}
\cong
\widehat G_{p,\nu}/H_{p,\nu}^{\perp},
\]

where

\[
H_{p,\nu}^{\perp}
=\{\chi\in\widehat G_{p,\nu}:\chi|_{H_{p,\nu}}=1\}.
\]

This quotient is the precise treatment of the “auxiliary-character aliasing” noted by the R05 reviewers: characters differing only by an algebraic relation are the **same Fourier character** before any analytic pole classification is made.

For fixed `S` and valuation profile `nu=(nu_p)_{p in S}`, CRT gives the actual constrained residue group

\[
H_{S,\nu}=\prod_{p\in S}H_{p,\nu}
\]

and a finite Fourier expansion of the accepted-state indicator

\[
W_{S,\nu}
=\sum_{\chi\in\widehat H_{S,\nu}}
\widehat W_{S,\nu}(\chi)\chi.
\]

There is therefore no unresolved redundancy in the character index set.

---

## 3. Pole-signature map and explicit principal sector

Every character `chi in widehat H_{S,nu}` pulls back through the multiplicative coefficient maps to fixed-conductor characters on the five pole slots. Define the pole-signature homomorphism

\[
\boxed{
\rho_{S,\nu}:\widehat H_{S,\nu}
\longrightarrow
\widehat{\mathscr U}_H\times
\widehat{\mathscr U}_{R_1}\times
\widehat{\mathscr U}_{R_2}\times
\widehat{\mathscr U}_{S_1}\times
\widehat{\mathscr U}_{S_2}
}
\]

by

\[
\rho_{S,\nu}(\chi)
=(\chi_H,\chi_{R_1},\chi_{R_2},\chi_{S_1},\chi_{S_2}),
\]

where each component is the induced Dirichlet or Gaussian/ray-class character multiplying the corresponding pure zeta slot.

The **principal pole sector** is now the concrete kernel

\[
\boxed{
\mathcal K_{S,\nu}:=\ker\rho_{S,\nu}.
}
\]

Thus `chi` lies in the principal sector if and only if all five displayed induced characters are principal. A character may be nontrivial on an auxiliary mixed coordinate and still belong to `K_{S,nu}`; that is not an exception or an aliasing problem. It simply means the character acts only inside the holomorphic mixed factor.

This kernel definition is external: the five factor slots are listed explicitly, the ambient redundancy has already been quotiented out, and membership is decided by the five induced characters.

---

## 4. Why the complete principal sector reproduces the exact local multiplier

For fixed `S`, define `Res_S(F)` to be the coefficient of the **full raw principal polar term** in the zero-mode asymptotic after inserting a finite residue function `F` on the actual constrained local state space, while retaining the same archimedean chamber and 2-adic branch.

This is a linear functional of `F` because finite residue insertion is linear before Perron inversion.

For one Fourier character `chi`:

- if `rho_{S,nu}(chi)` is nontrivial in at least one pole slot, the corresponding full principal residue is zero because at least one zeta pole is replaced by a holomorphic fixed-conductor `L`-factor;
- if `chi in K_{S,nu}`, all five raw pole slots survive, and its holomorphic coefficient contributes to `Res_S`.

Therefore

\[
Res_S(W_{S,\nu})
=\sum_{\chi\in\mathcal K_{S,\nu}}
\widehat W_{S,\nu}(\chi)Res_S(\chi).
\]

So the sum over the **entire** kernel, not one raw auxiliary tuple, is exactly the principal leading coefficient.

Now evaluate the same linear functional directly in physical local variables. For each inert `p`, the unrestricted zero-mode local mass is

\[
L_{p,0}=\frac{p+1}{p-1},
\]

while the accepted tagged mass is

\[
L^W_{p,0}=\frac{p+5}{2(p-1)}.
\]

Hence

\[
\frac{L^W_{p,0}}{L_{p,0}}
=\lambda_p
=\frac{p+5}{2(p+1)}.
\]

Because the primes in `S` are fixed and CRT makes the local insertion a tensor product, direct local evaluation gives

\[
\boxed{
\frac{Res_S(W_S)}{Res_S(1)}
=\prod_{p\in S}\lambda_p.
}
\]

Combining the two evaluations of the **same linear residue functional** proves that the complete principal sector, including every harmless alias or mixed-coordinate character in its kernel, reproduces exactly

\[
\boxed{\prod_{p\in S}\lambda_p}.
\]

No independence of redundant auxiliary coordinates is assumed.

---

## 5. The tagged factor `2` is an exact ambient multiplicity and cannot undercount

Fix a canonical raw incidence counted by `A_q(B)`. The distinguished face `q` has exactly two edge legs. Form the tagged ambient set

\[
\mathcal T_q(B)
=\{(X,t):X\text{ is a raw }q\text{-incidence},\ t\text{ is one of its two face legs}\}.
\]

Therefore, as a finite identity,

\[
\boxed{|\mathcal T_q(B)|=2A_q(B).}
\]

Now fix another face `r != q`. The faces `q` and `r` share **exactly one** edge. If a canonical object is counted by `O_{qr}(B)`, choose on its distinguished `q` incidence the tag equal to that shared edge. The second integral face then says exactly that the tagged square condition

\[
x_t^2+z^2=w^2
\]

holds over the integers, hence it passes every modular test `W_p` for every `p in S`.

The map

\[
X\in O_{qr}(B)
\longmapsto
(X,\text{the unique }q\cap r\text{ edge})
\]

is injective into the accepted tagged set. This remains true for triple-face objects: for a fixed ordered pair `(q,r)` there is still one unique shared edge.

Consequently, for every finite `B` and every fixed `S`,

\[
\boxed{O_{qr}(B)\le A^{\rm tag}_{q,S}(B).}
\]

The factor `2` is therefore not an informal “safe multiplicity”: it is the exact cardinality ratio between the unconstrained tagged ambient set and the raw `q`-incidence set. It can overcount accepted tags, but it cannot undercount a true pair overlap.

---

## 6. Every sector outside the kernel loses at least one pole after all aliasing

Take

\[
\chi\in\widehat H_{S,\nu}\setminus\mathcal K_{S,\nu}.
\]

Since `K_{S,nu}=ker rho_{S,nu}`, at least one explicitly listed component among

\[
\chi_H,\chi_{R_1},\chi_{R_2},\chi_{S_1},\chi_{S_2}
\]

is nonprincipal. There is no remaining auxiliary cancellation to consider: ambient characters which agree on the algebraically constrained state space were already identified in `widehat H_{S,nu}`, and the signature is computed **after** that quotient.

At the corresponding pure factor slot, a principal zeta factor is replaced by a fixed-conductor nonprincipal Dirichlet or nonzero-infinity-type Gaussian/ray-class Hecke `L`-factor. By `13-13fl`, it is holomorphic at `s=1` and has the fixed-strip polynomial growth needed for Riesz/Perron.

The split-prime mixed correction is absolutely convergent in the weighted Wiener algebra on the fixed half-plane. Twisting coefficients by unit-modulus fixed characters does not enlarge its majorant. Hence the mixed correction is holomorphic and cannot create or restore a pole.

Thus the total polar order is lower by at least one slot. Applying the same finite-order Riesz/Perron, curved-region, boundary, and harmonic estimates gives, for each fixed character tuple,

\[
O_S(B(\log B)^2)
=o(B(\log B)^3).
\]

For fixed `S`, there are only finitely many valuation profiles and finitely many characters. Therefore all sectors outside the kernel contribute

\[
\boxed{o_S(B(\log B)^3).}
\]

with no uniformity in `S` asserted.

---

## 7. Fixed-S asymptotic and overlap squeeze

The unconstrained tagged population has leading coefficient `2D_q`. Section 4 multiplies its principal coefficient by the exact fixed-local ratio, and Section 6 makes every nonprincipal sector lower order. Hence

\[
\boxed{
A^{\rm tag}_{q,S}(B)
=2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)B(\log B)^3
+o_S(B(\log B)^3).
}
\]

For inert `p>=7`,

\[
\lambda_p\le\frac34.
\]

Choose `k` distinct inert primes `p_i>=7`, fix

\[
S_k=\{p_1,\ldots,p_k\},
\]

and first let `B->infinity`. The finite tagged injection gives

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q\prod_{p\in S_k}\lambda_p
\le2D_q(3/4)^k.
\]

Only then let `k->infinity`. Therefore

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}.
\]

Since `T(B)` is contained in every pair overlap,

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

The quantifier order remains

```text
fix S -> B -> infinity -> enlarge S.
```

No growing-modulus theorem and no perfect-cuboid nonexistence assumption are used.

---

## 8. R06 Gate C closure

The DeepSeek §14 objections are closed at proof-facing level by four explicit mechanisms:

1. **channels:** `P={H,R1,R2,S1,S2}` is the displayed set of pure principal zeta slots;
2. **aliasing:** ambient character redundancy is quotiented by `H^perp` before pole classification;
3. **principal coefficient:** the full kernel contribution equals the direct local residue functional, whose ratio is `prod lambda_p`;
4. **lower order:** outside the kernel, the explicit pole-signature map has a nonprincipal component, and the holomorphic mixed correction cannot restore the lost pole.

The finite tagged injection separately proves that the factor `2` cannot undercount the true overlap set.

```text
STAGE13_13FM=COMPLETE_FIXED_S_PRINCIPAL_POLE_SECTOR_CLOSURE
R06_GATE_C=COMPLETE
POLE_CHANNELS=H,R1,R2,S1,S2
ACTUAL_CONSTRAINED_CHARACTER_GROUP_USED=true
AUXILIARY_CHARACTER_ALIASING_QUOTIENTED_BEFORE_POLE_CLASSIFICATION=true
PRINCIPAL_POLE_SECTOR=KER_POLE_SIGNATURE_MAP
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
