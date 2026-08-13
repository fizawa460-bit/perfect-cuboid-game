# Stage13-13fr — R07 concrete fixed-S residue model

> STATUS: `STAGE13_13FR_R07_CONCRETE_FIXED_S_RESIDUE_MODEL`
>
> PURPOSE: close R07 Gate B by replacing the schema-only `G_{p,nu}` / `Omega_{p,nu}` principal-sector discussion with one explicit inert-prime state model in which the second-face test, local density, finite Fourier expansion, pole signature and overlap injection are all evaluated.
>
> INPUTS: the symbolic inert-unit calculation of Stage13-12ag, the valuation decomposition of Stage13-13fg, and the fixed-twist analytic contract of Stage13-13fq.

Fix an inert prime

\[
p\equiv3\pmod4.
\]

The local test attached to a tagged distinguished `q`-face is always the reduction modulo `p` of the **actual second-face square condition**. No unnamed auxiliary local predicate is used below.

---

## 1. Global tagged incidence and its reduction

For a distinguished integral face write

\[
x^2+y^2=P^2,
\qquad
P^2+z^2=d^2,
\]

with the outer primitive parametrization

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
 d=\frac{h(r^2+s^2)}2,
\qquad (r,s)=1.
\]

Choose one of the two distinguished-face legs as the tag; call it `x`. If a second integral face uses the same edge, then for some integer `w`

\[
x^2+z^2=w^2.
\]

Reduction modulo `p` therefore gives

\[
\bar x^2+\bar z^2=\bar w^2.
\]

Hence every true pair overlap satisfies the explicit local predicate

\[
W_p(x,z):=1_{\{x^2+z^2\in QR_0(\mathbf F_p)\}}=1.
\]

This proves, in the same coordinates used below,

```text
true global second-face square
-> local second-face square modulo p
-> W_p=1.
```

The other possible tag is obtained by `x<->y`; all formulas below are symmetric in the two face legs. The real chamber order `a<b<c` is archimedean and does not alter this finite-field symmetry.

---

## 2. Exact valuation strata

Put

\[
a=v_p(h),\qquad b=v_p(r),\qquad c=v_p(s).
\]

Because `p` is inert in `Z[i]`, if `p|h` then `p|P`, and `x^2+y^2=P^2` forces `p|x,y`; also `p|z`. This contradicts primitive gcd one. Thus

\[
a=0.
\]

Since `(r,s)=1`, `min(b,c)=0`. Consequently every local state belongs to exactly one of

```text
U    : (a,b,c)=(0,0,0),
R_b  : (0,b,0), b>=1,
S_c  : (0,0,c), c>=1.
```

These are the complete inert valuation strata.

For the unrestricted zero mode, with formal valuation weights `Y,Z`,

\[
L_{p,0}(Y,Z)
=1+\sum_{b\ge1}Y^b+\sum_{c\ge1}Z^c
=\frac{1-YZ}{(1-Y)(1-Z)}.
\]

At `Y=Z=p^{-1}`,

\[
L_{p,0}=\frac{p+1}{p-1},
\qquad
L_{p,0}^{\rm pos}=\frac{2}{p-1}.
\]

Hence positive valuation has local mass fraction `2/(p+1)`.

---

## 3. Positive-valuation states pass automatically

Suppose `b>=1` or `c>=1`. Then `p|P`. From

\[
x^2+y^2=P^2
\]

and inertness, `p|x` and `p|y`. Primitivity then forces `p\nmid z`. Therefore

\[
x^2+z^2\equiv z^2\pmod p,
\]

which is a nonzero square. Thus

\[
W_p=1
\]

on every `R_b` and `S_c` state.

This is the exact reason the positive-valuation contribution is accepted with probability one; it is not an independence assumption.

---

## 4. Unit stratum as one explicit constrained finite set

On `U`, all relevant quantities are units. Divide the two Pythagorean equations by `P^2` modulo `p`, and define

\[
X=x/P,
\quad Y=y/P,
\quad Z=z/P,
\quad \Delta=d/P.
\]

The actual constrained residue set is

\[
\boxed{
\Omega_{p,U}
=\{(X,Y,Z,\Delta)\in\mathbf F_p^4:
X^2+Y^2=1,
\ \Delta^2-Z^2=1\}.
}
\]

No group structure is asserted for `Omega_{p,U}`. It is a finite subset of the ambient additive coordinate space, equivalently a finite set on which one may restrict characters from any chosen finite abelian ambient encoding.

The accepted subset is

\[
\boxed{
\Omega^W_{p,U}
=\{\omega\in\Omega_{p,U}:X^2+Z^2\in QR_0(\mathbf F_p)\}.
}
\]

The local test is therefore literally

\[
W_p(\omega)=1_{\Omega^W_{p,U}}(\omega).
\]

The two conics have

\[
\#\{(X,Y):X^2+Y^2=1\}=p+1,
\qquad
\#\{(Z,\Delta):\Delta^2-Z^2=1\}=p-1,
\]

so

