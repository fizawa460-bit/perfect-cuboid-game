# Stage35-EX 現在の状態（2026-11-21 時点）

この文書は、Stage35-EX の現在の状態を1枚で示すための状態サマリである。正式な採用状態は `MAIN-STATE.json` が保持し、この文書はそれを変更しない。2026-11-08〜09 の公開整理で書かれた入口・要約文書群は当時の状態記述のままであり、現在の状態はこの文書を参照すること。

## 全体状態

- **凍結中。** 所有者が 2026-11-12 に Stage35-EX を凍結した（`STAGE35EX-FROZEN-20261112.md`、判定は `review-20261112/CONTINUATION-JUDGEMENT.md`、監査は `review-20261112/AUDIT-CLAUDE-20261112.md`）。
- **正式権威は V74 / Goal4AK のまま不変。** `MAIN-STATE.json` の schema は `STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_...`、status は `ACTIVE_RESEARCH_AUDITED_INTERMEDIATE_NO_E1_CREDIT`。E1・Stage35・完全直方体への credit はない。
- **凍結判定がカバーする範囲としない範囲。** 判定は、再開条件（非 indexed 点を indexed へ帰着する定理、または HIGH の一様相関上界）なしに LOW スロット作業と −30 関係探索を再開しないことを述べる（`review-20261112/CONTINUATION-JUDGEMENT.md`）。一方で判定は、下記の 2026-11-10 再開 wave 群（PR #1861）には触れていない。wave 群は判定より前に走った記録であり、判定に統合されていない側記録として残る。

## 経緯（状態に関わるものだけ）

| 日付 | 出来事 | 出典 |
|---|---|---|
| 2026-11-08 | 所有者指示：公開作業のみ。row393 スナップショット後は研究一時停止 | `MAIN-START-HERE.md` 冒頭の指示ブロック |
| 2026-11-09 | 公開整理の範囲を「主要ルートのみ」に確定（PR #1854） | `publication/README.md`、`materials/README.md` |
| 2026-11-10 | 所有者認可で同じ signed −30 / row393 ルートだけを再開し、6波の関係収穫を実施（PR #1861） | `research/r3-row393-resume-20261110/README.md`、`MAIN-BATCH-HANDOFF.md` 冒頭ブロック |
| 2026-11-12 | 所有者が Stage35-EX を凍結 | `STAGE35EX-FROZEN-20261112.md` |
| 2026-11-21 | minus30-lab の実験群（PR #1895・#1897・#1898）と本状態サマリ | `research/minus30-lab/README.md` |

## −30 の状態

対象は signed −30、C29（種数52）と次数105・署名 (7,49) の根体 K。還元は `dim_F2 Sel^(2)(J/Q) = 9 + c_Cl`、元 source は rank J(Q) ≥ 10 を要求する（`publication/major-routes/04-minus30.md`、`materials/negative30-mw-selmer/row384/PROOF.md`）。従って無条件の c_Cl = 0 または rank ≤ 9 の認証で元 source は排除できるが、どちらも未達である。

### 監査済みの到達点（row393、2026-11-08）

- ノルム ≤ 6768 の878小基底について、個別 Cl/2 零化 **628**、形式残余 **181**（`publication/major-routes/04-minus30.md` の row393 表、`materials/classgroup-and-different/audits/row393.txt`）。
- 数値行列 14186×43814、Q/F2 rank 13627、整数核 559（`materials/classgroup-and-different/CLAIMS.json`）。
- 留保：row393 定理の原典照合は PENDING（`materials/classgroup-and-different/CLAIMS.json` の `SOURCE_THEOREM_VERIFICATION_PENDING`、`publication/major-routes/ROW393-PRIMARY-THEOREM-GATE.md` は de la Maza 定理の適用について D-1 PASS を記録）。
- 181 は有限関係商の形式残余であり、真の類群の階数・上界ではない（`materials/classgroup-and-different/README.md`）。

### 未監査の現在記録（再開 wave 1–6、2026-11-10）

- 同じ有限表示の上で、形式残余 **181 → 175**、個別 Cl/2 零化 **628 → 636**、累計の新整元 4632 個・独立主関係 4619 本。残存先頭は P_(953,0)（`research/r3-row393-resume-20261110/README.md`、`MAIN-BATCH-HANDOFF.md` 冒頭ブロック）。
- wave 群自身の留保（各 wave の README が明記）：**著者再演のみで外部独立監査はない。正式な row394 採用はなく、"394" は作業用ラベルである。類群生成は未認証。残余は類群の次元でも上界でもない。無条件排除は 0。**
- 従って 175 / 636 は「現在の記録」ではあるが「監査済みの到達点」ではない。181 / 628 を引用するときは row393 到達点として引用すること。

