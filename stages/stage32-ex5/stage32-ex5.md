# stage32-ex5 — receiver breadth remap

## 目的

V6/O210/Q602 への過度な固定を外し、Stage29→Stage32 の全 receiver を改めて対応付ける。目標は「別の武器の名前」ではなく、現在の数値・field・quantifier に本当に接続できる独立ルートを一つ選ぶこと。

## ゴール

1. 全 Stage32 receiver の有限 ledger と、各々の現 status（適用可/入力不足/不適用）。
2. V6/O210 を経由しない、またはそれを補強する一本の priority route。
3. その route の最小証明責務・入力・成功時の adapter を書いた実行仕様。

## 簡易ロードマップ

1. Stage29 の最終量化域（unibranch g0/g1、有効性、multibranch ledger）を再固定する。
2. 既存 arsenal を見ずに候補を出す：effective cone/fixed components、equigeneric Hilbert/Severi、modular uniformization、Galois descent、有限 exact enumeration の改善など。
3. 各候補を object・field・mask・quantifier・reverse adapter の5項目で採点する。
4. 既存 arsenal と照合し、重複は落とし、最も短い「新しい入力→receiver 排除」鎖を一つ選ぶ。
5. その鎖だけを EX1–EX4 または新規 microdiagnostic へ接続する。

## 最初の停止条件

広い文献探索や一般定理の名前だけで「適用可能」としない。V6 一枝だけの結論を Stage32 全体の前進として数えない。
## 共通の扱い

- **探索用・非権威**です。MAIN authority、Q602/O210、survivors `[73,97,235]`、既存の完了/未完了判定を変更しません。
- credit 階層は番号ではなく、`NECESSARY_CONDITION_ONLY`（必要条件のみ）、`BRANCH_EXCLUSION`（明記した一枝の実排除）、`FULL_TARGET_CLOSURE`（既存adapterを通した対象全体の閉鎖）で記録します。`NECESSARY_CONDITION_ONLY` を `FULL_TARGET_CLOSURE` と記録しません。
- 結果は「仮定」「対象」「量化域」「使った外部入力」「未接続のadapter」を明記します。実在する曲線・正規化・marked dataを仮定した議論は、その仮定を外しません。
- 自動化は、先に有限の入出力契約と再現コマンドを決めます。大規模探索、生成物、freshness CIは、探索葉が成功してからの統合時だけにします。
