# Stage12-N1-2h：small/large modulus・eccentricity分割とPoisson監査

## 判定

Stage12-N1-2g で障害になった「増大する楕円の eccentricity」は、偶奇条件と二つの局所 coprimality 条件を **Poisson summation の前に周期関数として統合する**ことで、二次元 core では除去できる。

ただし、Poisson 後に得られる位相は古典的な Kloosterman sum ではなく、

\[
e\!\left(
\pm
\frac{C\sqrt{k^2+\ell^2}}
{bcd\sqrt{u}}
\right)
\]

型の Ramanujan 重み付き nonlinear reciprocal phase である。通常の additive spacing が直接働く領域は形式的主項の \(9/32\) に限られ、残る \(15/32\) の clustered core と \(1/4\) の one-dimensional wing には新しい平均評価が必要である。

分類は

```text
C_poisson_isotropization_succeeds_hybrid_spacing_only_partial
```

とする。

## 1. 出発点

Stage12-N1-2e 以降の固定法表示は

\[
h=au,\qquad r=bv,\qquad s=cw
\]

であり、\(a,b,c\) は奇数、pairwise coprime、素因数は \(1\bmod 4\) に限られる。領域は

\[
au\bigl((bv)^2+(cw)^2\bigr)\le 2B,
\qquad bv<cw,
\]

条件は

\[
(v,w)=1,\qquad (v,c)=1,\qquad (w,b)=1.
\]

偶奇は次の二種類である。

1. \(v,w\) がともに奇数：\(u\) は任意。
2. \(v,w\) が異なる偶奇：\(u\) は偶数。

## 2. shallow height と terminal \(u\) の除去

\(c=\max(b,c)\) として

\[
U=\frac{B}{ac^2},\qquad
t=\log U,\qquad
L=\log B
\]

と置く。Stage12-N1-2f の形式的主項では、この block の重みは \(t\) である。

### 2.1 shallow block

\(t\le \tau L\) の形式的主項比率は厳密に

\[
F_{\mathrm{shallow}}(\tau)
=
6\tau^2-8\tau^3+3\tau^4.
\]

したがって \(\tau\to0\) なら shallow block は \(o(1)\) 比率になる。

### 2.2 terminal \(u\)

一つの法 block で

\[
u\le U^{1-\sigma}
\]

へ制限すると、除外する harmonic main term は

\[
\int_{U^{1-\sigma}}^U\frac{du}{u}
=
\sigma\log U
\]

であり、block 主項のちょうど \(\sigma\) 比率である。

保持領域では短い側の格子長が

\[
\sqrt{\frac{U}{u}}\ge U^{\sigma/2}
\]

となる。

### 2.3 canonical cutoff

\[
\tau=\sigma=L^{-1/4}
\]

と選ぶと、

\[
F_{\mathrm{shallow}}(\tau)=O(L^{-1/2}),
\qquad
F_{\mathrm{terminal}}=\sigma=O(L^{-1/4}),
\]

かつ保持領域の短辺長は

\[
U^{\sigma/2}
\ge
\exp\!\left(\frac12\sqrt L\right)
\]

となる。

## 3. visibility divisor の small/large 分割

偶奇条件によって \(v,w\) が同時に偶数である場合を除外した後、

\[
\mathbf 1_{(v,w)=1}
=
\sum_{\substack{d\mid v,w\\d\ {\rm odd}}}\mu(d).
\]

また \((v,c)=(w,b)=1\) より、寄与する \(d\) は

\[
(d,bc)=1
\]

を満たす。

一つの slice で \(v\le V,w\le W\) とすると、

\[
\sum_{d>D}
\left\lfloor\frac Vd\right\rfloor
\left\lfloor\frac Wd\right\rfloor
\le
VW\sum_{d>D}\frac1{d^2}
\le
\frac{VW}{D-1}.
\]

保持領域の短辺を \(H\) とし、

\[
D=H^{1/2}
\]

とすれば、large-\(d\) tail は \(O(H^{-1/2})\) 比率となり、small-\(d\) 側でも除算後の短辺は \(H^{1/2}\) 以上残る。

この分割は、少なくとも exponent budget 上では large visibility divisor を主項より低次へ追い出す。

## 4. 周期統合による isotropization

\(d\) を奇数、\((d,bc)=1\) とし、

\[
v=dm,\qquad w=dn,
\qquad
x=bdm,\qquad y=cdn
\]

と置く。

### 4.1 odd-odd class

