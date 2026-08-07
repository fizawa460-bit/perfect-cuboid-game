# Stage12-N1-3d：Selberg--Delange reference lock

> **STATUS:** `CLARIFICATION_01_REFERENCE_LOCK_COMPLETE`
>
> **REFERENCE:** Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Third Edition, Graduate Studies in Mathematics 163, AMS, Chapter II.5, Theorem II.5.2, p. 281
>
> **ADOPTED_PARAMETERS:** `z=1` for `beta`; `z=2` for `g=1*beta`

## 0. 修正方針

旧文書の一部は、Tenenbaum II.5.2を参照しながら

\[
\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\}
\]

型の特定zero-free-region remainderを書いていた。しかし、この特定形を本系列で必要なinputとして固定する必要はない。

本稿ではTheorem II.5.2のfinite-order Selberg--Delange expansionだけを採用する。必要な精度に応じて展開次数 `J` を一度大きく選び、任意の固定log-power savingを得る。

従って、以後の標準入力は

```text
SPECIFIC_KOROBOV_VINOGRADOV_REMAINDER=NOT_REQUIRED
ARBITRARY_FIXED_LOG_POWER_REMAINDER=ADOPTED
```

とする。

---

## 1. 採用する一般形

Dirichlet series

\[
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s}
=\zeta(s)^zH(s)
\]

がTenenbaumのhypothesis `P(z;c0,delta,M)`を満たすとする。Theorem II.5.2の採用形は、各固定整数 `J>=1` に対して

\[
\sum_{n\le x}f(n)
=
x\sum_{j=0}^{J-1}
\widetilde c_j
\frac{(\log x)^{z-j-1}}{\Gamma(z-j)}
+O_{J,f}\!\left(
x(\log x)^{\Re z-J-1}
\right).
\]

ここで `tilde c_j` は `s=1` におけるanalytic factorから決まる。

本系列では `z` が正整数1または2なので、`1/Gamma(z-j)` により主多項式は有限次数で止まる。

---

## 2. `beta` に対する `z=1` input

`beta` はStage12-N1-3d definition sheetで定義した非負乗法関数である。

\[
B_\beta(s)
:=
\sum_{n\ge1}\frac{\beta(n)}{n^s}
=
\zeta(s)L(s,\chi_4)J_\beta(s).
\]

従って

\[
B_\beta(s)=\zeta(s)H_\beta(s),
\qquad
H_\beta(s):=L(s,\chi_4)J_\beta(s),
\]

すなわち `z=1`。

採用する結論は、任意の固定 `A>0` に対して

\[
\boxed{
B_\beta(x)
:=
\sum_{n\le x}\beta(n)
=
c_\beta x
+O_A\!\left(
x(\log(2x))^{-A}
\right).
}
\]

`c_beta=H_beta(1)` は正定数である。

---

## 3. `g=1*beta` に対する `z=2` input

\[
g(n):=(1*\beta)(n)
\]

なのでDirichlet seriesは

\[
G_g(s)
:=
\sum_{n\ge1}\frac{g(n)}{n^s}
=
\zeta(s)B_\beta(s)
=
\zeta(s)^2H_\beta(s).
\]

従って `z=2`。

採用する結論は、任意の固定 `A>0` に対して

\[
\boxed{
\sum_{n\le x}g(n)
=
x\{c_g\log x+d_g\}
+O_A\!\left(
x(\log(2x))^{-A}
\right),
}
\]

ここで `c_g,d_g` は `H_beta` の `s=1` 近傍展開から決まる。Stage12-N1-3c.Gで必要なのはleading coefficientと、任意固定log-power savingを持つ一様remainderである。

---

## 4. hypothesis checklist

### 4.1 coefficient majorant

`q congruent 1 mod 4` に対し

\[
0\le\beta(q^j)<2.
\]

従って

\[
0\le\beta(n)
\le2^{\omega(n)}
\le\tau(n).
\]

また

\[
g(n)=\sum_{d\mid n}\beta(d)
\le
\sum_{d\mid n}\tau(d)
\ll\tau_3(n).
\]

よって両係数列は固定次数divisor majorantで支配される。

### 4.2 analytic factor

`q congruent 1 mod 4` のlocal factorを `x=q^{-s}` と書くと

\[
J_{\beta,q}(s)
=(1-x)\{1+(b_q-1)x\},
\qquad
b_q=\frac{2(q-1)}{q+1}.
\]

\[
J_{\beta,q}(s)-1
=O(q^{-1-\sigma})+O(q^{-2\sigma}).
\]

`p congruent 3 mod 4` では

\[
J_{\beta,p}(s)=1-p^{-2s}.
\]

従って任意の固定 `epsilon>0` に対し、`Re s>=1/2+epsilon` の閉部分領域でEuler積 `J_beta(s)` は局所一様絶対収束し、正則である。

`L(s,chi_4)` は非主指標のDirichlet `L`-functionで、`s=1` 近傍で正則かつ非零である。従って `H_beta(s)` は `s=1` 近傍で正則である。

### 4.3 vertical growth

`J_beta` の絶対収束部分は上記半平面の閉部分領域で一様有界である。必要なvertical growthは `L(s,chi_4)` の固定stripにおける標準的多項式growthへ還元される。

### 4.4 two-variable cross correction

coprime conditionを分離するcross correctionはlocalに

\[
C_\ell(s_1,s_2)-1
=O(\ell^{-\sigma_1-\sigma_2})
\]

である。従って `Re(s_1+s_2)>1` で絶対収束し、`(1,1)` の近傍で正則である。

このfactorは各一変数Selberg--Delange inputを破壊せず、係数展開後はweighted absolute normにより一様長方形誤差へ移される。

---

## 5. retained regionで十分であること

Stage12-N1-3aおよび3c.Gのretained scaleは

\[
S_0
=
\exp\!\left(\frac12(\log B)^{1/4}\right).
\]

`x>=S_0` では

\[
(\log x)^{-A}
\ll
(\log B)^{-A/4}.
\]

box個数とkernel変分で失う固定対数冪を `C` とする。Theorem II.5.2の展開次数 `J` を、対応する `A` が `4(C+10)` より大きくなるよう固定すれば、全boxを合計したremainderは

\[
o((\log B)^3)
\]

となる。

従って、本証明は特定のsubexponential remainderを必要としない。

---

## 6. supersession rule

以後、次を標準参照とする。

- `z=1`: `B_beta(x)=c_beta x+O_A(x(log 2x)^(-A))`
- `z=2`: `sum_{n<=x}g(n)=x(c_g log x+d_g)+O_A(x(log 2x)^(-A))`

旧2o、旧Final、3a、3c.Gに現れる特定の

\[
\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\}
\]

は、使用可能性を否定するものではないが、Stage12-N1-2のclosureに必要な引用済みinputとしては採用しない。本reference lockのarbitrary fixed log-power formで置き換える。

---

## 7. bibliography lock

- Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Third Edition, Graduate Studies in Mathematics 163, American Mathematical Society, Chapter II.5, Theorem II.5.2, p. 281.
- Régis de la Bretèche and Gérald Tenenbaum, *Remarks on the Selberg--Delange method*, Acta Arithmetica 200 (2021), 349--369. 補助的背景のみ。今回のreference lockの主引用は上記book theoremである。

```text
CLARIFICATION_01=CLOSED_BY_STAGE12_N1_3D_REFERENCE_LOCK
SPECIFIC_3_5_ZERO_FREE_REMAINDER=NOT_USED
SELBERG_DELANGE_Z1=LOCKED
SELBERG_DELANGE_Z2=LOCKED
```