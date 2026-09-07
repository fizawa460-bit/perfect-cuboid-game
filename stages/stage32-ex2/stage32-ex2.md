# stage32-ex2 — V6 member reconstruction / fixed components

## 目的

Picard class V6 を「数値クラス」のまま扱わず、実際の section・curve member・固定成分分解、またはその不在を作る。これにより EX1/EX3 の仮想的な曲線を実在する対象へ接続できるかを調べる。

## ゴール

次のいずれかを得る。

1. V6 の明示的な member（方程式、section、ideal、または検証可能な構成）。
2. fixed/moving decomposition と各成分の交叉数・既約性に関する補題。
3. 現有の source-bound data からは member を作れないことの、入力不足としての正確な診断。

\(h^0\ge294\) は section が多数「存在する」下界であり、個々の明示 section の提示ではない。

## 簡易ロードマップ

1. \(L=\mathcal O(D)\) を固定し、既知140・対称性・torsor/Galois から実際に得られる section 源を棚卸しする。
2. 交叉数から固定成分候補を列挙し、負の交叉を持つ候補だけを exact に検査する。
3. 群作用で小さい不変/固有部分空間を取り出し、section 候補を有限化する。
4. theta/modular 座標または ideal/syzygy 表現が source-bound に得られる場合だけ、member を構成して Picard class・既約性・種数を検証する。
5. 成功時は EX1 と EX3 に渡す actual-carrier adapter を明記する。

## 最初の停止条件

数値的有効性を実効的 member の存在に読み替えない。外部座標系・線束の同一視が未証明なら、計算は「候補生成」までに留める。
## 共通の扱い

- **探索用・非権威**です。MAIN authority、Q602/O210、survivors `[73,97,235]`、既存の完了/未完了判定を変更しません。
- credit 階層は番号ではなく、`NECESSARY_CONDITION_ONLY`（必要条件のみ）、`BRANCH_EXCLUSION`（明記した一枝の実排除）、`FULL_TARGET_CLOSURE`（既存adapterを通した対象全体の閉鎖）で記録します。`NECESSARY_CONDITION_ONLY` を `FULL_TARGET_CLOSURE` と記録しません。
- 結果は「仮定」「対象」「量化域」「使った外部入力」「未接続のadapter」を明記します。実在する曲線・正規化・marked dataを仮定した議論は、その仮定を外しません。
- 自動化は、先に有限の入出力契約と再現コマンドを決めます。大規模探索、生成物、freshness CIは、探索葉が成功してからの統合時だけにします。
