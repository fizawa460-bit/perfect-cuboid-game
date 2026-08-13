# Stage13-13fg — fixed inert-prime transfer and overlap squeeze

> STATUS: `STAGE13_13FG_FIXED_INERT_TRANSFER_LEMMA`
>
> PURPOSE: close R05 Gate G by replacing the compressed fixed-prime overlap paragraph with a proof-facing finite-character transfer, exact inert multiplier, principal-pole-sector decomposition, and explicit order-of-limits squeeze.
>
> INPUTS: Gates A–F; exact inert local states from 13-12ae/13-12ag; fixed-conductor Dirichlet/Gaussian-Hecke contracts from 13-13ff.
>
> SCOPE: pair/triple overlap only. No effective growing-modulus estimate is claimed.

Write

\[
D_q:=\frac{\kappa I_q}{3\pi^3},
\qquad
A_q(B)\sim D_qB(\log B)^3.
\]

For a pair overlap `O_{qr}(B)`, tag one of the two legs of the distinguished `q` face. If the tag is the shared edge with the second integral face, then the tagged square test below holds. We retain the two tags only as a safe upper multiplicity, so the unconstrained tagged population has leading constant `2D_q`.

For every fixed finite inert-prime set `S` we prove

\[
\boxed{
A^{\rm tag}_{q,S}(B)
=
2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)
B(\log B)^3
+o_S(B(\log B)^3),
}
\]

with

\[
\boxed{\lambda_p=\frac{p+5}{2(p+1)}}.
\]

No uniformity in `S` is used.

---

## 1. Tagged local test

For one tagged raw incidence write

\[
x^2+y^2=P^2,
\qquad
P^2+z^2=d^2.
\]

If the tagged leg `x` is shared by a second integral face, then

\[
x^2+z^2=w^2.
\]

For inert `p\equiv3 (mod 4)`, define

\[
W_p=1_{\{x^2+z^2\in QR_0(\mathbf F_p)\}}.
\]

Every genuine tagged pair overlap passes every chosen `W_p`. The local calculation is symmetric under exchange of the two face legs, so the same multiplier applies to either tag and every canonical direction.

---

## 2. Exact inert valuation states

Use

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\qquad(r,s)=1.
\]

At inert `p`, put `a=v_p(h)`, `b=v_p(r)`, `c=v_p(s)`. Primitivity forces `a=0`: if `p|h`, then `p|P,z`, and inertness in `x^2+y^2=P^2` forces `p|x,y`, contradicting primitive gcd one. Also `(r,s)=1` gives `min(b,c)=0`.

Hence the only allowed states are

```text
U    : (0,0,0)
R_b  : (0,b,0), b>=1
S_c  : (0,0,c), c>=1.
```

The unrestricted inert zero-mode local series is

\[
L_{p,0}(Y,Z)
=1+\sum_{b\ge1}Y^b+\sum_{c\ge1}Z^c
=\frac{1-YZ}{(1-Y)(1-Z)}.
\]

At `Y=Z=p^{-1}`,

\[
L_{p,0}=\frac{p+1}{p-1},
\qquad
\text{positive-valuation mass}=\frac{2}{p-1},
\]

so the positive-valuation fraction is exactly

\[
\frac{2}{p+1}.
\]

Every positive-valuation state passes `W_p` automatically: `p|P` forces `x\equiv y\equiv0`, while primitivity forces `z` to be a unit, hence `x^2+z^2\equiv z^2`.

---

## 3. Unit-state acceptance and exact lambda

On the unit state normalize `P=1`:

\[
X^2+Y^2=1,
\qquad
D^2-Z^2=1.
\]

For inert `p`, the two curves have `p+1` and `p-1` points, hence `T=p^2-1` pairs. The symbolic quadratic-character calculation of 13-12ag gives signed sum `S=2(p-1)`, while exactly four unit states have `X^2+Z^2=0`. Therefore

\[
N_{\rm acc}=\frac{T+S+4}{2}=\frac{(p+1)^2}{2}.
\]

Thus

\[
\boxed{\alpha_p=\frac{p+1}{2(p-1)}}.
\]

Adding the automatic positive-valuation mass,

\[
L^W_{p,0}
=\alpha_p+\frac{2}{p-1}
=\frac{p+5}{2(p-1)},
\]

and hence

