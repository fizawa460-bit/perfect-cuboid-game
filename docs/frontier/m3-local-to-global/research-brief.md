# K16-C3-M3-LOCAL-TO-GLOBAL 研究指示書
## 外部AI向け・repoアクセス不要版

### 0. 研究ミッション

完全直方体問題の途中段階として、**primitive canonical Euler brick 集団 `M3(B)` の上での局所 squareclass 条件を、同じ `M3` counting measure 上の大域的な分布・sieve statement に移す**ことが目的である。

この課題は「局所密度を計算する課題」ではない。odd prime、実場所、2-adic の主要局所計算は既に完了している。未解決なのは、それらを

- primitive
- canonical ordering
- Euclidean height `R<=B`
- one object = one count
- Euler-brick conditionを既に満たす `M3`

という**正確な物理集団**へ移す global adapter である。

Stage29 frozen frontier での分類は **Class 3 = new theorem / genuinely new proof mechanism required**。

---

## 1. Exact target population

\[
\mathcal E_3(B)=
\{(a,b,c)\in\mathbf Z_{>0}^3:
0<a<b<c,\ \gcd(a,b,c)=1,\ R=\sqrt{a^2+b^2+c^2}\le B,
\]
\[
a^2+b^2,\ a^2+c^2,\ b^2+c^2
\text{ are all integer squares}\}.
\]

\[
M_3(B)=\#\mathcal E_3(B).
\]

重要:

- `M3` は Euler brick population。
- `R` の整数性は要求しない。
- perfect cuboid population `P(B)` は `M3(B)` のうちさらに `R∈Z` を満たすもの。
- global `P(B)=0` は未証明。
- exact finite censusでは `P(B)=0` through `B<=10^9` だが、これは有限計算であり非存在証明ではない。

現在の certified global corridor:

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}
\ge \frac{27}{40\pi^2}>0,
\]

および任意の固定 `0<\eta<1/46` に対して

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

真の growth exponent、asymptotic formula、`P(B)/M3(B)` は未知。

---

## 2. このkernelの exact wall

現在不足しているものは次の一文に集約できる。

> correlated seven-squareclass local information を、exact primitive canonical `M3(B)` under `R<=B` に対して uniform local-to-global / equidistribution / large-sieve theorem として移す。

最低限、以下のどれかが欲しい。

### Target A: fixed finite prime set equidistribution

固定有限 prime set `S` と、各 `p∈S` の local state `Ω_p` に対し、

\[
\frac{
\#\{E\in M_3(B): E\text{ realizes }\Omega_p\ \forall p\in S\}
}{
M_3(B)
}
\to
\prod_{p\in S}\mu_p(\Omega_p)
\]

型の theorem を exact physical `M3` measure で証明する。

### Target B: quantitative uniformity

上記に modulus / finite prime set に依存する explicit error term を付ける。

\[
\#M_3(B;\Omega_S)
=
M_3(B)\prod_{p\in S}\mu_p(\Omega_p)
+
O(\mathcal E(B,S)).
\]

prime cutoff `z=z(B)` を増大できる程度なら非常に価値が高い。

### Target C: same-measure sieve

`M3` 上で追加 squareclass condition を課した集合に対し、nontrivial upper/lower/survival bound を直接証明する。

### Target D: terminal-scale bridge

もし最終的に

\[
P(B)/M_3(B)
\]

の nontrivial scale まで出せたら、これは次kernel `TERMINAL-P-OVER-M3` への直接入力になる。ただし `P/M3 -> 0` だけでは `P=0` は従わない。

---

## 3. 絶対にやり直さなくてよいこと

以下は既に exact / audited。

1. odd-prime seven-form branch combinatorics。
2. odd-prime triple-point valuation correlation。
3. odd-prime exact local density `Delta_p`。
4. real positive chamber に local obstruction がないこと。
5. 2-adic exact state automaton。
6. \(\Delta_2=1/53760\)。
7. physical squareclass crosswalk。
8. primitive Euler brick の global Master-Hit coverage。

これらを再計算して「新成果」としてはいけない。

---

## 4. 最重要: ambient density と M3 density を混同しない

seven-form base は

\[
L=(x,y,z,x+y,x+z,y+z,x+y+z).
\]

physical edge pointでは

\[
[x:y:z]=[a^2:b^2:c^2].
\]

したがって `M3` 上では

```text
x, y, z
x+y, x+z, y+z
```

の最初の6形式はすでに global Q-squares であり、最後の

```text
x+y+z
```

が space-diagonal predicate。

一方、Stage29で計算済みの `Delta_p` は **full seven-line local sign-cover object** の local density である。

よって次の推論は禁止:

```text
ambient Delta_p
= conditional probability of space-square inside M3
```

これは未証明。

