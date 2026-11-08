# Stage35EX — row393停止時点の全ルート公開索引

**研究はrow393で一時停止。現在の作業は公開整理です。**

99管理IDすべてに、目的・到達点・障壁・保存された再開条件・元資料リンクを持つページを用意しました。R1 9、R2 8、R3 10、R4 52、R5 20。歴史的統合先や横断系列を含むため、99本の独立数学ルート・99定理ではありません。

- [全99件を読む](CATALOGUE.md)
- [CSVで一覧を見る](catalogue.csv) · [構造化JSON](catalogue.json)
- [材料の掲載範囲と次の移植単位](MATERIALS.md)
- [監査・採用の範囲](AUDIT-SCOPE.md)
- [R3研究記録330–393](research-records/R3-330-393.md)

## 最初に守る区別

この索引は管理原文の出典付き転記です。新しい数学研究、独立再監査、定理の昇格、Stage閉鎖を行っていません。`../MAIN-STATE.json` の正式な採用状態は変更しません。元の採用済み結果を取り消すものでもありません。

原文にあるACTIVE・研究中・NEXTは入力側の記録です。新しい研究・row394以降への継続は、明示的なユーザー再開指示まで実行しません。

row393の独立監査は `PASS_SCOPED_DEPENDENT_20261108_SOURCE_THEOREM_VERIFICATION_PENDING`。有限算術等への限定PASSと、外部定理の原典適用照合待ちを分けます。B<2^94を完全独立監査済みと書かず、181を真の類群階数・上界と扱いません。元−30とBranch Bは未解決です。

## 元資料との対応

`sources/R1.json`〜`R5.json`は今回読んだ管理索引を保持します。各カードから元の台帳行と原文へ辿れます。数百KBの索引データをチャットに丸ごと開く必要はありません。下の検証器で件数・ハッシュ・特定IDを確認できます。

研究の主要な議論にはGitHub上の所在を作り、全原本・原ログはDriveから回収できる形を維持します。このPRで全証明・全計算証書本体を移したとは主張しません。

## ローカル検証

リポジトリrootで：

```sh
python stages/stage35-ex/publication/verify_catalogue.py --summary
python stages/stage35-ex/publication/verify_catalogue.py --id R3-07
```

標準Pythonのみを使います。この索引検証器は数学計算を行わず、掲載対象・転記の完全性・全99ID・統合先・出典対応・相対リンク・ハッシュ・旧正式状態の保持を検査します。既存数学検証器の実行条件を変更しません。新しいGitHub Actions workflowは追加していません。
