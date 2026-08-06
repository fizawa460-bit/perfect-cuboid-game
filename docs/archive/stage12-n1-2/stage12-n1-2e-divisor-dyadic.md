# Stage12-N1-2e：G の約数指示関数展開と dyadic 法範囲

## 結論

Stage12-N1-2d では、約数展開後に二次合同根

\[
t^2\equiv-1\pmod m
\]

を扱う可能性を候補として残した。しかし、\(G\) を三変数に対して正確に Möbius 反転すると、少なくとも \(G\) 本体についてはこの経路を通る必要がない。

\[
G(n)=\prod_{q\equiv1\pmod4}(2v_q(n)+1)
\]

に対し、

\[
\lambda_1(d)=
\begin{cases}
2^{\omega(d)},& d\text{ の全素因数が }1\pmod4,\\
0,&\text{それ以外}
\end{cases}
\]

ただし \(\lambda_1(1)=1\) と置くと、厳密に

\[
G(n)=\sum_{d\mid n}\lambda_1(d)
\]

となる。

さらに三変数では

\[
G(hrs)=
\sum_{\substack{a\mid h,\ b\mid r,\ c\mid s\\
(a,b)=(a,c)=(b,c)=1}}
\lambda_1(a)\lambda_1(b)\lambda_1(c).
\]

これは上界ではなく厳密な恒等式である。各 \(q\equiv1\pmod4\) について、指数を \(a,b,c\) のうち高々一つへ割り当てる項だけが係数2を持ち、二つ以上へ同時に割り当てる混合差分は0になる。

したがって、Stage12-N1-2b の共有素因子補正 \(K(h,rs)\) は、三つの約数法 \(a,b,c\) を互いに素とする条件へ正確に吸収できる。

## exact raw 和の書き換え

双曲線領域を

\[
\mathcal D_B=\left\{(h,r,s):
1\le r<s,\ (r,s)=1,\ h(r^2+s^2)\le2B,\ h(r^2+s^2)\equiv0\pmod2
\right\}
\]

とすると、

\[
C_{\mathrm{raw}}(B)=
\sum_{(h,r,s)\in\mathcal D_B}
\sum_{\substack{a\mid h,\ b\mid r,\ c\mid s\\
(a,b)=(a,c)=(b,c)=1\\
(a,b,c)\ne(1,1,1)}}
\lambda_1(a)\lambda_1(b)\lambda_1(c).
\]

\(h=au, r=bv, s=cw\) と置くと、固定された法に対する内部問題は

\[
au\left(b^2v^2+c^2w^2\right)\le2B,
\qquad bv<cw
\]

上の格子点計数になる。\(a,b,c\) はすべて奇数なので、元の偶奇条件は

\[
u(v^2+w^2)\equiv0\pmod2
\]

へ移る。また \((b,c)=1\) の下では

\[
(bv,cw)=1
\]

は

\[
(v,w)=(v,c)=(w,b)=1
\]

と同値である。

従って、直近の解析対象は二次合同根ではなく、異方的楕円領域内の倍数格子・coprime・偶奇条件を同時に扱う問題である。

## 実際の dyadic 範囲

元の変数を

\[
H\le h<2H,\qquad R\le r<2R,\qquad S\le s<2S
\]

へ分割する。非空ブロックでは端点定数を除いて

\[
H(R^2+S^2)\ll B,\qquad R<2S,\qquad HS^2\ll B.
\]

約数法を

\[
A\le a<2A,\qquad M\le b<2M,\qquad N\le c<2N
\]

へ分けると、

\[
A\ll H,\qquad M\ll R,\qquad N\ll S.
\]

さらに各点で

\[
abc\le hrs<B
\]

が成立する。最後の不等式は \(r<s\) により

\[
2rs<r^2+s^2
\]

であることから従う。したがって、結合された法の真の範囲は \(B\) 未満である。

スケール変換後の変数長は概ね

\[
u\asymp H/A,\qquad v\asymp R/M,\qquad w\asymp S/N.
\]

素朴には \((H,R,S,A,M,N)\) の dyadic ブロックは \(O((\log B)^6)\) 個であり、実際には \(HS^2\ll B\) などでさらに減る。

