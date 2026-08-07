# Stage12-N1-3g：fixed-height shallow sector の直接評価

> **STATUS:** `R05_FIXED_HEIGHT_SHALLOW_SECTOR_CLOSED_IN_TEXT`
>
> **SOURCE_AUDIT:** Stage12-N1-2 全体ゼロベース監査 R05
>
> **SCOPE:** primitive-first exact sum の fixed-height shallow sector
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_R06_FULL_REAUDIT`

## 0. 修正対象

`L=\log B` とし

\[
X_0:=\exp(L^{1/4}),
\qquad
X_{r,s}:=\frac{\lambda(r,s)B}{r^2+s^2},
\]

\[
\lambda(r,s)=
\begin{cases}
2,&r,s\text{ odd},\\
1,&r,s\text{ opposite parity}
\end{cases}
\]

とする。

R05監査は、retained sector `X_{r,s}\ge X_0` のfixed-height remainderは閉じている一方、

\[
1\le X_{r,s}<X_0
\]

となるshallow sectorについて、旧Finalが

```text
shallow fixed-height sector: o(BL^3) by nonnegative rectangle upper bounds
```

と結論だけを書き、必要なmajorantとshell計算を展開していないことを指摘した。

本稿ではshallow contributionをexact primitive-first和から直接上から押さえ、

\[
O(BL^{5/2})=o(BL^3)
\]

を示す。

---

## 1. exact shallow contribution

primitive-first formulaは

\[
C_{\rm prim}(B)
=
\sum_{1\le r<s\atop(r,s)=1}
\sum_{m\le X_{r,s}}A_{r,s}(m).
\]

shallow partを

\[
\mathcal S_{\rm sh}(B)
:=
\sum_{\substack{1\le r<s,(r,s)=1\\1\le X_{r,s}<X_0}}
\sum_{m\le X_{r,s}}A_{r,s}(m)
\]

と定義する。上限は整数部分を意味する。

Stage12-N1-2のexact formulaより

\[
A_{r,s}(1)=G(rs)-1\ge0,
\]

また `m>1` では、`m` の全素因数が `1 mod 4` の場合に

\[
A_{r,s}(m)
=
G(rs)
\prod_{p\mid m}
\frac{2}{2v_p(rs)+1},
\]

それ以外では0である。従って全ての `m\ge1` について

\[
\boxed{
0\le A_{r,s}(m)
\le
G(rs)2^{\omega(m)}.
}
\]

ここで `\omega(m)` は異なる素因数の個数である。

---

## 2. height coefficient のsummatory majorant

恒等式

\[
2^{\omega(m)}
=
\sum_{d\mid m}\mu^2(d)
\]

から、`X\ge1` に対して

\[
\begin{aligned}
\sum_{m\le X}2^{\omega(m)}
&=
\sum_{d\le X}\mu^2(d)
\left\lfloor\frac Xd\right\rfloor\\
&\le
X\sum_{d\le X}\frac1d\\
&\ll X\log(2X).
\end{aligned}
\]

従って

\[
\boxed{
\sum_{m\le X}A_{r,s}(m)
\ll
G(rs)X\log(2X)
}
\]

が `r,s,X` に一様に成り立つ。

shallow sectorでは `X_{r,s}<X_0` なので

\[
\sum_{m\le X_{r,s}}A_{r,s}(m)
\ll
G(rs)X_{r,s}\log(2X_0).
\]

---

## 3. `G` の一変数平均

\[
G(n)
=
\prod_{\substack{q\mid n\\q\equiv1(4)}}(2v_q(n)+1)
\]

のDirichlet seriesを

\[
\mathcal G(s)
:=
\sum_{n\ge1}\frac{G(n)}{n^s}
\]

とする。

prime-power local factorsは

\[
\sum_{a\ge0}G(p^a)x^a
=
\frac1{1-x}
\qquad(p=2\text{ or }p\equiv3(4)),
\]

\[
\sum_{a\ge0}G(q^a)x^a
=
\sum_{a\ge0}(2a+1)x^a
=
\frac{1+x}{(1-x)^2}
\qquad(q\equiv1(4)).
\]

従ってprime by primeに

\[
\boxed{
\mathcal G(s)
=
\zeta(s)^2L(s,\chi_4)E_G(s),
}
\]

\[
E_G(s)
=
(1-2^{-s})
\prod_{p\text{ odd}}(1-p^{-2s}).
\]

`E_G` は `\Re s>1/2` で絶対収束し、`s=1` の近傍で正則である。既に固定した `z=2` Selberg--Delange input、またはその非負係数上界形により

\[
\boxed{
M_G(Y)
:=
\sum_{n\le Y}G(n)
\ll
Y\log(2Y).
}
\]

必要なのはこのupper boundだけであり、leading constantは使用しない。

---

## 4. weighted radial shell bound

`Q\ge1` に対し

\[
\Sigma_G(Q)
:=
\sum_{\substack{r,s\ge1\\Q<r^2+s^2\le2Q}}
G(r)G(s).
\]

shellを正方形に含めると

\[
\begin{aligned}
\Sigma_G(Q)
&\le
\left(
\sum_{n\le\sqrt{2Q}}G(n)
\right)^2\\
&\ll
Q\{\log(2Q)\}^2.
\end{aligned}
\]

よって

\[
\boxed{
\sum_{\substack{r,s\ge1\\Q<r^2+s^2\le2Q}}
\frac{G(r)G(s)}{r^2+s^2}
\ll
\{\log(2Q)\}^2.
}
\]

coprimality、orientation、parity条件を外した上界なので、元のshallow sumにも適用できる。

---

## 5. shallow radial annulus

shallow pointでは

\[
1\le X_{r,s}<X_0.
\]

`1\le\lambda(r,s)\le2` なので

\[
\frac{B}{X_0}
<
r^2+s^2
\le
2B.
\]

このannulusは

\[
O(1+\log X_0)
\]

個のdyadic radial shellsで被覆できる。

Section 4のshell boundを合計し、`r^2+s^2\le2B` 上で `\log(2Q)\ll L` を用いると

\[
\boxed{
\sum_{\substack{1\le r<s,(r,s)=1\\1\le X_{r,s}<X_0}}
\frac{\lambda(r,s)G(rs)}{r^2+s^2}
\ll
L^2\log(2X_0).
}
\]

ここで `(r,s)=1` なら `G(rs)=G(r)G(s)` であり、上界では `\lambda\le2`、coprimality、orientationを外した。

---

## 6. shallow contribution の完結評価

Section 2より

\[
\begin{aligned}
\mathcal S_{\rm sh}(B)
&\ll
\sum_{\rm shallow}
G(rs)X_{r,s}\log(2X_0)\\
&=
B\log(2X_0)
\sum_{\rm shallow}
\frac{\lambda(r,s)G(rs)}{r^2+s^2}.
\end{aligned}
\]

Section 5を代入して

\[
\boxed{
\mathcal S_{\rm sh}(B)
\ll
B L^2\{\log(2X_0)\}^2.
}
\]

`X_0=\exp(L^{1/4})` なので

\[
\log(2X_0)\ll L^{1/4},
\]

従って

\[
\boxed{
\mathcal S_{\rm sh}(B)
\ll
B L^{5/2}
=
o(BL^3).
}
\]

これはodd--odd branchとopposite-parity branchを同時に含む一様評価である。

---

## 7. retained / shallow と radial core / wing の独立性

二つの分割を混同しない。

1. **fixed-height retained/shallow split**
   \[
   X_{r,s}\ge X_0
   \quad\text{or}\quad
   1\le X_{r,s}<X_0.
   \]
   retained remainderは3e、shallow exact contributionは本3gで処理する。

2. **radial core/wing split**
   \[
   r,s\ge U
   \quad\text{or}\quad
   \min(r,s)<U,
   \qquad
   U=\exp(\tfrac12L^{1/4}).
   \]
   これはresidue mainのradial Stieltjes transferを3fで処理するための別分割である。

3gは3fのwing estimateをshallow estimateとして流用せず、primitive-first exact sumを直接評価している。

---

## 8. final error budget への組込み

fixed-height部分は

\[
\sum_{r,s}
\sum_{m\le X_{r,s}}A_{r,s}(m)
\]

を次に分ける。

- retained main residue;
- retained remainder：`o(BL^{-A})`、3e;
- shallow exact contribution：`O(BL^{5/2})`、3g;
- constant `-1`、floor、endpoint：既存評価。

従ってfixed-height全領域について

\[
C_{\rm prim}(B)
=
\mathcal M(B)+o(BL^3)
\]

のnonresidue error budgetが文書内で閉じる。

radial residue mainは3fのcore/wing transferにより

\[
\mathcal M(B)
\sim
\frac{\kappa}{12\pi}BL^3.
\]

本稿は主係数、Euler factors、radial係数 `\pi/48`、orientation factor、最終係数 `1/12` を変更しない。

---

## 9. closure codes

```text
R05_MAJOR_01_FIXED_HEIGHT_SHALLOW=CLOSED_BY_STAGE12_N1_3G
A_RS_NONNEGATIVE_MAJORANT=PROVED
SUM_2OMEGA=O(X_LOG_X)=PROVED
G_ONE_VARIABLE_MEAN=O(Y_LOG_Y)=PROVED
WEIGHTED_RADIAL_SHELL=O((LOG_Q)^2)=PROVED
SHALLOW_ANNULUS_SHELL_COUNT=O(LOG_X0)=PROVED
FIXED_HEIGHT_SHALLOW_BOUND=O(B_L^(5/2))=PROVED
FIXED_HEIGHT_SHALLOW=o(B_L^3)=PROVED
MAIN_CONSTANT_CHANGED=false
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_R06_FULL_REAUDIT
```