\[
|\Omega_{p,U}|=p^2-1.
\]

Stage13-12ag proves symbolically, using only the quadratic character identity and `J(chi,chi)=1`, that

\[
|\Omega^W_{p,U}|=\frac{(p+1)^2}{2}.
\]

Thus the exact unit acceptance is

\[
\boxed{
\alpha_p
=\frac{|\Omega^W_{p,U}|}{|\Omega_{p,U}|}
=\frac{p+1}{2(p-1)}.
}
\]

This is a count in the same set in which `W_p` was defined.

---

## 5. One explicit local state space including valuations

For proof-facing Fourier bookkeeping it is convenient to keep valuations and unit residues separated. Define the disjoint local state space

\[
\Omega_p
:=
\Omega_{p,U}
\sqcup\{R_b:b\ge1\}
\sqcup\{S_c:c\ge1\},
\]

with zero-mode measure determined by the local Dirichlet weights:

- each point of `Omega_{p,U}` shares the unit-stratum mass uniformly;
- `R_b` has weight `p^{-b}`;
- `S_c` has weight `p^{-c}`.

The accepted state set is

\[
\Omega_p^W
:=
\Omega^W_{p,U}
\sqcup\{R_b:b\ge1\}
\sqcup\{S_c:c\ge1\}.
\]

Therefore the accepted zero-mode local series is exactly

\[
L^W_{p,0}
=\alpha_p+\frac{2}{p-1}
=\frac{p+5}{2(p-1)}.
\]

Dividing by the unrestricted local series gives

\[
\boxed{
\lambda_p
=\frac{L^W_{p,0}}{L_{p,0}}
=\frac{p+5}{2(p+1)}.
}
\]

In particular `lambda_3=1`, and for every inert `p>=7`,

\[
\lambda_p\le\frac34.
\]

The same `lambda_p` applies to either tag because `X^2+Y^2=1` and the unit-state measure are symmetric under `X<->Y`.

---

## 6. Fixed finite `S` and the exact Fourier object

Fix once and for all a finite inert set `S`. For each `p in S`, choose a finite abelian ambient encoding `G_p` large enough to record the unit residue coordinates used by the coefficient system; for example one may use the product of the rational unit coordinates together with the Gaussian residue coordinate used by the angular factor. Let

\[
\iota_p:\Omega_{p,U}\longrightarrow G_p
\]

be the actual coordinate map. The only object expanded is the finite function

\[
f_p(g)
:=\begin{cases}
W_p(\omega),&g=\iota_p(\omega)\text{ for an admissible state},\\
0,&\text{otherwise},
\end{cases}
\]

with multiplicities absorbed into the coefficient measure when `iota_p` is not injective.

Fourier inversion on the finite abelian group gives

\[
f_p(g)=\sum_{\chi\in\widehat G_p}\widehat f_p(\chi)\chi(g).
\]

For fixed `S`, CRT gives

\[
G_S=\prod_{p\in S}G_p,
\qquad
f_S=\prod_{p\in S}f_p,
\]

and hence a finite tensor-product expansion. There is no modulus depending on `B`.

### Alias quotient is now concrete

Two ambient characters are equivalent exactly when their restrictions through `iota_p` agree on every actual admissible residue state with nonzero coefficient weight. Let

\[
N_p
:=\{\chi\in\widehat G_p:
\chi(\iota_p(\omega))=1
\text{ for every admissible }\omega\}.
\]

Then the effective character set is `widehat G_p/N_p`. If two representatives differ by an element of `N_p`, their values are identical on every coefficient state; therefore they produce **the same twisted coefficient system term by term**. Any induced pole-slot signature is consequently representative-independent. This is the missing well-definedness implication.

---

## 7. Five pole slots and the principal sector

After the already-frozen zero-mode factorization, the only unbounded pole-producing slots are

```text
H, R1, R2, S1, S2,
```

corresponding to the one `h`-zeta copy and the two copies attached to each of `r` and `s`.

For an effective character class, define its pole signature to be the five induced multiplicative characters appearing on these five pure channels after the finite residue character is inserted into the coefficient system. Because equivalent ambient characters give the same coefficient system term by term, this five-tuple is well-defined on the effective quotient.

Define

\[
\mathcal K_{p}
=\{[\chi]:\text{all five induced pole-slot characters are principal}\}.
\]

For fixed `S`, `K_S=prod K_p` after CRT.

This definition deliberately allows nontrivial ambient aliases whose action is confined to holomorphic mixed coordinates. It does not identify the principal sector with one raw all-trivial tuple.

---

## 8. Principal residue equals the physical local average

Let `Res` denote the linear functional extracting the coefficient of the full five-slot principal pole from the fixed-`S` zero-mode Dirichlet series. Evaluate the same finite Fourier expansion in two ways.

### Fourier-side evaluation

Every effective class outside `K_S` is missing at least one principal pole slot and has zero full principal residue. Therefore

\[
\operatorname{Res}(f_S)
=\sum_{[\chi]\in K_S}
\widehat f_S([\chi])\operatorname{Res}([\chi]).
\]

