# 36R-01 REVIEW BUNDLE — C3_p の 2-被覆降下の類の「形の定理」（外部査読用、自己完結）

作成 2026-10-14。状態：未査読の候補。AI による作成で、人手の確認はない。RESULTS には載せていない。

## 査読者へのお願い
1. §2 の表の各行について、§3 の証明に穴がないかを確認してください。特に：
   (a) 対称性 t→1/t で v_ℓ(t)≥0 に帰着してよいか（各行の主張が (1↔2, 3↔4) の入れ替えで不変か）。
   (b) ℓ | P−Q の行：「v(G3)<n なら G1/G3∈1+ℓZ_ℓ」と「v(G3)≥n なら G2≡G4≡u0」の2つの場合分けで尽くされているか。
   (c) ℓ | H の行：差 p_j²−p_k² の付値が6組すべてちょうど n であること（差の表）。
   (d) 「型」が排他的であること（a, b, a±b, P±Q, H の奇素因数が互いに素）。
2. 系 1 の δ の形（h, α, β, μ1, μ2, ν1, ν2 と 2 の冪）が表から正しく出ているか。
3. 系 3（端点の類）で使っている「端点の点では δ1=δ2」は、別ファイル 36R-00 の命題（端点 ⇒ G1G2 が平方）に依存します。
   この束の中では「δ1=δ2 を満たす類については」という条件つきの主張として読んでください。
4. 反例の探し方：適当な p=a/b、奇素数 ℓ、t∈Q_ℓ で ∏G_j(t) が平方になるものを取り、表の条件を直接確かめる。
   付録のスクリプトはこれを厳密な局所像の計算で網羅的に行います。

## 1. 設定

p=a/b（a,b 互いに素な整数、p∉{0,±1}）、e=a+b, f=a−b, P=a²−b², Q=2ab, H=a²+b², c=(p+1)/(p−1)=e/f。
C3_p : y² = G1·G2·G3·G4、G_j(t) = t² + p_j²、(p_1,p_2,p_3,p_4) = (p, 1/p, c, 1/c)。
1G の整数形式とは Q1=b²v²·G1, Q2=a²v²·G2, Q3=(f²v²/g)·G3, Q4=(e²v²/g)·G4（t=u/v、g は平方）で、
平方因子なし部分は同じ：δ_j = [G_j(t)] ∈ Q*/Q*²。G_j>0 なので δ_j は正の平方因子なし整数、δ1δ2δ3δ4 は平方。

奇素数 ℓ は a, b, a−b, a+b, P−Q, P+Q, H のうち高々1つしか割らない（どの2つの最大公約数も 4 の約数）。
これを ℓ の **型** と呼ぶ。どれも割らない奇素数を「良い素数」と呼ぶ。

## 2. 定理（形の定理、全ての p、無条件）

(t,y)∈C3_p(Q)、γ_j := G_j(t) の Q_ℓ*/Q_ℓ*² での類とする。奇素数 ℓ について：

| ℓ の型 | 成り立つこと |
|---|---|
| ℓ ≡ 3 (mod 4)（型は問わない） | v_ℓ(G_j(t)) は4つとも偶数 |
| 良い素数 | v_ℓ(G_j(t)) は4つとも偶数 |
| ℓ \| ab | γ1 = γ2 = 1、γ3 = γ4 |
| ℓ \| a²−b² | γ3 = γ4 = 1、γ1 = γ2 |
| ℓ \| P−Q | γ1 = γ3、γ2 = γ4、かつ ℓ は δ1,δ3 の組と δ2,δ4 の組の両方は割らない |
| ℓ \| P+Q | γ1 = γ4、γ2 = γ3、かつ ℓ は δ1,δ4 の組と δ2,δ3 の組の両方は割らない |
| ℓ \| H | v_ℓ(G_j(t)) の偶奇は4つとも同じ |

