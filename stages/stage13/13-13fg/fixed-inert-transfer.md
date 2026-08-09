# Stage13-13fg — fixed inert-prime transfer and overlap squeeze

> STATUS: `STAGE13_13FG_FIXED_INERT_TRANSFER_LEMMA`
>
> PURPOSE: close R05 Gate G by replacing the compressed fixed-prime overlap paragraph with a proof-facing finite-character transfer, principal/nonprincipal decomposition, exact inert multiplier, and explicit order-of-limits squeeze.
>
> INPUTS: the raw directional asymptotic and common arithmetic factor already audited in Gates A–F; the exact inert local-state calculation of 13-12ae/13-12ag; and the fixed-conductor Dirichlet/Gaussian-Hecke contracts made explicit in 13-13ff.
>
> SCOPE: pair/triple overlap only. No effective growing-modulus estimate is claimed.

Write

\[
D_q:=\frac{\kappa I_q}{3\pi^3},
\qquad
A_q(B)\sim D_q B(\log B)^3.
\]

For a pair of canonical face types `q,r`, let `O_{qr}(B)` denote the pair overlap. A pair-overlap object has a shared edge. Relative to the distinguished `q` face, tag one of its two legs; if the tag is the shared edge then a second-face square condition must hold. We use the two possible tags only as a safe upper multiplicity. Thus

\[
O_{qr}(B)\le A^{\rm tag}_{q,S}(B)
\]

for the population of tagged raw incidences passing every chosen local test in a finite inert-prime set `S`, and the unconstrained tagged population has leading constant `2D_q`.

The point of this gate is to prove, for every fixed finite `S`,

\[
\boxed{
A^{\rm tag}_{q,S}(B)
=
2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)
B(\log B)^3
+o_S(B(\log B)^3),
}
\]

where

\[
\boxed{
\lambda_p=\frac{p+5}{2(p+1)}
}
\]

for every inert odd prime `p\equiv3 (mod 4)`.

The subscript `S` on the remainder is deliberate: no uniformity as `|S|` grows is used or needed.

---

## 1. One tagged overlap test

For a tagged raw incidence write

\[
x^2+y^2=P^2,
\qquad
P^2+z^2=d^2.
\]

If the tagged leg is shared with a second integral face, then

\[
x^2+z^2=w^2.
\]

For an inert odd prime

\[
p\equiv3\pmod4,
\]

define

\[
W_p=1_{\{x^2+z^2\in QR_0(\mathbf F_p)\}}.
\]

Every genuine tagged pair-overlap passes `W_p=1` for every such `p`.

The tag matters only to select which face leg appears in the test. The unit-state calculation is symmetric under interchange of the two face legs, so the same local multiplier applies to either tag and to every canonical direction.

---

## 2. Exact inert valuation states

Use the odd-prime outer coordinates

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\qquad (r,s)=1.
\]

At an inert `p`, put

\[
a=v_p(h),\qquad b=v_p(r),\qquad c=v_p(s).
\]

Primitivity forces

\[
a=0.
\]

Indeed, if `p|h` then `p|P,z`; inertness in `x^2+y^2=P^2` forces `p|x,y`, contradicting primitive gcd one. Also `(r,s)=1` gives

\[
\min(b,c)=0.
\]

Therefore the complete allowed valuation states are

```text
U    : (a,b,c)=(0,0,0)
R_b  : (a,b,c)=(0,b,0), b>=1
S_c  : (a,b,c)=(0,0,c), c>=1.
```

The unrestricted zero-mode inert local series is

\[
L_{p,0}(Y,Z)
=1+\sum_{b\ge1}Y^b+\sum_{c\ge1}Z^c
=\frac{1-YZ}{(1-Y)(1-Z)}.
\]

At `Y=Z=p^{-1}`,

\[
L_{p,0}(p^{-1},p^{-1})=\frac{p+1}{p-1},
\]

and the positive-valuation mass is exactly

\[
\frac{2}{p-1}.
\]

Hence its fraction of the unrestricted local mass is exactly

\[
\frac{2}{p+1}.
\]

Every positive-valuation state passes the tagged square test automatically: `p|P` forces `x\equiv y\equiv0 (mod p)`, while primitivity forces `z` to be a unit, so `x^2+z^2\equiv z^2`.

---

## 3. Unit-state symbolic acceptance

On the unit state normalize `P=1`. Then

\[
X^2+Y^2=1,
\qquad
D^2-Z^2=1.
\]

For inert `p`, these have respectively `p+1` and `p-1` points, so the unrestricted unit state contains

\[
T=p^2-1
\]

normalized pairs.

The symbolic quadratic-character calculation already expanded in 13-12ag gives

