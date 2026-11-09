# Stage35EX row393まで：現行証明鎖のGitHub収載数と未対応前提（2026-11-09）

> **2026-11-09追補：以下の旧「未対応13候補」は全13件の本文をGitHubへ追加しました。** 追加で11件の直接親（S219–221/S231–232/S254–258/S266）を発見・移植し、計24件の原著・採否を補完しました。現在の残課題は[新たな親15識別子の必要性/重複判定](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md)です。本文コピーと数学独立監査・計算コード全収載は別です。**旧13候補を未収載と誤読しないこと。**

## 依頼された厳密な新基準

**現行row393までに実際に利用して成立した命題**は、証明本文、重要な親補題、原条件、訂正/正式採否、結果の再現に不可欠なコードと入力を、第三者がGoogle DriveにログインせずGitHub上で辿れるようにする。途中で止まった試行、障壁だけの議論、旧NEXT、重複資料、無関係の深い旧親研究、全ログはGitHubには要約・出典リンクのみでよい。引用する通常の公刊数学定理は原典書誌と本件に使う正確な定理文・仮定を記述する（著作権のある論文全文の再配布は義務にしない）。

これは**前の「主要ルートと直近原証明だけ、深い親はDrive参照可」より強い公開条件**。既存の55本文の存在はこの新基準の完了を意味しない。数学的妥当性の独立再監査は「収載の完結性」とは別ゲート。

## 今回確認できた「すでにGitHubにある」本体：55本文相当

| 範囲 | 論点数 | distinct原文数 | GitHubの入口 | 限定 |
|---|---:|---:|---|---|
| C195、R2/C189、C241、C195直接前提11件、S270・LOW前段、C196〜C200、C183・R5-C220等の主要ルート | 25 | 25 | [主要ルート証明](README.md)・[24件map](PRIMARY-SOURCE-MAP.json) | C194/C241など障壁主体の文書も含むので「純粋に必須な25数学定理」とは呼ばない |
| LOW元source row367/368/369/376 | 4 | 4 | [第1群](../../materials/original-source-exclusions/README.md) | 条件付きの独立監査を保持 |
| 元−30のMW/Selmer row370–384（376を除く） | 14 | 14 | [第2群](../../materials/negative30-mw-selmer/README.md) | row377の原監査本文は未発見 |
| 同じ数体の類群・不同 row385–393 | 9 | 9 | [第3群](../../materials/classgroup-and-different/README.md) | row393の外部原典が未照合 |
| 固定±18の局所/全球基礎 row361–364 | 4 | 3 | [第4群](../../materials/selmer18-parent-chain/README.md) | 361と362は同じ証明本文。−30の105次体と混同しない |
| **直結の主題別計** | **56** | **55** | | **この55は最低限の中核数であり、全親証明の最終必要総数ではない** |

さらに、上の55件とは別に、[第1群](../../materials/original-source-exclusions/README.md)で名前とGitHubの本文パスを確認できる**少なくとも7件の上流原証明・親資料**（row365、row366、S263、C118、C35-11、C35-12、row339）が保存済み。重複を数えず、特定できた一次本文・主要親本文としては**少なくとも62件相当**。この7件を「独立定理7本」とは呼ばない。第4/第5群に他の旧親計算証書もあるが、個数・必須性を未分類なのでこの62に足さない。

## 今回見つかった、GitHubで専用本文がまだ対応づかない13候補

2026-11-09時点のGitHubツリー16,075エントリを対象に、Stage35EX由来の**名前からのファイルパス**を確認。等価な証明が別名やハッシュ名で保存されている可能性は残るので、以下は「未対応・未判定」であり「必ず欠落」「13本とも必須」とは断定しない。

