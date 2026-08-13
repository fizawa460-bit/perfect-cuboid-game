# Stage15-6dv — exact cell-normalized residual switch and comparison with 6cf/6ci

Base: merged Stage15-6du after fresh audit PASS. Execute the selected `RESIDUAL_CELL_COMPLEMENTARY_SWITCH_WITH_PELL_POSTFILTER` route, but first determine whether cell normalization changes the complementary receiver at all.

Fix one exact reconstructed physical state with
\[
m=abM,\qquad n=cdN,\qquad r=acU,\qquad s=bdV,
\]
where the four cells are pairwise coprime, `H=abcd`,
\[
HMNUV\le B,\qquad R\le B,
\]
and all primitivity, positivity, canonical, exactly-two and direction masks are retained. For a decorated switched pair `(d_S,e_O)`, put
\[
q=d_Se_O,
\]
with the bounded 2-primary convention already isolated. Stage15-6ct gives
\[
\gcd(q,H)=1.
\]
The exact `phi(d_S)phi(e_O)` weight, the common squarefree survivor core `k`, and `kg^2\mid\Delta` are retained throughout.

## 1. Exact cell-normalized S/O residual forms

Define
\[
F_S^+=a^2b^2M^2+c^2d^2N^2,
\qquad
T_S^-=|a^2c^2U^2-b^2d^2V^2|,
\]
\[
F_O^-=|a^2b^2M^2-c^2d^2N^2|,
\qquad
T_O^+=a^2c^2U^2+b^2d^2V^2.
\]
These are not new forms: exactly
\[
F_S^+=m^2+n^2=A_S,\quad T_S^-=|r^2-s^2|=B_S,
\]
\[
F_O^-=|m^2-n^2|=A_O,\quad T_O^+=r^2+s^2=B_O.
\]
The decorated switch conditions are therefore
\[
\boxed{d_S\mid F_S^+,\quad d_S\mid T_S^-},
\qquad
\boxed{e_O\mid F_O^-,\quad e_O\mid T_O^+}.
\]
For odd channel support the S and O divisors are coprime prime by prime, so `q=d_Se_O` is a decorated product rather than an undecorated replacement of the two channels.

Because `(q,H)=1`, every cell coefficient is a unit modulo every odd prime power in `q`. Thus the divisibilities have an exact residual-coordinate root-line form. For the S channel define modulo `d_S`
\[
\rho_S\equiv cd(ab)^{-1},\qquad \sigma_S\equiv bd(ac)^{-1}.
\]
Then
\[
d_S\mid F_S^+
\iff
M^2+\rho_S^2N^2\equiv0\pmod{d_S},
\]
\[
d_S\mid T_S^-
\iff
U^2-\sigma_S^2V^2\equiv0\pmod{d_S}.
\]
Likewise modulo `e_O`, with the corresponding unit ratios `rho_O,sigma_O`,
\[
e_O\mid F_O^-
\iff
M^2-\rho_O^2N^2\equiv0\pmod{e_O},
\]
\[
e_O\mid T_O^+
\iff
U^2+\sigma_O^2V^2\equiv0\pmod{e_O}.
\]
This is the precise new **cell-normalized adapter**: after fixing the cells, the switched modulus is transverse to `H` and the cell coefficients can be removed from the modular root-line equations by invertible diagonal changes of residual coordinates.

It is only a modular-coordinate adapter. It does not divide the integer forms by `H` or reduce their integer sizes.

## 2. Decorated multiplicity-one complementary switch

For every decorated `d_S` define uniquely
\[
u_S=F_S^+/d_S,\qquad v_S=T_S^-/d_S.
\]
Conversely a positive pair `(u_S,v_S)` satisfying
\[
F_S^+/u_S=T_S^-/v_S\in\mathbf Z_{>0}
\]
recovers the unique decorated divisor
\[
d_S=F_S^+/u_S=T_S^-/v_S.
\]
Likewise
\[
u_O=F_O^-/e_O,\qquad v_O=T_O^+/e_O
\]
with the inverse relation
\[
e_O=F_O^-/u_O=T_O^+/v_O.
\]
Hence
\[
(d_S,e_O)
\longleftrightarrow
(u_S,v_S;u_O,v_O)
\]
is multiplicity one **with the S/O channel decoration retained**. Distinct decompositions having the same numerical product `q` are not collapsed.

The exact statewise switched weight is still
\[
\varphi(d_S)\varphi(e_O).
\]
No `phi` weight is discarded and no core or completion multiplicity is recharged.

