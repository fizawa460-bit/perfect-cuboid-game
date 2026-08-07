# Stage12-N1-3i：rectangle入力とSelberg--Delange参照の最終自己完結化

> **STATUS:** `FINAL_REFERENCE_DEPENDENCIES_CLOSED_IN_TEXT`
>
> **SCOPE:** Stage12-N1-2 primitive oriented count
>
> **THEOREM_STATUS:** `SELF_CONTAINED_PROOF_TEXT_AFTER_R06_R07_EXTERNAL_CHECKS`

## 0. 目的

外部再検算では、Stage12-N1-3a の長方形誤差

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

は独立再計算と一致した。一方、3a が入力としていた

\[
B_\beta(X):=\sum_{n\le X}\beta(n)\ll X
\]

と、coprime cross correction の係数ノルム

\[
M_\delta:=\sum_{a,b\ge1}\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty
\]

が旧2pへの参照として残っていた。また Selberg--Delange の使用条件は reference lock に概要だけがあり、active proof との対応を一箇所に固定していなかった。

本稿ではこの三点を現行定義から直接導く。旧2p本文は active proof に復帰させない。

---

## 1. `B_beta(X) << X` の直接証明

### 1.1 `beta` の局所因子

`beta` は乗法関数で

\[
\beta(q^j)=b_q:=\frac{2(q-1)}{q+1}
\quad(q\equiv1\pmod4,\ j\ge1),
\]

それ以外の素数 `p` では `beta(p^j)=0` (`j>=1`) である。

\[
B_\beta(s):=\sum_{n\ge1}\frac{\beta(n)}{n^s}
\]

とする。`x=p^{-s}` と書けば `q≡1 mod4` で

\[
B_{\beta,q}(s)=1+\frac{b_qx}{1-x}=\frac{1+(b_q-1)x}{1-x},
\]

その他の素数では local factor は1である。従って prime by prime に

\[
\boxed{B_\beta(s)=\zeta(s)L(s,\chi_4)J_\beta(s)}
\]

であり、`J_beta` の局所因子は

\[
J_{\beta,2}(s)=1-2^{-s},
\]

\[
J_{\beta,p}(s)=1-p^{-2s}\quad(p\equiv3\pmod4),
\]

\[
J_{\beta,q}(s)=(1-q^{-s})\{1+(b_q-1)q^{-s}\}\quad(q\equiv1\pmod4).
\]

`q≡1 mod4` では

\[
b_q-2=-\frac4{q+1},\qquad 0<b_q-1=\frac{q-3}{q+1}<1,
\]

よって `sigma=Re(s)` に対し

\[
J_{\beta,q}(s)-1=(b_q-2)q^{-s}-(b_q-1)q^{-2s}
\]

から

\[
|J_{\beta,q}(s)-1|\ll q^{-1-\sigma}+q^{-2\sigma}.
\]

`p≡3 mod4` では `O(p^{-2sigma})` である。したがって任意の固定

\[
\sigma\ge\frac12+\delta_0\quad(\delta_0>0)
\]

で `J_beta(s)` は局所一様に絶対収束する。特に

\[
J_\beta(s)=\sum_{n\ge1}\frac{j_\beta(n)}{n^s}
\]

の係数について

\[
\boxed{\sum_{n\ge1}\frac{|j_\beta(n)|}{n}<\infty.}
\]

### 1.2 `zeta(s)L(s,chi_4)` の係数平均

\[
a(n):=(1*\chi_4)(n)
\]

と置けば

\[
\zeta(s)L(s,\chi_4)=\sum_{n\ge1}\frac{a(n)}{n^s}.
\]

`chi_4` の部分和は周期性から一様有界である。従って Dirichlet の判定または部分和分により

\[
\sum_{d\le Y}\frac{\chi_4(d)}d=O(1).
\]

一方

\[
\begin{aligned}
A(Y):=\sum_{n\le Y}a(n)
&=\sum_{d\le Y}\chi_4(d)\left\lfloor\frac Yd\right\rfloor\\
&=Y\sum_{d\le Y}\frac{\chi_4(d)}d+O(Y),
\end{aligned}
\]

ゆえに

\[
\boxed{A(Y)\ll Y.}
\]

### 1.3 convolution による結論

Dirichlet series の積から `beta=j_beta*a` である。したがって

\[
\begin{aligned}
B_\beta(X)
&=\sum_{e\le X}j_\beta(e)A(X/e)\\
&\ll X\sum_{e\le X}\frac{|j_\beta(e)|}{e}\\
&\ll X.
\end{aligned}
\]

よって3aで必要な粗い入力は、旧2pを参照せず

\[
\boxed{B_\beta(X)\ll X\qquad(X\ge1)}
\]

