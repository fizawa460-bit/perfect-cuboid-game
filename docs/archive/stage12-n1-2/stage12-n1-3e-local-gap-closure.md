# Stage12-N1-3e：R02限定レビューで残った二つの局所補題

> **STATUS:** `R02_LOCAL_GAPS_CLOSED_IN_TEXT`
>
> **PARENT_BUNDLE:** `PC-N1-2-REPAIRED-PROOF-20260807-R02`
>
> **SCOPE:** fixed-circle outer average and parity-weighted local constant only
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_LIMITED_REAUDIT`

## 0. 目的

R02修正箇所限定レビューは、中心経路を否定せず、次の二点をself-contained bundleへ明示するよう要求した。

1. fixed-circle pointwise remainderをretained `(r,s)` regionで平均する補題;
2. parity-weighted rectangle coefficient
   \[
   C_\lambda^{(0)}=\frac{8}{\pi^2}\eta
   \]
   のprime-by-prime局所因子計算。

本稿はこの二点だけを定義から書き下す。新しい中心方針、fixed-`(b,c)` kernel lemma、または強いpointwise savingは導入しない。

---

# Part I. fixed-circle remainderのouter average

## 1. `G`, `H_abs`, `W` の完全な定義

`n>=1` に対して

\[
G(n)
:=
\prod_{\substack{q^t\Vert n\\q\equiv1\pmod4}}
(2t+1).
\]

固定pairに現れるfinite Euler correctionの絶対 `1/2`-normを、整数変数で

\[
H_{\rm abs}(n)
:=
\prod_{\substack{q^t\Vert n\\q\equiv1\pmod4}}
\left(
1+
\frac{4t}{(2t+1)(\sqrt q-1)}
\right)
\]

と定義する。空積は1である。

さらに

\[
\boxed{W(n):=G(n)H_{\rm abs}(n)}
\]

と置く。`W` は非負乗法関数であり、prime powersでは

\[
W(p^t)=1
\qquad(p=2\text{ or }p\equiv3\pmod4),
\]

\[
\boxed{
W(q^t)
=(2t+1)+\frac{4t}{\sqrt q-1}
}
\qquad(q\equiv1\pmod4).
\]

従って `(r,s)=1` なら

\[
W(rs)=W(r)W(s).
\]

Stage12-N1-3bのpointwise estimateはこの記号で

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(W(rs)X^{1/2}\right)
\]

である。

---

## 2. 一変数平均のEuler分解

Dirichlet級数を

\[
\mathcal W(s)
:=
\sum_{n\ge1}\frac{W(n)}{n^s}
\qquad(\Re s>1)
\]

とする。

### 2.1 `p=2` または `p congruent 3 mod 4`

`x=p^{-s}` とすると

\[
\mathcal W_p(s)
=\sum_{t\ge0}x^t
=\frac1{1-x}.
\]

### 2.2 `q congruent 1 mod 4`

`x=q^{-s}` とすると

\[
\begin{aligned}
\mathcal W_q(s)
&=1+\sum_{t\ge1}
\left(2t+1+\frac{4t}{\sqrt q-1}\right)x^t\\
&=
\frac{1+x+4x/(\sqrt q-1)}{(1-x)^2}.
\end{aligned}
\]

これを

\[
\boxed{
\mathcal W(s)=\zeta(s)^2L(s,\chi_4)E_W(s)
}
\]

と分解する。局所補正は

\[
E_{W,2}(s)=1-2^{-s},
\]

\[
E_{W,p}(s)=1-p^{-2s}
\qquad(p\equiv3\pmod4),
\]

\[
E_{W,q}(s)
=(1-q^{-s})
\left(
1+q^{-s}+\frac{4q^{-s}}{\sqrt q-1}
\right)
\qquad(q\equiv1\pmod4).
\]

最後の因子について、`sigma=Re s` とすると

\[
E_{W,q}(s)-1
=O(q^{-\sigma-1/2})+O(q^{-2\sigma}).
\]

従って任意の固定 `delta>0` に対して、Euler積

\[
E_W(s)=\prod_p E_{W,p}(s)
\]

は `Re s>=1/2+delta` の局所コンパクト集合上で絶対かつ局所一様に収束する。有限個の小素数を分離すれば `(s=1)` の近傍で正則かつ非零である。

よって、Stage12-N1-3dで固定したSelberg--Delangeの `z=2` 特殊形を適用でき、ある定数 `c_W>0,d_W` に対して

\[
\sum_{n\le T}W(n)
=T(c_W\log T+d_W)
+O_A\!\left(T(\log(2T))^{-A}\right)
\]

が任意の固定 `A>0` について成り立つ。以下に必要なのはその帰結

\[
\boxed{
M_W(T):=\sum_{n\le T}W(n)
\ll T\log(2T)
}
\]

だけである。

---

## 3. dyadic shell平均補題

### 補題 3e.1

すべての `Q>=2` に対して

\[
\boxed{
\sum_{\substack{r<s,\ (r,s)=1\\Q<r^2+s^2\le2Q}}
W(rs)
\ll Q(\log(2Q))^2
}
\]

が成り立つ。

### 証明

shell内では

\[
r,s\le(2Q)^{1/2}.
\]

また `(r,s)=1` なので `W(rs)=W(r)W(s)` である。非負性を用いてorientation、coprimality、shell条件を外すと

\[
\begin{aligned}
\sum_{\substack{r<s,(r,s)=1\\Q<r^2+s^2\le2Q}}W(rs)
&\le
\sum_{r,s\le(2Q)^{1/2}}W(r)W(s)\\
&=M_W((2Q)^{1/2})^2\\
&\ll Q(\log(2Q))^2.
\end{aligned}
\]

これで従う。`□`

---

## 4. retained regionでの総誤差

parity branchのheight係数を

\[
\lambda_{r,s}\in\{1,2\}
\]

とし、

\[
X_{r,s}
=\frac{\lambda_{r,s}B}{r^2+s^2}
\]

と置く。retained regionでは

\[
X_{r,s}\ge X_0,
\qquad
X_0=\exp((\log B)^{1/4}).
\]

従って

\[
r^2+s^2\le\frac{2B}{X_0}.
\]

`Y<r^2+s^2<=2Y` のshell上で、補題3e.1により

\[
\begin{aligned}
\sum_{\rm shell}W(rs)X_{r,s}^{1/2}
&\ll
\sqrt{\frac BY}
\sum_{\rm shell}W(rs)\\
&\ll
\sqrt{BY}(\log(2Y))^2.
\end{aligned}
\]

`Y` をdyadicに `2B/X_0` まで合計すると、幾何級数の最大shellが支配し、

\[
\boxed{
\sum_{\substack{r<s,(r,s)=1\\X_{r,s}\ge X_0}}
W(rs)X_{r,s}^{1/2}
\ll
BX_0^{-1/2}(\log B)^2
}
\]

を得る。

さらに

\[
X_0^{-1/2}
=\exp\!\left(-\frac12(\log B)^{1/4}\right)
\]

は任意の固定対数冪より速く減少する。従って任意の固定 `A>0` に対して

\[
\boxed{
BX_0^{-1/2}(\log B)^2
=o\!\left(B(\log B)^{-A}\right)
}
\]

である。これによりR02限定レビューの `OUTER_AVERAGE_LEMMA` は閉じる。

---

# Part II. `C_lambda^(0)=8 eta/pi^2` の局所因子計算

## 5. 係数と二変数級数

\[
g(n):=(1*\beta)(n)=\pi\gamma(n)
\]

とし、parity weightを

\[
\lambda(r,s)
:=1+\mathbf1_{r\text{ odd}}\mathbf1_{s\text{ odd}}
\]

と置く。

二変数係数とDirichlet級数を

\[
a_\lambda(r,s)
:=\lambda(r,s)g(r)g(s)\mathbf1_{(r,s)=1},
\]

\[
D_\lambda(s_1,s_2)
:=
\sum_{r,s\ge1}
\frac{a_\lambda(r,s)}{r^{s_1}s^{s_2}}
\]

とする。

一変数級数は

\[
G_g(s)
:=\sum_{n\ge1}\frac{g(n)}{n^s}
=\zeta(s)^2H_g(s),
\]

\[
H_g(s)=L(s,\chi_4)J_\beta(s).
\]

leading rectangle coefficientは

\[
\boxed{
C_\lambda^{(0)}
=H_g(1)^2C_\lambda(1,1)
}
\]

である。以下、`C_lambda` の局所因子を明示する。

---

## 6. odd-prime coprime correction

odd prime `p` に対して

\[
U_p(s):=\sum_{k\ge1}\frac{g(p^k)}{p^{ks}},
\qquad
G_{g,p}(s)=1+U_p(s).
\]

coprimalityにより、`p` は `r,s` の両方を割れないので

\[
\boxed{
D_{\lambda,p}(s_1,s_2)
=1+U_p(s_1)+U_p(s_2)
}
\]

である。従って

\[
\boxed{
C_{\lambda,p}(s_1,s_2)
=
\frac{1+U_p(s_1)+U_p(s_2)}
{(1+U_p(s_1))(1+U_p(s_2))}
}
\]

となる。

---

## 7. 2-adic parity factor

`g(2^k)=1` である。`x=2^{-s_1}`, `y=2^{-s_2}` とする。

- `v_2(r)=v_2(s)=0` ではodd--oddなのでweightは2;
- coprimalityにより、正の2進指数を持てるのは一方だけ;
- opposite parityではweightは1。

従って

\[
\boxed{
D_{\lambda,2}(s_1,s_2)
=2+\frac{x}{1-x}+\frac{y}{1-y}
}
\]

である。一変数local factorは

\[
G_{g,2}(s_i)=\frac1{1-2^{-s_i}}.
\]

よって

\[
\boxed{
C_{\lambda,2}(s_1,s_2)
=D_{\lambda,2}(s_1,s_2)(1-x)(1-y)
}
\]

であり、`x=y=1/2` を代入すると

\[
\boxed{C_{\lambda,2}(1,1)=1.}
\]

また `J_{\beta,2}(1)=1-2^{-1}=1/2` なので、2-adic contributionは

\[
\boxed{
J_{\beta,2}(1)^2C_{\lambda,2}(1,1)
=\frac14.
}
\]

---

## 8. `p congruent 3 mod 4`

この場合 `g(p^k)=1` である。`x=p^{-1}` とすると

\[
G_{g,p}(1)=\frac1{1-x},
\]

\[
D_{\lambda,p}(1,1)
=1+\frac{2x}{1-x}
=\frac{1+x}{1-x}.
\]

従って

\[
C_{\lambda,p}(1,1)
=
D_{\lambda,p}(1,1)(1-x)^2
=1-x^2
=1-p^{-2}.
\]

一方

\[
J_{\beta,p}(1)=1-p^{-2}.
\]

したがって、global factor `L(1,chi_4)^2` を前へ出した後のnormalized local contributionは

\[
\boxed{
J_{\beta,p}(1)^2C_{\lambda,p}(1,1)
=(1-p^{-2})^3.
}
\]

---

## 9. `q congruent 1 mod 4`

\[
b_q:=\frac{2(q-1)}{q+1},
\qquad x=q^{-1}.
\]

このとき

\[
g(q^k)=1+kb_q,
\]

\[
G_{g,q}(1)
=\sum_{k\ge0}(1+kb_q)x^k
=
\frac{1+(b_q-1)x}{(1-x)^2}.
\]

従って

\[
D_{\lambda,q}(1,1)
=2G_{g,q}(1)-1
=
\frac{q+1}{q-1}
\left(1+\frac{4q}{(q+1)^2}\right).
\]

また

\[
J_{\beta,q}(1)
=(1-x)(1+(b_q-1)x).
\]

`C_{lambda,q}=D_{lambda,q}/G_{g,q}^2` を使うと

\[
\begin{aligned}
J_{\beta,q}(1)^2C_{\lambda,q}(1,1)
&=(1-x)^6D_{\lambda,q}(1,1)\\
&=
(1-q^{-2})
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\end{aligned}
\]

従って

\[
\boxed{
J_{\beta,q}(1)^2C_{\lambda,q}(1,1)
=(1-q^{-2})\eta_q
}
\]

である。ここで

\[
\eta_q
:=
\left(1+\frac{4q}{(q+1)^2}\right)(1-q^{-1})^4.
\]

---

## 10. 全積

constant sheetの定義は

\[
\eta
=
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^2
\prod_{q\equiv1(4)}\eta_q.
\]

Sections 7--9を掛けると

\[
\begin{aligned}
C_\lambda^{(0)}
={}&
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^3\\
&\times
\prod_{q\equiv1(4)}(1-q^{-2})\eta_q.
\end{aligned}
\]

したがって

\[
C_\lambda^{(0)}
=
\eta
\prod_{\ell\text{ odd prime}}(1-\ell^{-2}).
\]

最後に

\[
\prod_{\ell\text{ odd prime}}(1-\ell^{-2})
=\frac{1}{(1-2^{-2})\zeta(2)}
=\frac8{\pi^2}.
\]

よって

\[
\boxed{
C_\lambda^{(0)}
=\frac8{\pi^2}\eta.
}
\]

これによりR02限定レビューの `PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY` は閉じる。

---

## 11. radial係数への接続

Stage12-N1-3c.Gで証明したfull-quadrant radial integralは

\[
\frac\pi{48}(\log B)^3.
\]

orientation `r<s` はその半分なので、harmonic mainは

\[
\frac12\cdot\frac\pi{48}\cdot
C_\lambda^{(0)}(\log B)^3
=
\frac\eta{12\pi}(\log B)^3.
\]

fixed-height residueの外側係数 `B/pi` を戻すと

\[
\frac\eta{12\pi^2}B(\log B)^3.
\]

さらに `eta=pi*kappa` から

\[
\frac\eta{12\pi^2}
=\frac\kappa{12\pi}.
\]

この節は新しいradial argumentではなく、上のlocal identityが既存の `1/12` 計算へ正しく接続することの確認である。

---

## 12. 判定

R02修正箇所限定レビューが要求した二つの局所補題について、

```text
OUTER_AVERAGE_LEMMA=CLOSED_BY_STAGE12_N1_3E_PART_I
PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY=CLOSED_BY_STAGE12_N1_3E_PART_II
R02_REMAINING_LOCAL_GAPS=NONE_IN_TEXT
CENTRAL_ROUTE_CHANGED=false
FIXED_BC_KERNEL_USED=false
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_LIMITED_REAUDIT
```

とする。

これは独立再監査の判定を先取りしない。R03 bundleでこの二点を限定再監査し、`CLOSED` が返った場合に限り、修正箇所限定レビューを閉じる。