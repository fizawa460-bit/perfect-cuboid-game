# PR #1854: 最古の数学的親原著・残る接続境界

> **2026-11-09 PR #1860 続行訂正（元の歴史的本文は保存）**：この下の`CANONICAL_MARKING_AND_SIGNED_WARD_ORBIT_TRANSFER=UNVERIFIED`などは第１周**当時の一括判定**。現在は[最古E3／35EX-21/31／R1-239標識の明示橋](PR1860-E3-LABEL-INDEXED-BRIDGE-AUDIT.md)で、positive cuboid→selected４平方（この本文§Equation-level crosswalkの既知成果）、35EX-31原始marking、E3有理`τ=(C+A)/B`とR1の`τ=(t+1)/(t−1)`、同じE/P/T0・`Q−Qsharp`の代数式を照合した。**A/B偶奇標識の不一致は障壁ではない**。なおselected physicalから**必ず`D_n=T0+2nP`の部分群に入る**とは主張しない。S193第一枝・有限奇数枝・無限独立枝を区別し、全inner indexed BranchB網羅と数学独立監査はOPEN。原著129件の件数やStage35採否は変更しない。


2026-11-09 / R3-07 LOW through row393; R2-01 MID/HIGH at same snapshot. **This is a rough mathematical-parent/source map, not a proven minimal dependency closure.** No row394 research.

## Original sources now preserved on GitHub

| Original mathematical input | File | Status/scope |
|---|---|---|
| Physical selected diagonal four-square and Kummer lift into E3 | [E3-selected-physical-kummer.md](proofs/earliest-foundations/E3-selected-physical-kummer.md) | Historical provisional; direct model derivation |
| E3/Q(t) rank-one/torsion/saturation proof | [E3-generic-MW.md](proofs/earliest-foundations/E3-generic-MW.md) | Historical provisional; computation/source assumptions not replayed |
| Branch B actual Section13 genus-2 cover / reciprocal 2-isogenous quotient | [BranchB-Section13.md](proofs/earliest-foundations/BranchB-Section13.md) | Scoped structural audit retained; NOT an unconditional specialization theorem |
| Branch B actual Section16 nonsquare lemma with corrective Section17 | [BranchB-Section16.md](proofs/earliest-foundations/BranchB-Section16.md) | Only a(t) nonsquare retained; obsolete saturation split **HOLD** |

The first two are complete readable original texts; Section13/16 are verbatim sections from the large historical Branch-B research document. They were read from Drive and added with provenance. Native layout/byte identity, source calculations and external classical theorem proofs are not newly certified.

**These are mathematical ancestors older than S121 and C195.** Section13 is a direct source of S121's genus-2 / reciprocal-isogeny formulas. Section16's precise Fermat-descent lemma is used by S194/S195, without adopting its later-withdrawn specialization promotion.

## Two distinct types of ancestry

**Physical/source-wide spine** (math input, not strict every-adjacent-edge DAG):

Selected positive four-square source → [E3 physical](proofs/earliest-foundations/E3-selected-physical-kummer.md) → [S230](proofs/active-ancestors/S230.md) / [S231](proofs/active-ancestors/S231.md) → [S232](proofs/active-ancestors/S232.md) → [S233](proofs/C195-upstream/S233.md) / [S237](proofs/C195-upstream/S237.md) / [S243](proofs/active-ancestors/S243.md) → [S251](proofs/active-ancestors/S251.md), [S252](proofs/active-ancestors/S252.md), [S253](proofs/active-ancestors/S253.md) → [S263](../../materials/original-source-exclusions/parents/S263.md), [S268](proofs/C195-upstream/S268.md), [S269](proofs/C195-upstream/S269.md) → [C195](proofs/C195-canonical-source.md) (later rederivation of canonical source, NOT the historical start).

**Conditional generic/finite branches**, not all mandatory parents of rank-independent spine:

- [E3 generic MW](proofs/earliest-foundations/E3-generic-MW.md) + [Section13](proofs/earliest-foundations/BranchB-Section13.md) → [S121](proofs/active-ancestors/S121.md) → S122–126 → S190 (generic-image scoped ancestry).
- [Section16 nonsquare](proofs/earliest-foundations/BranchB-Section16.md) + S193 → [S194](proofs/active-ancestors/S194.md) / [S195](proofs/active-ancestors/S195.md) → S196 / [S231](proofs/active-ancestors/S231.md) (finite-odd scoped branch). **The Section16 saturation split was withdrawn**, and S232's independent point-only claims must not inherit its finite-odd scalar assumption.

R3 terminus: [R3-07 chain](PR1854-R3-07-CHAIN.md) → [row393](../../materials/classgroup-and-different/proofs/row393.md). −30 unconditional exclusion, complete LOW and Branch B remain OPEN. R2 terminus: [S270](proofs/foundations/S270.md), C160/C175/C185 and 155/197 → [C189](proofs/active-ancestors/C189.md) in [R2-01 chain](PR1854-R2-01-CHAIN.md). The correlated strict upper <75% remains OPEN.

## Equation-level crosswalk: existing 35EX-21 surface to the selected E3 physical packet

This is an **exact substitution of equations already printed in the older originals**, not a newly admitted theorem, primitive-label transfer, or converse to all Stage35 cases.

