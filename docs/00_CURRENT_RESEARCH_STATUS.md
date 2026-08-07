# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1302-JST`
>
> **CURRENT_BASE_COMMIT:** `c1951efb82c307421e1a34040eea7890230cb0fa`
>
> **CURRENT_STAGE:** `Stage12-N1-3g prepared; R06 full zero-base re-review next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2_PENDING_FINAL_STAGE12_R06`
>
> **SERIES_STATUS:** `STAGE12_R05_REPAIR_PREPARED_PENDING_R06`
>
> **R04_FULL_REVIEW_VERDICT:** `REPAIRABLE`
>
> **R04_MAJOR:** `SMALL_COORDINATE_WING`
>
> **R04_MAJOR_STATUS:** `CLOSED_BY_STAGE12_N1_3F_AND_ACCEPTED_BY_R05`
>
> **R05_FULL_REVIEW_VERDICT:** `REPAIRABLE`
>
> **R05_FATAL:** `0`
>
> **R05_MAJOR:** `FIXED_HEIGHT_SHALLOW_SECTOR_BOUND_NOT_DERIVED`
>
> **3G_TEXT_STATUS:** `R05_MAJOR_CLOSED_IN_TEXT_PENDING_R06`
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_R06_FULL_REAUDIT`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage12-n1-3g-fixed-height-shallow-sector.md`
3. `docs/stage12-n1-2-final-r05.md`
4. `docs/review/stage12-n1-2-final-full-rereview-manifest-20260807-r06.md`
5. `review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R06.html`
6. `docs/stage12-n1-2-final-r04.md`
7. `docs/stage12-n1-3f-small-coordinate-wing.md`

## 1. 現在の候補定理

3d definition sheetで定義されたprimitive oriented countについて

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

この主張はperfect cuboidの存在、canonical count、exact-one-face countを含まない。

## 2. R05全体ゼロベース監査

R05はFinal R04を定義から全体再監査し、次を返した。

```text
VERDICT=REPAIRABLE
FATAL=0
MAJOR=1
MINOR=1
SMALL_COORDINATE_WING=CLOSED
NEW_CENTRAL_GAP=FIXED_HEIGHT_SHALLOW_SECTOR_BOUND_NOT_DERIVED
THEOREM_STATUS=PLAUSIBLE_REPAIRABLE_NOT_CLOSED
```

R04で見つかったsmall-coordinate wingは3fにより正式に閉じた。今回残ったのは、fixed-height shallow sectorについて旧Finalが

```text
shallow fixed-height sector: o(BL^3) by nonnegative rectangle upper bounds
```

と結論だけを書き、exact contribution、coefficient majorant、shell分割、log次数を展開していなかった点である。

## 3. Stage12-N1-3g

```text
docs/stage12-n1-3g-fixed-height-shallow-sector.md
```

`L=log B`、`X0=exp(L^(1/4))`、

\[
X_{r,s}=\frac{\lambda(r,s)B}{r^2+s^2}
\]

とする。shallow contributionは

\[
\mathcal S_{\rm sh}(B)
=
\sum_{\substack{r<s,(r,s)=1\\1\le X_{r,s}<X_0}}
\sum_{m\le X_{r,s}}A_{r,s}(m).
\]

exact formulaから

\[
0\le A_{r,s}(m)\le G(rs)2^{\omega(m)}
\]

を得る。また

\[
2^{\omega(m)}=\sum_{d\mid m}\mu^2(d)
\]

より

\[
\sum_{m\le X}2^{\omega(m)}\ll X\log(2X).
\]

`G` のDirichlet seriesは

\[
\sum_{n\ge1}\frac{G(n)}{n^s}
=
\zeta(s)^2L(s,\chi_4)
(1-2^{-s})\prod_{p\text{ odd}}(1-p^{-2s}),
\]

従って

\[
\sum_{n\le Y}G(n)\ll Y\log(2Y).
\]

これによりradial shellごとに

\[
\sum_{Q<r^2+s^2\le2Q}G(r)G(s)
\ll Q(\log(2Q))^2.
\]

shallow条件は両parity branchをまとめて

\[
B/X_0<r^2+s^2\le2B
\]

を与える。このannulusは`O(log X0)`個のdyadic shellで被覆されるため

\[
\sum_{\rm shallow}
\frac{\lambda(r,s)G(rs)}{r^2+s^2}
\ll L^2\log(2X_0).
\]

