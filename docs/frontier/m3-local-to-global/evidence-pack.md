# K16-C3-M3-LOCAL-TO-GLOBAL 証拠・数式パック
## 外部AI向け・repoアクセス不要版

この文書は研究指示書の companion evidence pack。ここに書かれた「既知」は、元repository内で既に監査済みの内容として扱う。外部AIはこれらを再証明する必要はないが、研究上必要なら独立チェックしてよい。

---

# A. Population definitions

## A1. Physical host

\[
\mathcal U(B)=\{(a,b,c)\in\mathbf Z_{>0}^3:
0<a<b<c,\ \gcd(a,b,c)=1,\ R=\sqrt{a^2+b^2+c^2}\le B\}.
\]

face predicates:

```text
F_ab = [a^2+b^2 is an integer square]
F_ac = [a^2+c^2 is an integer square]
F_bc = [b^2+c^2 is an integer square]
S    = [R is an integer]
```

## A2. Euler-brick population

\[
M_3(B)=
\#\{(a,b,c)\in\mathcal U(B):F_{ab}=F_{ac}=F_{bc}=1\}.
\]

## A3. Perfect-cuboid population

\[
P(B)=
\#\{(a,b,c)\in\mathcal U(B):
F_{ab}=F_{ac}=F_{bc}=S=1\}.
\]

したがって

\[
P(B)\le M_3(B)
\]

であり、

\[
P(B)/M_3(B)
\]

が literal final survival ratio。

global scaleは未知。

---

# B. Current global M3 theorem surface

certified:

\[
\liminf_{B\to\infty}
\frac{M_3(B)}{B^{1/3}}
\ge
\frac{27}{40\pi^2}>0.
\]

任意の固定 `0<eta<1/46` に対して

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

finite baseline examples:

```text
M3(2000)=7
M3(10000)=18
M3(50000)=42
M3(200000)=82
M3(1000000)=219
```

これらはfinite factsであり、asymptotic fittingに使ってはならない。

endpoint finite census:

```text
P(B)=0 for every B<=10^9
```

global:

```text
P(B)=0  NOT PROVED
```

---

# C. Master-Hit global coverage

2 primitive Pythagorean triples:

\[
(U_1,V_1,W_1)=(r^2-s^2,2rs,r^2+s^2),
\]

\[
(U_2,V_2,W_2)=(m^2-n^2,2mn,m^2+n^2).
\]

primitive conditions:

```text
r>s>0, gcd(r,s)=1, opposite parity
m>n>0, gcd(m,n)=1, opposite parity
```

put

\[
g=\gcd(U_1,U_2).
\]

Then

\[
X=\frac{U_1U_2}{g},
\qquad
Y=\frac{V_1U_2}{g},
\qquad
Z=\frac{U_1V_2}{g}.
\]

third-face quantity:

\[
\mathcal M=
(V_1U_2)^2+(U_1V_2)^2.
\]

space quantity:

\[
\mathcal H=
(U_1U_2)^2+(V_1U_2)^2+(U_1V_2)^2.
\]

relations:

\[
g^2(Y^2+Z^2)=\mathcal M,
\]

\[
g^2(X^2+Y^2+Z^2)=\mathcal H.
\]

したがって

```text
Euler brick condition  <=> M is a square
perfect cuboid condition <=> M and H are squares
```

（first two facesはconstructionでsquare）。

### Coverage theorem

任意の primitive Euler brick `(X,Y,Z)` について unique odd edgeを `X` とする。

\[
d=\gcd(X,Y),\qquad e=\gcd(X,Z).
\]

2つの primitive Pythagorean facesから uniquely

```text
X/d = U1, Y/d = V1
X/e = U2, Z/e = V2
```

を得る。

primitivityより

\[
\gcd(d,e)=1.
\]

\[
g=\gcd(U_1,U_2)
\]

なら

\[
d=U_2/g,\qquad e=U_1/g.
\]

よって

\[
(X,Y,Z)=
(U_1U_2/g,\ V_1U_2/g,\ U_1V_2/g).
\]

したがって **every primitive Euler brick is a gcd-normalized Master-Hit**。

これはthin subfamilyではなく global coverage。

---

# D. Physical-to-squareclass crosswalk

set

\[
[x:y:z]=[a^2:b^2:c^2].
\]

six projective Kummer ratios:

