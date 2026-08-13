# Stage15-6dw — quantitative test and equivalence/negative certificate for the residual switch

Base: Stage15-6dv. The exact cell-normalized adapter is now known. Test whether it improves either side of the `D0` decomposition on the same physical survivor measure.

Keep the decorated pair `(d_S,e_O)`, `q=d_Se_O`, the exact weight
\[
\lambda(d_S,e_O)=\varphi(d_S)\varphi(e_O),
\]
`R<=B`, `(q,H)=1`, `kg^2|Delta`, all survivor masks, and the branch-aware completion postfilter.

## 1. Large side: no new inverse-D0 moment from cell normalization

For one switched state, 6dv proves exactly
\[
q^2=\frac{\Delta_{MN}\Delta_{UV}}{u_Sv_Su_Ov_O},
\]
with multiplicity one. Therefore the large condition `q>D0` is equivalent to
\[
\boxed{
u_Sv_Su_Ov_O<\frac{\Delta_{MN}\Delta_{UV}}{D_0^2}.}
\]
This is the Stage15-6cf/6ci complementary condition after the cell substitution and nothing stronger.

Retaining the exact weight gives the survivor large-side receiver
\[
\mathcal L_{>D_0}^{\rm surv}(B)
=
\sum_{x\in\mathcal S(B)}
\sum_{\substack{d_S\mid G_S(x),\ e_O\mid G_O(x)\\d_Se_O>D_0}}
\varphi(d_S)\varphi(e_O),
\]
where `S(B)` is the exact reconstructed survivor population, with `k=1` and `k>1` branches both included.

The switch is a bijective relabeling inside each state. Thus an estimate
\[
\mathcal L_{>D_0}^{\rm surv}(B)
\ll B^{1+o(1)}D_0^{-\sigma}
\]
with `sigma>0` would require a new average relating the complementary product to the physical survivor distribution. Neither `(q,H)=1` nor `HMNUV<=B` supplies such an average: `(q,H)=1` removes shared prime support only, while the exact switched numerator remains the quartic-difference product `Delta_MN Delta_UV`.

The branch postfilters do not repair this gap. For fixed reconstructed base data they contribute at most the already-charged `B^{o(1)}` completion multiplicity, but there is no certified correlation saying that large `q` or small complementary product causes a polynomial fraction of those base states to fail the `k=1` factor-gap or `k>1` Pell postfilter.

Therefore
\[
\boxed{\sigma>0\text{ is not proved by the cell-normalized complementary switch}.}
\]
This is a current-input negative certificate, not an impossibility theorem for a future survivor-distribution estimate.

## 2. Small side: the modular cell adapter does not improve the fringe exponent

For `q<=D0`, the new cell normalization removes unit coefficients modulo `d_S,e_O`. This is an invertible diagonal change of residue coordinates. Consequently it preserves:

- the number of legal root orientations;
- the root-line lattice index;
- the decorated `(d_S,e_O)` measure;
- the geometry-of-numbers boundary dimension.

Hence the certified fixed/moderate modulus profile used in 6ch remains, up to the same harmless unit relabeling,
\[
N_{d_S,e_O}(B)
\ll
\frac{B(\log B)^5}{q^2}
+
B(\log B)^{9/2+\varepsilon}q^{10+\varepsilon}.
\]
After exact `phi(d_S)phi(e_O)` summation this again yields
\[
\mathcal M_{\le D_0}(B)
\ll
B(\log B)^5(\log D_0)^2
+
B(\log B)^{9/2+\varepsilon}D_0^{13+\varepsilon}.
\]
The cell-unit change does not alter the `q^{10+epsilon}` boundary/error factor. Therefore it does not open a polynomial threshold `D0=B^theta`.

The `k=1` factor-gap and `k>1` Pell completion are attached after this base/modulus count. With only a `B^{o(1)}` pointwise completion bound and no same-measure rejection density, they cannot convert the displayed error into `B^{1-delta+o(1)}q^beta` with a fixed `delta>0`.

Thus
\[
\boxed{\delta>0\text{ is not proved by the cell-normalized switch or its branch postfilters}.}
\]

## 3. Precise comparison with 6cf/6ci

The comparison is now exact rather than verbal:

1. **new exact adapter:** because `(q,H)=1`, the cell coefficients are units modulo the switched channels, so the modular conditions become normalized residual root lines;
2. **same integer switch:** the complementary cofactors are literally `A_S/d_S`, `B_S/d_S`, `A_O/e_O`, `B_O/e_O` after substitution;
3. **same large size identity:** `q^2=Delta_MN Delta_UV/(u_Sv_Su_Ov_O)` is the 6cf identity in cell coordinates;
4. **same small local index:** invertible coefficient removal does not change the 6ch root-line lattice count;
5. **new physical bridge does not couple to q:** `HMNUV<=B` and `(q,H)=1` do not yield an inverse `D0` moment without a new distribution theorem.

Therefore the route is not merely renamed: it has produced and consumed a legitimate modular cell adapter. Quantitatively, however,
\[
\boxed{
\text{RESIDUAL CELL SWITCH}
=\text{6cf/6ci switch}+\text{unit-coordinate adapter},
}
\]
and the adapter is exponent-neutral with current inputs.

## 4. No-double-charge and branch audit

- For `k=1`, enumerate at most one first factor-gap completion fiber and use the second factor equation only as a postfilter.
- For `k>1`, enumerate at most one first Pell/ideal-unit completion fiber and use the second norm only as a postfilter.
- The branch union is disjoint in `k` and is summed, never multiplied.
- No `B^o(1)` completion factor is used as a fake `D0` saving.
- `phi(d_S)phi(e_O)` is retained until a separately certified inequality is invoked.
- No Stage14 exponent is cross-promoted.

## 5. Quantitative ledger

The current certified outputs remain
\[
\boxed{\delta>0:\ \mathrm{NO}},
\qquad
\boxed{\sigma>0:\ \mathrm{NO}},
\]
with no executable polynomial overlap window.

```text
STAGE15_6_SUBSTAGE=6dw
STAGE15_6DW_LARGE_SWITCH_EQUIVALENT_TO_6CI=true
STAGE15_6DW_CELL_ADAPTER_EXPONENT_NEUTRAL=true
STAGE15_6DW_INVERSE_D0_MOMENT_PROVED=false
STAGE15_6DW_SMALL_ROOT_LINE_INDEX_UNCHANGED=true
STAGE15_6DW_SMALL_FRINGE_POWER_GAIN_PROVED=false
STAGE15_6DW_K1_POSTFILTER_FIXED_POWER_PROVED=false
STAGE15_6DW_KGT1_POSTFILTER_FIXED_POWER_PROVED=false
STAGE15_6DW_DELTA_PROVED=false
STAGE15_6DW_SIGMA_PROVED=false
STAGE15_6DW_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6DW_NEGATIVE_CERTIFICATE=CURRENT_INPUT_EQUIVALENCE
STAGE15_6DW_EXIT=NEGATIVE_CERTIFICATE_FROZEN_NEXT_ROUTE_SELECTION_READY
```
