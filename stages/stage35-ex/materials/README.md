# Stage35EX — 証明・計算資料の移植

最初に[主要ルート本文・証明・条件・監査・障壁](../publication/major-routes/README.md)を読む。以下の5群は既収載の詳細根拠として共有する。

**現行の移植範囲（2026-11-09・ユーザー指定）：主要ルートのみ。** 主要な成果・証明本文・成立条件・監査状態・重要な障壁を中心にまとめる。原資料と詳細な証拠はDriveの参照先を残す。全99IDの本文、全親証書、全原ログの網羅移植を完了条件にしない。深い親証書・途中版・重複データを順次取り込む旧方針は失効する。新しいPRを作らず、PR #1854を使う。

研究はrow393で停止中。公開作業は[PR #1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)だけで継続し、新しいPRは作らない。既存の証明・証書・監査記録を原資料と対応させて保存する。

- [第1群：±18・指定指数群・+30の元source排除](original-source-exclusions/README.md)
- [第2群：−30のMW/Selmer・Artin/Hecke資料](negative30-mw-selmer/README.md)
- [第3群：類群・非分岐部分・不同・有限上界](classgroup-and-different/README.md)
- [第4群：固定±18の親Selmer証書](selmer18-parent-chain/README.md)
- [第5群：C117–C119 HCSとR1/R4の関連資料](hcs-crosslane-c117-119/README.md)
- [全99管理IDの索引](../publication/CATALOGUE.md)
- [移植進捗と次の資料群](MIGRATION-STATUS.json)

第1群は4件の排除証明と直近の親入力、C35-08/11/12の全算術パッケージを含む。第2群は14記録とその証拠ZIP全172メンバー、13件の読める原監査本文を保存した。row377の監査リンク先空文書は明記している。全99件の証明本文が移植済みという意味ではない。−30・全LOW・Branch BはOPEN。既存の正式採用状態は変更しない。

第3群はrow385–393の9記録・9監査と全529証拠メンバーを重複せず保存する。row393の定理原典照合待ちと、形式181と真の類群の区別を保持する。

第4群は固定±18の既知7対数・36次数体の類数1・真正Selmer9と入れ子の数学的前提を補完する。−30側の105次数体へ類数1を移さず、row362の独立監査待ちとrow361の監査本文所在未確認を保持する。

第5群はC118のHCS親資料と同時期のR1/R4の関連議論を24 native文書・6再演コードで補完する。過去の暫定研究の採用範囲と、正式採択・外部監査の区別を保持する。

## 主要原証明の追補（2026-11-09）

[20件の追加した主要原著本文と未完了チェック](../publication/major-routes/MIGRATION-COMPLETION-CHECKLIST.md)および[出典対応map](../publication/major-routes/PRIMARY-SOURCE-MAP.json)。C195の11前提、S270、P112関連3本、C196〜C200を含む。数学的な意味での独立再監査・移植完了・mainマージを意味しない。
