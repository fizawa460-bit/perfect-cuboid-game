# 36R-02 REVIEW BUNDLE — C3_p の自明類の還元：W_λ とその商 X_λ, Y_λ, E′_λ（外部査読用、自己完結）

作成 2026-10-14。状態：未査読の候補。AI による作成で、人手の確認はない。RESULTS には載せていない。

## 背景（この束だけで読めるように）
C3_p : y²=(t²+p²)(t²+p⁻²)(t²+c²)(t²+c⁻²)、c=(p+1)/(p−1)、p=a/b∈Q∖{0,±1}。
「retained 点」は t∉{0,±1,∞} の有理点。t=0,±1,∞ には常に有理点がある。
先行する記録（LOG 1L, 1R）は、点ごとに Q(i) の類 D(t) を定義し、D(t)=sqf(n0) の類（自明類）が
種数2曲線 X_λ に帰着することを述べている。この束は、それを証明つきで整理し、新しい商 Y_λ, E′_λ を加える。

## 査読者へのお願い
1. 補題 2 の H¹(Gal(K/Q), K*²)=0 の証明。
2. 定理 A の同値（D(t)=sqf(n0) ⇔ W_λ の有理点）。
3. 定理 B の3つの商の式（付録 A の sympy で確認済み）と、ヤコビ多様体の同種類の議論。
   特に「Y_λ の因子 y²=(x+4)(x²+8x−4λ²) が E_{n0} に Q 上同型」の計算。
4. 定理 C：商の有理点が W_λ の有理点に持ち上がる条件。系 (Y) の証明で、既知の 6 点の逆像が t=0,∞ だけであること。
5. 補題 4（t=±1 は自明類に入らない）。

## 1. 設定と自明類の定義

p=a/b、P=a²−b², Q=2ab, H=a²+b², n0=ab(a²−b²)、λ=(P²−Q²)/(PQ)、K=Q(i)。
l1=bt+ia, l2=at+ib, l3=ft+ie, l4=et+if（e=a+b, f=a−b）、N(l_j)=Q_j（1G の形式、v=1）。
F(t) := l1·l̄2·l̄3·l4。

**補題 1（恒等式）.** F(t) = n0·( q(t) + 2iλ·t(t²+1) )、q(t)=t⁴+6t²+1。
また N(F)=Q1Q2Q3Q4=(abef)²·f_p(t)。（sympy、`scripts/36R-02_verify_W.py`）

**補題 2（類 D(t)）.** (t,y)∈C3_p(Q) なら F(t)∈D·K*² となる正の平方因子なし整数 D=D(t) がただ1つある。
証明：F·F̄ は有理数の平方なので F̄≡F (mod K*²)、つまり F の類は Gal(K/Q) 不変。
完全列 1→K*²→K*→K*/K*²→1 から (K*/K*²)^G の Q* の像による余核は H¹(G,K*²) に入る。
1→μ2→K*→K*²→1 と Hilbert 90 より H¹(G,K*²)→H²(G,μ2)=Z/2→H²(G,K*)=Q*/N(K*) は完全で、
右の写像は −1 を −1 の類に送る。−1 は Q(i) からのノルムでないので単射、よって H¹(G,K*²)=0。
したがって F=d·β²（d∈Q*）。d は Q*∩K*²=±Q*² を法として決まるので、正の平方因子なし整数として一意。∎

t=0 で F=n0（補題 1）。**自明類** を D(t)=sqf(n0) となる点の集合と定義する（t=0,∞ はここに入る）。
t=±1 は自明類に入らない（下の補題 4）。

## 2. 定理（自明類の還元、全ての p）

曲線 W_λ を
```text
W_λ :  U² − V² = t⁴+6t²+1,   U·V = λ·t·(t²+1)
```
とおく（C3_p の不分岐2重被覆、種数5）。

