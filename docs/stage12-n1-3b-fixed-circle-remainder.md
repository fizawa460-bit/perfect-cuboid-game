# Stage12-N1-3b：fixed-circle remainder の平均一様修復

> **STATUS:** `MAJOR_02_CLOSED_AT_AVERAGED_REMAINDER_LEVEL`
>
> **SOURCE_AUDIT:** `docs/review/stage12-n1-2-full-audit-r01.md`
>
> **SUPERSEDES:** Stage12-N1-2k §2–§3 の `ω(X)` 全域引き出し
>
> **THEOREM_STATUS:** `REPAIRABLE — NOT CLOSED`

## 0. 目的と主張範囲

本稿は、独立監査R01の **MAJOR-02** を修復する。

Stage12-N1-2kでは、fixed-`(r,s)` convolution error

\[
G(rs)
\sum_{\ell\le X}
|h_{r,s}(\ell)|(X/\ell)^{1/2}\omega(X/\ell)
\]

から `ω(X)` を全域へ引き出していた。しかし、採用しているzero-free-region saving `ω(t)` は十分大きい `t` で減少するため、`X/ℓ≤X` から得られる不等号の向きは必要なものと逆である。

本稿では `ω(X)` を引き出さない。代わりに

\[
0<\omega(Y)\le 1
\]

だけを使い、finite Euler correctionの絶対 `1/2`-normから正しいpointwise estimate

\[
R_{r,s}(X)
\ll
G(rs)H_{\rm abs}(rs)X^{1/2}
\]

を導く。このpointwise estimateは旧2kより弱いが、retained regionでは `X≥X_0` であるため、outer `(r,s)` averageには

\[
X_0^{-1/2}
\]

のsavingが生じ、任意の固定対数冪より小さい総誤差になる。

本稿だけでは次を閉じない。

- MAJOR-03：完全なcoupled-region transferと係数 `1/12`;
- MAJOR-04：自己完結bundle;
- Tenenbaum参照固定、control character、Final再統合などの二次項目。

したがって候補漸近式全体は引き続き `NOT CLOSED` とする。

---

## 1. base partial sum とfinite Euler correction

Stage12-N1-2kのbase係数を

\[
F_0(s)
=
\sum_{n\ge1}\frac{a_0(n)}{n^s}
=
\frac{\zeta(s)L(s,\chi_4)}
{(1+2^{-s})\zeta(2s)}
\]

とする。base partial sumを

\[
A_0(Y):=\sum_{n\le Y}a_0(n)
\]

と書けば、固定円のprimitive lattice-point estimateから

\[
A_0(Y)
=
\frac{Y}{\pi}+E_0(Y),
\]

\[
E_0(Y)
\ll
Y^{1/2}\omega(Y)
\qquad(Y\ge1)
\]

を用いる。有限範囲は暗黙定数へ吸収し、以後

\[
|E_0(Y)|\ll Y^{1/2}
\qquad(Y\ge1)
\]

という弱い形だけを使用する。

固定されたcoprime pair `(r,s)` に対して

\[
H_{r,s}(s)
=
\sum_{\ell\ge1}
\frac{h_{r,s}(\ell)}{\ell^s}
\]

をStage12-N1-2kのfinite Euler correctionとする。`p^t∥rs`, `p≡1 (mod 4)` では

\[
h_{r,s}(p^j)
=
(-1)^j\frac{4t}{2t+1}
\qquad(j\ge1).
\]

絶対 `1/2`-normを

\[
H_{\rm abs}(rs)
:=
\sum_{\ell\ge1}
\frac{|h_{r,s}(\ell)|}{\ell^{1/2}}
\]

と置く。Euler積表示は

\[
H_{\rm abs}(rs)
=
\prod_{\substack{p^t\Vert rs\\p\equiv1(4)}}
\left(
1+
\frac{4t/(2t+1)}{\sqrt p-1}
\right),
\]

であり有限である。

Stage12-N1-2jで定義したpositive versionは厳密に

\[
A^+_{r,s}
=
G(rs)(a_0*h_{r,s})
\]

を満たす。

---

## 2. pointwise remainderの正しい再評価

### 補題 3b.1

すべてのcoprime pair `(r,s)` と `X≥1` に対して

\[
\boxed{
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(
G(rs)H_{\rm abs}(rs)X^{1/2}
\right)
}
\]

が成り立つ。暗黙定数は `r,s,X` に依存しない。

ここで

