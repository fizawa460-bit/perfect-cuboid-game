# Stage12-N1-3d：Definitions and counting convention

> **STATUS:** `MAJOR_04_DEFINITION_SHEET_COMPLETE`
>
> **SCOPE:** Stage12-N1-2 primitive oriented count only
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT`

## 0. このsheetの目的

本稿は新しい解析補題を導入しない。独立監査R01のMAJOR-04に対応し、Stage12-N1-2で数えている対象、重複度、orientation、raw / primitiveの関係を単独で復元できるように固定する。

最終対象は、以下の式で定義される **primitive oriented count** `C_prim(B)` である。これは完全直方体そのものの個数、辺順序を忘れたcanonical count、またはexact-one-face countへの自動変換を意味しない。

以下、`B` は正整数とする。実数 `B` への拡張は `C(B):=C(floor(B))` とする。

---

## 1. 双曲線座標とadmissible parameter set

正整数 `h,r,s` に対して

\[
p=hrs,
\qquad
c=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2
\]

と置く。Stage12-N1-2のparameter conventionは

\[
1\le r<s,
\qquad
(r,s)=1.
\]

`r<s` はこの系列におけるorientation conventionの一部であり、`r,s` の交換を二重計数しない。

height boundとintegrality conditionをまとめた集合を

\[
\boxed{
\mathcal D_B
:=
\left\{(h,r,s)\in\mathbb N^3:
1\le r<s,
(r,s)=1,
h(r^2+s^2)\le2B,
h(r^2+s^2)\equiv0\pmod2
\right\}.
}
\]

最後の偶奇条件は次と同値である。

- `r,s` がともに奇数なら `r^2+s^2` は偶数で、`h` に追加偶奇制約はない。
- `r,s` がopposite parityなら `r^2+s^2` は奇数で、`h` は偶数でなければならない。

---

## 2. multiplicity weight `G`

素数 `q` と整数 `n` に対して `v_q(n)` を `q`-進付値とする。

\[
\boxed{
G(n)
:=
\prod_{\substack{q\mid n\\q\equiv1\pmod4}}
\left(2v_q(n)+1\right).
}
\]

空積は1とする。Stage12-N1-2のraw multiplicityは

\[
G(hrs)-1
\]

である。`-1` を含むこの重み自体をcounting definitionの一部とし、別のrepresentation conventionへ置き換えない。

---

## 3. raw oriented count

\[
\boxed{
C_{\rm raw}(B)
:=
\sum_{(h,r,s)\in\mathcal D_B}
\bigl(G(hrs)-1\bigr).
}
\]

このcountは次の意味でorientedである。

1. parameter pairに `r<s` を課す。
2. Stage12で選ばれた共有面・構成方向を保持する。
3. 3辺の全置換によるcanonical quotientを行わない。

Stage12-N1-2fでrepeated-side contributionが恒等的に0であることを確認しているため、この系列では

\[
C_{\rm distinct,raw}(B)=C_{\rm raw}(B)
\]

を使用する。ただし、これはcanonical countとの一致を意味しない。

---

## 4. primitive countの対象レベル定義

raw objectをその全辺の共通整数scaleで分類すると、raw countとprimitive countの間にexact relation

\[
C_{\rm raw}(B)
=
\sum_{k\le B}
C_{\rm prim}(\lfloor B/k\rfloor)
\]

がある。従ってMöbius inversionにより

\[
\boxed{
C_{\rm prim}(B)
:=
\sum_{k\le B}
\mu(k)
C_{\rm raw}(\lfloor B/k\rfloor).
}
\]

これをStage12-N1-2のprimitive oriented countの定義とする。ここで `mu` はMöbius関数である。

この式は解析上の近似ではなく、raw対象をglobal contentで分解したexact identityである。

---

## 5. primitive-first exact reindexing

固定されたcoprime pair `(r,s)` に対し

\[
\boxed{
A_{r,s}(m)
:=
\sum_{k\mid m}
\mu(k)
\left\{G\!\left((m/k)rs\right)-1\right\}.
}
\]

parity branchを

\[
\lambda(r,s)
:=
\begin{cases}
2,&r,s\text{ がともに奇数},\\
1,&r,s\text{ がopposite parity}
\end{cases}
\]

とする。`(r,s)=1` のためboth-even branchは存在しない。

Stage12-N1-2jのprimitive-first reindexingは

\[
\boxed{
C_{\rm prim}(B)
=
\sum_{1\le r<s\atop(r,s)=1}
\sum_{m\le \lambda(r,s)B/(r^2+s^2)}
A_{r,s}(m).
}
\]

である。内側上限のfloorは和記号に含める。

二branchを分けて書けば

\[
\sum_{\substack{1\le r<s,(r,s)=1\\r,s\text{ odd}}}
\sum_{m\le2B/(r^2+s^2)}A_{r,s}(m)
\]

と

\[
\sum_{\substack{1\le r<s,(r,s)=1\\r,s\text{ opposite parity}}}
\sum_{m\le B/(r^2+s^2)}A_{r,s}(m)
\]

の和である。

---

## 6. primitive height coefficientの明示式

`m=1` では

\[
A_{r,s}(1)=G(rs)-1.
\]

`m>1` では、`m` が `1 mod 4` 以外の素因数を含むと

\[
A_{r,s}(m)=0.
\]

`m` の全素因数が `1 mod 4` なら

\[
\boxed{
A_{r,s}(m)
=
G(rs)
\prod_{p\mid m}
\frac{2}{2v_p(rs)+1}.
}
\]

positive versionを

\[
A^+_{r,s}(m)
:=
A_{r,s}(m)+\mathbf1_{m=1}
\]

とする。

---

## 7. residue-side arithmetic functions

### 7.1 `beta`

`beta` は乗法関数で、

\[
\beta(1)=1,
\]

\[
\boxed{
\beta(q^j)
=
\frac{2(q-1)}{q+1}
\quad
(q\equiv1\pmod4,\ j\ge1),
}
\]

\[
\boxed{
\beta(p^j)=0
\quad
(p=2\text{ or }p\equiv3\pmod4,\ j\ge1).
}
\]

従って `beta(n)` は、`n` の全素因数が `1 mod 4` のときだけ非零である。

### 7.2 `gamma` と `g`

\[
\boxed{
\gamma(n)
:=
\frac1\pi
\sum_{d\mid n}\beta(d),
}
\]

\[
\boxed{
g(n):=\pi\gamma(n)=(1*\beta)(n).
}
\]

`g` は非負乗法関数である。`q≡1 mod 4` なら

\[
g(q^k)=1+k\frac{2(q-1)}{q+1},
\]

それ以外の素数 `p` では `g(p^k)=1`。

### 7.3 `rho`

fixed-divisor modelで使うlocal-density weightを

\[
\boxed{
\rho(n)
:=
\prod_{p\mid n}\frac{p}{p+1}
}
\]

とする。`rho(1)=1`。

---

## 8. fixed-height partial sumとremainder

\[
\boxed{
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1+R_{r,s}(X).
}
\]

Stage12-N1-3bで証明した一様pointwise boundは

\[
\boxed{
R_{r,s}(X)
\ll
G(rs)H_{\rm abs}(rs)X^{1/2},
}
\]

ここで

\[
H_{\rm abs}(rs)
:=
\sum_{\ell\ge1}
\frac{|h_{r,s}(\ell)|}{\ell^{1/2}}
\]

はfinite Euler correctionのabsolute `1/2`-normである。

`X_{r,s}:=\lambda(r,s)B/(r^2+s^2)`、`L:=\log B` とし、

\[
X_0:=\exp(L^{1/4}).
\]

- retained region: `X_{r,s}>=X_0`
- shallow region: `X_{r,s}<X_0`

と定義する。

---

## 9. error-profile notation

一変数Selberg–Delange入力のremainder profileを `E_N(X)` と書く場合、単調包絡線を

\[
\boxed{
E_{N,*}(X)
:=
\sup_{Y\ge X}E_N(Y)
}
\]

とする。Stage12-N1-3dのreference lockでは、特定の未照合なKorobov--Vinogradov型remainderを必須とせず、任意次数のlog-power remainderを採用する。

---

## 10. orientedとcanonicalを混同しない

Stage12-N1-2の `C_prim(B)` は、上記parameter conventionとmultiplicityを保持するoriented countである。

canonical countを作るには、少なくとも

- 3辺の置換作用;
- どの面が整数面対角線を持つかというincidence;
- 複数面が条件を満たす場合のoverlap correction;
- exact-one / exact-two / exact-threeの区別

を別に処理する必要がある。

従って

\[
C_{\rm prim}(B)
\neq
\text{canonical exact-one-face count}
\]

を一般には仮定しない。固定係数を掛けるだけの自動変換も行わない。

---

## 11. theorem target

Stage12-N1-2の候補定理は、このsheetで定義した対象に限り

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}
B(\log B)^3.
}
\]

完全直方体の存在・非存在、canonical count、Stage13のface-ratio定数は主張しない。

---

## 12. source map

- raw parameter sumと`G`: Stage12-N1-2b
- repeated-side zeroと三法constant: Stage12-N1-2f
- global Möbiusとprimitive-first coefficient: Stage12-N1-2j
- `beta`, `gamma`, `eta`: Stage12-N1-2j〜2k
- corrected fixed-height remainder: Stage12-N1-3b
- residue-first radial transfer: Stage12-N1-3c.G

このsheetを今後のcounting conventionの標準参照とする。