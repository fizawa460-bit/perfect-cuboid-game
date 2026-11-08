# Stage35EX R3-07 row383　元 −30 に必要な零点の三帯と二次拡大のガロア群

2026-11-07 JST。P23 R3-07 LOW。対象は全許容原始標識付き基底上の同じ元 signed \(-30\)。著者厳密再現PASS。row383独立数学監査待ち。

\(K=\mathbb Q(\theta)\) を \(C_{29}\) の次数105の根体とする。**任意の非自明な通常類群二次指標 \(\chi\) について、\(L(s,\chi)\) は次の三領域の和集合に零点を持つ。** 以下の有限小数は厳密値。

| \(\lvert\operatorname{Im}s\rvert\) | \(\operatorname{Re}s\) |
|---|---|
| \(0.26<\lvert\operatorname{Im}s\rvert<0.77\) | \(0.562<\operatorname{Re}s\le1\) |
| \(1.03<\lvert\operatorname{Im}s\rvert<1.46\) | \(0.572<\operatorname{Re}s\le1\) |
| \(1.70<\lvert\operatorname{Im}s\rvert<2.12\) | \(0.605<\operatorname{Re}s\le1\) |

この和集合の面積は \((\operatorname{Re}s,|\operatorname{Im}s|)\) で測るとrow382の長方形の約39%。元 \(-30\) なら \(c_{\rm Cl}=\dim_{\mathbb F_2}\mathrm{Cl}(K)[2]\ge1\) なので、このうち少なくとも一つの零点が必要。全該当指標に対する三領域の無零性から \(c_{\rm Cl}=0\) と元 \(-30\) の排除が従う。

別に、\(K\) の正規閉包 \(L\) はガロア群 \(S_{105}\) を持つ。非自明な通常類群二次指標の類体 \(E/K\) があれば、その正規閉包 \(M/\mathbb Q\) は
\[
 \operatorname{Gal}(M/\mathbb Q)\simeq W(D_{105})
       = V\rtimes S_{105},
 \qquad V=\ker(\mathbb F_2^{105}\xrightarrow{\ \sum\ }\mathbb F_2).
\]
一般に独立な \(r\) 指標の類体を合成したものの正規閉包は \(V^r\rtimes S_{105}\) を持つ。これらはGRHを使わない必要条件。

## 1. 試験関数

次数・署名 \((105,7,49)\)、最大整環と絶対判別式 \(\Delta\) は親row373–375。二つの2上の主素イデアルと4,140本の監査済み主イデアル関係から得る2,492個の奇素イデアル類の零性はrow381–382。全非自明通常類群二次指標に対して、この2,492個と2上では \(\chi(\mathfrak p)=1\)。指定分裂が類群を生成するとの仮定は置かない。

\[
 B_\ell(x)=\ell^{-1}\mathbf 1_{[-\ell/2,\ell/2]}(x),\qquad
 g=B_{229/25}*B_{397/200}^{*2}*B_{56/125}^{*3},
 \qquad R=g*g,\qquad F_0=R/R(0).
\]
\(F_0\) は \(F_0(0)=1\)、\(0\le F_0\le1\) の偶関数で、支持半幅は \(T=7237/500\)。長さの多重集合を \(\mathcal L\) とする。\(x\ge0\) で
\[
 F_0(x)=S^{-1}\sum_{a>0}c_a(a-x)_+^{11},\quad
 S=\sum_{a>0}c_a a^{11},\quad
 R(0)=S/(11!\prod_{\ell\in\mathcal L}\ell^2).
\]
節点は \(a=T-\sum_{\ell}j_\ell\ell\)、係数は \(\prod_\ell(-1)^{j_\ell}\binom2{j_\ell}\) の同じ節点上の和。\(j_\ell\in\{0,1,2\}\) は各出現を別々に走る。一様密度12本の畳み込みを区間の両端で展開した式である。

試験関数は
\[
 F(x)=F_0(x)P(x),\qquad P(x)=\sum_j\lambda_j\cos(v_jx).
\]
\(v_0=0\)、他の \(v_j>0\)。全20組の有理数は `fixture383.json` に固定した。証書は \(\sum_j\lambda_j=1\)、\(\lambda_0>\sum_{j>0}|\lambda_j|\) を厳密に確認する。従って \(F(0)=1\)、\(F\ge0\)。係数は数値探索で選んだ。以下の判定に探索時の丸めや格子点の符号は使わない。

\(z=s-1/2\) として、両側Laplace変換を
\[
 \phi_0(z)=R(0)^{-1}
       \prod_{\ell\in\mathcal L}\left(\frac{\sinh(\ell z/2)}{\ell z/2}\right)^2,\qquad
 \phi(z)=\sum_j\frac{\lambda_j}{2}
       \bigl(\phi_0(z+iv_j)+\phi_0(z-iv_j)\bigr)
\]
と書く。商の原点では連続値1を取る。

