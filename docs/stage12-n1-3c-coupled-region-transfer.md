# Stage12-N1-3c：coupled-region transfer の完全変数展開と幾何kernel課題

> **STATUS:** `MAJOR_03_PARTIALLY_RESOLVED_GEOMETRIC_KERNEL_OPEN`
>
> **SOURCE_AUDIT:** `docs/review/stage12-n1-2-full-audit-r01.md`
>
> **SUPERSEDES:** Stage12-N1-2n §3 および旧Final §5の概要的な `L^3/12` 移送
>
> **THEOREM_STATUS:** `REPAIRABLE — NOT CLOSED`
>
> **MERGE_STATUS:** `DO_NOT_MERGE_WHILE_GEOMETRIC_KERNEL_LEMMA_IS_OPEN`

## 0. 目的と今回の到達点

本稿は、独立監査R01の **MAJOR-03** を扱う。

旧2nと旧Finalでは、長方形主項から

\[
\int_{2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=\frac{L^3}{12}
\]

へ移る部分が概要に留まり、次が明示されていなかった。

- 元の辺変数 `(r,s)`;
- divisor variables `(b,c)`;
- 倍数変数 `(u,v)`;
- radial kernel `(r^2+s^2)^{-1}`;
- odd–odd / opposite-parity のheight係数;
- orientation `r<s`;
- 正確な二変数Stieltjes移送;
- 修正版長方形誤差のkernel適用後評価。

本稿では、これらを一つの等式鎖へ戻す。また、算術側の二変数Stieltjes移送と係数 `1/12` の計算を厳密に分離する。

その結果、旧文書で隠れていた残件は次の一つへ縮約される。

> **Geometric kernel lemma.** fixed divisor variables `(b,c)` に対するanisotropic primitive harmonic lattice sumを、必要な平均一様誤差でarchimedean kernelへ置換すること。

この補題は現在の文書群からは証明できていない。従って、本稿はMAJOR-03を完全には閉じず、`DO_NOT_MERGE` とする。

---

## 1. primitive-first 主項の正確な形

Stage12-N1-3bにより、fixed-`(r,s)` height sumは

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(G(rs)H_{\rm abs}(rs)X^{1/2}\right)
\]

であり、retained regionにおけるremainderのouter averageは主項より十分小さい。

従って、MAJOR-03ではheight remainderを切り離し、residue mainだけを扱う。

\[
q=r^2+s^2,
\]

とし、parity branchのheight係数を

\[
\lambda(r,s)=
\begin{cases}
2,&r,s\text{ がともに奇数},\\
1,&r,s\text{ がopposite parity}
\end{cases}
\]

とする。`(r,s)=1` なのでboth-evenは存在しない。

residue mainは

\[
\mathcal M(B)
=
B
\sum_{1\le r<s\atop(r,s)=1}
\frac{\lambda(r,s)}{r^2+s^2}
\gamma(rs)
\mathbf 1_{r^2+s^2\le \lambda(r,s)B}.
\]

Stage12-N1-2jのdivisor expansion

\[
\gamma(n)=\frac1\pi\sum_{d\mid n}\beta(d)
\]

を代入すると

\[
\mathcal M(B)
=
\frac{B}{\pi}
\sum_{1\le r<s\atop(r,s)=1}
\frac{\lambda(r,s)}{r^2+s^2}
\mathbf 1_{r^2+s^2\le \lambda(r,s)B}
\sum_{d\mid rs}\beta(d).
\]

ここまでは等式であり、`L^3/12` の近似を使っていない。

---

## 2. divisor variables と倍数変数の完全分離

`(r,s)=1` なので、各 `d|rs` は一意に

\[
d=bc,
\qquad b\mid r,
\qquad c\mid s,
\qquad (b,c)=1
\]

と分解される。また `β` は乗法的なので

\[
\beta(d)=\beta(b)\beta(c).
\]

\[
r=bu,
\qquad
s=cv
\]