として直接閉じる。この節は Selberg--Delange を使用しない。

---

## 2. coprime cross correction の weighted absolute norm

### 2.1 exact local correction

3aで用いる二変数和を

\[
S(R,S)=\sum_{r\le R}\sum_{s\le S}\beta(r)\beta(s)\mathbf1_{(r,s)=1}
\]

とする。`q≡1 mod4` に対し

\[
U_q(s):=\sum_{k\ge1}\frac{\beta(q^k)}{q^{ks}}=\frac{b_q q^{-s}}{1-q^{-s}}.
\]

coprime 条件により二変数 local factor は

\[
D_q(s_1,s_2)=1+U_q(s_1)+U_q(s_2).
\]

一変数 local factor は `1+U_q(s)` なので

\[
D_q(s_1,s_2)=(1+U_q(s_1))(1+U_q(s_2))C_q(s_1,s_2),
\]

ここで

\[
\boxed{C_q(s_1,s_2)=1-V_q(s_1)V_q(s_2)}
\]

かつ

\[
V_q(s):=\frac{U_q(s)}{1+U_q(s)}=\frac{b_q q^{-s}}{1+(b_q-1)q^{-s}}.
\]

`beta` が消える `p=2` および `p≡3 mod4` では correction は1である。従って

\[
C(s_1,s_2)=\prod_{q\equiv1(4)}C_q(s_1,s_2).
\]

### 2.2 local coefficient `l^1` norm

`|b_q-1|<1` なので

\[
V_q(s)=b_q q^{-s}\sum_{j\ge0}(-1)^j(b_q-1)^jq^{-js}.
\]

`V_q(s)=\sum_{k\ge1}v_{q,k}q^{-ks}` と書くと

\[
|v_{q,k}|=b_q|b_q-1|^{k-1}.
\]

任意の固定 `delta>0` と `sigma>=1/2+delta` に対し

\[
\sum_{k\ge1}|v_{q,k}|q^{-k\sigma}
=\frac{b_q q^{-\sigma}}{1-|b_q-1|q^{-\sigma}}
\ll_\delta q^{-\sigma}
\]

一様に成立する。従って `sigma_i>=1/2+delta` なら `C_q-1=-V_q(s_1)V_q(s_2)` の二変数係数 weighted `l^1` norm は

\[
\ll_\delta q^{-\sigma_1-\sigma_2}\ll_\delta q^{-1-2\delta}.
\]

素数和 `sum_q q^{-1-2delta}` は収束するので Euler product の係数 `l^1` norm も収束する。すなわち

\[
C(s_1,s_2)=\sum_{a,b\ge1}\frac{c(a,b)}{a^{s_1}b^{s_2}}
\]

に対し

\[
\boxed{
M_\delta:=\sum_{a,b\ge1}\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty
\qquad(\delta>0).
}
\]

これは3aで使う `M_{2epsilon}` を直接含む。

---

## 3. Selberg--Delange theorem input の明示固定

### 3.1 外部定理として採用する範囲

Selberg--Delange法そのものは本稿内で再証明しない。外部定理として採用するのは次の有限次数展開だけである。

Dirichlet series

\[
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s}=\zeta(s)^zH(s)
\]

について、係数が固定次数 divisor majorant で支配され、`H` が `s=1` を含む標準 Selberg--Delange 領域

\[
\sigma>1-\frac{c_0}{\log(2+|t|)}
\]

で正則かつ固定 strip 上で多項式 growth を持つ場合、各固定整数 `J>=1` に対して

\[
\sum_{n\le x}f(n)
=x\sum_{j=0}^{J-1}\widetilde c_j\frac{(\log x)^{z-j-1}}{\Gamma(z-j)}
+O_{J,f}\left(x(\log x)^{\Re z-J-1}\right)
\]

を使用する。

これは Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Third Edition, Chapter II.5, Theorem II.5.2, p.281 に対して本系列が使用している working form である。後続文献による同定でも、同 theorem は `F(s)=zeta(s)^alpha G(s)` と、`G` の上記型領域での解析性を仮定して各固定 `J` の有限展開を与えるものとして記述されている。

この節は theorem の証明を置き換えるものではなく、**何を外部定理として使い、何を本系列内で検証するか**を固定する。

### 3.2 `beta` (`z=1`) の仮定対応

\[
B_\beta(s)=\zeta(s)H_\beta(s),\qquad H_\beta(s)=L(s,\chi_4)J_\beta(s).
\]

