# Stage12-N1-2g：geometry-of-numbers・Möbius分解・平均誤差の一様性監査

## 判定

通常の geometry-of-numbers と、三つの coprime 条件に対する Möbius 分解を点ごとに適用し、誤差を絶対値で加算する方法だけでは、Stage12-N1-2f の形式的主項を漸近式へ昇格できない。

分類は

```text
B_pointwise_geometry_of_numbers_not_sufficient_averaged_anisotropic_input_required
```

とする。

## 1. 固定法格子点問題

Stage12-N1-2e の変数変換

\[
h=au,\qquad r=bv,\qquad s=cw
\]

後、固定された pairwise-coprime な法 \((a,b,c)\) に対して数える対象は

\[
au\bigl(b^2v^2+c^2w^2\bigr)\le 2B,
\qquad bv<cw,
\]

および

\[
(v,w)=1,\qquad (v,c)=1,\qquad (w,b)=1
\]

と偶奇条件を満たす格子点である。

固定 \(u\) で

\[
T_u=\sqrt{\frac{2B}{au}}
\]

と置くと、楕円の半軸はおよそ

\[
X_u=\frac{T_u}{b},\qquad Y_u=\frac{T_u}{c}
\]

である。ordinary lattice points に対する Lipschitz principle または definable-family の lattice-counting theorem は、面積主項に加えて

\[
O(X_u+Y_u+1)
\]

型の境界誤差を与える候補となる。Barroero–Widmer の定理は、projection volume と successive minima を用いて、この種の ordinary count を一様に整理する枠組みを与える。

ただし、この段階では visibility と局所 coprimality は未処理である。

## 2. 三つの coprime 条件の Möbius 分解

厳密に

\[
\mathbf 1_{(v,w)=1}\mathbf 1_{(v,c)=1}\mathbf 1_{(w,b)=1}
=
\sum_{d\mid v,w}\mu(d)
\sum_{e\mid v,c}\mu(e)
\sum_{f\mid w,b}\mu(f)
\]

と展開できる。

各 \((d,e,f)\) に ordinary boundary estimate を適用し、絶対値で加算すると、少なくとも \(d\) に関する harmonic sum が現れる。\(b,c\) の divisor multiplicity を楽観的に無視しても、固定 \((a,b,c)\) の誤差モデルは

\[
E_{a,b,c}(B)
\ll
\frac{B\log(2B)}{abc}
\]

となる。

これは真の誤差の下界ではなく、点ごとの境界評価を絶対値で通した場合の上界予算である。

## 3. 全法加算後の次数

\[
x=\log a,\qquad y=\log b,\qquad z=\log c,
\qquad L=\log B
\]

とする。法の有効領域は

\[
x+2\max(y,z)<L
\]

で、その体積は

\[
\int 1\,dx\,dy\,dz=\frac{L^3}{12}.
\]

固定法誤差に含まれる追加の \(\log B=L\) を掛けると、全法絶対誤差モデルは

\[
\frac{1}{12}B L^4
\]

となる。

一方、Stage12-N1-2f で得た形式的 raw 主項の対数単体積分は

\[
\frac{1}{48}B L^4.
\]

従って、elementary geometry-of-numbers と absolute Möbius summation の組合せは、主項と同じ \(B(\log B)^4\) 次数しか与えない。省略した \(b,c\) の divisor cost を入れる前の時点で、raw 漸近式を閉じられない。

## 4. 固定領域の高度な結果が直接使えない理由

Zhai の primitive planar-domain result では、固定された滑らかな領域 \(D\) に対して

\[
B_D(x)=\frac{6}{\pi^2}\operatorname{area}(D)x
+O\bigl(x^{1/2}\omega(x)\bigr)
\]

型の無条件誤差が得られ、RH の下では指数 \(1/2\) 未満の誤差も与えられる。

