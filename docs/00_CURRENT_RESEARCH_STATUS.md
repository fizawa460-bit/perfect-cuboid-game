# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1217-JST`
>
> **CURRENT_BASE_COMMIT:** `efe6ba788fa30e2c8f33b9cc98f99006dde34775`
>
> **CURRENT_STAGE:** `Stage12-N1 Final R03 consolidated; R04 full zero-base re-review next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2_PENDING_FINAL_STAGE12_R04`
>
> **SERIES_STATUS:** `STAGE12_R03_LIMITED_REVIEW_CLOSED_PENDING_FULL_R04`
>
> **R01_REPAIR_ITEMS:** `ALL_CLOSED_IN_REVIEW_CHAIN`
>
> **R02_LIMITED_REVIEW_VERDICT:** `REPAIRABLE`
>
> **R03_LIMITED_REREVIEW_VERDICT:** `CLOSED`
>
> **R03_NEW_CENTRAL_GAP:** `NONE`
>
> **THEOREM_STATUS:** `FULL_ZERO_BASE_REREVIEW_CANDIDATE`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage12-n1-2-final-r03.md`
3. `docs/review/stage12-n1-2-final-full-rereview-manifest-20260807-r04.md`
4. `review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04.html`
5. `docs/stage12-n1-3d-definition-sheet.md`
6. `docs/stage12-n1-3d-constant-sheet.md`
7. `docs/stage12-n1-3d-selberg-delange-reference-lock.md`
8. `docs/stage12-n1-3e-local-gap-closure.md`

履歴bundleは必要な場合だけ参照する。

```text
review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html
review/PC-N1-2-LIMITED-REREVIEW-20260807-R03.html
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

R03限定再レビューでは、R02から残った二項目について

```text
VERDICT=CLOSED
OUTER_AVERAGE_LEMMA=CLOSED
PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY=CLOSED
NEW_CENTRAL_GAP=NONE
```

が返された。

ただしR03は二項目限定レビューであり、証明全体をゼロから再監査したものではない。ユーザーの希望により、現行証明を一つに統合したFinal R03を作り、R04で全体を再監査する。

## 2. Final R03

```text
docs/stage12-n1-2-final-r03.md
```

Final R03は次の五文書を一つのMarkdownへ完全収録する。

1. `docs/stage12-n1-3d-definition-sheet.md`
2. `docs/stage12-n1-3d-constant-sheet.md`
3. `docs/stage12-n1-3d-selberg-delange-reference-lock.md`
4. `docs/stage12-n1-2-final-r02.md`
5. `docs/stage12-n1-3e-local-gap-closure.md`

古いstatus labelは執筆時点の履歴として残るが、現行statusはこの文書冒頭の

```text
DOCUMENT_STATUS=FULL_ZERO_BASE_REREVIEW_CANDIDATE
```

である。

Final R03は新しい数学的ショートカットを導入せず、監査対象を単一ファイルへ固定するための決定論的な統合物である。

## 3. R04 full zero-base re-review bundle

```text
BUNDLE_ID=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04
FINAL_DOCUMENT=docs/stage12-n1-2-final-r03.md
MANIFEST=docs/review/stage12-n1-2-final-full-rereview-manifest-20260807-r04.md
HTML=review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04.html
SOURCE_SNAPSHOT_COMMIT=efe6ba788fa30e2c8f33b9cc98f99006dde34775
SOURCE_LEDGER_SHA256=9938c98890850d545704128cb5a06c98cbc1422dfa14b0717a87abb1ea414435
```

R04は限定レビューではない。過去の`CLOSED`判定を前提にせず、次をゼロベースで再確認する。

- counting definitionとexact Möbius relation;
- primitive-first formulaとparity branches;
- fixed-circle remainderとouter average;
- `z=1`, `z=2` Selberg--Delange inputs;
- coprime rectangle asymptotic;
- odd-prime / 2-adic local factors;
- `C_lambda^(0)=8 eta/pi^2`;
- radial Stieltjes transferと係数`1/12`;
- shallow、arc、annulus、diagonal、floor、endpointを含む全誤差予算;
- `eta=pi*kappa`と最終定数;
- superseded fixed-`(b,c)` lemmaが暗黙使用されていないこと。

## 4. 監査履歴

### R01 full audit

```text
VERDICT=REPAIRABLE
FATAL=0
MAJOR=4
MINOR=2
CLARIFICATION=1
```

修復割当:

```text
MAJOR_01=CLOSED_BY_STAGE12_N1_3A
MAJOR_02=CLOSED_BY_STAGE12_N1_3B
MAJOR_03=CLOSED_BY_STAGE12_N1_3C_G
MAJOR_04=CLOSED_BY_STAGE12_N1_3D
CLARIFICATION_01=CLOSED_BY_STAGE12_N1_3D_REFERENCE_LOCK
MINOR_01=CLOSED
MINOR_02=CLOSED_BY_SELF_CONTAINED_R02
```

### R02 limited repair review

```text
VERDICT=REPAIRABLE
REMAINING_LOCAL_GAPS=OUTER_AVERAGE_LEMMA,PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY
FATAL=0
OPEN_CENTRAL_ROUTE=0
```

### R03 limited re-review

```text
VERDICT=CLOSED
OUTER_AVERAGE_LEMMA=CLOSED
PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY=CLOSED
NEW_CENTRAL_GAP=NONE
```

## 5. 重要な証明戦略

旧3cで設定したfixed-`(b,c)` anisotropic kernel lemmaは最終定理より強く、現行証明では使用しない。

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
```

現行経路は

\[
g(n)=\pi\gamma(n)=(1*\beta)(n)
\]

を元変数 `(r,s)` 上で平均するresidue-first routeである。

## 6. R04で要求する判定

```text
CLOSED
REPAIRABLE
OPEN
STALE_SOURCE
UNREADABLE_SOURCE
```

`CLOSED`の場合だけ、Stage12-N1-2の全体監査を完了扱いにする。

`REPAIRABLE`または`OPEN`の場合はStage13-3以降を再開しない。

## 7. 禁止事項

- R04 full review前に `FINAL_COMPLETE` または無条件の `proved` と呼ばない。
- R03の限定`CLOSED`を全証明のゼロベース監査と同一視しない。
- fixed-`(b,c)` kernel lemmaを使用しない。
- specific `3/5` remainderをreference-lock済みinputとして復活させない。
- oriented asymptoticからcanonical countへ固定係数変換しない。
- ユーザーの明示依頼なしにPRをマージしない。

## 8. State codes

```text
STAGE12_N1_3A_COMPLETE
STAGE12_N1_3B_COMPLETE
STAGE12_N1_3C_G_COMPLETE
STAGE12_N1_3D_COMPLETE
STAGE12_N1_3E_COMPLETE
R03_LIMITED_REREVIEW_VERDICT=CLOSED
FINAL_R03_CONSOLIDATED
THEOREM_STATUS=FULL_ZERO_BASE_REREVIEW_CANDIDATE
STAGE13_3_PAUSED_PENDING_FINAL_STAGE12_R04
NEXT_TASK=FULL_ZERO_BASE_REREVIEW_OF_PC_N1_2_FINAL_R04
```