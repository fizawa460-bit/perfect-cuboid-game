# Stage12-N1-3j：weighted l1 Euler product と vertical growth の最終明示化

> **STATUS:** `FINAL_SELF_CONTAINMENT_DETAIL_CLOSED_IN_TEXT`
>
> **SCOPE:** Stage12-N1-2 primitive oriented count
>
> **PARENT:** `docs/stage12-n1-3i-final-reference-closure.md`
>
> **THEOREM_STATUS:** `SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL`

## 0. 目的

Stage12-N1-3i は、旧2pへの active dependency を除き、

\[
B_\beta(X)\ll X
\]

および coprime cross correction の

\[
M_\delta
:=
\sum_{a,b\ge1}
\frac{|c(a,b)|}{(ab)^{1/2+\delta}}
<\infty
\]

を現行定義から導いた。

その後の外部再検算は、3i §2.1--§2.2 の局所代数と

\[
\|C_q-1\|_\delta\ll_\delta q^{-1-2\delta}
\]

を独立に再計算して一致を確認した。一方、

```text
sum_q ||C_q-1||_delta < infinity
    =>
coefficient weighted l1 norm of prod_q C_q is finite
```

の最終移行が標準的事実として一文で処理されていた。また 3i §3 の vertical-growth 記述について、functional equation を使う対象が `L(s,chi_4)` であり `J_beta` ではないことを、同じ active text 内でさらに明示できる。

本稿はこの二点だけを補う。新しい解析的入力や新しい主項計算は導入しない。

---

## 1. 二変数 weighted l1 Dirichlet algebra

固定

\[
\sigma_\delta:=\frac12+\delta,
\qquad \delta>0
\]

とする。二変数算術関数

\[
f:\mathbf N^2\to\mathbf C
\]

に対し

\[
\|f\|_\delta
:=
\sum_{m,n\ge1}
\frac{|f(m,n)|}{(mn)^{\sigma_\delta}}
\]

と置く。

二変数 Dirichlet convolution を

\[
(f*g)(m,n)
:=
\sum_{ad=m}\sum_{be=n}f(a,b)g(d,e)
\]

で定義する。

### 補題 3j.1（劣乗法性）

\[
\boxed{
\|f*g\|_\delta
\le
\|f\|_\delta\,\|g\|_\delta.
}
\]

### 証明

Tonelli の定理を非負級数に適用すると

\[
\begin{aligned}
\|f*g\|_\delta
&=
\sum_{m,n\ge1}
\frac1{(mn)^{\sigma_\delta}}
\left|
\sum_{ad=m}\sum_{be=n}f(a,b)g(d,e)
\right|\\
&\le
\sum_{a,b,d,e\ge1}
\frac{|f(a,b)|\,|g(d,e)|}
{(abde)^{\sigma_\delta}}\\
&=
\left(
\sum_{a,b\ge1}
\frac{|f(a,b)|}{(ab)^{\sigma_\delta}}
\right)
\left(
\sum_{d,e\ge1}
\frac{|g(d,e)|}{(de)^{\sigma_\delta}}
\right).
\end{aligned}
\]

よって主張を得る。\(\square\)

また写像

\[
f(m,n)
\longmapsto
\frac{f(m,n)}{(mn)^{\sigma_\delta}}
\]

によりこの空間は通常の \(\ell^1(\mathbf N^2)\) と等長同型である。従って \(\|\cdot\|_\delta\) に関して完備である。

---

## 2. 局所 Euler factors から global coefficient norm へ

3i §2 の exact local factor を使う。

\[
C_q(s_1,s_2)
=1-V_q(s_1)V_q(s_2)
=:1+E_q(s_1,s_2)
\]

と書く。3i §2.2 で既に

\[
\boxed{
\eta_q
:=
\|E_q\|_\delta
\ll_\delta q^{-1-2\delta}
}
\]

が得られているので

\[
\sum_{q\equiv1(4)}\eta_q<\infty.
\]

有限素数集合 \(Q\) に対し

\[
P_Q:=\prod_{\substack{q\le Q\\q\equiv1(4)}}(1+E_q)
\]

を二変数 Dirichlet convolution product として解釈する。

補題3j.1から

\[
\|P_Q\|_\delta
\le
\prod_{q\le Q}(1+\eta_q)
\le
\exp\left(\sum_q\eta_q\right).
\]

従って有限積のノルムは一様有界である。