**定理 A.** 写像 (t,U,V)↦t は
`W_λ(Q) ∖ {t=0,∞}` から「C3_p の自明類の retained 点の t 座標の集合」への全射で、各ファイバーは (U,V)↦(−U,−V) の2点。
特に：**自明類に retained 点がない ⇔ W_λ(Q) の点は t∈{0,∞} のみ**。

証明：D(t)=sqf(n0) ⇔ F/n0=q+2iλt(t²+1) が K の平方 (U+iV)² ⇔ U²−V²=q(t), UV=λt(t²+1)（補題 1）。
W_λ の点から y は n0²(q²+4λ²t²(t²+1)²)=Q1Q2Q3Q4 で定まる。∎

**定理 B（3つの商）.** W_λ の Q 上の対合と商は次のとおり（恒等式はすべて sympy で確認）。

| 対合 | 不変量 | 商 | ヤコビ多様体 |
|---|---|---|---|
| σ1:(t,U,V)→(−1/t, U/t², −V/t²) | S=t−1/t, B=V/t, y=S(B²−λ²) | X_λ : y²=−(B⁴+8B²−4λ²)(B²−λ²)（種数2） | E_ρ × E_{n0} に同種（1R） |
| σ3:(t,U,V)→(−t, U, −V) | m=V/t, y=(2U(λ²−m²)−λm(m²+4))/λ | **Y_λ : y²=(m²+4)(m⁴+8m²−4λ²)**（種数2） | E_σ × E_{n0} に同種 |
| σ2:(t,U,V)→(1/t, U/t², V/t²) | A=U/t, B=V/t, y=A(λ²−B²)/λ | **E′_λ : y²=(B²+4)(λ²−B²)**（種数1） | E_τ に同種 |

- Y_λ の因子：x=m² で y²=(x+4)(x²+8x−4λ²)。λ²+4=(H²/(PQ))² なので右辺の根は −4, −4±2H²/(PQ)。
  X=x+4 で y²=X³−δ²X、δ=2H²/(PQ)。sqf(δ)=sqf(2PQ)=sqf(n0) なので、これは合同数曲線 E_{n0} に Q 上同型（証明つき）。
  もう一方の因子は、Y_λ→C3_p/(t→−t)=E_σ が定数でない写像なので E_σ に同種（証明つき）。
- E′_λ：W_λ/σ2→C3_p/(t→1/t)=E_τ は種数1どうしの定数でない写像なので同種（証明つき）。
- 数値確認：無作為な 76 個の p で、素数 5〜400 のフロベニウスの跡が 3 組とも一致（`outputs/36R-02_isogeny_check.out`）。

**定理 C（有理点の対応。1R の「⇔」の正確な形）.**
1. `W_λ(Q)∖{t=0,∞}` → X_λ(Q) の像は「y≠0 かつ (y/(B²−λ²))²+4 が有理数の平方」である点の集合。
   t は t−1/t=S=y/(B²−λ²) から決まる。**X_λ(Q) に非自明な点があるだけでは、自明類の retained 点は出ない**（平方条件が要る）。
2. `W_λ(Q)∖{t=0,∞}` → Y_λ(Q) の像は「m≠±λ, ∞ で、U:=λ(y+m(m²+4))/(2(λ²−m²)) に対し U·m/λ−1 が 0 でない有理数の平方」である点の集合（t²=Um/λ−1）。
3. E′_λ(Q) については R=AB/λ=t+1/t で、R²−4 が平方であることが条件。

**系（十分条件）.** 次のどれか1つが成り立てば、C3_p の自明類に retained 点はない。
- (X) X_λ(Q)={(±λ,0)}。
- (Y) Y_λ(Q)={(±λ,±λ(λ²+4)), ∞±}（6点）。
- (E′) E′_λ(Q) の点で R²−4 が 0 でない平方になるものがない（例：rank E_τ=0 で捩れ点を調べる）。

