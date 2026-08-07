# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1339-JST`
>
> **CURRENT_BASE_COMMIT:** `f88bdd0b79daaf4e7b4ccd664c0a44eb60811fa0`
>
> **CURRENT_STAGE:** `Stage12-N1-3h prepared; R07 physical zero-base re-review next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2_PENDING_STAGE12_R07`
>
> **R06_FULL_REVIEW_VERDICT:** `CLOSED`
>
> **R06_FATAL:** `0`
>
> **R06_MAJOR:** `0`
>
> **R06_NEW_CENTRAL_GAP:** `NONE`
>
> **EXTERNAL_ZERO_BASE_REVIEW:** `REPAIRABLE_SELF_CONTAINMENT_ONLY`
>
> **EXTERNAL_NEW_CENTRAL_MATHEMATICAL_GAP:** `NONE`
>
> **3H_TEXT_STATUS:** `PROVENANCE_VERTICAL_GROWTH_AND_RADIAL_BOUNDARY_CLOSED_IN_TEXT_PENDING_R07`
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_R07_FULL_REAUDIT`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage12-n1-3h-zero-base-provenance-closure.md`
3. `docs/stage12-n1-2-final-r06-zero-base.md`
4. `docs/review/stage12-n1-2-final-zero-base-rereview-manifest-20260807-r07.md`
5. `review/PC-N1-2-FINAL-ZERO-BASE-REREVIEW-20260807-R07.html`
6. `docs/stage12-n1-2-final-r05.md`
7. `review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R06.html`

## 1. 現在の候補定理

3d definition sheetで定義されたprimitive oriented countについて

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

この主張はperfect cuboidの存在、canonical count、exact-one-face count、最終比率を含まない。

## 2. R06全体ゼロベース監査

R06は定義から最終誤差予算まで再監査され、次を返した。

```text
VERDICT=CLOSED
FATAL=0
MAJOR=0
FIXED_HEIGHT_SHALLOW=CLOSED
SMALL_COORDINATE_WING=CLOSED
RECTANGLE_ASYMPTOTIC=CLOSED
RADIAL_TRANSFER=CLOSED
FINAL_ERROR_BUDGET=CLOSED
NEW_CENTRAL_GAP=NONE
THEOREM_STATUS=CLOSED_FOR_PRIMITIVE_ORIENTED_COUNT
```

別の独立レビューも全34項目を再確認し、`CLOSED / FATAL=0 / MAJOR=0`を返した。

## 3. 外部zero-baseレビューの再オープン理由

追加の外部レビューは、局所因子、radial coefficient `pi/48`、shallow sector `O(BL^(5/2))`を独立再計算し、一致を確認した。新しいfatalまたはcentral mathematical gapは見つからなかった。

ただし、R06 physical bundleには次の導出本文が物理的に収録されていなかった。

- Stage12-N1-3aのrectangle error導出;
- 旧2b・2e・2f・2j・2kにある`G`, `kappa`, `A_rs`, `beta`, `gamma`, `eta`の由来;
- `L(s,chi_4)`のvertical polynomial growthの展開;
- radial integralで`x,y>=1`が角度端を切る効果の明示計算。

従って判定差は数学的反例ではなく、`zero-base full review`に要求する物理的自己完結性の水準である。

```text
R06_MATHEMATICAL_REVIEW=CLOSED
EXTERNAL_PHYSICAL_SELF_CONTAINMENT_REVIEW=REPAIRABLE
EXTERNAL_NEW_CENTRAL_MATHEMATICAL_GAP=NONE
```

## 4. Stage12-N1-3h

```text
docs/stage12-n1-3h-zero-base-provenance-closure.md
```

3hは次を実施する。

1. active proofとhistorical provenanceを分離する;
2. `L(s,chi_4)`のvertical growthを、absolute convergence、functional equation、Stirling、Phragmen--Lindelofから導く;
3. radial integralの正確な角度域
   \[
   \arcsin(1/t)\le\theta\le\pi/2-\arcsin(1/t)
   \]
   を用い、端点切取り誤差が`O(1)`であることを示す;
