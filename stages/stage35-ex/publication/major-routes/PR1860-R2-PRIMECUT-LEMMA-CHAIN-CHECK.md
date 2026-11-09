# PR #1860｜R2-01 C187(155/197)の証明親を式単位で接続：first-entry／H補正／４枝

**2026-11-09／IN_PROGRESS／NOT_A_FULL_MATH_AUDIT／DO_NOT_MERGE。** 対象はC189が採用したC187の155/197 **下界**だけ。論理的親の使う命題を確認し、元の無限移動baseの物理sourceとの量化子を変更しない。R2目標のTRUE ４枝相関`strict<75%` **上界**や、完全直方体不存在とは別。

## 1. 「C185原著」の二つの識別子を混同しない

[このPRの数式原著](proofs/active-ancestors/C185-R2-prime-cut-original.md)の**本文の題名はR2 C184**（prime-cutの元提出）である。一方、[R0 C185統合本文](proofs/active-ancestors/C185.md)はそれを依存採用した親の受取側。ファイル名C185-R2-prime-cut-originalは**数学の同一性を示す利便的収載名**であって、「R2がもともとC185として定理を提出した」という歴史主張にはしない。さらに[C187の155/197原著](proofs/R2-uniform-thresholds.md)は、この採用済みC185係数をR0 C174/C175の全基底heightへ合成した後続結果。

## 2. 数学的に使う６つの論理辺

| 子で使う命題・式 | 具体的な親原著 | 何を継承し、何を継承しないか |
|---|---|---|
| 全signed整数`m,n`の同一`b_n`の公約数、odd first-entryの完全付値 | [S268 §3–4](proofs/C195-upstream/S268.md) → [R2 C160 §1–2](proofs/active-ancestors/C160-R2-strong-gcd-original.md) | S268の`r_n=B|Z_n|/b_n`はoriginal楕円軌道で定義、`gcd(b_n,2ABC)=1`。C160のSG.1は`v₂(m)=v₂(n)`なら`gcd(b_m,b_n)=b_{gcd(|m|,|n|)}`、異なれば１。SG.2は`p|b_m ⇔ m/h_p`が奇整数・`v_p(b_{h_pt})=β_p+v_p(t)`（odd t）。goodだけでなく**nodal H**でも形式群の単位元近傍を使う。完全物理packetの存在はこの恒等式の前提ではない。 |
| noncritical Hの初出`β_p`は`≤2v_p(H)`、criticalは**深さ無上限** | [S258 §2–4](proofs/active-ancestors/S258.md) と [S268 §4](proofs/C195-upstream/S268.md) | `T_e≤H_{odd}²`に**noncritical H initial-depthのみ**を入れる。criticalキャンセルを`T_e`へ紛れ込ませたりcapしたりしない。 |
| 元の同じS243四正整数根からの４canonical`z_i` | [S243](proofs/active-ancestors/S243.md) → [S275 §2–3](proofs/active-ancestors/S275.md) | `R_{J±}=(U₄±U₃)/κ, R_{K±}=(U₂±U₁)/κ`、`e_i=gcd(R_i,d)`から`R_i/e_i=z_i²`、`\prod_i z_i=b_m`・四つは互いに素。**canonical ４因子はexact-top GOOD/H protected４因子ではない**。S275の§4 twist全family NO-GOはC187下界の親でない。 |
| protected exact TOPと、proper first-entry・noncritical Hの厳密な差 | [S318 §2–3](proofs/active-ancestors/S318.md)、[S270 §4–5](proofs/foundations/S270.md) | `U_i|z_i`。noncritical Hが`h_p=m`となっても、S270 protectedには**含めない**。odd-prime mやdyadicでも「全topだから全protected」と省略しない。 |
| 必要な「proper」集合を素数割り指数だけに圧縮 | [R2 C184（C185で採用）原著 §3–5](proofs/active-ancestors/C185-R2-prime-cut-original.md) | `L_m=lcm_{\ell|m,\ell\;odd\;prime}b_{m/\ell}`。`R_m=gcd(b_m/L_m,m)`はsquarefree。`C_{prop}=gcd(b_m,mL_m)`、各枝`U_i=z_i/gcd(z_i,mL_m T_e)`、全ordinary βも一度だけ数える。S268の全odd除数`F_m`より疎なexact prime-cutを与える。 |
| all-base 155/197の有理二次式と正しい親の範囲 | [R2 C174原著](proofs/active-ancestors/C174-R2-hybrid-height-original.md)、[R5 C157原著](proofs/active-ancestors/C157-R5-eightP-height-original.md)、[R0 C175](proofs/active-ancestors/C175.md) → [C187](proofs/R2-uniform-thresholds.md) → [C189](proofs/active-ancestors/C189.md) | R5 C157の8P height→C174のC<65536でλ4／他でλ3→C175のκ=25408/727→C187の`Q4,Q1`。算術の端点照合は[別監査](PR1860-R2-CORE-PARENT-CHECK.md)。参照数を数学定理数にしない。 |

