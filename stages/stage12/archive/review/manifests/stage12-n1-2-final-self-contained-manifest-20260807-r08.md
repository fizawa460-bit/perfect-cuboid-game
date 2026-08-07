# Stage12-N1-2 final self-contained manifest R08

> **BUNDLE_ID:** `PC-N1-2-FINAL-SELF-CONTAINED-20260807-R08`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3i`
>
> **SOURCE_SNAPSHOT_COMMIT:** `4fa4c70ad375dc90c5a99cd8d39f4caf4c47ff34`
>
> **SOURCE_LEDGER_SHA256:** `77b40002d4534ee5e24f8d7f711e7f12d1ea51994d58affe49e161cf33f71248`
>
> **HISTORICAL_PROVENANCE_COMMIT:** `8d6910e8e68145e474f92716460a1cc6f384ecf1`
>
> **CONTENT_SHA256:** `8ccbeca25711e9b793b5a86a0ebdcfaeb1164d1edc1798c35929d3e3ce191e3a`
>
> **FINAL_DOCUMENT:** `docs/stage12-n1-2-final-r07-self-contained.md`
>
> **PHYSICAL_PAGE:** `review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R08.html`
>
> **DOCUMENT_STATUS:** `SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL`

## Scope

This bundle freezes the Stage12-N1-2 proof of the primitive oriented asymptotic

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

It does not assert existence or non-existence of a perfect cuboid, a canonical-count asymptotic, an exact-one-face asymptotic, or a Stage13 ratio theorem.

## Why R08 exists

R06 and a second independent review returned `CLOSED / FATAL=0 / MAJOR=0`. A stricter later recalculation independently reproduced the local factors, the shallow-sector estimate, the corrected rectangle exponent, the radial coefficient and lower-limit treatment, and found no new fatal or major mathematical gap. Its last remaining objections were light reference dependencies:

```text
B_beta(X)<<X still referenced to old 2p
M_delta<infinity still referenced to old 2p
Tenenbaum II.5.2 application checklist not collected in one active source
```

Stage12-N1-3i closes those dependencies without reactivating the superseded 2p route.

## Direct closures in Stage12-N1-3i

```text
BETA_LINEAR_UPPER_BOUND=CLOSED_DIRECTLY_BY_STAGE12_N1_3I_SECTION_1
BETA_COPRIME_CROSS_WEIGHTED_NORM=CLOSED_DIRECTLY_BY_STAGE12_N1_3I_SECTION_2
SELBERG_DELANGE_APPLICATION_MAP=CLOSED_BY_STAGE12_N1_3I_SECTION_3
RECTANGLE_SMALL_COEFFICIENT_STEP=CLOSED_BY_STAGE12_N1_3I_SECTION_4
OLD_2P_ACTIVE_DEPENDENCY=NONE
```

The `B_beta(X)<<X` proof is direct: it rederives

\[
B_\beta(s)=\zeta(s)L(s,\chi_4)J_\beta(s),
\]

proves absolute convergence of `J_beta` at `s=1`, uses bounded partial sums of `chi_4`, and finishes by Dirichlet convolution. This coarse bound does not rely on Selberg--Delange.

For the coprime correction, `q≡1 mod4` has the exact local form

\[
C_q(s_1,s_2)=1-V_q(s_1)V_q(s_2),
\qquad
V_q(s)=\frac{b_qq^{-s}}{1+(b_q-1)q^{-s}},
\]

and the local weighted coefficient mass is `O(q^{-1-2delta})` at `sigma_1=sigma_2=1/2+delta`. Therefore

\[
\sum_{a,b\ge1}\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty.
\]

## External theorem boundary

Selberg--Delange itself remains an external published theorem-level input. The active reference is Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Third Edition, Graduate Studies in Mathematics 163, Chapter II.5, Theorem II.5.2, p.281.

Stage12-N1-3i states the finite-order working form used and maps the assumptions to `beta` (`z=1`) and `g=1*beta` (`z=2`). Stage12-N1-3h supplies the fixed-strip polynomial vertical growth. No specific Korobov--Vinogradov `3/5` remainder is required.

## Active precedence

```text
ACTIVE_CURRENT_PROOF=docs/stage12-n1-2-final-r05.md
ACTIVE_RECTANGLE_DERIVATION=Stage12-N1-3a_Lemma_3a.1
ACTIVE_VERTICAL_AND_RADIAL_BOUNDARY=Stage12-N1-3h
ACTIVE_FINAL_REFERENCE_CLOSURE=Stage12-N1-3i
3A_REFERENCES_TO_OLD_2P_INPUTS=SUPERSEDED_BY_3I
2F_FORMAL_RAW_ASYMPTOTIC=PROVENANCE_ONLY
2K_OLD_FIXED_CIRCLE_REMAINDER=SUPERSEDED_BY_3B_AND_3E
2K_OLD_SHALLOW_BOUND=SUPERSEDED_BY_3G
3A_OLD_RETAINED_MIN_RS_APPLICATION=SUPERSEDED_BY_3F
OLD_2P_ACTIVE_DEPENDENCY=NONE
SUPERSEDED_FIXED_BC_KERNEL=NOT_USED
SPECIFIC_3_5_ZERO_FREE_REMAINDER=NOT_USED
```

## Physical source set

The R08 physical page contains nine complete sources:

1. active Final R05 through Stage12-N1-3g;
2. active Stage12-N1-3a rectangle derivation;
3. historical 2b origin of the parameter sum and `G`;
4. historical 2e exact divisor expansion of `G`;
5. historical 2f derivation of `kappa` and the three-variable local factors;
6. historical 2j derivation of `A_rs`, `beta`, `gamma`;
7. historical 2k derivation of `eta` and `eta=pi*kappa`;
8. active Stage12-N1-3h vertical-growth and radial-boundary closure;
9. active Stage12-N1-3i final reference closure.

Historical entries are embedded from exact Git objects at the provenance commit. They provide derivational provenance without reactivating superseded conclusions.

## Final project status

```text
FATAL_MATHEMATICAL_GAP=NONE_IDENTIFIED
MAJOR_MATHEMATICAL_GAP=NONE_IDENTIFIED
FINAL_REFERENCE_DEPENDENCIES=CLOSED_IN_TEXT
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
THEOREM_SCOPE=PRIMITIVE_ORIENTED_COUNT_ONLY
ADDITIONAL_EXTERNAL_REVIEW=NOT_REQUIRED_AS_PROJECT_GATE
STAGE13_CAN_RESUME_AFTER_R08_IS_MERGED_AND_STAGE12_IS_FROZEN
```

```text
CHECKPOINT=END_OF_MANIFEST
CONTENT_SHA256=8ccbeca25711e9b793b5a86a0ebdcfaeb1164d1edc1798c35929d3e3ce191e3a
END_OF_BUNDLE=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R08
```
