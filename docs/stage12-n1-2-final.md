# Stage12-N1-2 Final：primitive oriented count の漸近式

## 0. 主張範囲

本稿は、Stage12-N1-2 系列で定義した primitive oriented count `C_prim(B)` の漸近式をまとめた完成稿である。完全直方体の存在、`N_1` 全体、または別の exact-multiplicity count への自動変換は主張しない。

## 定理

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\qquad(B\to\infty).
\]

ここで `κ` は Stage12-N1-2f〜2k で確定した primitive oriented count の Euler 積定数である。

---

## 1. primitive-first reduction

共有面対角線の双曲線座標化により

\[
p=hrs,
\qquad
c=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\]

\[
1\le r<s,\qquad (r,s)=1,\qquad h(r^2+s^2)\le2B
\]

を得る。global Möbius 反転を最初に処理する primitive-first reindexing により、外側平均で増幅される boundary layer を除去する。

固定された coprime pair `(r,s)` に対する height 部分和は

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1+R_{r,s}(X),
\]

\[
\gamma(n)=\frac1\pi\sum_{d\mid n}\beta(d).
\]

odd–odd と opposite-parity の差は height 上限係数と 2-adic 前置因子に吸収される。

---

## 2. fixed-circle reduction と局所定数

primitive-first の主項は概略

\[
B\sum_{r<s\atop(r,s)=1}
\frac{\gamma(rs)}{r^2+s^2}
\]

へ帰着する。fixed-circle remainder は Stage12-N1-2k の評価を用いる。

二法 Euler 定数を `η` とすると、各奇素数で

\[
\frac{\eta_p}{\kappa_p}=(1-p^{-2})^{-1},
\]

archimedean・2-adic 前置因子比は `8/π` である。したがって

\[
\frac{\eta}{\kappa}
=
\frac8\pi
\prod_{p\ {m odd}}(1-p^{-2})^{-1}
=
\frac8\pi\cdot\frac{\pi^2}{8}
=
\pi,
\]

すなわち

\[
\eta=\pi\kappa.
\]

---

## 3. 多変数定理を使わない一変数化

未検証の de la Bretèche 直接適用は使用しない。代わりに

\[
\beta(q^j)=\frac{2(q-1)}{q+1}
\quad(q\equiv1\pmod4,\ j\ge1)
\]

で定める乗法関数の一変数級数

\[
B_\beta(s)=\sum_{n\ge1}\frac{\beta(n)}{n^s}
\]

を用いる。局所因子は

\[
A_q(s)=1+\frac{b_q q^{-s}}{1-q^{-s}},
\qquad b_q=\frac{2(q-1)}{q+1}.
\]

`x=q^{-s}` とすると

\[
A_q(s)=\frac{1+(b_q-1)x}{1-x}.
\]

よって

\[
B_\beta(s)=\zeta(s)L(s,\chi_4)J(s).
\]

`q≡1 (mod 4)` では

\[
J_q(s)=(1-x)(1+(b_q-1)x),
\]

`p≡3 (mod 4)` では

\[
J_p(s)=1-p^{-2s}.
\]

さらに

\[
J_q(s)-1
=O(q^{-1-\sigma})+O(q^{-2\sigma}),
\qquad \sigma=\Re s.
\]

したがって任意の固定 `ε>0` に対し、`Re s>1/2+ε` で Euler 積 `J(s)` は局所一様絶対収束し、正則かつ非零である。

Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Third Edition, Chapter II.5, Theorem II.5.2 の `z=1` 特殊形を適用して

\[
B_\beta(X):=\sum_{n\le X}\beta(n)
=c_\beta X+O(XE(X)),
\]

\[
E(X)=
\exp\{-c(\log X)^{3/5}(\log\log X)^{-1/5}\}
\]

を得る。暗黙定数は `X` に依存しない。

---

## 4. coprime correction と一様長方形補題

\[
f(r,s)=\beta(r)\beta(s)1_{(r,s)=1}
\]

に対する二変数級数は

\[
F(s_1,s_2)
=B_\beta(s_1)B_\beta(s_2)C(s_1,s_2)
\]

と分解される。局所的に

\[
C_q(s_1,s_2)-1
=O(q^{-\sigma_1-\sigma_2}),
\]

したがって任意の固定 `δ∈(0,1/4)` に対し

\[
M_\delta:=
\sum_{a,b\ge1}
\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty.
\]

長方形和

\[
S(R,S)=
\sum_{r\le R}\sum_{s\le S}
\beta(r)\beta(s)1_{(r,s)=1}
\]

は

\[
S(R,S)=
\sum_{a\le R,b\le S}
c(a,b)B_\beta(R/a)B_\beta(S/b)
\]

と書ける。`A=R^{1/2}`, `D=S^{1/2}` とし、

\[
(a\le A,b\le D),
(a>A,b\le D),
(a\le A,b>D),
(a>A,b>D)
\]

の四領域へ分割する。

小係数領域では一変数誤差を `E_*(R^{1/2})`, `E_*(S^{1/2})` で一様化する。大係数領域では

\[
B_\beta(X)\ll X\log(2X)
\]

と `M_δ` を用いる。これにより

\[
\boxed{
S(R,S)=\mathfrak C RS
+O_\delta\!\left(
RS\{E_*(R^{1/2})+E_*(S^{1/2})\}
+R^{1/2+\delta}S
+RS^{1/2+\delta}
\right)
}
\]

を得る。ここで

\[
\mathfrak C=c_\beta^2C(1,1).
\]

暗黙定数は `R,S` に一様である。

---

## 5. 結合領域への移送

対数変数

\[
y=\log r,
\qquad z=\log s,
\qquad L=\log B
\]

を用いる。height の主項長さは

\[
\Phi_L(y,z)=\bigl(L-2\max(y,z)\bigr)_+
\]

で表される。

retained regionを固定比の対数dyadic boxesへ分割する。各boxで `r^2+s^2` はbox scaleと定数倍で比較でき、`Φ_L` の全変動は `O(1)` である。二変数 Abel／Stieltjes 部分和分を各boxへ適用すると、長方形主項は

\[
\int_{y,z\ge0\atop2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=
\frac{L^3}{12}
\]

へ移送される。

retained regionでは

\[
\min(R,S)
\ge
\exp\{\tfrac12(\log B)^{1/4}\},
\qquad R,S\ll B^{1/2}.
\]

したがって長方形誤差は、polylogarithmically many boxesを合計しても

\[
o(BL^3)
\]

である。

---

## 6. 境界項

shallow領域は `τ=L^{-3/4}` として

\[
O(BL^{3/2+o(1)}).
\]

対角・円弧境界は全dyadic scaleを合計して

\[
O(BL^{2+o(1)}).
\]

floor endpoint は安全側に

\[
O(BL^{1+o(1)}).
\]

いずれも `o(BL^3)` である。parityは primitive-first の2-adic bookkeepingにより主定数へ正確に吸収される。

---

## 7. 定理の証明

Sections 1–6により、primitive oriented count の主項は二法定数 `η` と正規化対数体積 `1/12` を用いて

\[
C_{\rm prim}(B)
\sim
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

`η=πκ` を代入すると

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3.
\]

これで定理が従う。\(\square\)

---

## 8. 監査履歴

詳細な導出・有限監査・修復履歴は既存の Stage12-N1-2j〜2p および review R03〜R05 に保存する。本稿を今後の標準参照文書とする。