必要なら、
- six-form local locus
- seven-form local locus
- そのconditional ratio
を exact `M3` parameter measure から再定義すること。

`Delta_p` は重要な入力だが、**そのまま M3 survival factor ではない**。

---

## 5. 最も有望な既存の global coverage mechanism: Master-Hit

任意の primitive Euler brick は、2本の primitive Pythagorean triples から exact に回収できる。

2本を

\[
(U_1,V_1,W_1)=(r^2-s^2,2rs,r^2+s^2),
\]

\[
(U_2,V_2,W_2)=(m^2-n^2,2mn,m^2+n^2),
\]

とする。各pairは通常の primitive Pythagorean 条件

```text
gcd(r,s)=1, opposite parity, r>s>0
gcd(m,n)=1, opposite parity, m>n>0
```

を満たす。

\[
g=\gcd(U_1,U_2)
\]

として

\[
X=\frac{U_1U_2}{g},\qquad
Y=\frac{V_1U_2}{g},\qquad
Z=\frac{U_1V_2}{g}.
\]

primitive Euler brick `(X,Y,Z)` はこの形で global coverage される。

第三face条件は

\[
Y^2+Z^2 \text{ is a square}
\]

すなわち

\[
\mathcal M=
(V_1U_2)^2+(U_1V_2)^2
\]

がsquareであることと同値。

space-diagonal条件は

\[
X^2+Y^2+Z^2\text{ is a square}
\]

すなわち scaling 前では

\[
\mathcal H=
(U_1U_2)^2+(V_1U_2)^2+(U_1V_2)^2
\]

がsquareであることと同値。

### なぜこのrepresentationが重要か

primitive Euler brick `(X,Y,Z)` には unique odd edge があり、そのodd edgeを共有する2つの primitive Pythagorean face から、上記の2本の primitive triples が回収される。したがってこれは単なるthin subfamilyではなく、**全 primitive Euler brick の exact coverage**。

このため本kernelの第一候補は:

> Master-Hit parameter space 上で、`M3` 条件 `M square` を既に課した集団について、`H` の local squareclass / congruence states の equidistribution を証明する。

ambient `P^2` から直接攻めるより、こちらの方が exact global coverage を最初から保持できる可能性が高い。

---

## 6. 推奨研究ルート A: Master-Hit congruence/equidistribution

### A1. parameter-to-object multiplicityを固定

まず以下を theorem-level に明示する。

- primitive `(r,s)` / `(m,n)` conditions
- sign/order symmetries
- unique odd edge
- canonical reorder `0<a<b<c`
- `g=gcd(U1,U2)` normalization
- 1つの `M3` object が parameter tuples から何回現れるか
- physical height `R<=B` が parameter space でどの region になるか

ここを曖昧にしたまま density を論じない。

### A2. finite modulus distribution

固定 modulus `q` に対し、Master-Hit parameter tuples modulo `q^k` を分類し、

```text
primitive Pythagorean conditions
gcd(U1,U2)
Master square condition
space squareclass state
```

のjoint distributionを調べる。

重要なのは「Master square conditionでconditionした後」のspace state。

### A3. global lattice/counting theorem

必要なのは raw parameter boxes ではなく、`R<=B` とprimitive/canonical normalizationを保つ count。

候補species:

- geometry-of-numbers + Möbius inversion
- adelic/lattice equidistribution
- large sieve on polynomial images
- square-sieve after conditioning on `Master=square`
- fibration by one Pythagorean pair
- height zeta / harmonic analysis if exact hostを作れる場合

### A4. finite-S theoremから growing-primeへ

fixed `S` ができたら、error dependenceを精密化して

\[
z=z(B)
\]

を増やせるか調べる。

---

## 7. 推奨研究ルート B: K3 / toric host の conditional transfer

Euler-brick third-face completionは、共通two-face toric host

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

上の generically degree-two K3 cover として扱える。

既知:

```text
dim Y = 2
rank Pic(Y) = 6
physical Euclidean height is matched to the frozen toric/anticanonical height interface
```

Huang v3 の toric equidistribution / Selberg sieve は、ambient toric host上では強力。

しかし現在までの hostile review では:

> Browning–Loughran / Huang ambient sieve statements do not preserve the exact conditional M3 physical measure.

と判定済み。

したがってこのルートで必要なのは、

```text
toric host Y
 -> degree-2 K3 lift condition
 -> rational Euler-brick points M3
 -> seven-squareclass local state
```

を同じ measure でつなぐ conditional theorem。

単に Huang を引用して ambient `Y(Q)` を数えるだけでは不合格。

---

## 8. 使える Huang v3 machinery

既存研究で使った theorem species:

