# Stage35EX：row393到達ルートの数学的親証明対応表（2026-11-09）

**対象は現行の結論を導く論証の実際の親補題**。失敗ルート・障壁のみの記録・旧NEXTはDrive参照を許す。数学的主張の独立再監査を今回追加するものではない。研究本体はrow393停止、Branch B OPEN、PR #1854 draft/unmerged。

## 本日の追加：24原証明/採否本文をGitHubに保存

前回の未対応13件（S243, S251–253, S259–262, S265, S267, C175/C185/C189）をすべて出典IDから本文取得し、新たに見つかった直接数学的親11件（S219–221, S231–232, S254–258, S266）も保存した。

- S243のGoogle Docsネイティブ表1件・**12セル**はセル単位でMarkdown表へ復元。旧S240の2表24セルとは別。
- **S255は重要な訂正**：旧GitHub `S255.md` は原稿 `SECTION255-CURRENT.md`（管理用抜粋）だった。[原論証CARD](proofs/active-ancestors/S255.md)を正式な数学本文のリンクとし、[旧CURRENT](proofs/active-ancestors/S255-current.md)は歴史資料として保持。誤った全文収載認定を防ぐ。
- S265はタイトルにBARRIERとあるが、実際に使用する **odd signed `ε=+1` と全指数のformal-unit lemma**を含むので本文必須。有限素数フィルタ単独では不在証明にならない。
- C175/C185/C189は統合/採否本文であり、新たな3独立定理ではない。C189はR2の155/197を`ACCEPT_DEPENDENT_UNIFORM_THRESHOLD_EXTENSION`とする歴史的なR0採否。条件は現行のR2本文/主要ルート解説を優先。

## 現行結果の主要依存経路

```text
signed source C195 ──> four-root/physical Kummer S243
                 └──> S232+S233+S237 denominator, roles and local order
S219 -> S220 -> S221 (point-only local H/Pell math)
                            -> S258 actual critical H
S232,S243,S251,S253 -> S254 -> S255(CARD) -> S256 -> S257 -> S258
S258+S252/S256 -> S259 -> S260 -> S261 -> S262 (LIMIT: nonobstruction)
S263+S264 -> S265 (odd ε=+1) -> S266 (even depth)
S259/S260/S266 and above actual-source adapters -> S267 -> S270
C174+C175, C185 -> R2 uniform 155/197 -> C189 dependent R0 adoption
row367/368/369/376 + C181/R5-C212/S264/C183 -> LOW 9 abs /16 signed
row370..384 -> row385..393 -> 105-degree class-group/formal181
```

線は「代表的に先行する入力」の図であり、個々の完全な有向非巡回グラフは下の表/機械台帳の`parents`を参照。並列する同じ補題の別ルート、後の訂正、何も加えないnonobstructionは**新規 saving と数えない**。

## 追加した原著と上流入力