## 必要な平均誤差

固定法に対する格子点数を \(N_{a,b,c}^{H,R,S}(X)\)、将来導出する体積・局所密度主項を \(V_{a,b,c}^{H,R,S}(X)\) とし、

\[
E_{a,b,c}^{H,R,S}(X)
=N_{a,b,c}^{H,R,S}(X)-V_{a,b,c}^{H,R,S}(X)
\]

と置く。一つの法ブロックに対する加重誤差は

\[
\mathcal E=
\sum_{a\asymp A,\ b\asymp M,\ c\asymp N}
\lambda_1(a)\lambda_1(b)\lambda_1(c)
E_{a,b,c}^{H,R,S}(X)
\]

である。

raw 段階で十分な入力の一例は、ある固定 \(\delta>0\) に対し

\[
\sum_{\text{admissible dyadic blocks}}|\mathcal E|
\ll X^{1-\delta}
\]

という三法平均の一様評価である。これは点ごとの \(m^{1/2}\) 型評価ではなく、法 \((a,b,c)\) 全体での cancellation を要求する。

large sieve 型の二乗平均へ翻訳するには

\[
W_2(A,M,N)=
\sum_{a\asymp A,b\asymp M,c\asymp N}
\lambda_1(a)^2\lambda_1(b)^2\lambda_1(c)^2
\]

と置く。Cauchy–Schwarz により

\[
|\mathcal E|
\le W_2(A,M,N)^{1/2}
\left(\sum|E_{a,b,c}^{H,R,S}(X)|^2\right)^{1/2}.
\]

\(L=\log(2X)\) とすると、各 admissible block で

\[
\sum|E_{a,b,c}^{H,R,S}(X)|^2
\ll
\frac{X^{2-2\delta}}{L^{12}W_2(A,M,N)}
\]

が得られれば、各ブロックの誤差は \(X^{1-\delta}/L^6\) 以下となり、全ブロックを足して \(O(X^{1-\delta})\) になる。これは十分条件として設定した誤差予算であり、既知定理として主張するものではない。

## global Möbius 反転の予算

primitive oriented count は

\[
C_{\mathrm{prim}}(B)=
\sum_{k\le B}\mu(k)
C_{\mathrm{distinct,raw}}(\lfloor B/k\rfloor)
\]

である。raw 誤差が

\[
E(X)\ll X^{1-\delta}(\log X)^C
\]

であっても、外側を絶対値で足すと一般に \(O(B(\log B)^C)\) まで戻り、冪節約は保存されない。

従って、この誤差が最終的に十分かを判断するには、次の二点が先に必要である。

1. distinct raw 主項が \(B\) を何乗の対数で上回るか
2. repeated-side 項がその主項に対して低次か

主項が \(B(\log B)^\eta\)（\(\eta>0\)）であれば、反転後の \(O(B)\) 級誤差は低次になり得る。主項が線形級だけなら、外側の Möbius cancellation を別途使う必要がある。

## 判定

分類は

`A_exact_divisor_expansion_replaces_quadratic_root_route`

とする。

確定したことは次の通り。

- \(G\) は正係数の厳密な約数指示関数和である
- \(G(hrs)\) は互いに素な三つの座標法へ厳密分解できる
- 結合法は点ごとに \(B\) 未満である
- 直近の必要入力は三法平均の加重格子点誤差であり、\(t^2\equiv-1\pmod m\) の根に対するlarge sieveではない

次は Stage12-N1-2f として、体積・局所密度主項、その対数次数、repeated-side 寄与を確定する。

## 文献上の境界

Shparlinski のモジュラー双曲線評価や、Duke–Friedlander–Iwaniec 型の二次合同根の equidistribution は、法を動かした合同根・Weyl和を扱う強力な候補である。しかし今回の厳密展開が直接生成する対象は座標倍数格子であり、それらの定理を現段階で直接適用する根拠はない。

- Igor E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879.
- Hieu T. Ngo, *On Roots of Quadratic Congruences*, arXiv:2107.13301.