\(m\) が奇数かつ \((m,c)=1\) である条件は、法 \(2c\) の unit residue と同じである。その Fourier coefficient は Ramanujan sum

\[
c_{2c}(k).
\]

同様に \(n\) 側は \(c_{2b}(\ell)\) である。

\(x\) の物理周期は

\[
bd(2c)=2bcd,
\]

\(y\) の物理周期も

\[
cd(2b)=2bcd.
\]

### 4.2 opposite-parity classes

\(m\) が偶数かつ \((m,c)=1\) の Fourier coefficient は

\[
c_c(k),
\]

\(m\) が奇数の場合は \(c_{2c}(k)\) である。\(n\) 側も同様に \(c_b(\ell)\) または \(c_{2b}(\ell)\) となる。

いずれの parity class でも共通物理周期は

\[
Q=2bcd.
\]

### 4.3 Poisson formula

円 sector 上の滑らかな weight を \(W_R(x,y)\) とすると、一つの parity class は

\[
\frac1{Q^2}
\sum_{k,\ell\in\mathbb Z}
A_c(k)A_b(\ell)
\widehat W_R\!\left(\frac{k}{Q},\frac{\ell}{Q}\right)
\]

となる。ここで \(A_c,A_b\) は上記 Ramanujan coefficient である。

零周波数では

\[
A_c(0)=\varphi(c),\qquad
A_b(0)=\varphi(b)
\]

となり、odd-odd class と二つの opposite-parity class を合わせると、Stage12-N1-2f の2進局所因子が回収される。

### 4.4 意味

以前の表示では、半軸比 \(c/b\) の楕円族を一様に数える必要があった。周期統合後は、

- 幾何：固定された円 sector
- 双対分母：共通の \(Q=2bcd\)
- 算術：Ramanujan coefficients

へ分離される。

したがって eccentricity の困難は消滅したわけではないが、**幾何の変形問題から、Ramanujan 重み付き modulus-average 問題へ移動した**。

## 5. 双対位相

円弧境界へ stationary phase を適用すると、非零周波数の radial parameter は

\[
Z=
\frac{R}{Q}\sqrt{k^2+\ell^2}
\]

となり、位相は概略

\[
e(\pm Z).
\]

一方、

\[
R\asymp
\sqrt{\frac{B}{a}}\,u^{-1/2}
\]

なので、\(u\)-和の位相は

\[
e\!\left(
\pm
\frac{C\sqrt{k^2+\ell^2}}
{bcd\sqrt u}
\right)
\]

となる。

\[
S(U,A)=\sum_{u\asymp U}e(Au^{-1/2})
\]

に二階微分判定を適用すると、

\[
S(U,A)
\ll
A^{1/2}U^{-1/4}
+
A^{-1/2}U^{5/4}.
\]

\(Z=A/\sqrt U\) と書けば

\[
S(U,A)
\ll
Z^{1/2}+UZ^{-1/2}.
\]

したがって各周波数について \(Z\gg1\) なら相殺候補がある。ただし、この評価だけでは二次元周波数、Ramanujan coefficients、\(b,c,d\) 和を同時に加算できない。

## 6. 主項を三領域へ厳密分割

\(b\le c\) とし、

\[
y=\log b,\qquad
z=\log c,\qquad
t=\log\frac{B}{ac^2}
\]

と置く。\(d\) は subpower cutoff 内なので、leading logarithmic fraction には影響しない。

全形式的主項積分を \(L=1\) に正規化すると

\[
I_{\mathrm{all}}=\frac1{48}.
\]

### Zone A：separated two-dimensional core

\[
Q\le\sqrt R.
\]

leading log coordinates では

\[
y+\frac z2\le\frac t4.
\]

この積分は

\[
I_A=\frac3{512},
\qquad
\frac{I_A}{I_{\mathrm{all}}}
=\frac9{32}.
\]

### Zone B：clustered two-dimensional core

\[
\sqrt R<Q\le R.
\]

積分は

\[
I_B=\frac5{512},
\qquad
\frac{I_B}{I_{\mathrm{all}}}
=\frac{15}{32}.
\]

### Zone C：one-dimensional wing

\[
Q>R.
\]

積分は

\[
I_C=\frac1{192},
\qquad
\frac{I_C}{I_{\mathrm{all}}}
=\frac14=\frac8{32}.
\]

従って

\[
\frac9{32}+\frac{15}{32}+\frac8{32}=1.
\]

また二次元 Poisson core 全体 \(Q\le R\) は

\[
\frac9{32}+\frac{15}{32}
=\frac34
\]

