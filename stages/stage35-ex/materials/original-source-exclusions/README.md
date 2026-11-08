# 元source排除の証明・証拠 — 第1移植群

2026-11-08。研究は **row393で停止中**。このディレクトリは既存成果を保存・再現可能にするための移植であり、新しい数学研究・監査・正式採択ではない。

| 元記録 | 保存した結論 | 独立監査の範囲 | 証明 |
|---|---|---|---|
| row367 | 固定 ±18 の元source排除 | 固定C2と既監査の親に依存するPASS | [本文](row367/REPORT.md) / [監査](audits/row367.md) |
| row368 | 列挙21絶対指数・両符号42枠の元source排除 | C118等を継承する限定PASS | [本文](row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md) / [監査](audits/row368.md) |
| row369 | 48,78,90,120,132 の両符号10枠の元source排除 | C35-11/12等を継承するPASS_SCOPED_DEPENDENT | [本文](row369/STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER_20261106.md) / [監査](audits/row369.txt) |
| row376 | **+30のみ**の元source排除 | row370/373/374とrow375の単元符号全射を継承するPASS_SCOPED_DEPENDENT | [本文](row376/PROOF.md) / [監査](audits/row376.md) |

row368の対象は Ward5: 24,36,54,56,64,66,84,94,96,104,114,124,126,144 と、Ward3: 32,80,88,92,122,128,152。いずれも同じ原始標識付き基底からの必要条件を使う。指数枠の数を実際の解の個数と解釈しない。

**−30、全LOW、Branch BはOPEN。** MW階数7、CT値c、全MWの163進上側空間Uは、この移植でも証明済みにしない。全物理母集団からindexed sourceへの上流の写像と被覆も別の未閉鎖事項。詳細は [CLAIMS.json](CLAIMS.json)。

## 保存内容と依存関係

- row367の数学本文・全局所検証入力・生成器・検証器、直近の親row365の数学本文と全math入力、row366の本文と監査を保存した。row364の本文と局所所属証書も保存した。
- row368/369/376の証拠ZIPを全ファイル展開して保存した。row376の数学本文は元ZIPの外にあるため、別途Drive原稿と照合して追加した。
- 4件それぞれの後日の独立監査を別ファイルとして保存した。元原稿・元READMEにある「監査PENDING」やNEXTは執筆当時の履歴であり、現在の研究再開指示ではない。
- 共通の[S263](parents/S263.md)、[S264](parents/S264.txt)、[C118](parents/C35-118/export.txt)、[C35-12](parents/C35-12/PROOF.md)、[row339](parents/row339-PROOF.md)、row376が継承する[row370](parents/row370-PROOF.md)・[373](parents/row373-PROOF.md)・[374](parents/row374-PROOF.md)・[375](parents/row375-PROOF.md)の本文を保存した。Google Docsはtext/plain書き出しを明記し、保存済みMarkdownは元バイトを維持した。
- C35-12への旧リンクにはIDの大文字・小文字の誤りがあった。R3の旧正本rows18–20で正しいIDを確認した。[SOURCE-ERRATA.json](SOURCE-ERRATA.json)に訂正先を記録し、元原稿は改変していない。
- 前回不足していた **C35-08/11/12** を追加した。[C35-11本文](parents/C35-11/PROOF.md)、[C35-12本文](parents/C35-12/PROOF.md)、[算術パッケージ](parents/C35-11-12/)、[当時の読戻し記録](parents/C35-11-12/READBACK-RECEIPT.md) を保持する。積分、厳密Cantor、局所Selmer、PARI大域認証、signed6写像の元コード・入力・出力を含む。C35-08の6ファイルはC35-11/12内の同一バイトと照合し、一組だけ保存した。
- **親証明鎖全体の自己完結移植は未完了。** C118が参照する以前の証書、row364以前のSelmer完全性証書、row370/373/374/375の全算術パッケージ等は、親原典への依存として残る。今回の再演算はそれらをゼロから認証するものではない。

原ZIPと各ファイルのSHA-256、選択した移植先、Driveに残したファイルは [SOURCE-INVENTORY.json](provenance/SOURCE-INVENTORY.json) に一対一で記録した。省いたものは主に管理正本の更新ログと重複した親ZIPで、元ZIPはDriveに残る。原ZIP全体のチェックサム検査は展開前に実施した。`provenance/*SHA256SUMS.original*` は元の全ZIP用であり、選択移植した部分だけに `sha256sum -c` を実行しない。移植後は下記検証器を使う。

## ローカル検証

Python 3.12で、まず標準ライブラリだけの保存整合性検証を実行する。

```bash
python verify_migration.py
python -O verify_migration.py
```

算術を再演算する場合は [requirements.txt](requirements.txt) の環境を用意し、このディレクトリから実行する。

```bash
python -m pip install -r requirements.txt
python replay.py --output /tmp/stage35ex-source-exclusions-replay.json
```

`replay.py` は一時コピー上で元の検証器を実行する。row365/367は通常と `-O`、row368/369/376は通常実行の計7回。後者3本は `assert` を使うため `-O` の実行を証拠にしない。row368/369の生成JSONは元ファイルとバイト比較、row376の標準出力は凍結JSONと内容比較し、保存した証書を上書きしない。

追加した親算術も、一時コピー上で再実行できる。SymPy 1.14.0とPARI/GP、または `requirements-parents.txt` のcypari2環境を使う。

```bash
python replay_parent_certificates.py --output /tmp/stage35ex-parent-replay.json
```

親のPython検証5本とPARI認証1本を実行する。Python5本の標準出力は元ログとバイト比較する。PARI/GP実行ファイルがない場合はcypari2で元GP文末の `quit;` だけを除いて評価し、実際の版と認証値を記録する。PARIの版により基本単元の表示は変わるため、旧ログとの同一性は主張しない。元のpickle入力はFractionのみの制限読込みで先に点検し、原ファイルは改変しない。親の算術再現も、一般理論や原始source被覆の新独立監査ではない。

実施済みの環境・コマンド・終了値・出力digestは [LOCAL-REPLAY.json](LOCAL-REPLAY.json) を参照。有限算術の再現PASSは、一般理論・全親証明・独立数学監査の新たな認証を意味しない。GitHub Actionsの実行は不要。

99管理IDの索引は [PR #1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)。これはその資料本体移植の第1群であり、99件すべての証明・証拠の移植完了ではない。
