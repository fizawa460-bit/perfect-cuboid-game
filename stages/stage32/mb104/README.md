# Stage32 / MB104 — 研究資料・独立監査・検算証拠（同期保管）

**これは研究資料の移送先であり、Stage32のactive controllerではありません。** 現在の正式な controller は [`../final-chain/32-03-multibranch/STATE.json`](../final-chain/32-03-multibranch/STATE.json) です。そこに記載された `FROZEN_AUDIT_REPAIR_READY_NO_CREDIT` と `retained_frontier` 27件、およびcredit firewallを変更・解除しません。

この資料は2026-11-01時点のGoogle Drive正本から採取したエビデンスと履歴です。完全直方体の存在・非存在、母集団全体の有限窓、実候補の排除、公式creditを証明または昇格するものではありません。

## 読み方

- `research/MB104-F35.md` 〜 `MB104-F82.md` — 横断研究F35〜F82（新規第6ルートではなくA〜Eに帰属）。
- `audits/` — 独立監査資料。PASSは原文記載の条件範囲に限定し、HOLD/FAILを尊重。
- `status/` — Drive上の現行統合スナップショット。GitHubのcontroller/STATEの代替ではない。
- `history/` — F01〜F34の履歴。初期F01〜F05の原文の一対一同定は未完。
- `route-e/` — E関連の補助研究資料。
- `evidence/F61-legacy/`, `evidence/F62-legacy/` — **旧版、検証器に`assert`があり `python -O` で検査が消える。未修復・未昇格。**
- `evidence/F63/` 〜 `evidence/F67/` — ZIPから展開した証明書・検証器・計算データ。旧ZIPを相対パス参照するコードは**このままでは再実行できない**。修正・独立再検証が必要。
- `AUDIT_SCOPE.md` — 元監査の成立条件・HOLD一覧。
- `SHA256SUMS.txt` — ここに保存したファイルのSHA-256（このファイル自身は除く）。

## 重要な重複・失効規則

F45=F46は同じnorm平方ゲートの異なる記述。F51/F52の無循環な旧推論はF53で訂正。F55のPicard64部分は再導出。F81の旧全p′=2上界はFAIL、F82の追補Dは同一Y・標識二次指標保存の追加条件付きです。**未監査研究を新たな独立数学成果としてクレジットしないこと。**

## 機械的検査

`stages/stage32/mb104/` 内で `sha256sum -c SHA256SUMS.txt` を実行してください。これはソースバイトの整合性の検査であり、数学的妥当性・再現実行PASSではありません。

元のZIPはGoogle Driveにのみ保管。**GitHubにはZIPを1本も登録していません。**
