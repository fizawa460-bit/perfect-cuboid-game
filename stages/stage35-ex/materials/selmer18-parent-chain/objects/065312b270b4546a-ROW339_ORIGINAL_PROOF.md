# Stage35EX / R3-07 — 他の signed index への排除拡張：|n|=18、種数17商の163進一点円盤ゲート

- RUN: `R3-20261102-SIGNED18-G17-P163-ONE-DISK-CANDIDATE`
- 日付：2026-11-02 JST
- 対象：Stage35EX Branch B / R3-07_ONLY / original indexed signed n=+18,−18
- 判定：`NEW_SCOPED_DEPENDENT_ARITHMETIC_PREFLIGHT`（p=163 finite arithmetic exact PASS） / `ONE_DISK_GATE_CONDITIONAL` / `TRUE_MW_ANNIHILATOR_NOT_COMPUTED` / `SOURCE_EXCLUSIONS_FORMAL=0` / `BRANCH_B=OPEN` / `R0 C35-200 UNCHANGED`

## 1. 着手前の重複判定と現在の原典

元の有理 source は一つの正の primitive labelled A²+B²=C², C odd、original E:y²=x(x−A²)(x+C²), P=(AC,ABC), T0=(0,0)、元の signed D_n=T0+[2n]P と厳密に固定する。元の scalar σ_n=B²+x(D_n)>0 の有理平方は full source の必要条件（旧S263）。S269 は真の同一 primitive integer Gaussian、actual signed POINT、W_n/W_(2|n|)、S243 の四正整数根／共通 c、Q/Qsharp、負の実物理符号、必要時TRUE S270全GOOD/H TOP/PROPERを保持し、補助曲線上の自由な有理点と同一視しない。

旧R1-239 (`1a2gIRRMh7ve0FWFTyF_-KDXci3fEpEDiTKk7E1w3tD4`)：B-even 側は旧S264で |n|=18 除外済み。A-even/B-odd 側では original σ_±18 が有理平方なら actual W17,W19 の four homogeneous Ward factors G_i (度数36,36,45,45) が全て正の整数平方。さらに独立有限体検証により p∈{3,7,11,19,31,47,163,251} | A を要求する（163はその1つ）。旧R1-256 (`1Bg3HTX34RPd_0D_Ged9dgmFotw20S-dY`)：これらを四個の単因子有理平方点 g_i(z), z=B⁴/(AC)² として genus17,17,22,22 の character 曲線に移す論理および逆像条件はすでに証明。**種数17商を新規構成と再登録しない。** 旧R1-240 の「任意有限素数集合の局所平方だけでは原sourceを排除できない」方法制限を継承し、有限素数追加で閉鎖したと主張しない。

旧R3 row338 p23 genus7 は signed -12 専用の f11/f13 とその同一source t±点であり、異なる f17/f19 からなる |n|=18 に23進消滅微分をそのまま転用しない。旧C118±6、旧R1-237±14、旧R5-C205±16、旧R1-243±20/±22 等の既出除外を再creditしない。

## 2. ±18 同一sourceに固有の163進局所円盤

旧R1-239の真正 monic irreducible g_{17,1},g_{17,2} ∈ Z[Z] は度数36、f17(Z)=g_{17,1}(Z)g_{17,2}(Z)。各々の正整数平方 `G_i(U,V)=V^72 g_i((U/V)^2)`（U=B², V=AC）から、`g_i(z)` は正の **有理** 平方（V^72 自体が平方）。

逆数モデルを取る：

\[
 h_i(X)=X^{36}g_{17,i}(1/X)\in\mathbf Z[X],\qquad C_i:Y^2=h_i(X),\qquad g(C_i)=17.
\]

旧R1-256の同種数商を reciprocal 記法で明示したのみで、新しい曲線分類creditなし。任意の元 source はそれぞれの C_i 上で

\[
 X=1/z=(AC/B^2)^2>0,\qquad
 Y_i=X^{18}\sqrt{g_{17,i}(z)}\in\mathbf Q,\qquad Y_i^2=h_i(X)
\]

を与える。163|A, gcd(A,B)=1 なので B は163進単元、したがって

\[
 v_{163}(X)=2v_{163}(AC/B^2)\ge2.
\]

一方 g_i は monic より `h_i(0)=1`。各 Y_i の符号を選択すれば `Y_i≡1(mod163)`。よって元sourceの必要有理点は常に C_i の P0=(0,1) と同一の163進残余円盤、かつ X≠0 を占める。これは正規化された **source forward 必要条件** であって補助点からsourceへの逆命題ではない。

## 3. 今回新しく厳密検査した p=163 finite 算術

添付 stdlib+SymPy 検証コードで original f0..f19 の正規化漸化式を再構築し、f17=monic36*monic36, f19=−monic45*monic45 を exact factor_list で再検査。p163で `t=A/C` の非零162残余を全て検査し、4因子が同時に平方（0を含む）となるものは **0件**。したがって p163∤AC は source 条件と矛盾する（旧R1-239の独立再現であり新credit0）。