- effective equidistribution with polynomial dependence on finite adelic covering level
- Selberg sieve for local conditions detected modulo a uniformly bounded prime power
- split toric varietyでの explicit equidistribution exponent
- generically finite cover degree `>1` の adelic image に対する logarithmic thinning

実際に `Y=Bl_4(P1xP1)` では

```text
dim Y = 2
rank Pic(Y) = 6
gamma = 8 + epsilon
```

として、別のselector問題で mod-`p^2` bad events と growing cutoff

\[
N=(\log B)^\lambda,\qquad \lambda<1/88
\]

を組み、dimension-2 Selberg sieveを成立させた実績がある。

これは本kernelにそのまま適用できるわけではないが、以下の部品は再利用候補:

```text
bounded prime-power detectability
adelic level dependence
primitive handling
height comparison
bad-prime removal
Selberg denominator G(N)
growing-prime error bookkeeping
```

---

## 9. 推奨研究ルート C: fibration

Master-Hit / Peschmann 側には globally covering Euler-marginal fibration がある。

各 fixed parameter pairに対する genus-one / elliptic machineryは存在するが、

```text
bounded Mordell-Weil enumeration
```

はglobal coverageにならない。

このkernelでfibrationを使うなら、

- family-uniform rank/control
- uniform congruence distribution
- specialization with quantitative height control

のどれかが必要。

これは `MOVING-FIBER-ARITHMETIC` kernel と近く、重複研究になりやすいので第一候補ではない。

---

## 10. やってはいけないルート

### 禁止1: local Euler productをそのままglobal densityと宣言

```text
prod_p Delta_p
```

を formal に書くだけでは theorem ではない。

### 禁止2: ambient `P^2` densityを M3 densityとする

M3は6 square conditionsをglobalに既に満たした非常に特殊なsubset。

### 禁止3: Stage19/20 local lawsとの掛け算

Stage20側には別のthird-face blocker law

\[
\delta_2=2/9,
\]

\[
\delta_p=
\frac{2(p-\chi_4(p))}{p^2+6p+1}
=
2/p+O(p^{-2})
\]

がある。

これは selected two-face toric host 上の別measure。

Stage29 seven-form `Delta_p` と掛けてはいけない。

### 禁止4: Saunderson等のthin subfamilyだけでclosure

subfamily equidistributionは sanity check にはなるが、全M3をcoverしない限りkernel closureではない。

### 禁止5: finite computationをglobal theoremへ昇格

有限 prime、有限 height、有限 parameter windowは evidence にすぎない。

### 禁止6: `P/M3 -> 0` から非存在を結論

density zeroはemptinessではない。

---

## 11. 成果判定

### Level 0 — 不合格
- local density再計算のみ
- ambient sieveのみ
- finite experimentsのみ
- heuristic Euler productのみ

### Level 1 — 有用partial
- Master-Hit parameter multiplicity/height contractを完全固定
- exact conditional local factorsを導出
- fixed modulusでのparameter-state countをrigorousに証明

### Level 2 — kernel前進
- fixed finite prime setに対する same-M3 equidistribution theorem
- quantitative congruence count with explicit error
- physical `R<=B`, primitive, canonical を完全保持

### Level 3 — 強い前進
- growing-prime uniformity
- Selberg/large-sieve bound on exact M3
- nontrivial same-M3 survival decay

### Level 4 — terminal input
- `P(B)/M3(B)` のexplicit asymptotic/corridor/power-log saving
- ただし非存在claimは不可

---

## 12. 最初の具体的作業

最初に以下を順に実行することを推奨する。

1. Master-Hit representationを研究の主座標として採用できるか検証。
2. 1 primitive Euler brickあたりのparameter multiplicityを厳密化。
3. `R<=B` を `(r,s,m,n)` の inequality として上下から固定。
4. fixed odd prime `p` について、`Master square` でconditionした parameter tuples の `H` squareclass distributionを symbolic / finite-field algebraで計算。
5. そのlocal conditional lawが、既知のambient seven-form `Delta_p` とどう関係するかを明示。
6. fixed modulus `q` での equidistribution theorem候補を選定。
7. primitive/gcd条件を Möbius inversion 等で戻す。
8. error termが得られたら growing-prime sieveへ進む。

最初から「perfect cuboid非存在」を証明しようとしない。まず **same-M3 local-to-global theorem** を作ること。

---

## 13. 外部AIへの最終問い

> primitive canonical Euler brick 全体を exact にcoverする Master-Hit parametrizationを用い、`Master` がsquareであるという Euler-brick conditionでconditionした後の `H-total` squareclass statesについて、fixed finite modulus / fixed finite prime setでの equidistributionを証明できるか。さらにその誤差をuniform化して growing-prime Selberg/large sieveへ接続できるか。ambient `P^2` / toric densityへ逃げず、`R<=B`, gcd=1, canonical multiplicityを保持せよ。
