# Stage12-N1-2i：15/32 clustered core と 1/4 wing の指数予算監査

## 結論

Stage12-N1-2h で未処理だった

- `15/32` の clustered two-dimensional core
- `1/4` の one-dimensional eccentric wing

は、**保持した deep・nonterminal・small-visibility-divisor 領域に限れば、古典的な指数対 `(1/6,2/3)` と Ramanujan 和の厳密な約数展開で必要誤差へ届く構造**になっている。

分類は

```text
A_retained_core_and_wing_close_boundary_layers_remain
```

とする。

ただし、raw または primitive の漸近式そのものはまだ証明していない。真の残課題は、Stage12-N1-2h で誤差として切り捨てた shallow-height 層と terminal-u 層である。

## 1. Ramanujan 和で重要なのは二乗平均だけではない

Ramanujan 和には厳密な恒等式

\[
c_q(n)=\sum_{r\mid(q,n)}r\mu(q/r)
\]

がある。従って

\[
|c_q(n)|\le(q,n)
\]

であり、さらに

\[
\sum_{n\bmod q}|c_q(n)|^2=q\varphi(q)
\]

が成り立つ。

有限区間については、約数展開を絶対値で足すだけで

\[
\sum_{1\le n\le K}|c_q(n)|
\le K\,2^{\omega(q)}
\]

を得る。

今回の核心は、係数が大きい場合には必ずその大きさを生む約数 `r` が周波数 `n` を割ることである。つまり、**大きな算術係数は最低周波数へ自由に集中できず、同時に周波数も大きくなる**。

Stage12-N1-2h では係数と周波数を分離して spacing を考えたため、`15/32` 領域に新しい nonlinear large sieve が必要に見えた。今回はこの相関を先に使う。

監査スクリプトでは次を有限検算した。

- Ramanujan 約数公式：8,256件
- 周期二乗平均：128法
- truncated first moment bound：32,768件

## 2. 使用する指数対

`u\asymp U` 上の位相は

\[
f(u)=A u^{-1/2},\qquad Z=\frac{A}{\sqrt U}
\]

である。

指数対 `(\kappa,\lambda)` により、標準的な偏微分条件と部分和変換の下で

\[
\sum_{u\asymp U}R_u^{1/2}e(f(u))
\ll
R^{1/2}Z^\kappa U^\lambda
\]

型の評価を使う。

今回は古典的な

\[
(\kappa,\lambda)=\left(\frac16,\frac23\right)
\]

だけを代入する。より新しい指数対の最適化は、この適合性判定には不要だった。

## 3. 二次元 core：`Q\le R`

`b\le c` として

\[
Q=2bcd,
\qquad
X=\frac{R}{bd},
\qquad
Y=\frac{R}{cd}
\]

と置く。

この領域には Stage12-N1-2h の `9/32` と `15/32` の双方が含まれる。

### 3.1 軸周波数

`k=0` または `l=0` の周波数は別に処理する。零座標側には `\varphi(b)` または `\varphi(c)` が現れるが、非零座標側は Ramanujan first moment で足せる。

`Q\le R` から

\[
b\le Y,
\qquad
c\le X
\]

が従い、軸周波数の誤差はブロック主項 `M_block` に対して

\[
\ll \operatorname{polylog}(B)\frac{M_{\rm block}}{Y}
\]

となる。

### 3.2 内部周波数

\[
\sqrt{k^2+l^2}\asymp K,
\qquad k,l\ne0
\]

のshellを考える。Ramanujan 約数公式を展開すると、shell全体の絶対係数は

\[
\ll
K^2\,2^{\omega(b)+\omega(c)}
\]

となる。

Poisson の曲率境界振幅と `u` の指数対評価を組み合わせると、shell誤差は

\[
E_K
\ll
W U^\lambda
R^{1/2+\kappa}
Q^{-1/2-\kappa}
K^{1/2+\kappa}
\]

となる。`W` は固定次数の divisor weight を表す。

物理空間で境界を幅 `\Delta` だけ平滑化すると、dual cutoff は概ね

\[
K\le \frac Q\Delta
\]

である。従ってFourier側は

\[
E_{\rm Fourier}
\ll
W U^\lambda R^{1/2+\kappa}
\Delta^{-1/2-\kappa},
\]

境界層側は

\[
E_{\rm boundary}
\asymp
\frac{UR\Delta}{Qd}
\]

となる。

`(1/6,2/3)` を代入して均衡させると

\[
\Delta_*
=(Qd)^{3/5}U^{-1/5}R^{-1/5}.
\]

`\Delta_*\ge1` なら、主項に対する相対誤差は

\[
\ll
W(Qd)^{3/5}U^{-1/5}R^{-6/5}
\le
W(d/R)^{3/5}.
\]

`\Delta_*<1` なら `\Delta=1` とし、その条件自体を使うことで相対誤差は `\ll W/R` となる。