| 候補 | 引継ぎ先で使う前提・状態 | Drive原資料 | 判断 |
|---|---|---|---|
| S243 | S270/S289が使う四根・元半点チャート | [原資料](https://docs.google.com/document/d/1Ms3kaCbsaZrIS_eCQJXmk2HWtJ5hI0yIEIp0PmxThAc/edit) | REQUIRED_LEMMA_VERIFY_SCOPE |
| S251 | 分母素数全体のKummer/節点H/order8 | [原資料](https://docs.google.com/document/d/1nvoy5SM71GANiWp1u9b1nMjyEE5awN1t2xa4eQJKcbE/edit) | REQUIRED_LEMMA_VERIFY_SCOPE |
| S252 | 高さ正規化・H支持・index下界 | [原資料](https://drive.google.com/file/d/1xXbdt9AD-HEdo2XmwIVRQ8ymY7_ahb5z/view) | REQUIRED_LEMMA_VERIFY_SCOPE |
| S253 | 両側分母/H次数衝突 | [原資料](https://drive.google.com/file/d/1oUW7fLzqqwPg-4qk8hnZilA05Zc4K2EH/view) | REQUIRED_LEMMA_VERIFY_SCOPE |
| S259 | PROPERの高さ・critical衝突; 選んだカードとCURRENTの正本照合要 | [原資料](https://docs.google.com/document/d/1PfTD6K1xBnULpNjhXrBGPTMB8vwtRolYT4GJMy5YW4I/edit) | REQUIRED_SOURCE_SELECTION_PENDING |
| S260 | full packetのGOODまたはcritical TOP高さ | [原資料](https://drive.google.com/file/d/1AaHYUY-rghdqWXcl8RlECG8RO8bUzo3m/view) | REQUIRED_LEMMA_VERIFY_SCOPE |
| S261 | GOOD TOPと役割独立Kummer | [原資料](https://drive.google.com/file/d/1-1srMWOjsR0K23xGy-Lmpmg0iNRdmqii/view) | REQUIRED_LEMMA_VERIFY_SCOPE |
| S262 | 四根boundary/formal inverseの適用限界 | [原資料](https://drive.google.com/file/d/1vX6MN2t91AT5fWtTDy-NHipYd6B8I34N/view) | REQUIRED_LEMMA_VERIFY_SCOPE |
| S265 | 有限素数paired squareclassの障壁; S270が使うodd/dyadic/full-unit補題は別原著の可能性 | [原資料](https://drive.google.com/file/d/1pAzUE_9pR5ICm4UUTK_uiYG5ihwTdUTC/view) | REVIEW_IF_BARRIER_ONLY |
| S267 | Hノルム容量・T0補正・joint TOP高さ | [原資料](https://drive.google.com/file/d/1Pg4vGCG1g_oXDYoerPEC5-gfGrucnNCL/view) | REQUIRED_LEMMA_VERIFY_SCOPE |
| C175 | R2の統一高さの古い親/C175 | [原資料](https://docs.google.com/document/d/1-PcT2I_liBMRBrOmUvkgM1Cd5PWw6rig4wz35IY-izs/edit) | REQUIRED_LEMMA_VERIFY_SCOPE |
| C185 | 旧sparse protected TOP係数とR0限定採否 | [原資料](https://docs.google.com/document/d/1udKxKN7DBwDla86i1pB7B1O500z5YMFlU3tu9HZCf5A/edit) | REQUIRED_ADOPTION_PROOF |
| C189 | 155/197のR0採否・成立条件 | [原資料](https://docs.google.com/document/d/10MNKZS2aWJ6rZVi1YxgIliuX9kxIJAPlY3EWwhf5d48/edit) | REQUIRED_AUTHORITY_RECORD |

**最優先の照合順序**：①R2のC175/C185とC189の採否、②S270の真の前提S243・S251/252/253・S259/260/261/262・S267、③S265が本当に親補題か障壁だけか、④C195/row393までのその他の数学的親証明が実際に必要なら再帰的に追加。元原文と等価なGitHub本文がすでにあればコピーせず直接リンクする。

**正確な必要総件数は未確定。** 現時点で確認済み中核55本文、追加で所在が確認できる親7本文、未対応候補13件。したがって「55/55完了」「62/75=82.7%完了」等の率は**禁止**。13件は補題の必須性と代替収載を調べてから必要分母に組み込む。

## 残る公開ゲート

- 各**現行結論→その根拠→それに必要な親補題**の逆向き依存を閉じる。とくにC175/C185/S243等を単なるDriveリンクで済ませない。
- 独立の有限計算を読者が検証できるよう、各証明に不可欠な入力・短い再現コード・結果をGitHubに固定する。数値グラフや失敗試行ログの完全移植は不要。
- [row393 de la Maza Theorem1+系](ROW393-PRIMARY-THEOREM-GATE.md)の原典の仮定・公式を確認し、使った命題の正確な形をGitHubに記録する。原論文全文を無断複製しない。
- [元資料忠実性監査](NATIVE-DOCS-FIDELITY-REVIEW.md)は新規24原資料で本文24/24一致、S240のネイティブ2表復元済み。これは親数学的証明の完全性を保証しない。
- 継続するopen事項：−30、LOW全体、Branch B、indexedとwide、Cl/2全尽性、形式181。新規無条件排除0。

**PR #1854はdraft・未マージ、研究はrow393で停止。Google Driveの現行正本やR0等の研究運用状態は変更しない。**

## 2026-11-09実作業による最新判定

[24件追加の数学的親補題・R0採否原著、条件付き参照と未対応15件を含む新正本表](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md)。初期13は13/13本文収載、追加11も収載済み。S255は管理CURRENTから数学CARDへ修復済み。今回の原証明追加は独立検証済み定理24件という意味ではない。現行の完結性は引き続きPARTIAL。