\[
\frac yx,\quad
\frac zx,\quad
\frac{x+y}{x},\quad
\frac{x+z}{x},\quad
\frac{y+z}{x},\quad
\frac{x+y+z}{x}.
\]

physical integer edge pointで

\[
y/x=(b/a)^2,
\qquad
z/x=(c/a)^2.
\]

さらに

```text
(x+y)/x square <=> F_ab
(x+z)/x square <=> F_ac
(y+z)/x square <=> F_bc
(x+y+z)/x square <=> S
```

整数について `Q-square` と `integer square` の間にgapはない。

したがってM3上では

```text
x,y,z,x+y,x+z,y+z
```

がglobal squares。

perfect cuboidではさらに

```text
x+y+z
```

がsquare。

---

# E. Seven-form local object

\[
L=(x,y,z,x+y,x+z,y+z,x+y+z).
\]

full local sign-cover liftでは7値が共通local squareclassに入ることが必要。

これは7 independent Bernoulli conditionsではない。

branch arrangementには triple points があり、valuation correlationがある。

---

# F. Odd-prime exact branch law

odd prime `p`。

\[
\epsilon=\chi_p(-1),\qquad
\eta=\chi_p(2).
\]

`A_k(p)`:
`P^2(F_p)` 上で exactly `k` branch lines がvanishし、remaining nonzero branch valuesが一つの共通quadratic characterを持つ reduction points の個数。

既知 exact:

\[
A_1=
\frac34(p-4-\epsilon)
+\frac{1+\epsilon}{8}(p-5)
+\frac{3(1+\epsilon)}{16}(p-11-4\eta-a_E(p)),
\]

\[
A_2=\frac34(1+\epsilon)(1+\eta),
\]

\[
A_3=\frac32(3+\epsilon).
\]

ここで

\[
E:y^2=x^3-x
\]

かつ `a_E(p)` はそのFrobenius trace。

`p=3` にextra branch intersectionはない。

`p=2` のみseparate。

`A0(p)` は次の定義だけでも独立に再構成可能:

> `P^2(F_p)` のbranch-avoiding pointsのうち、7 branch valuesがnonzeroかつ共通quadratic characterを持つ点数。

audit済み asymptotic:

\[
\frac{A_0(p)}{(p-3)^2}
=
\frac1{64}+O(1/p).
\]

---

# G. Odd-prime valuation correlation

eligible reduction cylinder内で

\[
q_0=1,
\]

\[
q_1=\frac1{2(p+1)},
\]

\[
q_2=\frac1{4(p+1)^2}.
\]

triple pointではvanishing branchesは literal に

```text
r, s, r+s
```

なので独立でない。

exact:

\[
q_3(p)=
\frac{
p^2-(3+\chi_p(-1))p+1
}{
8(p+1)^2(p^2+1)
}.
\]

したがって

\[
q_3\ne q_1^3.
\]

これは genuinely joint endpoint information。

各 `F_p` projective cylinderの normalized mass:

\[
\frac1{p^2+p+1}.
\]

full seven-form exact odd-prime local density:

\[
\boxed{
\Delta_p=
\frac{
A_0+A_1q_1+A_2q_2+A_3q_3
}{
p^2+p+1
}
}.
\]

asymptotic:

\[
\Delta_p=\frac1{64}+O(1/p).
\]

### computational validation already done

- exact finite-field enumeratorで odd primes `<100` を検証。
- independent auditで odd primes `<200` を再検証。
- floating arithmetic不使用。

---

# H. Real place

physical chamber:

\[
x>0,\ y>0,\ z>0.
\]

7形式すべてpositive。

したがって

```text
no real squareclass obstruction
```

---

# I. Exact 2-adic density

branch-avoiding Q2 liftでは7 nonzero branch valuesが共通 Q2 squareclassに入ることが必要。

`P^2(F2)` には7 primitive parity cylinders。

surviveするのは unique odd coordinateを持つ3 cylinders。

例: `y` oddとしてscale `y=1`。

\[
X=x/y\in2\mathbf Z_2,
\qquad
Z=z/y\in2\mathbf Z_2.
\]

必要:

```text
X, Z, 1+X, 1+Z, X+Z, 1+X+Z
```

がQ2 squares。

非零Q2 numberがsquare iff

```text
valuation even
odd unit == 1 mod 8
```

