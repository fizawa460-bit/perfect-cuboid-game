# Stage35EX — row393停止時点の主要ルートと全99ID索引

> [**PR #1854の最新：R3-07(row393)・R2-01の端から端までの粗い証明鎖**](major-routes/PR1854-ENDTOEND-CHAIN.md)。Google Driveから数学原著11本を追加し、古い数学親の所在を補った。**これは研究・原著本文の粗い接続図であり、厳密な再帰的論理閉包や数学的独立監査PASSではない。** 旧版の資料数・未対応数は履歴として保持。

> **新しい整理方針（2026-11-09）：** [**PR #1854 現行作業入口：R3-07(row393)／R2-01の2本だけの数学的証明鎖**](major-routes/PR1854-START-HERE.md)。以下の6章・99管理IDは参考索引であって、独立した移植対象ではない。現行数学結果へ至る不可欠な親のみGitHubで追い、計算証拠は後回し。以前の130本文を進捗率の分母に使わない。

**現行の移植範囲（2026-11-09・ユーザー指定）：主要ルートのみ。** 主要な成果・証明本文・成立条件・監査状態・重要な障壁を中心にまとめる。原資料と詳細な証拠はDriveの参照先を残す。全99IDの本文、全親証書、全原ログの網羅移植を完了条件にしない。深い親証書・途中版・重複データを順次取り込む旧方針は失効する。新しいPRを作らず、PR #1854を使う。

**研究はrow393で一時停止。現在の作業は公開整理です。** 公開作業は[PR #1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)一つにまとめ、続きを同じPRへ追加します。

99管理IDすべてに、目的・到達点・障壁・保存された再開条件・元資料リンクを持つページを用意しました。R1 9、R2 8、R3 10、R4 52、R5 20。歴史的統合先や横断系列を含むため、99本の独立数学ルート・99定理ではありません。

- [主要ルート本文・証明・成立条件・監査・障壁](major-routes/README.md)
- [C195以前の主要前提：原証明収載の未完了箇所](major-routes/C195-DEPENDENCIES.md)
- [全99件を読む](CATALOGUE.md)
- [CSVで一覧を見る](catalogue.csv) · [構造化JSON](catalogue.json)
- [資料の掲載範囲と未完了部分](MATERIALS.md)
- [第1資料群：元source排除の証明・検証コード](../materials/original-source-exclusions/README.md)
- [第2資料群：−30のMW/Selmer・Artin/Hecke資料](../materials/negative30-mw-selmer/README.md)
- [第3資料群：類群・非分岐部分・不同・有限上界](../materials/classgroup-and-different/README.md)
- [第4資料群：固定±18の親Selmer証書](../materials/selmer18-parent-chain/README.md)
- [第5資料群：C117–C119 HCS・R1/R4の関連資料](../materials/hcs-crosslane-c117-119/README.md)
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
