# Stage35EX R3-07 row358 — 全有限素点の偶付値への還元と真正2-Selmer上界17

2026-11-04 / P23-R3-LOW / 固定signed ±18のC₂のみ

**新しい限定成果（内部証明、独立数学監査待ち）：**

\[
 h_K=|\mathrm{Cl}(\mathcal O_K)|\le15,\qquad
 c_K=\dim_{\mathbb F_2}\mathrm{Cl}(\mathcal O_K)[2]\le3,
\]
\[
 \dim\operatorname{Sel}^{(2)}(J_2/\mathbb Q)\le14+c_K\le17,
 \qquad 7\le\operatorname{rank}J_2(\mathbb Q)\le17.
\]

従来の監査済み数値上界31を17へ改善する。ここで **c_Kは通常類群、c_SはS類群**であり、同一視しない。row357の監査済み h_S≤13、c_S≤3 はそのまま保存する。

今回の主な差分は、既に完全生成された有限局所fake像がすべて単数代表を持つことを使い、全球fake候補を「全有限素点で付値が偶数」の空間へ入れる点にある。未構成のS付値方向を個々に生成せず処理できる。局所像の新しい生成定理や古典解析手法の発明としては再計上しない。通常類数の次数16排除はrow357のTable4補助検算でも既に扱われており、今回はそれを数値表に依存しない直接証書にする。この部分単独に新しい上界としてのcreditは付けない。

## 1. 対象と継承する証明

K=Q(θ)、h₂(θ)=0、deg h₂=36、C₂:y²=h₂(x)、J₂=Jac(C₂)、g=17。
正確な37係数は `math/parents/order.json` の `h2_coefficients_ascending` に固定し、同一係数をrow342由来の有理除数、row355、単数資料と照合する。h₂はmonic、h₂(0)=1で、P₀=(0,1)は有理点である。

\[
 (r_1,r_2)=(4,16),\qquad
 D_K=2^{24}\cdot2843\cdot13963\cdot329475607
 \cdot1034386920659\cdot23910039195629
 =5427028083166736357520103768895827763994388594688.
\]

継承する事実は次のとおり。

| 親成果 | 継承する範囲 |
|---|---|
| row344/345 | 最大整環、正確な判別式・signature、各局所の分解と真正Kummer次元 |
| row351/352 | 真正Selmerからfake平方類への写像、核次元≤1、既知MW下界7 |
| row353 | 5奇bad素点での真正局所像の完全生成。独立監査済みの範囲を継承 |
| row355 | Q₂でfake18次元・真正19次元の完全生成。独立PASS_SCOPED |
| row356 | 実在する全球単数4証人による追加rank4。独立PASS_SCOPED |
| row357 | h_S≤13、c_S≤3、真正≤31。2026-11-04の独立PASS_SCOPEDを現行正本から採用 |

旧成果の監査合格を今回の新しい大域還元・通常類群評価の監査合格へ転用しない。

## 2. すべての有限局所fake像は単数で表せる

K_p=K⊗Q_p=∏_{𝔭|p}K_𝔭とし、局所fake標的を K_p*/(K_p*² Q_p*) とする。

| p | (e_𝔭,f_𝔭) | 完全fake像の次元 | 単数代表を持つ生成元 |
|---|---|---:|---|
| 2 | (3,4),(3,8) | 18 | row355の旧6・不分岐3・tame9 |
| 2843 | (1,1)×3,(2,1),(1,15),(1,16) | 4 | D1a,D1b,D2,E4 |
| 13963 | (1,1),(2,1),(1,33) | 1 | D1a |
| 329475607 | (1,1)×2,(2,1),(1,32) | 2 | D1a,D4 |
| 1034386920659 | (1,1),(2,1),(1,33) | 1 | D1a |
| 23910039195629 | (2,1),(1,10),(1,24) | 1 | D1b（真正像にはfakeゼロのD∞を追加） |

2進では、既存の整数基底 ω_j=u^j/2^⌊j/3⌋、u=(θ+3)/2、t=u³/2を用いる。O_K/(u)=F₁₆×F₂₅₆で、代表 a=Σa_jω_j の剰余は Σ(a_{3k} mod2)t^k。18代表すべてについて剰余多項式と既存の次数12剰余多項式のgcdが1であり、両成分で単数である。38平方類座標と−1のスカラーを使ったrankも18と再照合する。

奇badでは元の6除数の G(θ)/θ^d を各既存剰余因子に直接代入し、分子・分母のnormが非零であることを再計算した。2843のE4=(4,y)−P₀も f_i(4)f_i(0)≠0 で単数。局所D∞のfake像はゼロなので問題ない。これらが完全局所像を生成することは既存の真正次元との一致から継承する。