と置く。`β` のsupportから `b,c` は奇数である。

条件 `(r,s)=1` は

\[
(u,v)=1,
\qquad
(u,c)=1,
\qquad
(v,b)=1,
\qquad
(b,c)=1
\]

と同値である。

また、`b,c` が奇数なのでparity branchは `(u,v)` のparityだけで決まり、

\[
\lambda(bu,cv)=\lambda(u,v).
\]

従って主項は正確に

\[
\boxed{
\mathcal M(B)
=
\frac{B}{\pi}
\sum_{b,c\ge1\atop(b,c)=1}
\beta(b)\beta(c)
\mathcal K_B(b,c)
}
\]

と書ける。ここでradial / height / orientationをすべて保持したkernelは

\[
\boxed{
\mathcal K_B(b,c)
:=
\sum_{u,v\ge1\atop
(u,v)=1,\ (u,c)=1,\ (v,b)=1,\ bu<cv}
\frac{\lambda(u,v)}{b^2u^2+c^2v^2}
\mathbf 1_{b^2u^2+c^2v^2\le\lambda(u,v)B}
}.
\]

これが旧2nで省略されていた完全な変数対応である。

- `(r,s)`：元のprimitive edge parameters;
- `(b,c)`：`γ(rs)` のdivisor variables;
- `(u,v)`：`r=bu`, `s=cv` の倍数変数;
- `(b^2u^2+c^2v^2)^{-1}`：消してはいけないradial kernel;
- `bu<cv`：orientation `r<s`;
- `λ(u,v)`：odd–odd / opposite-parity height factor。

---

## 3. archimedean とlocal-densityから予測されるkernel

\[
\rho(n):=
\prod_{p\mid n}\frac{p}{p+1}
\]

とする。

### 3.1 奇素数local density

fixed coprime `(b,c)` に対し、倍数変数は

\[
(u,v)=1,
\qquad
(u,c)=1,
\qquad
(v,b)=1
\]

を満たす。

奇素数 `p` について、基準primitive densityに対する追加比は

\[
\frac{1-p^{-1}}{1-p^{-2}}
=rac{p}{p+1}
\]

である。従ってodd-prime densityは

\[
\prod_{p\ \mathrm{odd}}(1-p^{-2})\rho(bc)
=
\frac{8}{\pi^2}\rho(bc).
\]

### 3.2 2-adic weighted mass

`b,c` は奇数である。`u,v` のparity classの通常密度は

\[
\text{odd--odd}:\frac14,
\qquad
\text{opposite parity}:\frac12.
\]

height係数を掛けた2-adic massは

\[
2\cdot\frac14+1\cdot\frac12=1.
\]

従って、2-adic branchはleading logarithmic coefficientに追加損失を与えない。odd–odd branchのradial cutoff `\sqrt{2B}` とopposite-parity branchのcutoff `\sqrt B` の差は `\log 2` の定数差であり、leading `L^3` には影響せず、最大でもlower-log termへ入る。

### 3.3 orientation とradial integral

座標

\[
x=bu,
\qquad
y=cv
\]

を用いるとJacobianは `(bc)^{-1}`。orientation `bu<cv` は第一象限の角度 `π/4` のsectorである。

radial harmonic integralは

\[
\int\frac{dx\,dy}{x^2+y^2}
=
\int d\theta\int\frac{dt}{t}.
\]

上端は `t\asymp B^{1/2}`、下端は `t\asymp\max(b,c)` であるため、leading logarithmic lengthは

\[
\frac12
\left[
L-2\max(\log b,\log c)
\right]_+.
\]

angle `π/4`、odd-prime density `8ρ(bc)/π^2`、radial factor `1/2` を合わせると、予測されるkernel mainは

\[
\boxed{
\mathcal K_B^{\rm main}(b,c)
=
\frac{\rho(bc)}{\pi bc}
\left[
L-2\max(\log b,\log c)
\right]_+.
}
\]

