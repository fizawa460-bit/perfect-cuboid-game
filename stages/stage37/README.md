# Stage37 — Google Driveを正本とする研究記録の同期

**正本:** [Google Drive Stage37](https://drive.google.com/drive/folders/1k517ClZPSIFbPi2jKROLJrYilt4XYe1p)

**研究の現在地 (Drive 2026-10-12):** `Stage37-NEW-INPUT-DELTA-AUDIT-229HI-A47`。研究生産状態 `HOLD`、主要ゲート `M3-T11-GATE-001 OPEN`、`GLOBAL_COUNTING_CREDIT=0`。これはStage37完了や完全直方体の解決を意味しません。

## 最初に読む

1. [MAIN-STATE.json](MAIN-STATE.json): 現行の正本状況（A47、カード一覧728行、課題、禁止事項）。
2. [MAIN-START-HERE.md](MAIN-START-HERE.md): 読む順序、次の正確な研究課題、履歴と現行の区別。
3. [DRIVE-SOURCE-MANIFEST.json](DRIVE-SOURCE-MANIFEST.json): Google Drive内の**6フォルダ・1,138個**の原文の対応表と転記方式。
4. [SYNC-VALIDATION.md](SYNC-VALIDATION.md): コピーと照合の結果、例外と復元方式。
5. [drive-snapshot-20261110](drive-snapshot-20261110/): 原文スナップショット。

## 同期範囲

| Driveフォルダ | 研究資料数 | GitHubの置き場所 |
|---|---:|---|
| Stage37直下 | 5 | `drive-snapshot-20261110/stage37root/` |
| 現行Research Cards | 447 | `drive-snapshot-20261110/cards/` |
| 監査 | 169 | `drive-snapshot-20261110/audit/` |
| 個別カード | 457 | `drive-snapshot-20261110/individual/` |
| 旧版保管庫 | 5 | `drive-snapshot-20261110/legacy/` |
| 旧版からの移行元カード | 55 | `drive-snapshot-20261110/legacy_moved/` |
| **合計** | **1,138** | |

各フォルダの `INVENTORY.json` に原ファイルID、名前、Drive URL、MIME、サイズ、日付を記録。各`slice-*.json`などに原文または可逆なBase64文字列が入っています。

**特殊な保存形式:**
- `current-docs/RESULT-LEDGER/` と `current-docs/NEGATIVE-REGISTER/`: 現行の大きなGoogle Docsから抽出したテキストを、順番付きファイルに分割。
- `current-index/`: 現行の7タブGoogle Sheetカード索引をXLSXエクスポートし、Base64の10分割で保持。Google Sheets特有の数式・書式がXLSXで完全に再現されるとは保証しない。
- `historical-large/`: 旧巨大ルートは`HISTORY_ONLY`、編集・自動復活を禁止。
- `legacy/`: 分離前のMAIN/RESULTS/CARD-INDEXはすべて履歴。現行の正本としては使わない。

**3件のGoogle Docsは取得元で本文が空**と記録。本文を捏造せず、IDと原URLを残しています。

## Driveに基づく現行ルール

```text
CURRENT=A47 / 229HI-A47
CARD-INDEX_CANONICAL=カード一覧!A728:Y728
OPERATIONAL_AUTHORITY=M3-T11-229
LATEST_MATHEMATICAL_CONSTRUCTION=M3-T11-228
M3-T11-230=NOT_ISSUED
PRIMARY_GATE=M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT=0
RESEARCH_PRODUCTION_STATUS=HOLD
FORMAL_ROUTE_SWITCH=NONE
PERFECT_CUBOID_CONCLUSION=NONE
```

A47の7-full `Wminus` は**特定の希薄な算術部分集団**の結果であり、全体の`P(B)=o(B^{1/3})`を示したものではありません。カード索引の`AI-10-RECALL`は既存`#REF!`/意味検索`HOLD`なので、`カード一覧`の実行を伴わない派生結果を正本扱いしません。

**管理上の同期は数学的な敵対的監査の再実施を条件としません。** Driveにある`PASS`・`HOLD`・`RETRACTED`などの原文ラベルを変更せず転記しただけです。

## GitHubへの反映

PR #1867は**Draft・未マージ**。このブランチで1,138ファイルの証拠品が読める状態に整理しました。ユーザーの明示的な承認なしにmainへマージしないこと。