\[
S=2(p-1)
\]

for the signed character sum, while exactly four unit states have `X^2+Z^2=0`. Therefore

\[
N_{\rm acc}=\frac{T+S+4}{2}=\frac{(p+1)^2}{2}.
\]

Thus the accepted unit mass relative to the normalized unit local mass is

\[
\boxed{
\alpha_p=\frac{p+1}{2(p-1)}.
}
\]

Combining this with the automatic positive-valuation mass gives

\[
L^W_{p,0}
=\alpha_p+\frac{2}{p-1}
=\frac{p+5}{2(p-1)}.
\]

Dividing by the unrestricted local factor,

\[
\boxed{
\lambda_p
:=\frac{L^W_{p,0}}{L_{p,0}}
=\frac{p+5}{2(p+1)}
=\frac12+\frac{2}{p+1}.
}
\]

Hence

\[
\boxed{\lambda_p\le\frac34\qquad(p\ge7,\ p\equiv3\pmod4).}
\]

This exact formula, not a soft `1/2+O(1/p)`, is the multiplier used below.

---

## 4. Why a residue condition is not merely a single Euler-factor replacement

A divisibility condition such as `p|r` is genuinely p-adic and may be handled directly in the `p`-local valuation state. A unit residue condition such as `W_p`, however, depends on the residue modulo `p` of integers built from all prime factors. It is therefore not justified to say only “replace the `p`th Euler factor” and stop.

For fixed `p`, after splitting the three valuation strata above, the remaining unit residue predicate is a finite function on a finite product of residue groups. Denote the relevant finite unit group by `G_p`. Fourier inversion on `G_p` gives the exact identity

\[
W_p(u)=\sum_{\chi\in\widehat G_p}c_{p,\chi}\chi(u),
\qquad
c_{p,\chi}
=\frac1{|G_p|}\sum_{u\in G_p}W_p(u)\overline{\chi(u)}.
\]

Depending on the coordinate channel, these characters are ordinary Dirichlet characters on rational unit variables or fixed-conductor Gaussian/ray-class characters on the Gaussian face variable. This is precisely the fixed-conductor external boundary recorded in Gate F.

For a finite prime set

\[
S=\{p_1,\ldots,p_k\},
\qquad M=\prod_{p\in S}p,
\]

CRT tensors the local residue groups and character groups:

\[
G_S\cong\prod_{p\in S}G_p,
\qquad
\widehat G_S\cong\prod_{p\in S}\widehat G_p.
\]

Therefore the simultaneous indicator is an exact finite character expansion

\[
W_S:=\prod_{p\in S}W_p
=\sum_{\boldsymbol\chi\in\widehat G_S}
 c_{S,\boldsymbol\chi}\,\boldsymbol\chi.
\]

There are finitely many terms because `S` is fixed before `B->infinity`.

---

## 5. Principal tuple and the exact product of local multipliers

Call the tuple in which every residue character is principal the **principal character tuple**. In that tuple all pole-producing global factors are the same principal zeta/zero-angular factors as in the raw zero mode. The archimedean chamber kernel is also unchanged because the residue test is finite and arithmetic.

The principal coefficient is the finite local average of the accepted residue states, separately in each valuation stratum. With the normalization of §2–3, this multiplies the raw local zero-mode mass at `p` by exactly

\[
\lambda_p.
\]

CRT makes the principal finite-local factor multiplicative across distinct fixed primes, hence the principal tuple contributes

\[
\boxed{
2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)
B(\log B)^3
}
\]

at leading order.

No direction-dependent arithmetic factor is introduced here. The category `q` remains only in the real chamber factor already contained in `D_q`; the inert residue calculation is symmetric in the tagged face legs and is independent of the chamber direction.

---

## 6. Mixed split-prime correction under the fixed residue refinement

The raw proof factors the coefficient system into pure pole-producing channels times a mixed Euler correction controlled in the weighted Wiener algebra.

For the principal tuple, primes outside the fixed modulus `M` carry exactly the raw principal characters, so the infinite split-prime mixed correction is literally the same one as in the unconstrained zero mode. The finitely many primes dividing `M` are absorbed into the finite local acceptance multiplier above.

For a nonprincipal fixed-conductor tuple, characters at primes `q\nmid M` have modulus at most one. The Gate B coefficientwise estimates are phase-uniform, so inserting these character phases cannot enlarge the weighted-Wiener majorant. Consequently:

1. the mixed Euler quotient remains absolutely convergent and holomorphic on the same fixed half-plane;
2. its logarithmic moments remain finite, with constants allowed to depend on fixed `S` and the finite character tuple;
3. it cannot create a pole at `s=1` or restore a pole removed by a nonprincipal Dirichlet/Hecke factor.

