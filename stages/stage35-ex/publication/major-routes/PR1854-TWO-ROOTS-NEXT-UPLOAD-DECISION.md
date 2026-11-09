# PR #1854｜R3-07・R2-01だけの「GitHub既収載／不足候補／2周目に移す物」判定

> **2026-11-09 範囲修正：根は2つだけ。** R3-07 = P23-LOW（研究経緯row393まで）、R2-01 = P23-MID/HIGH（同時点、C189採択の155/197必要下界まで）。**R1〜R5の99管理ルートは移植対象の分母ではない。** その索引カードだけあって原著を全移植していない、という事実は現在の2本の不足件数にならない。別レーン名の成果は**R3-07/R2-01の既採用命題が実際に使った数学補題だけ**評価する。
>
> **結論：両ルートの現在判明している主要原著はほぼGitHubに入っている。以前の不足リストにあったS230、S238、S321、S322、C160、Section16、row351/352は今は収載済み／既存証明へ接続済み。** 必須と確定した「Driveにしかない完成原証明」はこの照合時点では**具体的に特定されていない**。ただし**必須原著総数／欠落ゼロの証明は未確定**。未確認の論理接続や外部原典は「未収載原著」と別に記す。

## 判定記号

- **G** GitHubに原著または引用を満たす本文あり。**2周目の重複アップ不要**。
- **V** GitHub本文同士の使用条件・同値性が未監査。**追加アップの前に既存本文で足りるか確認**。
- **D** 現行二ルートに対する論理的必要性未確定。**Drive原著を参照、移植保留**。
- **X** 外部定理の原典照合待ち。**論文全文の移植ではなく定理番号・仮定・代入を記録**。
- **O** 目標は未証明／まだ存在が確認されない論証。**「Driveに完成原証明がある」扱いにしない**。

## R3-07：LOW、row393まで（このルートだけから後退）

| 主張・節目 | 今の証拠品と場所 | 判定 | 2周目の具体的扱い |
|---|---|---|---|
| 同じ正の有理物理source／原始標識／signed Ward | [35EX-21](../../35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md)・[35EX-31](../../35ex-31/primitive-source-marking-endpoint-equivalence.md)（**PR外の既存GitHub**）、[E3物理原著](proofs/earliest-foundations/E3-selected-physical-kummer.md)、[C195](proofs/C195-canonical-source.md)・[S268/S269](proofs/C195-upstream/S268.md) | **G/V** | 正の物理方程式の代入は確認済み。**原始標識・実符号・indexed元軌道への移送は未照合**。必要と確定した欠落原著が見つかった場合のみ収載 |
| 現行LOW指数集合を制限する旧マスク | [C181](proofs/foundations/C181.md)、[C183](proofs/foundations/C183.md)、[S264](proofs/foundations/S264.md)、[旧R5-C212](proofs/foundations/R5-C212.md)、[C220/訂正C224](proofs/foundations/R5-C220.md)、[P112再集計](proofs/foundations/R5-P112-rebin.md) | **G/V** | 旧マスクと現在の9絶対／16 signed枠の差分・量化子照合だけ。**古いR1/R4/R5全ルートは調べない** |
| ±18の採用済み排除 | [row339/342/343/350/351原著](proofs/R3-18-upstream/row342.md)、[row345既存原著](../../materials/selmer18-parent-chain/objects/01d05437afc6fa87-PROOF_C2_TRUE_LOCAL_KUMMER_DIMENSIONS_JA.md)、[row352既存原著](../../materials/selmer18-parent-chain/objects/5fd888550f0b7d57-PROOF_C2_INFINITY_RANK7_AND_TRUE_FAKE_KERNEL_JA.md)、[row361/363](../../materials/selmer18-parent-chain/proofs/row361.md)、[row364〜367](../../materials/original-source-exclusions/row367/REPORT.md) | **G/V** | 主張→親証明のリンクはある。row344〜349を連番で取り込まず、**row364等が本当に使う未収載の原証明が発見された時だけ**対応 |
| Ward3/5/7の採用済み排除 | [S238](proofs/active-ancestors/S238.md)・[S320](proofs/active-ancestors/S320.md)・[S321](proofs/active-ancestors/S321.md)・[S322](proofs/active-ancestors/S322.md)、[S263](../../materials/original-source-exclusions/parents/S263.md)、[C118](../../materials/original-source-exclusions/parents/C35-118/export.txt)、[C35-11/12](../../materials/original-source-exclusions/parents/C35-11/PROOF.md)、[row368](../../materials/original-source-exclusions/row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md)・[row369](../../materials/original-source-exclusions/row369/STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER_20261106.md) | **G/V** | S238/S321/S322は**すでに収載**。S322とrow369の必要箇所の同値性だけ確認 |
| +30の排除（−30は含まない） | [row370〜375の親索引](PR1854-R3-07-CHAIN.md)、[row376原証明](../../materials/original-source-exclusions/row376/PROOF.md) | **G** | 原著追加不要。+30に限定 |
| −30の現行到達 | [row377〜384](../../materials/negative30-mw-selmer/README.md)、[row385〜393](../../materials/classgroup-and-different/README.md)、[row393原証明](../../materials/classgroup-and-different/proofs/row393.md)、[適用境界](ROW393-PRIMARY-THEOREM-GATE.md) | **G/X/O** | **de la Maza Theorem1・系の条件/規約照合をGitHub上の短い出典ノートとして完結させる**。計算現物の追加はDrive参照可。形式残余181から全尽Cl/2や−30無条件排除を捏造しない |

