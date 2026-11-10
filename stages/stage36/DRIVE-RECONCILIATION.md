# Stage36 / Stage38 — Google Drive正本との同期（2026-11-10）

**管理状態の正本：Google Drive。** このGitHub同期はDriveに記録された研究の進行・成果・保留・出典・監査状態を転記する作業であり、敵対的監査を前提条件としない。**数学的命題を新規に認証したという意味でもない。**

## 現在の研究管理

| 対象 | Drive正本に基づく状態 | GitHubの参照先 |
|---|---|---|
| Stage38全体 | `CLOSED_FOR_NOW`（2026-10-14） | [Stage38 状態](../stage38/DRIVE-STATUS.md) |
| Stage38-L1 | 2026-10-13にL1のみ正式閉鎖 | [Stage38 L1 closure v3](36R-import-20261110/sources/stage38_l1_closure_v3.md) |
| Stage38-L2 | R-19/R-21/R-22をDrive側RESULTSに昇格済みと記録 | [Stage38 継承台帳](36R-import-20261110/sources/stage38_inheritance_ledger.md) |
| Stage38-L3/本線 | 1G〜1Tを未査読候補として凍結、Stage36へ移管 | 同上 |
| Stage36 | 2026-10-14に36Rとして研究再開 | [36R START-HERE](36R-import-20261110/sources/stage36_00_start_here.md) |
| **Stage36現在** | **`PARKED_PROVISIONAL`（36R-06、Drive 2026-10-16更新）** | [MAIN-STATE.json](MAIN-STATE.json) |
| 次のログ番号 | **36R-07**。現行の自動研究NEXTは無し | [Drive状態JSON](36R-import-20261110/sources/36R-06_state.json) |

**現在の主要分類**は `CLASS3_RETAINED_WITH_SHARPER_CAMPEDELLI_THEOREM`（暫定）。候補台帳は `LIVE=0`、`UNTESTED=2 (B7,N5)`。残る一様命題 `(T')` は未解決で、`R29_CAMP2_CLOSED=false`、`Q11_CAMPEDELLI_CLOSED=false`、`ENDPOINT_CLOSED=false`、完全直方体の存在・非存在とも結論無し。

## Driveから引き継いだ研究上の記録

- **36R-00/04**：`J`、`C_H`と端点の量化条件を再整理。記録上、`(T') ⇔ U(Q)=empty`。原文をそのまま保存。
- **36R-01/02**：Selmer型の必要条件、自明類の曲線族への還元。部分結果と候補が混在するため原文の区分を維持。
- **36R-03/05**：固定パラメータのQC等、`p=53/8`の第3類、有限範囲の計算結果。これらを`∀p`の定理に昇格しない。
- **36R-06**：ピタゴラス境界点による`C_H(Q)`無限性（命題A）とBrauer–Maninの制限（命題B）を**Driveに記載された主張として引き継ぐ**。Drive自身が外部査読前と明記している状態を保持。
- **Stage38**：L1閉鎖とL2のDrive側昇格とL3未査読候補を混同しない。

Drive `ROADMAP v3` の最新版コピーは [ROADMAP-CURRENT.md](ROADMAP-CURRENT.md)。従来の [ROADMAP.md](ROADMAP.md) は旧36-01〜36-10の履歴・既存source lockのためバイト変更せず保持。06_ADDENDUMの優先順位、旧Stage36の修正禁止条件も保存。

## 旧GitHub版Stage36との関係

旧`36-09FE`状態と禁止された`36-09FF`のNEXTは、[履歴JSON](historical/MAIN-STATE-V296R3-36-09FE.json)へ原文のまま保存済み。旧数学証明書、source lock、有限計算、旧ロードマップは消していない。

**現行の`MAIN-STATE.json`はDriveの36R-06を表し、旧36-09FFを研究NEXTとして再開しない。** 旧36-09FE専用の歴史的検証器は上記履歴JSONを読む。

## 同期と数学的審査の線引き

- **同期自体に敵対的監査は不要。** Driveの研究状況に記載された「未査読」「暫定」「保留」をそのまま引き継ぐ。
- Driveの研究判断として、36R-04/05/06の数学的外部査読と独立の白紙再探索が今後の再開条件に書かれている。これは**GitHub同期の許可条件ではない**。
- 参考に [DESK-REVIEW.md](36R-import-20261110/DESK-REVIEW.md) を保存したが、これは別途行われた部分的な数学検討であり、Driveの記録を改変したり同期をブロックしたりしない。
- Claude Docsにある現行RESULTS/WORKING/INDEXの全内容まで取り込んだとは主張しない。同期範囲は確認できたDrive側の36R/Stage38正本（2026-10-16まで）。

## Drive正本のリンク

- [Stage36 36Rフォルダ](https://drive.google.com/drive/folders/1yvGV17wbZ7x1u8KtU1yiqCAPkCrTUnVL)
- [Stage36 ROADMAP v3](https://drive.google.com/file/d/11r4VP0790owxONdm2EeUPk9YAd1RJNvM/view)
- [36R-06 状態JSON](https://drive.google.com/file/d/1l9jXsKyawZtVvaE3-m6TckpXVQm6pV_n/view)
- [36R-06 保留監査](https://drive.google.com/file/d/1BiHaaXkFgosWjzMj-AkxUwcMyuUiJgoK/view)
- [Stage38 一時閉鎖記録](https://drive.google.com/file/d/1JG1k2WrQR_rSZLBogcMRC-kuf_067Yis/view)
- [Stage38 → Stage36 継承台帳](https://drive.google.com/file/d/1pI9-eErCmdAGpAbcUz2cfY7mQkXj-qJ6/view)

## 2026-11-10 source completeness reconciliation

The earlier partial source manifest has been superseded: the [Stage36 full source manifest](36R-import-20261110/SOURCE-MANIFEST.json) now enumerates and locates **all 20/20 files** in the 36R Google Drive folder, including 36R-01/02 review bundles, open-problem versions, initial/updated state JSON, and original resume prompts. Its [README](36R-import-20261110/README.md) documents the source precedence and remaining cross-service limitation.

Stage38 evidence is indexed in the [complete 83-file source inventory](../stage38/drive-snapshot-20261110/MANIFEST.json), with 80 text records, two fully reconstructable ZIPs, and one Google Docs review-log text snapshot. The [Stage38 README](../stage38/drive-snapshot-20261110/README.md) explains how to recover every file from the read-only bundles.

The pre-Stage38 Drive frozen `MAIN-STATE`, `MAIN-START-HERE` and handoff were copied into `36R-import-20261110/historical-drive/`. Older GitHub 36-09FE proofs, source locks and its archived state remain unchanged.

**Do not claim live Claude Docs parity.** The Drive 36R `00_START-HERE` explicitly identifies Claude Docs RESULTS / WORKING / INDEX / main LOG / L1 LOG as a separate authoritative service. Those five live texts are not obtainable from the connected Google Drive or GitHub contents in this session; historical Drive `CAMPEDELLI_RESULTS` (to R-14) and `WORKING` (to 0C) have been transferred and correctly labeled *historical*, not current.

No newer item was found in the checked 36R folder after 2026-10-16 or in the Stage38 folder after 2026-10-14. This is a claim about the listed folders, not a claim about all other services or all private documents.

**Bookkeeping sync status:** Drive Stage36/Stage38 folder content transfer complete; cross-service live Claude Docs results/index transfer NOT verified. Mathematical hostile audit is **not** a prerequisite for this copying.
