# stage32-ex3 — O210 modular cover / monodromy

## 目的

q'=4 の V6 bidegree \((105,81)\)、第一射影の étale 性、第二射影側の ramification 総量 \(192\)、O=210 を、正規化上の cover・branch-cycle・monodromy として整理する。数値帳簿では見えない cover 構造から新しい必要条件を探す。

## ゴール

1. O210 を排除する、または許される monodromy/fibre 型を真に狭める補題。
2. \(Q(T)=602\)・residue への**明示的な**下流述語（対象と adapter 付き）。
3. actual carrier がないため条件論に止まる場合、その条件と不足データの確定。

## 簡易ロードマップ

1. どの map がどの normalization に作用するかを source-lock し、曲線の存在を暗黙に仮定しない。
2. degree \(105,81\)、étale/ramification 条件を Riemann–Hurwitz と fibre 分割へ正確に翻訳する。
3. V4 torsor と両射影の monodromy を区別し、branch-cycle の可能型を有限化する。
4. 既知の involution/character と整合する型だけを残し、O=210 と照合する。
5. 剰余型が残るなら Q602 の3残存値への adapter を書く。書けない場合は Q/O を更新しない。

## 最初の停止条件

「第一射影 étale」から全体の unramified/bijective 正規化を導かない。仮想 cover の分類を、V6 全体や Q602 の排除と呼ばない。
## 共通の扱い

- **探索用・非権威**です。MAIN authority、Q602/O210、survivors `[73,97,235]`、既存の完了/未完了判定を変更しません。
- ここで得たのが「必要条件」だけなら成果は①です。V6の一枝を実際に排除できて②、既存adapterを通して対象全体を閉じて初めて③です。①を③と記録しません。
- 結果は「仮定」「対象」「量化域」「使った外部入力」「未接続のadapter」を明記します。実在する曲線・正規化・marked dataを仮定した議論は、その仮定を外しません。
- 自動化は、先に有限の入出力契約と再現コマンドを決めます。大規模探索、生成物、freshness CIは、探索葉が成功してからの統合時だけにします。
