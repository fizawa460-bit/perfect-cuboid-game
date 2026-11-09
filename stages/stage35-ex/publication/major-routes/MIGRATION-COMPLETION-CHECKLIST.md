# Stage35EX 主要成果の移植完了要件と未完了チェック

**判定：PARTIAL / NOT_COMPLETE（2026-11-09、PR #1854 draft）。** 主要6まとまりの説明、既存5詳細資料群、既存3中央原証明に加え、Google Driveから重要な原証明・訂正・履歴テキスト24本を新たに保存した。全99管理ID本文、深い親証書、途中版、生ログの全数複製は**完了要件から除外**する。

## 移植完了の定義

1. 六ルートについて最終結論・対象の量化子・成立条件・条件付き/暫定/撤回/OPEN・監査範囲・重要な障壁が整合する。
2. 中心結論の証明に実質必要な原証明がGitHub本文として読め、旧命題が重複ならリンクを使う。
3. C195で再証明する部分と旧S268/S269/C174/S289/S290依存の部分、R1-223の訂正、S270定義の前提を区別する。
4. LOW残9絶対/16 signedのP112導出と、MID/HIGH 155/197のTRUE/PROPER定義を原資料から辿れる。
5. C196〜C200を現行C195の条件と接続し、弱い補助曲線から実際のsigned元点への無根拠な推論をしない。
6. 収載元ID→GitHub本文→依存先が検証でき、レビュー後に初めて移植完了を宣言する。正式研究採択・数学的独立監査とは別。

## 今回の実移植24本

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
| −30 | row381, row385〜393の原文・監査・証拠 | row393のde la Maza原典定理照合がPENDING、Cl/2全尽生成は未証。指数−30はOPEN |
| 逆写像・幾何 | C241とC194、C196〜C200全本文 | exact actual signed POINTとPrym/dual4の適用範囲および失効したNEXTを精査 |
| 横断ルート | 99管理ID索引と5資料群 | original indexed vs wide vs physical、formal adoptionと仮採択・条件付きの区別を点検 |

## 移植完了を宣言する前のゲート

- P112の独立整数再binは完了。残る検査は元マスクの正確な適用条件・歴史的採否を全経路で照合すること。
- C196〜C200およびS270/C189の**記録上の依存条件・量化子・失効NEXT照合は完了**。残るのは個々の代数計算・親前提の数学的監査、原著の数式/表表示忠実性の確認。
- GitHubに残した24本文の改行・数式・表の抽出漏れ確認と経路リンクの実在チェック。
- 研究はrow393で停止、Branch B/Stage35/E1/無条件−30/全LOWはOPEN。row393 SOURCE_THEOREM_VERIFICATION_PENDINGのまま。99ID索引は全99原文の収載を意味しない。
- PR #1854はdraft/open、mainへはマージしない。新しいPRも作らない。

[主要ルートREADME](README.md) · [C195依存](C195-DEPENDENCIES.md) · [原文出典map](PRIMARY-SOURCE-MAP.json) · [5詳細資料群](../../materials/README.md)