それ以外の奇pではC₂は良還元を持ち、fake局所Kummer像は不分岐である。K/Qもpで不分岐であり、Poonen–Schaefer Proposition12.2–12.3から、Q_pスカラーを掛ければ各成分で偶付値、したがって平方を除いて単数になる。**2進に不分岐と単数の同値を適用してはいない。** 2進は上の明示生成元によって処理した。

## 3. 全球の有理スカラーで全有限付値を偶数にする

fake Selmer像の任意の類をα∈K*で代表する。各有理素数pにおいて前節より

\[
 \alpha=u_p\,\beta_p^2\,q_p,
 \qquad u_p\in\prod_{\mathfrak p\mid p}\mathcal O_{K_\mathfrak p}^{*},
 \quad q_p\in\mathbb Q_p^{*}.
\]

従って、すべての𝔭|pで同一のδ_p=v_p(q_p) mod2を使って

\[
 v_\mathfrak p(\alpha)\equiv\delta_p e_\mathfrak p\pmod2.
\]

各有理素数pの上には少なくとも1つ奇数e_𝔭がある。badでは表で確認でき、残りではe=1である。このためαの全付値がゼロのpではδ_p=0とでき、δ_p≠0は有限個に限る。

\[
 q=\prod_p p^{\delta_p}\in\mathbb Q^{*}
\]

と置けば、qαの**全有限素点**での付値が偶数になる。qを掛けても全球fake類は変化しない。個々の素イデアルが主であるという仮定も、S付値基底の構成も不要である。

したがって

\[
 E=\{[\alpha]\in K^*/K^{*2}:v_\mathfrak p(\alpha)\in2\mathbb Z
       \text{ for every finite }\mathfrak p\}
\]

とすると、全fake Selmer像はEの K*/(K*² Q*) への像\bar Eに入る。

S上の21付値を単なるベクトル空間として見ると、有理素数6本のスカラーパターンのrankは6で、残る15次元の付値商がこの条件で消える。ただし、**「31から15を引く」計算はしない。** 通常類群とS類群の差があるため、次節で全域の次元を直接評価する。

## 4. 有限偶付値空間の次元

全有限素点に関する通常の理想平方完全列は

\[
 0\longrightarrow\mathcal O_K^*/\mathcal O_K^{*2}
 \longrightarrow E\longrightarrow\mathrm{Cl}(\mathcal O_K)[2]
 \longrightarrow0.
\]

具体的には(α)=𝔞²を[𝔞]へ送り、逆に2捩れ理想類を取れば𝔞²=(α)から元を持ち上げる。核は単数平方類である。これは2進での不分岐拡大の完全列を主張したものではなく、理想の偶付値の完全列である。

Dirichlet単数rankは19、実埋め込みがあるので根の1の2部分は{±1}。従ってdim E=20+c_K。

q∈Q*がEに入るなら、各pの奇数e_𝔭よりv_p(q)は偶数。ゆえにqは±有理平方である。−1は実埋め込みによりKで平方でないので、Eからfake標的への核はちょうど⟨−1⟩、次元1。

\[
 \boxed{\dim\bar E=19+c_K.}
\]

## 5. 通常類数h_K≤15をGRHなしで認証

通常Hilbert類体H/Kを使う。無限素点を法に含めない通常類群に対応するので、実素点も不分岐であり

\[
 [H:K]=h_K,\quad (r_1(H),r_2(H))=(4h_K,16h_K),
 \quad D_H=D_K^{h_K}.
\]

**通常Hilbert類体でS素点が完全分裂すると仮定しない。** ここでは素点項をすべて捨てる。

### 5.1 試験関数の正値性と積分

\[
 g(z)=\frac{3(\sin z-z\cos z)}{z^3},\quad g(0)=1,
 \qquad f(x)=g(x/\sqrt{27})^2.
\]

p(t)=¾(1−t²)·1_{|t|≤1} は確率密度で、その特性関数がgである。よってg²のFourier変換は非負の密度p*pで、f≥0、f≤1。独立なW,W′の分散はそれぞれ1/5だから

