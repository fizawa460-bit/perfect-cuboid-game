# PR #1860｜Gate D 外部一次文献２件の照合

**2026-11-09 JST｜R3-07／R2-01｜D-1 PASS・D-2 PASS。原典照合の残数は０件。** [第２周の終了判定表](PR1860-SECOND-PASS-EXIT-CHECKLIST.md)と[機械可読監査記録](PR1860-GATE-D-TWO-EXTERNAL-PRIMARY-AUDIT.json)を参照。

## D-1｜de la Maza と row393 §2

### 読んだ一次本文

Ana-Cecilia de la Maza, *Bounds for the smallest norm in an ideal class*, *Mathematics of Computation* 71(240) (2002), 1745–1758。AMSの直接PDF URLは取得時に403を返したため、誌名・著者・巻号・通し頁・論文番号が一致するCiteSeerX所収の掲載版本文を読んだ。pp. 1746–1747 の式 (1)–(7) と Theorem 1／Corollary、pp. 1748–1749 の証明と式 (11)、pp. 1750–1751 の Lemma 2／Proposition 2 を照合した。[掲載版PDF](https://citeseerx.ist.psu.edu/document?doi=1b6ff134947b9273c37cb81b7a73217d3d9562f7&repid=rep1&type=pdf) · [DOI](https://doi.org/10.1090/S0025-5718-01-01373-4)

### Theorem 1 と Corollary の命題

紙面の数式を以下の記号で記録する。$C$ を数体 $K$ のイデアル類、$\mathfrak a_C$ を $C$ 内の最小ノルムの整イデアル、$A_C=N(\mathfrak a_C)$ とする。$a_m$ は $C$ に属するノルム $m$ の整イデアルの個数。$n=r_1+2r_2=[K:\mathbb Q]$ とする。Theorem 1 は式 (4)–(5) の重みについて、任意の実数 $y$ で次を与える。

$$
B_{\mathrm{thm}}\sum_{m\ge A_C} a_m F_\gamma\!\left(y-\log(m/A_C)\right)
\ \ge\ t_0 e^y-\frac{\sqrt{|d_K|}}{A_C},
\qquad
B_{\mathrm{thm}}=\frac{\pi^{n/2}}{\kappa R_\gamma(1)P(1) A_C}>0.
$$

ここで $\kappa=2^{r_1+r_2}\pi^{r_2}R_K/(w_K\sqrt{|d_K|})$ であり、$R_K$ はレギュレーター、$w_K$ は $K$ 内の1の冪根の個数。式 (11) の正定数は

$$
t_0=\pi^{n/2}\frac{R_\gamma(0)T(0)}{R_\gamma(1)P(1)}
=\pi^{n/2}\frac{R_\gamma(0)}{R_\gamma(1)}
 \left(\frac{\Gamma(1+\gamma)}{\Gamma(\tfrac12+\gamma)}\right)^{r_1}
 \left(\tfrac12+\gamma\right)^{r_2}.
$$

Corollary（p. 1747, (7)）は、ある $y_1\in\mathbb R$ に対して **全ての $y\le y_1$** で $F_\gamma(y)\le 0$ なら $N(\mathfrak a_C)\le\sqrt{|d_K|}/(t_0e^{y_1})$ とする。Theorem 1 に $y=y_1$ を代入すると $m\ge A_C$ より全ての重みの引数が $y_1$ 以下になり、左辺が非正になる。row393 の $B$ はこの系の上界を表す。

### row393 の仮定と原文の対応

| 原典の条件・規約 | row393 §2での照合 |
|---|---|
| pp. 1746, 1748–1749。式 (6) の $\zeta_C$ は通常イデアル類 $C$ に属する全整イデアルを数える。定理の証明で $C'=[\mathfrak d_K]C^{-1}$ を使う | row393 の対象は $\mathrm{Cl}(K)$。全正元での同値という条件は課されない。異なる類 $C'$ も許されるので不同の主性は仮定に入らない |
| p. 1746, (1)–(3)。$\Gamma_{r_1,r_2}(s)=\Gamma(s/2)^{r_1+r_2}\Gamma((s+1)/2)^{r_2}$、$P(s)=\Gamma_{r_1,r_2}(s)/\Gamma_{r_1,r_2}(s+2\gamma+1)$、$T(s)=\Gamma_{r_1,r_2}(1-s)/\Gamma_{r_1,r_2}(s+2\gamma+1)$ | $(r_1,r_2,n)=(7,49,105)$ によりガンマ因子の指数は $(56,49)$。三式とも一致 |
| p. 1746, (4)。$c_0=1+2\gamma$ とし、$R_\gamma(s)(1+c_0/s)^{r_1+r_2}(1+c_0/(s+1))^{r_2}$ が $\sum_{i=0}^{\ell}e_i\prod_{j=0}^{n_i}(s+a_{ij})^{-1}$、$\ell\ge 0,\ e_i,a_{ij}\ge 0,\ n_i>0$ と書ける | row393 の展開では係数とシフトが非負で、共通の $(s+\lambda)^{-2}$ が各項にあるので各積の因子数は２以上。さらに p. 1751 の Proposition 2 の $(\alpha_1,\alpha_2)=(\lambda,\lambda)$ そのもの。原文は $0\le\alpha<\beta<\gamma<\alpha_1\le\alpha_2$ を許す |
| p. 1746, (5)。$\operatorname{Re}s=-\delta_1$ を下から上へ積分し、係数は $1/(2\pi i)$、核は $e^{(1-s)y}T(s)R_\gamma(s)$。$-\delta_1\le\operatorname{Re}s\le0$ に $R_\gamma$ の極がない | row393 の $\varepsilon$ が $\delta_1$ に当たる。$0<\varepsilon<\beta$ と取れ、極 $-\beta,-\lambda$ はその閉帯の左。積分の向き・符号・正規化は一致 |
| pp. 1750–1751, Lemma 2／Proposition 2 (16)–(17)。負の留数を使い、符号を保証する $y_0$ の下界を与える | $\delta_2=\gamma$ では横切る極は $-\beta$ だけで、留数は $-L$。$T(-\gamma+it)$ の分子・分母は共役なので絶対値１。(17) の二つの対数の引数は、row393 の $L=(\beta-\alpha)T(-\beta)/(\lambda-\beta)^2$ と $M=(\gamma-\alpha)/(2(\gamma-\beta)(\lambda-\gamma))$ に一致。よって $y_1=(\log L-\log M)/(\gamma-\beta)$ まで $F_\gamma(y)\le 0$ |
| pp. 1747, 1749, (7), (11)。$t_0e^{y_1}$ はノルム上界の分母 | $\pi^{105/2}$ は $t_0$ の分子。ガンマ漸化式で指数 $7,49$ の row393 の表示を得る。符号のある判別式には系の $\sqrt{\lvert d_K\rvert}$ を用いる |

積分線移動の帯 $-\gamma\le \sigma=\operatorname{Re}s\le-\varepsilon$ では $T$ に極がなく、Stirling 評価で $|T(\sigma+it)|=O(|t|^{-105(\sigma+\gamma)})$ が一様に成り立つ。$R(s)=O(|s|^{-2})$ により両縦線で絶対収束し、水平辺の寄与は消える。Theorem 1 の証明は部分ゼータの関数等式、凸性評価、留数と Lemma 1 の非負性を使う。数体次数の制限、GRH、零点不在の仮定は課されていない。

**D-1 PASS**。既存の区間計算が使った $B=\sqrt{|\Delta_K|}/(t_0 e^{y_0})<2^{94}$ への定理適用が一致する。固定数体・署名・判別式は row393 の親入力に依存する。[row393 §2](../../materials/classgroup-and-different/proofs/row393.md) · [先行の数値照合](ROW393-PRIMARY-THEOREM-GATE.md)

## D-2｜Mordell と Branch B §15.4

### 読んだ一次本文と命題

L. J. Mordell, *Diophantine Equations*, Academic Press, 1969, Chapter 4 “Quartic Equations with only Trivial Solutions”, p. 19 の $k=1$, Eq. (7′) と p. 20 に続く降下証明を、同版のページ別複製で確認した。前段の一般式 (7) は $x^4+kx^2y^2+y^4=z^2$。$k=1$ の原文が扱う命題は次の通り。

$$
x^4+x^2 y^2+y^4=z^2,\qquad x,y,z\in\mathbb Z,\quad \gcd(x,y)=1.
$$

解は $x^2=1,\ y=0$ または $x=0,\ y^2=1$ に限られ、どちらも $z^2=1$。本文の非負化は平方による対称性、異なる偶奇と奇数の $y$ を最小に選ぶことは降下証明の内部の整理。p. 20 では同じ $k=1$ の方程式への降下で矛盾を得る。[p. 19・式 (7′)](https://fliphtml5.com/xlghd/zrvl/Diophantine_Equations_%28L.J._Mordell%29/32/) · [p. 20・証明続き](https://fliphtml5.com/xlghd/zrvl/Diophantine_Equations_%28L.J._Mordell%29/33/) · [出版社の章書誌](https://doi.org/10.1016/S0079-8169(08)60005-7)

### §15.4 への適用

既存の代数照合で、§15.4 の二つの $\alpha_\pm$ 分岐はどちらも $z_{\mathrm B},w\in\mathbb Q$ と $w^2=z_{\mathrm B}^4+z_{\mathrm B}^2+1$ に帰着する。$z_{\mathrm B}=m/n$ を既約に取り $n>0$ とする。$W=n^2w\in\mathbb Q$ の平方は $m^4+m^2n^2+n^4\in\mathbb Z$ なので $W\in\mathbb Z$。原典の $(x,y,z)=(|m|,n,|W|)$ が原始条件を満たす。$n\ne0$ より (7′) は $m=0$、従って $z_{\mathrm B}=0$ を強制する。

既存の例外処理ではこのとき $\alpha_+$ 枝は $r=0,-2$、$\alpha_-$ 枝は $r=0,2$ に限られる。$r=0$ は両枝で3-torsionの $x=0$ と矛盾し、$r=\pm2$ は $\alpha=0$ を強制する。原稿の $t>1$ では $\alpha=a^2>0$。

**D-2 PASS**。§15.4 の3-torsion排除が使う古典命題の式・原始条件・結論が一致する。[Branch B §15.4](proofs/earliest-foundations/BranchB-Section15-torsion.md) · [S194への依存関係監査](PR1860-BRANCHB-PARTITION-AND-TORSION-PARENT-CHECK.md)

## 第２周の終了判定

| Gate | 判定 |
|---|---|
| A | PASS（初回候補23/23） |
| B | PASS（初回外と追加節11/11） |
| C | PASS（固定依存辺39/39。旧 #37 の外部原典は D-1 で解決） |
| D | PASS（原命題と適用条件2/2） |
| E | PASS（固定終端7/7。必要な著者原著の未収載０件） |

**R3-07・R2-01の第２周の原著収集・依存関係確認は完了。PR #1860はDraft・未マージ。** 判定範囲は固定された原著の所在、使用命題・条件、外部２件の一次照合。全証明の独立数学監査・算術証書の再演は別扱い。R3-07の−30無条件排除、R2-01の相関４枝のstrict 75%未満上界、完全直方体の不存在は未解決。
