# Stage12-N1-2m：反復Selberg–Delangeとcoprime補正の監査

## 結論

Stage12-N1-2lで未検証と判定した de la Bretèche の多変数定理を避け、二法重み \(\beta\) を一変数Dirichlet級数とcoprime補正へ分解する。

判定は

```text
A_ITERATED_SELBERG_DELANGE_MAIN_TERM_FACTORIZATION_CLOSED_REGION_REMAINDER_PENDING
```

とする。

- 一変数 \(\beta\) 級数は \(s=1\) で単純極を持つ。
- 二変数の互いに素条件は、二つの一変数因子と、\(\Re(s_1+s_2)>1\) で絶対収束するcross correctionへ厳密分解できる。
- 従って長方形領域または滑らかな積重み上では、反復Selberg–Delangeにより主項と局所定数を得られる。
- ただし最終的な結合領域 \(h(r^2+s^2)\le 2B\) へ戻す際のpartial summation、境界層、誤差の一様積分をこの段階だけでは完了していない。

したがって、2lで見つかった「多変数定理の仮定未確認」は回避できるが、最終漸近式を再び CLOSED とするには、次段階で結合領域への移送誤差を閉じる必要がある。

---

## 1. 一変数 \(\beta\) Dirichlet級数

\[
\beta(p^j)=\frac{2(p-1)}{p+1}
\quad(p\equiv1\pmod4,\ j\ge1),
\]

それ以外を0とする。一変数級数

\[
B_\beta(s)=\sum_{n\ge1}\frac{\beta(n)}{n^s}
\]

の局所因子は、\(q\equiv1\pmod4\) に対して

\[
1+\frac{b_q q^{-s}}{1-q^{-s}},
\qquad b_q=\frac{2(q-1)}{q+1}=2+O(q^{-1}).
\]

従って

\[
\log B_\beta(s)
=2\sum_{q\equiv1(4)}q^{-s}+O(1)
=\log\frac1{s-1}+O(1),
\]

となり、\(s=1\) で単純極を持つ。

より具体的には

\[
B_\beta(s)=\zeta(s)L(s,\chi_4)\,J(s),
\]

と書け、\(J(s)\) は少なくとも \(\Re s>1/2+\varepsilon\) の固定近傍で正則かつ非零になる。局所一次項を \(\zeta L\) で除去した残りが \(1+O(q^{-2\sigma})\) になるためである。

従って通常の一変数Selberg–Delangeにより

\[
\sum_{n\le x}\beta(n)=c_\beta x+O\left(x\,E(x)\right)
\]

型の評価を使用できる。ここで \(E(x)\to0\) は選択するzero-free region版に依存する。本段階では認証された最良誤差を主張せず、必要な一様版を次段階で固定する。

---

## 2. coprime二法Euler積の厳密分解

対象係数を

\[
f(r,s)=\beta(r)\beta(s)1_{(r,s)=1}
\]

とする。二変数Dirichlet級数

\[
F(s_1,s_2)=\sum_{r,s\ge1}\frac{f(r,s)}{r^{s_1}s^{s_2}}
\]

の \(q\equiv1\pmod4\) 局所因子は

\[
L_q(s_1,s_2)
=1+\frac{b_q q^{-s_1}}{1-q^{-s_1}}
 +\frac{b_q q^{-s_2}}{1-q^{-s_2}},
\]

である。同じ素数が両変数を割る項はcoprime条件により除かれる。

一変数局所因子

\[
A_q(s)=1+\frac{b_q q^{-s}}{1-q^{-s}}
\]

を使うと

\[
L_q(s_1,s_2)=A_q(s_1)A_q(s_2)C_q(s_1,s_2),
\]

\[
C_q(s_1,s_2)
=1-\frac{u_q(s_1)u_q(s_2)}{(1+u_q(s_1))(1+u_q(s_2))},
\quad
u_q(s)=\frac{b_q q^{-s}}{1-q^{-s}}.
\]

よって

\[
C_q(s_1,s_2)=1+O\left(q^{-\sigma_1-\sigma_2}\right)
\]

が一様に成り立つ。したがって

\[
C(s_1,s_2)=\prod_{q\equiv1(4)}C_q(s_1,s_2)
\]

は

\[
\Re(s_1+s_2)>1
\]

で絶対収束し、\((1,1)\) の近傍で正則かつ非零である。

従って

\[
F(s_1,s_2)=B_\beta(s_1)B_\beta(s_2)C(s_1,s_2)
\]

という厳密分解を得る。

---

## 3. 反復Selberg–Delangeで得られる範囲

長方形和

\[
S(R,S)=\sum_{r\le R}\sum_{s\le S}
\beta(r)\beta(s)1_{(r,s)=1}
\]

または固定された滑らかな積重み

\[
\sum_{r,s}\beta(r)\beta(s)1_{(r,s)=1}
W_1(r/R)W_2(s/S)
\]

については、一方の変数を固定して一変数Selberg–Delangeを適用し、その主項係数を他方の変数で再度平均する方法が使える。

cross correctionが \((1,1)\) 近傍で正則であるため、主項定数は

\[
\operatorname*{Res}_{s_1=1}B_\beta(s_1)
\operatorname*{Res}_{s_2=1}B_\beta(s_2)
C(1,1)
\]

で与えられる。これはStage12-N1-2kの二法Euler定数 \(\eta\) の有限素数局所因子と一致する。

この段階で de la Bretèche のP2・P3を検証する必要はない。

---

## 4. まだ残る結合領域の問題

最終対象は単純な長方形和ではなく、概略

\[
h(r^2+s^2)\le2B
\]

とprimitive-first height weightを含む。固定 \(h\) または固定radial shellごとに二法和を評価し、partial summationで戻す必要がある。

この移送では次を明示的に確認する必要がある。

1. 一変数Selberg–Delange誤差が、外側変数・shell parameterに対して一様であること。
2. \(r<s\)、parity class、\((r,s)=1\) を含む切断で、境界誤差が \(o(B(\log B)^3)\) になること。
3. shallow cutoffとmain regionの接続で、2jの低次評価を二法主項に合わせて再導出すること。
4. 2h–2iのPoisson・指数対評価が最終ルートで不要なのか、一部のみ再利用するのかを確定すること。

これらはStage12-N1-2nで監査する。

---

## 5. 有限監査の意味

専用スクリプトでは以下を確認する。

- 先頭11個の \(1\bmod4\) 素数で、二変数局所因子と一変数因子×cross correctionが有理数として完全一致。
- cross correctionの一次項がなく、最初の混合項が \(q^{-s_1-s_2}\) であること。
- \(C_q(1,1)\) の有限部分積が正で安定すること。
- 長方形有限和とEuler係数列が小範囲で一致すること。

有限監査は解析接続やSelberg–Delange誤差の証明ではない。

---

## 6. 判定

2lのレビュー指摘に対して、de la Bretècheの直接適用を使わない修復経路は成立する。

ただし、現段階で閉じたのは

- 一変数極構造
- coprime cross correctionの絶対収束
- 長方形・積重み上の主項因子分解

までである。

最終結合領域への一様移送が残るため、Stage12-N1-2系列全体の状態は引き続き

```text
REPAIRABLE_AFTER_ADVERSARIAL_REVIEW
```

とする。

次は

```text
Stage12-N1-2n:
反復Selberg–Delange主項をradial/height結合領域へ移送し、
境界・一様誤差・2h–2iとの継承関係を確定する監査
```

とする。