**系 1（Selmer 集合の形）.** 全ての p と全ての有理点について
```text
δ = ( 2^{ε1}·h·α·μ1·ν1,  2^{ε2}·h·α·μ2·ν2,  2^{ε3}·h·β·μ1·ν2,  2^{ε4}·h·β·μ2·ν1 )
```
- h | H、α | (a²−b²)、β | ab、μ1μ2 | (P−Q)、ν1ν2 | (P+Q)（すべて平方因子なし、互いに素）
- h, α, β, μ_i, ν_i の素因数はすべて ≡ 1 (mod 4)（μ_i, ν_i は ≡ 1 (mod 8)）
- ε_j∈{0,1}、ε1+ε2+ε3+ε4 は偶数

したがって Sel(C3_p) ⊆ T(type(p)) := 上の形の δ の集合で、
`|T| ≤ 8 · 2^{ω₁(H)+ω₁(a²−b²)+ω₁(ab)} · 3^{ω₁(P²−Q²)}`（ω₁ は ≡1 mod 4 の素因数の個数）。
自明類は (1,1,1,1)、境界類は h=sqf(H) で (h,h,2h,2h)。

**系 2（組曲線のひねりは h を見ない）.** δ_jδ_k の奇数部分は
`δ1δ2, δ3δ4 → μ1μ2ν1ν2`、`δ1δ3, δ2δ4 → αβ·ν1ν2`、`δ1δ4, δ2δ3 → αβ·μ1μ2`。
1G の6本の組曲線 `δ_jδ_k·Y² = X(X+p_j²)(X+p_k²)`（X=t²）のひねりは H の素因数を含まない。
同じ (ε, α, β, μ, ν) で h だけが違う類は、6本とも同じ曲線になる。

**系 3（端点に関係する類）.** 端点の点（36R-00：G1G2 と G3G4 が個別に平方、つまり δ1=δ2, δ3=δ4）では
μ1=μ2=ν1=ν2=1。したがって端点の類は
```text
δ = ( 2^ε·h·α, 2^ε·h·α, 2^ε'·h·β, 2^ε'·h·β )
```
の形に限られ、P±Q の素因数は現れない。このとき X=t² は p だけで決まる2本の曲線
`Y²=X(X+p²)(X+p⁻²)`、`Y²=X(X+c²)(X+c⁻²)`（ひねりなし）の有理点になる。

**系 4（Legendre 条件。表の「類が等しい／自明」の部分）.** 全ての p と全ての有理点について：
- 奇素数 ℓ | ab ならば δ1, δ2 は Q_ℓ の平方（ℓ∤δ1δ2 かつ (δ1/ℓ)=(δ2/ℓ)=1）、δ3δ4 も Q_ℓ の平方。
- 奇素数 ℓ | a²−b² ならば δ3, δ4 は Q_ℓ の平方、δ1δ2 も Q_ℓ の平方。
- 奇素数 ℓ | P−Q ならば δ1δ3, δ2δ4 は Q_ℓ の平方。ℓ | P+Q ならば δ1δ4, δ2δ3 は Q_ℓ の平方。

これは系 1 の形の δ に対する明示的な有限個の条件で、p の素因数分解だけから判定できる（ℓ≡3 mod 4 の素数にも効く）。
例：境界類 (h,h,2h,2h)、h=sqf(H) では、ℓ | a なら H≡b² で条件は満たされる（境界類は常に生き残る。実際に点がある）。

## 3. 証明

共通の道具：(i) ℓ が奇数なら 1+ℓZ_ℓ ⊂ Q_ℓ*²。(ii) γ1γ2γ3γ4=1（y²=∏G_j）。
(iii) 対称性 t→1/t：G1(t)=(tp)²G2(1/t)、G3(t)=(tc)²G4(1/t)。表の各行は (1↔2, 3↔4) の入れ替えで不変なので、
v_ℓ(t)≥0 としてよい。

**ℓ≡3 (mod 4).** G_j(t)=(u²+p_j²v²)/v² は有理数の二平方和。ℓ≡3 (mod 4) では二平方和の付値は偶数。
（1P の補題 A はこの一行で出る。型による場合分けは不要。）

**良い素数.** p_j は全て単数、p_j²−p_k² も全て単数（下の表）。v(G_j(t))>0 なら k≠j で
G_k(t)≡p_k²−p_j² は単数。(ii) より v(G_j(t)) は偶数。

