# Stage35EX R3-07：S類群の無条件上界 h_S≤13、c_S≤3

2026-11-04 JST。固定signed ±18の同じC₂:Y²=h₂(X)、種数17、係数体K=Q(θ)・次数36。P23-LOWの一部分だけを対象とする。

**新しい限定成果：**

\[
h_S:=|\mathrm{Cl}(\mathcal O_{K,S})|\le13,
\qquad c_S:=\dim_{\mathbf F_2}\mathrm{Cl}(\mathcal O_{K,S})[2]\le3.
\]

監査済みrow356の \(\dim\mathrm{Sel}^{(2)}(J_2/\mathbf Q)\le28+c_S\) と合わせ、

\[
\boxed{\dim\mathrm{Sel}^{(2)}(J_2/\mathbf Q)\le31},
\qquad 7\le\operatorname{rank}J_2(\mathbf Q)\le31.
\]

これは未知だったc_Sに数値上界を与える。c_Sの正確な値、S類群の全不変因子、完全な全球平方類基底を計算したものではない。既存の記号的上界28+c_Sも保持する。目標の16以下、全MWの163進消滅微分、元source排除は未達。新しいQ有理MW点0、元source排除0、P23-LOW・Branch BはOPEN。

今回の新上界は**内部厳密証明・有理数検算PASS／独立数学監査PENDING**。受領したrow356のPASS_SCOPEDは、旧4制約と28+c_Sだけに適用する。

## 1. 着手前の照合と新規性

R0唯一ACTIVE、R3担当行8・経緯339–356、R5のP23/K04、row344の最大整環・判別式・署名、row346/348のS素点、row356証明と独立監査を確認した。既知12単数の局所交差は既に完了し、追加cutを生まないので反復しない。

方法そのものは新規ではない。旧Section159の次数12体、R3-C187の次数21体にもPoitou–Odlyzko法が使われている。次数21体については、局所補正の分母を訂正した現行カードまで照合した。今回の差分は、**同じ次数36体・署名(4,16)・実際のS分解に対する新しい数値上界**。他の体のS類群ゼロをこの体へ移さない。

通常類群の完全関係行列や指数1単数群を先に完成する代わりに、S類群に対応する類体の判別式を用いて、ここで必要な上界だけを証明する。有限素数探索の打切りや推測類数を上界として使わない。

## 2. 入力とS類体

旧row344の認証入力は

\[
[K:\mathbf Q]=36,\quad(r_1,r_2)=(4,16),
\]
\[
D_K=2^{24}\cdot2843\cdot13963\cdot329475607
\cdot1034386920659\cdot23910039195629
=5427028083166736357520103768895827763994388594688.
\]

Sは2と上記五奇bad有理素数上の全21素イデアル。2上はe=3、剰余次数4と8の二素点なので、Sには**絶対ノルム16の素イデアル**が一つ含まれる。根判別式の参考値は約22.58072だが、この小数は判定には使用しない。

H_S/Kを通常のS-Hilbert類体とする。通常類群の商

\[
\mathrm{Cl}(\mathcal O_{K,S})
\simeq \mathrm{Cl}(\mathcal O_K)/\langle[\mathfrak p]:\mathfrak p\in S\rangle
\]

に対応する有限アーベル拡大なので、h=h_S=[H_S:K]について、有限素点・実素点で不分岐、Sの全素点は完全分解する。従って

\[
[H_S:\mathbf Q]=36h,\quad(r_1(H_S),r_2(H_S))=(4h,16h),
\quad D_{H_S}=D_K^h.
\]

特にH_Sには絶対ノルム16の素イデアルがh個ある。これは実際のS分解と類体の定義から従う。一般の不分岐拡大でSが完全分解すると仮定しているわけではない。無限素点での不分岐を保つ通常類体を用い、署名を変更しない。

## 3. GRHなしの明示公式

a=1/128として