\[
\boxed{
\lambda_p
=\frac{L^W_{p,0}}{L_{p,0}}
=\frac{p+5}{2(p+1)}
=\frac12+\frac{2}{p+1}.
}
\]

Therefore

\[
\boxed{\lambda_p\le\frac34\quad(p\ge7,\ p\equiv3\pmod4).}
\]

---

## 4. Why finite residue conditions require characters

A divisibility condition such as `p|r` is genuinely p-adic and belongs to the valuation state. A unit residue condition such as `W_p` depends on residues modulo `p` of integers built from all prime factors. It is therefore not enough to say only “replace the pth Euler factor”.

After the valuation strata are fixed, the unit residue predicate is a finite function on a finite product of unit groups `G_p`. Fourier inversion gives

\[
W_p(u)=\sum_{\chi\in\widehat G_p}c_{p,\chi}\chi(u),
\qquad
c_{p,\chi}=\frac1{|G_p|}\sum_{u\in G_p}W_p(u)\overline{\chi(u)}.
\]

The characters that appear are ordinary Dirichlet characters on rational unit variables and fixed-conductor Gaussian/ray-class characters on the Gaussian face variable. These are exactly the fixed-conductor objects covered by Gate F.

For fixed

\[
S=\{p_1,\ldots,p_k\},
\qquad M=\prod_{p\in S}p,
\]

CRT gives

\[
G_S\cong\prod_{p\in S}G_p,
\qquad
\widehat G_S\cong\prod_{p\in S}\widehat G_p,
\]

and therefore the simultaneous test has an exact finite character expansion

\[
W_S=\prod_{p\in S}W_p
=
\sum_{\boldsymbol\chi\in\widehat G_S}
 c_{S,\boldsymbol\chi}\,\boldsymbol\chi.
\]

Because `S` is fixed, this is a fixed finite sum before `B->infinity`.

---

## 5. Principal pole sector

The auxiliary character parameterization can have algebraic relations among coordinates. Consequently it is safer not to identify the leading sector with the single raw tuple in which every auxiliary character symbol is literally trivial.

Define the **principal pole sector** to be the set of character tuples whose induced characters on every pole-producing unbounded multiplicative channel are principal. Any auxiliary character combination that is nontrivial only on a holomorphic mixed coordinate but induces the principal character on all pole channels is included in this sector.

For this whole sector:

1. the pole-producing zeta/zero-angular factors are exactly the raw principal factors;
2. the archimedean chamber kernel `J_q` is unchanged;
3. finite Fourier inversion over the accepted residue states gives the exact local average `lambda_p` at each `p`;
4. CRT makes those local averages multiplicative across `S`.

Hence the **sum of all principal-pole-sector tuples**, not merely one auxiliary tuple, contributes

\[
\boxed{
2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)
B(\log B)^3.
}
\]

This formulation automatically handles harmless auxiliary-character aliasing and is the exact leading coefficient required by the fixed-local transfer.

The multiplier is direction-independent: the category remains only in the real chamber factor inside `D_q`, while the inert acceptance is a symmetric finite arithmetic condition on the tagged oriented variables.

---

## 6. Mixed split-prime correction

The raw coefficient system is pure pole-producing channels times a mixed Euler correction controlled in the weighted Wiener algebra.

For every fixed character tuple, values of the inserted characters at primes `q\nmid M` have modulus at most one. Gate B's coefficientwise bounds are phase-uniform, so these twists do not enlarge the weighted-Wiener majorant. Therefore the mixed quotient:

- stays absolutely convergent and holomorphic on the same fixed half-plane;
- keeps finite logarithmic moments, with constants allowed to depend on fixed `S` and the fixed tuple;
- cannot create a pole at `s=1` or restore a pole removed from a pure channel.

Inside the principal pole sector it only changes the finite holomorphic coefficient already included in the finite Fourier sum that evaluates to `prod lambda_p`. Outside that sector it cannot undo pole loss.

This is the missing compatibility statement between the fixed residue refinement and the split-prime mixed correction.

---

## 7. Nonprincipal pole sectors are lower order

Every tuple outside the principal pole sector induces a nonprincipal character on at least one pole-producing unbounded multiplicative channel. Hence at least one principal pole factor is replaced by either

- a nonprincipal fixed-conductor Dirichlet `L`-function; or
- a nontrivial fixed-conductor Gaussian/ray-class Hecke `L`-function.

Gate F gives holomorphy at `s=1` and fixed-strip polynomial growth. Section 6 shows the mixed correction is holomorphic and cannot restore the lost pole. Thus the total zero-mode pole order drops by at least one.

