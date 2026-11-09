# R3-07・R2-01 数学原著移植 第２周｜第１差分

2026-11-09。**前提：[#1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)をmainへマージ済み**（`db8c89f`）。[第１周の収載行列](PR1854-PROOF-EVIDENCE-PRESENCE-MATRIX.md)は歴史時点の記録として残し、この文書と[JSON](PR1854-PASS2-SOURCE-DELTA.json)に第２周の差分だけ追記する。

**この第２周は証明鎖の数学原著本文の収載作業**。原著の再読とGitHub本文の一致確認は、数学的定理の独立監査PASSとは異なる。計算証拠・ZIP・検証コードの移植や再演はまだしていない。R3はrow393停止、R2のstrict75%上界・全LOW排除・Branch B・Stage35はOPEN。

## A. 後続で直接使用が確認でき、Drive原著本文を収載した３件

| ID | Drive原著 | 今回のGitHub原著 | 使用箇所（既存） | 証拠区分 |
|---|---|---|---|---|
| row344｜最大整環・2素点分解 | [Drive](https://drive.google.com/file/d/1DvnLJWqL8VFfCPLiwM0doS2uA9qrs9yh/view) | [原著本文](proofs/R3-18-upstream/row344.md) | row345 / row355 | **今回収載。取得本文との一致確認済み** |
| row353｜5奇bad素点の真正局所Kummer基底 | [Drive](https://drive.google.com/file/d/1aHsGWaaPpkJ7JaMhspYnsoKVVMwhQqTd/view) | [原著本文](proofs/R3-18-upstream/row353.md) | row364 | **今回収載。取得本文との一致確認済み** |
| row355｜2進真正Kummer完全生成 | [Drive](https://drive.google.com/file/d/1q23ycRB14SpWlnAsbWECaWRs6QcIGGlZ/view) | [原著本文](proofs/R3-18-upstream/row355.md) | row363 / row364 | **今回収載。取得本文との一致確認済み** |

- **row344**：既存[row345](../../materials/selmer18-parent-chain/objects/01d05437afc6fa87-PROOF_C2_TRUE_LOCAL_KUMMER_DIMENSIONS_JA.md)と[row351](proofs/R3-18-upstream/row351.md)は、全最大整環・2素点分解の旧結果を前提にする。後続の言及だけでは最大性の証明本文を代替しない。
- **row353**：[row364](../../materials/original-source-exclusions/parents/row364/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105.md)が5つの奇数悪素点の全局所生成系を既出として再利用。row353原著には具体的な局所除数と基底の導出がある。
- **row355**：[row363](../../materials/selmer18-parent-chain/proofs/row363.md)と[row364](../../materials/original-source-exclusions/parents/row364/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105.md)が完全2進Kummer局所生成元を直接再利用。これらは新規の全球結論を扱う文書であり、row355の19局所生成元の構成を一から全再証明する文書ではない。

上記３本はDriveで取得したMarkdownを**加工せず**保存し、GitHubから再読したテキストとの完全一致を個別に確認。Git blob SHA・出典URL・読み戻しフラグはJSONに固定。数式の正当性や同梱JSON・検証器の再演は**未検証**。

## B. 依然Drive原著のみ：９件（移植要否の判定待ち）

| ID | Drive原著 | 後続の引用候補 | 判定 |
|---|---|---|---|
| row346｜全球S単数・ノルム平方候補 | [Drive](https://drive.google.com/file/d/1Yd1kTZN9mr8zFX10HN8zeqwjit_cvJkM/view) | row348 / row350 | **未収載・同値性未監査** |
| row347｜独立整数単数12本 | [Drive](https://drive.google.com/file/d/1a7_BRnS1vrZ5vgdyl5Wrjqn0O-Fo3Kaa/view) | row348 / row359 | **未収載・同値性未監査** |
| row348｜S素イデアル主関係・7付値方向 | [Drive](https://drive.google.com/file/d/1MaB1FihiOKabuqaVxOBqhEuEWsfpuPwo/view) | row349 / row350 | **未収載・同値性未監査** |
| row349｜単数指数13・非8乗 | [Drive](https://drive.google.com/file/d/1yYOj_OVFpbLHx6NBqSJCVXvNXcDW6RqP/view) | row359 / row351 | **未収載・同値性未監査** |
| row356｜4局所条件による全球候補制限 | [Drive](https://drive.google.com/file/d/1jPKjxGj_AgWhUcQi16XpsPD0ICKVxpfH/view) | row357 / row358 | **未収載・同値性未監査** |
| row357｜S類群上界13 | [Drive](https://drive.google.com/file/d/1O_xehDwMFSk1mWaggGorBpAjahBlHjUx/view) | row358 / row363 | **未収載・同値性未監査** |
| row358｜有限偶付値とtrue Selmer 17上界 | [Drive](https://drive.google.com/file/d/1iprQvIDXgodniosJeFohMm-PcKXZl17p/view) | row359 / row363 | **未収載・同値性未監査** |
| row359｜新単数3本・true Selmer≤14 | [Drive](https://drive.google.com/file/d/1CXLvx5rApWdr8hyzsx5YjL2Vl3T2BG6Y/view) | row360 / row361 / row363 | **未収載・同値性未監査** |
| row360｜163進全MW円盤・個数上界14 | [Drive](https://drive.google.com/file/d/1P0FB4LbFqFp7kx88i04NzAehKi-g8eXW/view) | row361 / row363 | **未収載・同値性未監査** |

**注意：** ９件＝追加必須９件ではない。まず後続本文内の厳密な再証明の有無、直接使う定理、証書所在、前提の差異を１件ずつ突合する。たとえばrow357の旧類群上界はrow363の類群1に上書きされても、row358の歴史的証明の論理的親として必要な場合は別に記録する。判定を一括確定しない。

## C. R2-01（まだ追加していない）

[第１周行列](PR1854-PROOF-EVIDENCE-PRESENCE-MATRIX.md)のS250、S271〜274、S280、S283、C188、C191、BranchB §1–12、C193などは**そのまま保留**。特にS280→C189の実使用を先に確認。S250は既存[S251](proofs/active-ancestors/S251.md)の再述があるため重複を急がない。R2側で新規追加した数学原著は０件。

## D. 次の作業

1. R3 row346→349とrow356→360について、**定理・仮定・証明箇所を後続GitHub本文と行単位で比較**し、必要なら原著をそのまま収載する。
2. row344 / 353 / 355が参照する計算証書・JSON・検証器のGitHub内重複を確認し、数学本文だけの今回の移植と別に所在／再演未実施を記録する。
3. R2 S280のC189への直接依存を点検。S250や旧枝を追加するか否かを個別に確定する。
4. 必須親の完全閉包・外部Bérczes/de la Maza適用条件・独立数学監査は未完として維持。

**管理ルール：** 第１周の129収載済みを再計上しない。新規の数学結論やsource排除を本作業で認定しない。正式MAIN-STATE、Drive R0、研究NEXTは書き換えない。
