# Stage35EX row393：現行数学的証明鎖の依存グラフと親本文（2026-11-09）

**現在の状態：初期34件、親5件、上流9件、さらに上流6件、finite-branch親5件、S121の合計60件の原著・採否本文をGitHubに追加保存。PR #1854 draft / 未マージ。移植完了は未宣言。** 本文転記は数学定理の独立監査を意味しない。元研究はrow393停止、Branch B・−30・全LOW等はOPEN。

## 採用する移植境界

- **GitHub必須：** row393までの現行結論の論理的な鎖に不可欠な原証明・補題、各適用条件、訂正、採否、再現に必要な最小コード/証拠。
- **Drive参照可：** 使用しない障壁、失敗したルート、旧NEXT、重複・検証ログ、途中版。原著論文は本文全文の転載ではなく使用した外部定理の仮定と正確な式をGitHubへ記録する。
- 「本文を追加した」「原文と表示が同一」「数学を独立検算した」「研究が無条件に閉じた」は四つの異なる判定。今回変わったのは第一項と祖先のリンク対応。

## 今回の増補34件

第一段：前回未対応とされた**13件の本文すべて**を取り込み。第二段：S219–221/S231–232/S254–258/S266の**11件**を取り込み。第三段：S194–196/S213/S218/S228–229/S235/S275/S318の**10件**を取り込み。合計**34件**。うちC175/C185/C189はR0採否・統合を含むので、34件の独立数学定理が新たに証明されたわけではない。

[S243](proofs/active-ancestors/S243.md)のGoogle Docs表1件（3行×4列、12セル）はMarkdown表へ復元。[S255](proofs/active-ancestors/S255.md)は初回に誤ってCURRENT（管理要旨）を本文としたため、元の完全数学CARDに差し替え、[管理CURRENT](proofs/active-ancestors/S255-current.md)を歴史ファイルとして保持した。13件＋新21件という別数えは用いず、**新34原著/採否本文**とする。

## 現行主要鎖の図

```text
S194 -> S195 -> S196 -> S228/S229（finite-odd branchの限定的空性）
             └─> S231 -> S232 分母・位数条件 ─┐
S235 -> S243 四根/Kummer ───────────────┤
S213 -> S218 -> S219 -> S220 -> S221      │
                               └-> S258 critical H
S232+S237+S243+S251+S253 -> S254 -> S255 -> S256 -> S257 -> S258
                                      S258 -> S259 -> S260 -> S261 -> S262
S263/S264 -> S265 odd epsilon=+1 -> S266
S259/S260/S266 + S252/S267 -> S270 genuine four TOP masses
S275 -> S318 + C175/C185 -> R2 lower threshold 155/197 -> C189 R0 adoption
LOW proofs row361..376 + older C181/C183/R5-C212 -> 9 abs / 16 signed
−30: row370..384 -> row385..393 -> formal quotient181 / class group bound conditional
```

**注意：** 上図は要点のみで、全親は以下の一覧の`parents`を参照。S219〜S221の旧finite-oddでの`dQ=mP`をS258の無限位数ルートへ持ち込まない。後続が使うのは個別に証明されたpoint-onlyの局所恒等式。S229が閉じるのはfinite-odd physical packetであって、Branch B全体ではない。S262は局所逆写像の*非障害*であり物理解排除ではない。S265のodd ε=+1は使用、同稿の有限素数の非閉鎖は障壁扱い。S275のeta捻り群のno-goは成果の二重計上不可。S318のGOOD化にはH側の追加条件が必要。S252のsuperelliptic外部定理は未照合。

## 34件の出典と実際に引用する数学的親