### 主張フラグの現状

| 主張 | 状態 | 根拠 |
|---|---|---|
| c_Cl = 0（無条件） | **未証明**。row381 の結論は二次 Hecke GRH 条件付きのまま | `materials/negative30-mw-selmer/CLAIMS.json`: `c_Cl_zero_unconditionally_proved=false` |
| rank J(Q) ≤ 9 | **未証明（OPEN）** | 同上および `publication/major-routes/04-minus30.md` |
| ZF2（Ω₂ の無零性） | **未証明・未検査**。row384 が残した義務のうち唯一未着手のもの | `materials/negative30-mw-selmer/CLAIMS.json`: `ZF2_proved=false` |
| δ★ の Sel4 非リフト / q★ | **UNDETERMINED**。rows 385–387 で検査は執行済みで、判定は生成認証の欠落で止まっている | `materials/classgroup-and-different/CLAIMS.json`: `qstar_computed=false`、`true_Sel4_decided=false`；`materials/negative30-mw-selmer/CLAIMS.json`: `delta_star_Sel4_nonlift_proved=false` |
| LOW 残余 | 無条件残余は 9 絶対指数・16 signed 枠（row393 時点から不変） | `materials/negative30-mw-selmer/audits/row383.txt`・`row384.txt` |
| E1 | credit なし | `MAIN-STATE.json` status |

q★ の障害は名前が付いている：q★ を決める row387 の経路は Cl(O_K)/2Cl(O_K) の全尽基底（各類に I² = (α) の証人付き）を入力に要求するが、生成の認証にはノルム < 2⁹⁴ の全素イデアル処理が必要で、処理済みの878基底では生成自体が未証明である（`publication/major-routes/ROW393-PRIMARY-THEOREM-GATE.md`、`research/minus30-lab/exp15-qstar/NOTES.md`）。

## minus30-lab（2026-11-21 の実験群）

`research/minus30-lab/` は、凍結判定が残した未完義務に対して未試行の小さい実験を記録した研究ノートであり、STATE・ledger・credit は変更しない（PR #1895・#1897・#1898）。row383/384 の試験関数族は、重み・長さ・ε・シフト・深さの全軸でフロンティアを地図化し終えた。認証済みの帯改善は得られたが、ゴールに接続した物差し——最弱帯の不足分と文献の明示的無零領域の不足分の比、約 **3100倍**——は桁では動いていない（文献の到達点は Re ≥ 0.99986、必要は帯の端 0.63〜0.68）。詳細は `research/minus30-lab/README.md` と `research/minus30-lab/LEDGER.md`。

## 文書の読み方

- **現在の状態**：この文書、`MAIN-STATE.json`（正式権威）、`MAIN-START-HERE.md`（入口と所有者指示）、`materials/negative30-mw-selmer/CLAIMS.json`・`materials/classgroup-and-different/CLAIMS.json`（主張フラグ）。
- **歴史的記録**（当時の記録として読む。現状記述ではない）：`STAGE35EX-FROZEN-20261112.md`、`review-20261112/`、`MAIN-BATCH-HANDOFF.md`、`materials/` の rows 361–393 の本文・監査、`35ex-01/` 〜 `35ex-35/`、`runkeys/`、`snapshots/`、`research/r3-row393-resume-20261110/`（未監査の側記録）、`publication/` の PR1854・PR1860 作業文書群。
- **現状記述としては superseded**（2026-11-08〜09 の公開整理時点の記述。冒頭に状態注記あり）：`README.md`、`publication/README.md`、`publication/MATERIALS.md`、`publication/major-routes/README.md`、`publication/major-routes/04-minus30.md`、`publication/major-routes/06-cross-lane.md`、`materials/README.md` および `materials/` の各資料群 README。これらが述べる「row393で停止」は公開整理時点の枠組みであり、2026-11-10 の再開 wave と 2026-11-12 の凍結を含まない。特に `04-minus30.md` の row393 を終点とする数値（形式残余181・先頭 P_(827,0)）は監査済み到達点であって現在の記録ではない。
