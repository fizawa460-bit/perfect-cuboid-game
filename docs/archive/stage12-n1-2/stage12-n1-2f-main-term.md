# Stage12-N1-2f：体積・局所密度主項、対数次数、repeated-side寄与

## 判定

Stage12-N1-2e の三法展開から、固定法ごとの体積・局所密度係数、形式的な対数次数、repeated-side寄与を確定した。

確定した構造は次の通りである。

- 固定法 \((a,b,c)\) の主項係数は明示できる
- 三法和のEuler積は \(s=1\) で3位の極を持つ
- raw oriented count の形式的主項は \(B(\log B)^4\)
- global Möbius反転後のprimitive oriented count は形式的に \(B(\log B)^3\)
- repeated-side contribution は全高さで恒等的に0

ただし、固定法格子点数の一様誤差が未証明なので、以下は**主項構造の確定**であり、漸近式そのものの証明ではない。

## 1. 固定法の体積と局所密度

Stage12-N1-2e の厳密展開では

\[
G(hrs)=
\sum_{\substack{a\mid h,\ b\mid r,\ c\mid s\\
(a,b)=(a,c)=(b,c)=1}}
\lambda_1(a)\lambda_1(b)\lambda_1(c)
\]

であり、\(a,b,c\) はすべて \(1\pmod4\) 素数だけに支えられるため奇数である。

固定した \((a,b,c)\) に対し

\[
h=au,\qquad r=bv,\qquad s=cw
\]

と置く。奇素数 \(p\) におけるcoprime密度は次の通り。

- \(p\nmid bc\)：\(1-p^{-2}\)
- \(p^e\Vert b\)：\(p^{-e}(1-p^{-1})\)
- \(p^e\Vert c\)：\(p^{-e}(1-p^{-1})\)

従って、基準となるprimitive密度に対する追加因子は

\[
\rho(bc)=\prod_{p\mid bc}\frac{p}{p+1}
\]

となる。

2進条件は、\((r,s)\) がともに奇数の場合のh長さ2倍と、異なる偶奇の場合のh偶数制限がちょうど釣り合う。

- odd–odd：剰余質量 \(1/4\)、h長さ因子2、寄与 \(1/2\)
- opposite parity：剰余質量 \(1/2\)、h長さ因子1、寄与 \(1/2\)

合計2進局所因子は1である。

領域 \(0<r<s\) の角度は \(\pi/4\)。\((r^2+s^2)^{-1}\) の動径積分は \((1/2)\log B\) を与えるため、固定法の形式的主項は

\[
V_{a,b,c}(B)=
\frac{B}{\pi abc}\rho(bc)
\left[\log\frac{B}{a\max(b,c)^2}\right]_+
+\text{lower-log terms}.
\]

\(a=b=c=1\) では

\[
V_{1,1,1}(B)\sim \frac1\pi B\log B
\]

となる。有限監査でも、unweighted parameter points を \(B\log B/\pi\) で割った比は、\(B=1,000\) の0.801から \(B=200,000\) の0.888へ増加している。

## 2. 三法Euler積と対数次数

\(q\equiv1\pmod4\) に対する局所因子は

\[
F_q(s)=
1+\frac{2}{q^s-1}
+\frac{4q}{(q+1)(q^s-1)}.
\]

第一項以外は、それぞれ

- \(q\)-冪をh法 \(a\) へ割り当てる寄与
- \(q\)-冪をr法 \(b\) またはs法 \(c\) へ割り当て、\(\rho(q)=q/(q+1)\) を含めた寄与

である。

Euler積は

\[
\prod_{q\equiv1(4)}F_q(s)
=\zeta(s)^3L(s,\chi_4)^3H(s)
\]

と分解でき、\(H\) は \(s=1\) で正則かつ非零。従って三法和は3位の極を持つ。

その正規化定数を

