# Stage12-N1-2j：primitive-first Möbius と boundary layer 監査

## 判定

Stage12-N1-2i で残った shallow-height 層と terminal-u 層は、global Möbius 反転を最後に絶対値で処理する順序をやめ、最初に `h` 方向へ畳み込むことで構造的に解消できる。

分類は

```text
A_primitive_first_boundary_layers_close_uniform_average_remainder_open
```

とする。

primitive N1 漸近式そのものはまだ主張しない。残る課題は、固定 `(r,s)` の部分和に対する averaged uniform remainder と、二法 `beta` 重みでの最終的な平滑化・endpoint bookkeeping である。

## 1. global Möbius を切断前に移す

raw oriented count の重みは

\[
G(hrs)-1
\]

であり、global primitive count は厳密に

\[
C_{\rm prim}(B)
=
\sum_{k\le B}\mu(k)
C_{\rm raw}(\lfloor B/k\rfloor)
\]

である。

ここで dyadic 分割、shallow cut、terminal-u cut を行う前に

\[
n=kh
\]

と置き換える。

固定された coprime pair `(r,s)` に対して

\[
A_{r,s}(m)
=
\sum_{k\mid m}
\mu(k)\{G((m/k)rs)-1\}
\]

を定義する。

### 1.1 `r,s` がともに奇数

この場合

\[
q=r^2+s^2
\]

は偶数で、raw `h` に偶奇制約はない。Möbius 畳み込み後の有効 height は奇数で、素因数はすべて `1 mod 4` に限られる。

直接表示は

\[
\sum_{m\le 2B/q}A_{r,s}(m).
\]

### 1.2 `r,s` が opposite parity

この場合 `q` は奇数で、raw parameterization では `h` が偶数である。

reindex 後の height `n` に対する係数は

\[
\sum_{k\mid n\atop n/k\ {m even}}
\mu(k)\{G((n/k)rs)-1\}.
\]

`G` は2進指数に依存しないため、これは

- `v_2(n)=1` のときだけ非零
- `n=2m` と書けば係数は `A_{r,s}(m)`

となる。

従って直接表示は

\[
\sum_{m\le B/q}A_{r,s}(m).
\]

## 2. primitive height weight の厳密式

`m=1` では

\[
A_{r,s}(1)=G(rs)-1.
\]

`m>1` では、`m` に `1 mod 4` 以外の素数が含まれると

\[
A_{r,s}(m)=0.
\]

すべての素因数が `1 mod 4` なら

\[
A_{r,s}(m)
=
G(rs)
\prod_{p\mid m}
\frac{2}{2v_p(rs)+1}.
\]

この値は非負整数である。

監査では次を有限検算した。

- local Möbius convolution：16,416件
- parity-restricted convolution：21,888件
- residue local identity：352件
- `beta` divisor expansion：1,000件

## 3. fixed `(r,s)` Dirichlet series

`m=1` の `-1` を戻して

\[
A^+_{r,s}(m)=A_{r,s}(m)+\mathbf 1_{m=1}
\]

と置く。

Dirichlet series は

\[
\sum_{m\ge1}\frac{A^+_{r,s}(m)}{m^s}
=
G(rs)
\prod_{p\equiv1(4)}
\left(
1+
\frac{2}{2v_p(rs)+1}
\frac{p^{-s}}{1-p^{-s}}
\right).
\]

`p\nmid rs` の base product は

\[
\prod_{p\equiv1(4)}
\frac{1+p^{-s}}{1-p^{-s}}
=
\frac{\zeta(s)L(s,\chi_4)}
{(1+2^{-s})\zeta(2s)}.
\]

これは `s=1` に単純極を持ち、その residue は

\[
\frac1\pi
\]

である。

`p^t\Vert rs` の finite correction は

\[
R_{p,t}(s)
=
\frac{
1-\frac{2t-1}{2t+1}p^{-s}
}{1+p^{-s}}.
\]

従って residue weight は

\[
\gamma(rs)
=
\frac1\pi
\prod_{p^t\Vert rs\atop p\equiv1(4)}
\left(
1+rac{2t(p-1)}{p+1}
\right).
\]

候補部分和は

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1+R_{r,s}(X).
\]

## 4. 三法から二法への縮約

multiplicative function `beta` を

\[
\beta(p^j)
=
\frac{2(p-1)}{p+1}
\quad
(p\equiv1\pmod4,\ j\ge1)
\]

で定義し、それ以外の素数を含む場合は0とする。

local identity

\[
1+rac{2t(p-1)}{p+1}
=
\sum_{j=0}^{t}\beta(p^j)
\]

から

