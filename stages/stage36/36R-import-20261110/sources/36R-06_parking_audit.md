# 36R-06 — 36-09 保留監査（Cycle Exploration Safety Protocol）（2026-10-14）

```text
UNIT=36-09 保留監査（36R-04・36R-05 による受け皿の実質的な変更を受けたもの）
PROTOCOL=docs/research-os/policies/cycle-exploration-safety-protocol.md（§4 EXHAUSTIVE_VIEW_AUDIT, §5 BLIND_REDISCOVERY, §8 保留規則）
NEW=(i) C_H(Q) は全ての監査済み H で無限集合（証明つき）
    (ii) Brauer–Manin 障害では U_H(Q)=∅ も U(Q)=∅ も原理的に示せない（Br について証明つき）
36-10 CLASSIFICATION（暫定。外部／hostile 監査前）=CLASS3_RETAINED_WITH_SHARPER_CAMPEDELLI_THEOREM
R29_CAMP2_CLOSED=false  Q11_CAMPEDELLI_CLOSED=false  ENDPOINT_CLOSED=false  ALL_P_EXCLUSION=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false  PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
これは研究管理上の保留であって、receiver の数学的な閉鎖ではない（追補 06 §4）。
```

## 0. 監査の入力

| 項目 | 内容 | 根拠 |
|---|---|---|
| 受け皿 | R29-CAMP2（Stage29-02hb）／K16-C3-CAMPEDELLI-UNIFORM-TORSOR（Stage29-16）。変更なし | 追補 06 §1 |
| 決定的な帰結 | 監査済みの H のどれかで q_H(U(Q))=∅ | 36-09 `sufficient_replacement_target` |
| 現在の正確な形 | (T') ∀p∈Q∖{0,±1}: E_p(Q) ⊂ {t∈{0,±1,∞}}。U(Q)=∅ と同値 | 36R-00 命題 1、36R-04 命題 3・4 |
| 前回の台帳 | 36-09I（B1〜B11, C2）、36-09T/V/W/Y/Z による更新 | `stages/stage36/36-09*/` |
| 実質的な受け皿の変更 | 36R-04（J と C_H の関係、端点 ⇔ δ1δ2=平方）、36R-05（端点 Selmer、反例 53/8） | §3 の起動条件 4 と 5 |

起動条件（プロトコル §3）：4（新しい厳密な同一性）と 5（保留しようとしている）に該当する。

## 1. 新しく示したこと（監査の途中で得た2つの事実）

**命題 A（C_H(Q) は無限）.** 監査済みの全ての核 H（10 個）で C_H(Q) は無限集合。
証明：既約なピタゴラス三つ組 (a1,a2) と a3=0 で、7 つの値 x=a1², y=a2², 0, x+y, x, y, x+y は全て平方なので、
(a1,a2,0,…) は Sbar の Q 点。底の点 [x:y:0] を通る分岐線は A3 だけ（三重点でも二重点でもない）なので、
Sbar の滑らかな点で、像は Cbar_H の滑らかな点（A1 点は三重点の上にしかない、29-02hb §3）。
よって解消 C_H に一意に持ち上がり、C_H(Q) の点になる。三つ組は無限にあり、底の点は相異なる。∎
（機械検算：`scripts/36R-06_boundary_points.py`、27 個の三つ組で全条件を確認）
これらの点は a3=0 なので U の外、したがって U_H の外（36-03：q_H⁻¹(U_H)=U）。

系 A.1 **C_H(Q)=∅ という形の主張は偽**。36-10 の `R29_CAMP2_CLOSED_BY_QUOTIENT_EMPTINESS` は、商全体の空性の意味では到達不能で、
使えるのは制限された受け皿 U_H(Q)=∅（36-09 の第 1 形）だけ。36-03 の `global_C_H_Q_points_on_branch_are_not_ruled_out=true` は、実際に点がある、に強められる。

**命題 B（Brauer–Manin は U_H(Q)=∅ を示せない）.** 全ての監査済み H で
`U_H(A_Q) ∩ C_H(A_Q)^{Br} ≠ ∅`。したがって Brauer–Manin 障害で U_H(Q)=∅ を示すことはできない。
証明：C_H は滑らかな射影曲面で q=p_g=0。よって Pic(C̄_H) は有限生成、Br(C̄_H) ≅ H³(C_H,Z)_tors は有限で、Br(C_H)/Br₀ は有限。
代表 A_1,…,A_m をとる。有限集合 S があって、v∉S では各 A_i の評価は C_H(Q_v) 上で恒等的に 0。
命題 A の点 P は滑らかなので、各 v で P に v 進的に近い U_H(Q_v) の点 Q_v がある（U_H は稠密な開集合）。
評価は局所定数なので、v∈S では Q_v を十分近くとれば ev_{A_i}(Q_v)=ev_{A_i}(P)。v∉S ではどちらも 0。
よって Σ_v ev_{A_i}(Q_v) = Σ_v ev_{A_i}(P) = 0（相互律）。(Q_v) ∈ U_H(A_Q) ∩ C_H(A_Q)^{Br}。∎
- 同じ議論は S と U（端点そのもの）にも、境界点 (3,4,0) を使ってそのまま通る。
- エタール Brauer 集合についても、P を含むひねりの上で同じ議論が通るはずだが、ここでは書き切っていない（概略のみ）。

## 2. BLIND_REDISCOVERY（受け皿 (T') と U(Q)=∅ だけから生成）

**開示**：この会話の前半で 36-09 と 36-09I の台帳を読んでいるので、プロトコル §5 の「台帳を見ずに生成」は完全には守れていない。
生成は受け皿から先に行い、照合は後に行ったが、独立性は保証できない。独立な白紙生成を別のセッションで行うことを推奨する（§6）。

| ID | 見方 | 分類 | 理由 |
|---|---|---|---|
| N1 | 曲線族の一様な点の個数評価（Stoll、Katz–Rabinoff–Zureick-Brown、Dimitrov–Gao–Habegger） | BLOCKED | 個数の上界であって空性ではない。E_p には既知点が常にある（t=0,∞,±1）ので、上界がそれ以下でない限り何も出ない |
| N2 | モジュラー法（Frey 曲線・レベル下げ） | BLOCKED | 定義方程式は全て 2 次。レベル下げに要る ℓ 乗（ℓ≥3 の指数）がない |
| N3 | Bombieri–Lang／Vojta | BLOCKED（無条件の主張として） | 予想。仮定しても例外曲線の外の有限性で、空性は出ない |
| N4 | F1・F2 の Q(p) 上の楕円曲面（生成ランク＋特殊化） | BLOCKED（一様な主張として） | 特殊化でランクが上がる（a<40 で 34% の p は両方 rank≥1）。固定 p の判定（66%）としては有効 |
| N5 | 族に対する一様な非可換 Chabauty（Kim、族の 2 次 Chabauty） | UNTESTED（保持） | 研究の最前線で、ここで検査できる実装も定理もない。rank が族で有界かも不明 |
| N6 | 錐の整数点（Siegel 型） | BLOCKED | スケーリングで有理点は全て整数点になり、得るものがない |
| N7 | L 関数・BSD による族の扱い | DOMINATED | 固定 p の rank 0 判定（36-R6）に含まれる |
| N8 | E_p = Φ1 ×_t Φ2（2 本の種数 1 曲線の t 座標の一致） | EQUIVALENT（N4 と） | Φ_i は F_i と同種（次数 2 の写像 (t,y)↦(t², ty)） |
| N9 | 端点の類の一様な局所消去 | BLOCKED | 反例 53/8（36R-05） |
| N10 | 商 C_H 上の Brauer–Manin | BLOCKED（原理的） | 命題 B |
| N11 | C_H の空性 | BLOCKED（偽） | 命題 A |

## 3. 台帳との照合（36-09I/T/V/W/Y/Z の状態から更新）

| 台帳 | 前の状態 | 新しい状態 | 根拠 |
|---|---|---|---|
| B1 一様な H¹ Selmer | BLOCKED | BLOCKED（強化：C_H(Q) は無限なので、降下は非自明な H-トルソル類を持つ無限個の商の点を扱う必要がある） | 36-05、命題 A |
| B2 単一の位での障害 | BLOCKED | BLOCKED（強化：自明類・境界類は全ての p で大域の点を持つ） | 36-09I、36R-05 §4.3 |
| B3 有限の曲線・被覆への分解 | LIVE → C3_p 連鎖 | BLOCKED（一様な主張として）。固定 p の登録簿としては有効 | 36-09J〜FE、36R-03/05 |
| B4 制限つき分岐交わり | BLOCKED | EQUIVALENT（Im_H∩Im_J=Im_U） | 36R-04 命題 3 |
| B5 Brauer／エタール Brauer | BLOCKED_UPSTREAM | **BLOCKED（原理的、Br について証明つき）** | 命題 B |
| B6 曲線底への fibration | BLOCKED | BLOCKED（r は C_H に降りない） | 36-09G、36R-04 命題 5 |
| B7 標準 Campedelli モデルからの移送 | UNTESTED | **UNTESTED（保持）**。商全体の空性の移送は不可能（命題 A）。U_H 版を移送できる文献の定理は見つからなかった（Web 検索 2 件、§5） | 検査できる対象がない |
| B8 幾何・位相的分類 | BLOCKED | BLOCKED | 36-09 |
| B9 漸近・篩 | DOMINATED | DOMINATED | 36-09 |
| B10 中間符号商・指標 | DOMINATED | DOMINATED（J=S/⟨g⟩ もその1つ） | 36-09I、36R-04 |
| B11 多くの位の相互律 | BLOCKED（一様な閉鎖として） | BLOCKED | 36-09Z |
| C2 Gauss 整数のノルム圧縮 | BLOCKED | BLOCKED | 36-09V |
| 36-09Z「受け皿固有の交わり」 | LIVE_NEXT | EQUIVALENT（命題 3 で端点と同値。固定 p の登録簿 36-09AA〜FE として消化済み） | 36R-04 |
| N1〜N11 | 新規 | §2 のとおり | |

集計：LIVE 0、UNTESTED 2（B7、N5。どちらも今は検査できない理由つき）、他は BLOCKED／EQUIVALENT／DOMINATED。SPLIT の条件（LIVE か高価値の UNTESTED が 2 つ以上で、互いに独立）は満たさない。

## 4. 保留規則（プロトコル §8）の確認

| 条件 | 状態 |
|---|---|
| 未処理の LIVE がない | 満たす（0） |
| 全ての候補が BLOCKED／EQUIVALENT／DOMINATED、または理由つきで UNTESTED | 満たす（B7、N5 は理由つき） |
| 最後の受け皿の変更（36R-04/05）以降に EXHAUSTIVE_VIEW_AUDIT と BLIND_REDISCOVERY を実施 | 実施した。ただし BLIND は事前露出を開示（§2） |
| 欠けている定理を量化子・測度・高さ・マスクつきで明示 | §5 |
| 不可能性を主張しない | 主張していない（命題 A・B は特定の形の主張についてだけ） |

## 5. 欠けている定理（保留時に記録する Class-3 の未解決障害）

```text
MISSING_THEOREM (T'):
  ∀ p ∈ Q∖{0,±1}:  E_p(Q) ⊂ { t ∈ {0, ±1, ∞} },
  E_p : y1² = (t²+p²)(t²+p⁻²),  y2² = (t²+c²)(t²+c⁻²),  c=(p+1)/(p−1)
量化子：全ての p（例外なし）、全ての高さ。測度・密度ではない（点ごと）。
マスク：物理的開集合 a1a2a3≠0（境界 t∈{0,±1,∞}, p∈{0,±1,∞} は 36R-04 §2 の表）。
同値：(T') ⇔ J と端点の条件 ⇔ U(Q)=∅ ⇔ 全ての監査済み H で q_H(U(Q))=∅（36R-00, 36R-04）。
```

**より鋭い Campedelli 定理（保留時に記録する、証明済みの部分）.**
1. 全ての監査済み H で Im_U = Im_J ∩ Im_H。J 上で H-トルソル条件は δ1δ2=平方 の 1 本に尽きる（36R-04 命題 2・3）。
2. 全ての監査済み H で C_H(Q) は無限（命題 A）。商全体の空性は偽で、受け皿は U_H(Q) の形でしか閉じ得ない。
3. Brauer–Manin 障害では U_H(Q)=∅ は示せない（命題 B）。
4. retained 点の C3_p の類は T_end(p) に入り、局所像を通るのは a<70 の 99.7% で自明類と境界類だけ。この 2 類は全ての p で大域の点を持ち、降下では消せない（36R-01、36R-05）。
5. 固定 p の除外の道具：F1/F2 の rank 0（a<40 で 66%）、組曲線、E_ρ/E_τ、X_λ/Y_λ の QC（36R-03, 36R-05, 本線 1G〜1T）。∀p には届かない。

**文献の確認（B7）.** Campedelli 曲面の有理点・Brauer 群についての算術的な定理を Web 検索で探したが、該当するものは見つからなかった
（一般論のみ：[Colliot-Thélène の講義](https://www.imo.universite-paris-saclay.fr/~colliot/CTSDAA.pdf)、[Brauer–Manin と Ш](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/42C530BD1F7C692B7B89B3E857D33DB6/S1461157000001455a.pdf/the-brauer-manin-obstruction-and-iii2.pdf)）。
直方体の曲面の側では [The fundamental group of surfaces parametrizing cuboids（arXiv 2310.12710）](https://arxiv.org/pdf/2310.12710) が π₁ を扱っているが、算術的な空性の定理ではない。
検索は 2 回だけで網羅的ではない。B7 を UNTESTED のまま保持する理由として記録する。

## 6. 判定と次の手続き

```text
CYCLE_ROUTE_STATUS=BLOCKED_NEW_PATTERN_ISOLATED
CYCLE_ACTIVE_RECEIVER=(T') ⇔ U(Q)=∅ ⇔ q_H(U(Q))=∅ (全 H)；商の側は U_H(Q)=∅（C_H(Q) は無限）
CYCLE_LIVE_CANDIDATES=0
CYCLE_UNTESTED_CANDIDATES=2 (B7, N5)
CYCLE_EXHAUSTIVE_VIEW_AUDIT=true
CYCLE_BLIND_REDISCOVERY=true（事前露出を開示。独立な再実施を推奨）
CYCLE_SPLIT_TRIGGERED=false
CYCLE_PARKING_AUDIT_COMPLETE=true（暫定。BLIND の独立性と命題 A・B の査読が条件）
CYCLE_NEW_VIEW=商の有理点は境界のピタゴラス点で無限、Brauer–Manin は境界点の近傍で必ず通る
CYCLE_NEW_VIEW_SOURCE=INTERNAL_DERIVATION
STAGE36_CLASSIFICATION_PROVISIONAL=CLASS3_RETAINED_WITH_SHARPER_CAMPEDELLI_THEOREM
```

- **保留を推奨する**：36-10 の 4 つの語のうち、到達可能で根拠があるのは `CLASS3_RETAINED_WITH_SHARPER_CAMPEDELLI_THEOREM` だけ。
  `R29_CAMP2_CLOSED_BY_QUOTIENT_EMPTINESS`（商全体の形）は命題 A により不可能、U_H の形と `…_BY_RECEIVER_MATCHED_REPLACEMENT` は (T') の証明を要し未達、`SPLIT_TRIGGERED_DISTINCT_OBSTRUCTIONS` は条件を満たさない。
- **確定させる前に要るもの**（研究管理上の手続き。数学的な閉鎖ではない）：
  1. 命題 A・B の外部／hostile 査読（短く、査読しやすい。36-R7 に追加）。
  2. 独立な白紙生成（BLIND_REDISCOVERY）を、台帳を読んでいない別のセッションで 1 回。新しい LIVE が出たら保留を取り消す。
  3. 36R-04 命題 3・4、36R-05 の反例の査読。
- 保留後も、固定 p の登録簿（36-R5/R6）と査読（36-R7）は並行して続けてよい。ただし ROADMAP §6 のとおり、固定 p の除外を増やすこと自体は目的にしない。

## 7. 維持したもの・限界

- 既存の Stage36・Stage38 の成果はすべて維持。台帳の旧い状態は上書きせず、この表で更新理由を併記した。
- 命題 B の「v∉S で評価が恒等的に 0」と「Br/Br₀ が有限」は標準的な事実として使った（q=p_g=0 の滑らかな射影曲面）。エタール Brauer への拡張は概略のみ。
- 命題 A は初等的で、機械検算もしている。