**ℓ | a（v(p)=n>0、c は単数）.** G2=p⁻²(1+p²t²) で 1+p²t²∈1+ℓZ_ℓ、よって γ2=1。
v(t)=0 なら G1=t²(1+p²/t²) で γ1=1、(ii) より γ3=γ4。
v(t)>0 なら G3=c²(1+t²/c²)、G4=c⁻²(1+c²t²) で γ3=γ4=1、(ii) より γ1=1。
ℓ | b は p→1/p（G1↔G2、c→−c で G3,G4 は不変）で同じ。

**ℓ | a∓b.** c または 1/c の付値が正で p は単数。上の議論を (1,2)↔(3,4) を入れ替えて使う。

**ℓ | P−Q.** p−c=(p²−2p−1)/(p−1) なので v(p−c)=v(P−Q)=n>0。p,c は単数、u0:=p⁻²−p² も単数（ℓ∤PH）。
v(G3(t))<n なら G1/G3=1+(p²−c²)/G3∈1+ℓZ_ℓ で γ1=γ3、(ii) より γ2=γ4。
v(G3(t))≥n なら t²≡−c²≡−p² (mod ℓ) で、G2(t)≡G4(t)≡u0 は同じ単数剰余、よって γ2=γ4=[u0]、(ii) より γ1=γ3。
「両方の組は割らない」：v(G1(t))>0 または v(G3(t))>0 なら t²≡−p² (mod ℓ) で G2(t), G4(t) は単数（≡u0）。
同様に v(G2(t))>0 または v(G4(t))>0 なら G1(t), G3(t) は単数（≡−u0）。
ℓ | P+Q は p+1/c=(p²+2p−1)/(p+1) を使って (1,4),(2,3) で同じ。

**ℓ | H（v(p²+1)=n>0）.** p_j²+1 の付値は全て ≥n、p_j²−p_k² の付値は全てちょうど n（下の表）。
v(t²−1)<n なら G_j/(t²−1)=1+(p_j²+1)/(t²−1)∈1+ℓZ_ℓ で、4つの類は全て [t²−1] に等しい。
v(t²−1)≥n なら全ての v(G_j)≥n。差の付値がちょうど n なので、v(G_j)>n となる j は高々1つ。
残り3つは付値ちょうど n、(ii) より残る1つの付値も n と同じ偶奇。∎

**差の表（sympy で確認、`scripts/36R-01_differences.py`）.**
```text
p²−p⁻² = P·H/(ab)²            c²−c⁻² = 4·Q·H/P²
p²−c²  = (P−Q)·H/(b·f)²        p²−c⁻² = (P+Q)·H/(b·e)²
p⁻²−c² = −(P+Q)·H/(a·f)²       p⁻²−c⁻² = −(P−Q)·H/(a·e)²
p²+1 = H/b²,  p⁻²+1 = H/a²,  c²+1 = 2H/f²,  c⁻²+1 = 2H/e²
```

系 1：表から、ℓ≡3 mod 4 と良い素数は δ を割らない。ℓ | a²−b² は δ3,δ4 を割らず δ1,δ2 を同じ偶奇で割る（α）。
ℓ | ab は同様に β。ℓ | P−Q は (δ1,δ3) か (δ2,δ4) の一方だけ（μ1, μ2）。ℓ | P+Q は ν1, ν2。ℓ | H は4つ全てか、どれも割らない（h）。
P±Q の奇素因数は (P+Q)²+(P−Q)²=2H² より ≡±1 (mod 8)、うち δ に現れるのは ≡1 (mod 8)。
系 2, 3 は系 1 の式から直接。系 3 の後半は G1G2=□ ⇔ δ1δ2=1。

## 4. 検証

- **形の定理の数値検査**（`scripts/36R-01_shape_check.py`、出力 `outputs/36R-01_shape_check_A30_L45.out`）：
  a<30 の全ての p と奇素数 ℓ≤45 について、局所像 Im_ℓ(p)={(γ1,…,γ4) : C3_p(Q_ℓ) の点} を
  証明つきの ℓ 進分割（円盤上で付値と単数剰余が一定であることをテイラー係数で判定）で **厳密に** 計算し、
  表の条件を全ての元で検査。3,497 件で違反 0。
