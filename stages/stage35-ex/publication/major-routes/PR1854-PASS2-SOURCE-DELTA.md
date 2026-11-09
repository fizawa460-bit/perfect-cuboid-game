# R3-07・R2-01｜PR #1854を受けた証明原著の第２周：最新収載・未収載の差分

**更新：2026-11-09。対象は R3-07（±18とrow393への経緯）・R2-01（S270とC189の155/197下界）だけ。** 前PR[#1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)は`db8c89f`でmainにマージ済み。本第２周は[#1860](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1860)のDraftで追記し、数学結論や研究正本に手を加えない。

## 結論：どれだけあって、どこまで上げたか

| 対象 | 件数 | 意味 |
|---|---:|---|
| 第１周の数学原著（重複除去） | **129** | #1854の差分に入っておりmainにマージ済み。独立した必須数学定理の個数ではない |
| 以前からGitHubにある数学本文 | **2** | 35EX-21・35EX-31。#1854の差分ではなかったが既存 |
| 第１周行列で発見した、Driveのみの原著候補 | **23** | その時点で独立原著ファイルがGitHubに見つからなかった候補の数 |
| 上の23候補から今回GitHub原著本文を追加 | **12** | すべてR3-07 ±18。Drive取得テキストとGitHub再読テキストが各件一致 |
| 残りDriveのみ | **11** | すべてR2周辺。うち10件は現在のC187/C189/S270証明の**直接の数学親としては確認されない**参考・重複・旧側枝、1件は旧最古文書の精査を保留 |
| R3±18の確認済み12原著のうち未移植 | **0** | ただし証明書/計算の移植や数学独立監査は別問題 |

**注意：129 + 2 + 12 = 数学的必須証明の総数、という算数はしない。** 23はその時点で見つかった候補群の数であり、**全数学祖先の再帰閉包を証明済みとは言えない**。今後、S194の旧Section16引用や外部原典・原計算証書の不足は別に出る可能性がある。

## A. R3-07 ±18で追加した数学原著：12件（全件GitHub再読一致）

| 原著 | 現在のGitHub原著 | Drive原著 | 既存で結果を継承・使用している例 |
|---|---|---|---|
| **row344** 全最大整環と2の素イデアル分解 | [収載原文](proofs/R3-18-upstream/row344.md) | [元Drive](https://drive.google.com/file/d/1DvnLJWqL8VFfCPLiwM0doS2uA9qrs9yh/view) | row345 / row351 / row355 |
| **row346** 全球S単数群の構造、ノルム平方候補 | [収載原文](proofs/R3-18-upstream/row346.md) | [元Drive](https://drive.google.com/file/d/1Yd1kTZN9mr8zFX10HN8zeqwjit_cvJkM/view) | row348 / row350 |
| **row347** 独立な12本の整数単数 | [収載原文](proofs/R3-18-upstream/row347.md) | [元Drive](https://drive.google.com/file/d/1a7_BRnS1vrZ5vgdyl5Wrjqn0O-Fo3Kaa/view) | row348 / row359 |
| **row348** 7方向のS付値と主イデアル関係 | [収載原文](proofs/R3-18-upstream/row348.md) | [元Drive](https://drive.google.com/file/d/1MaB1FihiOKabuqaVxOBqhEuEWsfpuPwo/view) | row349 / row350 |
| **row349** 13指数の非飽和とθの4乗・非8乗 | [収載原文](proofs/R3-18-upstream/row349.md) | [元Drive](https://drive.google.com/file/d/1yYOj_OVFpbLHx6NBqSJCVXvNXcDW6RqP/view) | row359 / row351 |
| **row353** 奇bad5素点の局所Kummer生成系 | [収載原文](proofs/R3-18-upstream/row353.md) | [元Drive](https://drive.google.com/file/d/1aHsGWaaPpkJ7JaMhspYnsoKVVMwhQqTd/view) | row364 |
| **row355** 完全な2進Kummer局所像 | [収載原文](proofs/R3-18-upstream/row355.md) | [元Drive](https://drive.google.com/file/d/1q23ycRB14SpWlnAsbWECaWRs6QcIGGlZ/view) | row363 / row364 |
| **row356** 全球候補の四局所cut | [収載原文](proofs/R3-18-upstream/row356.md) | [元Drive](https://drive.google.com/file/d/1jPKjxGj_AgWhUcQi16XpsPD0ICKVxpfH/view) | row357 / row358 |
| **row357** S類群上界13 | [収載原文](proofs/R3-18-upstream/row357.md) | [元Drive](https://drive.google.com/file/d/1O_xehDwMFSk1mWaggGorBpAjahBlHjUx/view) | row358 / row363 |
| **row358** 有限偶付値・真Selmer≤17 | [収載原文](proofs/R3-18-upstream/row358.md) | [元Drive](https://drive.google.com/file/d/1iprQvIDXgodniosJeFohMm-PcKXZl17p/view) | row359 / row363 |
| **row359** 3追加単数・真Selmer≤14 | [収載原文](proofs/R3-18-upstream/row359.md) | [元Drive](https://drive.google.com/file/d/1CXLvx5rApWdr8hyzsx5YjL2Vl3T2BG6Y/view) | row360 / row361 / row363 |
| **row360** 163進全MW円盤・基底数≤14 | [収載原文](proofs/R3-18-upstream/row360.md) | [元Drive](https://drive.google.com/file/d/1P0FB4LbFqFp7kx88i04NzAehKi-g8eXW/view) | row361 / row363 |

各行のGit blob SHA、元Drive URL、テキスト一致フラグは[機械台帳](PR1854-PASS2-SOURCE-DELTA.json)に保存。**原著本文をコピーしたのであって、元JSON証明書・計算ZIP・Python検証器の移植や再演を保証していない。**

row345・row352は[#1854の収載行列](PR1854-PROOF-EVIDENCE-PRESENCE-MATRIX.md)から既存GitHub本文へ接続できるため、改めてコピーしていない。row351、361、363、364、367もすでに#1854に保存されている。row357の旧S類群上界13、row359の旧Selmer≤14などは後続のより強い結果で更新された**歴史的証明鎖の親**として保存し、現在の独立最良定理だと取り違えない。

## B. R2側のDrive-only原著11件：そのまま一括移植しない根拠

| 原著 | Drive | 現行の二ルート証明鎖との関係 | 処置 |
|---|---|---|---|
| **S250** GOOD分母2-Kummer半点・order8 | [Drive原著](https://docs.google.com/document/d/10NtB8i-f1WVC7NPm4bpM5KxXGnPnjfn_LxPSw8jqas8/edit) | 現行R2の必要な結果はS251本文に再述。重複移植しない。 | **既存S251内に再述** |
| **S271** dyadic exact TOP四次式 | [Drive原著](https://docs.google.com/document/d/1eJxTmBp0-X0vEc3ccE9C-cdhOn7Gk5rLwI9OWuy3OcM/edit) | dyadic限定の旧側枝。155/197下界の直接親ではない。 | **現行対象の直接親と確認できず** |
| **S272** dyadic genus33と楕円商 | [Drive原著](https://docs.google.com/document/d/1UWQOece3VQt447Y7mdQxxOdcizNpEQ_EqDNjE8_gMIA/edit) | 幾何学的受け皿。現行下界の直接親ではない。 | **現行対象の直接親と確認できず** |
| **S273** genus17のetale double cover | [Drive原著](https://docs.google.com/document/d/1zwv674vrXnkmFzySToYW8bt-SdrWCV3U0N5YeniamGU/edit) | 旧dyadic被覆枝。現行下界の直接親ではない。 | **現行対象の直接親と確認できず** |
| **S274** dyadic twist・2torsion | [Drive原著](https://docs.google.com/document/d/1obXBSopay9GAnLqc9gEOXz8zG9Oy3cCcrwOIeJUZ-Ew/edit) | twist枝の歴史的制限。現在の下界証明には不要。 | **現行対象の直接親と確認できず** |
| **S280** 四根cross productとsigned W | [Drive原著](https://docs.google.com/document/d/1WdOKrD2JQ7F6VRKlUx04aDsqIPlNF8NinXM7dtAINrg/edit) | C189の歴史的列挙のみ。155/197の数学前提としての引用はない。 | **現行対象の直接親と確認できず** |
| **S283** 実回転phase密度 | [Drive原著](https://docs.google.com/document/d/1CWG97DLy6JJ5MYtJrb4Q7J5IGPVV4WGnWtyqnv5Utu0/edit) | 固定基底上の符号密度であり、現行155/197下界の親ではない。 | **現行対象の直接親と確認できず** |
| **C188** K21類群訂正と採否 | [Drive原著](https://docs.google.com/document/d/1gNnTh4AbS_xHcG6dZY4XvUcaqXtiadDslpLK_1ih8wM/edit) | 異なるK21対象の訂正。2ルート主証明の直接親でない。 | **現行対象の直接親と確認できず** |
| **C191** C187提出採否・A21量化訂正 | [Drive原著](https://docs.google.com/document/d/1FrUqVQdUdC2WbhdwAYlMxzEq1YTi5SHqHRVjq-tsTWc/edit) | 後日訂正の統合記録。C189の155/197数学原著ではない。 | **現行対象の直接親と確認できず** |
| **BranchB-1-12** 旧Branch B大文書、§1–12を含む | [Drive原著](https://docs.google.com/document/d/1CKLon3eRKjsEVuIwgpSTV4DKHQ5GRWsfDw2SA6T5vNI/edit) | 巨大な旧文書の全量コピーはしない。S121以前の依存鎖で未収載の固有補題が明示されたときに抜粋を調査。 | **旧基礎部の判定保留** |
| **C193** generic non-map次数障壁 | [Drive原著](https://drive.google.com/file/d/1D8QNpX2k-O36w76ZoTqbVDdUFJClNnLj/view) | 旧写像障壁の記録。現行の正方向証明親ではない。 | **現行対象の直接親と確認できず** |

### R2で実際に確かめたこと

- [C187の155/197下界原著](proofs/R2-uniform-thresholds.md)は、S243、S251/253/263/267/268/269、S270、S275、S318、C175・C185などを挙げる。**S280・S283・S271〜274をその下界の直接証明として使った記述はない**。
- [C189原著](proofs/active-ancestors/C189.md)はS280をR1側撤回史の「dominate」の列挙に一度記載するが、これはC187の155/197導出の親としての採用ではない。
- [S251原著](proofs/active-ancestors/S251.md)はS250のorder8半点条件を *This is precisely S250, reiterated only for a unified statement.* と明言。したがって結果だけならS251で充足。
- [S275原著](proofs/active-ancestors/S275.md)は旧S271〜274のdyadic枝を説明しつつ、全指数のcanonical branchとtwist全集合のNO-GOを別途述べる。**S271〜274の全個別幾何学証明がC187へ直接必要とは言えない**。S275自身の数学・前提監査は引き続き未完。
- C188は別のK21類群訂正、C191は後日の提出整合とR4量化訂正、C193はgeneric non-map障壁。R3の固定36次数体やR2の155/197下界の直接証明原著としては採用しない。
- 大規模なBranchB旧文書（§1–12を含む）は100k字超。GitHubには[E3物理source](proofs/earliest-foundations/E3-selected-physical-kummer.md)、[E3 generic MW](proofs/earliest-foundations/E3-generic-MW.md)、[BranchB Section13](proofs/earliest-foundations/BranchB-Section13.md)、[Section16](proofs/earliest-foundations/BranchB-Section16.md)を既に収載している。§1–12の固有の必須補題はこの調査では孤立して特定できていないため、**未判定１件**として残し、127k字を理由なく丸ごと追加しない。

## C. 未完了の項目と再開位置

1. **数学的な必要十分の親DAGは未完**：収載済みファイルの記述を逆向きに辿って、後続で結果が使われたのか単に履歴として引用されたのか、欠けた祖先がないか逐一確認する。
2. **第２の層は計算証拠**：row344〜360の原JSON証書・検算器・元ZIPがどこにあるかは別途照合する。今回、本文だけで完全再演可能とは宣言しない。
3. **外部定理・古い橋**：R2 S252 Bérczes、R3 row393 de la Mazaの原典仮定は依然として未確認。**S194の旧Branch B Section16のa(t)非平方補題の原著位置は[既収載Section16・17](proofs/earliest-foundations/BranchB-Section16.md)および[S194](proofs/active-ancestors/S194.md)で解決済み**。ただし外部Fermat降下定理の独立照合や、撤回されたspecialization二分法の復活はしていない。
4. **研究状態は据え置き**：R3 row393停止、R2相関strict75%上界・無条件−30排除・全LOW・Branch B・Stage35はOPEN。DriveのR0、正式MAIN-STATE、NEXTは変更しない。

## 第二周の作業境界

今回確認できた **R3の12原著の未収載0** は、あくまで「発見済み12本の数学原著本文がPR #1860に入った」の意味。完証・数学独立監査・全証拠のbyte-complete保管を意味しない。未確認をPASSへ書き換えない。