\[
f(x)=e^{-ax^2},\qquad F(x)=\frac{f(x)}{\cosh(x/2)},\qquad
\Phi(s)=2\int_0^\infty F(x)\cosh((s-1/2)x)\,dx
\]

を選ぶ。Fとその導関数は十分速く減衰し、Weilの明示公式の条件を満たす。ここで使用するのは明示公式の恒等式であり、有限台を仮定した類群生成アルゴリズムの定理をGaussianへ無条件に転用するものではない。

境界Re(s)=0,1では

\[
\operatorname{Re}\Phi(1+it)=\operatorname{Re}\Phi(it)
=2\int_0^\infty e^{-ax^2}\cos(tx)\,dx
=\sqrt{\pi/a}\,e^{-t^2/(4a)}\ge0.
\]

Re Φは閉帯内で有界な調和関数で、虚部が無限大へ向かうと一様に0へ近づく。長方形での最小値原理を極限へ適用すると、帯0≤Re(s)≤1の全体でRe Φ≥0。従ってDedekindゼータの非自明零点の寄与は非負であり、零点を臨界線上へ置くGRHは不要。

次数n・実埋込み数rの任意の数体Lに対して、無条件明示公式の零点寄与を落とすと

\[
\log D_L\ge n(\gamma+\log(4\pi))+r
-n I_1-r I_2-E+P_L,
\]
\[
I_1=\int_0^\infty\frac{1-f(x)}{\sinh x}\,dx,
\quad I_2=\int_0^\infty\frac{1-f(x)}{2\cosh^2(x/2)}\,dx,
\quad E=4\int_0^\infty f(x)\,dx=2\sqrt{\pi/a},
\]
\[
P_L=4\sum_{\mathfrak P}\log N\mathfrak P
\sum_{m\ge1}\frac{f(m\log N\mathfrak P)}{1+(N\mathfrak P)^m}.
\]

正規化した局所補正は上式の分母1+(N𝔓)^mを使う。これは旧C187の修正版と同じ正規化であり、原著の明示公式とも照合した。

## 4. 積分・素点項を有理不等式へ落とす

1−e^{-ax²}≤ax²と

\[
\int_0^\infty\frac{x^2}{\sinh x}\,dx=\frac72\zeta(3),
\qquad
\int_0^\infty\frac{x^2}{2\cosh^2(x/2)}\,dx=\frac{\pi^2}{3}
\]

から、I₁≤7aζ(3)/2、I₂≤aπ²/3。前者は1/sinh xの正項指数級数、後者は部分積分後の交代指数級数から得られる厳密なモーメントである。

H_Sのノルム16素点h個とm=1の項だけを残し、ほかの非負項をすべて落とす。ℓ=log16について

\[
P_{H_S}\ge h\frac{4\ell}{17}e^{-a\ell^2}
\ge h\frac{4\ell}{17}(1-a\ell^2).
\]

最後の括弧は正である。明示公式にn=36h、r=4h、log D_H=h log D_Kを代入すると

\[
h\Delta\le E,
\]
\[
\Delta=36(\gamma+\log(4\pi))+4-\log D_K
-a\left(126\zeta(3)+\frac{4\pi^2}{3}\right)
+\frac{4\ell}{17}(1-a\ell^2).
\]

## 5. 正確な定数証明書と結論

添付の標準Python検証器は、外部の小数定数を仮定せず、Fractionによって次を構成する。

- π：Machin公式16 arctan(1/5)−4 arctan(1/239)と各36項の交代級数誤差。
- log x：2冪で1≤y≤2へ正規化し、z=(y−1)/(y+1)のatanh級数48項と正の幾何級数tail上界。
- γ：N=8192の調和和からH_N−log(N+1)<γ<H_N−log N。
- ζ(3)：N=100の和と、残余の積分上下界。

評価の方向をすべて安全側へ丸めて

\[
\Delta>\frac{3006074464919}{10^{12}}>3,
\qquad E=2\sqrt{128\pi}<41
\]