4. 3a Lemma 3a.1のrectangle exponent導出をactiveとし、3aの旧retained applicationは3fでsupersedeする。

## 5. R07 physical zero-base bundle

```text
BUNDLE_ID=PC-N1-2-FINAL-ZERO-BASE-REREVIEW-20260807-R07
COMPLETED_THROUGH=Stage12-N1-3h
FINAL_DOCUMENT=docs/stage12-n1-2-final-r06-zero-base.md
MANIFEST=docs/review/stage12-n1-2-final-zero-base-rereview-manifest-20260807-r07.md
HTML=review/PC-N1-2-FINAL-ZERO-BASE-REREVIEW-20260807-R07.html
SOURCE_SNAPSHOT_COMMIT=1cc47f22be84e2924671294c88f2613d7cbafcd4
SOURCE_LEDGER_SHA256=9e8fe78faca3e30f9bfa9db9ef5cfd7b5c33187e94889c46aa3ab83b011c6f98
HISTORICAL_PROVENANCE_COMMIT=8d6910e8e68145e474f92716460a1cc6f384ecf1
```

R07は一つのphysical pageへ次の8 sourceを全文収録する。

1. active Final R05;
2. Stage12-N1-3a;
3. historical 2b;
4. historical 2e;
5. historical 2f;
6. historical 2j;
7. historical 2k;
8. Stage12-N1-3h。

historical sourceの誤差主張を再活性化しない。active precedenceは次である。

```text
2F_FORMAL_RAW_ASYMPTOTIC=PROVENANCE_ONLY
2K_OLD_FIXED_CIRCLE_REMAINDER=SUPERSEDED_BY_3B_AND_3E
2K_OLD_SHALLOW_BOUND=SUPERSEDED_BY_3G
3A_OLD_RETAINED_MIN_RS_APPLICATION=SUPERSEDED_BY_3F
SUPERSEDED_FIXED_BC_KERNEL=NOT_USED
```

## 6. 監査履歴

```text
R01_FULL_AUDIT=REPAIRABLE
R02_LIMITED_REVIEW=REPAIRABLE
R03_LIMITED_REREVIEW=CLOSED
R04_FULL_ZERO_BASE_REVIEW=REPAIRABLE_SMALL_COORDINATE_WING
R05_FULL_ZERO_BASE_REVIEW=REPAIRABLE_FIXED_HEIGHT_SHALLOW
R06_FULL_ZERO_BASE_REVIEW=CLOSED
R06_SECOND_INDEPENDENT_REVIEW=CLOSED
R06_EXTERNAL_SELF_CONTAINMENT_REVIEW=REPAIRABLE
R07_REPAIR=STAGE12_N1_3H_AND_PHYSICAL_PROVENANCE_BUNDLE
```

## 7. 次の作業

1. R07 builderとCIでphysical bundleを生成・検証する;
2. ユーザーの明示操作でPRをマージする;
3. R07 HTMLとR07 manifestを、外部参照なしの完全zero-base監査へ渡す;
4. R07が`CLOSED`を返した場合にStage12-N1-2の最終監査状態を固定する;
5. その後Stage13-3へ戻る。

## 8. 禁止事項

- R07監査前に物理的自己完結性まで無条件で`CLOSED`と呼ばない。
- historical 2f/2kのsuperseded error claimをactive proofへ戻さない。
- `retained => min(R,S)>=S0`を再使用しない。
- fixed-`(b,c)` anisotropic kernel lemmaを使用しない。
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
STAGE12_N1_3G_COMPLETE
STAGE12_N1_3H_COMPLETE_IN_TEXT
R06_FULL_REVIEW_VERDICT=CLOSED
R06_EXTERNAL_SELF_CONTAINMENT_REVIEW=REPAIRABLE
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_R07_FULL_REAUDIT
STAGE13_3_PAUSED_PENDING_STAGE12_R07
NEXT_TASK=PHYSICAL_ZERO_BASE_REREVIEW_OF_PC_N1_2_R07
```
