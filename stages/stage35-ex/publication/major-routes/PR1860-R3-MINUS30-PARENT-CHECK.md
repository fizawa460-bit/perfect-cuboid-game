# PR #1860｜R3-07 −30からrow393まで：数学原著本文24本の再帰所在確認

**IN PROGRESS / NOT A CLOSURE CERTIFICATE / DO NOT MERGE**。対象はR3-07のrow370〜393のみ。第１周でGitHubに入った原数学本文の再確認であり、99ルート全体の分類はしない。

## 今回実際に確認したこと

- 24件全件について **現在の #1860 ブランチから実ファイルを読み込み、存在と内容を確認**。したがってこの24行の「原著本文そのもの」は**欠落０**。ただし、24本が数学的に独立・必要・十分という結論は出していない。
- 前半のrow370～376（±30の六平方／2進Kummer／+30限定排除）と、後半row378～393（−30条件付き排除、類群・有限関係・原典照合）を分けて扱う。**row377は別の補助枝であって、row378→393の自動的必須親とは認定しない。**
- row370は既知row335/338の二点法を言及するものの、自分の本文で同じ−30に必要な六平方・31進二方向の導出を含む。古い番号が登場しただけで必須原著の追加要求にはしない。
- row393にはde la Mazaの書誌・式・有理パラメータが書かれているが、**外部定理の仮定・正規化の直接原典照合は未完**。外部PDF全文を無断でGitHubへコピーすることとは異なる。

## 各行：実在する著者数学本文、親として引用する先、限定

| row | GitHub上にある数学本文 | 直接使う／名前が出る数学親（必要性は検証途中） | 状態／未達成 |
|---|---|---|---|
| row370 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/original-source-exclusions/parents/row370-PROOF.md) | S263, S264 | AUTHOR_EXACT_PASS_INDEPENDENT_PENDING |
| row371 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row371/STAGE35EX_R3_07_ROW371_SIGNED30_LOG31_RANK5_20261106.md) | row370 | AUTHOR_EXACT_PASS_INDEPENDENT_SCOPE_AS_HISTORIC |
| row372 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row372/PROOF.txt) | row371 | SCOPED_LOCAL_KUMMER |
| row373 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/original-source-exclusions/parents/row373-PROOF.md) | row371, row372 | SCOPED_DYADIC_KUMMER |
| row374 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/original-source-exclusions/parents/row374-PROOF.md) | row373 | SCOPED_ODD_SUPPORT |
| row375 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/original-source-exclusions/parents/row375-PROOF.md) | row370, row373, row374 | MW8_10_LOWER_ONLY |
| row376 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/original-source-exclusions/row376/PROOF.md) | row370, row373, row374, row375 | PLUS30_ONLY |
| row377 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row377/PROOF.md) | 同一２ルートの必須親としては未認定 | SIDE_RESULT_AUDIT_DOCUMENT_EMPTY |
| row378 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row378/PROOF.md) | row370, row374, row375, row376, S243, S269 | ARTIN_COUPLING_NO_EXCLUSION |
| row379 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row379/PROOF.md) | row378 | HECkE_GRH_CONDITIONAL |
| row380 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row380/PROOF.md) | row373, row374, row378, row379 | CONDITIONAL_ARTIN |
| row381 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row381/PROOF.md) | row373, row374, row375, row380 | SIGNED_MINUS30_EXCLUSION_ONLY_UNDER_HECkE_GRH |
| row382 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row382/PROOF.md) | row381 | NECESSARY_HECkE_ZERO_WINDOW |
| row383 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row383/PROOF.md) | row381, row382 | NECESSARY_HECkE_ZERO_BANDS |
| row384 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/negative30-mw-selmer/row384/PROOF.md) | row381, row382, row383 | TWO_BANDS_NECESSARY_NOT_NOZERO |
| row385 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row385.md) | row381, row384 | H1_J4_LIFT_NOT_TRUE_SEL4 |
| row386 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row386.md) | row385, row373 | KUMMER_THREE_CURVE_IMAGE_CLASSES_ONLY |
| row387 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row387.md) | row386, row374 | CT_FIRST_ARGUMENT_NOT_EVALUATED |
| row388 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row388.md) | row381, row387 | FINITE_RELATIONS_NOT_ALL_CL2 |
| row389 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row389.md) | row388 | FINITE_RELATIONS_NOT_ALL_CL2 |
| row390 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row390.md) | row389 | FINITE_RELATIONS_NOT_ALL_CL2 |
| row391 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row391.md) | row390 | FINITE_RELATIONS_NOT_ALL_CL2 |
| row392 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row392.md) | row391 | FINITE_RELATIONS_AND_DIFFERENT_NOT_ALL_CL2 |
| row393 | [収載原著](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/stage35ex-r3r2-math-sources-pass2/stages/stage35-ex/materials/classgroup-and-different/proofs/row393.md) | row392, row381, EXTERNAL_DE_LA_MAZA_THEOREM1 | FINITE_RELATIONS181_NOT_CL2_BOUND_AND_SOURCE_THEOREM_PENDING |

## 自己完結を阻む未判定ゲート

1. **row370の元source適用**：S263/S264の厳密なsigned±30 Ward平方の適用条件と、後続row371～375の前提が同一基底・同一指標・同一曲線かを命題単位で確定する。
2. **row378→381のHecke仮定**：row381の−30排除は二次Hecke GRH条件付き。数学原著がGitHubにあることだけで無条件の排除へ昇格しない。
3. **row385→393の類群**：6768小因子基底の全Cl/2生成、c_Cl、q★、真Sel4を証明した原著は存在しない（未証明研究ゲート）。**181は形式的残余**。
4. **外部de la Mazaの適用**：row393で使用したTheorem1と系に対する有理試験関数のadmissibilityと符号規約を原典と直接照合。既存のGitHub原著は著者の定理適用説明であり、原典監査PASSではない。
5. **row377の監査原稿**：第１周でDrive原監査が空/BOMと記録された。数学的原著本文はGitHubにあるため、これを「原数学証明の未収載１件」と誤算しない。監査証拠の未確認欄を保持。
6. **計算資料の範囲**：資料群2の172 ZIP memberと資料群3の529 memberは#1854に保存済み。今回の原著位置確認では再演していない。数学的十分性を判断する前提証書は別層の監査ゲートとして残す。

**結論は『row370〜393の数学本文24本は収載済み』まで。** 数学的祖先DAGの必要十分・外部定理適用・無条件−30排除・全LOWは依然 OPEN。第２周の調査自体は継続。