This is the precise reason the split-prime mixed correction does not invalidate the principal/nonprincipal separation.

---

## 7. Every nonprincipal tuple is lower order

Consider one nonprincipal character tuple in the finite expansion of `W_S`. At least one unbounded multiplicative channel carries a nonprincipal character. In the Euler-product factorization this replaces at least one pole-producing principal factor by one of:

- a nonprincipal Dirichlet `L`-function of fixed conductor; or
- a nontrivial Gaussian/ray-class Hecke `L`-function of fixed conductor/nonzero angular type.

By Gate F these factors are holomorphic at `s=1` and have the required fixed-strip polynomial growth. The mixed correction of §6 is holomorphic and cannot restore the missing pole.

Thus the total pole order at the zero-mode corner drops by at least one. Applying the same finite Riesz/Perron/residue machinery as in Gates C–F gives, for each fixed nonprincipal tuple,

\[
O_{S,\boldsymbol\chi}(B(\log B)^2)
\]

at the rectangular zero-mode level, plus the already-audited curved/boundary/harmonic errors, all of which are `o(B(log B)^3)`. Since the character expansion has only finitely many terms for fixed `S`, their total is

\[
\boxed{o_S(B(\log B)^3).}
\]

No estimate uniform in `S` is asserted.

This is enough for the overlap squeeze because the limit order is fixed `S`, then `B->infinity`, then enlarge `S`.

---

## 8. Fixed-S constrained asymptotic

Combining the principal tuple and all nonprincipal tuples yields, for every fixed finite inert-prime set `S`,

\[
\boxed{
A^{\rm tag}_{q,S}(B)
=
2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)
B(\log B)^3
+o_S(B(\log B)^3).
}
\]

The factor `2` is only the safe two-tag upper multiplicity. It is not used as an exact two-to-one description of pair overlaps.

The OE/EE distinction is purely 2-adic. Since every `p\in S` is odd, the same inert multiplier and fixed-character transfer apply separately to each parity branch; the finite 2-adic normalization factors out before taking the ratio.

---

## 9. Order-of-limits squeeze

There are arbitrarily many inert primes `p\equiv3 (mod 4)` without invoking Dirichlet's theorem on primes in progressions. If `p_1,...,p_k` were all such primes, then

\[
N=4p_1\cdots p_k-1\equiv3\pmod4
\]

has a prime divisor `q\equiv3 (mod 4)` not among them.

Choose any `k` distinct inert primes

\[
S_k=\{p_1,\ldots,p_k\},
\qquad p_i\ge7,
\]

and **hold `S_k` fixed**. Every pair-overlap object passes all tests, so

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

Only now let `k->infinity`. Hence

\[
\boxed{
O_{qr}(B)=o(B(\log B)^3)
}
\]

for every pair of face directions.

The triple overlap is a subset of every pair overlap, so

\[
\boxed{
T(B)=o(B(\log B)^3).
}
\]

No perfect-cuboid nonexistence assumption is used.

The quantifier order is permanently locked as

```text
fix S_k
-> B -> infinity
-> k -> infinity.
```

There is no choice `k=k(B)` and no modulus growing with `B`.

---

## 10. Exactly-one transfer

The exact inclusion-exclusion identity is

\[
N_q=A_q-O_{qr}-O_{qs}+T.
\]

Since

\[
A_q(B)\sim D_qB(\log B)^3
\]

and all pair/triple overlaps are lower order,

\[
N_q(B)\sim D_qB(\log B)^3
=\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

Summing the three directions and using `sum I_q=pi^2/8` gives

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

Thus Gate G changes no theorem constant.

---

## 11. What this repairs relative to R04

R04 compressed the fixed-prime transfer enough that an adversarial reader still had to supply several steps. Gate G makes them explicit:

1. divisibility strata and unit residue conditions are separated;
2. unit residue predicates are expanded by finite character orthogonality rather than asserted to be a one-prime Euler-factor replacement;
3. the principal character tuple is identified and shown to contribute exactly `prod lambda_p`;
4. the mixed split-prime correction is shown to remain holomorphic and unable to alter pole order under fixed characters;
5. every nonprincipal tuple loses at least one pole and is lower order;
6. constants may depend on fixed `S`; no growing-modulus uniformity is used;
7. the order `fix S -> B limit -> enlarge S` is explicit.

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
PRINCIPAL_TUPLE_MULTIPLIER=product_{p_in_S}_lambda_p
MIXED_CORRECTION_REMAINS_HOLOMORPHIC=true
NONPRINCIPAL_TUPLE_POLE_LOSS_AT_LEAST_ONE=true
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