[35EX-21](../../35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md) has positive rational points with
```text
P_x^2=1+x^2,  P_y^2=1+y^2,
z^2=x^2+y^2,  w^2=1+x^2+y^2.
```
Thus `1+z^2=w^2`. Choose a positive rational common scale `A` so `(A,B,C)=A(1,z,w)` is a **primitive positive integer** Pythagorean triple (hence `C` odd). Set
```text
r=A*x, s=A*y, p=A*P_x, q=A*P_y, B=A*z, C=A*w.
```
The displayed 35EX-21 equations give, with no appeal to the generic Mordell–Weil rank,
```text
r^2+s^2=B^2,
p^2=A^2+r^2,
q^2=A^2+s^2=C^2-r^2.
```
Since `s^2=B^2-r^2`, these are exactly the **unindexed selected four-root equations** used in the [E3 physical/Kummer original](proofs/earliest-foundations/E3-selected-physical-kummer.md) and [S231, §0](proofs/active-ancestors/S231.md), after dividing all lengths by `C` and writing `alpha=A^2/C^2`, `beta=B^2/C^2`. Indeed
```text
rho=r/C, sigma=s/C, pi=p/C, kappa=q/C,
pi^2=alpha+rho^2, sigma^2=beta-rho^2, kappa^2=1-rho^2.
u=-rho^2, v=+rho*pi*kappa:
v^2=u(u-alpha)(u+1).
```
The opposite sign `v=-rho*pi*kappa` is the signed sheet required when the **actual** Ward point is stipulated to have negative `Y`; it is **not** a deduction of the Ward index. Conversely, any positive rational `(A,B,C,r,s,p,q)` satisfying these physical equations maps back to the stated 35EX-21 positive surface equations by division by `A`.

**Boundary, not swept under the algebra:** 35EX-21's named genus-5 fibration fixes its *first source conic* `(x,P_x)`, while the E3 physical presentation fixes the diagonal triangle `(A,B,C)`. Both sets of equations sit on the same rational cuboid surface, but these are **different choices of fibration**, and the displayed substitution does not identify their rational fibers as the same named fiber. [35EX-31](../../35ex-31/primitive-source-marking-endpoint-equivalence.md) controls additional primitive two-source marking and edge-permutation gauges. The exact correspondence of that marking to the SAME labelled E3 original packet, the specialized `D_n=T0+2nP` with signed `|n|>=3`, the required `Q/Qsharp` and infinite class, and the conditional generic/specialization transfer remains **UNVERIFIED**. In particular, the `Q(t)` generic rank-one theorem cannot be promoted to every rational specialization.

**Status:** `EQUATION_LEVEL_POSITIVE_PHYSICAL_SOURCE_CROSSWALK=CHECKED_BY_SUBSTITUTION`; `CANONICAL_MARKING_AND_SIGNED_WARD_ORBIT_TRANSFER=UNVERIFIED`; `MATHEMATICAL_PARENT_CLOSURE=NOT_CERTIFIED`. This does not extend research beyond row393 or change theorem credit.

## Older mathematical GitHub material and still unverified exact bridge

GitHub already contains [35EX-21 normalized surface/genus5 fibration](../../35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md) and [35EX-31 primitive source marking](../../35ex-31/primitive-source-marking-endpoint-equivalence.md). **These are earlier primary mathematical files; their positive rational surface equations now have the explicit substitution above into the E3 physical square package.** That formula-level match does **not** certify canonical source marking, specific selected-fiber identity, sign, signed Ward index, or the full specialized physical population. Their exact marked/orbit/quantifier transfer remains **MATCH_UNVERIFIED**, so no claim of ultimate earliest-source closure.

**Branch-B source sections 1–12 scope check:** The original [large Branch-B document](https://docs.google.com/document/d/1CKLon3eRKjsEVuIwgpSTV4DKHQ5GRWsfDw2SA6T5vNI/edit) does precede Section13 with its Section1 primitive integral E3 model, Sections4/10/11 adjacent-denominator canonical-base results, and the Section13 opening says the earlier normalization is retained. The displayed **Section13 genus-2/reciprocal quotient algebra**, however, takes the squareclass-difference input already explicitly written in [E3 physical](proofs/earliest-foundations/E3-selected-physical-kummer.md) and derives the quotient by substitution. Thus Sections1–12 are **not yet classified as individually mandatory for the current two target conclusions**; historical precedence alone is not an import requirement. The completeness/independence of any denominator claims carried to a surviving R2/R3 gate remains an audit boundary. No silent assertion of Section1–12 mathematical closure is made.

Further open: S250 within S251 equivalence; C160→C185 exact transport; external Bérczes Thm2.1(i) (S252); external de la Maza theorem (row393); generic vs specialized E3 transfer and Section13/16 correction; computational replay and source layout; necessity of individual older finite-odd branches. [C124](https://docs.google.com/document/d/1VLG7UBzuh07DIkkzsO5iL3kseCnCBtgMSSiE3lpu5fU/edit) / [C193](https://drive.google.com/file/d/1D8QNpX2k-O36w76ZoTqbVDdUFJClNnLj/view) / C192 are **NOT_AUTOMATIC_REQUIRED_MATH_PARENTS** and were not bulk uploaded.

**Conclusion:** Actual oldest mathematical material reached and preserved here: E3 physical, E3 generic MW, BranchB Section13 and the Section16 nonsquare lemma, alongside older existing 35EX-21/31 context. A globally closed mathematical dependency chain back to every primitive Stage35 source adapter is still **NOT CERTIFIED**. File count ≠ theorem count.
