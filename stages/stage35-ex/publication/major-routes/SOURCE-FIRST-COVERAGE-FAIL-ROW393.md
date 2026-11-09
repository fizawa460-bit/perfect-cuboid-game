# row393 数学的原証明移植：130件の網羅性否定と原本起点監査

**判定：SOURCE-FIRST-COVERAGE-FAIL / 必要総数未確定。2026-11-09 JST。**

この文書は既存棚卸しの検証であり、新しい原証明のアップロードではない。計算コード・入力・期待結果・ZIPはユーザー指示により対象外。R0/ownerの正式採否・数学の正誤判定を新規変更しない。

## 前の130件は何だったか

主要ルートに収載した24+60+3=87本文と、GitHubのLOW・−30・類群・Selmer・HCSで選んだ43本文の合計にすぎない。元のR0・R1-R5索引全行から原著を列挙したものではなく、GitHubの正式Stage35EX単位も除外。**130を上限、完了率の分母、漏れのない総数として使用してはならない。**

## 原本側の一次点検（実際に各レーンのシート範囲を取得）

| レーン | 経緯／成果の非空データ行 | 全原文所在の非空データ行 | 対象タブ |
|---|---:|---:|---|
| R1 | 287 | 861 | `R1-研究経緯` / `R1-全原文棚卸` |
| R2 | 285 | 746 | `R2-研究経緯` / `R2-全原文棚卸` |
| R3 | 392 | 903 | `R3-研究経緯` / `R3-全原文棚卸` |
| R4 | 119 | 972 | `成果・重複` / `資料所在・棚卸` |
| R5 | 20 | 運用原典リンク50 | `研究系列・継続管理` / `原典と運用` |
| **合計** | **1,103行** | **R1-R4計3,482行＋R5運用50行** | |

行は独立数学定理を数えない。1件の成果に多数の実行・コード・提出・訂正・監査・重複があり、異なる台帳間にも重複がある。集計条件は各既知タブでヘッダ行を除き、指定範囲内の非空行のみ。Google Driveの索引が世界中の全資料を網羅するという保証も未認証。使用した正確なタブ・範囲・URLは [検証設定JSON](SOURCE-FIRST-COVERAGE-FAIL-ROW393.json)。

## GitHub既存資料側の見落とし

`stages/stage35-ex/35ex-01`〜`35ex-35` の正式研究単位には、**145の実在ファイル**、うち `35ex-35` だけで**75ファイル**がある。例えばGoal4AIの次数31同次主性、Goal4AJの分子・除数、Goal4AKの明示的関数など、数学内容と監査を伴う別の系列。これらは従来の130選定リストに入れていなかった。ただし正式GitHub `MAIN-STATE.json` のGoal4AK/E1と、Google DriveのR0研究正本とrow393 R3-07の条件付き採否は**同じ権威・同じ主張とは見なさない**。最終公開範囲との関係を項目ごとに判定。

## 130件から抜けていた研究原著の具体例（新規採用を意味しない）

- [C35-226原著](https://docs.google.com/document/d/1N7820EQUpHIFKE2KcPqIaScWc31xzHrr-HUc-_mXO48/edit)：labelled `(4,3,5)`で楕円曲線rank=1を2-isogeny降下で証明し、C195に条件付けた固定基底の全signed指数障害。**INTERNAL_PROVISIONAL・PARTIALで、moving全基底やStage35閉鎖ではない**。以前の130原著IDマップに含めていない。
- [C35-210原著](https://docs.google.com/document/d/13Z_cTp5cS-P1SFa5wWqniDqWCQ8Cgj6ZzFiDtteCrbs/edit)：strict original POINTのC素点局所衝突による`d_C=1`補題。明記状態は`RESEARCH_PROVED_DEPENDENT_NOT_ACTIVATED`であり、**正式採択と同一視禁止**。
- [R4 E18ref rank下界の原著](https://docs.google.com/document/d/1LgmJa9iPC40Bpo6flUEvs6VsZRpplQoB4VWSWl8loyM/edit)：R4の成果台帳は関連成果に後日のR0統合済み表示があるが、原著の当時時点は`R0_PREPARED_NOT_ACCEPTED`。正しい最新R0採否を時系列で照合する必要がある。130原著IDマップに未収載。
- [S238原著](https://docs.google.com/document/d/1F4Jo3DmcS-Z6TdUcSsITKr3jaTQtA_GN_oh506ssCZs/edit)：元指数の2進平方類補題で、後日のLOW系に実際に引用される。130外の直接的な数学親候補。

固定基底の例示・内部の従属結果・未採用研究と、row393までの**正式採択済み一般定理**を分離してから必須性を決める。単にタイトルにPROOFとあるだけで収載義務にはしない。

## 「漏れなし」を第三者が判断できる検証方法

1. **原本を固定：** R0現行正本、R1/R2/R3の研究経緯、R4の成果・重複、R5の系列、各全原文棚卸、R3 row393の最新版と監査、GitHub正式 `MAIN-STATE.json`を、出典ID・対象範囲・snapshotとともに記録。
2. **全研究記録を分類：** `ADOPTED_LOAD_BEARING` / `RETAINED_SCOPED` / `PROVISIONAL_NOT_ACTIVATED` / `HISTORICAL_OR_DUPLICATE` / `WITHDRAWN` / `BARRIER_ONLY`。後日の採否を優先し、旧OWNER COMMITTEDを新R0 ACCEPTとしない。どの行を除外したかも全件残す。
3. **成果を標準化：** 同じ定理の異なるC/S/P/row番号を同一命題キーにまとめる。ただし異なる labelled 基底・同一source条件・+/-符号・rank下界/上界・GRH有無を統合しない。
4. **各成果と数学親をリンク：** 原典Drive ID → 数学的主張と仮定 → 後続が使う補題 → GitHub source path/blob SHA。既存本文中の完全同値証明なら新アップ0で満たし、単なる言及は満たしたと数えない。
5. **逆方向と順方向を突合：** row393現行採用成果から遡った全必須親を収めるだけでなく、原本の全記録行に収載・不要・重複・未採用のいずれかの理由が付くことを確認。未対応・必要性未判定が1件でもあれば`COVERAGE_FAIL`。
6. **分母を初めて確定：** `必須数学原証明の異なる命題数`と`GitHubでその完全数学本文を満たした件数`から進捗率を計算。数学的独立監査と計算証拠は第1段階の外で別判定。

### 現時点の監査結論

**原本起点の全行処理・採否突合・親の再帰閉包は未完了。数学的に必要な総数、GitHubが満たした必要数、残る原証明数、進捗率は全てUNKNOWN。** 4直接親不足という旧メモも新たな全体漏れ判定後に更新する必要がある。row393研究停止・PR #1854 draft未マージ・Drive正本非改変・新しい物理排除credit0。