- **1Q の主張の独立な再現**（`scripts/36R-01_local_image_exact.py`、出力 `outputs/36R-01_local_image_A90_L75.*`）：
  a<90、ℓ≡1 mod 4、ℓ≤75 の 7,193 件で、厳密な局所像が (ℓ, 型, n, 符号 d) の関数になっているかを検査。
  150 通りのキーで **衝突 0**。1Q の「型・ℓ・付値・符号1個で決まる」は、1Q とは別のアルゴリズムでも再現された。
- 1Q の像（根の近くを全類許す上からの近似）より、積条件 (ii) を課した厳密な像の方が小さく単純になる。
  例：ℓ | ab では厳密な像は {(1,1,κ,κ)} の部分集合で、1Q の表にある非対角の成分は積条件で消える。

## 5. 適用範囲と、言っていないこと

- 形の定理は **必要条件**（⊆）。T(type(p)) の元がすべて Selmer 集合に入るとは言っていない。
- ℓ=2 の条件は ε の偶奇の和だけ（8 通り）。2 進の精密な像は未計算。
- 単数部分の符号条件は系 4 の分だけ入れた。良い素数と ℓ | H での符号条件、および系 4 を超える細部は入れていない。厳密な像の明示式（1Q の表の厳密版）は未了。
  数値では (ℓ, 型, n, d) で決まることを確認済みで、証明は §3 と同じ円盤ごとの議論で書けるはずだが、まだ書いていない。
- 全 p の除外ではない。自明類と境界類は常に T に入り、実際に有理点（t=0,∞ と t=±1）を持つ。
- 仮説 H は使っていない。

## 付録 A：差の表の確認スクリプト（sympy）
```
# 36R-01: the table of differences p_j^2 - p_k^2 and p_j^2 + 1 used in the proof of the Shape Theorem
import sympy as sp
a, b = sp.symbols('a b')
p = a/b; c = (p+1)/(p-1); e = a+b; f = a-b
P = a**2-b**2; Q = 2*a*b; H = a**2+b**2
ok = True
def check(name, lhs, rhs):
    global ok
    z = sp.simplify(lhs - rhs) == 0; ok &= bool(z); print(('PASS ' if z else 'FAIL ') + name)
check('p^2 - p^-2 = P H/(ab)^2', p**2 - p**-2, P*H/(a*b)**2)
check('c^2 - c^-2 = 4 Q H/P^2', c**2 - c**-2, 4*Q*H/P**2)
check('p^2 - c^2 = (P-Q) H/(b f)^2', p**2 - c**2, (P-Q)*H/(b*f)**2)
check('p^2 - c^-2 = (P+Q) H/(b e)^2', p**2 - c**-2, (P+Q)*H/(b*e)**2)
check('p^-2 - c^2 = -(P+Q) H/(a f)^2', p**-2 - c**2, -(P+Q)*H/(a*f)**2)
check('p^-2 - c^-2 = -(P-Q) H/(a e)^2', p**-2 - c**-2, -(P-Q)*H/(a*e)**2)
check('p^2 + 1 = H/b^2', p**2 + 1, H/b**2)
check('p^-2 + 1 = H/a^2', p**-2 + 1, H/a**2)
check('c^2 + 1 = 2H/f^2', c**2 + 1, 2*H/f**2)
check('c^-2 + 1 = 2H/e^2', c**-2 + 1, 2*H/e**2)
check('p - c = (P-Q)/(b f)', p - c, (P-Q)/(b*f))
check('p + 1/c = (P+Q)/(b e)', p + 1/c, (P+Q)/(b*e))
check('(P+Q)^2 + (P-Q)^2 = 2 H^2', (P+Q)**2 + (P-Q)**2, 2*H**2)
print('ALL PASS' if ok else 'SOME FAIL')
```

出力：
```
PASS p^2 - p^-2 = P H/(ab)^2
PASS c^2 - c^-2 = 4 Q H/P^2
PASS p^2 - c^2 = (P-Q) H/(b f)^2
PASS p^2 - c^-2 = (P+Q) H/(b e)^2
PASS p^-2 - c^2 = -(P+Q) H/(a f)^2
PASS p^-2 - c^-2 = -(P-Q) H/(a e)^2
PASS p^2 + 1 = H/b^2
PASS p^-2 + 1 = H/a^2
PASS c^2 + 1 = 2H/f^2
PASS c^-2 + 1 = 2H/e^2
PASS p - c = (P-Q)/(b f)
PASS p + 1/c = (P+Q)/(b e)
PASS (P+Q)^2 + (P-Q)^2 = 2 H^2
ALL PASS
```

