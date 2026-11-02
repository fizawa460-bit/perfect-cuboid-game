# MB104 — Claude 用の起動メモ（2026-11-02 時点）

**この文書は案内だけです。** 正本ではありません。数学の結果・credit・監査判定・STATE の値はここで変更も昇格もしません。食い違ったら正本（下の「読む順番」の 2〜4）が優先です。

## 1. 読む順番

1. この文書（全体の地図と、既知の食い違い）。
2. `../STATE.json` — GitHub 側の MB の正本。`status`、`next_obligation`、`resume_obligation`、`retained_frontier`、`credit_firewall` を見る。
3. `drive-research/status/MB104-ROUTE-INDEX-V030.md` — Drive 側の研究台帳（索引 v0.30）。冒頭の CURRENT 行と「現在の運用ゲート」。
4. `drive-research/status/MB104-RESEARCH-OVERVIEW-V025.md` — 研究統合記録 v0.25。`A_EXISTING_ROUTE`〜`E_EXISTING_ROUTE` と `NEXT_A`〜`NEXT_E`。
5. `drive-research/AUDIT_SCOPE.md` — 各 F 文書の監査範囲・HOLD・重複規則。
6. 必要になった F 文書・監査文書だけ（`drive-research/research/`、`audits/`、`evidence/`）。

Drive 側の資料は 2026-11-01 時点の写しです。Drive の最新版はこれより進んでいる可能性があります。

## 2. いまの状態

### 2.1 GitHub 側（`../STATE.json`）

- `status`: `FROZEN_AUDIT_REPAIR_READY_NO_CREDIT`。`current_node`: MB104。完了・保持は MB101〜MB103。
- `next_obligation`: `MB104-20261026-AUDIT-REPAIR-REAUDIT`（現行 main での独立再監査）。
- `resume_obligation`: `MB104-000707-E2-UNIQUE-PAIR-M1-POSTULATION-OR-BULK`。e=2 の一意な対について、m=1 の 36 個の高エネルギー準位（Q=118..186 の偶数と Q=192）か、非線形の bulk を扱う。
- `retained_frontier`: 27 項目。すべて credit 0。B 系の5項目（b3 商・衝突会計・分岐半因子・η 指標線・反不変導手の source wall）もここにある。
- `credit_firewall`: すべて false（受け手・有効性・定理・端点・存在／非存在・merge）。

### 2.2 Drive 側（索引 v0.30／統合 v0.25）

- 運用ゲート: `ACTIVE_POST_AUDIT_RESEARCH_ZERO_CREDIT`。通常の MB104 研究は再開してよい。重い計算・成果の昇格・GitHub への書き込みは、別途ユーザーの許可が必要。
- ルートの状態:

| ルート | 状態 | 次にやること（要約） |
|---|---|---|
| A（対写像 r=1..4、864 支持、Stein 補正） | PARKED／数学は OPEN | κ 補題は PROVISIONAL。使うなら独立監査を通し、さらに r=1,2 を閉じる別の証明が要る |
| B（導手・符号・norm 平方） | PARKED／数学は OPEN | 実 source 上の反不変一次 jet・導手符号の貼り合わせに、種数1を感じ取る新しい制約が要る。「データ待ち」だけでは再開条件にならない |
| C（w の零点、種数1） | OPEN | C16 の w 零点の強制、または C17R の特殊配置への独立制約 |
| D（D1: F81 CM 族、D2: F82 二脚） | 条件付き PASS を保持 | D1 は可変 CM 族の一様な実効上限。D2 は一様な B_s か deg h1+deg h2 の上界 |
| E（CORELESS／NO NONEMPTY CLUMP） | OPEN／PARKED | 6 超平面の全付値、または補助 W の実分岐を強制する証明 |

- MB104 全体の有限窓は OPEN。実候補の排除は 0、credit は 0。

## 3. 既知の食い違い・古い記述（未修正）

台帳を編集しない方針なので、次の点は正本を直していません。直すかどうかはユーザーが決めます。