さらに \(Q'<Q''\) なら

\[
P_{Q''}
=
P_{Q'}*
\prod_{Q'<q\le Q''}(1+E_q),
\]

よって

\[
\begin{aligned}
\|P_{Q''}-P_{Q'}\|_\delta
&\le
\|P_{Q'}\|_\delta
\left\|
\prod_{Q'<q\le Q''}(1+E_q)-1
\right\|_\delta\\
&\le
\exp\left(\sum_q\eta_q\right)
\left\{
\prod_{Q'<q\le Q''}(1+\eta_q)-1
\right\}.
\end{aligned}
\]

尾部和 \(\sum_{q>Q'}\eta_q\to0\) なので右辺は \(Q'\to\infty\) で0へ行く。従って \((P_Q)\) は \(\|\cdot\|_\delta\) に関する Cauchy 列であり、完備性からある二変数係数列 \(c(a,b)\) へ収束する。

各固定 \((a,b)\) の係数は、\(ab\) を割る有限個の素数しか関与しないため、十分大きい \(Q\) で安定する。従ってこの \(\ell^1\)-極限の Dirichlet series は、係数ごとにも analytic Euler product

\[
C(s_1,s_2)=\prod_{q\equiv1(4)}C_q(s_1,s_2)
\]

と一致する。

したがって

\[
\begin{aligned}
M_\delta
&=
\sum_{a,b\ge1}
\frac{|c(a,b)|}{(ab)^{1/2+\delta}}\\
&=
\|c\|_\delta\\
&\le
\prod_q(1+\eta_q)\\
&\le
\exp\left(\sum_q\eta_q\right)
<\infty.
\end{aligned}
\]

すなわち

\[
\boxed{
M_\delta<\infty
\qquad(\delta>0)
}
\]

の3i §2 最終ステップは、外部 Banach-algebra 定理を引用せず本文内で閉じる。

特に3aが使用する \(M_{2\varepsilon}\) はこの補題の直接の特殊例である。

---

## 3. vertical growth の対象を明示的に分離する

3iで用いる analytic factor は

\[
H_\beta(s)
=
L(s,\chi_4)J_\beta(s).
\]

ここで **functional equation を使うのは \(L(s,\chi_4)\) だけであり、\(J_\beta\) に functional equation を仮定しない。**

### 3.1 `J_beta`

3i §1.1 の局所評価

\[
|J_{\beta,q}(s)-1|
\ll
q^{-1-\sigma}+q^{-2\sigma}
\]

および \(p\equiv3\pmod4\) での \(O(p^{-2\sigma})\) から、任意の固定 \(\varepsilon>0\) に対し

\[
\sigma\ge\frac12+\varepsilon
\]

で Euler product は \(t\) に一様な majorant により絶対収束する。従ってその閉半平面上で

\[
\boxed{
J_\beta(\sigma+it)
\ll_\varepsilon 1.
}
\]

この有界性には functional equation、Stirling formula、Phragmen--Lindelof のいずれも不要である。

### 3.2 `L(s,chi_4)`

一方、非主 primitive Dirichlet L-function \(L(s,\chi_4)\) については、その標準 functional equation を用いる。

任意の固定 \(\varepsilon>0\) に対し、右境界 \(\sigma=1+\varepsilon\) では Dirichlet series の絶対収束から一様有界である。左境界 \(\sigma=-\varepsilon\) では functional equation と Stirling formula により、右半平面の有界値へ移して

\[
L(-\varepsilon+it,\chi_4)
\ll_\varepsilon
(1+|t|)^{A_\varepsilon}
\]

を得る。Phragmen--Lindelof を固定 strip

\[
-\varepsilon\le\sigma\le1+\varepsilon
\]

へ適用すれば

\[
\boxed{
L(\sigma+it,\chi_4)
\ll_\varepsilon
(1+|t|)^{A_\varepsilon}
}
\]

となる。指数の最適値は不要である。

### 3.3 `H_beta`

Selberg--Delangeで必要な領域は \(s=1\) に接する領域であり、十分小さい固定 \(c_0>0\) を選べば

\[
\sigma>
1-\frac{c_0}{\log(2+|t|)}
\]

は \(\sigma>1/2+\varepsilon\) の範囲に含められる。そこでは3.1と3.2を掛け合わせて

\[
\boxed{
H_\beta(\sigma+it)
\ll_\varepsilon
(1+|t|)^{A_\varepsilon}.
}
\]

従って vertical polynomial-growth 条件は

```text
J_beta: absolute convergence => bounded
L(s,chi_4): functional equation + Stirling + Phragmen--Lindelof => polynomial growth
H_beta=L*J_beta: product => polynomial growth
```

という三段階で、誤解なく自己完結に確認される。

---

## 4. 3i・3aへの適用

この補修により、3i §2 の

```text
sum_q local weighted l1 norm < infinity
=> global coefficient weighted l1 norm < infinity
```

は補題3j.1と有限積 Cauchy 論法で完全に展開された。

また3i §3のvertical-growth入力は、`J_beta` の有界性と `L(s,chi_4)` のfunctional equation由来のgrowthを明確に分離した。

従って3aのrectangle proofで必要な

\[
B_\beta(X)\ll X,
\qquad
M_{2\varepsilon}<\infty,
\]

およびfinite-order Selberg--Delangeのanalytic-factor growthは、published Selberg--Delange theoremそのものを除いてactive text内で追跡できる。

---

## 5. 最終状態

```text
WEIGHTED_L1_DIRICHLET_SUBMULTIPLICATIVITY=CLOSED_BY_STAGE12_N1_3J
EULER_PRODUCT_TO_GLOBAL_WEIGHTED_L1=CLOSED_BY_STAGE12_N1_3J
J_BETA_VERTICAL_BOUND=ABSOLUTE_CONVERGENCE_ONLY
L_CHI4_VERTICAL_BOUND=FUNCTIONAL_EQUATION_STIRLING_PL
H_BETA_VERTICAL_BOUND=CLOSED_BY_STAGE12_N1_3J
J_BETA_FUNCTIONAL_EQUATION_ASSUMED=false
OLD_2P_ACTIVE_DEPENDENCY=NONE
SELBERG_DELANGE_THEOREM=EXTERNAL_PUBLISHED_THEOREM_LEVEL_INPUT
NEW_CENTRAL_MATHEMATICAL_GAP=NONE_IDENTIFIED
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
THEOREM_SCOPE=PRIMITIVE_ORIENTED_COUNT_ONLY
```

この修正は主項係数、局所因子、rectangle指数、radial transfer、shallow sector、small-coordinate wing、最終誤差予算を変更しない。
