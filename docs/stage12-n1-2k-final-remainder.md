# Stage12-N1-2k：最終平均誤差・Euler定数・二法主項監査

## 結論

Stage12-N1-2jで残った

- fixed \((r,s)\) partial sum の平均一様誤差
- 二法Euler積 \(\eta\) と三法Euler積 \(\kappa\) の一致
- \(\beta\) 二法重みに対するcore／wingおよびendpoint整理

は、既知の固定領域primitive格子点評価と多変数平均値定理を使う標準的な段階まで閉じる。

分類は

```text
A_N1_2_leading_asymptotic_closed_at_standard_theorem_level_series_complete
```

とする。

Stage12-N1-2bで定義したprimitive oriented countについて、

\[
\boxed{
C_{\mathrm{prim}}(B)
\sim
\frac{\kappa}{12\pi}\,B(\log B)^3
}
\]

が最終的な先頭漸近式となる。

これは完全直方体の存在・非存在を主張するものではなく、N1-2で定義した向き付き計数の漸近式である。また、Euler積の数値は認証区間ではない。

---

## 1. fixed \((r,s)\) 問題は固定円問題へ変換できる

Stage12-N1-2jの正のversion

\[
A^+_{r,s}(m)=A_{r,s}(m)+1_{m=1}
\]

のDirichlet級数は

\[
F_{r,s}(s)
=
G(rs)\,F_0(s)\,H_{r,s}(s)
\]

と分解できる。base部分は

\[
F_0(s)
=
\frac{\zeta(s)L(s,\chi_4)}
{(1+2^{-s})\zeta(2s)}
=
\sum_{n\ge1}\frac{a_0(n)}{n^s},
\]

かつ

\[
a_0(n)=
\begin{cases}
2^{\omega(n)},&
p\mid n\Rightarrow p\equiv1\pmod4,\\
0,&\text{otherwise}.
\end{cases}
\]

奇数 \(n\) について、\(4a_0(n)\) は

\[
x^2+y^2=n,\qquad (x,y)=1
\]

を満たす整数点の個数に厳密に一致する。従ってbase partial sumは、円内のprimitive格子点をmod \(2\) の固定剰余類に制限した問題である。

Wenguang Zhaiの固定滑らか凸領域に対するprimitive格子点評価と同じMöbius・zero-free-region処理により、

\[
\sum_{n\le X}a_0(n)
=
\frac{X}{\pi}
+
O\!\left(
X^{1/2}\omega(X)
\right),
\]

\[
\omega(X)
=
\exp\!\left(
-c(\log X)^{3/5}
(\log\log X)^{-1/5}
\right)
\]

を使える。

重要なのは、ここで領域が変形する楕円族ではなく、**一つの固定円と有限個のparity class**になったことである。Stage12-N1-2gで問題だったeccentricityの一様性は発生しない。

---

## 2. \(rs\) 依存は有限Euler補正だけに残る

\(p^t\Vert rs,\ p\equiv1\pmod4\) に対して

\[
H_{r,s}(s)
=
\prod_{p^t\Vert rs}
\frac{
1-\frac{2t-1}{2t+1}p^{-s}
}{
1+p^{-s}
}.
\]

その局所係数は

\[
h_{r,s}(p^j)
=
(-1)^j\frac{4t}{2t+1}
\qquad(j\ge1).
\]

従って

\[
A^+_{r,s}
=
G(rs)\,(a_0*h_{r,s})
\]

が厳密に成り立つ。

絶対係数の \(1/2\)-重みは

\[
H_{\mathrm{abs}}(rs)
=
\prod_{\substack{p^t\Vert rs\\p\equiv1(4)}}
\left(
1+
\frac{4t/(2t+1)}{\sqrt p-1}
\right)
\]

で制御できるため、

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+
O\!\left(
G(rs)H_{\mathrm{abs}}(rs)
X^{1/2}\omega(X)
\right)
\]

を得る。

ここで

\[
\gamma(rs)
=
\frac1\pi
\prod_{\substack{p^t\Vert rs\\p\equiv1(4)}}
\left(
1+\frac{2t(p-1)}{p+1}
\right).
\]

監査スクリプトでは次を有限検算した。

- base Dirichlet係数：5,000件
- primitive odd-circle表現数：2,500件
- fixed-\((r,s)\) correction convolution：39,296件
- \(\beta\) 局所上界：147素数

---

## 3. fixed-\((r,s)\) remainderを全体で足す

\[
W(n)=G(n)H_{\mathrm{abs}}(n)
\]

と置く。これは固定された非負乗法関数である。

- \(p\equiv3\pmod4\) では局所一次係数は \(1\)
- \(p\equiv1\pmod4\) では局所一次係数は \(3+O(p^{-1/2})\)

なので、Dirichlet級数のpole orderは \(2\) である。従って通常のSelberg–Delange上界により

\[
\sum_{n\le R}W(n)\ll R\log R.
\]

保持領域では

\[
X\ge X_0
=
\exp\!\left((\log B)^{1/4}\right).
\]

