# Stage35EX 主要ルート本文 — row393停止時点

> [**PR #1854の最新：R3-07(row393)・R2-01の端から端までの粗い証明鎖**](PR1854-ENDTOEND-CHAIN.md)。Google Driveから数学原著11本を追加し、古い数学親の所在を補った。**これは研究・原著本文の粗い接続図であり、厳密な再帰的論理閉包や数学的独立監査PASSではない。** 旧版の資料数・未対応数は履歴として保持。

> **新しい整理方針（2026-11-09）：** [**PR #1854 現行作業入口：R3-07(row393)／R2-01の2本だけ**](PR1854-START-HERE.md)。以下の6章・99管理IDは参考索引であって、独立した移植対象ではない。現行数学結果へ至る不可欠な親のみGitHubで追い、計算証拠は後回し。以前の130本文を進捗率の分母に使わない。

**最新移植スナップショット（2026-11-09）**：新たな親原著・R0採否本文**60件**を[最新出典台帳](ACTIVE-ANCESTOR-SOURCE-MAP.json)へ収載。既存24件の文字列照合とは別集団。未対応識別子**7**は[役割別に仕分け](ACTIVE-PARENT-TRIAGE-AND-REPLAY-GATES.md)し、必須定理7本とは数えない。S316の[最小script＋期待JSONと実行結果照合](proofs/active-ancestors/S316-replay/README.md)はPASS（有限再演算のみ）。数学的独立監査と移植全体は未完了。

2026-11-09 JST。主要な成果・証明の流れ・成立条件・監査状態・重要な障壁を、次の六つのまとまりで読む。六つは説明上の区分であり、独立定理数ではない。全99管理IDの原文は既存の[索引](../CATALOGUE.md)に残す。

| 主要なまとまり | 最終的に分かっていること | 残る核心 |
|---|---|---|
| [1. 元のWard軌道とcanonical整数源](01-canonical-source.md) | C195の正しい補平方からGaussian・役割・POINTを再構成。現行帯では四根とQ無限商も継承 | 同じ元軌道の大域補平方の排除・有効全分類 |
| [2. MID/HIGHの真正四TOP質量](02-mid-high.md) | C189採択の全基底155/197下界。全PROPER・ordinary βを保持 | 同じ対象への相関上界 |
| [3. LOWの元source排除](03-low-exclusions.md) | ±18、列挙されたWard3/5/7の指数、+30の対象限定排除 | 9絶対指数・16 signed枠の全基底処理 |
| [4. −30のSelmer・類群](04-minus30.md) | 条件付き排除、主関係の追加と形式残余181 | 無条件の全尽生成・階数上界。row393原典照合 |
| [5. 逆写像・補助幾何・局所法の障壁](05-geometry-local.md) | 原始ρの厳密逆判定、固定曲線の成果、有限局所検査の限界 | 元の同じ点への写像と大域的な空性 |
| [6. 横断ルートの対象と量化子](06-cross-lane.md) | P23分担、固定指数の有限性、indexedとwideの区別 | 全域閉鎖に必要な命題のままOPEN |

各本文は元の証明・監査・管理索引へ直接つながる。中央原証明C195・R2の155/197・C241の3件に加え、直接前提11件、S270/C181/R5-C212/S264/C196〜C200の20件に、C183/R5-C220/R5-C224訂正/R5-P112の4件を追加保存した（追加の資料本文24件、うち追加の原証明22件・訂正/履歴資料2件。旧中央3件と合わせ主要原証明25件）。原著本文には当時のPENDINGやNEXTも残るため、現在の成立条件・訂正・監査範囲は上の整理本文を先に読む。[出典対応](SOURCES.json)は取得方式・原資料の更新日時・本文ハッシュを記録する。native Docsからの論理的テキスト抽出と、元ZIPのバイトを混同しない。

研究はrow393で停止。無条件−30・全LOW・Branch BはOPENで、row393はSOURCE_THEOREM_VERIFICATION_PENDING。今回の公開整理は新研究・新規独立監査・正式採択ではない。正式V74のMAIN-STATEは別の保持された権威であり変更しない。

[C195の11直接前提の原証明](C195-DEPENDENCIES.md)は取得・収載済み。ただし[完了チェックリスト](MIGRATION-COMPLETION-CHECKLIST.md)に残るP112の整数集合差の再構成は済んだが、S270/C189、C196〜C200の論理対応は記録照合済み。24件の本文テキスト一致とS240ネイティブ2表の修復は完了。親数学証明の全面独立検査は未了。以前の移植完了表示は訂正する。今回の点検は公開内容の転記・案内・条件表示を対象とし、独立数学監査ではない。全資料・全99ID本文・深い親証書の追加コピーは完了条件にしない。[PR #1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)はドラフトで保持し、mainへのマージは行わない。

[全体入口](../README.md) · [既存5資料群](../../materials/README.md) · [移植進捗](../../materials/MIGRATION-STATUS.json)

[追加24資料の対応map](PRIMARY-SOURCE-MAP.json) · [移植完了要件・未完了事項](MIGRATION-COMPLETION-CHECKLIST.md)

[旧P112→現行LOW残9絶対/16 signedの出典接続](P112-RESIDUAL-RECONCILIATION.md)

[四TOPとC189の成立条件・採否照合](S270-C189-SCOPE-CROSSCHECK.md) · [C196〜C200の適用範囲・失効NEXT照合](C196-C200-DEPENDENCY-REVIEW.md)

### 追補検証（2026-11-09）

[24原資料テキスト一致・S240表修復](NATIVE-DOCS-FIDELITY-REVIEW.md) · [親証明の実際に独立検算した初等範囲と未監査範囲](MAJOR-PARENT-MATH-PAPER-CHECK.md) · [row393引用定理の一次原文照合ゲート](ROW393-PRIMARY-THEOREM-GATE.md)。一次文献が未確認のため、row393のB<2^94を**原典照合まで完了した無条件類代表定理**と断定しない。PRはdraft、移植全体の完了判定は保留。

## 現行のユーザー指定：必須証明鎖はGitHubで自己完結（2026-11-09）

[必要数・収載数・当時の未対応13候補の歴史台帳](ACTIVE-PROOF-SPINE-COVERAGE.md)を基準とする。現在の直接中核は56論点／原証明本文55件相当、明記された別の親証明少なくとも7件も収載。ただし親証明鎖は未閉鎖。Google Drive参照のみでよいのは障壁・失敗ルート・歴史・重複等であり、現行結果の論理的に不可欠な親補題はGitHub本文と最小限証書へ対応づける。

## 現行証明鎖の親補題・採否34資料をGitHubへ追加（2026-11-09：履歴）

[最新数学依存表（新34件・未対応候補12識別子）](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md)と[出典・blob SHA・親関係JSON](ACTIVE-ANCESTOR-SOURCE-MAP.json)。最初の13候補、直接親11件、上流10件（S194/195/196、S213/218、S228/229、S235、S275、S318）を本文収載済み。34件は数学的に独立した34新定理ではなく、採否・限定的結果も含む。S255は管理CURRENTから完全数学CARDへ修正、S243のネイティブ表12セルを復元。

[旧24件のテキスト忠実性検査](NATIVE-DOCS-FIDELITY-REVIEW.md)はその24件の24/24一致のみを保証し、新34件へ外挿しない。残る12識別子の必須性・重複判定、S252 Bérczes・S196 quartic・row393 de la Maza原典、不可欠な有限計算証拠と独立数学監査はPENDING。Branch B・−30無条件排除・全LOWはOPEN。研究row393停止、PR #1854 draft未マージ。


## 最新追補（60件版、2026-11-09）

34件を出発点に直接・上流の26親原著を追加し、S289/S290は既存本文で対応した。[source map](ACTIVE-ANCESTOR-SOURCE-MAP.json)および[依存表](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md)を現行とする。旧34件時点の12識別子は履歴で、現在の未対応候補は[別紙の7識別子](ACTIVE-PARENT-TRIAGE-AND-REPLAY-GATES.md)。計算はS316のみ新たなstandalone replay PASS、他は未照合。独立数学監査・外部定理の仮定/正規化は未了、row393停止・PR draft/未マージ。
