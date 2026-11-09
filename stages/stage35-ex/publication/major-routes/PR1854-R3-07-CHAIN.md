# R3-07：row393までに至る数学的証明鎖（PR #1854）

**第1対象：P23-LOW、R3研究経緯のrow393で停止。** [R3-07運用記録](../routes/R3-07.md)が正本への入口。ここにあるリンクは「GitHub上に原著が存在する」の確認であり、親鎖が数学的に完全に閉じたという判定ではない。新しい原証明・計算証拠は今回追加しない。

## 最終地点

- [row393の原証明](../../materials/classgroup-and-different/proofs/row393.md)、[同じ成果の限定独立監査](../../materials/classgroup-and-different/audits/row393.txt)、[外部de la Maza一次定理の未照合ゲート](ROW393-PRIMARY-THEOREM-GATE.md)。
- [R3研究経緯row330〜393](../research-records/R3-330-393.md)と[−30の論理的境界](04-minus30.md)。
- row393での形式残余181は真Cl/2次元・上界ではない。−30の無条件排除、全LOW、Branch Bは未達成。外部定理の適用仮定はSOURCE_THEOREM_VERIFICATION_PENDING。

## 対象限定のLOW排除（保存済み）

- [row367 ±18](../../materials/original-source-exclusions/row367/REPORT.md)
- [row368 Ward3/5](../../materials/original-source-exclusions/row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md)
- [row369 Ward7](../../materials/original-source-exclusions/row369/STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER_20261106.md)
- [row376 +30のみ](../../materials/original-source-exclusions/row376/PROOF.md)

row368はWard3/5列挙、row369はWard7列挙。row376は**+30だけ**であり、−30まで排除したとは扱わない。現行LOW残余は9絶対指数／16 signed枠。[LOWの対象と量化子](03-low-exclusions.md)。

## ±18：R3で使ったSelmer数学親

- [row361/362](../../materials/selmer18-parent-chain/proofs/row361.md)
- [row363](../../materials/selmer18-parent-chain/proofs/row363.md)
- [row364](../../materials/original-source-exclusions/parents/row364/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105.md)
- [row365](../../materials/original-source-exclusions/parents/row365/REPORT.md)
- [row366](../../materials/original-source-exclusions/row367/parent_evidence/ROW366_PROOF.md)

row362はrow361と同一原著なので重複しない。row351/352等のさらに古い真正Selmer→fakeの数学親は、既存GitHubオブジェクト内証明と正確な主張をまだ対応付ける必要がある。

## Ward3/5/7：既存親本文

- [S263](../../materials/original-source-exclusions/parents/S263.md)
- [C118](../../materials/original-source-exclusions/parents/C35-118/export.txt)
- [C35-11](../../materials/original-source-exclusions/parents/C35-11/PROOF.md)
- [C35-12](../../materials/original-source-exclusions/parents/C35-12/PROOF.md)
- [row339](../../materials/original-source-exclusions/parents/row339-PROOF.md)

**S238の一様2進平方類**と**S321のW5/W7同じsource分割**は、採用LOW証明に引用されるにもかかわらず、現時点でGitHub内の完全同値証明への対応未了。S322はrow369等の既存本文に必要部分が完全にあるかを先に判定する。ここを障壁文書とひとまとめにして除外しない。

## −30前段：元source必要条件・局所Kummer・階数

- [row370](../../materials/original-source-exclusions/parents/row370-PROOF.md)
- [row371](../../materials/negative30-mw-selmer/row371/STAGE35EX_R3_07_ROW371_SIGNED30_LOG31_RANK5_20261106.md)
- [row372](../../materials/negative30-mw-selmer/row372/PROOF.txt)
- [row373](../../materials/original-source-exclusions/parents/row373-PROOF.md)
- [row374](../../materials/original-source-exclusions/parents/row374-PROOF.md)
- [row375](../../materials/original-source-exclusions/parents/row375-PROOF.md)

## −30後段：R3でrow393まで進展した数学本文

- [row377](../../materials/negative30-mw-selmer/row377/PROOF.md)
- [row378](../../materials/negative30-mw-selmer/row378/PROOF.md)
- [row379](../../materials/negative30-mw-selmer/row379/PROOF.md)
- [row380](../../materials/negative30-mw-selmer/row380/PROOF.md)
- [row381](../../materials/negative30-mw-selmer/row381/PROOF.md)
- [row382](../../materials/negative30-mw-selmer/row382/PROOF.md)
- [row383](../../materials/negative30-mw-selmer/row383/PROOF.md)
- [row384](../../materials/negative30-mw-selmer/row384/PROOF.md)
- [row385](../../materials/classgroup-and-different/proofs/row385.md)
- [row386](../../materials/classgroup-and-different/proofs/row386.md)
- [row387](../../materials/classgroup-and-different/proofs/row387.md)
- [row388](../../materials/classgroup-and-different/proofs/row388.md)
- [row389](../../materials/classgroup-and-different/proofs/row389.md)
- [row390](../../materials/classgroup-and-different/proofs/row390.md)
- [row391](../../materials/classgroup-and-different/proofs/row391.md)
- [row392](../../materials/classgroup-and-different/proofs/row392.md)
- [row393](../../materials/classgroup-and-different/proofs/row393.md)

これらの各rowをすべて直前rowの形式的な論理親と主張してはいない。row377は別補助成果を含む。row381の−30排除は二次Hecke GRH条件付き、row385–393は類群Cl/2全尽性を証明していない。

## このルートの証明本文として残る確認

1. 現行で利用したLOW排除とrow393から逆向きに、**実際に使う数学的補題**を列挙して上記のGitHub証明に接続。S238/S321・row351/352・S322等は必要範囲を照合する。
2. row393のde la Maza原典Theorem 1と直後の系の仮定・係数・規約の一致を確認する。有限算術のPASSを原典確認PASSとしない。
3. 過去の不採用・障壁だけの研究は原本Drive参照で足りる。**採用結果の不可欠な親補題はGitHub原著か完全同値証明を要求**。
4. 計算コード・ZIP・期待値はユーザー指示で**後回し**。独立数学監査も別ゲート。

**現状：部分収載。数学原証明の必須総数・不足数・完了率は未確定。** [二ルートの入口](PR1854-START-HERE.md)。