## 3. Exact commutative comparison with Stage15-6cf

The cell map
\[
(a,b,c,d;M,N,U,V)\mapsto(m,n,r,s)
\]
is injective once the cross-gcd cells are fixed. Under this substitution the four residual forms are literally the four ambient forms used in 6cf. Therefore the diagram
\[
\text{decorated }(d_S,e_O)
\to
\text{ambient complementary cofactors}
\]
commutes exactly with
\[
(m,n,r,s)\leftrightarrow(a,b,c,d;M,N,U,V).
\]
More concretely,
\[
d_S^2=\frac{F_S^+T_S^-}{u_Sv_S},
\qquad
e_O^2=\frac{F_O^-T_O^+}{u_Ov_O}.
\]
Multiplying gives
\[
\boxed{
q^2
=\frac{F_S^+F_O^-T_S^-T_O^+}{u_Sv_Su_Ov_O}.
}
\]
But
\[
F_S^+F_O^-
=\left|(abM)^4-(cdN)^4\right|
=:\Delta_{MN},
\]
\[
T_S^-T_O^+
=\left|(acU)^4-(bdV)^4\right|
=:\Delta_{UV}.
\]
Hence
\[
\boxed{
q^2=\frac{\Delta_{MN}\Delta_{UV}}{u_Sv_Su_Ov_O}.
}
\]
This is exactly the 6cf complementary form-size identity after the cell substitution. No extra factor of `H`, `1/H`, `MNUV`, or `R` appears.

Thus the cell-normalized switch has one genuine exact refinement over 6cf: the modular coefficient-removal adapter and the explicit transversality `(q,H)=1`. The integer complementary map and its size identity are **equivalent to 6cf**, not a new receiver.

## 4. Why product height does not automatically refine the switched size

The physical bridge
\[
HMNUV\le B
\]
controls the product of residual coordinates. It does not replace the quartic-difference product
\[
\Delta_{MN}\Delta_{UV}
\]
by a smaller expression. In particular the two factors contain sums/differences of fourth powers and no common factor `H` is available to divide because `(q,H)=1` is a prime-support statement, not a magnitude identity.

Therefore the exact implication `q>D_0` is still only
\[
u_Sv_Su_Ov_O
<\frac{\Delta_{MN}\Delta_{UV}}{D_0^2},
\]
which is the same information available in 6ci after substitution.

## 5. Branch-aware completion is attached only afterward

After the decorated switch and any attempted base-state counting:

- if `k=1`, the primitive factor-gap completion from repaired 6ds is a postfilter;
- if squarefree `k>1`, the Pell/unit-orbit second-norm completion from repaired 6ds is a postfilter.

Each branch has only the already-charged `B^{o(1)}` completion multiplicity for fixed reconstructed base data. Neither branch is inserted into the complementary switch as a second independent weight.

## 6. Measure and no-double-charge audit

- `R<=B` remains the population cutoff; `HMNUV<=B` is only its exact consequence.
- `(d_S,e_O)` and `phi(d_S)phi(e_O)` remain decorated and exact.
- `(q,H)=1` is used only to invert cell coefficients modulo `q`.
- `kg^2|Delta` and all survivor masks remain attached.
- the 6da/6ds completion is charged once, after the base switch.
- no Stage14 exponent is imported.

```text
STAGE15_6_SUBSTAGE=6dv
STAGE15_6DV_RESIDUAL_FORMS_EXACT=true
STAGE15_6DV_DECORATED_DE_PRESERVED=true
STAGE15_6DV_CELL_COEFFICIENT_REMOVAL_MOD_Q_EXACT=true
STAGE15_6DV_Q_COPRIME_H_USED_AS_UNIT_ADAPTER_ONLY=true
STAGE15_6DV_COMPLEMENTARY_SWITCH_MULTIPLICITY_ONE=true
STAGE15_6DV_PHI_WEIGHTS_EXACT=true
STAGE15_6DV_SWITCH_COMMUTES_WITH_6CF=true
STAGE15_6DV_INTEGER_SWITCH_EQUIVALENT_TO_6CF=true
STAGE15_6DV_NEW_ADAPTER=MODULAR_CELL_COEFFICIENT_REMOVAL
STAGE15_6DV_NEW_SIZE_GAIN_PROVED=false
STAGE15_6DV_BRANCH_COMPLETION_POSTFILTER_ONLY=true
STAGE15_6DV_EXIT=QUANTITATIVE_REFINEMENT_TEST_READY
```
