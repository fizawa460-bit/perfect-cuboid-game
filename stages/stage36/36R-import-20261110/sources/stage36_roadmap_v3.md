# Stage36 ROADMAP v3（2026-10-16、36R-00〜36R-06 反映）

v2（`01_ROADMAP_v2.md`、2026-10-14）は残す。追補 `06_ADDENDUM_receiver_and_completion.md` が v2 より優先されることは変わらず、v3 もその追補に従う。
v3 は各葉の現状と、その後に分かった事実・暫定の分類を反映したもの。

## 0. ゴール（変更なし）

- 受け皿：Stage29-16 の `K16-C3-CAMPEDELLI-UNIFORM-TORSOR`、Stage29-02hb の `R29-CAMP2`。変更しない。
- Stage36 の役割：監査済み Campedelli 商に対する一様な H-torsor 算術的降下、または同じ排除帰結を与える代替定理の確立。
- 最終分類は旧 ROADMAP §36-10 の 4 語のみ：
  `R29_CAMP2_CLOSED_BY_QUOTIENT_EMPTINESS` / `R29_CAMP2_CLOSED_BY_RECEIVER_MATCHED_REPLACEMENT` /
  `CLASS3_RETAINED_WITH_SHARPER_CAMPEDELLI_THEOREM` / `SPLIT_TRIGGERED_DISTINCT_OBSTRUCTIONS`。新しい終了条件は作らない。
- **補足**：受け皿の閉鎖は完全直方体の非存在と同等以上（端点の点は全ての C_H に写る。36R-04 で (T′) ⇔ U(Q)=∅）。
- 研究管理上の完了 ≠ receiver の数学的閉鎖。

## 1. 現在の到達点

| 葉 | 状態 | ログ |
|---|---|---|
| 36-R1 | 完了。(T) ⇔ J(Q)=∅、(T′) ⇔ U(Q)=∅、J と C_H の関係 | 36R-00, 36R-04 |
| 36-R2 | 部分的。形の定理（全 p、無条件）は証明済み。符号条件・2 進の細部は有限の補完作業 | 36R-01 |
| 36-R3 | 定理の候補。自明類 ⇔ W_λ、商 X_λ・Y_λ・E′_λ | 36R-02 |
| 36-R4e | 完了。a<70 の 1469 個中 99.7% で端点 Selmer 集合は {自明類, 境界類}。反例 53/8 により一様な定理としては偽 | 36R-05 |
| 36-R5 | 固定 λ のみ。W の完全性を厳密計算で確認、Y_λ で 9 類を決着、38/23 は未決 | 36R-03 |
| 36-R6 | 未着手（低優先） | — |
| 36-R7 | 並行。査読の残りあり | — |
| 36-09 保留監査 | 完了（暫定）。LIVE 0、UNTESTED 2 | 36R-06 |

## 2. 確定した事実（v2 以降に新しく得たもの。いずれも外部査読前）

1. **J と C_H**：J = S/⟨e_B1+e_B2⟩ は、どの監査済み C_H の商でも被覆でもない。基底で Im_U = Im_J ∩ Im_H（全 10 核）。（36R-04 命題 2・3）
2. **端点の条件**：J の点が端点になる条件は δ1δ2 = 平方 の 1 本（s+1 ≡ G1G2）。(T′)「全ての p で E_p(Q) ⊂ {t∈{0,±1,∞}}」⇔ U(Q)=∅。（36R-04 命題 4）
3. **fibration は C_H に降りない**：C3_p を切り出す r は C_H の関数ではない。（36R-04 命題 5）
4. **C_H(Q) は無限**：a3=0 のピタゴラス点が全ての C_H に滑らかな有理点を与える。商全体の空性 C_H(Q)=∅ は偽。（36R-06 命題 A）
5. **Brauer–Manin の限界**：U_H(A_Q) ∩ C_H(A_Q)^{Br} ≠ ∅。Brauer–Manin で U_H(Q)=∅ は示せない（エタール Brauer は概略のみ）。（36R-06 命題 B）
6. **降下の限界**：自明類と境界類は全ての p で本物の点（t=0,∞ と t=±1）を持つので、降下では消せない。（36R-05 §4.3）
7. **固定 p の新しい判定**：F1 : Y²=X(X+p²)(X+p⁻²)、F2 : Y²=X(X+c²)(X+c⁻²) のどちらかが rank 0（捩れ Z/4×Z/2）なら E_p に retained 点なし。a<40 で 66%。（36R-05）

## 3. 暫定の分類

```text
STAGE36_CLASSIFICATION_PROVISIONAL = CLASS3_RETAINED_WITH_SHARPER_CAMPEDELLI_THEOREM
MISSING_THEOREM (T′) : ∀p∈Q∖{0,±1}: E_p(Q) ⊂ {t∈{0,±1,∞}}
   E_p : y1²=(t²+p²)(t²+p⁻²), y2²=(t²+c²)(t²+c⁻²), c=(p+1)/(p−1)
   全ての p、全ての高さ、点ごと。マスク a1a2a3≠0。
   (T′) ⇔ U(Q)=∅ ⇔ 全ての監査済み H で q_H(U(Q))=∅
R29_CAMP2_CLOSED=false  Q11_CAMPEDELLI_CLOSED=false  ENDPOINT_CLOSED=false  ALL_P_EXCLUSION=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false  PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

「より鋭い Campedelli 定理」として記録する内容は §2 の 1〜6。

## 4. 確定の前に要ること（優先順）

1. **外部査読**：36R-06 命題 A・B、36R-04 命題 3・4、36R-05 の反例 53/8。
2. **独立な白紙生成**：台帳（36-09 系、36R-06）を読んでいない別セッションで BLIND_REDISCOVERY を 1 回。新しい LIVE が出たら保留を取り消す。
3. **UNTESTED 2 件の再開条件を明記**：
   - B7（標準 Campedelli モデルからの移送）：U_H 版の算術的定理が文献にあれば再開。商全体の空性の移送は命題 A により不可。
   - N5（族に対する一様な非可換 Chabauty）：検査できる定理・実装が得られれば再開。

## 5. 並行してよいこと（受け皿は閉じない）

- 36-R6：rank 0 の L 関数による裏取り（ellrank のみの判定を確定させる）。
- 36-R7：査読の残り（a≤20 の要約、1G〜1T、36R-01/02 の査読束）。
- 固定 p の登録簿：F1/F2 判定の範囲拡大、38/23 の篩、境界類だけ残った 53/8・61/45、36-R2 の有限の補完作業。

## 6. やらないこと

- 固定 p の除外を増やすこと自体を目的にしない（v2 から継続）。
- 仮説 H に依存する無限性を増やさない（v2 から継続）。
- Brauer 経路（CAMP4）を CAMP2 の自動的な閉包として扱わない（v2 から継続）。
- **商全体の空性 C_H(Q)=∅ を目指さない**（命題 A で偽）。
- **Brauer–Manin で U_H(Q)=∅ を狙わない**（命題 B）。
- **局所条件だけで自明類・境界類を消そうとしない**（§2.6）。

## 7. ファイル

ローカル：`C:\Users\fizaw\claudework\stage36_resume\`（ログ `36R-00`〜`36R-06`、`scripts/`、`outputs/`、最新の状態 `04_STATE_local_after_36R-06.json`）。