しかし Stage12 の領域は \(b/c\) に依存し、その eccentricity は主項領域全体で無制限に増大する。さらに order-sector、偶奇、成長する合同法、\(u\) 和、\(\lambda_1(a)\lambda_1(b)\lambda_1(c)\) 重みが追加される。既存の fixed-\(D\) 定理は、これらを一様に含む三法族としては述べられていない。

## 5. bounded eccentricity だけでは主項を取れない

固定 \(K\) に対し

\[
|\log b-\log c|\le K
\]

へ制限する。形式的主項積分は厳密に

\[
I_{\mathrm{bal}}(L,K)
=
\frac{KL^3}{6}
-rac{K^2L^2}{2}
+rac{2K^3L}{3}
-rac{K^4}{3}
\]

である。一方、全領域は

\[
I_{\mathrm{all}}(L)=\frac{L^4}{48}.
\]

従って

\[
\frac{I_{\mathrm{bal}}(L,K)}{I_{\mathrm{all}}(L)}
\sim \frac{8K}{L}\longrightarrow0.
\]

つまり、eccentricity が有界な compact family に対して一様な定理が得られても、それが回収するのは主項より一つ低い対数次数である。先頭の \(B(\log B)^4\) 係数には、増大する eccentricity を含む一様性が必要となる。

## 6. 平均誤差定理との対応

固定された凸領域について dilation parameter を平均する mean-square・first-moment theorem は再利用候補である。しかし Stage12 が必要とする平均は

- \(h,r,s\) の dyadic block
- \(a,b,c\) の divisor-modulus block
- 変化する eccentricity \(b/c\)
- reciprocal sampling \(T_u^2=2B/(au)\)
- visibility と局所 coprimality
- \(\lambda_1\) 重み

を同時に含む六変数型である。固定領域の dilation average は、この相関した族を直接制御しない。

## 7. 十分な新入力

raw 漸近式だけなら

\[
E_{\mathrm{raw}}(B)=o\bigl(B(\log B)^4\bigr)
\]

でよい。

primitive oriented 主項は \(B(\log B)^3\) なので、outer Möbius inversion を絶対値で処理する場合、

\[
E_{\mathrm{raw}}(X)\ll X(\log X)^\beta,
\qquad \beta<2
\]

なら十分である。実際、外側の \(k\) 和で対数次数が一つ増える。

さらに

\[
E_{\mathrm{raw}}(X)\ll X^{1-\delta}(\log X)^C
\]

という固定 \(\delta>0\) の冪節約が得られれば、outer Möbius 和の絶対値評価は \(O(B)\) となり、primitive 主項に対して十分低次となる。

従って必要なのは、全 anisotropic 三法族に対する weighted visible-ellipse discrepancy であり、次のいずれかである。

1. \(B\) に関する冪節約
2. 少なくとも raw 総誤差 \(O(B(\log B)^{2-\eta})\)
3. outer Möbius 和または内部 \((d,e,f)\) 和での符号相殺

## 結論

既存の ordinary geometry-of-numbers、coprime Möbius 分解、fixed-domain primitive-point theorem、固定領域の平均誤差定理は、部分的な構成要素としては有効である。しかし、それらをそのまま接続しても必要な一様剰余は得られない。

残る入力は、unbounded eccentricity と三法重みを同時に扱う averaged anisotropic discrepancy である。

次は Stage12-N1-2h として、small/large modulus・eccentricity 分割を厳密化し、Poisson summation と hybrid large sieve により不足する平均相殺が得られるかを監査する。

## 文献

- Fabrizio Barroero and Martin Widmer, *Counting lattice points and o-minimal structures*, arXiv:1210.5943.
- Wenguang Zhai, *On primitive lattice points in planar domains*, Acta Arithmetica 109 (2003), 1–26.
- A. Ivić, E. Krätzel, M. Kühleitner and W. G. Nowak, *Lattice points in large regions and related arithmetic functions: Recent developments in a very classic topic*, arXiv:math/0410522.