## 付録 B：厳密な局所像の計算（Python 標準ライブラリのみ）
```
# 36R-01: exact local images of the 2-cover descent map of C3_p at primes l = 1 mod 4, by certified l-adic subdivision,
# and test of the claim (LOG 1Q) that the image depends only on (l, type, n, sign d).
#   C3_p : y^2 = G1 G2 G3 G4,  G_j = t^2 + p_j^2,  (p_1..p_4) = (p, 1/p, c, 1/c),  c = (p+1)/(p-1),  p = a/b.
#   Im_l(p) = { ([G1(t)],..,[G4(t)]) in (Q_l^*/squares)^4 : (t,y) in C3_p(Q_l) }   (at a root of G_j the j-th class is
#   the product of the other three; t = oo gives (1,1,1,1)).
# Certification: G(t0 + l^k T) = c0 + c1 T + c2 T^2; if ord c0 < min(ord c1, ord c2) the class of G is constant on the disc.
# usage: python 36R-01_local_image_exact.py AMAX LMAX
import sys, math, json
from fractions import Fraction as Fr
from collections import defaultdict

def val(x, l):
    x = Fr(x)
    if x == 0: return None
    n, d, e = x.numerator, x.denominator, 0
    while n % l == 0: n //= l; e += 1
    while d % l == 0: d //= l; e -= 1
    return e
def cls(x, l):
    """class of x in Q_l^*/squares as (ord mod 2, legendre(unit))"""
    e = val(x, l); u = Fr(x) / Fr(l) ** e
    r = u.numerator * pow(u.denominator, -1, l) % l
    return (e % 2, 1 if pow(r, (l - 1) // 2, l) == 1 else -1)
def cmul(x, y): return ((x[0] + y[0]) % 2, x[1] * y[1])
def sqrt_m1(l, N=60):
    r = next(x for x in range(2, l) if (x * x + 1) % l == 0)
    M = l
    for _ in range(N):
        M *= l; r = (r - (r * r + 1) * pow(2 * r, -1, M)) % M
    return r, M

def image(a, b, l):
    p = Fr(a, b); c = (p + 1) / (p - 1)
    ps = [p, 1 / p, c, 1 / c]
    ir, M = sqrt_m1(l)
    def root_in_disc(j, chart, t0, k):
        # roots of G_j: t = +- i p_j ; in chart s = 1/t: s = +- i / p_j ... (-1/(i p) = i/p)
        w = ps[j] if chart == 't' else 1 / ps[j]
        if val(w, l) < 0: return False
        wv = w.numerator * pow(w.denominator, -1, M) % M
        for sg in (1, -1):
            rt = sg * ir * wv % M
            d = (rt - (t0.numerator * pow(t0.denominator, -1, M))) % M
            if d == 0 or val(d, l) >= k: return True
        return False
    out = set()
    def node(chart, t0, k, depth=0):
        assert depth < 50
        lk = Fr(l) ** k
        cl = []; inexact = []
        for j in range(4):
            q2 = ps[j] ** 2
            if chart == 't': c0, c1, c2 = t0 * t0 + q2, 2 * t0 * lk, lk * lk
            else:            c0, c1, c2 = 1 + q2 * t0 * t0, 2 * q2 * t0 * lk, q2 * lk * lk   # G/t^2 = 1 + p^2 s^2
            v0 = val(c0, l); v1 = val(c1, l); v2 = val(c2, l)
            if v0 is not None and (v1 is None or v0 < v1) and v0 < v2: cl.append(cls(c0, l))
            else: cl.append(None); inexact.append(j)
        if not inexact:
            prod = (0, 1)
            for x in cl: prod = cmul(prod, x)
            if prod == (0, 1): out.add(tuple(cl))
            return
        if len(inexact) == 1 and root_in_disc(inexact[0], chart, t0, k):
            j = inexact[0]; prod = (0, 1)
            for i, x in enumerate(cl):
                if i != j: prod = cmul(prod, x)
            cl[j] = prod; out.add(tuple(cl)); return
        for r in range(l): node(chart, t0 + r * lk, k + 1, depth + 1)
    node('t', Fr(0), 0); node('s', Fr(0), 1)
    return frozenset(out)

def type_datum(a, b, l):
    e, f = a + b, a - b; H = a * a + b * b; P = a * a - b * b; Q = 2 * a * b
    chi = lambda x: 1 if pow(x % l, (l - 1) // 2, l) == 1 else -1
    def prime_to(x):
        n = 0
        while x % l == 0: x //= l; n += 1
        return n, x
    for nm, x in (('a', a), ('b', b), ('a-b', f), ('a+b', e), ('P-Q', P - Q), ('P+Q', P + Q), ('H', H)):
        if x % l == 0:
            n, x1 = prime_to(x)
            if nm == 'a': d = chi(x1 * b)
            elif nm == 'b': d = chi(x1 * a)
            elif nm == 'a-b': d = chi(2 * b * x1)
            elif nm == 'a+b': d = chi(2 * b * x1)
            elif nm in ('P-Q', 'P+Q'): d = chi(H * x1)
            else:
                ir, M = sqrt_m1(l)
                pv = a * pow(b, -1, M) % M
                r = ir if (pv - ir) % l == 0 else (M - ir)
                w = ((pv - r) % M) // l ** n
                d = chi(2 * w)
            return (nm, n, d)
    return None

if __name__ == '__main__':
    AMAX, LMAX = int(sys.argv[1]), int(sys.argv[2])
    primes = [l for l in range(5, LMAX + 1) if l % 4 == 1 and all(l % q for q in range(2, int(l ** .5) + 1))]
    table = defaultdict(lambda: defaultdict(list)); cnt = 0
    for a in range(2, AMAX):
        for b in range(1, a):
            if math.gcd(a, b) != 1: continue
            for l in primes:
                td = type_datum(a, b, l)
                if td is None: continue
                im = image(a, b, l); cnt += 1
                table[(l,) + td][im].append((a, b))
    coll = 0; rows = []
    for key in sorted(table):
        ims = table[key]
        n = sum(len(v) for v in ims.values())
        if len(ims) > 1: coll += 1
        rows.append(dict(l=key[0], type=key[1], n=key[2], d=key[3], cases=n, distinct_images=len(ims),
                         image_sizes=sorted(len(i) for i in ims), examples=[v[0] for v in ims.values()][:4]))
    by_type = defaultdict(lambda: [0, 0, 0])
    for r in rows:
        t = by_type[r['type']]; t[0] += r['cases']; t[1] += 1; t[2] += r['distinct_images'] > 1
    print('cases', cnt, 'keys (l,type,n,d)', len(rows), 'keys with more than one image', coll)
    for t, (c, k, bad) in sorted(by_type.items()): print(f'  type {t:4s}: cases {c:6d}  keys {k:4d}  keys with collisions {bad}')
    for r in rows:
        if r['distinct_images'] > 1: print('COLLISION', r)
    json.dump(rows, open(f'../outputs/36R-01_local_image_A{AMAX}_L{LMAX}.json', 'w'))
```

