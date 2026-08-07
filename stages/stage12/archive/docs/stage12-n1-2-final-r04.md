# Stage12-N1-2 Final R04 — primitive oriented count, consolidated through 3f

> **BUNDLE_ID:** `PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3f`
>
> **SOURCE_SNAPSHOT_COMMIT:** `b0208ce33204a3c5f5a52afec146b08a313203f1`
>
> **SOURCE_LEDGER_SHA256:** `f758808bc7f36307b9abcb2b6038ce497735619382fc7bc3056c65cc246cf16f`
>
> **DOCUMENT_STATUS:** `FULL_ZERO_BASE_REREVIEW_CANDIDATE_AFTER_R04_REPAIR`
>
> **COUNTING_TARGET:** `C_prim(B)` as defined in the embedded definition sheet

## Purpose and status

This is the single consolidated current proof source for a new full zero-base re-review of

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

The previous R04 full review returned `REPAIRABLE` with one material gap: the old proof treated `min(R,S)>=S_0` as if it followed from the fixed-height retained condition. Stage12-N1-3f replaces that invalid implication by a disjoint radial decomposition into a core and two small-coordinate wings.

## Effective supersession rule

The following old sentence, wherever it appears inside historical embedded sources, is **not active**:

```text
retained boxes satisfy min(R,S) >= S0
```

The active replacement is:

```text
core boxes are defined by R,S >= S0;
the complementary r-wing and s-wing are bounded directly by Stage12-N1-3f
```

This is the only mathematical precedence override introduced after Final R03. All other embedded content remains subject to zero-base review. Historical status labels do not replace the status of this consolidated file, and earlier `CLOSED` decisions are not binding.

The theorem concerns the primitive **oriented** count only. It does not assert existence of a perfect cuboid, a canonical-count asymptotic, or an exact-one-face asymptotic.

## Immutable source ledger

| source | path | Git blob SHA |
|---|---|---|
| Definitions and counting convention | `docs/stage12-n1-3d-definition-sheet.md` | `b44f76a890363708d6274d14b7f7154894debc7b` |
| Constant sheet | `docs/stage12-n1-3d-constant-sheet.md` | `3428f220c35c3625589dc44abf55819b48109631` |
| Selberg--Delange reference lock | `docs/stage12-n1-3d-selberg-delange-reference-lock.md` | `23f887107b0babaadfcf6d6dc2e4255921c3651d` |
| Integrated repaired proof R02 | `docs/stage12-n1-2-final-r02.md` | `e343182e82d9ecacf844fa7e508662749d43b55b` |
| Stage12-N1-3e local-gap closure | `docs/stage12-n1-3e-local-gap-closure.md` | `a61ba1fe84f49c92e4ccbcd5755ea1e3e0bf5ae5` |
| Stage12-N1-3f small-coordinate wing closure | `docs/stage12-n1-3f-small-coordinate-wing.md` | `e2c77dc23744cb0b9866b40e7a4c0646b0994dd6` |


---

# EMBEDDED SOURCE 1/6 — Definitions and counting convention

> **PATH:** `docs/stage12-n1-3d-definition-sheet.md`  
> **GIT_BLOB_SHA:** `b44f76a890363708d6274d14b7f7154894debc7b`

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


---

# EMBEDDED SOURCE 2/6 — Constant sheet

> **PATH:** `docs/stage12-n1-3d-constant-sheet.md`  
> **GIT_BLOB_SHA:** `3428f220c35c3625589dc44abf55819b48109631`

# Stage12-N1-3d：Constant sheet for `kappa`, `eta`, and front factors