を得る。後者は512π<41²という有理不等式で確認でき、数値平方根は不要。従ってh≥14なら

\[
h\Delta>14\cdot3=42>41>E
\]

と矛盾する。よって**h_S≤13**。有限アーベル群の2捩れ部分の位数2^{c_S}はh_Sを割るので、2^{c_S}≤13<16、すなわち**c_S≤3**。

独立な比較として、著者サイトのOdlyzko無条件Table4・b=14.5の行でも、次数16の不分岐類体は排除される。しかし、同サイトにOCR誤記の留保があるため、**上の主証明は表の数値に依存しない**。Gaussian・明示公式・有理評価が主証明である。

この結果から、S類群の2-primary部分の候補型は

\[
0,\ C_2,\ C_4,\ C_2^2,\ C_8,\ C_4\times C_2,\ C_2^3
\]

のいずれかに限定される。ただし、どの型かは未確定であり、通常類群全体の値も計算していない。S類群=0、c_S=0又は類数1と読み替えない。

## 6. Selmer目標への接続と残る未知方向

受領済みrow356の独立監査は、28+c_Sの上界をPASS_SCOPEDと確認した。これに今回のc_S≤3を代入して、true Selmer≤31、fake像≤30を得る。旧28+c_Sを破棄して31へ弱めるのではなく、**記号的上界と無条件の数値評価を両方保持する**。

旧全fake空間W_Sは34+c_S次元なので37以下。既知S単数群のfake像は13方向であり、残る商の次元は最大24。内訳の安全な予算は、未構成の通常単数7方向・S付値14方向・S類群由来最大3方向である。これは未知方向の**次元予算**であり、実際の平方類代表や局所行列を構成したという意味ではない。

既知単数側の核6方向は旧六有理除数のfake像で尽きる。今後は未知の方向を被覆する平方類代表・上側情報を認証し、その共通局所写像の独立rankを得る。最悪c_S=3として、今回までの4方向に加えてさらに15方向の独立制約、又は同等に強い別の全域上界がtrue Selmer≤16の十分条件。c_Sをさらに小さくできれば必要な追加rankも減るが、通常類群の全不変因子・指数1単数の完成を一律必須には戻さない。

数値31は種数17に対するordinary Chabautyの入口を満たさない。全MWへの163進消滅微分・a₀単元、旧source円盤X∈163²Z₁₆₃\{0},Y≡1との非交差は引き続き別の未証明事項。元signed ±18は排除されておらず、LOW残余削減0。

## 7. 前報のπ表記の追補

前報row356§5の既知S単数群の説明では、π₀=u−2と、旧row348のπを区別する必要があった。正しくは

\[
\alpha=u-1,\quad \pi_{348}=\frac{u-2}{u-1}=\frac{\pi_0}{\alpha},
\quad\pi_0^3=2\epsilon,
\quad\pi_{348}^3=2\epsilon/\alpha^3.
\]

従ってfake商で[π₃₄₈]=[εα]。αは既知単数群にあるため、「既知S単数群から新たな許容方向が増えない」という結論は変わらない。row356の4証人・det1・28+c_Sの証明もこのπの略記に依存しない。旧主証明のSHAは凍結したまま、この追補で表記を訂正する。今回のGaussian類群上界はπを使用しない。

## 8. 検算・監査状態・台帳更新

標準Pythonのみ、外部CASやNumPyは不要。

```bash
cd math
python3 verify_gaussian_sclass_bound.py
python3 -O verify_gaussian_sclass_bound.py
```

通常・最適化とも35検査・4負検査が一致。すべての不等式判定は整数・有理数で行い、表示用の小数は証明に使わない。一般の明示公式、Gaussianの零点寄与非負性、類体対応は本文の数学的依存であり、プログラムがこれらの解析・類体論を形式証明するという主張ではない。新成果の独立数学監査は未実施。

