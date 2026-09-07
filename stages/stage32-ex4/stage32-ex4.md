# stage32-ex4 — absolute marking source / adapter

## 目的

inner-conjugacy invariant だけでは選べない absolute W-line を、実際に marked された外部データ（ppav/torsor/J[2] など）から固定する道を調べる。これは Q602 の3残存値へ算術的に届く可能性がある唯一の明確な橋の一つ。

## ゴール

1. source-bound な absolute W-line と、その座標/作用/検証手順。
2. その line から Q602 の \(73,97,235\) へ届く完全な adapter。
3. 既存文献・既存成果が提供するのは抽象共役類までで、絶対 marking を供給しないという範囲限定の診断。

## 簡易ロードマップ

1. 必要な marked datum を一文で仕様化する（base point、torsor trivialization、J[2] basis、Galois action 等）。
2. FSM/theta/Stoll/KRR 等の候補 source を、実在の marking があるかだけで棚卸しする。
3. 得られた datum から matrix/action を source-bound に抽出し、W-line 選択を独立 verifier で再計算する。
4. その選択が residue 計算へどう流れるかを一本の adapter として固定する。
5. selection 不可なら「不足している外部 datum」を名前付きで返す。

## 最初の停止条件

trace・order・conjugacy class の追加計算で absolute line が選べると期待しない。source が circular に KRR 的な選択を仮定しているなら、それを selection の根拠にしない。
## 共通の扱い

- **探索用・非権威**です。MAIN authority、Q602/O210、survivors `[73,97,235]`、既存の完了/未完了判定を変更しません。
- credit 階層は番号ではなく、`NECESSARY_CONDITION_ONLY`（必要条件のみ）、`BRANCH_EXCLUSION`（明記した一枝の実排除）、`FULL_TARGET_CLOSURE`（既存adapterを通した対象全体の閉鎖）で記録します。`NECESSARY_CONDITION_ONLY` を `FULL_TARGET_CLOSURE` と記録しません。
- 結果は「仮定」「対象」「量化域」「使った外部入力」「未接続のadapter」を明記します。実在する曲線・正規化・marked dataを仮定した議論は、その仮定を外しません。
- 自動化は、先に有限の入出力契約と再現コマンドを決めます。大規模探索、生成物、freshness CIは、探索葉が成功してからの統合時だけにします。