従って、必要なgeometric kernel statementは

\[
\mathcal K_B(b,c)
=
\mathcal K_B^{\rm main}(b,c)
+\mathcal R_B(b,c)
\]

と書いたとき、最終的に

\[
\sum_{(b,c)=1}
\beta(b)\beta(c)\mathcal R_B(b,c)
=o((\log B)^3)
\]

を示すことである。

このweighted average remainderが現在の中心未証明項である。

---

## 4. density-corrected divisor coefficient

kernel mainへ `ρ(bc)` が現れるため

\[
\alpha(n):=\beta(n)\rho(n)
\]

と置く。`(b,c)=1` なら

\[
\rho(bc)=\rho(b)\rho(c),
\]

従ってkernel mainを代入した算術和は

\[
\mathcal M_{\rm model}(B)
=
\frac{B}{\pi^2}
\sum_{b,c\ge1\atop(b,c)=1}
\frac{\alpha(b)\alpha(c)}{bc}
\Phi_L(\log b,\log c),
\]

\[
\Phi_L(y,z)
:=
[L-2\max(y,z)]_+.
\]

`q≡1 (mod 4)` と `j≥1` に対し

\[
\alpha(q^j)
=
\frac{2q(q-1)}{(q+1)^2}.
\]

二変数係数

\[
a(b,c)
:=
\alpha(b)\alpha(c)\mathbf1_{(b,c)=1}
\]

を定義する。

---

## 5. arithmetic rectangle constant は `η`

二変数Dirichlet級数

\[
F_\alpha(s_1,s_2)
=
\sum_{b,c\ge1}
\frac{a(b,c)}{b^{s_1}c^{s_2}}
\]

を考える。

`q≡1 (mod 4)` のlocal factorは

\[
1+
\frac{a_q q^{-s_1}}{1-q^{-s_1}}
+
\frac{a_q q^{-s_2}}{1-q^{-s_2}},
\qquad
 a_q=\frac{2q(q-1)}{(q+1)^2}.
\]

`(s_1,s_2)=(1,1)` では

\[
1+2\frac{a_q}{q-1}
=
1+\frac{4q}{(q+1)^2}.
\]

各変数の `ζ(s)L(s,χ_4)` poleを除いたnormalized local factorは

\[
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\]

`p≡3 (mod 4)` では

\[
(1-p^{-2})^2,
\]

`p=2` では

\[
(1-2^{-1})^2,
\]

また

\[
L(1,\chi_4)^2=\left(\frac\pi4\right)^2.
\]

従って二変数residue constantは、Stage12-N1-2kで定義した

\[
\boxed{
\eta
=
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^2
\prod_{q\equiv1(4)}
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4
}
\]

と一致する。

つまり `η` は、density-corrected divisor variables `(b,c)` のrectangle main coefficientそのものである。

---

## 6. density-corrected rectangle lemma

`α(q^j)=2+O(q^{-1})` であり、Stage12-N1-3aと同じ一変数factorizationおよびcoprime cross correctionが成立する。

従って、Stage12-N1-3aのproofを `β` から `α` へそのまま行うと、任意の固定

\[
0<\varepsilon<\frac18
\]

に対し

\[
A_\alpha(R,S)
:=
\sum_{b\le R,c\le S}a(b,c)
\]

は

\[
\boxed{
A_\alpha(R,S)
=
\eta RS
+O_\varepsilon\!\left(
RS\{E_{\alpha,*}(R^{1/2})+E_{\alpha,*}(S^{1/2})\}
+R^{3/4+\varepsilon}S
+RS^{3/4+\varepsilon}
\right)
}
\]

を満たす。

ここで `E_{α,*}` は対応する一変数zero-free-region errorの単調包絡線であり、retained regionでは任意の固定対数冪より小さい。

この補題の証明で必要な変更はlocal coefficient `β(q^j)` を `α(q^j)` に置き換えることだけで、weighted cross normの収束領域と大係数尾部の指数はStage12-N1-3aと同じである。

