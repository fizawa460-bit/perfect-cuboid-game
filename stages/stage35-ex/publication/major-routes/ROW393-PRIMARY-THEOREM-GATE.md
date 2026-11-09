# row393｜de la Mazaの一次文献適用と先行の独立数値照合

**2026-11-09 JST｜D-1 PASS（原命題・適用条件）。** [row393 §2](../../materials/classgroup-and-different/proofs/row393.md)に対し、de la Maza, *Bounds for the smallest norm in an ideal class*, Math. Comp. 71(240) (2002), 1745–1758 の掲載版を読んだ。pp. 1746–1747のTheorem 1・Corollaryと式 (4)–(7)、pp. 1748–1749の証明・式 (11)、pp. 1750–1751のLemma 2・Proposition 2を照合した。[原論文の掲載版PDF](https://citeseerx.ist.psu.edu/document?doi=1b6ff134947b9273c37cb81b7a73217d3d9562f7&repid=rep1&type=pdf) · [D-1照合の詳細](PR1860-GATE-D-TWO-EXTERNAL-PRIMARY-AUDIT.md)

[著者時点の独立監査記録](../../materials/classgroup-and-different/audits/row393.txt)と以下の数値スポットチェックは先行記録。数体・署名・判別式はrow393の固定親入力を使う。

## 実際に独立確認した数学的な部分

row393のパラメータ`gamma=107/500`,`alpha=13/1000`,`beta=77/1000`,`lambda=83/250`は`0<alpha<beta<gamma<lambda`を満たす。記載された有理関数R(s)の(1+constant/s)による展開は因数の整理により恒等的に成り、係数が非負となることを初等代数で確認できる。この展開は原典 (4) の因子数・符号条件を満たし、Proposition 2 の α₁=α₂=λ に一致する。

署名(r1,r2)=(7,49)、n=105で
```text
Gamma_K(s) = Gamma(s/2)^56 Gamma((s+1)/2)^49,
T(s)=Gamma_K(1−s)/Gamma_K(s+2 gamma+1),
P(s)=Gamma_K(s)/Gamma_K(s+2 gamma+1).
```
s=−gamma+itならTの分子と分母は複素共役で絶対値1。極s=−betaの留数が負、積分線のR寄与の上界`M=(gamma-alpha)/(2(gamma-beta)(lambda-gamma))`は初等的に導出できる。横方向の積分の消滅は移動帯でのGamma比の一様Stirling評価とR(s)の二次減衰で確認した。

mpmath高精度**独立再計算**（数値スポットチェックであり、今回新たに厳密区間証明を実装したとは言わない）：
```text
y0 = 92.17927173951989346507732452779997162419284883944…
t0 = 2392987572649699066.29245936001987010127929309097…
```
`t0=pi^(105/2)*R(0)*T(0)/(R(1)*P(1))`と、Gamma漸化式後の`[Gamma(1+gamma)/Gamma(1/2+gamma)]^7*(1/2+gamma)^49`を使う表式の数値は一致した。親row388のMinkowski値`305922182163644868409789020105260848381707484595.80948...`から同じ固定判別式を代数的に逆算して得るBのチェックは
```text
B = 13305064640793337858066482154.806669566197438920115256...
2^94 = 19807040628566084398385987584,
B/2^94 ≈ 0.67173410153985976.
```
で一致した。これは親判別式の独立再計算ではない。過去のArb/mpmath.ivによる区間算術の記録はそのまま別証拠として保持する。

## 適用判定

- 原典の通常イデアル類とrow393の類群が一致。GRH、零点不在、不同の主性の仮定を課さない。
- Mellin積分の符号・線方向・ガンマ規格化が一致。原典 (17) の下界に δ₂=γ、α₁=α₂=λ を入れるとrow393の $y_0$ になる。
- Corollary (7) と (11) を併用すると $B=\sqrt{|\Delta_K|}/(t_0e^{y_0})$。既存の区間計算と合わせ、固定数体の各通常イデアル類にノルムが $B$ 以下の整イデアル代表が存在し、$B<2^{94}$ となる。

6768の878基底によるCl/2全尽生成、形式181とc_Clの関係、−30無条件排除は未解決。全算術証書の独立再演は別の監査範囲。

[主要移植チェックリスト](MIGRATION-COMPLETION-CHECKLIST.md) · [既存類群研究](04-minus30.md)