登録先：既存R3経緯356行の監査状態をPASS_SCOPEDへ同期し、今回のh_S≤13・c_S≤3・true≤31を経緯357行へ限定新成果として登録する。R3担当行C8:G8、R0唯一ACTIVE、R5のK04/P23には「c_S正確値UNKNOWN／上界3取得／新上界は独立監査PENDING」を区別して反映する。旧主証明と親証書は変更しない。

保存後の再読検証：R3の19セル、R5の4セル、R0 ACTIVEの5段落が予定内容と一致。研究経緯339–355と隣接セルの保持、既存書式・validation、新規行の正しい原文リンク、R0の対象外1559要素の保持を確認した。現行NEXTは一つ。Google画面の描画検証は行わずAPI書式メタデータで確認し、列幅・行高・レイアウトは変更していない。

現行NEXTのうち「c_Sの何らかの認証上界を得る」は今回解消。次は未知全球方向の構成・被覆と追加制約rank。局所生成や既知12単数の再計算を復活させない。P23-LOW全残余・全原始標識付き基底・両有効符号がR3の最終目標。R2のMID/HIGH、S231 formal HOLD、B_wide/E1、R0 formal C35-200の境界は維持する。

## 9. 根拠

- [Odlyzko, 1990 survey](https://www.numdam.org/item/JTNB_1990__2_1_119_0.pdf)：§2、Eq.(2.3)、Gaussianを含む減衰する試験関数と無条件positivity。表の単なる参照ではなく明示公式を適用した。
- [Belabas–Diaz y Diaz–Friedman, Small generators of the ideal class group, 著者版](https://www.math.u-bordeaux.fr/~kbelabas/research/OnBach.pdf)：§5、Eq.(18),(20),(21)。無条件の正規化と帯の最小値原理。今回使うのは恒等式とpositivityで、GRHを仮定した生成限界ではない。
- [Milne, Class Field Theory v4.03](https://www.jmilne.org/math/CourseNotes/CFTc.pdf)：V.3 Example3.9、Exercise3.15。通常Hilbert類体とS完全分解の商対応。
- [Odlyzko表の説明](https://www-users.cse.umn.edu/~odlyzko/unpublished/discr.bound.tables.txt)、[無条件Table4](https://www-users.cse.umn.edu/~odlyzko/unpublished/discr.bound.table4)、[OCR留保](https://www-users.cse.umn.edu/~odlyzko/comments/discr.bound.tables.cmnts)。表は比較検算のみ。
- [旧Section159・次数12体](https://docs.google.com/document/d/1T_LoLWLWowI0SwuN43wlgfD1hH5f_VStpdHaYG9dDxk/edit)、[旧C187・次数21体の修正版](https://docs.google.com/document/d/1qdI3dH8beHeqWgcmq83zMjZiDVFHBRhlf6BDkqR8vMU/edit)。既存手法として照合し再credit0。両体の数値結果をKへ転用しない。
- [row356独立監査](https://drive.google.com/file/d/1jLJa5Z8XXnA4-7n0NJ9eKBZ2YXvNB2Kn/view)、[監査証拠](https://drive.google.com/file/d/1SmLkBzGufPtmPvOfriILLX1OjndHajXv/view)。対象の旧証明SHAはf46e31bbdad9625bba7a9138f7674c37c9e2d26092301d475c1062f5401b61a0。
- [R3正本](https://docs.google.com/spreadsheets/d/17BQc6iakGQ7tdxMAVORnOPGa6KjH0uiaiAbbVMO2kRs/edit)、[R0正本](https://docs.google.com/document/d/1UKVlpL0CmAEAIpRN_eE63JllyN1RjqbBaGIG2o4UH4Q/edit)、[R5統合](https://docs.google.com/spreadsheets/d/1SLRGqevuQs8RSkhOWhHO67vcpcmC0F304E9ClYB89ag/edit)。

新規性判定：既存の無条件解析・類体論の、同一36次数体に対する新しい限定上界。新しい一般的方法、完全類群計算、数値上界16以下、source排除の主張はしない。