`X∈2Z2` について `X` と `1+X` がsimultaneously squareとなるstate:

\[
v_2(X)=2a,\qquad a\ge2,
\]

かつ odd-unit(`X`) ≡ 1 mod 8。

conditional mass:

\[
w_a=2^{-2a-2}.
\]

\[
\sum_{a\ge2}w_a=\frac1{48}.
\]

same for `Z`。

`X+Z` correlation:

```text
a=b        -> fail
|a-b|=1    -> fail
|a-b|>=2   -> pass
```

one surviving parity cylinder success mass:

\[
(1/48)^2
-\sum_{a\ge2}w_a^2
-2\sum_{a\ge2}w_aw_{a+1}
\]

\[
=
\frac1{2304}
-\frac1{3840}
-\frac1{7680}
=
\frac1{23040}.
\]

3 of 7 parity cylinders survive, therefore

\[
\boxed{
\Delta_2=
\frac37\cdot\frac1{23040}
=
\frac1{53760}
}.
\]

よって

```text
TWO_ADIC_LOCAL_OBSTRUCTION_EMPTY = false
```

すなわちQ2で局所空集合ではない。

known local witness:

```text
Euler brick (44,117,240)
```

では

\[
44^2+117^2+240^2=73225\equiv1\pmod8.
\]

これはQ2-space-square witnessだが rational perfect cuboidではない。

---

# J. Critical firewall: Delta_p is not yet an M3 conditional density

`Delta_p` は full seven-form local sign-cover density。

M3 pointでは最初の6形式が global square。

したがって本当に必要なlocal objectは概念的には

\[
\Pr_p(
x+y+z\text{ is locally square}
\mid
x,y,z,x+y,x+z,y+z\text{ are in the M3 local state}
)
\]

に近い。

ただし `M3 local state` のmeasure自体をどう定義するかがglobal parametrizationと絡むため、ambient `P^2(Q_p)` conditional probabilityを自動採用してはいけない。

このconditional normalizationの厳密化自体が有用なpartial result。

---

# K. Separate Stage20 local blocker law — DO NOT MULTIPLY

別問題として、selected two-face toric host上のthird-face completionには

\[
\delta_2=\frac29,
\]

odd `p`:

\[
\delta_p=
\frac{2(p-\chi_4(p))}{p^2+6p+1}
=
\frac2p+O(p^{-2}).
\]

これは Stage20 Euler-brick selectionを生む local blocker。

Stage29 seven-form lawとはbase measureが違う。

禁止:

\[
\delta_p\cdot\Delta_p
\]

を独立factorとして使うこと。

---

# L. Toric / K3 geometry available

common shared-edge two-face host:

\[
Y=
\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1).
\]

known:

```text
Y is smooth proper split toric surface
dim Y = 2
rank Pic(Y) = 6
```

third-face completionは generically degree-2 K3 cover。

physical height interfaceは既存研究で matched。

ただし rational points on K3 cover = M3 の exact conditional measureについて general asymptotic theoremはない。

---

# M. Huang v3 machinery already used elsewhere

source metadata retained in project:

```text
Zhizhong Huang
arXiv:2111.01509v3
revision date: 17 Jul 2026
```

projectで利用した theorem species:

1. effective equidistribution with polynomial dependence on finite adelic covering level
2. Selberg sieve for local conditions detected modulo uniformly bounded prime power
3. split toric varietiesで condition (EE)
4. generically finite cover degree >1 の adelic imageに logarithmic thinning

`Y` では

```text
dim Y = 2
rank Pic(Y) = 6
gamma = 8 + epsilon
```

別selectorで mod-`p^2` bad subsetを使い、proof-level conservative error

\[
N^{44+\varepsilon}(\log B)^{-1/2+\varepsilon}
\]

と

\[
G(N)\gg(\log N)^2
\]

を組み、

\[
N=(\log B)^\lambda,\qquad 0<\lambda<1/88
\]

で growing-prime sieveを成立させた実績がある。

### しかし本kernelにはそのまま使えない理由

Huang theoremは ambient toric host上のequidistributionを与える。

本kernelが必要なのは

```text
already conditioned on being a primitive canonical Euler brick M3
```

というmeasure。

project内 hostile review の結論:

```text
Browning–Loughran / Huang ambient sieve statements
do not preserve the exact conditional M3 physical measure.
```

