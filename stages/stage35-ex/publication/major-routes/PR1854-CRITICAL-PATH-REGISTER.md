# PR #1854｜最小ルートに該当する原著・補助・旧枝の個別一覧

> **これが先に読む一覧表です。** [PR全1106変更ファイルを1件ずつ記載した原本](PR1854-ALL-CHANGED-FILES.md)から、数学原著と最新の補助枝を抽出し、最小研究系譜への関係で区分。**既にGitHubに入っている資料**の区分であり、これからアップロードする候補一覧ではない。2026-11-09、棚卸し基準head `474b725cf9ec3fd5b0b58e177aaef6642380c06a`。
>
> **判定は「本線に見える原著／現在使用する補助／旧条件枝／非主鎖／本文精査待ち」の整理で、厳密な最小依存証明の完了を意味しない。** 同じ命題が後続原著内に再証明されていれば独立原著の追加は不要。

## 最小研究ルートとこの一覧の関係

1. **共通主幹 A0**：物理E3・四平方・四根／分母・同一source・signed Ward／Gaussian。S270はR2の四TOP入口。既存GitHub35EX-21/31はこのPRの「追加ファイル」ではない。
2. **R3主幹 A1**：LOW採用排除と±18/Ward/±30を経たrow393。未解決の−30をPASSとしない。
3. **R2主幹 A2**：protected TOP＋ALL PROPER、155/197下界、C189採択。strict相関上界は未証明。
4. **B**：現在の主張の適用範囲・訂正に必要な場合だけ持つ最新側枝。**C・D・G**の古い分岐・未判定原著は、現在の使用箇所を発見するまで「必須」と数えない。
5. **E 計算／F 索引**は[全件台帳](PR1854-ALL-CHANGED-FILES.md)で区別。計算原物の今後の追加はDrive参照で可。


## A0｜共通・物理原著／source主鎖（全件台帳31件）

| ID | このPRにある原著パス | 2周目の判断 |
|---:|---|---|
| 0569 | [`materials/original-source-exclusions/parents/S263.md`](../../materials/original-source-exclusions/parents/S263.md) | GitHub既収載：重複アップ不要 |
| 0570 | [`materials/original-source-exclusions/parents/S264.txt`](../../materials/original-source-exclusions/parents/S264.txt) | GitHub既収載：重複アップ不要 |
| 0893 | [`publication/major-routes/proofs/C195-canonical-source.md`](./proofs/C195-canonical-source.md) | GitHub既収載：重複アップ不要 |
| 0897 | [`publication/major-routes/proofs/C195-upstream/R1-228.md`](./proofs/C195-upstream/R1-228.md) | GitHub既収載：重複アップ不要 |
| 0898 | [`publication/major-routes/proofs/C195-upstream/S233.md`](./proofs/C195-upstream/S233.md) | GitHub既収載：重複アップ不要 |
| 0899 | [`publication/major-routes/proofs/C195-upstream/S237.md`](./proofs/C195-upstream/S237.md) | GitHub既収載：重複アップ不要 |
| 0900 | [`publication/major-routes/proofs/C195-upstream/S240.md`](./proofs/C195-upstream/S240.md) | GitHub既収載：重複アップ不要 |
| 0901 | [`publication/major-routes/proofs/C195-upstream/S268.md`](./proofs/C195-upstream/S268.md) | GitHub既収載：重複アップ不要 |
| 0902 | [`publication/major-routes/proofs/C195-upstream/S269.md`](./proofs/C195-upstream/S269.md) | GitHub既収載：重複アップ不要 |
| 0903 | [`publication/major-routes/proofs/C195-upstream/S289.md`](./proofs/C195-upstream/S289.md) | GitHub既収載：重複アップ不要 |
| 0904 | [`publication/major-routes/proofs/C195-upstream/S290.md`](./proofs/C195-upstream/S290.md) | GitHub既収載：重複アップ不要 |
| 0947 | [`publication/major-routes/proofs/active-ancestors/S230.md`](./proofs/active-ancestors/S230.md) | GitHub既収載：重複アップ不要 |
| 0948 | [`publication/major-routes/proofs/active-ancestors/S231.md`](./proofs/active-ancestors/S231.md) | GitHub既収載：重複アップ不要 |
| 0949 | [`publication/major-routes/proofs/active-ancestors/S232.md`](./proofs/active-ancestors/S232.md) | GitHub既収載：重複アップ不要 |
| 0954 | [`publication/major-routes/proofs/active-ancestors/S243.md`](./proofs/active-ancestors/S243.md) | GitHub既収載：重複アップ不要 |
| 0955 | [`publication/major-routes/proofs/active-ancestors/S251.md`](./proofs/active-ancestors/S251.md) | GitHub既収載：重複アップ不要 |
| 0956 | [`publication/major-routes/proofs/active-ancestors/S252.md`](./proofs/active-ancestors/S252.md) | GitHub既収載：重複アップ不要 |
| 0957 | [`publication/major-routes/proofs/active-ancestors/S253.md`](./proofs/active-ancestors/S253.md) | GitHub既収載：重複アップ不要 |
| 0958 | [`publication/major-routes/proofs/active-ancestors/S254.md`](./proofs/active-ancestors/S254.md) | GitHub既収載：重複アップ不要 |
| 0961 | [`publication/major-routes/proofs/active-ancestors/S256.md`](./proofs/active-ancestors/S256.md) | GitHub既収載：重複アップ不要 |
| 0962 | [`publication/major-routes/proofs/active-ancestors/S257.md`](./proofs/active-ancestors/S257.md) | GitHub既収載：重複アップ不要 |
| 0963 | [`publication/major-routes/proofs/active-ancestors/S258.md`](./proofs/active-ancestors/S258.md) | GitHub既収載：重複アップ不要 |
| 0964 | [`publication/major-routes/proofs/active-ancestors/S259.md`](./proofs/active-ancestors/S259.md) | GitHub既収載：重複アップ不要 |
| 0965 | [`publication/major-routes/proofs/active-ancestors/S260.md`](./proofs/active-ancestors/S260.md) | GitHub既収載：重複アップ不要 |
| 0966 | [`publication/major-routes/proofs/active-ancestors/S261.md`](./proofs/active-ancestors/S261.md) | GitHub既収載：重複アップ不要 |
| 0967 | [`publication/major-routes/proofs/active-ancestors/S262.md`](./proofs/active-ancestors/S262.md) | GitHub既収載：重複アップ不要 |
| 0968 | [`publication/major-routes/proofs/active-ancestors/S265.md`](./proofs/active-ancestors/S265.md) | GitHub既収載：重複アップ不要 |
| 0969 | [`publication/major-routes/proofs/active-ancestors/S266.md`](./proofs/active-ancestors/S266.md) | GitHub既収載：重複アップ不要 |
| 0970 | [`publication/major-routes/proofs/active-ancestors/S267.md`](./proofs/active-ancestors/S267.md) | GitHub既収載：重複アップ不要 |
| 0985 | [`publication/major-routes/proofs/earliest-foundations/E3-selected-physical-kummer.md`](./proofs/earliest-foundations/E3-selected-physical-kummer.md) | GitHub既収載：重複アップ不要 |
| 0992 | [`publication/major-routes/proofs/foundations/S264.md`](./proofs/foundations/S264.md) | GitHub既収載：重複アップ不要 |