| 対象 | 今回維持した数学的範囲 | 親（太字は対応付け/必要性判定待ち） | GitHub原著 |
|---|---|---|---|
| S219 | local H/Pell point-only approximation; old scalar dQ=mP is NOT imported | [S213](proofs/active-ancestors/S213.md)、[S218](proofs/active-ancestors/S218.md) | [本文](proofs/active-ancestors/S219.md) |
| S220 | one higher H/Pell deformation coefficient | [S219](proofs/active-ancestors/S219.md) | [本文](proofs/active-ancestors/S220.md) |
| S221 | all-H coefficient D=1/(4t0^2) and local-centers lemma | [S219](proofs/active-ancestors/S219.md)、[S220](proofs/active-ancestors/S220.md) | [本文](proofs/active-ancestors/S221.md) |
| S231 | complete physical source direct square denominator and parity | [S194](proofs/active-ancestors/S194.md)、[S195](proofs/active-ancestors/S195.md)、[S196](proofs/active-ancestors/S196.md)、[S228](proofs/active-ancestors/S228.md)、[S229](proofs/active-ancestors/S229.md) | [本文](proofs/active-ancestors/S231.md) |
| S232 | b>1; all denominator primes outside 2ABC; ord(Pbar)=4h where h//n/ odd quotient | [S231](proofs/active-ancestors/S231.md)、**S230（要照合）**、[S228](proofs/active-ancestors/S228.md)、[S229](proofs/active-ancestors/S229.md) | [本文](proofs/active-ancestors/S232.md) |
| S243 | global common-c four roots and true Q Kummer class (not finite-base emptiness) | [S235](proofs/active-ancestors/S235.md)、[S237](proofs/C195-upstream/S237.md)、**S242（要照合）** | [本文](proofs/active-ancestors/S243.md) |
| S251 | all denominator H/good primes; local 2-half and order 8 | [S232](proofs/active-ancestors/S232.md)、[S233](proofs/C195-upstream/S233.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、**S250（要照合）** | [本文](proofs/active-ancestors/S251.md) |
| S252 | effective base-dependent H-supported bound, not source exclusion | [S232](proofs/active-ancestors/S232.md)、[S237](proofs/C195-upstream/S237.md)、[S240](proofs/C195-upstream/S240.md)、[S251](proofs/active-ancestors/S251.md)、**EXTERNAL_BERCZES_THM2_1（要照合）** | [本文](proofs/active-ancestors/S252.md) |
| S253 | two compulsory roles and same order2 signature at H | [S232](proofs/active-ancestors/S232.md)、[S233](proofs/C195-upstream/S233.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md) | [本文](proofs/active-ancestors/S253.md) |
| S254 | seed2/3 actual orbit odd-multiple denominator propagation | [S232](proofs/active-ancestors/S232.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md) | [本文](proofs/active-ancestors/S254.md) |
| S255 | arbitrary-seed gcd and Pell H-support; CARD replaces management CURRENT | [S232](proofs/active-ancestors/S232.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S254](proofs/active-ancestors/S254.md) | [本文](proofs/active-ancestors/S255.md) |
| S256 | H-entry beta exact valuation and height normalization | [S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S254](proofs/active-ancestors/S254.md)、[S255](proofs/active-ancestors/S255.md) | [本文](proofs/active-ancestors/S256.md) |
| S257 | Pell comparison precision/deep exception receiver | [S219](proofs/active-ancestors/S219.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S254](proofs/active-ancestors/S254.md)、[S255](proofs/active-ancestors/S255.md)、[S256](proofs/active-ancestors/S256.md) | [本文](proofs/active-ancestors/S257.md) |
| S258 | actual critical H definition via local next-digit, two roles | [S219](proofs/active-ancestors/S219.md)、[S220](proofs/active-ancestors/S220.md)、[S221](proofs/active-ancestors/S221.md)、[S253](proofs/active-ancestors/S253.md)、[S255](proofs/active-ancestors/S255.md)、[S256](proofs/active-ancestors/S256.md)、[S257](proofs/active-ancestors/S257.md) | [本文](proofs/active-ancestors/S258.md) |
| S259 | rolewise PROPER height and EQUAL first-entry critical | [S252](proofs/active-ancestors/S252.md)、[S256](proofs/active-ancestors/S256.md)、[S258](proofs/active-ancestors/S258.md) | [本文](proofs/active-ancestors/S259.md) |
| S260 | full GOOD-or-critical TOP entry height | [S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S254](proofs/active-ancestors/S254.md)、[S256](proofs/active-ancestors/S256.md)、[S258](proofs/active-ancestors/S258.md)、[S259](proofs/active-ancestors/S259.md) | [本文](proofs/active-ancestors/S260.md) |
| S261 | exact GOOD TOP Kummer role neutrality | [S232](proofs/active-ancestors/S232.md)、[S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S253](proofs/active-ancestors/S253.md)、[S258](proofs/active-ancestors/S258.md)、[S260](proofs/active-ancestors/S260.md) | [本文](proofs/active-ancestors/S261.md) |
| S262 | local inverse nonobstruction (NOT proof of emptiness) | [S240](proofs/C195-upstream/S240.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S260](proofs/active-ancestors/S260.md)、[S261](proofs/active-ancestors/S261.md) | [本文](proofs/active-ancestors/S262.md) |
| S265 | odd signed epsilon=+1, formal-unit lemma; finite-prime barrier is separate | [S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S263](../../materials/original-source-exclusions/parents/S263.md)、[S264](proofs/foundations/S264.md)、[S260](proofs/active-ancestors/S260.md)、[S261](proofs/active-ancestors/S261.md)、[S262](proofs/active-ancestors/S262.md) | [本文](proofs/active-ancestors/S265.md) |
| S266 | period depth and even valuation/primitive-family negative control | [S263](../../materials/original-source-exclusions/parents/S263.md)、[S265](proofs/active-ancestors/S265.md) | [本文](proofs/active-ancestors/S266.md) |
| S267 | H-norm crowding, unconditional integer bound within full original packet | [S237](proofs/C195-upstream/S237.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S252](proofs/active-ancestors/S252.md)、[S253](proofs/active-ancestors/S253.md)、[S259](proofs/active-ancestors/S259.md)、[S260](proofs/active-ancestors/S260.md)、[S261](proofs/active-ancestors/S261.md)、[S262](proofs/active-ancestors/S262.md)、[S263](../../materials/original-source-exclusions/parents/S263.md)、[S264](proofs/foundations/S264.md)、[S265](proofs/active-ancestors/S265.md)、[S266](proofs/active-ancestors/S266.md) | [本文](proofs/active-ancestors/S267.md) |
| C175 | R0 cross-lane integration; subset of retained uniform height constant and dedup | [C174](proofs/C195-upstream/C174.md)、[S263](../../materials/original-source-exclusions/parents/S263.md)、[S265](proofs/active-ancestors/S265.md) | [本文](proofs/active-ancestors/C175.md) |
| C185 | R0 scoped sparse TOP coefficient acceptance/dedup | **C160（要照合）**、[S268](proofs/C195-upstream/S268.md)、[S275](proofs/active-ancestors/S275.md)、[S318](proofs/active-ancestors/S318.md) | [本文](proofs/active-ancestors/C185.md) |
| C189 | R0 ACCEPT_DEPENDENT_UNIFORM_THRESHOLD_EXTENSION and withdraw previous duplicates | [C175](proofs/active-ancestors/C175.md)、[C185](proofs/active-ancestors/C185.md)、[S270](proofs/foundations/S270.md)、[R2_UNIFORM_155_197](proofs/R2-uniform-thresholds.md) | [本文](proofs/active-ancestors/C189.md) |
| S194 | quotient finite-odd vs infinite-class splitting, no global Branch B closure | **S193（要照合）**、**SECTION16_NONSQUARE（要照合）** | [本文](proofs/active-ancestors/S194.md) |
| S195 | finite odd class: two exact physical squarecovers | [S194](proofs/active-ancestors/S194.md)、**SECTION16_NONSQUARE（要照合）** | [本文](proofs/active-ancestors/S195.md) |
| S196 | one epsilon=1 physical cover uniformly empty, not entire Branch B | [S194](proofs/active-ancestors/S194.md)、[S195](proofs/active-ancestors/S195.md)、**EXTERNAL_FERMAT_QUARTIC（要照合）** | [本文](proofs/active-ancestors/S196.md) |
| S213 | ANY G/H endpoint group calculus; finite scalar setting not inherited by infinite branch | **S202（要照合）** | [本文](proofs/active-ancestors/S213.md) |
| S218 | formal local division depth; point-only identities reused, dQ=mP not reused | [S213](proofs/active-ancestors/S213.md)、**S202（要照合）** | [本文](proofs/active-ancestors/S218.md) |
| S228 | D_n denominator support under finite odd packet and q/AC local identities | [S213](proofs/active-ancestors/S213.md)、**S227（要照合）**、**S202（要照合）** | [本文](proofs/active-ancestors/S228.md) |
| S229 | finite odd original physical chamber emptiness, NOT infinite class exclusion | [S228](proofs/active-ancestors/S228.md)、**S227（要照合）** | [本文](proofs/active-ancestors/S229.md) |
| S235 | genus1/genus5/genus9 etale tower and mod8 restriction | [S232](proofs/active-ancestors/S232.md)、[S233](proofs/C195-upstream/S233.md)、**S234（要照合）** | [本文](proofs/active-ancestors/S235.md) |
| S275 | canonical all-index primitive four-root quartic factorization; eta union no-go not saving | [S243](proofs/active-ancestors/S243.md) | [本文](proofs/active-ancestors/S275.md) |
| S318 | odd-prime exact TOP and noncritical H correction; lower mass conditional | [S268](proofs/C195-upstream/S268.md)、[S269](proofs/C195-upstream/S269.md)、[S270](proofs/foundations/S270.md)、[S275](proofs/active-ancestors/S275.md)、[S267](proofs/active-ancestors/S267.md)、[S258](proofs/active-ancestors/S258.md)、**S316（要照合）** | [本文](proofs/active-ancestors/S318.md) |

## 初期34件時点の未対応の親識別子（当時12：履歴）

**C160、EXTERNAL_BERCZES_THM2_1、EXTERNAL_FERMAT_QUARTIC、S193、S202、S227、S230、S234、S242、S250、S316、SECTION16_NONSQUARE**。

この12は**「未移植必須数学定理12本」と等価ではない**。今後の再帰照合で、同じ証明が既収載本文中に内包されていればそのパスへ直接対応させる。

- **優先数学親**：S193（finite-oddの旧部分閉鎖）、S202（local H/G群アダプター）、S227（strict physical chord）、S234（genus9原構成）、S316（S318が使うfamily高さ）、原Section16のa-nonsquare補題。C160はC185が歴史的に借用するgcd/first-entry係数の正確な版を特定する。
- **重複・証明対象外の可能性**：S230はS228/229の外部的/独立算術監査、S242はS243の固定基底ランク例、S250のgood-prime結果はS251で再証明/再述。歴史・障壁のみならDrive参照でよい。
- **外部原典ゲート**：S252のBérczesほかsuperelliptic S-integer定理、S196で用いる4乗和の古典定理、そして独立にrow393 de la Mazaの類代表上界。定理本文と仮定を原典に照合できていない箇所は未監査。
- **計算再現ゲート**：各CARDにあるverify.py/期待JSONは、本文と別に最小限の数学上必要な入力/コードを特定して収載する。今回の34件すべてについてその独立再演算を実施したとは主張しない。

## 現在の数え方

[従来の中核55本文相当・親7の棚卸し](ACTIVE-PROOF-SPINE-COVERAGE.md)に、今回新規34件の親数学/採否文書を追加。重複、単一著者のまとめカード、採否だけの資料を独立定理数として加算しない。初期13未対応候補は全13原文収載で解消したが、**完全な親鎖と再現コードを含む必要総件数・完了率はまだ確定不可**。これからの公開作業は新しい[出典・直接依存の機械台帳](ACTIVE-ANCESTOR-SOURCE-MAP.json)を参照する。

研究正本R0/運用NEXTは未更新。GitHubのPRだけ編集。[移植完了チェック](MIGRATION-COMPLETION-CHECKLIST.md)

## 2026-11-09 第2波：不足していた数学的親5件を追加（履歴）

| ID | 実際に継承する範囲 | 直接参照される親（新たな依存候補） | GitHub原著 |
|---|---|---|---|
| S193 | scoped original first Branch-B subbranch exclusion, not global Branch B closure | S192, SECTION16_NONSQUARE | [S193](proofs/active-ancestors/S193.md) |
| S202 | finite-odd q-primary physical component escape reduction; dQ=mP retained only in finite-class setting | S194, S197, S200, S201 | [S202](proofs/active-ancestors/S202.md) |
| S227 | integral full-chord monic-square denominator lemma, not full physical closure; S231 partially re-proves denominator without relying on this | S197, S223, S225, S226 | [S227](proofs/active-ancestors/S227.md) |
| S234 | simultaneous quartic roots and two degree-8 genus-9 components; fixed-base finiteness does not close varying-base sources | S232, S233 | [S234](proofs/active-ancestors/S234.md) |
| S316 | all-base high-index original-source census, not packet or signed-source exclusion; author-side provisional | S252, S270, S291, S308, S312, S313, S314, S315 | [S316](proofs/active-ancestors/S316.md) |

**最新の未対応候補は20識別子（単純な不足定理数ではない）：** `C160`、`EXTERNAL_BERCZES_THM2_1`、`EXTERNAL_FERMAT_QUARTIC`、`S192`、`S197`、`S200`、`S201`、`S223`、`S225`、`S226`、`S230`、`S242`、`S250`、`S291`、`S308`、`S312`、`S313`、`S314`、`S315`、`SECTION16_NONSQUARE`。今回S193/S202/S227/S234/S316の原文を取り込んだため、旧12識別子のうち5件は本文として解消。ただしS192/S197/S200/S201/S223/S225/S226/S291/S308/S312/S313/S314/S315など、これらの本文から新しい上流の確認対象が生じた。既存GitHubにある別名の等価証明を優先照合し、重複は移植しない。S231はS227への依存を一部縮小するが、S228/229が用いる厳密chordの使用範囲を確認する。S234はFaltingsによる**固定基底**の有限性で、全基底の無根拠な排除に使わない。S316は著者側の暫定条件付き高指数censusで、全物理解排除ではない。S202の`dQ=mP`はfinite-odd packet限定。

今回5件のGitHub本文保存は独立数学監査・計算再実行ではない。外部Bérczes、古典quartic、row393 de la Mazaの原典ゲートは未解決。S193/S202/S227/S234/S316で引用する最小計算証書も個別に未照合。研究row393停止、Branch B等OPEN、PR draft未マージ。

## 2026-11-09 第3波：さらに古い数学的親9件の保存

| 親 | 利用中の限定命題 | 上流参照 | GitHub本文 |
|---|---|---|---|
| S192 | finite-integer subgroup x-isogeny receiver; not global Branch B closure | S190, S191 | [本文](proofs/active-ancestors/S192.md) |
| S197 | shifted odd full-chord receiver; scalar only for finite-odd | S193, S194, S195, S196 | [本文](proofs/active-ancestors/S197.md) |
| S200 | prime-power formal-depth finite-odd receiver; no global closure | S197, S198, S199 | [本文](proofs/active-ancestors/S200.md) |
| S201 | symmetric formal chord depth finite-odd receiver | S197, S198, S199, S200 | [本文](proofs/active-ancestors/S201.md) |
| S223 | original division integer/H-prime height necessary bound | S213, S218, S222 | [本文](proofs/active-ancestors/S223.md) |
| S225 | square-support B-boundary large-index necessary prefilters | S194, S198, S223, S224 | [本文](proofs/active-ancestors/S225.md) |
| S226 | even-index dual square envelope, not odd | S198, S225 | [本文](proofs/active-ancestors/S226.md) |
| S291 | signed orbit original height adapter; rank/growth open | S289, S290 | [本文](proofs/active-ancestors/S291.md) |
| S308 | S316 invokes section3–4 all-base 16P height certificate, not conditional d445 conclusion | S252, S291 | [本文](proofs/active-ancestors/S308.md) |

S316の (316.1)/(316.2) に直接用いる旧数学は **S252 / S270 / S291 / S308 (Sections3–4)**。S312/S313/S314/S315はS316の比較・後継/背景の記載であり、全件を数式証明の直親とは認定しない。S308のd445条件付き排除をall-base下界と混同しない。S226は偶数指数専用。旧finite-oddの `dQ=mP` を無限位数側へ持ち込まない。

**今回の追加本文累計48件**。これらは独立検証済みの48定理ではない。**最新未対応識別子15件（分類待ち）:** `C160`、`EXTERNAL_BERCZES_THM2_1`、`EXTERNAL_FERMAT_QUARTIC`、`S190`、`S191`、`S198`、`S199`、`S222`、`S224`、`S230`、`S242`、`S250`、`S289`、`S290`、`SECTION16_NONSQUARE`。旧12/20件は以前の時点の棚卸し。残る識別子には外部定理、監査・重複、古い親の論理的必須部分が混在するため、最終必要数・完了率は未定。計算証書の最小移植と独立再演算も未完了。

## 2026-11-09 第4波：有限位数・局所H側の古い必須親6件

| 親 | 継承する数学的範囲 | 直接の旧親 | GitHub本文 |
|---|---|---|---|
| S190 | scoped reciprocal pair exclusion, original S126 population and physical adapter held | S126 | [本文](proofs/active-ancestors/S190.md) |
| S191 | orientation and exact x-only S123/S126-to-S190 adapter; full upstream HOLD | S123, S126, S190 | [本文](proofs/active-ancestors/S191.md) |
| S198 | finite-odd homogeneous boundary with distinct even/odd conditions | S190, S194, S197 | [本文](proofs/active-ancestors/S198.md) |
| S199 | least-prime resonance necessary sieve, not full physical closure | S194, S197, S198 | [本文](proofs/active-ancestors/S199.md) |
| S222 | original P nontorsion and algebraic H-center necessity; no all-H exclusion | S213, S218, S221 | [本文](proofs/active-ancestors/S222.md) |
| S224 | finite conic projection/homogeneous scalar cap, not source exclusion | S198, S223 | [本文](proofs/active-ancestors/S224.md) |

S289/S290 はすでに [S289](proofs/C195-upstream/S289.md) / [S290](proofs/C195-upstream/S290.md) としてGitHubに存在したため、再コピーせず既存pathへ対応した。S190/S191の scoped 結論を全上流original physical adapterの独立監査PASSに昇格させない。S198のeven-only条件、S222の非torsion結論とH-centerの未排除、S224の有限射影を厳密に区別。

**追加資料は合計54件。** 新たな再帰・外部/重複を含む現在の未対応分類候補は9識別子：`C160`、`EXTERNAL_BERCZES_THM2_1`、`EXTERNAL_FERMAT_QUARTIC`、`S123`、`S126`、`S230`、`S242`、`S250`、`SECTION16_NONSQUARE`。この数は数学的に必須な欠落証明数ではない。S123/S126のscoped原資料、Section16 a-nonsquare、C160の正確なgcd補題、外部定理の原文条件、最小計算コードの連結を確認するまで移植完了は宣言しない。

## 2026-11-09 第5波：S123/S126の分岐に不可欠な親証明5件

| ID | この系で使われる限定主張 | 親 | GitHub原著 |
|---|---|---|---|
| S122 | reciprocal partner and paired-index MW split conditional on original Section121 adapter | S121 | [本文](proofs/active-ancestors/S122.md) |
| S123 | primitive-divisor transfer of reciprocal index pair; only GENERIC_IMAGE_MULTIPLE branch | S122 | [本文](proofs/active-ancestors/S123.md) |
| S124 | family Lang bound and normalized canonical-height inequality, external inequalities retained | S123 | [本文](proofs/active-ancestors/S124.md) |
| S125 | explicit Zsigmondy bound from direct 2-Kummer, external EMW Lemma3.3 and Silverman height comparison | S123, S124 | [本文](proofs/active-ancestors/S125.md) |
| S126 | 379-pair scoped index population based on audited S123–125 interface, full predecessor audit not claimed | S123, S124, S125 | [本文](proofs/active-ancestors/S126.md) |

S126の379組はS123–125のscoped前提とpopulation auditを保持する。S123はGENERIC_IMAGE_MULTIPLEという定義された部分分岐への必要条件であり、Branch B全体の排除ではない。S122が使うS121の元のquotient adapterは新たに確認対象になった。S124/S125の外部Silverman/EMWの正規化と定理仮定を独立照合したと主張しない。

**累計59原証明/採否資料をGitHubへ追加保存**。最新の未対応・要仕分けは8識別子：`C160`、`EXTERNAL_BERCZES_THM2_1`、`EXTERNAL_FERMAT_QUARTIC`、`S121`、`S230`、`S242`、`S250`、`SECTION16_NONSQUARE`。外部数学入力、監査だけの文書、再述/数値例、未収載の真の親を混在させた機械的リストであり、必要数学の不足数ではない。本文収載と最小計算証書再現、文字列忠実性、敵対的数学監査は別ゲート。PR #1854 draftで研究row393停止。

## 2026-11-09 第6波：元の同じ quotient の親 S121

[S121原著](proofs/active-ancestors/S121.md)を追加し、S122の同じD元点・2-isogeny quotient と GENERIC_IMAGE_MULTIPLE分岐の m,n 結合をGitHubで確認可能にした。S121の冒頭にあるSection120はBranch Aのsupport-migration障壁・研究ルートparkで、S121の元のSection13 quotient同一性の新規数学的親ではないため、[Driveの原資料](https://docs.google.com/document/d/1Oa02cmUsqchmR5TjMOSQZzbBWQxqOqn1LndiyrPCLU4/edit)への参照で維持する。Section13の従前のscoped hostile auditの範囲を今回再監査したわけではない。

**累計60件の追加原文・採否本文**。依存識別子残7候補：`C160`、`EXTERNAL_BERCZES_THM2_1`、`EXTERNAL_FERMAT_QUARTIC`、`S230`、`S242`、`S250`、`SECTION16_NONSQUARE`。真の必須親・外部定理・障壁/例示/再述を混同せず分類継続。原著収載≠計算証拠GitHub完結≠数学独立監査。研究停止とPR draft未マージを維持。
