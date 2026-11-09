# 固定±18の親Selmer証書 — 第4移植群

2026-11-09 JST。既存のrow361–364とその入れ子の数学資料を保存する。研究はrow393で停止中。[PR #1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)だけを更新し、新しいPRは作らない。

**対象は固定signed±18のC₂/J₂、36次数体である。−30側の105次数体へ類数1を移送しない。** row364の真正Selmer次元9をMW階数9と同一視せず、MW階数7..9、Cassels–Tate成分と全MWの163進上側Uの未確定を保持する。この親証書群による新規source排除は0。後続row367の既存±18排除は[第1群](../original-source-exclusions/README.md)に別途保存済み。

## 主資料と限定

| 記録 | 保存内容 | 本文・監査 |
|---|---|---|
| 361 | 既知7有理類の実際の163進対数119座標・単元minor137、既知7類だけを消す部分微分 | [本文](proofs/row361.md)。台帳のユーザー全再演PASS表示を原文保持。独立した監査報告ファイルは所在未確認。 |
| 362 | 既知7類の全球163冪飽和という従属系 | row361と同じ原稿。独立監査PENDINGの原表示を保持。 |
| 363 | 同じ36次数体の無条件類数1・19単数平方類完全被覆・残余2方向 | [本文](proofs/row363.md) / [監査](audits/row363.md) |
| 364 | 全場所のfake像8次元、真正Selmer9次元ちょうど。既知7類を法とする商2次元 | [本文](../original-source-exclusions/parents/row364/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105.md) / [監査](audits/row364.md) |

原台帳の12記録（345/352/355–364の該当行）、要約・監査・方法・障壁・当時のNEXTは[R3-SOURCE-RECORDS.json](R3-SOURCE-RECORDS.json)。当時のNEXTは現在の研究再開指示ではない。[CLAIMS.json](CLAIMS.json)で掲載範囲を固定する。

row361の旧原稿・原AUDIT_SCOPEにあるPENDINGと、後続台帳のユーザー全再演PASSは出典を分けて保存する。所在未確認の監査本文を読んだ扱いにしない。row362の従属系はrow363/364の監査によって自動的に独立監査済みにならない。既存監査コードの再演も新たな独立監査PASSではない。

## 保存と省略

現在Driveから取得した3原証拠ZIPと、その9入れ子、計12パッケージを照合した。全438メンバーを[SOURCE-INVENTORY.json](SOURCE-INVENTORY.json)へ記録し、数学コード・証明・入力・有限探索の記録を274対応保存する。別途取得した本文・監査・監査コードは6対応。同一内容は第1〜3群とも共有する。

8パッケージには原manifestがあり、その全393記載を選択前に検証した。原manifestを持たない4入れ子は、親ZIP内のSHA256に結び付けてCRC・内容を照合した。操作用のrecord_updatesはDriveに残し、意味のある親証明・親監査の控えは保存する。入れ子ZIPコンテナは原則として内容への対応を保持する。元検証器がZIP自体のSHA256を読む2件だけは、その元ZIPバイトも一度ずつ保存する。省略は一件ずつ理由付きであり、原ZIPそのものの完全復元は主張しない。

C118以前の証書や全物理母集団からindexed sourceへの上流写像を含む**全親鎖の自己完結は引き続き未完了**。全99管理IDの証明本文移植も完了していない。無条件−30、全LOW、Branch BはOPEN、row393の定理原典照合待ちも維持する。

## 復元と既存証書の再演

```bash
python verify_migration.py
python -O verify_migration.py
python restore_package.py --package row364 --destination /tmp/stage35ex-row364-math
```

復元は選択保存した数学・出典ファイルの元パスへの復元である。操作記録を省略しているため、元の全ZIP用verify_manifestを選択コピーへ実行しない。上記の移植検証器が保存した全バイトと明示省略を検査する。

Python 3.12、python-flint 0.9.0、SymPy 1.14.0、cypari2 2.2.4（PARI）で[20再演ジョブ](REPLAY-JOBS.json)を実行できる。独立した一時コピーへ復元し、公開原資料を上書きしない。完了済みジョブは同じ凍結資料に対して再利用できる。

```bash
python -m pip install -r requirements.txt
python replay.py --output /tmp/stage35ex-materials04-replay.json
python replay.py --resume --output /tmp/stage35ex-materials04-replay.json
```

通常実行が基本で、row364の明示的例外チェックだけの元検証器は指定ジョブに限り-Oも再演する。assertを使う古い親検証器を-Oで成功扱いにしない。原JSONとの比較では実行時間だけを除外する。探索・新しい候補生成・PARI別実装の全再監査はこの20ジョブに含まない。実際の検査範囲・出力は[LOCAL-REPLAY.json](LOCAL-REPLAY.json)へ記録する。

[全99管理ID](../../publication/CATALOGUE.md) · [資料全体](../README.md) · [移植進捗](../MIGRATION-STATUS.json)