\[
\gamma(rs)
=
\frac{G(rs)}{\pi}H_{r,s}(1).
\]

### 証明

convolutionを部分和へ入れると

\[
\sum_{m\le X}A^+_{r,s}(m)
=
G(rs)
\sum_{\ell\le X}
 h_{r,s}(\ell)A_0(X/\ell).
\]

base partial sumを代入して

\[
\sum_{m\le X}A^+_{r,s}(m)
=
\frac{G(rs)X}{\pi}
\sum_{\ell\le X}
\frac{h_{r,s}(\ell)}{\ell}
+
G(rs)
\sum_{\ell\le X}
 h_{r,s}(\ell)E_0(X/\ell).
\]

`H_abs(rs)<∞` から `H_{r,s}(1)` は絶対収束する。完全なresidueを足し引きすると、誤差は

\[
\mathcal E_1
:=
G(rs)
\sum_{\ell\le X}
 h_{r,s}(\ell)E_0(X/\ell)
\]

と

\[
\mathcal E_2
:=-
\frac{G(rs)X}{\pi}
\sum_{\ell>X}
\frac{h_{r,s}(\ell)}{\ell}
\]

の和になる。

第一項には `ω(X/ℓ)` を引き出さず、`|E_0(Y)|≪Y^{1/2}` を直接用いる。すると

\[
|\mathcal E_1|
\ll
G(rs)X^{1/2}
\sum_{\ell\le X}
\frac{|h_{r,s}(\ell)|}{\ell^{1/2}}
\le
G(rs)H_{\rm abs}(rs)X^{1/2}.
\]

第二項には

\[
\frac1\ell
\le
X^{-1/2}\ell^{-1/2}
\qquad(\ell>X)
\]

を用いて

\[
|\mathcal E_2|
\ll
G(rs)X
\sum_{\ell>X}
rac{|h_{r,s}(\ell)|}{\ell}
\]

\[
\ll
G(rs)X^{1/2}
\sum_{\ell>X}
rac{|h_{r,s}(\ell)|}{\ell^{1/2}}
\le
G(rs)H_{\rm abs}(rs)X^{1/2}.
\]

従ってpositive versionについて

\[
\sum_{m\le X}A^+_{r,s}(m)
=
\gamma(rs)X
+O\!\left(
G(rs)H_{\rm abs}(rs)X^{1/2}
\right).
\]

最後に

\[
A^+_{r,s}(m)
=
A_{r,s}(m)+\mathbf 1_{m=1}
\]

を戻せば定数項 `-1` を得る。`□`

---

## 3. 旧 `ω(X)` estimateを使用しないこと

旧Stage12-N1-2kの

\[
R_{r,s}(X)
\ll
G(rs)H_{\rm abs}(rs)X^{1/2}\omega(X)
\]

は本稿では使用しない。

問題は二つある。

1. convolution error内の `ω(X/ℓ)` を `ω(X)` へ一様に置き換えられない。
2. residueを有限和から完全な `H_{r,s}(1)` へ延長するtailは、`H_abs` だけを使うと自然に `X^{1/2}` 型となり、一般には同じ `ω(X)` factorを伴わない。

したがって、修復後のpointwise statementは意図的に

\[
O\!\left(G(rs)H_{\rm abs}(rs)X^{1/2}\right)
\]

へ弱める。必要なsavingはpointwise estimateではなく、次節のretained-height cutoffから得る。

---

## 4. outer `(r,s)` average

\[
W(n):=G(n)H_{\rm abs}(n)
\]

と置く。`W` は非負乗法関数であり、`(r,s)=1` なら

\[
W(rs)=W(r)W(s).
\]

Stage12-N1-2kの局所Euler解析から、ある固定 `K≥0` に対して

\[
M_W(T)
:=
\sum_{n\le T}W(n)
\ll
T(\log(2T))^K
\]

を使用できる。旧2kではより具体的に `K=1` の上界を記載しているが、以下では任意の固定 `K` で十分である。

辺pairに対して

\[
q=r^2+s^2
\]

とする。parity branchによるheight上限係数を `λ_{r,s}∈{1,2}` と書けば

\[
X_{r,s}
=
\frac{\lambda_{r,s}B}{q}.
\]

retained regionでは

\[
X_{r,s}\ge X_0,
\qquad
X_0
=
\exp\!\left((\log B)^{1/4}\right).
\]

従って

\[
q
\le
Q:=\frac{2B}{X_0}.
\]

### 補題 3b.2