| 証明/採否 | 重要な内容・適用先 | 著者が依存する親 | GitHub本文 |
|---|---|---|---|
| S219 | local H/Pell point-only approximation; old scalar dQ=mP is NOT imported | **S213（未対応）**、**S218（未対応）** | [原文](proofs/active-ancestors/S219.md) |
| S220 | one higher H/Pell deformation coefficient | [S219](proofs/active-ancestors/S219.md) | [原文](proofs/active-ancestors/S220.md) |
| S221 | all-H coefficient D=1/(4t0^2) and local-centers lemma | [S219](proofs/active-ancestors/S219.md)、[S220](proofs/active-ancestors/S220.md) | [原文](proofs/active-ancestors/S221.md) |
| S231 | complete physical source direct square denominator and parity | **S194（未対応）**、**S195（未対応）**、**S196（未対応）**、**S228（未対応）**、**S229（未対応）** | [原文](proofs/active-ancestors/S231.md) |
| S232 | b>1; all denominator primes outside 2ABC; ord(Pbar)=4h where h//n/ odd quotient | [S231](proofs/active-ancestors/S231.md)、**S230（未対応）**、**S228（未対応）**、**S229（未対応）** | [原文](proofs/active-ancestors/S232.md) |
| S243 | global common-c four roots and true Q Kummer class (not finite-base emptiness) | **S235（未対応）**、[S237](proofs/C195-upstream/S237.md)、**S242（未対応）** | [原文](proofs/active-ancestors/S243.md) |
| S251 | all denominator H/good primes; local 2-half and order 8 | [S232](proofs/active-ancestors/S232.md)、[S233](proofs/C195-upstream/S233.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、**S250（未対応）** | [原文](proofs/active-ancestors/S251.md) |
| S252 | effective base-dependent H-supported bound, not source exclusion | [S232](proofs/active-ancestors/S232.md)、[S237](proofs/C195-upstream/S237.md)、[S240](proofs/C195-upstream/S240.md)、[S251](proofs/active-ancestors/S251.md)、**EXTERNAL_BERCZES_THM2_1（未対応）** | [原文](proofs/active-ancestors/S252.md) |
| S253 | two compulsory roles and same order2 signature at H | [S232](proofs/active-ancestors/S232.md)、[S233](proofs/C195-upstream/S233.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md) | [原文](proofs/active-ancestors/S253.md) |
| S254 | seed2/3 actual orbit odd-multiple denominator propagation | [S232](proofs/active-ancestors/S232.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md) | [原文](proofs/active-ancestors/S254.md) |
| S255 | arbitrary-seed gcd and Pell H-support; CARD replaces management CURRENT | [S232](proofs/active-ancestors/S232.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S254](proofs/active-ancestors/S254.md) | [原文](proofs/active-ancestors/S255.md) |
| S256 | H-entry beta exact valuation and height normalization | [S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S254](proofs/active-ancestors/S254.md)、[S255](proofs/active-ancestors/S255.md) | [原文](proofs/active-ancestors/S256.md) |
| S257 | Pell comparison precision/deep exception receiver | [S219](proofs/active-ancestors/S219.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S254](proofs/active-ancestors/S254.md)、[S255](proofs/active-ancestors/S255.md)、[S256](proofs/active-ancestors/S256.md) | [原文](proofs/active-ancestors/S257.md) |
| S258 | actual critical H definition via local next-digit, two roles | [S219](proofs/active-ancestors/S219.md)、[S220](proofs/active-ancestors/S220.md)、[S221](proofs/active-ancestors/S221.md)、[S253](proofs/active-ancestors/S253.md)、[S255](proofs/active-ancestors/S255.md)、[S256](proofs/active-ancestors/S256.md)、[S257](proofs/active-ancestors/S257.md) | [原文](proofs/active-ancestors/S258.md) |
| S259 | rolewise PROPER height and EQUAL first-entry critical | [S252](proofs/active-ancestors/S252.md)、[S256](proofs/active-ancestors/S256.md)、[S258](proofs/active-ancestors/S258.md) | [原文](proofs/active-ancestors/S259.md) |
| S260 | full GOOD-or-critical TOP entry height | [S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S254](proofs/active-ancestors/S254.md)、[S256](proofs/active-ancestors/S256.md)、[S258](proofs/active-ancestors/S258.md)、[S259](proofs/active-ancestors/S259.md) | [原文](proofs/active-ancestors/S260.md) |
| S261 | exact GOOD TOP Kummer role neutrality | [S232](proofs/active-ancestors/S232.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S253](proofs/active-ancestors/S253.md)、[S258](proofs/active-ancestors/S258.md)、[S260](proofs/active-ancestors/S260.md) | [原文](proofs/active-ancestors/S261.md) |
| S262 | local inverse nonobstruction (NOT proof of emptiness) | [S240](proofs/C195-upstream/S240.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S260](proofs/active-ancestors/S260.md)、[S261](proofs/active-ancestors/S261.md) | [原文](proofs/active-ancestors/S262.md) |
| S265 | odd signed epsilon=+1, formal-unit lemma; finite-prime barrier is separate | [S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S263](../../materials/original-source-exclusions/parents/S263.md)、[S264](proofs/foundations/S264.md)、[S260](proofs/active-ancestors/S260.md)、[S261](proofs/active-ancestors/S261.md)、[S262](proofs/active-ancestors/S262.md) | [原文](proofs/active-ancestors/S265.md) |
| S266 | period depth and even valuation/primitive-family negative control | [S263](../../materials/original-source-exclusions/parents/S263.md)、[S265](proofs/active-ancestors/S265.md) | [原文](proofs/active-ancestors/S266.md) |
| S267 | H-norm crowding, unconditional integer bound within full original packet | [S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S259](proofs/active-ancestors/S259.md)、[S260](proofs/active-ancestors/S260.md)、[S261](proofs/active-ancestors/S261.md)、[S262](proofs/active-ancestors/S262.md)、[S263](../../materials/original-source-exclusions/parents/S263.md)、[S264](proofs/foundations/S264.md)、[S265](proofs/active-ancestors/S265.md)、[S266](proofs/active-ancestors/S266.md) | [原文](proofs/active-ancestors/S267.md) |
| C175 | R0 cross-lane integration; subset of retained uniform height constant and dedup | [C174](proofs/C195-upstream/C174.md)、[S263](../../materials/original-source-exclusions/parents/S263.md)、[S265](proofs/active-ancestors/S265.md) | [原文](proofs/active-ancestors/C175.md) |
| C185 | R0 scoped sparse TOP coefficient acceptance/dedup | **C160（未対応）**、[S268](proofs/C195-upstream/S268.md)、**S275（未対応）**、**S318（未対応）** | [原文](proofs/active-ancestors/C185.md) |
| C189 | R0 ACCEPT_DEPENDENT_UNIFORM_THRESHOLD_EXTENSION and withdraw previous duplicates | [C175](proofs/active-ancestors/C175.md)、[C185](proofs/active-ancestors/C185.md)、[S270](proofs/foundations/S270.md)、[R2_UNIFORM_155_197](proofs/R2-uniform-thresholds.md) | [原文](proofs/active-ancestors/C189.md) |

## まだGitHub内で閉じていない親入力（15候補、必要数未確定）

未対応識別子：**C160、EXTERNAL_BERCZES_THM2_1、S194、S195、S196、S213、S218、S228、S229、S230、S235、S242、S250、S275、S318**。

正確な仕分けは次のとおり。

- **本文照合を優先**：S194/S195/S196（元sourceの上流）、S228/S229（S232のbad-prime局所入力）、S213/S218（S219のpoint-only数学入力）、S235（S243四根/étaleの祖先）、C160/S275/S318（C185の係数とH-interface）。これらは現存GitHub内で等価な原証明があるかの重複調査を先行する。
- **既存証明内で包含・歴史的役割の可能性**：S230はS228/229の監査、S242はS243中の固定(8,15,17)ケース、S250のgood-prime結論はS251で再叙述済み。現行の一般命題に不可欠な箇所だけを特定し、障壁や重複だけなら追加しない。
- **公刊定理・適用仮定**：S252が引用するBérczesほかのsuperelliptic S-integer theorem 2.1(i)は原典条件未照合。S267のfactor-free Hノルム圧縮はS252のその外部S-integer上界を**必須としていない**。独立してrow393のde la Maza Theorem1+系も原典照合PENDING。
- **計算再現性**：今回の24原著にはScript/Result IDがある。使っている有限演算の最小検証コードと期待値のGitHub対応はまだ全件完了していない。本文保管=有限計算の独立再現完了ではない。

## 本日時点の数え方

従来の中核は**56論点、原証明本文55件相当**。旧親本文で別に所在を確認した**少なくとも7件**も既存GitHubにある。今回新たに**24件の原証明・採否資料本文**を追加（旧S255 CURRENTは履歴として別保存）。したがって「先に未対応とされた13件」は本文収載という意味では **13/13対応付け済み**。ただし、新たに親入力15候補が出現しており、**必要総数・全体完了率は未確定**。重複する論証・採否カード・補助障壁を数学の独立定理として足し算しない。

[追加24件の機械出典・blob SHA](ACTIVE-ANCESTOR-SOURCE-MAP.json) · [従来の55本文＋親7＋未対応13の調査起点](ACTIVE-PROOF-SPINE-COVERAGE.md) · [移植完了チェック](MIGRATION-COMPLETION-CHECKLIST.md)
