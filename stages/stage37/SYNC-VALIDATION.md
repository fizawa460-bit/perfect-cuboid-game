# Stage37 Google Drive → GitHub 同期検証（2026-11-10）

## 完了判定
**Google Driveの6フォルダに含まれる1,138件を、既存Draft PR #1867上へ転記済み。** GitHub mainへはマージしていない。

| 対象 | Drive内のファイル | GitHubに対応物あり |
| --- | ---: | ---: |
| Stage37 直下 | 5 | 5 |
| Stage37-AUDIT | 169 | 169 |
| M3-Legacy-Cold | 5 | 5 |
| M3-Legacy-Cold / カード分離・移行元 | 55 | 55 |
| M3-Research-Cards | 447 | 447 |
| M3-Research-Cards / 個別カード | 457 | 457 |
| **計** | **1,138** | **1,138** |

- Google Driveからフォルダ単位で再取得した**全1,138件のDrive ID・タイトル・所属フォルダ**が [SOURCE-MANIFEST](drive-snapshot-20261110/SOURCE-MANIFEST.json) と一致。重複や未登録のDrive IDは0件。
- [SOURCE-MANIFEST](drive-snapshot-20261110/SOURCE-MANIFEST.json) に記載されたGitHub保存物は計1,147件。同じGoogle DocsのWord書き出しとプレーンテキスト保存などの複数形式9件を含む。
- 実際の **PR #1867 のGitツリー**を再取得して、上記1,147件の**パス・Git blob SHA・サイズ**がすべて一致。不一致0、未保存0。
- 詳細な検証数値は [SYNC-VERIFICATION.json](drive-snapshot-20261110/SYNC-VERIFICATION.json) に記録。
- 既存PRの他のStage37証拠品も保持。今回の追記は `stages/stage37/` 内に限定。

## 保全上の注意

- **原本はGoogle Drive。** この同期は研究成果の査読・承認・再分類ではない。
- Google Docsは抽出本文やDOCX、Google SheetsはXLSXとして保存した。Google独自の編集構造・数式・書式までの完全なバイト一致は保証しない。ネイティブGoogle形式とGitHubのバイナリを同一と主張しない。
- Drive側の空のネイティブ文書3件（`1qKVqK_VHHDNz6-PxKH3vrzhvlXe0uPjEZDkMs7tT6Ms`、`1eL9jH0hTVAcn1C38vWMbjGpqrYeZzkTL7VqIAFzIKtE`、`1oB5QfXcPydvW3GIe4LUD2hDBtaDUZ0xjac3RQbRuD-0`）は空であるという状態とIDを保存し、本文を捏造していない。
- 現行は`229HI-A47`、カード一覧728行目。研究のゲートOPEN・クレジット0・生産HOLD・正式ルート変更なしを維持。
- **PR #1867はDraft・未マージ**。ユーザーの明示的指示なしにマージしない。

以前に生成された`indexes/`内の部分転記記録には過去の「NOT_TRANSFERRED」が残り得る。最終的な照合は必ず上記SOURCE-MANIFESTとSYNC-VERIFICATIONを見ること。
