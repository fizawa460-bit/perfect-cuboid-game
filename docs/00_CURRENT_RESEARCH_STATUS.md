# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1249-JST`
>
> **CURRENT_BASE_COMMIT:** `8449735ed6f5cd830d7e23908a859fdc50d62e39`
>
> **CURRENT_STAGE:** `Stage12-N1-3f prepared; R05 full zero-base re-review next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2_PENDING_FINAL_STAGE12_R05`
>
> **SERIES_STATUS:** `STAGE12_R04_REPAIR_PREPARED_PENDING_R05`
>
> **R03_LIMITED_REREVIEW_VERDICT:** `CLOSED`
>
> **R04_FULL_REVIEW_VERDICT:** `REPAIRABLE`
>
> **R04_FATAL:** `0`
>
> **R04_MAJOR:** `SMALL_COORDINATE_WING_NOT_COVERED_BY_MIN_RS_LOWER_BOUND`
>
> **3F_TEXT_STATUS:** `R04_MAJOR_CLOSED_IN_TEXT_PENDING_R05`
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_R05_FULL_REAUDIT`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage12-n1-3f-small-coordinate-wing.md`
3. `docs/stage12-n1-2-final-r04.md`
4. `docs/review/stage12-n1-2-final-full-rereview-manifest-20260807-r05.md`
5. `review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05.html`
6. `docs/stage12-n1-2-final-r03.md`
7. `docs/review/stage12-n1-2-final-full-rereview-manifest-20260807-r04.md`
8. `review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04.html`

主要source:

```text
docs/stage12-n1-3d-definition-sheet.md
docs/stage12-n1-3d-constant-sheet.md
docs/stage12-n1-3d-selberg-delange-reference-lock.md
docs/stage12-n1-2-final-r02.md
docs/stage12-n1-3e-local-gap-closure.md
docs/stage12-n1-3f-small-coordinate-wing.md
```

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

## 2. R04全体ゼロベース監査

R04はFinal R03を定義から全体再監査し、次を返した。

```text
VERDICT=REPAIRABLE
FATAL=0
MAJOR=1
MINOR=1
NEW_CENTRAL_GAP=SMALL_COORDINATE_WING_NOT_COVERED_BY_MIN_RS_LOWER_BOUND
THEOREM_STATUS=PLAUSIBLE_REPAIRABLE_NOT_CLOSED
```

監査で整合した項目:

- counting definitionとprimitive-first exact identity;
- fixed-circle remainderとouter average;
- locked Selberg--Delange inputs;
- rectangle asymptoticのlocal form;
- odd-prime / 2-adic local factors;
- `C_lambda^(0)=8 eta/pi^2`;
- `eta=pi*kappa`;
- radial leading integral `pi/48`;
- orientationと最終係数 `1/12`;
- superseded fixed-`(b,c)` lemmaが未使用であること。

残った問題は、fixed-height retained conditionから

\[
\min(R,S)\ge S_0
\]

を導いていた点だけである。この含意は成立しない。

## 3. Stage12-N1-3f

```text
docs/stage12-n1-3f-small-coordinate-wing.md
```

3fはradial regionを次に分ける。

```text
core: r,s >= U
r-wing: r < U
s-wing: s < U
U=exp((log B)^(1/4)/2)
```

一変数平均

\[
G_0(x)=\sum_{n\le x}g(n)\ll x\log(2x)
\]

から

\[
\sum_{n\le X}\frac{g(n)}{u^2+n^2}
\ll\frac{\log(2u)}u
\]

を導き、actual discrete wingを

\[
O((\log U)^3)=O((\log B)^{3/4})=o((\log B)^3)
\]

で評価した。continuous leading-density wingも同じ上界である。

rectangle asymptoticは定義により `R,S>=U` を満たすcoreだけへ適用する。core power tailは

\[
O(L^4U^{-1/4+\varepsilon})
\]