For each fixed tuple, the same Riesz/Perron/residue machinery gives at most

\[
O_S(B(\log B)^2)
\]

at rectangular zero mode, together with the Gate C–F curved/boundary/harmonic errors, all `o(B(log B)^3)`. Because the expansion is finite for fixed `S`, all nonprincipal pole sectors together contribute

\[
\boxed{o_S(B(\log B)^3).}
\]

No uniform estimate in `S` is claimed.

---

## 8. Fixed-S asymptotic

Combining the principal pole sector and all pole-losing sectors gives, for every fixed finite inert set `S`,

\[
\boxed{
A^{\rm tag}_{q,S}(B)
=
2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)
B(\log B)^3
+o_S(B(\log B)^3).
}
\]

The factor `2` is only a safe two-tag upper multiplicity, not an exact two-to-one statement for pair overlaps.

The OE/EE distinction is purely 2-adic. Every `p\in S` is odd, so the same multiplier and transfer apply branchwise; the finite 2-adic normalization factors out of the ratio.

---

## 9. Order-of-limits squeeze

There are arbitrarily many primes `3 mod 4` by the elementary Euclidean argument: if `p_1,...,p_k` were all of them, then

\[
N=4p_1\cdots p_k-1\equiv3\pmod4
\]

has a prime divisor `q\equiv3 (mod 4)` not in the list.

Choose `k` distinct inert primes `p_i>=7` and hold

\[
S_k=\{p_1,\ldots,p_k\}
\]

fixed. Every pair-overlap object passes all tests, so

\[
O_{qr}(B)\le A^{\rm tag}_{q,S_k}(B).
\]

Therefore

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q\prod_{p\in S_k}\lambda_p
\le
2D_q\left(\frac34\right)^k.
\]

Only after this `B`-limsup do we let `k->infinity`. Hence

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}
\]

for every pair direction. Since `T(B)` is a subset of every pair overlap,

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

No perfect-cuboid nonexistence assumption is used.

The quantifier order is locked as

```text
fix S_k
-> B -> infinity
-> k -> infinity.
```

There is no `k=k(B)` and no modulus growing with `B`.

---

## 10. Exactly-one transfer

The exact identity

\[
N_q=A_q-O_{qr}-O_{qs}+T
\]

combined with `A_q(B)~D_qB(log B)^3` and the overlap bounds yields

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

Summing directions and using `sum I_q=pi^2/8` gives

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

Gate G changes no theorem constant.

---

## 11. R04 objection closed by this lemma

This gate explicitly supplies the steps omitted in R04:

1. divisibility strata versus unit residue conditions;
2. finite character orthogonality and CRT;
3. principal **pole sector** rather than an unsafe one-tuple shorthand;
4. exact sector multiplier `prod lambda_p`;
5. phase-uniform mixed-correction compatibility;
6. at-least-one-pole loss outside the principal pole sector;
7. fixed-`S` constants and the exact order of limits.

---

## 12. Gate G locks

```text
STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER
INERT_LOCAL_STATES=U_Rb_Sc_ONLY
INERT_H_VALUATION_ZERO=true
INERT_POSITIVE_VALUATION_FRACTION=2/(p+1)
INERT_UNIT_ACCEPTANCE=(p+1)/(2(p-1))
INERT_LAMBDA=(p+5)/(2(p+1))
INERT_LAMBDA_LE_3_OVER_4_FOR_P_GE_7=true
FIXED_RESIDUE_TRANSFER=FINITE_CHARACTER_ORTHOGONALITY_PLUS_CRT
PRINCIPAL_POLE_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p
AUXILIARY_CHARACTER_ALIASING_INCLUDED=true
MIXED_CORRECTION_REMAINS_HOLOMORPHIC=true
NONPRINCIPAL_POLE_SECTOR_LOSS_AT_LEAST_ONE=true
NONPRINCIPAL_TOTAL=o_S(B(log B)^3)
FIXED_S_CONSTANTS_MAY_DEPEND_ON_S=true
LIMIT_ORDER=FIX_S_THEN_B_TO_INFINITY_THEN_ENLARGE_S
GROWING_MODULUS_THEOREM_USED=false
PAIR_OVERLAP=o(B(log B)^3)
TRIPLE_OVERLAP=o(B(log B)^3)
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13fh
```