証明（Y の場合。X は 1R と同じ）：(m,y)∈Y_λ(Q) が W_λ(Q) の点から来るとする。∞± は t=0, U=0, V²=−1 の点の像で、
W_λ(Q) の像ではない。m=±λ のとき U の2次方程式 U²(λ²−m²)−λm(m²+4)U+λ²(m²+4)=0 は1次に退化し U=λ/m=±1、
t²=Um/λ−1=0。よって t=0（もう一方の根 U=∞ は t=∞）。∎

**補題 4.** t=±1 は W_λ(Q) の点を与えない。証明：t=1 で U²=4±2H²/(PQ)、つまり U²=2(P+Q)²/(PQ) か −2(P−Q)²/(PQ)。
前者が平方 ⇔ 2PQ=4n0 が平方 ⇔ n0 が平方。n0=ab(a−b)(a+b) は平方でない（Fermat）。後者は負。∎

## 3. Y_λ が新しく与えるもの

- X_λ は rank(E_ρ)=rank(E_{n0})=1 のとき2次 Chabauty が使える（1S, 1T）。Y_λ は **rank(E_σ)=rank(E_{n0})=1** のとき使える。
  E_σ は全 p で rank≥1（R-21）なので、Y_λ では rank 0 による近道はない。
- a≤40 の 331 類の調査（`outputs/xqc/survey.jsonl`、ellrank の上下界が一致したもの）：
  X_λ が (1,1) の類 50、Y_λ が (1,1) の類 56、両方 24。**X が (1,1) でも E_ρ rank 0 でもなく、Y が (1,1) の類が 10**
  （17/6, 25/24, 27/2, 29/22, 31/26, 35/8, 36/25, 38/23, 38/27, 40/33）。この 10 類は 36R-03 で扱う。
- rank E_{n0}≥2 の類（a≤40 の 331 類中 201 類）には X_λ も Y_λ も使えない。rank E_{n0}=1 の 130 類の内訳：
  E_ρ rank 0 が 51、X が (1,1) が 50、Y だけが (1,1) が 10、どれでもないものが 19。W_λ のヤコビ多様体は
  E_σ×E_τ×E_ρ×E_{n0}² に同種で、rank E_{n0}≥2 だと rank≥4+… となり種数5に対して Chabauty の余地がない。
  これが自明類の壁の残り。

## 4. 適用範囲と、言っていないこと

- 定理 A〜C は全ての p で成り立つ恒等式と写像の主張。有理点の決定は含まない。
- 「自明類」は K の類 D(t)=sqf(n0) で定義している。δ=(1,1,1,1)（Q 上の降下の類）とは定義が違う。
  t=0,∞ はどちらにも入るが、2つの集合の包含関係はここでは主張しない。
- 一般の D の類については、1R の注（z=B²/c、c=n0/D）と同じ構成が使えるはずだが、ここでは検証していない。