従って

\[
\boxed{
\mathcal S_{\rm sh}(B)
\ll
BL^2\{\log(2X_0)\}^2
\ll BL^{5/2}
=o(BL^3).
}
\]

これはodd--odd / opposite-parity両branchを含む直接評価である。

## 4. 二つの領域分割

混同しない。

1. fixed-height retained/shallow split:
   \[
   X_{r,s}\ge X_0
   \quad\text{or}\quad
   1\le X_{r,s}<X_0.
   \]
   retained remainderは3e、shallow exact contributionは3g。

2. radial core/wing split:
   \[
   r,s\ge U
   \quad\text{or}\quad
   \min(r,s)<U,
   \qquad U=\exp(\tfrac12L^{1/4}).
   \]
   residue mainのradial transferは3f。

active proof rulesは

```text
OLD: retained boxes satisfy min(R,S) >= S0
NEW: radial core boxes are defined by R,S >= S0; wings are bounded by 3f

OLD: shallow fixed-height sector is lower order by an unstated rectangle bound
NEW: shallow exact contribution is O(BL^(5/2)) by 3g
```

である。

## 5. R06 full zero-base re-review bundle

```text
BUNDLE_ID=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R06
COMPLETED_THROUGH=Stage12-N1-3g
FINAL_DOCUMENT=docs/stage12-n1-2-final-r05.md
MANIFEST=docs/review/stage12-n1-2-final-full-rereview-manifest-20260807-r06.md
HTML=review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R06.html
SOURCE_SNAPSHOT_COMMIT=c9a91650bece7a2173af4f495212faf1a1054aeb
SOURCE_LEDGER_SHA256=511a055bd243e0b4f40d554c949e5c1c52db1cc412bcadae55eb8b99e6de2e49
```

Final R05はFinal R04全文と3g全文を一つに統合する。R06 manifestは3gだけでなく、定義から最終誤差予算まで再度ゼロベースで監査させる。

## 6. 監査履歴

```text
R01_FULL_AUDIT=REPAIRABLE
R02_LIMITED_REVIEW=REPAIRABLE
R03_LIMITED_REREVIEW=CLOSED
R04_FULL_ZERO_BASE_REVIEW=REPAIRABLE
R04_MAJOR=SMALL_COORDINATE_WING
R04_MAJOR_ACCEPTED_CLOSED_BY_R05=true
R05_FULL_ZERO_BASE_REVIEW=REPAIRABLE
R05_MAJOR=FIXED_HEIGHT_SHALLOW_SECTOR
R05_MAJOR_TEXT_REPAIR=STAGE12_N1_3G
```

## 7. 次の作業

1. 3g、Final R05、R06 HTML、R06 manifestのCIを確認する;
2. ユーザーの明示操作でPRをマージする;
3. R06 HTMLとR06 manifestを全体ゼロベース監査へ渡す;
4. R06が`CLOSED`を返した場合だけStage12-N1-2をfully auditedとして閉じる;
5. その後にStage13-3を再開する。

## 8. 禁止事項

- R06 full review前に`FINAL_COMPLETE`または無条件の`proved`と呼ばない。
- R05の`REPAIRABLE`を無視しない。
- fixed-height shallowとradial wingを同一視しない。
- `retained => min(R,S)>=S0`を再使用しない。
- fixed-`(b,c)` kernel lemmaを使用しない。
- oriented asymptoticからcanonical countへ固定係数変換しない。
- ユーザーの明示依頼なしにPRをマージしない。

## 9. State codes

```text
STAGE12_N1_3A_COMPLETE
STAGE12_N1_3B_COMPLETE
STAGE12_N1_3C_G_COMPLETE
STAGE12_N1_3D_COMPLETE
STAGE12_N1_3E_COMPLETE
STAGE12_N1_3F_COMPLETE
STAGE12_N1_3G_COMPLETE_IN_TEXT
R05_FULL_REVIEW_VERDICT=REPAIRABLE
R05_FIXED_HEIGHT_SHALLOW=CLOSED_IN_TEXT_PENDING_R06
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_R06_FULL_REAUDIT
STAGE13_3_PAUSED_PENDING_FINAL_STAGE12_R06
NEXT_TASK=FULL_ZERO_BASE_REREVIEW_OF_PC_N1_2_R06
```
