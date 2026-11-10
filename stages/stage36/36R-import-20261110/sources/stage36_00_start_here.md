# Stage36 再開 — START HERE（2026-10-14）

```text
STAGE=36 (resumed after Stage38)
ROOT_KERNEL=K16-C3-CAMPEDELLI-UNIFORM-TORSOR
RECEIVER=R29-CAMP2
PARENT_ROUTE=Q11-CAMPEDELLI
STAGE38=CLOSED_FOR_NOW (L1 CLOSED 2026-10-13; L2 promoted R-19/R-21/R-22; main line 1G–1T frozen as candidates)
R29_CAMP2_CLOSED=false
Q11_CAMPEDELLI_CLOSED=false
ENDPOINT_CLOSED=false
PERFECT_CUBOID_CONCLUSION=NONE
CONTROL_LOCATION=this folder (36R_RESUME_20261014)
```

## このフォルダの位置づけ

- Stage36 の旧 MAIN（`FROZEN__MAIN-START-HERE__MOVED-TO-STAGE38.md`、`FROZEN__MAIN-BATCH-HANDOFF__MOVED-TO-STAGE38.md`）は **凍結のまま再有効化しない**。
- Stage38 を一旦閉じたので、Stage36 の実行管理場所を **このフォルダ** に移す。
- GitHub リポジトリ側は「current-main 統合の再監査フリーズ」が残っている（数学の内容には影響しない運用上の問題）。リポジトリを権威として扱うのは、フリーズが解けてからにする。

## 起動時に読む順番（これ以外は必要になったときだけ）

1. この START-HERE
2. `01_ROADMAP_v2.md`（最新ロードマップ：36-01〜36-10 の現状と、新しい葉 36-R1〜）
3. `02_STAGE38_INHERITANCE_LEDGER.md`（Stage38 から持ち帰る結果の分類台帳）
4. `03_OPEN_PROBLEMS.md`（未解決問題 A〜F と「なぜ今再検討する価値があるか」）
5. `04_STATE.json`（フラグと現在の葉）
6. 現行の Claude Docs（下記）。**Drive 上の CAMPEDELLI_RESULTS.md / CAMPEDELLI_WORKING.md は古いスナップショット**（R-14・ログ0C 時点）なので権威として使わない。

## 現行の権威（2026-10-14 時点）

| 種類 | 場所 | 状態 |
|---|---|---|
| RESULTS（確立した結果） | Claude Docs `dcb03d7b-1596-44fa-97f8-dae72a9d434b` | R-1〜R-23 ＋ Stage38-L1 閉鎖記録 |
| WORKING（作業・未解決） | Claude Docs `f6e71910-0ece-4bf7-a3aa-233099283357` | W-1 にログ 1T までの前線 |
| INDEX（ログ一覧） | Claude Docs `7dc1abd2-281e-4f24-a85e-5c50221b0f1e` | ログ 1T と L1 まで |
| LOG（本線 0D〜1T） | Claude Docs `ceefcc13-248b-4187-992e-847c93123030` | |
| LOG L1 | Claude Docs `f2b35121-4ebb-4d87-be2a-d5e1b9aae631` | L1-00〜L1-1E、CLOSED |
| Stage36 ROADMAP（旧） | Drive `12PMQ2ji0mrfPHUX3Q18rvxdaoL_S9LtF` | 計画の由来。`01_ROADMAP_v2.md` が上書きする |
| Stage38 本体 / 閉鎖記録 | Drive `1NJBAt6NrF6G56HApjAw0MXPFIjvn84ML` / `1W-wbABybDBGx0CVggF0Ms0vUmOuYdD39` | 確定 |
| Stage38 Reference Pack | Drive `1CL6B_-gHy-eA93XRNbW1l8zgHRT4yk0F` | 権威ではない（道具の地図） |

Drive の Docs コネクタは本文を上書きできない。Claude Docs（RESULTS・WORKING・INDEX・LOG）は Claude が直接更新する。Drive には新しいファイルを追加する形で記録する。

## 番号の付け方

- 再開後のログ：`36R-00`, `36R-01`, …（2桁の36進。09 の次は 0A、0Z の次は 10）。
- RESULTS の新しい項目：`R-24` 以降。
- 外部査読用の束：`36R-NN_REVIEW_BUNDLE_*.md`（自己完結、Drive）。

## 守ること（Stage36 の防火壁 ＋ Stage38 で増えたもの）

```text
finite fixed-p exclusions              != all-p exclusion
conditional infinitude (Schinzel H)    != unconditional infinitude
Sel2 dimension                         != Mordell-Weil rank
CT pairing zero                        != rank 2
local admissibility                    != global rational point
elliptic-sector / C3_p exclusion       != C_H(Q) = empty
C_H(Q) = empty                         != R29_CAMP2_CLOSED (separate record needed)
quotient Q-point                       != endpoint Q-point
computation (PARI etc.)                != proof (unless the certificate is the proof and is replayable)
AI review passed once                  != human-verified
```

- 仮説 H への依存を増やす方向は優先しない。
- 計算で証明を代用しない。証明が立たないときは、阻害条件と必要な補題を書く。
- 承認済みの成果（RESULTS の項目）を上書き・削除しない。訂正は新しい番号で行う。