1. **STATE の監査状態が古い。** `audit_repair.status` は `PENDING_INDEPENDENT_HOSTILE_REAUDIT`、`research_resume_authorized` は false のまま。実際には、#1827 の exact head `adf4f05f` に対する独立監査が 2026-10-26 06:44 に PASS しており（review `PRR_kwDOTr52Y88AAAABUKn0LA`）、#1827 は 06:55 にマージされた。Drive 側はこの PASS を記録済みだが、GitHub の STATE は追従していない。
2. **STATE の PR 番号が古い。** `routing.active_pr_number` と `active_surface.pr_number` は 1827 のまま。#1827 はマージ済みで、開いている MB の PR はない。
3. **フォルダの移設。** #1846（2026-11-02 マージ）で `stages/stage32/final-chain/32-03-multibranch/` から `stages/stage32/32-03-multibranch/` へ移した。STATE 内のパスは書き換え済み。ただし証明書・旧監査記録・Drive 資料の中の旧パスは履歴としてそのまま残している。
4. **検証器は移設先では動かない可能性がある。** MB101〜MB104 の Python は移設前のバイトのまま（`parents[6]` などのルート深さ、固定 source-lock を前提にしている）。実行が必要になったら、その入口だけ直してから試す。
5. **ワークフロー。** `stage32-main-startup-authority.yml` は 2026-10-26 から形式エラーで動いていなかったため、2026-11-02 に GitHub の設定で無効化した（ファイルは残っている）。PR の自動検査で今も動くのは `stage32-claim-frontier-integrity.yml` だけ。

## 4. 重複・失効の規則（数え間違いを防ぐ）

- F45 と F46 は同じ norm 平方ゲート。成果は1件として数える。
- F51/F52 の循環推論は F53 で撤回。非循環の形は I = 1568m² + 2k（k ≥ 0）。
- F61/F62 の検証器は `assert` 依存（`python -O` で検査が消える）。旧版のまま、昇格しない。
- F63〜F67 の検証器は旧 ZIP への相対参照があり、このままでは再実行できない。
- F81 の旧「全 p′=2 で d ≤ 2^62+32」は FAIL。F82-D3 は D1 の系で、別の成果にしない。
- 固定モデル内の条件付き PASS（F61〜F68、C14/C18A など）を、実際の担体の排除へ自動的に広げない。

## 5. やってはいけないこと

- 台帳・索引・統合記録・監査正本・Drive 文書・STATE の数学的な値を、ユーザーの判断なしに編集すること。
- credit flag を変えること、成果を公式に認定すること、新しいルートや成果項目を作ること。
- push・merge・Drive へのアップロードを、ユーザーの OK なしに行うこと。
- 重い計算をユーザーの OK なしに始めること（計算は手元で行うのが原則）。

## 6. 手元の計算（32R）との関係

`C:\Users\fizaw\claudework\stage32_research\` の 32R ログ（次数 d ごとに、種数1以下の曲線がないかを調べる計算）は、MB104 の A〜E とは別の作業です。32R の結果を MB104 の成果として数えないこと。逆に、MB104 の結果を 32R の結果として数えないこと。

## 7. ファイルの地図

| 場所 | 中身 |
|---|---|
| `../STATE.json`、`../fib/STATE.json` | GitHub 側の正本（MB と MB-FIB） |
| `../LIVE.json`、`../MISSION.json`、`../PREFLIGHT.json` | 32-03 の起動用の参照 |
| `./`（この階層） | MB104 の検証器・証明書・数値資料・runkey・Genus7 資料 |
| `drive-research/research/` | F35〜F82 |
| `drive-research/history/` | F01〜F34 のまとめ |
| `drive-research/audits/` | 独立監査 A01〜A11 |
| `drive-research/evidence/` | F61〜F67 の証明書・検証器・データ |
| `drive-research/route-e/` | E の補助資料 E01〜E04 |
| `drive-research/status/` | 索引 v0.30 と統合記録 v0.25 |
| `drive-research/SHA256SUMS.txt` | バイト単位の整合性検査用（`sha256sum -c`。2026-11-02 に全件一致を確認） |
