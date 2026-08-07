# Stage12-N1-3f：small-coordinate wing の分離評価

> **STATUS:** `R04_SMALL_COORDINATE_WING_CLOSED_IN_TEXT`
>
> **SOURCE_AUDIT:** Stage12-N1-2 全体ゼロベース監査 R04
>
> **SCOPE:** radial Stieltjes transfer の error budget のみ
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_R05_FULL_REAUDIT`

## 0. 修正対象

R04全体ゼロベース監査は、retained condition

\[
X_{r,s}=\frac{\lambda(r,s)B}{r^2+s^2}\ge X_0
\]

から従うのはradial upper boundだけであり、

\[
\min(r,s)\ge S_0
\]

は従わないと指摘した。実際、`r=1` と大きな `s` のpairもretained regionに含まれる。

したがって、旧Final R02 §9および旧reference lock §5にある

```text
retained boxes imply min(R,S) >= S0
```

という読み方は撤回する。正しい役割分担は次である。

- `X_{r,s}>=X_0` はfixed-height remainderのretained/shallow分解に用いる。
- `r,s>=S_0` はradial rectangle transferの **core** を定義する追加cutoffである。
- `r<S_0` または `s<S_0` の **wing** はrectangle asymptoticを使わず、非負性と一変数平均で直接評価する。

本稿はこの三分割を明示し、small-coordinate wingがcubic logarithmic main termに寄与しないことを証明する。

---

## 1. 記号と利用する一変数上界

\[
L:=\log B,
\qquad
U:=S_0:=\exp\!\left(\frac12L^{1/4}\right).
\]

Stage12-N1-3dのSelberg--Delange inputから

\[
G_0(x):=\sum_{n\le x}g(n)
=x(c_g\log x+d_g)+O_A\!\left(x(\log(2x))^{-A}\right),
\]

特に一様に

\[
\boxed{G_0(x)\ll x\log(2x)}
\qquad(x\ge1)
\]

を用いる。`g` は非負であり、parity weightは

\[
1\le\lambda(r,s)\le2.
\]

coprimality indicatorを外すことは非負上界では安全である。

full-quadrant harmonic sumを

\[
\widetilde{\mathcal H}_\lambda(B)
:=
\sum_{\substack{r,s\ge1,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

とする。

---

## 2. 一変数kernel補題

### 補題 3f.1

すべての実数 `u>=1`, `X>=1` に対して

\[
\boxed{
\sum_{n\le X}\frac{g(n)}{u^2+n^2}
\ll
\frac{\log(2u)}u
}
\]

が成り立つ。暗黙定数は `u,X` に依存しない。

### 証明

まず `n<=u` では

\[
\sum_{n\le\min(X,u)}\frac{g(n)}{u^2+n^2}
\le
\frac{G_0(u)}{u^2}
\ll
\frac{\log(2u)}u.
\]

次に `u<n<=X` では `u^2+n^2>=n^2` なので

\[
\sum_{u<n\le X}\frac{g(n)}{u^2+n^2}
\le
\sum_{u<n\le X}\frac{g(n)}{n^2}.
\]

Stieltjes partial summationにより

\[
\sum_{u<n\le X}\frac{g(n)}{n^2}
\ll
\frac{G_0(X)}{X^2}
+
\frac{G_0(u)}{u^2}
+
\int_u^X\frac{G_0(t)}{t^3}\,dt.
\]

`G_0(t)<<t log(2t)` を代入すると

\[
\frac{G_0(X)}{X^2}
+
\frac{G_0(u)}{u^2}
+
\int_u^X\frac{G_0(t)}{t^3}\,dt
\ll
\frac{\log(2u)}u.
\]

`X<=u` の場合は最初の評価だけでよい。従って補題が従う。`□`

---

## 3. 離散wingの直接評価

wing集合を

\[
\mathcal W_U(B)
:=
\{(r,s)\in\mathbb N^2:r^2+s^2\le B,\ \min(r,s)<U\}
\]

とする。

### 補題 3f.2

\[
\boxed{
\sum_{\substack{(r,s)\in\mathcal W_U(B)\\(r,s)=1}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\ll
(\log(2U))^3
}
\]

が成り立つ。従って今回の `U` では

\[
\boxed{
\mathcal H_{\rm wing}(B)
=O(L^{3/4})
=o(L^3).
}
\]

### 証明

対称性、`lambda<=2`、非負性、coprimalityの除去により

\[
\mathcal H_{\rm wing}(B)
\ll
\sum_{r<U}g(r)
\sum_{s\le\sqrt B}
\frac{g(s)}{r^2+s^2}.
\]

補題3f.1を `u=r` に適用すると

\[
\mathcal H_{\rm wing}(B)
\ll
\sum_{r<U}\frac{g(r)\log(2r)}r.
\]

`A(t)=G_0(t)` と

\[
\phi(t)=\frac{\log(2t)}t
\]

にpartial summationを用いる。`A(t)<<t log(2t)` および

\[
|\phi'(t)|\ll\frac{\log(2t)}{t^2}
\]

から

\[
\sum_{r<U}\frac{g(r)\log(2r)}r
\ll
(\log(2U))^2
+
\int_1^U\frac{(\log(2t))^2}{t}\,dt
\ll
(\log(2U))^3.
\]

ここで `log U=L^(1/4)/2` なので

\[
(\log(2U))^3=O(L^{3/4}).
\]

従ってwingはcubic main scale `L^3` に対して低次である。`□`

---

## 4. 連続leading integralのwing mass

rectangle leading termのmixed densityは

\[
C_\lambda^{(0)}(\log x+1)(\log y+1)\,dx\,dy
\]

である。full radial leading integralとcore leading integralの差を制御するため、連続wingも評価する。

### 補題 3f.3

\[
\boxed{
\iint_{\substack{x,y\ge1,\ x^2+y^2\le B\\\min(x,y)<U}}
\frac{(\log x+1)(\log y+1)}{x^2+y^2}\,dx\,dy
\ll
(\log(2U))^3
}
\]

が成り立つ。

### 証明

対称性により `x<U` の領域を二倍すれば十分である。固定 `x>=1` に対して、`y<=x` と `y>x` に分けると

\[
\int_1^{\sqrt B}
\frac{\log y+1}{x^2+y^2}\,dy
\ll
\frac{\log(2x)}x.
\]

実際、`y<=x` ではdenominatorを `x^2` で下から押さえ、`y>x` では `y^2` で下から押さえる。

従ってwing integralは

\[
\ll
\int_1^U
\frac{(\log x+1)\log(2x)}x\,dx
\ll
(\log(2U))^3.
\]

`□`

同じ議論により、rectangle polynomialのlower-degree density、すなわち `1`, `log x`, `log y` の各項のwing integralも `O((log(2U))^3)` 以下であり、すべて `o(L^3)` である。

---

## 5. core上のrectangle transfer

coreを

\[
\mathcal C_U(B)
:=
\{(r,s)\in\mathbb N^2:r^2+s^2\le B,\ r\ge U,\ s\ge U\}
\]

とする。coreを

\[
[2^iU,2^{i+1}U)\times[2^jU,2^{j+1}U)
\]

型のdyadic boxへ分割する。このとき各boxのside scales `R,S` は

\[
R,S\ge U
\]

を満たす。これはretained conditionから導くものではなく、coreの定義そのものである。

kernel

\[
K(x,y)=\frac1{x^2+y^2}
\]

のboxwise partial-summation normは

\[
\|K\|_{{\rm PS},\mathcal B(R,S)}
\ll\frac1{R^2+S^2}.
\]

### 5.1 corrected power tail

rectangle remainderのpower partは

\[
E_{\rm pow}(R,S)
\ll
\log(2R)\log(2S)
\{R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}\},
\]

ここで固定 `0<epsilon<1/8` とする。`R<=S` の場合、kernel normを掛けると

\[
\frac{E_{\rm pow}(R,S)}{R^2+S^2}
\ll
L^2R^{-1/4+\varepsilon}.
\]

従ってcoreの各boxでは

\[
\frac{E_{\rm pow}(R,S)}{R^2+S^2}
\ll
L^2U^{-1/4+\varepsilon}.
\]

box数は `O(L^2)` なので全core power errorは

\[
\ll
L^4U^{-1/4+\varepsilon}
=o(L^{-A})
\]

であり、任意の固定 `A>0` に対して成立する。最後の等式は

\[
U^{-1/4+\varepsilon}
=
\exp\!\left(-\left(\frac14-\varepsilon\right)\frac12L^{1/4}\right)
\]

による。

### 5.2 Selberg--Delange remainder

rectangle remainderのlog-saving partは

\[
E_{\rm SD}(R,S)
\ll
RS\log(2R)\log(2S)
\{(\log(2R))^{-A}+(\log(2S))^{-A}\}.
\]

kernel normを掛け、`R,S>=U` を用いると、各box寄与は

\[
\ll
L^2(\log U)^{-A}
\ll
L^{2-A/4}.
\]

box数、arc-crossing boxes、boxwise partial summationで失う固定対数冪をまとめて `L^C` と書く。Selberg--Delange expansion orderを、`A/4>C+4` となるよう先に固定すれば、core全体のlog-saving errorは `o(L^3)` である。

### 5.3 artificial boundaryを作らないこと

transferは各dyadic box上で直接行う。従って `x=U` または `y=U` に新しい未評価のglobal boundary termを仮定しない。各boxの境界項はboxwise partial-summation normに含まれ、main polynomialのfull integralとcore integralの差は補題3f.3で制御される。

radial arcを横切るboxは従来どおり `O(L^2)`、lower rectangle polynomialとradial Stieltjes boundary termsも `O(L^2)+O((log U)^3)` である。

従ってcoreについて

\[
\boxed{
\widetilde{\mathcal H}_{\lambda,{\rm core}}(B)
=
C_\lambda^{(0)}
\iint_{\substack{x,y\ge U\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}\,dx\,dy
+o(L^3)
}
\]

が成り立つ。`+1`を含むmixed derivativeのlower-degree termsは `O(L^2)+o(L^3)` に入る。

---

## 6. coreとwingの再結合

補題3f.2によりactual discrete wingは `o(L^3)`、補題3f.3によりfull leading integralとcore leading integralの差も `o(L^3)` である。従って

\[
\begin{aligned}
\widetilde{\mathcal H}_\lambda(B)
&=
\widetilde{\mathcal H}_{\lambda,{\rm core}}(B)
+\widetilde{\mathcal H}_{\lambda,{\rm wing}}(B)\\
&=
C_\lambda^{(0)}
\iint_{\substack{x,y\ge1\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}\,dx\,dy
+o(L^3).
\end{aligned}
\]

既存のpolar calculation

\[
\iint_{\substack{x,y\ge1\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}\,dx\,dy
=
\frac\pi{48}L^3+O(L^2)
\]

を代入すると

\[
\boxed{
\widetilde{\mathcal H}_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{48}L^3+o(L^3).
}
\]

primitive diagonalは `(1,1)` のみなのでorientation `r<s` はleading termを半分にし、

\[
\mathcal H_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{96}L^3+o(L^3)
=
\frac\eta{12\pi}L^3+o(L^3).
\]

外側の `B/pi` と `eta=pi*kappa` を戻して

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3
=
\frac\kappa{12\pi}B(\log B)^3
}
\]

という候補漸近式の係数は変わらない。

---

## 7. fixed-height retained/shallow分解との独立性

本稿のcore/wing cutoffはradial harmonic transferのためのものである。fixed-height remainderに用いる

\[
X_{r,s}\ge X_0
\]

というretained conditionとは別の分解である。

従って最終error budgetでは次を別々に管理する。

1. fixed-height retained remainder:
   \[
   O(BX_0^{-1/2}(\log B)^2);
   \]
2. fixed-height shallow sector: 既存の非負rectangle upper boundにより `o(BL^3)`;
3. radial harmonic core: 本稿§5のrectangle transfer;
4. radial harmonic wing: 本稿§3の `O(L^{3/4})`;
5. radial arc、odd--odd annulus、diagonal、floor、constant `-1`: 既存の低次評価。

これらの領域や誤差を互いに同一視しない。

---

## 8. supersessionと修復判定

次の旧文言は本稿で置き換える。

```text
OLD: retained boxes satisfy min(R,S) >= S0
NEW: core boxes are defined by R,S >= S0; the complementary wings are bounded directly
```

R04監査のMAJORに対する状態は

```text
R04_MAJOR_01_SMALL_COORDINATE_WING=CLOSED_BY_STAGE12_N1_3F
DISCRETE_WING_BOUND=O((log U)^3)=O((log B)^(3/4))
CONTINUOUS_WING_BOUND=O((log U)^3)=O((log B)^(3/4))
CORE_RECTANGLE_TRANSFER=VALID_FOR_R_S_GE_U
RETAINED_IMPLIES_MIN_RS_LOWER_BOUND=FALSE_SUPERSEDED
MAIN_CONSTANT_CHANGED=false
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_R05_FULL_REAUDIT
```

とする。