## 3. 本回の計算式の照合

同じoriginal `b_m`と`z_i`について、S268・C160により奇素数`\ell|m`なら`b_{m/\ell}|b_m`。`L_m`に含まれないproper p の不足指数は高々１で、`m`をかけることで完全に復元する。したがってC185の`\gcd(b_m,mL_m)`は、上位top pを紛れ込ませない**すべてのproper first-entry prime-powerの正確な積**。S258の`T_e`を追加した`z_i/\gcd(z_i,mL_mT_e)`が、**同じ４canonical枝に割り当てられた protected TOP**に一致する。この使用箇所では、単にS275の`z_i`をS270の`U_i`と同一視しない。

C184の素数和を別の有限有理数計算で点検した：奇素数`3≤\ell≤127`について`\sum\ell^{-2}+129^{-2}+1/258 ≈ 0.20486896565886165 < 41/200=0.205`。従って`1-4\sum\ell^{-2}>1-4(41/200)=9/50`で、１％の`\frac4{100}=1/25`を差し引くと`9/50-1/25=7/50`。この計算は**元C185の疎化係数の補助確認**にすぎず、全prime-cut分割・原始base写像・原証書の独立検証ではない。15/197でなく**155/197**であることも、[C187原著端点](PR1860-R2-CORE-PARENT-CHECK.md)と区別。

## 4. 旧側枝を「不足原著」として数えない

- [S271〜S274 Drive原著](PR1854-PASS2-SOURCE-DELTA.md)：dyadic fixed-coefficient biquartics、genus33 curve、eta twistsの履歴。C187に必要なS275 **§2 all-index canonical因子そのものはS243から本文内で証明**している。したがってS271–274を４本一括で「C187数学原著欠落」とは判定しない。ただしS275§4の**独立したtwist命題**まで監査するなら別層の原著。
- S280はC189の歴史的索引に現れるが、C187の`Q4/Q1`に使用する式としては確認されない。**現時点ではDIRECT_PARENT_NOT_ESTABLISHED**。C189全記事の歴史的整合とは別。
- S252の**Bérczes外部定理（§2/§5）**はH-only支持の指数上界`M_H`に使われる。C187の`λ_k`・155/197には、本文で導いた**S252 §3/4**の倍点高さ比較を使う。外部定理の一次出典を読まずにPASSとはしないが、C187下界の「必須の外部未収載親」としては数えない。

## 5. 自己完結の残ゲート

1. 上記の式の**独立**算術検証／同一`b_m`の原始positive labelled A/B向きとfull sourceの量化子接続は、依然`MATH_SUFFICIENCY_OPEN`。
2. C174の全20,856小基底検算・C175の大基底κ証書は第１周に保存した原証書の独立再演に含まれていない。
3. 相関した４protected TOPの`strict<75%` **上界は新たに証明していない**。155/197は反対向きのLOWER。
4. 元の物理sourceが、選択したsame baseとsigned`D_n=T0+2nP`に必ず送られるという大域forwardは別ゲート。R2数式の内部正規化だけで解決したとはしない。

本PRは**Draftのまま**。正式R0／研究NEXT不変更。必要数学原著の全再帰総数は未確定。