したがって新規adapterが必要。

---

# N. Existing density/survival results around M3

nested hosts:

\[
H_{\ge1}=M_1\sqcup M_2\sqcup M_3,
\]

\[
H_{\ge2}=M_2\sqcup M_3,
\]

\[
H_{\ge3}=M_3.
\]

space intersections:

\[
S\cap H_{\ge1}=N_1\sqcup N_2\sqcup P,
\]

\[
S\cap H_{\ge2}=N_2\sqcup P,
\]

\[
S\cap H_{\ge3}=P.
\]

known:

\[
\frac{N_1+N_2+P}{M_1+M_2+M_3}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

and

\[
B^{-3/4}(\log B)^{-5}
\ll
\frac{N_2+P}{M_2+M_3}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

also

\[
\frac{P(B)}{M_2(B)+M_3(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

しかし最後だけは

\[
\frac{S\cap H_{\ge3}}{H_{\ge3}}
=
\frac{P}{M_3}
\]

で、global scale unknown。

これが「一段手前まではdensity theoremがあるが、M3内部の最後のsurvivalだけ未解決」という位置づけ。

---

# O. Known limitations / failed promotions

以下は既に「そのままでは足りない」と判定済み。

### O1. ambient toric density
exact M3 measureをpreserveしない。

### O2. fixed finite primes only
`B->∞` with fixed `S`, then enlarge `S` というtwo-limit statementだけでは growing-prime quantitative sieveにならない。

### O3. individual fiber arithmetic
fixed fiberのChabauty / Mordell-Weilは uniform M3 theoremではない。

### O4. thin family closure
Saunderson等のexplicit infinite familyはM3全体ではない。

### O5. finite endpoint census
`P=0` through `1e9` はglobal theoremではない。

### O6. local nonemptiness / local obstruction absence
local solubleだからglobal pointがある、またはlocal density positiveだからglobal density positive、とは言えない。

---

# P. Suggested exact finite-field experiment for new research

新規研究の最初のcomputational experimentとして、odd prime `p` ごとに Master-Hit parameters modulo `p` または `p^k` を列挙し、

```text
primitive Pythagorean pair 1
primitive Pythagorean pair 2
Master = square
H-total squareclass
gcd(U1,U2) local behavior
```

のjoint distributionを測る。

特に

\[
\Pr(
\mathcal H\in(\mathbf F_p^\*)^2
\mid
\mathcal M\in(\mathbf F_p^\*)^2,
\text{ admissible primitive-Pythagorean states}
)
\]

をまず見る。

ただしfinite-field experimentは theoremではない。目的は:

- correct conditional local factor の候補を見つける
- ambient `Delta_p` との差を確認する
- character-sumで証明可能な形を発見する

こと。

---

# Q. Potential theorem shape worth aiming for

最も価値が高い中間定理の例:

> For every fixed squarefree modulus `q` outside a finite bad set and every admissible local state `ω mod q`, the number of primitive canonical Master-Hit Euler bricks of Euclidean height `R<=B` realizing `ω` is
>
> \[
> c_\omega(q)\,M_3(B)+O(E(B,q)),
> \]
>
> uniformly for `q<=Q(B)`,
>
> with \(\sum_\omega c_\omega(q)=1\) and multiplicative local compatibility.

これが得られれば、7-squareclass conditionに対して Selberg / large sieve を構築できる可能性がある。

現状 `M3(B)` 自体に asymptotic formula がないので、絶対countのmain termより

\[
\#M_3(B;\omega)
\le
\alpha_\omega(q)M_3(B)+E(B,q)
\]

のような relative inequality でも十分価値がある。

---

# R. Internal provenance memo

元projectでの主な根拠ファイル名。外部AIはアクセス不要。

```text
docs/frontier/13-active-kernels.md
stages/stage20/final.md
stages/stage29/29-04/result.md
stages/stage29/29-08/result.md
stages/stage29/29-09/result.md
stages/stage29/29-12/result.md
stages/stage29/29-12/theorem-dependency-ledger.json
stages/stage29/29-15/bounded-execution.md
stages/stage29/29-15/post-work-audit.md
stages/stage28/28-40/huang-v3-growing-sieve-adapter.md
```

研究時はこのpack本文をauthorityとして使用してよい。