で任意の固定対数冪より小さく、Selberg--Delange remainderも展開次数を十分大きく固定すれば `o(L^3)` となる。

従ってactive proof ruleは

```text
OLD: retained boxes satisfy min(R,S) >= S0
NEW: core boxes are defined by R,S >= S0; complementary wings are bounded directly
```

である。

## 4. R05 full zero-base re-review bundle

```text
BUNDLE_ID=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05
COMPLETED_THROUGH=Stage12-N1-3f
FINAL_DOCUMENT=docs/stage12-n1-2-final-r04.md
MANIFEST=docs/review/stage12-n1-2-final-full-rereview-manifest-20260807-r05.md
HTML=review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05.html
SOURCE_SNAPSHOT_COMMIT=b0208ce33204a3c5f5a52afec146b08a313203f1
SOURCE_LEDGER_SHA256=f758808bc7f36307b9abcb2b6038ce497735619382fc7bc3056c65cc246cf16f
```

Final R04は六つのsource文書を一つに統合する。R05 manifestは過去の`CLOSED`を拘束的に扱わず、定義から最終error budgetまで再び全体監査させる。

特に次を明示的に確認する。

- fixed-height retained/shallowとradial core/wingが混同されていないこと;
- discrete wingとcontinuous wingがともに`o(L^3)`であること;
- core rectangle transferが`R,S>=U`だけで実行されること;
- artificial boundary `x=U`、`y=U`が未評価で残らないこと;
- full radial coefficient `pi/48`と最終`1/12`が変わらないこと。

## 5. 監査履歴

```text
R01_FULL_AUDIT=REPAIRABLE
R02_LIMITED_REVIEW=REPAIRABLE
R03_LIMITED_REREVIEW=CLOSED
R04_FULL_ZERO_BASE_REVIEW=REPAIRABLE
R04_FATAL=0
R04_MAJOR=SMALL_COORDINATE_WING
R04_MAJOR_TEXT_REPAIR=STAGE12_N1_3F
```

## 6. 重要な証明戦略

旧fixed-`(b,c)` anisotropic kernel lemmaは最終定理より強く、現行証明では使用しない。

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
```

現行経路は

\[
g(n)=\pi\gamma(n)=(1*\beta)(n)
\]

を元変数 `(r,s)` 上で平均するresidue-first routeである。

## 7. 次の作業

1. PR #79のCIと生成物を確認する;
2. ユーザーの明示操作でPR #79をマージする;
3. R05 HTMLとR05 manifestを全体ゼロベース監査へ渡す;
4. R05が`CLOSED`を返した場合だけStage12-N1-2をfully auditedとして閉じる;
5. その後にStage13-3を再開する。

## 8. 禁止事項

- R05 full review前に`FINAL_COMPLETE`または無条件の`proved`と呼ばない。
- R04の`REPAIRABLE`判定を限定レビューの`CLOSED`で上書きしない。
- `retained => min(R,S)>=S0`を再使用しない。
- fixed-`(b,c)` kernel lemmaを使用しない。
- specific `3/5` remainderをreference-lock済みinputとして復活させない。
- oriented asymptoticからcanonical countへ固定係数変換しない。
- ユーザーの明示依頼なしにPRをマージしない。

## 9. State codes

```text
STAGE12_N1_3A_COMPLETE
STAGE12_N1_3B_COMPLETE
STAGE12_N1_3C_G_COMPLETE
STAGE12_N1_3D_COMPLETE
STAGE12_N1_3E_COMPLETE
STAGE12_N1_3F_COMPLETE_IN_TEXT
R04_FULL_REVIEW_VERDICT=REPAIRABLE
R04_SMALL_COORDINATE_WING=CLOSED_IN_TEXT_PENDING_R05
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_R05_FULL_REAUDIT
STAGE13_3_PAUSED_PENDING_FINAL_STAGE12_R05
NEXT_TASK=FULL_ZERO_BASE_REREVIEW_OF_PC_N1_2_R05
```