fixed-\((r,s)\) remainderの総和は

\[
\ll
B(\log B)^2\omega(X_0).
\]

\(\omega(X_0)\) は任意の固定対数冪より速く減少するため、

\[
B(\log B)^2\omega(X_0)
=
o\!\left(B(\log B)^{-A}\right)
\]

が任意の固定 \(A\) に対して成り立つ。

shallow部分はStage12-N1-2jの

\[
\tau=(\log B)^{-3/4}
\]

を使い、

\[
O\!\left(B(\log B)^{3/2+o(1)}\right)
\]

であり、先頭主項 \(B(\log B)^3\) に対して低次である。

したがって、平均一様remainderは閉じる。

---

## 4. residueは二法 \(\beta\) 展開になる

\[
\beta(p^j)
=
\frac{2(p-1)}{p+1}
\qquad
(p\equiv1\pmod4,\ j\ge1)
\]

とし、それ以外を0とする。

\[
\gamma(n)
=
\frac1\pi\sum_{d\mid n}\beta(d).
\]

\((r,s)=1\) なので、\(r\) と \(s\) に一つずつdivisor modulusを置く二法問題へ分離する。

\(q\equiv1\pmod4\) の局所密度因子は

\[
1+\frac{4q}{(q+1)^2}.
\]

従って二法Euler定数を

\[
\eta
=
\left(\frac{\pi}{4}\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}
(1-p^{-2})^2
\prod_{q\equiv1(4)}
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4
\]

と定義する。

係数系は非負であり、関連する二変数Dirichlet級数はde la Bretècheのmultiple-sum theoremの標準仮定を満たす。smooth dyadic partitionとpartial summationにより、主項はdegree \(3\) の対数多項式となる。

また

\[
0\le\beta(p^j)<2
\]

なので、Stage12-N1-2iで許容した固定次数のRamanujan／divisor weightsに支配される。従ってcore・wing・smoothing・endpointの評価はそのまま移植できる。

---

## 5. \(\eta=\pi\kappa\) は厳密恒等式

Stage12-N1-2fの三法局所因子は、\(q\equiv1\pmod4\) で

\[
F_q(1)
=
\frac{q^2+6q+1}{q^2-1}.
\]

正規化後の局所因子を比較すると、

\[
\frac{\eta_q}{\kappa_q}
=
\frac{q^2}{q^2-1}
=
(1-q^{-2})^{-1}.
\]

\(p\equiv3\pmod4\) でも

\[
\frac{\eta_p}{\kappa_p}
=
(1-p^{-2})^{-1}.
\]

archimedean・2-adic前置因子の比は

\[
\frac{\eta_{\mathrm{front}}}
{\kappa_{\mathrm{front}}}
=
\frac8\pi.
\]

一方、

\[
\prod_{p\ {\rm odd}}
(1-p^{-2})^{-1}
=
(1-2^{-2})\zeta(2)
=
\frac{\pi^2}{8}.
\]

従って

\[
\boxed{\eta=\pi\kappa}.
\]

そのため二法表示の先頭定数は

\[
\frac{\eta}{12\pi^2}
=
\frac{\kappa}{12\pi},
\]

となり、Stage12-N1-2fのformal primitive constantと厳密に一致する。

素数上限200,000の診断値は

\[
\frac{\eta}{\pi\kappa}
=
0.9999996198305922,
\]

\[
\frac{\kappa}{12\pi}
\approx
0.0004922973154676823.
\]

数値はEuler積の収束確認であり、認証区間ではない。

---

## 6. 最終判定

Stage12-N1-2系列で必要だった項目は次の通り閉じた。

1. raw計数とprimitive計数の厳密なMöbius関係
2. 三法formal mainとpole order
3. repeated-side寄与が恒等的に0
4. anisotropic格子点問題のPoisson再編成
5. core／wingの指数予算
6. boundary layerのprimitive-first吸収
7. fixed-\((r,s)\) remainderの固定primitive-circle問題への縮約
8. 二法Euler積と三法Euler積の厳密一致
9. primitive oriented leading asymptoticの先頭定数

従って、**自動的に12-N1-2lへ進める必要はない**。

次は新しい解析段階ではなく、Stage12-N1-2b〜2k全体を対象とするadversarial AI reviewまたは人手レビューとする。

---

## 主張しないこと

- 完全直方体の存在または非存在
- \(\kappa,\eta\) の認証数値区間
- 独立査読済みの完成論文であること
- Stage12-N1の定義外にある別のexact-multiplicity減算
- 新しいprimitive格子点定理

---

## 文献

- Wenguang Zhai, *On primitive lattice points in planar domains*, Acta Arithmetica 109 (2003), 1–26.
- Régis de la Bretèche, *Estimation de sommes multiples de fonctions arithmétiques*, Compositio Mathematica 128 (2001), 261–298.
- Régis de la Bretèche and Gérald Tenenbaum, *Remarks on the Selberg–Delange method*, Acta Arithmetica 200 (2021), 349–369.