- coefficient majorant: `0<=beta(n)<=2^{omega(n)}<=tau(n)`;
- analytic factor: §1.1 により `J_beta` は `Re s>1/2` の任意の閉部分半平面で絶対収束し正則。`L(s,chi_4)` は非主指標の Dirichlet L-function なので正則;
- standard SD region: `c0>0` を十分小さく固定すれば `sigma>1-c0/log(2+|t|)` は `J_beta` の正則領域内に入る;
- vertical growth: Stage12-N1-3h §2 の関数等式、Stirling、Phragmen--Lindelof による固定 strip の polynomial bound;
- nonzero leading factor: `L(1,chi_4)=pi/4` かつ各 `J_beta(1)` local factor は正で絶対収束するため `H_beta(1)>0`。

従って `z=1` の有限次数 Selberg--Delange input を適用できる。

### 3.3 `g=1*beta` (`z=2`) の仮定対応

`g=1*beta` なので

\[
\sum_{n\ge1}\frac{g(n)}{n^s}=\zeta(s)B_\beta(s)=\zeta(s)^2H_\beta(s).
\]

analytic factor は `beta` と同じ `H_beta` であり、上の解析性と vertical growth をそのまま使う。また

\[
g(n)\le\sum_{d\mid n}\tau(d)\ll\tau_3(n)
\]

で coefficient majorant も満たす。従って `z=2` の有限次数 Selberg--Delange input を適用できる。

### 3.4 active conclusions

任意の固定 `A>0` に対し、展開次数を十分大きく固定して

\[
\boxed{\sum_{n\le x}\beta(n)=c_\beta x+O_A\bigl(x(\log(2x))^{-A}\bigr)}
\]

および

\[
\boxed{\sum_{n\le x}g(n)=x(c_g\log x+d_g)+O_A\bigl(x(\log(2x))^{-A}\bigr)}
\]

を使用する。なお3aの粗い入力 `B_beta(X)<<X` は §1 で Selberg--Delange に依存せず直接証明済みである。

---

## 4. 3a の small-coefficient region を外部参照なしで閉じる

3a の長方形畳み込み

\[
S(R,S)=\sum_{a\le R,b\le S}c(a,b)B_\beta(R/a)B_\beta(S/b)
\]

で `a<=R^{1/2}`, `b<=S^{1/2}` とする。Selberg--Delange expansion を

\[
B_\beta(Y)=c_\beta Y+O(YE(Y))
\]

と書き、単調包絡線 `E_*` を使えば

\[
E(R/a)\le E_*(R^{1/2}),\qquad E(S/b)\le E_*(S^{1/2}).
\]

従って積の誤差は

\[
\ll\frac{RS}{ab}\{E_*(R^{1/2})+E_*(S^{1/2})\}
\]

に吸収できる。§2 の weighted absolute convergence から

\[
\sum_{a,b}\frac{|c(a,b)|}{ab}<\infty
\]

なので small-coefficient region 全体は

\[
\boxed{O\left(RS\{E_*(R^{1/2})+E_*(S^{1/2})\}\right)}
\]

となる。これで3a Lemma 3a.1 の small-coefficient step も旧2p §3.1を参照せず再構成できる。

---

## 5. active supersession

以後、3aで使う二つの入力と Selberg--Delange の適用条件については本稿を active source とする。

```text
BETA_LINEAR_UPPER_BOUND=CLOSED_DIRECTLY_BY_STAGE12_N1_3I_SECTION_1
BETA_COPRIME_CROSS_WEIGHTED_NORM=CLOSED_DIRECTLY_BY_STAGE12_N1_3I_SECTION_2
SELBERG_DELANGE_APPLICATION_MAP=CLOSED_BY_STAGE12_N1_3I_SECTION_3
RECTANGLE_SMALL_COEFFICIENT_STEP=CLOSED_BY_STAGE12_N1_3I_SECTION_4
OLD_2P_REFERENCE_FOR_THESE_INPUTS=PROVENANCE_ONLY_NOT_REQUIRED
SPECIFIC_3_5_ZERO_FREE_REMAINDER=NOT_USED
```

Stage12-N1-3d reference lock は bibliography と finite-order theorem choice の記録として残すが、その schematic な hypothesis checklist は本稿 §3 の明示対応表で補完する。

---

## 6. 結論

外部再検算で最後に残った軽い参照依存は、旧2p全文を復活させずに現行定義から閉じた。

- `B_beta(X)<<X`: direct convolution proof;
- `M_delta<infinity`: exact local cross correction と weighted local `l^1` norm;
- Tenenbaum II.5.2: 使用する有限次数形と active hypotheses の対応を明示;
- 3a small-coefficient region: 本稿内の入力だけで再導出。

```text
FINAL_REFERENCE_DEPENDENCIES=CLOSED_IN_TEXT
OLD_2P_ACTIVE_DEPENDENCY=NONE
NEW_CENTRAL_MATHEMATICAL_GAP=NONE_IDENTIFIED
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
```
