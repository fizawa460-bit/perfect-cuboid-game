# PR #1860｜R2-01 C189→C187(155/197) 数学親の再帰的確認

**状態：IN PROGRESS / NOT A CLOSED PROOF DAG / DO NOT MERGE。** 対象はR2-01の採用下界C189/C187だけ。R2以外の路線や99ルートは探索しない。

## 結果：17原著のGitHub存在を実際に再確認

| 数学親 | このPRで確認した実ファイル |
|---|---|
| C189 | [GitHub本文](proofs/active-ancestors/C189.md) |
| C187 | [GitHub本文](proofs/R2-uniform-thresholds.md) |
| C185 | [GitHub本文](proofs/active-ancestors/C185.md) |
| C185-owner | [GitHub本文](proofs/active-ancestors/C185-R2-prime-cut-original.md) |
| C160-owner | [GitHub本文](proofs/active-ancestors/C160-R2-strong-gcd-original.md) |
| C174 | [GitHub本文](proofs/C195-upstream/C174.md) |
| C174-owner | [GitHub本文](proofs/active-ancestors/C174-R2-hybrid-height-original.md) |
| C157-owner | [GitHub本文](proofs/active-ancestors/C157-R5-eightP-height-original.md) |
| C175 | [GitHub本文](proofs/active-ancestors/C175.md) |
| S252 | [GitHub本文](proofs/active-ancestors/S252.md) |
| S268 | [GitHub本文](proofs/C195-upstream/S268.md) |
| S270 | [GitHub本文](proofs/foundations/S270.md) |
| S275 | [GitHub本文](proofs/active-ancestors/S275.md) |
| S318 | [GitHub本文](proofs/active-ancestors/S318.md) |
| S243 | [GitHub本文](proofs/active-ancestors/S243.md) |
| S269 | [GitHub本文](proofs/C195-upstream/S269.md) |
| S267 | [GitHub本文](proofs/active-ancestors/S267.md) |

R0統合要旨だけでは閉じない箇所について、本PRで著者原証明として **C160 strong-gcd、C185 prime-cut、C174 hybrid-height、R5 C157 8P** を新たに収載した。C175 conditional upperの著者原著２本も別途保存したが、155/197の**LOWER**導出の必須数学親とは混同しない。

## 継承している主な数学的な式と範囲

| 子 | 数学的親 | 必要な式・意味 |
|---|---|---|
| C189 | C187 | ADOPTION_155_197：C189.md body accepts C187 dependent bound |
| C187 | C185-owner | LOWER_QUADRATIC_SOURCE：C187.md old C185 9/50 and7/50; C185 owner §3-5 |
| C185-owner | C160-owner | ALL_INDEX_STRONG_GCD_INPUT：C185 owner §2 S268/C160 first entry and strong-gcd; R2 owner SG.1/SG.2 |
| C185-owner | S268 | FIRST_ENTRY_AND_TOP_PROPER：owner §2 old S268 §4 first-entry |
| C185-owner | S275 | FOUR_CANONICAL_FACTOR_INPUT：owner §2 S275 §2 and TOP/PROPER caveat §3 |
| C185-owner | S318 | NONCRITICAL_H_CORRECTION：owner §2 S318 H factor separation |
| C187 | C174-owner | ALL_BASE_LAMBDA_SELECTION：C187.md cE<12κλ* from C174/C175 |
| C174-owner | C157-owner | UNIFORM_EIGHTP_HEIGHT：C174 owner §2 λ3>L/16-41/768 from R5 C157 8P original |
| C174-owner | S252 | CANONICAL_HEIGHT_CERTIFICATE：C174 owner λ_k uses S252 §3–4 |
| C187 | C175 | KAPPA_TIGHTENING：C175 R0 §3 proves κ=25408/727 correction with C174 hybrid |
| S270 | S268 | FOUR_TOP_MASS：S270 §4 uses S268 §4 joint cofactor, S268 height estimates |
| S270 | S252 | NON_TORSION_AND_HEIGHT_ONLY：S270 §5 uses S252 §3-4, not H-supported §2 |
| C187 | S270 | FOUR_GENUINE_TOP_SCOPE：C187 keeps S270 four GOOD/critical H TOP, PROPER full beta |
| C187 | S243 | SAME_GLOBAL_FOUR_ROOTS：C187 source lock retains S243 integer four roots |
| C187 | S269 | SAME_SIGNED_GAUSSIAN：C187 source lock retains original Gaussian F/G point collision |
| C187 | S267 | ACTUAL_CRITICAL_H_MASK：C187 inherited S267 correct H classification |

## 重要な訂正：外部Bérczes定理は155/197下界の直接親ではない

[S252](proofs/active-ancestors/S252.md)の役割は分離する。

- **S252 §2と§5**：Bérczes et al. Theorem 2.1(i) で `H`-supported S整数座標の高さ上界 `M_H` を得て、指数上界 `N_H` に用いる。この分岐はその外部定理の適用の独立照合を必要とする。
- **S252 §3と§4**：楕円曲線の倍点の正確な同次resultant `R_E=256D^8H^4`、高さ比較 `|h(x(Z))−2hhat(Z)|≤c_E/3`、および正の `λ_k≤hhat(P)` を本文内で導く。**BérczesのM_Hを使用しない**。
- **S270 §4と§5**：その `λ_k` とS268の第一出現指数、４つの真TOPの全普通βを利用して、４枝のLOWERを導く。S252のH-supported `M_H` は式(269.7)〜(269.10)の前提ではない。
- **C185、C187**：S270/S268/C160/S275/S318・C174/C175の低側評価を使用。したがって現時点では **BérczesはC187の155/197を自己完結させる上で必須の未確認外部ゲートではない**。S252全章の主張まで監査するなら当然別ゲートとして残る。

## C187端点の独立有理数検算（代数式の一部だけ）

本文と同じ

\[Q_4(m)=\frac9{50}m^2-\frac{292192}{10905}m-\frac{107190}{727},\quad Q_1(m)=\frac7{50}m^2-\frac{292192}{10905}m-\frac{2692454}{18175}\]

について、整数有理数で再計算：

| 端点 | 厳密値 |
|---|---:|
| Q₄(154) | −266408/54525 |
| Q₄(155) | +104425/4362 |
| Q₁(196) | −1176986/54525 |
| Q₁(197) | +724039/109050 |

各二次式の導関数はそれぞれ155、197以降正。よって**与えられた親不等式を前提**にした切替端点の符号と単調性は一致。ただしこれはC175の一様 `κ` 証書、C185四枝不等式、S270元source同一性を独立再証明したPASSではない。

## 残りの依存監査

1. R2 S268の本来の第一出現・全ordinary-betaに対するS270、C185の適用が同一base／同一signed `D_n` で成立するか確認。
2. C174/R5 C157の全基底高下界 `λ_k` の仮定とR0 C175の `κ=25408/727` の全域証書が数学的に十分か継続照合。
3. S243四正整数根、S269原始Gaussian実点衝突、S275全指数canonical factorizationの仮定を固定して、旧条件の無断昇格を防ぐ。
4. 155/197は**保護された四枝の下界**であり、R2の主目標 `strict <75% ` 上界でも物理的排除でもない。証明鎖の資料充足と研究の完成は混同しない。

数学的必須親の**全再帰閉包、独立監査、未収載原著の追加探索は継続**。本PRはDraftのままで完了を宣言しない。
