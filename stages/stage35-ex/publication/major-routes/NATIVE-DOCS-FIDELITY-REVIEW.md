# Stage35EX｜24原資料のテキスト忠実性とGoogle Docs構造監査（2026-11-09）

**判定：24件すべての同一抽出方式での本文テキスト一致を確認。ネイティブ表2個の構造をS240で復元済み。文書の視覚的・数学的原物同一性は別。**

## 実施した検証

Google Drive connectorから、native Google Docs13件は `get_document_text` の `paragraphs.text` をLFで連結、保存済みMarkdown11件は `fetch` でreadable textを取得。GitHub上に置いた歴史的出典ヘッダーと区切り `---` を除き、末尾改行を除去して本文を文字列比較。対象は[24件出典台帳](PRIMARY-SOURCE-MAP.json)で特定する個別ファイルID。比較の結果、**13/13 native + 11/11 Markdown=24/24 一致**。これは単なる先頭・末尾比較ではない。

native Docs13件についてはさらにGoogle Docs API `get_document` の全tab構造を調査した。本文領域のテーブル構造はS240の**2表（4行×2列と4行×4列、計24セル）**のみ。他12件の本文領域にtableはなく、13件の本文領域でAPIが返したinlineObjectElement/equation要素は0。通常の文章中の数式（Unicode/ASCII文字列）はテキストとして保持される。

S240は文字列上の24セル内容は当初からあったが、行列構造が段落テキスト中で平坦化されていた。今回、`get_document_tables` の列・行・セル位置で[保存本文](proofs/C195-upstream/S240.md)に**Markdown表を2つ再構成**した。旧Git blob `03a7f87f214c3d8001cf98fe52ddbc73eb920e5e` は変更せずGit履歴に残す。新本文はMarkdown表示のため厳密なLF連結文字列とは同一でなくなるが、24セルの表示文字列と順序は保持。新blob SHAと出典を[台帳](PRIMARY-SOURCE-MAP.json)で追跡する。

## 24件の検査一覧

| 区分 | 対象 | 同一原文テキスト | 表構造 |
|---|---|---|---|
| native 6 | S233, S237, S240, R1-223, R1-228, C174 | 6/6 | S240のみ2表、その他0 |
| native 7 | C181, R5-C212, S264, C183, R5-C220, R5-C224訂正, R5-P112 | 7/7 | 全件0 |
| Markdown 11 | S268, S269, S289, S290, C194, S270, C196, C197, C198, C199, C200 | 11/11 | 元ファイルはMarkdown・新たな表構造変換なし |

## この検証では主張しないこと

- raw Google Docs段落の書式・余白・タブ位置・リンク装飾・数式レイアウト・脚注等のネイティブ表示と、GitHub Markdownの完全な見た目の一致。
- source ZIPのバイト同一性、元の証明の正しさ、引用された外部定理の原文確認。
- native Docの空白段落や末尾改行までの逐一バイト同一性。比較は保存時に指定したparagraph-text抽出規約に従う。
- 24件以外の既存5資料群全体のフォーマット再監査。

**今回の残作業のうち「24件の本文テキスト欠落」および「確認したnative表構造の欠落」は処理済み。** 独立した数学的妥当性検査とrow393の外部一次文献確認は別途PENDING。

[移植完了要件](MIGRATION-COMPLETION-CHECKLIST.md) · [出典台帳](PRIMARY-SOURCE-MAP.json)
