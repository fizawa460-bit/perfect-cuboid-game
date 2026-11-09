# Stage35EX 主要成果の移植完了要件と未完了チェック

> **PR #1860 第２周の現行判定**。R3-07・R2-01の固定範囲はA〜E全PASS。必要な著者原著の未収載０件、外部原典の未照合０件。[終了判定表](PR1860-SECOND-PASS-EXIT-CHECKLIST.md) · [外部２件の原典照合](PR1860-GATE-D-TWO-EXTERNAL-PRIMARY-AUDIT.md) この表の主要６区分全体の移植・独立数学監査は別範囲。

**第１周の60件版（履歴）**。親原証明・採否本文は**60件追加**、当時の要仕分けは**7識別子**（必須定理数とは別）。以下の24/24本文一致は従来の24件だけを対象とする。追加検証：24本文テキスト一致、S240の2 native表復元。親数理は当時の部分PASS。主要6まとまりの説明、既存5詳細資料群、既存3中央原証明に加え、Google Driveから重要な原証明・訂正・履歴テキスト24本を新たに保存した。全99管理ID本文、**現行結果を導かない**深い旧親証書、途中版、生ログの全数複製は完了要件から除外する。**現行結論に数学的に不可欠な親証明は深くてもGitHub内で追跡可能にする。**

## 移植完了の定義

1. 六ルートについて最終結論・対象の量化子・成立条件・条件付き/暫定/撤回/OPEN・監査範囲・重要な障壁が整合する。
2. 中心結論に必要な原証明と、その結論が実際に引用する親補題を再帰的にGitHub本文から辿れ、最低限の計算証書・入力をGitHubから復元できる。障壁・旧失敗・履歴だけDrive参照可。旧命題が重複ならリンクを使う。
3. C195で再証明する部分と旧S268/S269/C174/S289/S290依存の部分、R1-223の訂正、S270定義の前提を区別する。
4. LOW残9絶対/16 signedのP112導出と、MID/HIGH 155/197のTRUE/PROPER定義を原資料から辿れる。
5. C196〜C200を現行C195の条件と接続し、弱い補助曲線から実際のsigned元点への無根拠な推論をしない。
6. 収載元ID→GitHub本文→依存先が検証でき、レビュー後に初めて移植完了を宣言する。正式研究採択・数学的独立監査とは別。

## 既存第1群の実移植24本（24/24文字列照合の対象・履歴）

| 証明 | 支える部分 | GitHub原著テキスト | 現時点 |
|---|---|---|---|
| S233 | C195 rederives common-numerator subset | [本文](proofs/C195-upstream/S233.md) | TEXT_RETAINED / semantic review pending |
| S237 | C195 rederives formal-depth subset | [本文](proofs/C195-upstream/S237.md) | TEXT_RETAINED / semantic review pending |
| S240 | C195 uses original duplication adapter | [本文](proofs/C195-upstream/S240.md) | TEXT_RETAINED / semantic review pending |
| S268 | C195 inherits reduced primitive norm | [本文](proofs/C195-upstream/S268.md) | TEXT_RETAINED / semantic review pending |
| S269 | C195 inherits Gaussian quartic/signed POINT | [本文](proofs/C195-upstream/S269.md) | TEXT_RETAINED / semantic review pending |
| R1-223 | correction: no arbitrary role factorization | [本文](proofs/C195-upstream/R1-223.md) | TEXT_RETAINED / semantic review pending |
| R1-228 | fourth-power normal form | [本文](proofs/C195-upstream/R1-228.md) | TEXT_RETAINED / semantic review pending |
| C174 | uniform height and role context | [本文](proofs/C195-upstream/C174.md) | TEXT_RETAINED / semantic review pending |
| S289 | global four-root lift | [本文](proofs/C195-upstream/S289.md) | TEXT_RETAINED / semantic review pending |
| S290 | large-index same-Q infinity context | [本文](proofs/C195-upstream/S290.md) | TEXT_RETAINED / semantic review pending |
| C194 | generic auxiliary no-map barrier | [本文](proofs/C195-upstream/C194.md) | TEXT_RETAINED / semantic review pending |
| S270 | four TRUE TOP plus all PROPER ordinary β definitions | [本文](proofs/foundations/S270.md) | TEXT_RETAINED / semantic review pending |
| C181 | P112 / residual precursor | [本文](proofs/foundations/C181.md) | TEXT_RETAINED / semantic review pending |
| R5-C212 | signed-index domain projection | [本文](proofs/foundations/R5-C212.md) | TEXT_RETAINED / semantic review pending |
| S264 | mod8/sign obstruction | [本文](proofs/foundations/S264.md) | TEXT_RETAINED / semantic review pending |
| C196 | degree-8 correspondence | [本文](proofs/post-C195/C196.md) | TEXT_RETAINED / semantic review pending |
| C197 | kernel/descent | [本文](proofs/post-C195/C197.md) | TEXT_RETAINED / semantic review pending |
| C198 | boundary/Prym dual4 | [本文](proofs/post-C195/C198.md) | TEXT_RETAINED / semantic review pending |
| C199 | actual-index height comparison | [本文](proofs/post-C195/C199.md) | TEXT_RETAINED / semantic review pending |
| C200 | dual4 original signed POINT cover | [本文](proofs/post-C195/C200.md) | TEXT_RETAINED / semantic review pending |
| C183 | R0 C183、signed +12従属採択 | [原文](proofs/foundations/C183.md) | CORRECTED_FORMULA_CONTROLS |
| R5-C220 | signed +12 HIGHの元証明 | [歴史的原文](proofs/foundations/R5-C220.md) | ERRATUM_REQUIRED |
| R5-C224-erratum | C220の正規化曲線のX欠落を訂正 | [訂正文](proofs/foundations/R5-C224-erratum.md) | AUTHOR_CORRECTION |
| R5-P112 | 旧三マスクの有限指数再bin | [歴史的報告](proofs/foundations/R5-P112-rebin.md) | COUNTS_HISTORICAL_ONLY |

