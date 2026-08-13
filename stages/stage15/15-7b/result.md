# Stage15-7b — population, cutoff, measure, and provenance lock

Base: Stage15-7a. This substage freezes the exact objects and theorem interfaces used by the final Stage15 verdict.

## 1. Physical populations

A Stage15 box is a primitive canonical triple
\[
0<a<b<c,\qquad \gcd(a,b,c)=1.
\]
Define
\[
R(a,b,c)=\sqrt{a^2+b^2+c^2}.
\]
The ambient exactly-two population is
\[
\mathcal B_2(B)=\{(a,b,c):R\le B,\text{ exactly two face diagonals integral}\},
\]
and the survivor population is
\[
\mathcal A_2(B)=\{C\in\mathcal B_2(B):R\in\mathbf Z\}.
\]
Their counts are `M_2(B)` and `N_2(B)`.

On `A_2`, the integral space diagonal is `d=R`, so
\[
R\le B\iff d\le B.
\]
This is the exact Stage14-to-Stage15 cutoff adapter. No comparable-height replacement is used in the final comparison.

## 2. Ambient toric theorem contract

Stage15-2b identifies the physical shared-edge surface with the real chamber of the smooth split toric resolution
\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad \rho(Y)=6,
\]
with the Stage15 height `R` itself an anticanonical adelic height. It proves
\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5},\qquad C_{M_2}>0,
\]
and directionally
\[
M_{2,j}(B)\sim C_jB(\log B)^5,\qquad C_j>0.
\]
The third-face square locus is removed through a geometrically integral degree-two thin cover and contributes only `o(B(log B)^5)`.

External interfaces used by Stage15-2b are explicitly limited to:

- Batyrev--Tschinkel: anticanonical counting for smooth projective toric varieties;
- Huang: Manin--Peyre equidistribution/counting in adelic neighbourhoods on smooth proper split toric varieties;
- Browning--Loughran: zero density of thin subsets under the stated almost-Fano/equidistribution hypotheses.

No K3 counting conjecture enters the final Stage15 theorem chain.

## 3. Exact survivor normal form and multiplicity

Stage15-4 uses positive coprime toric pairs `(m,n)` and `(r,s)` and defines
\[
A=m^2r^2+n^2s^2=N(mr+i ns),
\qquad
B=m^2s^2+n^2r^2=N(ms+i nr).
\]
It proves
\[
\boxed{R\in\mathbf Z\iff AB\in\mathbf Z^2\iff \operatorname{sf}(A)=\operatorname{sf}(B)}.
\]
Equivalently, uniquely,
\[
A=kP^2,\qquad B=kQ^2
\]
for squarefree `k>0`.

The positive toric parameter pair is uniquely reconstructible from a primitive physical shared-edge incidence after fixing the unique shared edge and `x<y`. Therefore this normal form has no hidden parameter multiplicity.

## 4. Quantitative numerator provenance

Stage14 final Theorem 2.1 proves, for the primitive canonical exactly-two family with integral space diagonal `d<=B`,
\[
\boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]
It proves neither a matching lower bound nor an asymptotic, and it proves no perfect-cuboid statement.

Stage15-5 reuses this theorem only after the exact population/cutoff identification above. The numerator theorem is not promoted to the ambient `M_2` population.

## 5. Causal local-sieve provenance

Stage15-6 works on the same unique physical toric measure. For every good split prime `p=1 mod 4`, it computes
\[
\rho_p=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)},
\]
so
\[
1-\rho_p=\frac4p+O(p^{-2}).
\]
For inert `p=3 mod 4`, `rho_p=1`.

For every fixed finite split-prime set `S`, Stage15-6 proves the same-measure refined asymptotic
\[
M_{2,S}(B)=C_{M_2}\left(\prod_{p\in S}\rho_p\right)B(\log B)^5+o_S(B(\log B)^5).
\]
Taking `B->infinity` first and only then enlarging `S` proves `N_2/M_2->0`.

The quantifier order is part of the theorem. No growing-modulus uniformity is asserted.

## 6. Directional and finite evidence lock

Stage15-3 exact census through `B=100000` gives
\[
M_2=796698,\qquad N_2=89,
\]
with ratio about `1.11711e-4`. The directional survivor vector is `(33,33,23)`.

These numbers are finite diagnostic evidence only. Stage15-3 explicitly rejects an empirical global exponent and a directional survival-rate conclusion because its predeclared sample gates fail.

The rigorous directional conclusion available in Stage15-5 is only zero density in each direction, using `N_{2,j}\le N_2` and the positive directional ambient asymptotics. It does not compare survivor constants or directional killing rates.

## 7. No-double-charge and cross-promotion lock

- Stage14 numerator saving is charged once, in Stage15-5.
- Stage15-6 local parity factors are used for an independent qualitative proof, not multiplied into the Stage15-5 rate.
- Toric parameter uniqueness is multiplicity accounting, not a thinning factor.
- The squarefree core `k`, local orientations, Pell/factor completions, and other consumed Stage15-6 receivers are not recharged in Stage15-7.
- External future quantitative mechanisms remain future gates and are not treated as missing steps of the closed Stage15-6 proof.

## 8. Provenance table

| Final claim | Canonical source |
|---|---|
| physical ambient asymptotic | `stages/stage15/15-2b/result.md` |
| finite matched comparison | `stages/stage15/15-3/result.md` |
| exact squareclass normal form | `stages/stage15/15-4/result.md` |
| strongest survival ratio upper bound | `stages/stage15/15-5/result.md` + `stages/stage14/final.md` |
| independent causal zero density | `stages/stage15/15-6-final.md` |
| Stage15-7 synthesis contract | `stages/stage15/15-7-controller.json` |

```text
STAGE15_7_SUBSTAGE=7b
STAGE15_7B_POPULATION_LOCK=true
STAGE15_7B_EXACT_CUTOFF_LOCK=R_LE_B_EQUALS_D_LE_B_ON_A2
STAGE15_7B_TORIC_MEASURE_LOCK=true
STAGE15_7B_NORMAL_FORM_MULTIPLICITY_LOCK=true
STAGE15_7B_EXTERNAL_THEOREM_CONTRACT_LOCK=true
STAGE15_7B_FINITE_EVIDENCE_ASYMPTOTIC_PROMOTION=false
STAGE15_7B_NO_DOUBLE_CHARGE=true
STAGE15_7B_PROVENANCE_TABLE_FROZEN=true
STAGE15_7B_EXIT=FINAL_BUNDLE_R01_AND_MANIFEST
```