## R2-01：MID/HIGH、C189まで（このルートだけから後退）

| 主張・節目 | 今の証拠品と場所 | 判定 | 2周目の具体的扱い |
|---|---|---|---|
| same source・整数四根・signed Ward・Gaussianの共通幹 | [E3](proofs/earliest-foundations/E3-selected-physical-kummer.md)、[S230](proofs/active-ancestors/S230.md)、[S231](proofs/active-ancestors/S231.md)、[S232](proofs/active-ancestors/S232.md)、[S233/S237/S240](proofs/C195-upstream/S233.md)、[S243](proofs/active-ancestors/S243.md)、[S251](proofs/active-ancestors/S251.md)、[S253](proofs/active-ancestors/S253.md)、[S263/S268/S269](proofs/C195-upstream/S268.md)、[C195](proofs/C195-canonical-source.md) | **G/V** | 昔の欠落候補**S230はすでに収載**。重複アップ不要。独立数学監査は別 |
| TRUE四GOOD/critical-H TOP＋全PROPER | [S270](proofs/foundations/S270.md)、[S258〜267](proofs/active-ancestors/S258.md)、[S275](proofs/active-ancestors/S275.md)、[S316](proofs/active-ancestors/S316.md)、[S318](proofs/active-ancestors/S318.md) | **G/V** | S275/S318等の**現在使用する補正部分**だけ保持。S274単独の旧étale/twist探索の丸ごと移植はしない。S250の次数8補題は[S251内で再述](proofs/active-ancestors/S251.md) |
| 155/197の全基底必要下界と採択 | [C174](proofs/C195-upstream/C174.md)・[C175](proofs/active-ancestors/C175.md)・[C160](proofs/active-ancestors/C160.md)・[C185](proofs/active-ancestors/C185.md)・[C187原著](proofs/R2-uniform-thresholds.md)・[C189](proofs/active-ancestors/C189.md) | **G/V** | 昔の欠落候補**C160はすでに収載**。C160→C185のexact gcd/first-entryの同値性・適用先だけ監査。二重移植しない |
| S252が使う外部有効性定理 | [S252](proofs/active-ancestors/S252.md) | **G/X** | **Bérczes等 Theorem 2.1(i)** の正確な外部原典・代入仮定を短く記録。外部論文全文は上げない |
| 旧finite-odd/generic枝 | [S121〜126](proofs/active-ancestors/S121.md)、[Section13](proofs/earliest-foundations/BranchB-Section13.md)、[Section16](proofs/earliest-foundations/BranchB-Section16.md)、[S194〜196](proofs/active-ancestors/S194.md) | **G/D** | Section16非平方原著も**既収載**。現在のpositive source/point-only主張に必要な範囲だけ。旧generic rank1を特殊化へ無条件転用しない |
| strict相関上界 <75% | **現行未証明**、[S270/C189 scope](S270-C189-SCOPE-CROSSCHECK.md) | **O** | **数学が未完成なので、既存Driveの「完成原証明」として取り込まない**。新研究もしない |

## PR #1854の完成判定と2周目の「追加物」仕分け

| 分類 | 具体的な次の物 | 現状 |
|---|---|---|
| **今すぐ新しい原著を移植すべきと断定できるもの** | **現時点で具体名0件**。数が0と証明したわけではない | 対象の全証明親の数学的最小閉包は未認証 |
| **2周目最優先：既存原著の接続確認** | 35EX-21/31⇄E3の原始標識・同じindexed source、R3のrow344〜349に本当に必要な親、R2のC160→C185、S250→S251 | **追加が必要と分かった具体的原著だけ別PRへ** |
| **2周目最優先：外部一次定理の出典ノート** | row393 de la Maza、S252 Bérczes | 全文アップではなく定理番号、仮定、適用・未照合事項のノート |
| **Drive参照のみでよい** | 大規模計算ZIP／検算ログ／固定例S242／旧条件付きgeneric・finite-oddの未使用部分／古いNO-GO障壁 | 今あるGitHub原著を削除しない |
| **移植してはいけない「未完成の結論」** | R3 −30無条件排除、全LOW排除、R2 strict upper、Branch B全排除 | **存在を確認できない完成証明を仮定しない** |

**この表を作るためにR1〜R5の99個のルートを再棚卸しする必要はない。** このPRの[全ファイル一覧](PR1854-ALL-CHANGED-FILES.md)は既存の物理的資産の棚卸しとしてそのまま残し、**2周目の収載判定は常にこの2根専用表を優先**する。研究対象row394以降、main、Google Drive R0/NEXT、新しいPRは触れない。