原文は歴史的状態のまま残す。raw/Docs抽出の出典・blob SHAは[PRIMARY-SOURCE-MAP.json](PRIMARY-SOURCE-MAP.json)。新しい数学的除外や敵対的監査は生じない。

[旧P112のLOW36/MID9から現行LOW9絶対/16 signedへの集合差の独立再計算](P112-RESIDUAL-RECONCILIATION.md)は完了し、[標準Python検算](tools/verify_p112_residual.py)を保存した。これは整数集合の照合であって、親マスクの数学的独立監査ではない。

## ルート別の論理的残作業

| 主要区分 | 既収載の証拠・今回の追加 | なお必要な照合 |
|---|---|---|
| 元Ward/canonical source | C195と直接前提11本 | [C196–C200の論理依存レビュー](C196-C200-DEPENDENCY-REVIEW.md)済。C195と旧S268/S269/C174/S289/S290は親証明依存であり、独立数学再監査は未実施 |
| MID/HIGH | R2の155/197原文、C189採否のリンク、S270本文 | [定義・量化子・C189採否の照合](S270-C189-SCOPE-CROSSCHECK.md)済。旧S270/R2の親高さ計算を独立再実行したわけではない |
| LOW | row367/368/369/376の証明・監査とC181/R5-C212/S264本文 | **P112集合差の再構成は完了**。上記の独立整数再binとR0 C183＋C220/C224の符号補正を参照。親マスクの全称数学証明は依存を保持 |
| −30 | row381, row385〜393の原文・監査・証拠 | row393のde la Maza原典適用は[D-1 PASS](ROW393-PRIMARY-THEOREM-GATE.md)。Cl/2全尽生成と無条件−30排除は未証 |
| 逆写像・幾何 | C241とC194、C196〜C200全本文 | exact actual signed POINTとPrym/dual4の適用範囲および失効したNEXTを精査 |
| 横断ルート | 99管理ID索引と5資料群 | original indexed vs wide vs physical、formal adoptionと仮採択・条件付きの区別を点検 |

## 移植完了を宣言する前のゲート