---

## 7. 二変数Stieltjes移送と `1/12`

算術モデル和をStieltjes積分で書く。

\[
W_L(x,y)
:=
\frac{[L-2\max(\log x,\log y)]_+}{xy}.
\]

すると

\[
\sum_{(b,c)=1}
\frac{\alpha(b)\alpha(c)}{bc}
\Phi_L(\log b,\log c)
=
\iint W_L(x,y)\,dA_\alpha(x,y).
\]

主項measure `η dx dy` を代入すると

\[
\eta
\int_1^{e^{L/2}}
\int_1^{e^{L/2}}
\frac{[L-2\max(\log x,\log y)]_+}{xy}
\,dx\,dy.
\]

\[
y_1=\log x,
\qquad
y_2=\log y
\]

と変数変換すればJacobianは

\[
\frac{dx\,dy}{xy}=dy_1dy_2.
\]

よって積分は

\[
\eta
\int_{y_1,y_2\ge0\atop2\max(y_1,y_2)<L}
(L-2\max(y_1,y_2))\,dy_1dy_2.
\]

対角はmeasure zeroなので対称性を用いると

\[
2\eta
\int_0^{L/2}
\int_0^{z}
(L-2z)\,dy\,dz
=
2\eta
\int_0^{L/2}
z(L-2z)\,dz.
\]

直接計算して

\[
2
\left[
\frac{Lz^2}{2}-\frac{2z^3}{3}
\right]_{0}^{L/2}
=
\frac{L^3}{12}.
\]

従って

\[
\boxed{
\iint W_L(x,y)\,\eta dxdy
=
\frac{\eta}{12}L^3.
}
\]

外側のarchimedean factor `B/π^2` を戻すと

\[
\boxed{
\mathcal M_{\rm model}(B)
\sim
\frac{\eta}{12\pi^2}B(\log B)^3.
}
\]

Stage12-N1-2kのlocal identity `η=πκ` を用いれば

\[
\frac{\eta}{12\pi^2}
=
\frac{\kappa}{12\pi}.
\]

この節により、**kernel mainへ到達した後のStieltjes計算と係数 `1/12` は閉じる**。

---

## 8. rectangle errorのStieltjes適合性

対数dyadic box

\[
\mathcal B(R,S)=[R,2R]\times[S,2S]
\]

上で `W_L` は区分的 `C^2` であり、対角またはsupport境界を横切るboxは有限個のsubboxへ切る。

box内部では

\[
|W_L|
+R|\partial_xW_L|
+S|\partial_yW_L|
+RS|\partial_{xy}W_L|
\ll
\frac{L+1}{RS}.
\]

従って二変数部分和分で現れる境界値・一次変分・混合変分をまとめたノルムは

\[
\boxed{
\|W_L\|_{{\rm PS},\mathcal B}
\ll
\frac{L+1}{RS}.
}
\]

Stage12-N1-3a型のpower errorを掛けると、box寄与は

\[
\ll
(L+1)
\left(
R^{-1/4+\varepsilon}
+S^{-1/4+\varepsilon}
\right).
\]

retained divisor regionを

\[
\min(R,S)
\ge
S_0
:=
\exp\!\left(\frac12(\log B)^{1/4}\right)
\]

とすれば、これは任意の固定対数冪より小さい。多項対数個のboxを合計しても `o(L^3)` である。

一方、`min(R,S)<S_0` のshallow divisor regionのmain volumeは

\[
O\!\left(L^2\log S_0\right)
=
O(L^{9/4})
=o(L^3).
\]

zero-free-region errorも同じboxwise normでさらに小さい。

従って、density-corrected rectangle lemmaから算術モデル和へのStieltjes移送誤差は

\[
o(L^3)
\]

で閉じる。

ここで閉じたのは `K_B^{main}` を使う**算術モデル**であり、exact kernel `K_B` との差ではない。