## 付録 C：形の定理の数値検査
```
# 36R-01: numerical check of the Shape Theorem against exact local images (all odd primes l <= LMAX, a < AMAX).
# For every p = a/b and odd prime l the exact image Im_l(p) (certified subdivision) must satisfy:
#   l | ab        : [G1]=[G2]=1, [G3]=[G4]
#   l | a^2-b^2   : [G3]=[G4]=1, [G1]=[G2]
#   l | P-Q       : [G1]=[G3], [G2]=[G4]
#   l | P+Q       : [G1]=[G4], [G2]=[G3]
#   l | H         : all four valuations have the same parity
#   otherwise     : all valuations even
#   l = 3 mod 4   : all valuations even (Lemma A)
# usage: python 36R-01_shape_check.py AMAX LMAX
import sys, math, importlib.util
from fractions import Fraction as Fr
spec = importlib.util.spec_from_file_location('li', '36R-01_local_image_exact.py'); li = importlib.util.module_from_spec(spec); spec.loader.exec_module(li)

def image_any(a, b, l):
    if l % 4 == 1: return li.image(a, b, l)
    # l = 3 mod 4: G_j has no root in Q_l, plain subdivision terminates
    p = Fr(a, b); c = (p + 1) / (p - 1); ps = [p, 1 / p, c, 1 / c]; out = set()
    def node(chart, t0, k, depth=0):
        assert depth < 60
        lk = Fr(l) ** k; cl = []
        for j in range(4):
            q2 = ps[j] ** 2
            if chart == 't': c0, c1, c2 = t0 * t0 + q2, 2 * t0 * lk, lk * lk
            else:            c0, c1, c2 = 1 + q2 * t0 * t0, 2 * q2 * t0 * lk, q2 * lk * lk
            v0 = li.val(c0, l); v1 = li.val(c1, l); v2 = li.val(c2, l)
            if v0 is not None and (v1 is None or v0 < v1) and v0 < v2: cl.append(li.cls(c0, l))
            else:
                for r in range(l): node(chart, t0 + r * lk, k + 1, depth + 1)
                return
        prod = (0, 1)
        for x in cl: prod = li.cmul(prod, x)
        if prod == (0, 1): out.add(tuple(cl))
    node('t', Fr(0), 0); node('s', Fr(0), 1)
    return frozenset(out)

AMAX, LMAX = int(sys.argv[1]), int(sys.argv[2])
primes = [l for l in range(3, LMAX + 1) if all(l % q for q in range(2, int(l ** .5) + 1))]
one = (0, 1); stats = {}; bad = 0
for a in range(2, AMAX):
    for b in range(1, a):
        if math.gcd(a, b) != 1: continue
        H = a*a + b*b; P = a*a - b*b; Q = 2*a*b
        for l in primes:
            im = image_any(a, b, l)
            if (a*b) % l == 0: ty = 'ab'; ok = all(x[0] == one and x[1] == one and x[2] == x[3] for x in im)
            elif P % l == 0: ty = 'a2-b2'; ok = all(x[2] == one and x[3] == one and x[0] == x[1] for x in im)
            elif (P - Q) % l == 0: ty = 'P-Q'; ok = all(x[0] == x[2] and x[1] == x[3] for x in im)
            elif (P + Q) % l == 0: ty = 'P+Q'; ok = all(x[0] == x[3] and x[1] == x[2] for x in im)
            elif H % l == 0: ty = 'H'; ok = all(len({y[0] for y in x}) == 1 for x in im)
            else: ty = 'good'; ok = all(all(y[0] == 0 for y in x) for x in im)
            if l % 4 == 3: ok = ok and all(all(y[0] == 0 for y in x) for x in im); ty += ' (l=3 mod 4)'
            s = stats.setdefault(ty, [0, 0, 0]); s[0] += 1; s[1] += ok; s[2] = max(s[2], len(im))
            if not ok: bad += 1; print('VIOLATION', a, b, l, ty, sorted(im))
for ty, (n, ok, mx) in sorted(stats.items()): print(f'{ty:22s} cases {n:6d}  satisfy shape {ok:6d}  max |Im| {mx}')
print('violations', bad)
```

出力（a<30、ℓ≤45）：
```
H                      cases    205  satisfy shape    205  max |Im| 10
P+Q                    cases     43  satisfy shape     43  max |Im| 8
P+Q (l=3 mod 4)        cases    105  satisfy shape    105  max |Im| 4
P-Q                    cases     45  satisfy shape     45  max |Im| 8
P-Q (l=3 mod 4)        cases    110  satisfy shape    110  max |Im| 4
a2-b2                  cases    190  satisfy shape    190  max |Im| 4
a2-b2 (l=3 mod 4)      cases    314  satisfy shape    314  max |Im| 2
ab                     cases    185  satisfy shape    185  max |Im| 4
ab (l=3 mod 4)         cases    298  satisfy shape    298  max |Im| 2
good                   cases    946  satisfy shape    946  max |Im| 8
good (l=3 mod 4)       cases   1056  satisfy shape   1056  max |Im| 8
violations 0
```
