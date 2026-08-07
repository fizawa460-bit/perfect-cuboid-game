# Stage12-N1-3h：zero-base provenance と未展開解析細部の閉鎖

> **STATUS:** `R06_EXTERNAL_REVIEW_SELF_CONTAINMENT_CLOSED_IN_TEXT`
>
> **SCOPE:** Stage12-N1-2 primitive oriented count の自己完結性
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_R07_FULL_REAUDIT`

## 0. 修正対象

R06 bundle の数学的中心計算について、新しい反例や central gap は報告されなかった。一方、完全な zero-base review を名乗るには、次が同一 physical bundle 内で読める必要があるとの指摘を受けた。

1. rectangle error
   \[
   R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
   \]
   の導出本文;
2. `G`, `beta`, `eta`, `kappa` の由来となる旧2b・2e・2f・2j・2k本文;
3. Selberg--Delange input に必要な `L(s,chi_4)` の vertical polynomial growth;
4. radial integral で `x,y>=1` が角度端を切り取る効果の明示評価。

本稿は3と4を本文として補い、R07 builder が1と2を物理的に埋め込むための active / provenance 規則を固定する。

---

## 1. active proof と provenance source の区別

R07では次を一つのbundleへ収録する。

### Active current proof

- `docs/stage12-n1-2-final-r05.md`
- `docs/stage12-n1-3a-rectangular-error-repair.md`
- 本稿 `docs/stage12-n1-3h-zero-base-provenance-closure.md`

### Historical derivation provenance

commit `8d6910e8e68145e474f92716460a1cc6f384ecf1` から次を全文収録する。

- `docs/stage12-n1-2b-average.md`
- `docs/stage12-n1-2e-divisor-dyadic.md`
- `docs/stage12-n1-2f-main-term.md`
- `docs/stage12-n1-2j-boundary-layers.md`
- `docs/stage12-n1-2k-final-remainder.md`

これらを収録する目的は、parameterization、multiplicity `G`, divisor expansion, `kappa`, primitive-first `A_{r,s}`, `beta`, `gamma`, `eta` の導出をbundle外参照にしないことである。

ただし、historical source に含まれる後に修復された主張は active proof ではない。

```text
2f の formal raw asymptotic = provenance only
2k の旧 fixed-circle remainder = superseded by 3b / 3e
2k の旧 shallow declaration = superseded by 3g
3a §4 の retained => min(R,S)>=S0 application = superseded by 3f
```

3aでactiveなのは、特に補題3a.1のrectangle error導出である。radial coreへの適用はFinal R05内の3f規則、すなわちcoreを定義によって `R,S>=U` とする経路だけを使用する。

---

## 2. `L(s,chi_4)` の vertical growth

`chi_4` をmodulo 4のprimitive odd characterとする。completed functionを

\[
\Lambda(s,\chi_4)
:=
\left(\frac4\pi\right)^{(s+1)/2}
\Gamma\!\left(\frac{s+1}{2}\right)
L(s,\chi_4)
\]

と置く。primitive Dirichlet `L`-functionのfunctional equationにより

\[
\Lambda(s,\chi_4)=\Lambda(1-s,\chi_4)
\]

である。

任意の固定 `delta>0` に対し、`Re s>=1+delta` ではDirichlet級数が絶対収束するので

\[
L(\sigma+it,\chi_4)\ll_\delta1.
\]

左側境界 `sigma=-delta` ではfunctional equationとStirling formulaを用いる。固定幅のvertical stripでgamma比は `1+|t|` の固定冪であり、右側へ移された `L(1+delta-it,chi_4)` は有界だから、ある固定 `M_delta>0` が存在して

\[
L(-\delta+it,\chi_4)
\ll_\delta(1+|t|)^{M_\delta}.
\]

Phragmen--Lindelofをstrip `-delta<=sigma<=1+delta` に適用すると、strip全体で

\[
\boxed{
L(\sigma+it,\chi_4)
\ll_\delta(1+|t|)^{M_\delta}
}
\]

を得る。ここで指数の最適値は不要であり、固定多項式growthだけを使用する。

reference lockのanalytic factorは

\[
H_\beta(s)=L(s,\chi_4)J_\beta(s).
\]

`J_beta` は各閉部分半平面 `Re s>=1/2+epsilon` で局所一様絶対収束し、有界である。従って同じ領域で

\[
H_\beta(\sigma+it)
\ll_\epsilon(1+|t|)^{M_\epsilon}.
\]

よって、Final R05で採用したfinite-order Selberg--Delange inputのvertical polynomial-growth条件は、単なる「標準的growthへ還元」という宣言ではなく、functional equation、Stirling、Phragmen--Lindelofの三段階で確認できる。

```text
VERTICAL_GROWTH_L_CHI4=CLOSED_BY_STAGE12_N1_3H_SECTION_2
VERTICAL_GROWTH_H_BETA=CLOSED_BY_STAGE12_N1_3H_SECTION_2
```

---

## 3. radial integral の lower-limit boundary

\[
I(B)
:=
\iint_{\substack{x,y\ge1\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}\,dx\,dy,
\qquad L:=\log B.
\]

polar coordinates

\[
x=t\cos\theta,\qquad y=t\sin\theta
\]

では

\[
\frac{dx\,dy}{x^2+y^2}=\frac{dt}{t}\,d\theta.
\]

`t>=sqrt(2)` に対し

\[
\theta_0(t):=\arcsin(1/t).
\]

条件 `x,y>=1` は正確に

\[
\theta_0(t)
\le\theta\le
\frac\pi2-\theta_0(t)
\]

となる。従って

\[
I(B)=
\int_{\sqrt2}^{\sqrt B}
\int_{\theta_0(t)}^{\pi/2-\theta_0(t)}
\frac{(\log t+\log\cos\theta)(\log t+\log\sin\theta)}{t}
\,d\theta\,dt.
\]

full angle `0<=theta<=pi/2` で積分すると、

\[
\int_0^{\pi/2}
(\log t+\log\cos\theta)(\log t+\log\sin\theta)
\,d\theta
=
\frac\pi2(\log t)^2+O(\log t)+O(1),
\]

である。これは `log sin theta`, `log cos theta`, およびその積が端点で可積分であることから従う。

次に角度端の切取り誤差を評価する。`theta_0(t)\asymp1/t` であり、`0<theta<theta_0(t)` では

\[
|\log\sin\theta|\ll |\log\theta|,
\qquad
|\log\cos\theta|\ll1.
\]

従って両端を合わせた差は

\[
\ll
\frac{(\log t)^2}{t}
+
\int_0^{O(1/t)}|\log\theta|^2\,d\theta
\ll
\frac{(\log t)^2}{t}.
\]

radial measure `dt/t` を掛けると

\[
\int_{\sqrt2}^{\sqrt B}
\frac{(\log t)^2}{t^2}\,dt
=O(1).
\]

したがってlower-limitによるangular cutoffはcubic coefficientを変えない。full angleのleading termから

\[
\frac\pi2
\int_{\sqrt2}^{\sqrt B}
\frac{(\log t)^2}{t}\,dt
=
\frac\pi2\cdot\frac13\left(\frac L2\right)^3+O(1)
=
\frac\pi{48}L^3+O(1).
\]

cross termsは `O(L^2)`、constant angular termは `O(L)` なので、結局

\[
\boxed{
I(B)=\frac\pi{48}L^3+O(L^2).
}
\]

```text
RADIAL_LOWER_LIMIT_BOUNDARY=CLOSED_BY_STAGE12_N1_3H_SECTION_3
RADIAL_CUBIC_COEFFICIENT=PI_OVER_48_UNCHANGED
```

---

## 4. rectangle error のbundle内位置づけ

R07は3a全文を物理的に収録する。補題3a.1では、cross coefficients `c(a,b)` のweighted absolute normと

\[
B_\beta(X)\ll X
\]

を用い、係数領域を4分割して

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

を導出している。従ってこの指数はR07内でブラックボックスではない。

ただし3a §4に残る旧retained applicationは歴史的記述であり、active applicationは3fのcore/wing分割で置換する。

```text
RECTANGLE_EXPONENT_DERIVATION=EMBEDDED_STAGE12_N1_3A_LEMMA_3A_1
RECTANGLE_CORE_APPLICATION=STAGE12_N1_3F_ONLY
OLD_RETAINED_MIN_RS_APPLICATION=INACTIVE
```

---

## 5. 閉鎖判定

本稿とR07のsource inclusionにより、外部監査で指摘された自己完結性の不足に次のように対応する。

```text
STAGE12_N1_3A_BODY=EMBEDDED
G_ORIGIN_2B_2E=EMBEDDED_AS_PROVENANCE
KAPPA_ORIGIN_2F=EMBEDDED_AS_PROVENANCE
A_RS_BETA_ETA_ORIGIN_2J_2K=EMBEDDED_AS_PROVENANCE
VERTICAL_GROWTH=EXPLICITLY_DERIVED
RADIAL_LOWER_LIMIT=EXPLICITLY_DERIVED
NEW_CENTRAL_MATHEMATICAL_GAP=NONE_IDENTIFIED
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_R07_FULL_REAUDIT
```

これはR07監査前に定理を無条件で`CLOSED`と宣言するものではない。R07では、historical provenanceのどの箇所がactiveか、どの箇所が後続修復でsupersededかを含め、再び全鎖をゼロベースで確認する。