を占める。

## 7. large sieve の適合範囲

\(u\asymp U\)、radial frequency \(\sqrt m\) とする。二つの modulus \(q,q'\) の位相差が \(u\)-block で識別されるには概略

\[
R\sqrt m
\left|\frac1q-\frac1{q'}\right|
\gtrsim1
\]

が必要である。

隣接する \(q\asymp Q\)、最低周波数 \(m=1\) では

\[
R\left|\frac1q-\frac1{q+1}\right|
\asymp
\frac{R}{Q^2}.
\]

したがって通常の spacing による large sieve が自然に働く境界は

\[
Q\lesssim\sqrt R.
\]

これは Zone A の \(9/32\) に一致する。

Zone B では二次元 Poisson 自体は oscillatory だが、低周波数で隣接 modulus が cluster する。必要なのは単純な separation ではなく、

- reciprocal frequencies の additive energy
- Ramanujan coefficient の二乗平均
- \(u^{-1/2}\) 位相の nonlinear large sieve
- radial multiplicity \(k^2+\ell^2=m\)

を同時に制御する評価である。

## 8. Kloosterman large sieve との違い

Deshouillers–Iwaniec 系や Drappeau の spectral large sieve は、真正の Kloosterman sum や modular inverse を含む kernel を利用する。

Bettin–Chandee 型の Kloosterman fraction も

\[
e\!\left(\frac{a\overline m}{n}\right)
\]

を対象とする。

今回の kernel は

\[
e\!\left(
\frac{C\sqrt{k^2+\ell^2}}
{bcd\sqrt u}
\right)
\]

であり、modular inverse が存在しない。このため既存定理は verbatim には適用できない。

ただし reciprocal denominator と多変数 monomial 構造はあるため、

- van der Corput
- exponent pair
- Robert–Sargos 型多変数 monomial estimate
- nonlinear large sieve

は次段階の候補となる。

Pliego の三変数 monomial sum の研究でも、dyadic parallelepiped に既存 monomial bound を機械的に適用するだけでは critical range で十分でない場合が明示されている。従って Stage12 でも parameter budget を個別に行う必要がある。

## 9. Zone C の処理方針

\(Q>R\) では、共通周期表示による二次元 Poisson は低周波数を多数含む。

この領域では元の anisotropic lattice に戻り、\(b\le c\) の長い \(v\) 方向だけを Poisson summation または sawtooth expansion する。

固定 \(w\) に対する \(v\) の上端は

\[
\frac1b
\min\!\left(
cw,\sqrt{R^2-c^2w^2}
\right).
\]

局所条件 \((v,c)=1\) を周期展開すると、概略

\[
e\!\left(
\frac{k}{bc d}
\min\!\left(
cdw,\sqrt{R^2-c^2d^2w^2}
\right)
\right)
\]

型の一変数曲線位相になる。

これは Zone B の radial reciprocal phase と異なるため、別の exponent-pair budget が必要である。

## 10. 結論

Stage12-N1-2h で次が閉じた。

1. shallow height、terminal \(u\)、large visibility divisor を \(o(\mathrm{main})\) にする cutoff architecture。
2. parity と局所 coprimality を統合した共通正方周期 \(Q=2bcd\)。
3. Ramanujan Fourier coefficients の厳密式。
4. 主項の \(9/32\)、\(15/32\)、\(1/4\) 分割。
5. large-sieve spacing barrier \(Q=\sqrt R\)。
6. Poisson 後に必要となる具体的 nonlinear exponential sum。

未解決は次の二領域である。

- \(15/32\) の clustered two-dimensional core
- \(1/4\) の one-dimensional wing

次は Stage12-N1-2i として、

- Ramanujan sum の二乗平均
- \(u^{-1/2}\) に対する exponent pair
- radial frequency multiplicity
- Zone C の一変数曲線和

を指数予算へ代入し、raw 誤差

\[
O\!\left(B(\log B)^{2-\eta}\right)
\]

または \(B\) の冪節約に届くかを判定する。

## 文献

- Luca Brandolini and Giancarlo Travaglini, *Fourier analytic techniques for lattice point discrepancy*, arXiv:1909.03439.
- Sary Drappeau, *Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method*, arXiv:1504.05549.
- Sandro Bettin and Vorrapan Chandee, *Trilinear forms with Kloosterman fractions*, arXiv:1502.00769.
- Javier Pliego, *Estimates for a three-dimensional exponential sum with monomials*, arXiv:2211.02096.