retained regionにおけるfixed-circle remainderの総和は、任意の固定 `A>0` に対して

\[
\boxed{
\sum_{\substack{1\le r<s,\ (r,s)=1\\X_{r,s}\ge X_0}}
W(rs)X_{r,s}^{1/2}
=
o\!\left(B(\log B)^{-A}\right)
}
\]

である。

### 証明

`λ_{r,s}≤2` から

\[
\sum_{m retained}
W(rs)X_{r,s}^{1/2}
\ll
B^{1/2}
\sum_{\substack{r,s\ge1,\ (r,s)=1\\r^2+s^2\le Q}}
\frac{W(rs)}{(r^2+s^2)^{1/2}}.
\]

`Y<r^2+s^2≤2Y` のdyadic shellを考える。このshellでは `r,s≤(2Y)^{1/2}` なので、非負性とcoprimality上の乗法性から

\[
\sum_{\substack{Y<r^2+s^2\le2Y\\(r,s)=1}}
W(rs)
\le
\left(
\sum_{n\le(2Y)^{1/2}}W(n)
\right)^2
\]

\[
\ll
Y(\log(2Y))^{2K}.
\]

shell上で `(r^2+s^2)^{-1/2}≤Y^{-1/2}` だから

\[
\sum_{\substack{Y<r^2+s^2\le2Y\\(r,s)=1}}
\frac{W(rs)}{(r^2+s^2)^{1/2}}
\ll
Y^{1/2}(\log(2Y))^{2K}.
\]

`Y` をdyadicに `Q` まで足すと幾何級数の最大shellが支配し、

\[
\sum_{\substack{r,s\ge1,\ (r,s)=1\\r^2+s^2\le Q}}
\frac{W(rs)}{(r^2+s^2)^{1/2}}
\ll
Q^{1/2}(\log(2Q))^{2K}.
\]

よって総和は

\[
\ll
B^{1/2}Q^{1/2}(\log B)^{2K}
\ll
B X_0^{-1/2}(\log B)^{2K}.
\]

`X_0` の定義から

\[
X_0^{-1/2}
=
\exp\!\left(-\frac12(\log B)^{1/4}\right),
\]

これは任意の固定対数冪より速く減少する。従って任意の固定 `A>0` に対して

\[
B X_0^{-1/2}(\log B)^{2K}
=
o\!\left(B(\log B)^{-A}\right).
\]

補題が従う。`□`

---

## 5. shallow regionとの分離

補題3b.2はretained regionだけを対象とする。shallow regionはStage12-N1-2jで

\[
\tau=(\log B)^{-3/4}
\]

を使って別に切り出され、候補主項 `B(log B)^3` に対して低次となる安全側評価が与えられている。

本稿はshallow estimateを再証明しない。重要なのは、retained regionのfixed-circle remainderを閉じるために、旧2kのpointwise `ω(X)` savingを必要としないことである。

retained cutoff

\[
X\ge X_0
\]

そのものがouter averageに `X_0^{-1/2}` を与え、十分なsavingを生む。

---

## 6. 修復判定

独立監査R01のMAJOR-02に対して、次を実施した。

1. `ω(X/ℓ)` から `ω(X)` を引き出す不正な単調性操作を撤回した。
2. convolution errorとresidue tailを分離した。
3. `H_abs` の絶対 `1/2`-normから、一様pointwise estimate
   \[
   R_{r,s}(X)
   \ll
   W(rs)X^{1/2}
   \]
   を証明した。
4. `W` の固定対数次数平均上界とdyadic `q=r^2+s^2` shellを使い、retained regionの総誤差を
   \[
   B X_0^{-1/2}(\log B)^{O(1)}
   \]
   で評価した。
5. これは任意の固定対数冪より小さく、候補主項に対して十分低次である。
6. shallow regionとcoupled-region transferを混同せず、後者をMAJOR-03へ残した。

従って状態は

```text
MAJOR_01_RECTANGULAR_ERROR_EXPONENT=CLOSED_BY_STAGE12_N1_3A
MAJOR_02_FIXED_CIRCLE_REMAINDER=CLOSED_BY_STAGE12_N1_3B
MAJOR_03_COUPLED_REGION_TRANSFER=OPEN_NEXT_CENTRAL
MAJOR_04_REVIEW_SELF_CONTAINMENT=OPEN
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
NEXT_TASK=STAGE12_N1_3C_COUPLED_REGION_TRANSFER
```

とする。