## 2. 零点和の上界

通常類群の非自明二次指標に対するPoitouの明示公式を適用する。行382と同じ正規化では
\[
\begin{aligned}
 \sum_\rho\phi(\rho-1/2)&=-105\,\mathcal B_\chi(F),\\
 \mathcal B_\chi(F)&=\gamma+\log(8\pi)+\pi/30-\log(\Delta)/105-I(F)\\
 &\quad+\frac2{105}\sum_{\mathfrak p}\sum_{m\ge1}
    \log q\,q^{-m/2}F(m\log q)\chi(\mathfrak p)^m,\qquad q=N\mathfrak p,\\
 I(F)&=\int_0^\infty (1-F(x))\left(\frac1{2\sinh(x/2)}+
                              \frac1{30\cosh(x/2)}\right)\,dx .
\end{aligned}
\]
零点は重複度込み。\(F\) のコンパクト支持と滑らかさで式の仮定を満たす。偶数 \(m\) と既知分裂の符号は \(+1\)。残りの奇数 \(m\) は \(-1\) を下界とする。\(p>5003\) では \(2\log p>T\)。\(e^T<1{,}982{,}760\) までの一次因子だけを扱えばよい。row379の尾部を再計数し、147,058有理素数の一次因子147,527個が全件一致した。小素数ではrow378の因子順を法 \(p\) の因数分解で照合する。