\[
\kappa=
\left(\frac\pi4\right)^3
\left(1-\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3
\prod_{q\equiv1(4)}F_q(1)(1-q^{-1})^6
\]

と置く。

対数変数

\[
x=\log a,\qquad y=\log b,\qquad z=\log c,\qquad L=\log B
\]

を用いると、幾何的な残り対数は

\[
L-x-2\max(y,z)
\]

であり、

\[
\int_{x+2\max(y,z)<L}
\bigl(L-x-2\max(y,z)\bigr)\,dx\,dy\,dz
=\frac{L^4}{48}.
\]

従って形式的raw主項は

\[
C_{\rm raw}(B)
\sim
\frac{\kappa}{48\pi}B(\log B)^4.
\]

素数 \(p\le200,000\) の部分積では

\[
\kappa\approx0.01855917,
\qquad
\frac{\kappa}{48\pi}\approx1.23074\times10^{-4}.
\]

この数値は厳密な誤差区間ではなく、Euler積の有限部分積診断である。

## 3. global Möbius反転後の次数

既に確定した恒等式

\[
C_{\rm prim}(B)
=
\sum_{k\le B}\mu(k)
C_{\rm distinct\_raw}(\lfloor B/k\rfloor)
\]

は、Dirichlet/Mellin側で \(\zeta(s)\) を1因子除く操作に対応する。

raw側の総極次数5はprimitive側で4へ下がるため、形式的には

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3.
\]

したがって、rawの対数次数は4、primitive oriented countの対数次数は3である。

この次数低下は、Stage12-N1-2eで問題になった「Möbius反転後に誤差がどう残るか」を判断する基準になる。ただし、主項多項式と格子点誤差を一様に制御する証明はまだ必要である。

## 4. repeated-side寄与は恒等的に0

第一Pythagorean triangleの二脚が等しいことはない。従って重複し得るのは、第二triangleの脚 \(c\) が第一triangleのどちらかの脚 \(z\) と等しい場合だけである。

この場合

\[
z^2+w^2=p^2,
\qquad
z^2+p^2=d^2.
\]

第二式のtriangle \((z,p,d)\) では \(p\) が大きい脚であり、その \(p\) はtriangle \((z,w,p)\) の斜辺、さらに小さい脚 \(z\) が共通する。これは Zelator, *A Non-Existence Property of Pythagorean Triangles with a 3-D Application*, arXiv:0903.1280, Theorem 1 が禁止する配置そのものである。

Fermatのright-triangle theoremへの直接還元もできる。次を置く。

\[
u=\frac wp,\qquad t=\frac zp,\qquad v=\frac dp.
\]

すると

\[
u^2+t^2=1,
\qquad
v^2=1+t^2
\]

なので

\[
(v+u)^2+(v-u)^2=4.
\]

この有理直角triangleの面積は

\[
\frac{(v+u)(v-u)}2
=\frac{v^2-u^2}{2}
=t^2
\]

という非零有理平方になる。これは「有理直角triangleの面積は平方数にならない」というFermatの定理に反する。

従って

\[
C_{\rm distinct\_raw}(B)=C_{\rm raw}(B)
\]

はすべての \(B\) で恒等的に成立する。有限監査でも \(B\le200,000\) でrepeated-side parameter pointは0件だった。

## 結論

分類は

`A_formal_main_term_and_repeated_side_closed_uniform_error_open`

とする。

確定：

1. 固定法体積と全局所密度
2. 三法Euler積の3位の極
3. rawの形式的次数4
4. primitive oriented countの形式的次数3
5. repeated-side寄与の恒等的消滅

未証明：

- rawおよびprimitiveの漸近式そのもの
- 固定法に一様な格子点誤差
- Selberg–DelangeまたはTauberian移行に必要な解析条件
- primitive oriented countから \(N_1\) を単独抽出するためのexact-two/exact-three項の評価

次は Stage12-N1-2g として、固定法格子点誤差の一様評価が既存のgeometry-of-numbers、Möbius分解、平均誤差評価で閉じるかを監査する。

## 出典

- Konstantine Zelator, *A Non-Existence Property of Pythagorean Triangles with a 3-D Application*, arXiv:0903.1280, Theorem 1.
- Fermat's right-triangle theorem：有理直角triangleの面積は非零平方数にならない。