Stage12-N1-2h の保持領域では

\[
Y=\frac{R}{cd}\ge S_0,
\qquad
S_0=\exp\!\left(\frac12\sqrt{\log B}\right).
\]

よって

\[
\frac dR=\frac1{cY}\le\frac1{S_0}
\]

であり、core全体の相対誤差は

\[
\ll
\operatorname{polylog}(B)S_0^{-3/5}
\]

となる。

従って、`15/32` の cluster は指数予算上は閉じる。modulus spacing を直接解く必要はない。

## 4. 一次元 wing：`Q>R`

元の異方的座標へ戻し、長方向だけを sawtooth または one-dimensional Poisson で処理する。

\[
X=\frac{R}{bd}\ge
Y=\frac{R}{cd}\ge S_0
\]

とする。

### 4.1 順序境界

`x<y` が有効境界となる部分では、各短方向行のfloor誤差を足して

\[
D\ll WY
\]

である。面積 `XY` に対する相対誤差は

\[
\ll \frac W X\le\frac W Y.
\]

### 4.2 円弧境界

`X\le Y^2` の場合、Vaaler型のsawtooth切断と指数対 `(1/6,2/3)` により

\[
D(X,Y)
\ll
W X^{1/7}Y^{5/7}.
\]

従って

\[
\frac{D(X,Y)}{XY}
\ll
W X^{-6/7}Y^{-2/7}
\le
W Y^{-8/7}.
\]

一方 `X>Y^2` なら、振動評価を使わず `D\ll WY` としても

\[
\frac{D}{XY}\ll \frac W X<WY^{-2}.
\]

従ってwing全体では少なくとも

\[
\operatorname{polylog}(B)S_0^{-1}
\]

の相対節約が得られる。

## 5. 三法重みを足した後

上記で現れる `2^{\omega(n)}` や固定次数の `\tau(n)` は、最悪値を点ごとに使わない。`\lambda_1` を伴う調和和をEuler積で評価すると、固定次数ごとに有限次数の極しか持たないため、全体では `\log B` の固定冪の損失になる。

一方

\[
S_0^{-3/5}
=
\exp\!\left(-\frac{3}{10}\sqrt{\log B}\right)
\]

は任意の固定された負の対数冪より小さい。

したがって、保持した deep・nonterminal・small-d 領域のcoreとwingは、保守的なraw誤差目標

\[
O\bigl(B(\log B)^{2-\eta}\bigr)
\]

にも適合する。

## 6. 本当の残課題：boundary layer

Stage12-N1-2h では

\[
\tau=\sigma=(\log B)^{-1/4}
\]

として、shallow-height と terminal-u を lower-order mass として除いた。

shallow部分は

\[
B(\log B)^4 O(\tau^2)
=
O\bigl(B(\log B)^{7/2}\bigr),
\]

terminal部分は

\[
B(\log B)^4O(\sigma)
=
O\bigl(B(\log B)^{15/4}\bigr).
\]

どちらも raw 主項 `B(\log B)^4` に対しては `o(main)` だが、global Möbius反転を絶対値で通すための保守的目標 `B(\log B)^{2-\eta}` よりはるかに大きい。

単にcutoffを強めることもできない。一般に

\[
\tau=L^{-p},
\qquad
\sigma=L^{-q},
\qquad
L=\log B
\]

とすると、除外massを `B L^{2-\eta}` 未満にするには概ね

\[
p>1,
\qquad
q>2
\]

が必要となる。

しかし保持領域の最短辺は

\[
\log S_0
=\frac12\sigma\tau L
=\frac12L^{1-p-q}
\]

なので、この条件下では `S_0` が成長しない。

従って、boundary layerはさらに小さく切り捨てるのではなく、**主項またはMöbius構造の一部として実際に評価する必要がある**。

## 7. 次段階

Stage12-N1-2jでは次を監査する。

1. `u` または `h` をfloor関数で先に厳密加算する
2. shallow `U` を有限長Dirichlet polynomialとして扱う
3. terminal部分をMellin/Perron分離する
4. global Möbius反転を誤差切断より前に行い、境界層の符号相殺を利用できるか確認する
5. rawの対数多項式を少なくとも `B(\log B)^2` レベルまで展開できるか確認する

## 文献

- Timothy S. Trudgian and Andrew Yang, *Toward optimal exponent pairs*, arXiv:2306.05599.
- Pliego, *Estimates for a three-dimensional exponential sum with monomials*, arXiv:2211.02096.
- Tsz Ho Chan and Angel V. Kumchev, *On sums of Ramanujan sums*, arXiv:1009.4432.

これらの文献から完全なStage12定理を直接引用したわけではない。指数対の一般枠組みと手法適合性の参考として使用し、Ramanujan恒等式自体は有限監査を伴う初等恒等式として扱った。