## 付録 A：恒等式の確認スクリプト（sympy）
```
# 36R-01: symbolic verification of the trivial-class reduction  C3_p -> W -> {X_lam, Y_lam, E'_lam}
import sympy as sp
a, b, t, U, V, lam = sp.symbols('a b t U V lambda')
I = sp.I
e = a + b; f = a - b
P = a**2 - b**2; Q = 2*a*b; H = a**2 + b**2; n0 = a*b*(a**2 - b**2)
ok = True
def check(name, expr):
    global ok
    z = sp.expand(sp.together(expr)) == 0 or sp.simplify(expr) == 0
    ok &= bool(z); print(('PASS ' if z else 'FAIL ') + name)
l1 = b*t + I*a; l2 = a*t + I*b; l3 = f*t + I*e; l4 = e*t + I*f
cj = lambda z: z.subs(I, -I)
Q1 = b**2*t**2 + a**2; Q2 = a**2*t**2 + b**2; Q3 = f**2*t**2 + e**2; Q4 = e**2*t**2 + f**2
for nm, l, Qj in (('1', l1, Q1), ('2', l2, Q2), ('3', l3, Q3), ('4', l4, Q4)):
    check('N(l%s) = Q%s' % (nm, nm), sp.expand(l*cj(l)) - Qj)
F = sp.expand(l1*cj(l2)*cj(l3)*l4)
lamv = (P**2 - Q**2)/(P*Q)
qt = t**4 + 6*t**2 + 1
check('F = n0*(q(t) + 2 i lam t (t^2+1))', F - n0*(qt + 2*I*lamv*t*(t**2 + 1)))
check('F(0) = n0', F.subs(t, 0) - n0)
# C3_p model: Q1 Q2 Q3 Q4 = (ab ef)^2 * f_p(t)-normalisation
p = a/b; c = (p + 1)/(p - 1)
fp = (t**2 + p**2)*(t**2 + p**-2)*(t**2 + c**2)*(t**2 + c**-2)
check('Q1Q2Q3Q4 = (a b e f)^2 f_p(t)', Q1*Q2*Q3*Q4 - (a*b*e*f)**2*fp)
check('n0^2 (q^2 + 4 lam^2 t^2 (t^2+1)^2) = Q1Q2Q3Q4', n0**2*(qt**2 + 4*lamv**2*t**2*(t**2+1)**2) - Q1*Q2*Q3*Q4)
# W : U^2 - V^2 = q(t), U V = lam t (t^2+1)
def onW(expr):  # reduce modulo the two equations using V = lam t (t^2+1)/U and U^4 - q U^2 - lam^2 t^2 (t^2+1)^2 = 0
    ex = sp.together(expr.subs(V, lam*t*(t**2 + 1)/U))
    num = sp.numer(ex)
    rel = U**4 - qt*U**2 - lam**2*t**2*(t**2 + 1)**2
    return sp.rem(sp.expand(num), rel, U)
# sigma1 quotient X_lam
S = t - 1/t; B = V/t; y = S*(B**2 - lam**2)
check('X_lam : y^2 = -(B^4+8B^2-4lam^2)(B^2-lam^2)', onW(y**2 + (B**4 + 8*B**2 - 4*lam**2)*(B**2 - lam**2)))
# sigma3 quotient Y_lam (new)
m = V/t; yY = (2*U*(lam**2 - m**2) - lam*m*(m**2 + 4))/lam
check('Y_lam : y^2 = (m^2+4)(m^4+8m^2-4lam^2)', onW(yY**2 - (m**2 + 4)*(m**4 + 8*m**2 - 4*lam**2)))
# sigma2 quotient E'_lam
A_ = U/t; B_ = V/t; R = t + 1/t; yE = A_*(lam**2 - B_**2)/lam
check("E'_lam : A^2 - B^2 = R^2 + 4", onW(A_**2 - B_**2 - R**2 - 4))
check("E'_lam : A B = lam R", onW(A_*B_ - lam*R))
check("E'_lam : y^2 = (B^2+4)(lam^2-B^2)", onW(yE**2 - (B_**2 + 4)*(lam**2 - B_**2)))
# inverse on Y_lam: U, t^2 from (m, y)
ms, ys = sp.symbols('m y')
Uy = lam*(ys + ms*(ms**2 + 4))/(2*(lam**2 - ms**2)); z = Uy*ms/lam - 1
expr = sp.together(Uy**2 - ms**2*z - (z**2 + 6*z + 1))
num = sp.rem(sp.expand(sp.numer(expr)), ys**2 - (ms**2 + 4)*(ms**4 + 8*ms**2 - 4*lam**2), ys)
check('Y_lam inverse: U=lam(y+m(m^2+4))/(2(lam^2-m^2)), t^2 = U m/lam - 1 satisfy U^2 - m^2 t^2 = q(t)', num)
check('lam^2 + 4 = (H^2/(P Q))^2', lamv**2 + 4 - (H**2/(P*Q))**2)
print('ALL PASS' if ok else 'SOME FAIL')
```