> **STATUS:** `MAJOR_04_CONSTANT_SHEET_COMPLETE`
>
> **SCOPE:** Stage12-N1-2 primitive oriented leading coefficient
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT`

## 0. このsheetの目的

本稿は、独立監査R01で不足とされた

- `kappa` の完全なEuler積;
- `eta` の完全なEuler積;
- 各odd-prime local factor;
- 2-adic / archimedean front factor;
- `eta=pi*kappa` のprime-by-prime comparison;
- 最終係数 `1/(12*pi)` までのfactor ledger

を一枚に固定する。

以下、`p` は `3 mod 4` の奇素数、`q` は `1 mod 4` の奇素数を表す。

---

## 1. three-variable constant `kappa`

Stage12-N1-2fのthree-law Euler factorを

\[
F_q(s)
:=
1+
\frac{2}{q^s-1}
+
\frac{4q}{(q+1)(q^s-1)}
\qquad(q\equiv1\pmod4)
\]

とする。`s=1` では

\[
\boxed{
F_q(1)
=
\frac{q^2+6q+1}{q^2-1}.
}
\]

`kappa` を

\[
\boxed{
\begin{aligned}
\kappa
:={}&
\left(\frac\pi4\right)^3
\left(\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3\\
&\times
\prod_{q\equiv1(4)}
F_q(1)(1-q^{-1})^6.
\end{aligned}
}
\]

と定義する。

local notationでは

\[
\kappa_{\rm front}
:=
\left(\frac\pi4\right)^3
\left(\frac12\right)^3,
\]

\[
\kappa_p:=(1-p^{-2})^3,
\]

\[
\kappa_q
:=
\frac{q^2+6q+1}{q^2-1}
(1-q^{-1})^6.
\]

従って

\[
\kappa
=
\kappa_{\rm front}
\prod_{p\equiv3(4)}\kappa_p
\prod_{q\equiv1(4)}\kappa_q.
\]

normalized local factorsは `1+O(l^{-2})` であり、Euler積は絶対収束する。

---

## 2. two-variable residue constant `eta`

Stage12-N1-2kおよびStage12-N1-3c.Gのtwo-variable constantを

\[
\boxed{
\begin{aligned}
\eta
:={}&
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^2\\
&\times
\prod_{q\equiv1(4)}
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\end{aligned}
}
\]

と定義する。

local notationでは

\[
\eta_{\rm front}
:=
\left(\frac\pi4\right)^2
\left(\frac12\right)^2,
\]

\[
\eta_p:=(1-p^{-2})^2,
\]

\[
\eta_q
:=
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\]

したがって

\[
\eta
=
\eta_{\rm front}
\prod_{p\equiv3(4)}\eta_p
\prod_{q\equiv1(4)}\eta_q.
\]

ここでもnormalized factorsは `1+O(l^{-2})` であり、Euler積は絶対収束する。

---

## 3. `eta/kappa` のlocal comparison

### 3.1 `p congruent 3 mod 4`

\[
\boxed{
\frac{\eta_p}{\kappa_p}
=
\frac{(1-p^{-2})^2}{(1-p^{-2})^3}
=
(1-p^{-2})^{-1}.
}
\]

### 3.2 `q congruent 1 mod 4`

まず

\[
1+\frac{4q}{(q+1)^2}
=
\frac{q^2+6q+1}{(q+1)^2}.
\]

従って

\[
\begin{aligned}
\frac{\eta_q}{\kappa_q}
&=
\frac{
\dfrac{q^2+6q+1}{(q+1)^2}(1-q^{-1})^4
}{
\dfrac{q^2+6q+1}{q^2-1}(1-q^{-1})^6
}\\
&=
\frac{q^2}{q^2-1}
=
(1-q^{-2})^{-1}.
\end{aligned}
\]

よって

\[
\boxed{
\frac{\eta_q}{\kappa_q}
=(1-q^{-2})^{-1}.
}
\]

### 3.3 front factor

\[
\boxed{
\frac{\eta_{\rm front}}{\kappa_{\rm front}}
=
\frac{
(\pi/4)^2(1/2)^2
}{
(\pi/4)^3(1/2)^3
}
=
\frac8\pi.
}
\]

### 3.4 全積

\[
\prod_{\ell\ {
m odd}}
(1-\ell^{-2})^{-1}
=
(1-2^{-2})\zeta(2)
=
\frac{\pi^2}{8}.
\]

従って

\[
\boxed{
\frac\eta\kappa
=
\frac8\pi\cdot\frac{\pi^2}{8}
=
\pi,
}
\]

すなわち

\[
\boxed{\eta=\pi\kappa.}
\]

この恒等式は数値近似ではなく、front factorと各odd-prime local factorのexact comparisonである。

---

## 4. residue-first rectangle coefficient

Stage12-N1-3c.Gでは

\[
g(n)=\pi\gamma(n)=(1*\beta)(n)
\]

を元変数 `(r,s)` 上で平均する。

parity-weighted coprime rectangle sumのleading coefficientを `C_lambda^(0)` とすると、local calculationにより

\[
\boxed{
C_\lambda^{(0)}
=
\frac8{\pi^2}\eta.
}
\]

`8/pi^2` はodd-prime primitive density

\[
\prod_{\ell\ {
m odd}}(1-\ell^{-2})
=
\frac8{\pi^2}
\]

に一致する。

---

## 5. 2-adic parity ledger

`(r,s)=1` のため、許されるparity classはodd--oddまたはopposite parityだけである。

| branch | natural 2-adic mass | height factor `lambda` | weighted mass | radial cutoff |
|---|---:|---:|---:|---:|
| odd--odd | `1/4` | `2` | `1/2` | `r^2+s^2 <= 2B` |
| opposite parity | `1/2` | `1` | `1/2` | `r^2+s^2 <= B` |
| total |  |  | `1` |  |

従ってleading logarithmic coefficientにおける2-adic weighted massは正確に1である。

odd--odd branchのcutoff `2B` とcommon cutoff `B` の差は

\[
\log(2B)=\log B+\log2
\]

であり、cubic leading termを変えず、最大でもquadratic log termへ入る。

---

## 6. archimedean / orientation ledger

`L:=log B` とする。元変数上のleading mixed densityは

\[
C_\lambda^{(0)}
(\log x+1)(\log y+1)\,dx\,dy
\]

であり、cubic termは

\[
I(B)
:=
\int_{\substack{x,y\ge1\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}
\,dx\,dy
\]

から生じる。

polar coordinates

\[
x=t\cos\theta,
\qquad
y=t\sin\theta
\]

では

\[
\frac{dx\,dy}{x^2+y^2}
=
\frac{dt}{t}\,d\theta.
\]

full first quadrantのangular massは `pi/2` であり、

\[
\int_1^{B^{1/2}}
\frac{(\log t)^2}{t}\,dt
=
\frac{(L/2)^3}{3}
=
\frac{L^3}{24}.
\]

よって

\[
\boxed{
I(B)
=
\frac\pi{48}L^3+O(L^2).
}
\]

係数とkernelは `x,y` に対称である。primitive diagonal `x=y` はparameter levelでは `(r,s)=(1,1)` しか残さず `O(1)` なので、orientation `r<s` はleading termを正確に半分にする。

従ってoriented harmonic mainは

\[
\boxed{
\frac12\cdot
\frac\pi{48}\cdot
C_\lambda^{(0)}L^3
=
\frac\eta{12\pi}L^3.
}
\]

---

## 7. 最終front-factor product

fixed-height residue formulaには外側に

\[
\frac B\pi
\]

がある。前節のoriented harmonic coefficientを掛けると

\[
\frac B\pi
\cdot
\frac\eta{12\pi}L^3
=
\frac\eta{12\pi^2}B L^3.
\]

`eta=pi*kappa` を代入して

\[
\boxed{
\frac\eta{12\pi^2}
=
\frac\kappa{12\pi}.
}
\]

従って候補leading termは

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3
=
\frac\kappa{12\pi}B(\log B)^3.
}
\]

---

## 8. factor ledger summary

| source | factor |
|---|---:|
| fixed-height residue normalization | `B/pi` |
| parity-weighted coprime rectangle residue | `C_lambda^(0)=8 eta/pi^2` |
| full-quadrant radial cubic integral | `pi/48` |
| orientation `r<s` | `1/2` |
| combined | `eta B (log B)^3/(12 pi^2)` |
| exact local identity | `eta=pi*kappa` |
| final form | `kappa B (log B)^3/(12 pi)` |

---

## 9. diagnostic numerical values

既存のfinite prime productsは概ね

\[
\kappa\approx0.01855917,
\]

\[
\eta\approx0.05830533485,
\]

\[
\frac\kappa{12\pi}
\approx0.0004922973.
\]

を与える。これらはEuler積の収束診断であり、認証区間ではない。exact proofには使用しない。

---

## 10. source map

- `kappa`, `F_q`, three-law normalization: Stage12-N1-2f
- `eta`, local comparison `eta=pi*kappa`: Stage12-N1-2k
- `C_lambda^(0)`, parity ledger, radial/orientation factors: Stage12-N1-3c.G
- counting target: Stage12-N1-3d definition sheet

このsheetを今後のconstant normalizationの標準参照とする。


---

# EMBEDDED SOURCE 3/6 — Selberg--Delange reference lock

> **PATH:** `docs/stage12-n1-3d-selberg-delange-reference-lock.md`  
> **GIT_BLOB_SHA:** `23f887107b0babaadfcf6d6dc2e4255921c3651d`

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


---

# EMBEDDED SOURCE 4/6 — Integrated repaired proof R02

> **PATH:** `docs/stage12-n1-2-final-r02.md`  
> **GIT_BLOB_SHA:** `e343182e82d9ecacf844fa7e508662749d43b55b`

# Stage12-N1-2 Final R02：primitive oriented count repaired proof

> **DOCUMENT_STATUS:** `REPAIRED_PROOF_CANDIDATE_PENDING_INDEPENDENT_REAUDIT`
>
> **COUNTING_TARGET:** `C_prim(B)` from `stage12-n1-3d-definition-sheet.md`
>
> **CONSTANT_TARGET:** `kappa`, `eta` from `stage12-n1-3d-constant-sheet.md`
>
> **SUPERSEDES:** old `docs/stage12-n1-2-final.md`

## 0. 主張範囲と候補定理

本稿は、Stage12-N1-3a、3b、3c.G、3dを統合した自己完結版である。

対象はdefinition sheetで定義したprimitive oriented count

\[
C_{\rm prim}(B)
=
\sum_{k\le B}\mu(k)
C_{\rm raw}(\lfloor B/k\rfloor),
\]

\[
C_{\rm raw}(B)
=
\sum_{(h,r,s)\in\mathcal D_B}
\{G(hrs)-1\}.
\]

候補定理は

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}
B(\log B)^3
\qquad(B\to\infty).
}
\]

これは完全直方体の存在・非存在、canonical count、exact-one-face countへの自動変換を主張しない。

中心解析項MAJOR-01〜03と自己完結性MAJOR-04は本稿系列で修復した。ただし、独立再監査が完了するまでproject statusは `CLOSED` としない。

---

## 1. exact counting convention

\[
\mathcal D_B
=
\left\{(h,r,s)\in\mathbb N^3:
1\le r<s,
(r,s)=1,
h(r^2+s^2)\le2B,
h(r^2+s^2)\equiv0\pmod2
\right\},
\]

\[
G(n)
=
\prod_{\substack{q\mid n\\q\equiv1(4)}}
(2v_q(n)+1).
\]

`r<s` とStage12のdistinguished-face conventionを保持するため、このcountはorientedである。辺置換のcanonical quotientは行わない。

Stage12-N1-2fのrepeated-side nonexistenceにより

\[
C_{\rm distinct,raw}(B)=C_{\rm raw}(B)
\]

である。

---

## 2. primitive-first exact reindexing

固定coprime pair `(r,s)` に対し

\[
A_{r,s}(m)
=
\sum_{k\mid m}\mu(k)
\{G((m/k)rs)-1\}.
\]

parity factorを

\[
\lambda(r,s)
=
\begin{cases}
2,&r,s\text{ odd},\\
1,&r,s\text{ opposite parity}
\end{cases}
\]

とする。するとexactに

\[
\boxed{
C_{\rm prim}(B)
=
\sum_{1\le r<s\atop(r,s)=1}
\sum_{m\le\lambda(r,s)B/(r^2+s^2)}
A_{r,s}(m).
}
\]

`m=1` では

\[
A_{r,s}(1)=G(rs)-1.
\]

`m>1` では、全素因数が `1 mod 4` の場合だけ非零で、

\[
A_{r,s}(m)
=
G(rs)
\prod_{p\mid m}
\frac{2}{2v_p(rs)+1}.
\]

---

## 3. fixed-height partial sumとMAJOR-02修復

\[
\beta(1)=1,
\]

\[
\beta(q^j)=\frac{2(q-1)}{q+1}
\quad(q\equiv1(4),\ j\ge1),
\]

\[
\beta(p^j)=0
\quad(p=2\text{ or }p\equiv3(4),\ j\ge1).
\]

\[
\gamma(n)
=
\frac1\pi\sum_{d\mid n}\beta(d),
\qquad
g(n):=\pi\gamma(n)=(1*\beta)(n).
\]

fixed-height sumは

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1+R_{r,s}(X).
\]

Stage12-N1-3bでは、旧2kの不正な `omega(X/l)` の引き出しを使用せず、base circle remainderの弱い形とfinite Euler correctionのabsolute `1/2`-normから

\[
\boxed{
R_{r,s}(X)
\ll
G(rs)H_{\rm abs}(rs)X^{1/2}
}
\]

を得た。

`W(n):=G(n)H_abs(n)` とし、ある固定 `K` について

\[
\sum_{n\le T}W(n)
\ll T(\log(2T))^K
\]

を使う。retained region

\[
X_{r,s}
:=
\frac{\lambda(r,s)B}{r^2+s^2}
\ge
X_0:=\exp((\log B)^{1/4})
\]

では、dyadic radial shellにより

\[
\sum_{\rm retained}
W(rs)X_{r,s}^{1/2}
\ll
B X_0^{-1/2}(\log B)^{2K}.
\]

従って任意の固定 `A>0` に対して

\[
\boxed{
\sum_{\rm retained}R_{r,s}(X_{r,s})
=o\!\left(B(\log B)^{-A}\right).
}
\]

shallow regionは後のradial main estimateと一緒に低次化する。

---

## 4. residue mainへ還元

fixed-height mainを代入すると

\[
\mathcal M(B)
=
B
\sum_{1\le r<s\atop(r,s)=1}
\frac{\lambda(r,s)\gamma(rs)}{r^2+s^2}
\mathbf1_{r^2+s^2\le\lambda(r,s)B}.
\]

`(r,s)=1` と `g` の乗法性から

\[
\gamma(rs)=\frac1\pi g(r)g(s).
\]

従って

\[
\boxed{
\mathcal M(B)
=
\frac B\pi
\left\{
2\sum_{\substack{r<s,(r,s)=1\\r,s\text{ odd}\\r^2+s^2\le2B}}
\frac{g(r)g(s)}{r^2+s^2}
+
\sum_{\substack{r<s,(r,s)=1\\r,s\text{ opposite}\\r^2+s^2\le B}}
\frac{g(r)g(s)}{r^2+s^2}
\right\}.
}
\]

common cutoff版を

\[
\mathcal H_\lambda(B)
:=
\sum_{\substack{r<s,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

とする。odd--odd annulus `B<r^2+s^2<=2B` のharmonic massは `O((log B)^2)` なので

\[
\boxed{
\mathcal M(B)
=
\frac B\pi\mathcal H_\lambda(B)
+O(B(\log B)^2).
}
\]

---

## 5. Selberg--Delange reference lock

\[
B_\beta(s)
:=
\sum_{n\ge1}\frac{\beta(n)}{n^s}
=
\zeta(s)L(s,\chi_4)J_\beta(s).
\]

`J_beta` は任意の固定 `epsilon>0` に対して `Re s>=1/2+epsilon` の閉部分領域で局所一様絶対収束し、正則である。

Stage12-N1-3d reference lockではTenenbaum, Chapter II.5, Theorem II.5.2のfinite-order expansionを用い、特定の未照合subexponential remainderを必要としない。

任意の固定 `A>0` に対して

\[
\sum_{n\le x}\beta(n)
=
c_\beta x
+O_A(x(\log(2x))^{-A}).
\]

また `g=1*beta` なので

\[
G_g(s)
:=
\sum_{n\ge1}\frac{g(n)}{n^s}
=
\zeta(s)^2L(s,\chi_4)J_\beta(s),
\]

従って `z=2` caseから

\[
\boxed{
G_0(x)
:=
\sum_{n\le x}g(n)
=
x(c_g\log x+d_g)
+O_A(x(\log(2x))^{-A}).
}
\]

特に

\[
G_0(x)\ll x\log(2x).
\]

---

## 6. parity-weighted coprime rectangle lemma

\[
a_\lambda(r,s)
:=
\lambda(r,s)g(r)g(s)\mathbf1_{(r,s)=1},
\]

\[
T_\lambda(R,S)
:=
\sum_{r\le R}\sum_{s\le S}a_\lambda(r,s).
\]

二変数Dirichlet seriesは

\[
D_\lambda(s_1,s_2)
=
G_g(s_1)G_g(s_2)C_\lambda(s_1,s_2),
\]

ここでcross correction `C_lambda` は `Re(s_1+s_2)>1` で絶対収束する。

任意の固定 `0<epsilon<1/8` に対して

\[
\begin{aligned}
T_\lambda(R,S)
={}&C_\lambda^{(0)}RS\log R\log S
+RS\{C_{10}\log R+C_{01}\log S+C_{00}\}\\
&+O_{\varepsilon,A}\!\Bigl(
RS\log(2R)\log(2S)
\{(\log(2R))^{-A}+(\log(2S))^{-A}\}\\
&\hspace{24mm}
+\log(2R)\log(2S)
\{R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}\}
\Bigr).
\end{aligned}
\]

この式は、cross coefficientsを先に畳み込み、小係数領域で `z=2` 一変数展開を二回適用し、大係数領域でweighted absolute normを用いて得る。

Stage12-N1-3aで修復した

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

型のtail exponentと同じ機構であり、旧文書の不成立な `R^(1/2+delta)S` への強化は使用しない。

---

## 7. rectangle leading constant

constant sheetのlocal calculationにより

\[
\boxed{
C_\lambda^{(0)}
=
\frac8{\pi^2}\eta.
}
\]

ここで

\[
\eta
=
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^2
\prod_{q\equiv1(4)}
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\]

three-variable constantは

\[
\kappa
=
\left(\frac\pi4\right)^3
\left(\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3
\prod_{q\equiv1(4)}
\frac{q^2+6q+1}{q^2-1}
(1-q^{-1})^6.
\]

prime-by-prime comparisonから

\[
\boxed{\eta=\pi\kappa.}
\]

---

## 8. radial Stieltjes transferと係数 `1/12`

full quadrant harmonic sumを

\[
\widetilde{\mathcal H}_\lambda(B)
:=
\sum_{\substack{r,s\ge1,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

とする。

係数とkernelは対称であり、`r=s` とcoprimalityを同時に満たすのは `(1,1)` だけなので

\[
\mathcal H_\lambda(B)
=
\frac12\widetilde{\mathcal H}_\lambda(B)+O(1).
\]

二変数Stieltjes表示は

\[
\widetilde{\mathcal H}_\lambda(B)
=
\iint_{x^2+y^2\le B}
\frac1{x^2+y^2}
\,dT_\lambda(x,y).
\]

leading rectangle termのmixed derivativeは

\[
C_\lambda^{(0)}
(\log x+1)(\log y+1)\,dx\,dy.
\]

cubic termは

\[
I(B)
:=
\int_{\substack{x,y\ge1\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}
\,dx\,dy.
\]

polar coordinatesで

\[
\frac{dx\,dy}{x^2+y^2}
=
\frac{dt}{t}\,d\theta
\]

となり、`L=log B` として

\[
\boxed{
I(B)
=
\frac\pi{48}L^3+O(L^2).
}
\]

従って

\[
\widetilde{\mathcal H}_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{48}L^3
+o(L^3),
\]

orientationを半分にして

\[
\boxed{
\mathcal H_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{96}L^3
+o(L^3)
=
\frac\eta{12\pi}L^3
+o(L^3).
}
\]

ここで係数 `1/12` はradial kernelを保持したStieltjes integral、full-quadrant angle、orientation factorから得られている。

---

## 9. radial transfer error

対数dyadic box

\[
\mathcal B(R,S)=[R,2R]\times[S,2S]
\]

上で

\[
K(x,y)=\frac1{x^2+y^2}
\]

の部分和分ノルムは

\[
\|K\|_{{\rm PS},\mathcal B}
\ll
\frac1{R^2+S^2}.
\]

retained boxesでは

\[
\min(R,S)
\ge
S_0
:=
\exp\!\left(\frac12(\log B)^{1/4}\right).
\]

power-tail errorのbox contributionは、例えば `R<=S` なら

\[
\ll
(\log B)^2R^{-1/4+\varepsilon}.
\]

`epsilon<1/8` のため、これは任意の固定log-powerより小さい。Selberg--Delange remainderも展開次数を十分大きく固定することで同様に全box合計 `o(L^3)` となる。

shallow boxesの全harmonic massは

\[
O(L^{3/2}),
\]

radial arc boxesは

\[
O(L^2),
\]

lower rectangle polynomialとStieltjes boundary termsも

\[
O(L^2).
\]

従って

\[
\boxed{
\widetilde{\mathcal H}_\lambda(B)
-
\frac{\pi C_\lambda^{(0)}}{48}L^3
=o(L^3).
}
\]

---

## 10. endpointと非residue terms

- fixed-height remainder: `o(B(log B)^(-A))` on retained region by Stage12-N1-3b;
- shallow fixed-height sector: `o(BL^3)` by nonnegative rectangle upper bounds;
- constant `-1` in each fixed-height partial sum: `O(B)`;
- height floor replacement: `O(B(log B)^{1+o(1)})`;
- odd--odd cutoff `2B` versus `B`: `O(BL^2)`;
- primitive diagonal: `O(B)` after outer normalization;
- radial arc and Stieltjes boundaries: `O(BL^2)`.

すべて `o(BL^3)` である。

---

## 11. leading asymptoticの合成

Sections 4、8、9から

\[
\mathcal M(B)
=
\frac B\pi
\left\{
\frac\eta{12\pi}L^3+o(L^3)
\right\}
+O(BL^2).
\]

従って

\[
\mathcal M(B)
\sim
\frac\eta{12\pi^2}B L^3.
\]

Section 3と10のnonresidue termsはすべて低次なので

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3.
}
\]

最後に `eta=pi*kappa` を代入して

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac\kappa{12\pi}B(\log B)^3.
}
\]

---

## 12. supersession table

| 旧箇所 | 問題 | 標準置換 |
|---|---|---|
| 旧2p / 旧Final §4 | 不成立な `R^(1/2+delta)S` 強化 | Stage12-N1-3aの `R^(3/4+epsilon)S` 型 |
| 旧2k / 旧Final §1 | `omega(X/l)` の誤った引き出し | Stage12-N1-3bのpointwise `X^(1/2)` とouter average |
| 旧2n / 旧Final §5 | radial kernelを省略した概要的 `L^3/12` | Stage12-N1-3c.Gのresidue-first radial Stieltjes transfer |
| fixed-`(b,c)` 3c.G案 | 最終定理より強い未証明kernel statement | `SUPERSEDED_NOT_REQUIRED` |
| specific `3/5` remainder | theorem referenceとの接続未固定 | Stage12-N1-3d arbitrary fixed log-power reference lock |
| 旧Finalの外部記号 | 自己完結でない | 3d definition / constant sheetsと本R02 |

---

## 13. 現在の判定

本R02は監査R01のMAJOR-01〜04、CLARIFICATION-01、MINOR-01〜02に対応した再提出候補である。

```text
MAJOR_01=CLOSED_BY_3A
MAJOR_02=CLOSED_BY_3B
MAJOR_03=CLOSED_BY_3C_G
MAJOR_04=CLOSED_BY_3D
CLARIFICATION_01=CLOSED_BY_3D_REFERENCE_LOCK
MINOR_01=CORRECTED_IN_ARCHIVED_2J_AND_NEW_BUNDLE
MINOR_02=CLOSED_BY_SELF_CONTAINED_R02
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT
```

独立再監査が `CLOSED` を返すまでは、project-wideには「証明済み完成定理」と呼ばない。


---

# EMBEDDED SOURCE 5/6 — Stage12-N1-3e local-gap closure

> **PATH:** `docs/stage12-n1-3e-local-gap-closure.md`  
> **GIT_BLOB_SHA:** `a61ba1fe84f49c92e4ccbcd5755ea1e3e0bf5ae5`

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


---

# EMBEDDED SOURCE 6/6 — Stage12-N1-3f small-coordinate wing closure

> **PATH:** `docs/stage12-n1-3f-small-coordinate-wing.md`  
> **GIT_BLOB_SHA:** `e2c77dc23744cb0b9866b40e7a4c0646b0994dd6`

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


---

# Consolidated end marker

```text
CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05
```
