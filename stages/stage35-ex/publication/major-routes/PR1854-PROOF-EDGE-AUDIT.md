# PR #1854｜2ルートの原著引用辺・不足親の整理（第2回）

**対象：R3-07（row393まで）とR2-01（C189採択まで）だけ。** 原著が実際に呼ぶ親を辿るための表。本文の存在・引用の確認と、数学的な依存の必須性・完全性は区別する。計算証拠は保留。

## 数学的に重要な接続

| 結果 | GitHubで確認できる引用・前提 | 判定 |
|---|---|---|
| R3 row393 | [row392の関係・不同](../../materials/classgroup-and-different/proofs/row393.md#L10) | 本文収載。原典de la Maza適用は未確認 |
| R3 ±18 row367 | [row364真Selmer・row365・row366](../../materials/original-source-exclusions/row367/REPORT.md#L36) | 本文収載、一部のさらに前の親を要判定 |
| R3 row368 Ward3/5 | [S321因子分解](../../materials/original-source-exclusions/row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md#L36)＋C118 | **S321の完全数学原著が未対応** |
| R3 row369 Ward7 | [S321・S322のK/L分割](../../materials/original-source-exclusions/row369/STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER_20261106.md#L65) | S321未対応、S322の既存本文同値性要判定 |
| R3 +30 row376 | [row370/374/375](../../materials/original-source-exclusions/row376/PROOF.md#L37) | 本文収載、−30排除には使えない |
| R3 −30 row381 | [row373–375の真正算術](../../materials/negative30-mw-selmer/row381/PROOF.md#L45) | **GRH条件付き**排除、無条件へ昇格不可 |
| R2 C189 | [C175・C185係数](proofs/active-ancestors/C189.md#L17)、[C187の155/197](proofs/R2-uniform-thresholds.md#L46) | **下界**であり、R2目標の相関上界はOPEN |
| R2 C185 | [C160・S268・S275・S318](proofs/active-ancestors/C185.md#L24) | C160の補題同値性が未判定 |
| R2 S232 | [S230のA/C素点付値](proofs/active-ancestors/S232.md#L61) | **S230原著か同値証明が未対応** |
| R2 S251 | [S250のgood分母次数8を再述](proofs/active-ancestors/S251.md#L45) | 重複アップ不要の候補、本文の完全性を後で判定 |
| R2 S243 | [S242の固定基底rank2例](proofs/active-ancestors/S243.md#L42) | 固定例のみ。全基底四根定理の必須親と自動計上しない |

このほか原著本文にある引用辺 **計39件のsource行番号つき記録**は[機械可読台帳](PR1854-PROOF-EDGE-AUDIT.json)に保存した。39は必須定理数・不足ファイル数ではない。

## 残る検討ゲート（11識別子、11ファイルの不足ではない）

| ルート | 識別子 | 次の判定 |
|---|---|---|
| R3-07 | S238 | MISSING_MATH_PARENT_OR_EQUIVALENT：S321/C118 original dyadic squareclass |
| R3-07 | S321 | MISSING_MATH_PARENT_OR_EQUIVALENT：row368/369 Ward3/5/7 factorization |
| R3-07 | S322 | EQUIVALENT_PROOF_CHECK：row369 K/L split |
| R3-07 | row351/352 | IN_REPO_JSON_PROOF_LINKAGE：row364 true/fake Selmer |
| R3-07 | EXTERNAL_DE_LA_MAZA | EXTERNAL_PRIMARY_THEOREM_UNCHECKED：row393 norm bound |
| R2-01 | C160 | EQUIVALENT_PROOF_CHECK：C185 exact gcd / S268 first-entry |
| R2-01 | S230 | MISSING_MATH_PARENT_OR_EQUIVALENT：S232 rank-independent A/C local valuation |
| R2-01 | EXTERNAL_BERCZES_THM2_1 | EXTERNAL_PRIMARY_THEOREM_UNCHECKED：S252 height theorem |
| R2-01 | S242 | FIXED_EXAMPLE_SCOPE_ONLY：S243 (8,15,17) rank2 example |
| R2-01 | S250 | IN_REPO_RESTATEMENT_CHECK：S251 explicitly reiterates original order8 theorem |
| COMMON | SECTION16_NONSQUARE | SOURCE_UNKNOWN_CHECK_ROOT_RELEVANCE：S194 source nonsquare lemma |

R3ではS321・S238とrow351/352、R2ではC160・S230の同値証明確認が優先。外部de la Maza/Bérczesは定理原典の**仮定・適用式**が必要だが、論文全文の転載を求めない。

## 前回58リンクの補足：既にGitHubにある旧数学本文10件

R3の現在のLOW残数・+12と訂正を説明する **C181、C183、R5-C220、R5-C224、S264、R5-C212**、R2の高さ・共通親に使う **C174、R1-228**、祖先の引用を照合する **S232、S194**。10件はすでにGitHubに存在し、追加アップロードしない。前回の58参照とは別なので、既存参照の候補は**68パス**。68は必須総数ではない。

**結論：** 参照文書の整理は前進したが、二つの証明鎖の必須数学親の再帰的完結は未証明。必要総数・不足件数・進捗率はまだ算定しない。旧130本文やR1〜R5全原文調査を分母に戻さない。研究停止、PRドラフト未マージを保持。