出力：
```
PASS N(l1) = Q1
PASS N(l2) = Q2
PASS N(l3) = Q3
PASS N(l4) = Q4
PASS F = n0*(q(t) + 2 i lam t (t^2+1))
PASS F(0) = n0
PASS Q1Q2Q3Q4 = (a b e f)^2 f_p(t)
PASS n0^2 (q^2 + 4 lam^2 t^2 (t^2+1)^2) = Q1Q2Q3Q4
PASS X_lam : y^2 = -(B^4+8B^2-4lam^2)(B^2-lam^2)
PASS Y_lam : y^2 = (m^2+4)(m^4+8m^2-4lam^2)
PASS E'_lam : A^2 - B^2 = R^2 + 4
PASS E'_lam : A B = lam R
PASS E'_lam : y^2 = (B^2+4)(lam^2-B^2)
PASS Y_lam inverse: U=lam(y+m(m^2+4))/(2(lam^2-m^2)), t^2 = U m/lam - 1 satisfy U^2 - m^2 t^2 = q(t)
PASS lam^2 + 4 = (H^2/(P Q))^2
ALL PASS
```

## 付録 B：同種類の数値確認（PARI/GP）
```
/* 36R-01: numerical identification (traces of Frobenius) of the elliptic factors of Y_lam and E'_lam.
   Y_lam: y^2=(m^2+4)(m^4+8m^2-4lam^2):  Ya: y^2=(x+4)(x^2+8x-4lam^2) [x=m^2],  Yb: Y^2 = X^3+c1 X^2+c0 c2 X+c0^2 [X=c0/m^2]
   E'_lam: y^2=(B^2+4)(lam^2-B^2).   Compare with E_n0: y^2=x^3-n0^2 x, E_sigma: w^2=(x+p^2)(x+p^-2)(x+c^2)(x+c^-2), E_tau: v^2=(R^2+h^2)(R^2+16/h^2) */
same(E1, E2, bad) = { my(ok = 1); forprime(l = 5, 400, if (bad % l == 0, next); if (ellap(E1, l) != ellap(E2, l), ok = 0)); ok };
{
forstep (a = 2, 40, 1, for (b = 1, a-1, if (gcd(a,b) != 1 || random(6) != 0, next);
  p = a/b; c = (p+1)/(p-1); h = p - 1/p; P = a^2-b^2; Q = 2*a*b; lam = (P^2-Q^2)/(P*Q); if (lam == 0, next); n0 = a*b*(a^2-b^2);
  g = ('z+4)*('z^2+8*'z-4*lam^2); c0 = polcoef(g,0); c1 = polcoef(g,1); c2 = polcoef(g,2);
  Ya = ellinit([0, c2, 0, c1, c0]); Yb = ellinit([0, c1, 0, c0*c2, c0^2]);
  En0 = ellinit([0,0,0,-n0^2,0]);
  Es = ellinit(ellfromeqn('y^2 - ('x+p^2)*('x+p^-2)*('x+c^2)*('x+c^-2)));
  Et = ellinit(ellfromeqn('y^2 - ('x^2+h^2)*('x^2+16/h^2)));
  Ep = ellinit(ellfromeqn('y^2 - ('x^2+4)*(lam^2-'x^2)));
  bad = 2*3*a*b*(a^2-b^2)*(a^2+b^2)*(P^2-Q^2)*numerator(lam)*denominator(lam);
  print(a, "/", b, "  Ya~E_n0:", same(Ya, En0, bad), "  Yb~E_sigma:", same(Yb, Es, bad), "  E'~E_tau:", same(Ep, Et, bad));
));
}
quit
```

出力の要約：無作為な 76 個の p すべてで `Ya~E_n0:1 Yb~E_sigma:1 E'~E_tau:1`。