- P112の独立整数再binは完了。残る検査は元マスクの正確な適用条件・歴史的採否を全経路で照合すること。
- [収載数の新基準と未対応13候補](ACTIVE-PROOF-SPINE-COVERAGE.md)に従い、C175/C185、S243〜S267の現在実際に使う親補題とC189採否をGitHub内で接続する。外部障壁のみはDrive参照可。
- C196〜C200およびS270/C189の**記録上の依存条件・量化子・失効NEXT照合は完了**。残るのは個々の代数計算・親前提の全面数学監査（[限定数学検査](MAJOR-PARENT-MATH-PAPER-CHECK.md)では初等恒等式・端点のみPASS）。
- [24資料の同一抽出方式によるテキスト比較24/24 PASS](NATIVE-DOCS-FIDELITY-REVIEW.md)。S240の2ネイティブ表（全24セル）は復元。Google Docsの全視覚書式・数式レンダリングの原物同一性は別問題。
- [row393 de la Mazaの原典Theorem 1＋系の仮定・t0係数照合](ROW393-PRIMARY-THEOREM-GATE.md)は第２周でPASS。研究はrow393で停止。Branch B、Stage35、E1、無条件−30、全LOWはOPEN。
- [PR #1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)は第１周の記録。R3-07・R2-01の第２周は冒頭の終了判定表を参照。

[主要ルートREADME](README.md) · [C195依存](C195-DEPENDENCIES.md) · [原文出典map](PRIMARY-SOURCE-MAP.json) · [5詳細資料群](../../materials/README.md)

[移植本文の忠実性レビュー](NATIVE-DOCS-FIDELITY-REVIEW.md) · [親数学の限定再検算](MAJOR-PARENT-MATH-PAPER-CHECK.md) · [row393引用定理の原典照合](ROW393-PRIMARY-THEOREM-GATE.md)

[現行証明鎖の旧棚卸し（未対応13は追補で収載）](ACTIVE-PROOF-SPINE-COVERAGE.md)

## 続きの移植（2026-11-09：34件版の歴史記録）

旧未対応13件・直接親11件・追加の上流10件を合わせて**34件の原証明・採否本文**をGitHubに収載済み。[出典とblob SHA](ACTIVE-ANCESTOR-SOURCE-MAP.json)・[数学依存表](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md)を最新版とする。上流10件はS194/195/196、S213/218、S228/229、S235、S275、S318。S243のネイティブ表12セルをMarkdownへ復元。S255は数学CARDを採用、旧管理CURRENTを別保存。

**残る12識別子**：C160、EXTERNAL_BERCZES_THM2_1、EXTERNAL_FERMAT_QUARTIC、S193、S202、S227、S230、S234、S242、S250、S316、SECTION16_NONSQUARE。これは「必須定理が12本足りない」という意味ではない。必要な親を先に区別し、等価証明が既存GitHub本文にあれば重複追加しない。S230監査、S242固定基底例、S250の再述はDrive参照のみでよい可能性がある。

未完了ゲート：必要親の再帰的完結性、S252 Bérczes・S196古典quartic・row393 de la Maza定理の原典条件、証明を支える最小計算コード・入力・期待結果、独立数学監査。**従来24件の文字列照合PASSは新34件の文字列照合PASSではない。** 新数学信用0、完了率未確定、PR draft/未マージ。

## 第１周の完了ゲート判定（60件版、履歴）

- **本文移植**：旧24原文の24/24文字列照合、追加親/採否本文60件のGitHub保存とblob SHA台帳化。元の56中核論点/55本文相当の初期棚卸しと重複するため、独立命題数や必要総件数は計算しない。[最新source map](ACTIVE-ANCESTOR-SOURCE-MAP.json)。
- **依存親の再帰閉鎖**：未完了。[数学依存表](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md)と[未対応7識別子の役割分類](ACTIVE-PARENT-TRIAGE-AND-REPLAY-GATES.md)。S289/S290は既存GitHubを再利用。古いS120はBranch Aの障壁・parkでありS121の元quotient数学親ではないためDriveリンクで十分。
- **最小有限計算**：S316 standaloneスクリプトと原期待JSONを収載し実行、5,384バイト一致PASS。[再現手順](proofs/active-ancestors/S316-replay/README.md)。他の独立計算は依然マッピング未完了、実行PASSを発行しない。
- **数学・外部原典ゲート**：S252のBérczes、S196のPLUS四乗降下、Section16 nonsquare、C185のC160 gcd条件、row393 de la Maza Theorem 1＋系の正規化を独立照合するまでPASSにしない。形式181次元と真Cl/2を混同しない。
- **全体**：移植NOT_COMPLETE、完了率NOT_COMPUTABLE、新規研究定理認定0、研究row393停止、PR #1854 draft未マージ、main/Drive研究正本は変更なし。