### Physical-state evaluation

Before Fourier expansion, `Res` simply reads the principal zero-mode local measure of the accepted physical states. By Sections 2–5 the ratio of accepted to unrestricted local principal mass is exactly `lambda_p` at each inert prime. Since `S` is fixed and CRT tensorizes the physical state measure,

\[
\boxed{
\frac{\operatorname{Res}(f_S)}{\operatorname{Res}(1)}
=\prod_{p\in S}\lambda_p.
}
\]

Thus the **entire** principal sector, including any harmless aliases, contributes exactly the required multiplier `prod lambda_p`. There is no appeal to an undefined `Omega_{p,nu}` in this calculation.

---

## 9. Nonprincipal classes lose a pole termwise

Take an effective class outside `K_S`. By definition, at least one of the five induced pure-channel characters is nonprincipal.

- a rational nonprincipal fixed-conductor channel replaces its zeta pole by a Dirichlet `L`-factor holomorphic at `s=1`;
- a Gaussian/ray-class fixed twist is covered by Stage13-13fq and is holomorphic at `s=1` for retained nonzero angular type;
- the phase-uniform mixed Wiener correction is holomorphic and cannot create a new pole.

Hence every class outside `K_S` has pole order at least one below the principal five-slot order. Because the fixed-`S` Fourier expansion is finite, summing these terms cannot create a Laurent coefficient of an order absent from every summand. Cancellation can lower pole order; it cannot restore a missing higher-order pole.

Therefore the complete nonprincipal fixed-`S` contribution is

\[
o_S(B(\log B)^3).
\]

---

## 10. Tagged overlap injection in this model

For distinct faces `q,r`, a cuboid having both faces integral has a unique shared edge. Tag the `q`-incidence by that edge. The second integral face supplies the global square equation `x^2+z^2=w^2`, so by Section 1 the tagged incidence passes `W_p` for every selected inert `p`.

Tagging does not alter `h,r,s`, primitive status, the height cutoff, or any selected local residue coordinate. Thus for every fixed `S` and finite `B`,

\[
\boxed{
O_{qr}(B)\le A^{\rm tag}_{q,S}(B).
}
\]

The unconstrained tagged ambient population has exact cardinality `2A_q(B)` because each distinguished face has exactly two legs available for tagging. The shared-edge injection chooses one of them; factor `2` can overcount but never undercount pair overlaps.

---

## 11. Fixed-S asymptotic and squeeze

Combining the principal physical residue and lower-order nonprincipal sectors gives

\[
A^{\rm tag}_{q,S}(B)
=
2D_q\Bigl(\prod_{p\in S}\lambda_p\Bigr)
B(\log B)^3+o_S(B(\log B)^3).
\]

Choose `k` distinct inert primes `p>=7`, hold `S_k` fixed, and let `B->infinity`. Then

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q(3/4)^k.
\]

Only afterward let `k->infinity`. Equivalently, for `epsilon>0`, choose `k` first so `2D_q(3/4)^k<epsilon/2`, then choose `B_0(k)` so the fixed-`S_k` remainder is `<epsilon/2` for `B>=B_0(k)`. Hence

\[
O_{qr}(B)=o(B(\log B)^3).
\]

No growing-modulus theorem is used.

---

## 12. Gate locks

```text
STAGE13_13FR=COMPLETE_R07_CONCRETE_FIXED_S_RESIDUE_MODEL
R07_GATE_B=COMPLETE
R07_ACTUAL_RESIDUE_COORDINATES_EXPLICIT=true
R07_UNIT_RESIDUE_SET=Omega_pU_X2Y2_EQ_1_DELTA2_MINUS_Z2_EQ_1
R07_SECOND_FACE_TEST=W_p=1_{X2_PLUS_Z2_IN_QR0}
R07_GLOBAL_SECOND_FACE_IMPLIES_LOCAL_TEST=true
R07_POSITIVE_VALUATION_STATES_PASS_AUTOMATICALLY=true
R07_UNIT_ACCEPTANCE=(p+1)/(2(p-1))
R07_LOCAL_MULTIPLIER=(p+5)/(2(p+1))
R07_TAG_SYMMETRY_EXPLICIT=true
R07_EFFECTIVE_QUOTIENT_WELL_DEFINED=true
R07_REDUCED_POLE_SIGNATURE_WELL_DEFINED=true
R07_PRINCIPAL_RESIDUE_RATIO_COMPUTED_IN_SAME_MODEL=true
R07_PRINCIPAL_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p
R07_NONPRINCIPAL_TERM_WISE_POLE_LOSS=true
R07_FINITE_SUM_CANNOT_RESTORE_HIGHER_POLE=true
R07_TAGGED_SHARED_EDGE_INJECTION_FIXED_S_EXPLICIT=true
R07_GATE_B_BLOCKER_CLOSED=true
R07_REPAIR_BLOCKERS_OPEN=1
R07_BLOCKER_C_CURVED_REGION_SELF_CONTAINED_CLOSURE=true
R06_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fs
```