---

## 9. diagonal、arc、floorの位置づけ

### 9.1 divisor-variable diagonal

Stieltjes積分中の `b=c` は二次元measure zeroであり、離散寄与も一変数和になるためlower-log orderである。ただし、元のorientation境界は `b=c` ではなく `bu=cv` であり、これはexact geometric kernel内で処理しなければならない。

### 9.2 radial arc

radial cutoff

\[
b^2u^2+c^2v^2
\le
\lambda(u,v)B
\]

を横切るarc discrepancyもexact geometric kernel remainder `R_B(b,c)` の一部である。rectangle modelだけでは閉じない。

### 9.3 floor endpoint

height floorによる `O(1)` per `(r,s)` errorはresidue mainとは分離され、Stage12-N1-3bのouter bookkeepingおよび最終統合稿で扱う。`L^3/12` のStieltjes計算へ混入させない。

---

## 10. 現在残ったgeometric kernel lemma

MAJOR-03を完全に閉じるには、次を証明する必要がある。

### 必要補題 3c.G

\[
\mathcal K_B(b,c)
=
\frac{\rho(bc)}{\pi bc}
[L-2\max(\log b,\log c)]_+
+\mathcal R_B(b,c)
\]

であり、

\[
\boxed{
\sum_{b,c\ge1\atop(b,c)=1}
\beta(b)\beta(c)
\mathcal R_B(b,c)
=o((\log B)^3)
}
\]

が成り立つ。

必要な一様性は、次を同時に含む。

- anisotropy `b/c` が極端な場合;
- primitive condition `(u,v)=1`;
- side exclusions `(u,c)=1`, `(v,b)=1`;
- parity-dependent weightとradial cutoff;
- orientation boundary `bu=cv`;
- arc boundary;
- `b,c` 全体のweighted average。

素朴なMöbius inclusionとper-`(b,c)` perimeter errorでは、divisor-lossを伴う可能性があり、そのまま `β(b)β(c)` で総和すると `B(log B)^3` と同次数まで戻る危険がある。従って、現在の資料だけでこの平均誤差を閉じたとは言えない。

候補となる修復路は次のいずれかである。

1. congruence-restricted primitive lattice pointsのanisotropic familyに対する平均discrepancy;
2. smooth radial partition後のPoisson / large-sieve平均;
3. `(b,c)` とMöbius variablesを先にまとめるEuler–Stieltjes再編成;
4. exact kernelを直接二変数Mellin表示し、residueとcontour errorを平均評価する方法。

この選択は次の作業で決める。

---

## 11. 判定

本稿で完了した事項:

1. 元変数、divisor variables、倍数変数を含むexact main sumを復元した;
2. radial kernel、height cutoff、parity、orientationを保持した `K_B(b,c)` を定義した;
3. density-corrected coefficient `α=βρ` を導入した;
4. rectangle residue constantが `η` であることをlocal factorごとに確認した;
5. 二変数Stieltjes移送を完全に書き、model kernelから `ηL^3/12` を得た;
6. Stage12-N1-3aの修正版rectangle errorがmodel Stieltjes kernelに適合することを示した;
7. diagonal / arc / floorのうち、exact geometric kernelへ残る部分を明示した。

未完了:

- exact geometric kernel `K_B` からmodel kernel `K_B^{main}` へのweighted average remainder。

従って現在の状態は

```text
MAJOR_01=CLOSED_BY_STAGE12_N1_3A
MAJOR_02=CLOSED_BY_STAGE12_N1_3B
MAJOR_03=PARTIAL_EXACT_REDUCTION_AND_STIELTJES_COMPLETE_GEOMETRIC_KERNEL_OPEN
MAJOR_04=OPEN
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
MERGE_STATUS=DO_NOT_MERGE
NEXT_TASK=STAGE12_N1_3C_GEOMETRIC_KERNEL_LEMMA
```

とする。