次は今回の新finite算術。2本の reciprocal `h_i` は mod163で squarefree：

- g17第一因子：g(0)=17、h(0)=1、h mod163 既約因子次数 2,4,30。
- g17第二因子：g(0)=1、h(0)=1、h mod163 既約因子次数 6,6,10,14。

従って C_i は双方163で良還元。係数 `h_i^(81)` mod163 から17×17 Hasse–Witt 行列 `M_{ij}=[X^(163i−j)]h_i^81` (i,j=1..17) を exact polynomial arithmetic で計算。結果：

| 曲線 | det(M) mod163 | det(I−M)=#Jac(F163) mod163 |
|---|---:|---:|
| C_1 | 90 | 139 |
| C_2 | 95 | 90 |

いずれも det(M)≠0 なので163でordinary、Jac(F163)位数も163と互いに素。**#Jac(F163)そのもの、真MW rank、真Coleman logは未計算**。Hasse–Witt有限演算値は独立外部 hostile 監査待ち。コードと再現JSONを保全。

## 4. 有効な一点円盤 Coleman 排除定理（十分条件／未実現）

C_i上で g=17 個の正則微分基底 `ω_j=X^j dX/(2Y), 0≤j≤16` を取る。以下を必要とする。

(AN_i) **真の**全Jac_i(Q)を消す163進正則微分
\[
\omega=\sum_{j=0}^{16}a_j X^j\frac{dX}{2Y},\qquad a_j\in\mathbf Z_{163},\quad a_0\in\mathbf Z_{163}^{\times}
\]
が存在する（真rank/finite-index MW、または別法で真全消滅空間を確保）。このとき163進P0円盤に属する任意の有理点P=(X,Y)で X∈163 Z163, X≠0, Y≡1 mod163 は**存在しない**。

証明：局所座標Xの下で `ω=b(X)dX`, `b∈Z163[[X]]`, `b(0)=a0/2` は単元。`F(X)=∫_{P0}^{(X,Y)}ω=∑_{k≥1}b_{k−1}X^k/k`。X∈163Z163の非零値について、`F(X)/X ≡ b0 (mod163)` が成立する。k≥2項は `v163(X^(k−1)/k)≥1` で全て消える。よって `F(X)≠0`。全Jac(Q)消滅微分なら有理点P−P0の Coleman 積分は0でなければならず矛盾。∎

ここでは old signed−12 same-pair ±X を使う必要はなく、**片方の曲線の1個の同一source有理点**を排除すれば±18の両符号を一度に除外できる。ただし (AN_i) は未証。普通還元や p∤#Jac(F163) **だけでは** (AN_i) は成立しない。

## 5. 行列としての次の必要証明

優先順位：少なくとも一つの C_i の真MW階数 r_i<17 と有限指数で全rankを張る有理Jac divisor格子（または直接真annihilator）を厳密認証。次に163進ログを誤差保証付きで計算。行列 `L∈Q_163^(r_i×17)` の左零空間ではなく **係数列のkernel** に `a0` が163進単元のベクトルを得る。適切な163正規化で `Lbar` が F163 上 full row rankであれば、`e0=(1,0,...,0)` が Lbar のrow spanに入らない（`rank([Lbar;e0])=r_i+1`）ことが、mod163で a0≠0 のannihilatorが存在するための十分条件。163-adic precision・pivot・log誤差伝播の個別認証は必要。

これが成功すれば原S263 signed ±18とR1-239の四正整数平方/163|Aの必要方向を使い、同一source signed ±18を排除できる（S269 actual signed POINT等を緩和した source を対象にするので一方向の必要条件として十分）。**成功していない現時点では signed18 の源排除0、Branch B OPEN、R0 正式採択C35-200不変更。**

## 6. 重複・命題境界

- OLD・新credit0：S263、R1-239 四global factor square / p163|A、R1-256 genus17 character quotients / inverse base、R1-240 arbitrary finite prime saturation、元R3 row338 genus7 p23 annihilator・same-source −12。
- 新しい**限定算術検算と研究接続**：旧g17に対する reciprocal P0=(0,1) のp163 good ordinary / #Jac mod163 nonzero の全二曲線算術証明書、および同一元sourceが `v163(X)≥2` のP0残余円盤に落ちるという明示的163進受信ゲート。局所一点排除補題は標準Coleman/積分の直接帰結であり、数学的独立新定理として重複creditしない。
- 未証明：両 genus17 の真MW rank/有限指数生成、実際の163進annihilatorと `a0` unit、true signed±18 source排除、任意他indexへの拡張、g10同一tとS269 actual signed POINTの全領域、Branch B 閉鎖。

索引へは R3-07 の限定数学的到達点／行き詰まりとして登録。signed18の full original indexed exclusion、他の signed index、完全直方体不存在は報告しない。