無限素点の積分は \(\lambda=k+1/2\) での指数級数を使う。\(w=\lambda-iv_j\) とし、
\[
 J_0(w)=\int_0^\infty(1-F_0(x))e^{-wx}\,dx
       =\frac{11}{wS}\sum_a c_a I_{10}(a,w),\quad
 I_d(a,w)=\int_0^a(a-x)^d e^{-wx}\,dx .
\]
\(I_0=(1-e^{-wa})/w\)、\(I_d=(a^d-dI_{d-1})/w\) なので、\(I_{10}\) は \(w^{-1}\) の多項式と指数項の和で計算できる。変調後の項は
\[
 J(\lambda)=\sum_j\lambda_j
       \left[\frac1\lambda-\operatorname{Re}\bigl(w^{-1}-J_0(w)\bigr)\right].
\]
係数 \((1+(-1)^k/15)\) で1,024項足す。\(D_0=-F_0''(0)\) とすると自己相関のCauchy–Schwarzにより \(1-F_0(x)\le D_0 x^2/2\)。\(D'=D_0+\sum_j|\lambda_j|v_j^2\) とおけば \(1-F(x)\le D' x^2/2\)。尾は \((16/15)D'/[2(1024-1/2)^2]\) 以下。Arb 192-bit外向き区間計算は
\[
 \mathcal B_\chi(F)>49/5000,\qquad
 \sum_\rho\operatorname{Re}\phi(\rho-1/2)<-1.029
\]
を一様に証明する。用いた下界の式は \(0.00988588984309\ldots\)。

## 3. Hadamard零点重みを \(\sigma=7/5\) で評価

row382と同じ中心対称Hadamard積を実数 \(\sigma>1\) で対数微分する。
\[
\begin{aligned}
 M_\chi(\sigma)&=\sum_\rho\frac{\sigma-\operatorname{Re}\rho}{|\sigma-\rho|^2}\\
 &=\tfrac12\log\Delta+
   \tfrac72\bigl(\psi(\sigma/2)-\log\pi\bigr)+
   49\bigl(\psi(\sigma)-\log(2\pi)\bigr)+L'/L(\sigma,\chi).
\end{aligned}
\]
ここで \(\psi=\Gamma'/\Gamma\)。中心を移した位数1の完成関数の積では、反射対の標準因子の積が偶。関数等式から指数因子の一次項が消える。各零点の実重みの和は絶対収束する。

\(\chi=1\) が分かる素イデアルのEuler項を \(-\log q/(q^\sigma-1)\) で評価し、他では \(\log q/(q^\sigma+1)\) を上界とした。小素数の全成分と尾部の一次成分を計算する。残りは二つに分ける。

- \(p>B=5003\) の次数2以上は、剰余次数の和が105以下なので \(\sum_{p>B}105\log p/(p^{2\sigma}-1)\) 以下。分母を \((1-B^{-2\sigma})p^{2\sigma}\) で下から抑え、減少関数 \((\log x)x^{-2\sigma}\) の積分を使う。
- \(p>X=1{,}982{,}760\) の次数1では、\(\vartheta(x)=\sum_{p\le x}\log p\le(\log4)x\)。これは奇数 \(2m+1\) に対し \(\prod_{m+1<p\le2m+1}p\mid\binom{2m+1}{m}\le 2^{2m}\) を使った帰納法で得る。偶数 \(2m>2\) は合成数。部分和公式から上界は \(105(\log4)\sigma X^{1-\sigma}/[(\sigma-1)(1-X^{-\sigma})]\)。

Arbで \(M_\chi(7/5)<100\) を得た。上界の式は \(99.186384435239\ldots\)。

## 4. 三帯の外側を区間演算

\(u=|\operatorname{Re}\rho-1/2|\)、\(t=|\operatorname{Im}\rho|\)、\(a=\sigma-1/2\) と置く。関数等式で反射対の重みを平均する。
\[
 W(u,t)=\frac12\left(\frac{a-u}{(a-u)^2+t^2}
                      +\frac{a+u}{(a+u)^2+t^2}\right)
         \ \ge\ \frac{a}{\sigma^2+t^2}.
\]
\(\sum_\rho W=M_\chi(\sigma)\)。\(\operatorname{Re}\phi(\rho-1/2)=\operatorname{Re}\phi(u+it)\)。次に \(\varepsilon=1/100\) と置く。

- \(0\le t\le1/10\) は \(tT<\pi/2\) なので、\(F\ge0\) と \(\cos(tx)\ge0\) から \(\operatorname{Re}\phi\ge0\)。
- \(t\ge8>\max v_j\) では \(|\sinh(\ell(u+it)/2)|\le\cosh(\ell/4)\)。これを各変調項に使い、\(C_0=R(0)^{-1}\prod_\ell(2\cosh(\ell/4)/\ell)^2\) とすると
\[
 |\phi(u+it)|/W(u,t)
 \ \le\ C_0(\sigma^2+t^2)a^{-1}\sum_j|\lambda_j|(t-v_j)^{-12}.
\]
各項は \(t\ge8\) で減少し、\(t=8\) での上界をArbで \(0.007825\) 未満と確かめた。
- 中間は表の7閉矩形を二分し、全464小矩形で \(\operatorname{Re}\phi(u+it)+\varepsilon W(u,t)>0\) を認証した。

| \(t\) | \(u\) | 小矩形 |
|---|---|---:|
| \([0.1,0.26]\) | \([0,0.5]\) | 10 |
| \([0.77,1.03]\) | \([0,0.5]\) | 24 |
| \([1.46,1.70]\) | \([0,0.5]\) | 23 |
| \([2.12,8]\) | \([0,0.5]\) | 363 |
| \([0.26,0.77]\) | \([0,0.062]\) | 17 |
| \([1.03,1.46]\) | \([0,0.072]\) | 14 |
| \([1.70,2.12]\) | \([0,0.105]\) | 13 |

小矩形の中心を \(z_0=u_0+it_0\)、半径を \(r=\sqrt{(\delta u)^2+(\delta t)^2}<1/10\) とする。中心での次数7までの複素Taylor係数 \(b_k\) を計算する。定数項の実部から \(|\operatorname{Re}b_1|\delta u+|\operatorname{Im}b_1|\delta t+\sum_{k=2}^7|b_k|r^k\) を引く。Cauchyの評価に用いる半径は \(1/2\)。この円上で \(|\phi|\le (\sum_j|\lambda_j|)\phi_0(u_0+1/2)\) は \(F_0\ge0\) とその偶性から従う。よって残りの上界はこの値に \((2r)^8/(1-2r)\) を掛けたもの。\(W\) は同じ小矩形を包含するArb区間上で直接評価する。

三帯の外に全零点があれば \(\sum_\rho\operatorname{Re}\phi(\rho-1/2)\ge-\varepsilon M_\chi>-1\)。§2と矛盾。必要なら関数等式で零点を実部 \(>1/2\) 側に移すと冒頭の主張になる。

## 5. すべての通常類群二次拡大の正規閉包

`verify_galois383.py` は \(F_{29}\) の整数判別式 \(-2^{7210}\Delta\) と、次の法 \(p\) の因数分解を検算する。既約性は有限体のべき乗とGCDでも検査する。

| \(p\) | 因子次数 |
|---|---|
| \(3\) | \(6,33,66\) |
| \(31\) | \(4,5,48,48\) |
| \(43\) | \(2,2,9,10,11,71\) |
| \(199\) | \(1\)（重複度2）、\(27,76\) |

3と31の可能な部分和の共通部分は \(\{0,105\}\) なので既約。43のFrobeniusの990乗は71-cycle。次数105の非自明なブロック分割ではブロック数とサイズはともに35以下。71-cycleはそのどちらにも作用できないので群は原始。199の判別式付値は1で、次数1の素イデアル一つだけが分岐指数2。他は非分岐。惰性群から互換が入る。互換の共役が作る辺グラフの連結成分はブロック分割であり、原始性と辺の存在からグラフは連結。その辺互換で \(S_{105}\) が生成される。

\(E/K\) を通常類群の非自明二次指標の類体とする。もし \(E\subseteq L\) なら \(S_{104}=\operatorname{Gal}(L/K)\) の唯一の指数2部分群 \(A_{104}\) から
\(E=K(\sqrt{\operatorname{disc}K})\)。
ところが199上の非分岐成分ではこの判別式の付値は1。平方根を加えれば分岐し、通常類体に反する。従って \(E\cap L=K\)。

\(E=K(\sqrt b)\) と書く。有限素点で非分岐なので \(b\) の付値は偶、実素点で分裂するので \(b\) は全正。従って \(N_{K/\mathbb Q}(b)\) は正の有理平方。共役する105個の平方根の積は有理数となるので、正規閉包は \(V\rtimes S_{105}\) に入る。\(L\) 上の核は非零の \(S_{105}\)-安定部分空間。非零の偶パリティベクトルは105が奇数なので全1ではない。これと適当な互換で移したものの和は二座標の1ベクトル。その共役が \(V\) を張るので核は \(V\)。商は \(S_{105}\) であり、全群が \(V\rtimes S_{105}\) になる。

独立 \(r\) 指標では同様に \(V^r\rtimes S_{105}\) に入る。核の各元を105行の \(\mathbb F_2^r\) の列として、同一元内の二行の差が張る空間を \(D\subseteq\mathbb F_2^r\) と置く。互換との差とその共役により、核は任意の二行に \(d\in D\) を置く行列を含む。各列和0と次数105の奇数性により各行は他行との差の和なので \(D\) に属する。従って核は \(V\otimes D\)。もし \(D\) が真部分空間なら \(D\) を消す非零線形形式を取り、その係数で二次指標を積にする。この指標は独立性から非自明で、対応する平方根の積は \(L\) 上の核に固定される。対応する二次拡大が \(L\) に含まれて矛盾。よって \(D=\mathbb F_2^r\)。

さらに \([E:\mathbb Q]=210\)、\(|\operatorname{disc}E|=\Delta^2\)、署名 \((14,98)\)。\(\chi\) の誘導Artin表現は上の自然な符号付き105次元表現である。対角群 \(V\) の各座標指標が相異なり、\(S_{105}\) が座標を推移的に置換するので、複素表現として既約。したがって対象の誘導Artin表現の次数は105のままである。

## 6. 元sourceへの接続と残る課題

row382の独立監査で、row370の同一sourceの31進ジェットと八有理類の31進対数に基づく \(\operatorname{rank}J_{29}(\mathbb Q)\ge10\) の連結が支持された。row381の無条件上界 \(\dim\operatorname{Sel}^{(2)}\le9+c_{\rm Cl}\) により元 \(-30\) は \(c_{\rm Cl}\ge1\) を必要とする。これに§4と§5を適用する。

新規差分は三帯の厳密な必要零点領域、実部の帯別下限、通常類群二次拡大の正規閉包の構造。row382の31進計算は監査済みの入力。三帯の無零性と非自明指標の全尽的な記述が残る。通常類群の2階数0や同じ \(J_{29}\) のMW階数上界9の直接証明も十分条件。新規無条件排除0件。LOWの無条件残9絶対指数・16 signed枠。三帯の無零性の下では元 \(-30\) を排除し、元 \(+30\) の既存排除と合わせLOW残8絶対指数・15 signed枠。

- [Poitou明示公式の参照元 Belabas–Diaz y Diaz–Friedman、式(3)–(4)](https://doi.org/10.1090/S0025-5718-07-02003-0)
- [row382独立数学監査](https://docs.google.com/document/d/1gJ1KbYSF_AOaTu-d4nQYu_sIQoxU6rhfBpXKizDgEWU/edit)
- [row381独立数学監査](https://docs.google.com/document/d/1siQsZfW85ir4uLvAV9_uy7DVELHT1rrPXcyN5sbNUeE/edit)
- [row379の独立監査と尾部の因子表](https://docs.google.com/document/d/1TUdiWNrwp_NRtPlyPLzyUG7mOGyiXLEnnnyH8CSMCjE/edit)
- [row374の最大整環と判別式](https://drive.google.com/file/d/1UgkHK8KV9uqdNvDw7ABtR7Y4FjsBZxYA/view)