## A1｜R3-07・LOW主鎖（全件台帳53件）

| ID | このPRにある原著パス | 2周目の判断 |
|---:|---|---|
| 0276 | [`materials/classgroup-and-different/proofs/row385.md`](../../materials/classgroup-and-different/proofs/row385.md) | GitHub既収載：重複アップ不要 |
| 0277 | [`materials/classgroup-and-different/proofs/row386.md`](../../materials/classgroup-and-different/proofs/row386.md) | GitHub既収載：重複アップ不要 |
| 0278 | [`materials/classgroup-and-different/proofs/row387.md`](../../materials/classgroup-and-different/proofs/row387.md) | GitHub既収載：重複アップ不要 |
| 0279 | [`materials/classgroup-and-different/proofs/row388.md`](../../materials/classgroup-and-different/proofs/row388.md) | GitHub既収載：重複アップ不要 |
| 0280 | [`materials/classgroup-and-different/proofs/row389.md`](../../materials/classgroup-and-different/proofs/row389.md) | GitHub既収載：重複アップ不要 |
| 0281 | [`materials/classgroup-and-different/proofs/row390.md`](../../materials/classgroup-and-different/proofs/row390.md) | GitHub既収載：重複アップ不要 |
| 0282 | [`materials/classgroup-and-different/proofs/row391.md`](../../materials/classgroup-and-different/proofs/row391.md) | GitHub既収載：重複アップ不要 |
| 0283 | [`materials/classgroup-and-different/proofs/row392.md`](../../materials/classgroup-and-different/proofs/row392.md) | GitHub既収載：重複アップ不要 |
| 0284 | [`materials/classgroup-and-different/proofs/row393.md`](../../materials/classgroup-and-different/proofs/row393.md) | GitHub既収載：重複アップ不要 |
| 0368 | [`materials/negative30-mw-selmer/row371/STAGE35EX_R3_07_ROW371_SIGNED30_LOG31_RANK5_20261106.md`](../../materials/negative30-mw-selmer/row371/STAGE35EX_R3_07_ROW371_SIGNED30_LOG31_RANK5_20261106.md) | GitHub既収載：重複アップ不要 |
| 0375 | [`materials/negative30-mw-selmer/row372/PROOF.txt`](../../materials/negative30-mw-selmer/row372/PROOF.txt) | GitHub既収載：重複アップ不要 |
| 0414 | [`materials/negative30-mw-selmer/row377/PROOF.md`](../../materials/negative30-mw-selmer/row377/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0419 | [`materials/negative30-mw-selmer/row378/PROOF.md`](../../materials/negative30-mw-selmer/row378/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0425 | [`materials/negative30-mw-selmer/row379/PROOF.md`](../../materials/negative30-mw-selmer/row379/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0433 | [`materials/negative30-mw-selmer/row380/PROOF.md`](../../materials/negative30-mw-selmer/row380/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0450 | [`materials/negative30-mw-selmer/row381/PROOF.md`](../../materials/negative30-mw-selmer/row381/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0483 | [`materials/negative30-mw-selmer/row382/PROOF.md`](../../materials/negative30-mw-selmer/row382/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0501 | [`materials/negative30-mw-selmer/row383/PROOF.md`](../../materials/negative30-mw-selmer/row383/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0514 | [`materials/negative30-mw-selmer/row384/PROOF.md`](../../materials/negative30-mw-selmer/row384/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0566 | [`materials/original-source-exclusions/parents/C35-11/PROOF.md`](../../materials/original-source-exclusions/parents/C35-11/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0567 | [`materials/original-source-exclusions/parents/C35-118/export.txt`](../../materials/original-source-exclusions/parents/C35-118/export.txt) | GitHub既収載：重複アップ不要 |
| 0568 | [`materials/original-source-exclusions/parents/C35-12/PROOF.md`](../../materials/original-source-exclusions/parents/C35-12/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0571 | [`materials/original-source-exclusions/parents/row339-PROOF.md`](../../materials/original-source-exclusions/parents/row339-PROOF.md) | GitHub既収載：重複アップ不要 |
| 0573 | [`materials/original-source-exclusions/parents/row364/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105.md`](../../materials/original-source-exclusions/parents/row364/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105.md) | GitHub既収載：重複アップ不要 |
| 0576 | [`materials/original-source-exclusions/parents/row365/REPORT.md`](../../materials/original-source-exclusions/parents/row365/REPORT.md) | GitHub既収載：重複アップ不要 |
| 0592 | [`materials/original-source-exclusions/parents/row370-PROOF.md`](../../materials/original-source-exclusions/parents/row370-PROOF.md) | GitHub既収載：重複アップ不要 |
| 0593 | [`materials/original-source-exclusions/parents/row373-PROOF.md`](../../materials/original-source-exclusions/parents/row373-PROOF.md) | GitHub既収載：重複アップ不要 |
| 0594 | [`materials/original-source-exclusions/parents/row374-PROOF.md`](../../materials/original-source-exclusions/parents/row374-PROOF.md) | GitHub既収載：重複アップ不要 |
| 0595 | [`materials/original-source-exclusions/parents/row375-PROOF.md`](../../materials/original-source-exclusions/parents/row375-PROOF.md) | GitHub既収載：重複アップ不要 |
| 0608 | [`materials/original-source-exclusions/row367/REPORT.md`](../../materials/original-source-exclusions/row367/REPORT.md) | GitHub既収載：重複アップ不要 |
| 0628 | [`materials/original-source-exclusions/row367/parent_evidence/ROW366_PROOF.md`](../../materials/original-source-exclusions/row367/parent_evidence/ROW366_PROOF.md) | GitHub既収載：重複アップ不要 |
| 0639 | [`materials/original-source-exclusions/row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md`](../../materials/original-source-exclusions/row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md) | GitHub既収載：重複アップ不要 |
| 0646 | [`materials/original-source-exclusions/row369/STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER_20261106.md`](../../materials/original-source-exclusions/row369/STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER_20261106.md) | GitHub既収載：重複アップ不要 |
| 0649 | [`materials/original-source-exclusions/row376/PROOF.md`](../../materials/original-source-exclusions/row376/PROOF.md) | GitHub既収載：重複アップ不要 |
| 0669 | [`materials/selmer18-parent-chain/objects/01d05437afc6fa87-PROOF_C2_TRUE_LOCAL_KUMMER_DIMENSIONS_JA.md`](../../materials/selmer18-parent-chain/objects/01d05437afc6fa87-PROOF_C2_TRUE_LOCAL_KUMMER_DIMENSIONS_JA.md) | GitHub既収載：重複アップ不要 |
| 0675 | [`materials/selmer18-parent-chain/objects/065312b270b4546a-ROW339_ORIGINAL_PROOF.md`](../../materials/selmer18-parent-chain/objects/065312b270b4546a-ROW339_ORIGINAL_PROOF.md) | GitHub既収載：重複アップ不要 |
| 0683 | [`materials/selmer18-parent-chain/objects/14cbdac1663cc15d-PROOF_R3_07_FIVE_ODD_BAD_TRUE_KUMMER_GENERATORS_JA.md`](../../materials/selmer18-parent-chain/objects/14cbdac1663cc15d-PROOF_R3_07_FIVE_ODD_BAD_TRUE_KUMMER_GENERATORS_JA.md) | GitHub既収載：重複アップ不要 |
| 0726 | [`materials/selmer18-parent-chain/objects/5fd888550f0b7d57-PROOF_C2_INFINITY_RANK7_AND_TRUE_FAKE_KERNEL_JA.md`](../../materials/selmer18-parent-chain/objects/5fd888550f0b7d57-PROOF_C2_INFINITY_RANK7_AND_TRUE_FAKE_KERNEL_JA.md) | GitHub既収載：重複アップ不要 |
| 0759 | [`materials/selmer18-parent-chain/objects/91c82ae590d162c6-R1_239_SOURCE_ADAPTER.txt`](../../materials/selmer18-parent-chain/objects/91c82ae590d162c6-R1_239_SOURCE_ADAPTER.txt) | GitHub既収載：重複アップ不要 |
| 0778 | [`materials/selmer18-parent-chain/objects/b5f1e7a35902bcaa-ROW355_ORIGINAL_PROOF.md`](../../materials/selmer18-parent-chain/objects/b5f1e7a35902bcaa-ROW355_ORIGINAL_PROOF.md) | GitHub既収載：重複アップ不要 |
| 0810 | [`materials/selmer18-parent-chain/objects/e17450d343fede67-ROW359_FROZEN_PROOF.md`](../../materials/selmer18-parent-chain/objects/e17450d343fede67-ROW359_FROZEN_PROOF.md) | GitHub既収載：重複アップ不要 |
| 0832 | [`materials/selmer18-parent-chain/proofs/row361.md`](../../materials/selmer18-parent-chain/proofs/row361.md) | GitHub既収載：重複アップ不要 |
| 0833 | [`materials/selmer18-parent-chain/proofs/row363.md`](../../materials/selmer18-parent-chain/proofs/row363.md) | GitHub既収載：重複アップ不要 |
| 0907 | [`publication/major-routes/proofs/R3-18-upstream/row342.md`](./proofs/R3-18-upstream/row342.md) | GitHub既収載：重複アップ不要 |
| 0908 | [`publication/major-routes/proofs/R3-18-upstream/row343.md`](./proofs/R3-18-upstream/row343.md) | GitHub既収載：重複アップ不要 |
| 0909 | [`publication/major-routes/proofs/R3-18-upstream/row350.md`](./proofs/R3-18-upstream/row350.md) | GitHub既収載：重複アップ不要 |
| 0910 | [`publication/major-routes/proofs/R3-18-upstream/row351.md`](./proofs/R3-18-upstream/row351.md) | GitHub既収載：重複アップ不要 |
| 0952 | [`publication/major-routes/proofs/active-ancestors/S238.md`](./proofs/active-ancestors/S238.md) | GitHub既収載：重複アップ不要 |
| 0980 | [`publication/major-routes/proofs/active-ancestors/S321.md`](./proofs/active-ancestors/S321.md) | GitHub既収載：重複アップ不要 |
| 0981 | [`publication/major-routes/proofs/active-ancestors/S322.md`](./proofs/active-ancestors/S322.md) | GitHub既収載：重複アップ不要 |
| 0986 | [`publication/major-routes/proofs/foundations/C181.md`](./proofs/foundations/C181.md) | GitHub既収載：重複アップ不要 |
| 0987 | [`publication/major-routes/proofs/foundations/C183.md`](./proofs/foundations/C183.md) | GitHub既収載：重複アップ不要 |
| 0989 | [`publication/major-routes/proofs/foundations/R5-C220.md`](./proofs/foundations/R5-C220.md) | GitHub既収載：重複アップ不要 |

## A2｜R2-01・MID/HIGH主鎖（全件台帳5件）

| ID | このPRにある原著パス | 2周目の判断 |
|---:|---|---|
| 0906 | [`publication/major-routes/proofs/R2-uniform-thresholds.md`](./proofs/R2-uniform-thresholds.md) | GitHub既収載：重複アップ不要 |
| 0912 | [`publication/major-routes/proofs/active-ancestors/C175.md`](./proofs/active-ancestors/C175.md) | GitHub既収載：重複アップ不要 |
| 0913 | [`publication/major-routes/proofs/active-ancestors/C185.md`](./proofs/active-ancestors/C185.md) | GitHub既収載：重複アップ不要 |
| 0914 | [`publication/major-routes/proofs/active-ancestors/C189.md`](./proofs/active-ancestors/C189.md) | GitHub既収載：重複アップ不要 |
| 0993 | [`publication/major-routes/proofs/foundations/S270.md`](./proofs/foundations/S270.md) | GitHub既収載：重複アップ不要 |

## B｜現行訂正／適用条件／補助枝（全件台帳41件）

| ID | このPRにある原著パス | 2周目の判断 |
|---:|---|---|
| 0013 | [`materials/classgroup-and-different/audits/row385.txt`](../../materials/classgroup-and-different/audits/row385.txt) | 必要な訂正・引用範囲のみ維持 |
| 0014 | [`materials/classgroup-and-different/audits/row386.txt`](../../materials/classgroup-and-different/audits/row386.txt) | 必要な訂正・引用範囲のみ維持 |
| 0015 | [`materials/classgroup-and-different/audits/row387.txt`](../../materials/classgroup-and-different/audits/row387.txt) | 必要な訂正・引用範囲のみ維持 |
| 0016 | [`materials/classgroup-and-different/audits/row388.txt`](../../materials/classgroup-and-different/audits/row388.txt) | 必要な訂正・引用範囲のみ維持 |
| 0017 | [`materials/classgroup-and-different/audits/row389.txt`](../../materials/classgroup-and-different/audits/row389.txt) | 必要な訂正・引用範囲のみ維持 |
| 0018 | [`materials/classgroup-and-different/audits/row390.txt`](../../materials/classgroup-and-different/audits/row390.txt) | 必要な訂正・引用範囲のみ維持 |
| 0019 | [`materials/classgroup-and-different/audits/row391.txt`](../../materials/classgroup-and-different/audits/row391.txt) | 必要な訂正・引用範囲のみ維持 |
| 0020 | [`materials/classgroup-and-different/audits/row392.txt`](../../materials/classgroup-and-different/audits/row392.txt) | 必要な訂正・引用範囲のみ維持 |
| 0021 | [`materials/classgroup-and-different/audits/row393.txt`](../../materials/classgroup-and-different/audits/row393.txt) | 必要な訂正・引用範囲のみ維持 |
| 0343 | [`materials/negative30-mw-selmer/audits/row370.txt`](../../materials/negative30-mw-selmer/audits/row370.txt) | 必要な訂正・引用範囲のみ維持 |
| 0344 | [`materials/negative30-mw-selmer/audits/row371.txt`](../../materials/negative30-mw-selmer/audits/row371.txt) | 必要な訂正・引用範囲のみ維持 |
| 0345 | [`materials/negative30-mw-selmer/audits/row372.txt`](../../materials/negative30-mw-selmer/audits/row372.txt) | 必要な訂正・引用範囲のみ維持 |
| 0346 | [`materials/negative30-mw-selmer/audits/row373.md`](../../materials/negative30-mw-selmer/audits/row373.md) | 必要な訂正・引用範囲のみ維持 |
| 0347 | [`materials/negative30-mw-selmer/audits/row374.md`](../../materials/negative30-mw-selmer/audits/row374.md) | 必要な訂正・引用範囲のみ維持 |
| 0348 | [`materials/negative30-mw-selmer/audits/row375.md`](../../materials/negative30-mw-selmer/audits/row375.md) | 必要な訂正・引用範囲のみ維持 |
| 0349 | [`materials/negative30-mw-selmer/audits/row378.txt`](../../materials/negative30-mw-selmer/audits/row378.txt) | 必要な訂正・引用範囲のみ維持 |
| 0350 | [`materials/negative30-mw-selmer/audits/row379.txt`](../../materials/negative30-mw-selmer/audits/row379.txt) | 必要な訂正・引用範囲のみ維持 |
| 0351 | [`materials/negative30-mw-selmer/audits/row380.txt`](../../materials/negative30-mw-selmer/audits/row380.txt) | 必要な訂正・引用範囲のみ維持 |
| 0352 | [`materials/negative30-mw-selmer/audits/row381.txt`](../../materials/negative30-mw-selmer/audits/row381.txt) | 必要な訂正・引用範囲のみ維持 |
| 0353 | [`materials/negative30-mw-selmer/audits/row382.txt`](../../materials/negative30-mw-selmer/audits/row382.txt) | 必要な訂正・引用範囲のみ維持 |
| 0354 | [`materials/negative30-mw-selmer/audits/row383.txt`](../../materials/negative30-mw-selmer/audits/row383.txt) | 必要な訂正・引用範囲のみ維持 |
| 0355 | [`materials/negative30-mw-selmer/audits/row384.txt`](../../materials/negative30-mw-selmer/audits/row384.txt) | 必要な訂正・引用範囲のみ維持 |
| 0537 | [`materials/original-source-exclusions/audits/row367.md`](../../materials/original-source-exclusions/audits/row367.md) | 必要な訂正・引用範囲のみ維持 |
| 0538 | [`materials/original-source-exclusions/audits/row368.md`](../../materials/original-source-exclusions/audits/row368.md) | 必要な訂正・引用範囲のみ維持 |
| 0539 | [`materials/original-source-exclusions/audits/row369.txt`](../../materials/original-source-exclusions/audits/row369.txt) | 必要な訂正・引用範囲のみ維持 |
| 0540 | [`materials/original-source-exclusions/audits/row376.md`](../../materials/original-source-exclusions/audits/row376.md) | 必要な訂正・引用範囲のみ維持 |
| 0663 | [`materials/selmer18-parent-chain/audits/row363.md`](../../materials/selmer18-parent-chain/audits/row363.md) | 必要な訂正・引用範囲のみ維持 |
| 0664 | [`materials/selmer18-parent-chain/audits/row364-independent-check.py`](../../materials/selmer18-parent-chain/audits/row364-independent-check.py) | 必要な訂正・引用範囲のみ維持 |
| 0665 | [`materials/selmer18-parent-chain/audits/row364.md`](../../materials/selmer18-parent-chain/audits/row364.md) | 必要な訂正・引用範囲のみ維持 |
| 0894 | [`publication/major-routes/proofs/C195-upstream/C174.md`](./proofs/C195-upstream/C174.md) | 必要な訂正・引用範囲のみ維持 |
| 0896 | [`publication/major-routes/proofs/C195-upstream/R1-223.md`](./proofs/C195-upstream/R1-223.md) | 必要な訂正・引用範囲のみ維持 |
| 0911 | [`publication/major-routes/proofs/active-ancestors/C160.md`](./proofs/active-ancestors/C160.md) | 必要な訂正・引用範囲のみ維持 |
| 0959 | [`publication/major-routes/proofs/active-ancestors/S255-current.md`](./proofs/active-ancestors/S255-current.md) | 必要な訂正・引用範囲のみ維持 |
| 0960 | [`publication/major-routes/proofs/active-ancestors/S255.md`](./proofs/active-ancestors/S255.md) | 必要な訂正・引用範囲のみ維持 |
| 0971 | [`publication/major-routes/proofs/active-ancestors/S275.md`](./proofs/active-ancestors/S275.md) | 必要な訂正・引用範囲のみ維持 |
| 0977 | [`publication/major-routes/proofs/active-ancestors/S316.md`](./proofs/active-ancestors/S316.md) | 必要な訂正・引用範囲のみ維持 |
| 0978 | [`publication/major-routes/proofs/active-ancestors/S318.md`](./proofs/active-ancestors/S318.md) | 必要な訂正・引用範囲のみ維持 |
| 0979 | [`publication/major-routes/proofs/active-ancestors/S320.md`](./proofs/active-ancestors/S320.md) | 必要な訂正・引用範囲のみ維持 |
| 0988 | [`publication/major-routes/proofs/foundations/R5-C212.md`](./proofs/foundations/R5-C212.md) | 必要な訂正・引用範囲のみ維持 |
| 0990 | [`publication/major-routes/proofs/foundations/R5-C224-erratum.md`](./proofs/foundations/R5-C224-erratum.md) | 必要な訂正・引用範囲のみ維持 |
| 0991 | [`publication/major-routes/proofs/foundations/R5-P112-rebin.md`](./proofs/foundations/R5-P112-rebin.md) | 必要な訂正・引用範囲のみ維持 |

## C｜古い条件付き祖先（全件台帳37件）

※ 古いgeneric / finite-odd研究は歴史的親でも、R3/R2現在の各定理の必要親とは限らない。

| ID | このPRにある原著パス | 2周目の判断 |
|---:|---|---|
| 0915 | [`publication/major-routes/proofs/active-ancestors/S121.md`](./proofs/active-ancestors/S121.md) | 使用箇所の立証まで必須扱いしない |
| 0916 | [`publication/major-routes/proofs/active-ancestors/S122.md`](./proofs/active-ancestors/S122.md) | 使用箇所の立証まで必須扱いしない |
| 0917 | [`publication/major-routes/proofs/active-ancestors/S123.md`](./proofs/active-ancestors/S123.md) | 使用箇所の立証まで必須扱いしない |
| 0918 | [`publication/major-routes/proofs/active-ancestors/S124.md`](./proofs/active-ancestors/S124.md) | 使用箇所の立証まで必須扱いしない |
| 0919 | [`publication/major-routes/proofs/active-ancestors/S125.md`](./proofs/active-ancestors/S125.md) | 使用箇所の立証まで必須扱いしない |
| 0920 | [`publication/major-routes/proofs/active-ancestors/S126.md`](./proofs/active-ancestors/S126.md) | 使用箇所の立証まで必須扱いしない |
| 0921 | [`publication/major-routes/proofs/active-ancestors/S190.md`](./proofs/active-ancestors/S190.md) | 使用箇所の立証まで必須扱いしない |
| 0922 | [`publication/major-routes/proofs/active-ancestors/S191.md`](./proofs/active-ancestors/S191.md) | 使用箇所の立証まで必須扱いしない |
| 0923 | [`publication/major-routes/proofs/active-ancestors/S192.md`](./proofs/active-ancestors/S192.md) | 使用箇所の立証まで必須扱いしない |
| 0924 | [`publication/major-routes/proofs/active-ancestors/S193.md`](./proofs/active-ancestors/S193.md) | 使用箇所の立証まで必須扱いしない |
| 0925 | [`publication/major-routes/proofs/active-ancestors/S194.md`](./proofs/active-ancestors/S194.md) | 使用箇所の立証まで必須扱いしない |
| 0926 | [`publication/major-routes/proofs/active-ancestors/S195.md`](./proofs/active-ancestors/S195.md) | 使用箇所の立証まで必須扱いしない |
| 0927 | [`publication/major-routes/proofs/active-ancestors/S196.md`](./proofs/active-ancestors/S196.md) | 使用箇所の立証まで必須扱いしない |
| 0928 | [`publication/major-routes/proofs/active-ancestors/S197.md`](./proofs/active-ancestors/S197.md) | 使用箇所の立証まで必須扱いしない |
| 0929 | [`publication/major-routes/proofs/active-ancestors/S198.md`](./proofs/active-ancestors/S198.md) | 使用箇所の立証まで必須扱いしない |
| 0930 | [`publication/major-routes/proofs/active-ancestors/S199.md`](./proofs/active-ancestors/S199.md) | 使用箇所の立証まで必須扱いしない |
| 0931 | [`publication/major-routes/proofs/active-ancestors/S200.md`](./proofs/active-ancestors/S200.md) | 使用箇所の立証まで必須扱いしない |
| 0932 | [`publication/major-routes/proofs/active-ancestors/S201.md`](./proofs/active-ancestors/S201.md) | 使用箇所の立証まで必須扱いしない |
| 0933 | [`publication/major-routes/proofs/active-ancestors/S202.md`](./proofs/active-ancestors/S202.md) | 使用箇所の立証まで必須扱いしない |
| 0934 | [`publication/major-routes/proofs/active-ancestors/S213.md`](./proofs/active-ancestors/S213.md) | 使用箇所の立証まで必須扱いしない |
| 0935 | [`publication/major-routes/proofs/active-ancestors/S218.md`](./proofs/active-ancestors/S218.md) | 使用箇所の立証まで必須扱いしない |
| 0936 | [`publication/major-routes/proofs/active-ancestors/S219.md`](./proofs/active-ancestors/S219.md) | 使用箇所の立証まで必須扱いしない |
| 0937 | [`publication/major-routes/proofs/active-ancestors/S220.md`](./proofs/active-ancestors/S220.md) | 使用箇所の立証まで必須扱いしない |
| 0938 | [`publication/major-routes/proofs/active-ancestors/S221.md`](./proofs/active-ancestors/S221.md) | 使用箇所の立証まで必須扱いしない |
| 0939 | [`publication/major-routes/proofs/active-ancestors/S222.md`](./proofs/active-ancestors/S222.md) | 使用箇所の立証まで必須扱いしない |
| 0940 | [`publication/major-routes/proofs/active-ancestors/S223.md`](./proofs/active-ancestors/S223.md) | 使用箇所の立証まで必須扱いしない |
| 0941 | [`publication/major-routes/proofs/active-ancestors/S224.md`](./proofs/active-ancestors/S224.md) | 使用箇所の立証まで必須扱いしない |
| 0942 | [`publication/major-routes/proofs/active-ancestors/S225.md`](./proofs/active-ancestors/S225.md) | 使用箇所の立証まで必須扱いしない |
| 0943 | [`publication/major-routes/proofs/active-ancestors/S226.md`](./proofs/active-ancestors/S226.md) | 使用箇所の立証まで必須扱いしない |
| 0944 | [`publication/major-routes/proofs/active-ancestors/S227.md`](./proofs/active-ancestors/S227.md) | 使用箇所の立証まで必須扱いしない |
| 0945 | [`publication/major-routes/proofs/active-ancestors/S228.md`](./proofs/active-ancestors/S228.md) | 使用箇所の立証まで必須扱いしない |
| 0946 | [`publication/major-routes/proofs/active-ancestors/S229.md`](./proofs/active-ancestors/S229.md) | 使用箇所の立証まで必須扱いしない |
| 0950 | [`publication/major-routes/proofs/active-ancestors/S234.md`](./proofs/active-ancestors/S234.md) | 使用箇所の立証まで必須扱いしない |
| 0951 | [`publication/major-routes/proofs/active-ancestors/S235.md`](./proofs/active-ancestors/S235.md) | 使用箇所の立証まで必須扱いしない |
| 0982 | [`publication/major-routes/proofs/earliest-foundations/BranchB-Section13.md`](./proofs/earliest-foundations/BranchB-Section13.md) | 使用箇所の立証まで必須扱いしない |
| 0983 | [`publication/major-routes/proofs/earliest-foundations/BranchB-Section16.md`](./proofs/earliest-foundations/BranchB-Section16.md) | 使用箇所の立証まで必須扱いしない |
| 0984 | [`publication/major-routes/proofs/earliest-foundations/E3-generic-MW.md`](./proofs/earliest-foundations/E3-generic-MW.md) | 使用箇所の立証まで必須扱いしない |

## G｜内容別再分類待ちの数学資料（全件台帳32件）

※ 「未判定」は「未収載」ではなく、PRにある本文の使用箇所・役割が未確定という意味。

| ID | このPRにある原著パス | 2周目の判断 |
|---:|---|---|
| 0316 | [`materials/hcs-crosslane-c117-119/sources/R3_all4_proof.txt`](../../materials/hcs-crosslane-c117-119/sources/R3_all4_proof.txt) | 採用命題との対応を要確認 |
| 0321 | [`materials/hcs-crosslane-c117-119/sources/R3_p3_proof.txt`](../../materials/hcs-crosslane-c117-119/sources/R3_p3_proof.txt) | 採用命題との対応を要確認 |
| 0326 | [`materials/hcs-crosslane-c117-119/sources/R3_rank1_proof.txt`](../../materials/hcs-crosslane-c117-119/sources/R3_rank1_proof.txt) | 採用命題との対応を要確認 |
| 0331 | [`materials/hcs-crosslane-c117-119/sources/R4_tamagawa_proof.txt`](../../materials/hcs-crosslane-c117-119/sources/R4_tamagawa_proof.txt) | 採用命題との対応を要確認 |
| 0493 | [`materials/negative30-mw-selmer/row382/rational_inputs382.txt`](../../materials/negative30-mw-selmer/row382/rational_inputs382.txt) | 採用命題との対応を要確認 |
| 0686 | [`materials/selmer18-parent-chain/objects/184759f7f79f47e5-requirements.txt`](../../materials/selmer18-parent-chain/objects/184759f7f79f47e5-requirements.txt) | 採用命題との対応を要確認 |
| 0702 | [`materials/selmer18-parent-chain/objects/34d2d9226f1e8ee1-GLOBAL_PARENT_REPLAY_STDOUT.txt`](../../materials/selmer18-parent-chain/objects/34d2d9226f1e8ee1-GLOBAL_PARENT_REPLAY_STDOUT.txt) | 採用命題との対応を要確認 |
| 0709 | [`materials/selmer18-parent-chain/objects/4b09030b7c014fb6-ROW360_CURRENT_RECEIVED_INDEPENDENT_AUDIT.md`](../../materials/selmer18-parent-chain/objects/4b09030b7c014fb6-ROW360_CURRENT_RECEIVED_INDEPENDENT_AUDIT.md) | 採用命題との対応を要確認 |
| 0713 | [`materials/selmer18-parent-chain/objects/4cef508304e84c21-requirements.txt`](../../materials/selmer18-parent-chain/objects/4cef508304e84c21-requirements.txt) | 採用命題との対応を要確認 |
| 0716 | [`materials/selmer18-parent-chain/objects/508e9946a2f4bbb6-C35_122_DEDUP_EXCERPT.txt`](../../materials/selmer18-parent-chain/objects/508e9946a2f4bbb6-C35_122_DEDUP_EXCERPT.txt) | 採用命題との対応を要確認 |
| 0721 | [`materials/selmer18-parent-chain/objects/5989c218edc64f6b-quad_survivors.txt`](../../materials/selmer18-parent-chain/objects/5989c218edc64f6b-quad_survivors.txt) | 採用命題との対応を要確認 |
| 0727 | [`materials/selmer18-parent-chain/objects/5fd91320447dba8f-ROW355_INDEPENDENT_AUDIT_JA.md`](../../materials/selmer18-parent-chain/objects/5fd91320447dba8f-ROW355_INDEPENDENT_AUDIT_JA.md) | 採用命題との対応を要確認 |
| 0732 | [`materials/selmer18-parent-chain/objects/6b2136264ea83dc2-RUN_ROW353_MAIN_STDOUT.txt`](../../materials/selmer18-parent-chain/objects/6b2136264ea83dc2-RUN_ROW353_MAIN_STDOUT.txt) | 採用命題との対応を要確認 |
| 0744 | [`materials/selmer18-parent-chain/objects/7d84a940215ff5fa-ROW358_RECEIVED_INDEPENDENT_AUDIT.md`](../../materials/selmer18-parent-chain/objects/7d84a940215ff5fa-ROW358_RECEIVED_INDEPENDENT_AUDIT.md) | 採用命題との対応を要確認 |
| 0746 | [`materials/selmer18-parent-chain/objects/7e54dcb633df5b0a-STAGE35EX_R3_07_ALLMW_P163_DISK_BASECOUNT14_20261105.md`](../../materials/selmer18-parent-chain/objects/7e54dcb633df5b0a-STAGE35EX_R3_07_ALLMW_P163_DISK_BASECOUNT14_20261105.md) | 採用命題との対応を要確認 |
| 0757 | [`materials/selmer18-parent-chain/objects/8dd5f64aea15d81d-ROW352_EXACT_REPLAY_STDOUT.txt`](../../materials/selmer18-parent-chain/objects/8dd5f64aea15d81d-ROW352_EXACT_REPLAY_STDOUT.txt) | 採用命題との対応を要確認 |
| 0762 | [`materials/selmer18-parent-chain/objects/9a4c9b9de2af8517-STAGE35EX_R3_07_FINITE_EVEN_TRUE_SELMER17_20261104.md`](../../materials/selmer18-parent-chain/objects/9a4c9b9de2af8517-STAGE35EX_R3_07_FINITE_EVEN_TRUE_SELMER17_20261104.md) | 採用命題との対応を要確認 |
| 0766 | [`materials/selmer18-parent-chain/objects/a613356243ac7568-STAGE35EX_R3_07_GAUSSIAN_SCLASS_BOUND_20261104.md`](../../materials/selmer18-parent-chain/objects/a613356243ac7568-STAGE35EX_R3_07_GAUSSIAN_SCLASS_BOUND_20261104.md) | 採用命題との対応を要確認 |
| 0777 | [`materials/selmer18-parent-chain/objects/b4baf7e2619f0eec-ROW356_INDEPENDENT_AUDIT_REPORT.md`](../../materials/selmer18-parent-chain/objects/b4baf7e2619f0eec-ROW356_INDEPENDENT_AUDIT_REPORT.md) | 採用命題との対応を要確認 |
| 0783 | [`materials/selmer18-parent-chain/objects/bf11619fbd0b6610-ROW359_RECEIVED_INDEPENDENT_AUDIT.md`](../../materials/selmer18-parent-chain/objects/bf11619fbd0b6610-ROW359_RECEIVED_INDEPENDENT_AUDIT.md) | 採用命題との対応を要確認 |
| 0789 | [`materials/selmer18-parent-chain/objects/c1f93e15784763ee-cubic_survivors.txt`](../../materials/selmer18-parent-chain/objects/c1f93e15784763ee-cubic_survivors.txt) | 採用命題との対応を要確認 |
| 0798 | [`materials/selmer18-parent-chain/objects/c84962d6d248802c-requirements.txt`](../../materials/selmer18-parent-chain/objects/c84962d6d248802c-requirements.txt) | 採用命題との対応を要確認 |
| 0815 | [`materials/selmer18-parent-chain/objects/e6773cceb19ff221-RUN_PARENT352_STDOUT.txt`](../../materials/selmer18-parent-chain/objects/e6773cceb19ff221-RUN_PARENT352_STDOUT.txt) | 採用命題との対応を要確認 |
| 0821 | [`materials/selmer18-parent-chain/objects/f46e31bbdad9625b-STAGE35EX_R3_07_GLOBAL_LOCAL_FOUR_CUTS_20261104.md`](../../materials/selmer18-parent-chain/objects/f46e31bbdad9625b-STAGE35EX_R3_07_GLOBAL_LOCAL_FOUR_CUTS_20261104.md) | 採用命題との対応を要確認 |
| 0831 | [`materials/selmer18-parent-chain/objects/fffbc40432107cf0-RUN_PARENT345_STDOUT.txt`](../../materials/selmer18-parent-chain/objects/fffbc40432107cf0-RUN_PARENT345_STDOUT.txt) | 採用命題との対応を要確認 |
| 0972 | [`publication/major-routes/proofs/active-ancestors/S291.md`](./proofs/active-ancestors/S291.md) | 採用命題との対応を要確認 |
| 0973 | [`publication/major-routes/proofs/active-ancestors/S308.md`](./proofs/active-ancestors/S308.md) | 採用命題との対応を要確認 |
| 0994 | [`publication/major-routes/proofs/post-C195/C196.md`](./proofs/post-C195/C196.md) | 採用命題との対応を要確認 |
| 0995 | [`publication/major-routes/proofs/post-C195/C197.md`](./proofs/post-C195/C197.md) | 採用命題との対応を要確認 |
| 0996 | [`publication/major-routes/proofs/post-C195/C198.md`](./proofs/post-C195/C198.md) | 採用命題との対応を要確認 |
| 0997 | [`publication/major-routes/proofs/post-C195/C199.md`](./proofs/post-C195/C199.md) | 採用命題との対応を要確認 |
| 0998 | [`publication/major-routes/proofs/post-C195/C200.md`](./proofs/post-C195/C200.md) | 採用命題との対応を要確認 |

## D｜歴史・非主鎖の研究資料（全件台帳102件／ここでは数学原著のみ3件）

※ その他R1/R4/R5等の非現行レーンのルート案内は全件台帳に列挙。数学原著候補のみ下に表示。

| ID | このPRにある原著パス | 2周目の判断 |
|---:|---|---|
| 0895 | [`publication/major-routes/proofs/C195-upstream/C194.md`](./proofs/C195-upstream/C194.md) | 原則追加収載不要 |
| 0905 | [`publication/major-routes/proofs/C241-finite-local-limit.md`](./proofs/C241-finite-local-limit.md) | 原則追加収載不要 |
| 0953 | [`publication/major-routes/proofs/active-ancestors/S242.md`](./proofs/active-ancestors/S242.md) | 原則追加収載不要 |

## PR外の既存GitHub数学原著（別カウント）

| 資料 | PR差分？ | 本線との関係 |
|---|---|---|
| [35EX-21 曲面](../../35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md) | **差分ではない** | 最古の正の有理曲面 |
| [35EX-31 原始標識](../../35ex-31/primitive-source-marking-endpoint-equivalence.md) | **差分ではない** | source/marking |

## 2周目に追加するかどうかの決め方

**現在のR3-07またはR2-01の採用命題を選ぶ → 実際に使った補題の場所を確認 → 上記の既存原著または完全同値証明があれば追加しない → 必要かつ欠落する本文だけ別PR候補。** 計算原物はDriveへの出典リンクで可。古い「壁」は最新の条件・撤回に実際に必要な箇所だけ。

**非認定事項**：数学的祖先の完全閉包、外部Bérczes／de la Maza原典の適用、same-sourceとsigned Wardの標識移送、新しい数学的排除。R3 row394以降の研究は行わない。
