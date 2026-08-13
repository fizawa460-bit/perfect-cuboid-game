# Stage15-6cf — repaired physical-height-aware divisor switch

Base: Stage15-6ce. Audit repair.

For each physical ambient state `P in A(B)` define
\[
A_S=m^2+n^2,\quad B_S=|r^2-s^2|,\quad
A_O=|m^2-n^2|,\quad B_O=r^2+s^2,
\]
so that
\[
G_S=\gcd(A_S,B_S),\qquad G_O=\gcd(A_O,B_O).
\]
The exact identity
\[
G_SG_O=\sum_{d\mid G_S}\sum_{e\mid G_O}\varphi(d)\varphi(e)
\]
is split statewise at a parameter `D0>=1`, fixed before summation:
\[
G_SG_O=M_{\le D_0}(P)+M_{>D_0}(P),
\]
where
\[
M_{\le D_0}(P)=\sum_{\substack{d\mid G_S,e\mid G_O\\de\le D_0}}\varphi(d)\varphi(e),
\]
\[
M_{>D_0}(P)=\sum_{\substack{d\mid G_S,e\mid G_O\\de>D_0}}\varphi(d)\varphi(e).
\]
Therefore, without changing the physical population or cutoff,
\[
\sum_{P\in A(B)}G_S(P)G_O(P)
=\mathcal M_{\le D_0}(B)+\mathcal M_{>D_0}(B),
\]
with `mathcal M_*` obtained by summing the corresponding statewise terms over exactly the same primitive states satisfying `R<=B`.

## Complementary cofactor switch

For every divisor `d|G_S`, define uniquely
\[
a_S=A_S/d,\qquad b_S=B_S/d.
\]
Conversely a pair `(a_S,b_S)` satisfying
\[
A_S/a_S=B_S/b_S\in\mathbf Z_{>0}
\]
recovers the unique divisor
\[
d=A_S/a_S=B_S/b_S.
\]
Thus `d <-> (a_S,b_S)` is a bijection. Likewise
\[
a_O=A_O/e,\qquad b_O=B_O/e,
\]
with `e <-> (a_O,b_O)` bijective. Hence the large range has the exact switched form
\[
M_{>D_0}(P)=
\sum_{\substack{a_S\mid A_S,b_S\mid B_S\\A_S/a_S=B_S/b_S}}
\sum_{\substack{a_O\mid A_O,b_O\mid B_O\\A_O/a_O=B_O/b_O}}
\mathbf 1_{de>D_0}\,\varphi(d)\varphi(e),
\]
where
\[
d=A_S/a_S=B_S/b_S,\qquad e=A_O/a_O=B_O/b_O.
\]
There is no multiplicity loss: every original `(d,e)` contributes to exactly one complementary quadruple and vice versa.

The exact form-size relations are
\[
d^2=\frac{A_SB_S}{a_Sb_S},\qquad
e^2=\frac{A_OB_O}{a_Ob_O},
\]
so
\[
de=\sqrt{\frac{A_SB_SA_OB_O}{a_Sb_Sa_Ob_O}}.
\]
Using only `phi(n)<=n`, the large contribution obeys the certified inequality
\[
M_{>D_0}(P)\le
\sum_{\text{switched complementary quadruples}\atop de>D_0}
\sqrt{\frac{A_SB_SA_OB_O}{a_Sb_Sa_Ob_O}}.
\]
This is the precise complementary-divisor/form-size receiver; no uniform congruence density is inserted in the large range.

## Measure, weights, and quantifiers

- `D0` is chosen before the state and divisor sums.
- The switch is performed inside each fixed primitive physical state, so primitivity and `R<=B` are unchanged.
- `phi(d)phi(e)` is retained exactly until the final certified inequality `phi<=id`; no divisor weight is silently discarded.
- The channel cores are not charged here. The decomposition is of the ambient gcd-product moment itself, so AR-028 double charging is not introduced.
- Recombination is exact:
\[
\mathcal M_{\le D_0}(B)+\mathcal M_{>D_0}(B)
=\sum_{P\in A(B)}G_S(P)G_O(P).
\]
Therefore any proven upper bounds for the two displayed ranges automatically dominate the original first moment after addition.

No quantitative bound for either range is claimed in this repair.

```text
STAGE15_6_SUBSTAGE=6cf
STAGE15_6CF_PHYSICAL_DIVISOR_SWITCH_EXACT=true
STAGE15_6CF_COMPLEMENTARY_COFACTORS_DEFINED=true
STAGE15_6CF_COMPLEMENTARY_MAP_BIJECTIVE=true
STAGE15_6CF_PHI_WEIGHTS_EXACT_UNTIL_BOUND=true
STAGE15_6CF_MULTIPLICITY_ONE=true
STAGE15_6CF_PRIMITIVITY_PRESERVED=true
STAGE15_6CF_PHYSICAL_R_LE_B_PRESERVED=true
STAGE15_6CF_QUANTIFIER_ORDER_D0_FIRST=true
STAGE15_6CF_RECOMBINATION_EXACT=true
STAGE15_6CF_MEASURE_CORRECT=true
STAGE15_6CF_NO_DOUBLE_CHARGE=true
STAGE15_6CF_SMALL_RANGE_BOUND_PROVED=false
STAGE15_6CF_LARGE_RANGE_BOUND_PROVED=false
STAGE15_6CF_FIRST_MOMENT_PROVED=false
STAGE15_6CF_EXIT=RE_AUDIT_SPLIT_INDEPENDENCE_READY
```