\[
\gamma(n)
=
\frac1\pi\sum_{d\mid n}\beta(d)
\]

を得る。

`(r,s)=1` なので divisor は `r` 側と `s` 側に分離する。従って primitive-first 主項は、raw の三法 `(a,b,c)` ではなく、二法 `(b,c)` の geometry-of-numbers 問題へ縮約される。

二法 Euler factor は

\[
J_p(s)
=
1+
\frac{4p(p-1)}{(p+1)^2(p^s-1)}
\quad (p\equiv1\pmod4)
\]

となり、二位の極を持つ。radial logarithm と合わせて primitive の対数次数3を再現する。

素数20万までの部分積では

\[
\eta\approx0.05830533485,
\qquad
\frac{\eta}{\pi\kappa}\approx0.99999962.
\]

これにより候補定数

\[
\frac{\eta}{12\pi^2}
\]

と Stage12-N1-2f の

\[
\frac{\kappa}{12\pi}
\]

が数値的に一致する。これは診断値であり、部分積の誤差保証ではない。

## 5. boundary layer の解消

### 5.1 outer Möbius error が消える

global Möbius を exact reindexing で最初に処理したため、raw remainder を

\[
\sum_k|\mu(k)|\,|E(B/k)|
\]

で足す必要がない。

従って Stage12-N1-2i で使用した保守的な raw target

\[
B(\log B)^{2-\eta}
\]

は boundary layer に対して不要となる。primitive 主項

\[
B(\log B)^3
\]

に対して `o(main)` であればよい。

### 5.2 terminal-u 層

`h=a u` と分解せず、primitive height `m` の部分和を一度に評価する。

従って terminal-u 層は小さく切って捨てる対象ではなくなり、構造上消滅する。

### 5.3 shallow 層

primitive logarithmic simplex は

\[
\int_{y,z\ge0\atop 2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=
\frac{L^3}{12}.
\]

`shallow` 条件

\[
L-2\max(y,z)\le\tau L
\]

の主項比率は厳密に

\[
3\tau^2-2\tau^3.
\]

ここで

\[
\tau=L^{-3/4}
\]

と取れば shallow formal mass は

\[
O\left(BL^{3/2}\right),
\]

primitive main に対して十分 lower order である。

一方、保持領域の最短辺 proxy は

\[
S_0
=
\exp\left(\frac12\tau L\right)
=
\exp\left(\frac12L^{1/4}\right)
\]

まで成長する。Stage12-N1-2i の core/wing error に現れる `S_0^{-c}` は、依然として任意の固定対数冪を上回る節約になる。

## 6. exact finite equivalence

primitive-first formulaを直接列挙し、以前のglobal Möbius inversion結果と比較した。

| B | primitive-first | previous global Möbius | difference |
|---:|---:|---:|---:|
| 1,000 | 1,208 | 1,208 | 0 |
| 2,000 | 2,888 | 2,888 | 0 |
| 5,000 | 9,030 | 9,030 | 0 |
| 10,000 | 21,360 | 21,360 | 0 |
| 20,000 | 49,592 | 49,592 | 0 |
| 50,000 | 147,998 | 147,998 | 0 |
| 100,000 | 336,416 | 336,416 | 0 |
| 200,000 | 760,206 | 760,206 | 0 |

全63,638 pair block、126,955 nonzero primitive-height termを直接監査した。

## 7. 残る入力

必要なのは、保持領域

\[
X\ge\exp((\log B)^{1/4})
\]

での averaged estimate

\[
R_{r,s}(X)
\]

である。

base product は

\[
\frac{\zeta(s)L(s,\chi_4)}
{(1+2^{-s})\zeta(2s)}
\]

なので、Selberg–Delange または Perron contour に適合する。finite correction `R_{p,t}` の係数は各素数で絶対収束し、`rs` 依存は平均 divisor weight として処理する候補がある。

ただし、既存の fixed-function theorem をそのまま parameter-uniform statement として引用することはしない。次段階で平均誤差を明示的に証明または停止判定する。

## 8. 次段階

Stage12-N1-2kでは次を行う。

1. fixed `(r,s)` partial sum の averaged uniform remainder を導出する
2. 二法 Euler constant `eta=pi*kappa` を局所因子レベルで確定する
3. `lambda_1` から `beta` へ置き換えた二法 core/wing bookkeeping を再実行する
4. primitive N1 asymptoticを定理として閉じられるか最終判定する

## 文献

- Régis de la Bretèche and Gérald Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929.

この文献は multiplicative partial sum の一般枠組みとして参照する。Stage12で必要な `rs` 平均一様性は別途監査対象である。