\[
 1-g(z)^2=\mathbb E[1-\cos(z(W+W'))]\le z^2/5.
\]

また∫p²=3/5、Parsevalから∫₀∞g(z)²dz=3π/5なので

\[
 1-f(x)\le x^2/135,\qquad
 E_f=4\int_0^\infty f(x)dx=\frac{12\pi\sqrt{27}}5.
\]

明示公式の減衰条件を確実に満たすため、まずf_η(x)=e^{−ηx²}f(x)、η>0を用いる。Fourier非負性は畳み込みで保たれる。F_η=f_η/cosh(x/2)の変換Φは0≤Re(s)≤1で有界で、境界の実部はf_ηのFourier変換。調和関数の最小原理からReΦ(ρ)≥0となる。零点の実部を1/2とする仮定は不要。

0≤f≤1から1−f_η≤(1/135+η)x²、E_{f_η}≤E_f。各ηで明示公式を適用し、非負な零点項と素点項を捨てた後でη↓0とする。有限supportの類群生成定理を無限support関数へ直接適用しているのではない。

### 5.2 正規化と厳密不等式

用いるWeil明示公式の正規化は

\[
 \log D_L\ge n_L(\gamma+\log4\pi)+r_1(L)
 -n_L I_1-r_1(L)I_2-E_f+P_f,
\]

\[
 I_1=\int_0^\infty\frac{1-f(x)}{\sinh x}dx,
 \quad I_2=\int_0^\infty\frac{1-f(x)}{2\cosh^2(x/2)}dx,
 \quad P_f=4\sum_\mathfrak p\log N\mathfrak p
 \sum_{m\ge1}\frac{f(m\log N\mathfrak p)}{1+(N\mathfrak p)^m}\ge0.
\]

これはBelabas–Diaz y Diaz–Friedman §5の式(20)–(21)およびOdlyzko1990式(2.3)の正規化である。∫x²/sinh x=7ζ(3)/2、∫x²/[2cosh²(x/2)]=π²/3を使うと、L=Hについて

\[
 h_K\Delta_K\le E_f,
\]
\[
 \Delta_K=36(\gamma+\log4\pi)+4-\log D_K
 -\frac1{135}\left(126\zeta(3)+\frac{4\pi^2}3\right).
\]

Machinのπ公式の交代級数、有理数のlogのatanh級数、H₈₁₉₂−log8193<γ、ζ(3)の100項と積分剰余から、整数・Fraction比較のみで

\[
 \Delta_K>2.459565836749>\frac{49}{20},
 \qquad E_f<\frac{196}{5}=39.2.
\]

したがってh_K≥16なら h_KΔ_K>16·49/20=196/5>E_f、矛盾。よって

\[
 \boxed{h_K\le15,\quad c_K\le3.}
\]

通常類群の位数・群構造・c_Kの正確値は未決定。GRH、Odlyzkoの数値表のOCR、S素点の分裂、認証されていない数値積分に依存しない。解析的手法とTartar型関数は古典的であり、旧Section159および訂正済みK21研究と同じ方法の再利用である。

## 6. 既知の6独立制約を全有限偶付値空間へ適用

\bar E上のnormの有限付値はすべて偶数なので、norm平方条件はnormの符号1本で足りる。実根を既存の順序でr₁<r₂<r₃<r₄とし、符号bitをs_iとすると、実局所像はs₁=s₂、s₃=s₄を満たす。norm符号とs₁+s₂の2条件は、既存単数ε、γ₈上で

\[
 \begin{pmatrix}1&0\\1&1\end{pmatrix}
\]

となり独立。従ってnorm・実条件後の全域候補V₀はdim V₀≤17+c_K。

row356の4証人

\[
 w_1=\epsilon\gamma_8\gamma_6,\quad
 w_2=\gamma_8\gamma_{12},\quad w_3=\tau_3,\quad
 w_4=\epsilon\upsilon_3
\]

はすべて全球**単数**であり、全有限付値0、norm=1、実局所条件を満たす。よって今回のV₀にも入る。同じ2進障害の小行列は

\[
 M=\begin{pmatrix}
 1&1&0&0\\1&1&1&1\\0&1&1&0\\0&0&1&0
 \end{pmatrix},\qquad\det M=1.
\]

従ってV₀上の2進障害rank≥4。未知の単数・理想平方類を含む**全域**で

\[
 \dim\operatorname{Sel}_{\rm fake}\le17+c_K-4=13+c_K\le16.
\]

同じ計算を12単数上の結合行列で確認するとnorm・実条件と2進条件のrankは合計6である。2進rank6にさらに2を重複加算してはいない。

row351/352の全球cohomology比較（局所Brauer障害消滅とBr(Q)の局所大域単射を含む）から、真正Selmer→fake像の核は高々1次元。この比較を継承して

\[
 \boxed{\dim\operatorname{Sel}^{(2)}(J_2/\mathbb Q)
 \le13+c_K+1=14+c_K\le17.}
\]

既知MW下界7と合わせ7≤rank≤17。**fake≤16は真正≤16ではない。** 核1次元を消していない。

## 7. 重複判定、検証と監査状態

着手前に現行R0 ACTIVE_REGION、R3担当行と研究経緯339–357、R5のP23/K04、親証明を確認した。追加でR3経緯2–357と重複・障壁索引を照合し、この同じ36次数体に対する全有限偶付値還元と真正≤17への統合は既存登録にないことを確認した。一方、row357主証明155行相当のTable4補助比較と旧検証器の `table4 b14.5 independently forbids h>=16 even without S-prime term` は既出と判定した。通常h_K≤15の数値内容はこの既知補助結果を直接証明へ改善したもので、独立新規上界として二重登録しない。旧K21・次数12の類体/明示公式法そのものにも新規性を付けない。

| 項目 | 状態 |
|---|---|
| 新規性 | 既存局所像・4証人を継承した、新しい対象別の従属大域上界 |
| 通常実行・python -O | 各298検査・8負検査PASS |
| 単数代表 | 2進18代表、奇bad元6除数とE4を実データから再計算 |
| 解析定数 | 全比較は整数・Fraction。浮動小数は表示専用 |
| 親成果 | 元ファイル10件をSHA-256固定。同じ曲線・最大整環・局所像・4証人を継承 |
| 新row358の独立数学監査 | **PENDING / 未実施** |
| row355–357の既存独立監査 | 各既存の限定PASS_SCOPEDを維持 |

検証器は非機械的な数学定理を証明支援系で形式化したものではない。独立監査では、特に「局所単数代表→有理スカラーの全球貼合せ」「通常類群への完全列と−1の商」「Tartar正値性・Gaussian正則化・明示公式の正規化」「row351の真正Selmer比較」を確認してほしい。

## 8. 現在の障壁と唯一の現行NEXT

解消：未知のS付値14方向を1本ずつ構成し、さらに15本の新制約を探す必要は、この上界を得るためにはなくなった。この旧NEXTはrow358を前提とする現行運用では失効させる。S類群の上界取得、有限局所生成、同じ12単数部分群への反復も解消済みのままである。

次の十分条件は、**全域の残余候補 V₀∩kerλ₂ 上にさらに1本の独立制約**を証明すること、または通常類群c_K≤2を認証することである。前者では既知12単数部分群が既に尽きているため、同じ群の言い換えを追加rankと数えない。必要に応じ未構成の単数・理想平方類の代表または同等の全域上側情報を構成する。通常類群全体・全基本単数のindex1計算を自動的な必須条件にはしない。

上界17はg=17と等しく、まだrank<gを示していない。真正≤16または同等の適切なrank証明を得た後に、全MWに対する163進Coleman消滅微分・積分的a₀単元、旧非零source円盤 X=(AC/B²)²∈163²Z₁₆₃\{0}, Y≡1と元signed sourceの矛盾へ進む。

新MW点0、signed±18 source排除0、P23-LOW全域OPEN、Branch B OPEN。LOW全残余の全原始標識付き基底・両有効符号という目標は維持する。R2-01のMID/HIGH、S231正式監査HOLD、B_wide/E1は別範囲。R0正式管理C35-200は変更しない。

## 9. 原典と再演

- Poonen–Schaefer, *Explicit descent for Jacobians of cyclic covers of the projective line*, §§9,11–13、特にProposition12.2–12.3。https://math.mit.edu/~poonen/papers/descent.pdf
- Milne, *Class Field Theory*, V.3 Example3.9（通常Hilbert類体は実素点も不分岐）。https://www.jmilne.org/math/CourseNotes/CFTc.pdf
- Odlyzko, *Bounds for discriminants and related estimates for class numbers, regulators and zeros of zeta functions*, 1990, §2、式(2.3)。https://www.numdam.org/item/JTNB_1990__2_1_119_0.pdf
- Belabas–Diaz y Diaz–Friedman, *Small generators of the ideal class group*, §5、式(18),(20),(21)。本文の有限support生成定理を直接使わず、明示公式と境界正値性を用いる。https://www.math.u-bordeaux.fr/~kbelabas/research/OnBach.pdf

```bash
python3 math/verify_unramified_selmer_bound.py
python3 -O math/verify_unramified_selmer_bound.py
```

主証書：`math/finite_even_selmer_certificate.json`。通常・最適化の再演記録と親ファイルSHAは証拠ZIPに同梱する。既存の主証明・監査資料は変更しない。
