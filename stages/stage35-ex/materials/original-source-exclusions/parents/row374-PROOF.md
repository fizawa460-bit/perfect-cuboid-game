# Stage35EX R3-07 row374 — 奇判別式の完全分解と大域単元の2進条件

2026-11-06 JST。P23-R3-07 LOW、固定signed \(\pm30\)。\(C_{29}\) のrow373独立監査PASSを継承する。

**新結果。** 判別式の奇数部分は、指数が全て1の6素数の積。row373で2極大とした整数環は根体 \(K\) の最大整環 \(\mathcal O_K\) に等しい。全ての有限素イデアルでSelmer類の付値は偶数なので、例外集合 \(S\) は空。さらに、ノルム1の大域単元17本が2進所属条件に独立な障害を与える。従って
\[
\dim_{\mathbb F_2}\mathrm{Sel}^{(2)}(\mathbb Q,J_{29})
\ \le\ 38+\dim_{\mathbb F_2}\mathrm{Cl}(\mathcal O_K)[2].
\]
著者厳密再現PASS、独立監査PENDING。新規signed指数排除0。

## 1. 奇判別式と最大整環

\(F=F_{29}\)、\(K=\mathbb Q[\theta]\)、\(F(\theta)=0\)。親の別表示は
\[
G(T)=A_\star(-T^2)+TB_\star(-T^2),\qquad
G(\rho)=0,\qquad \theta=-\rho^2,\qquad t=\rho-1 .
\]
\(G\) はモニック次数105で \(F(-T^2)=G(T)G(-T)\)。親row373の2極大な整数環を \(\mathcal O'\) とする。その基底は \(t^i/2^{\lfloor i/3\rfloor}\)（\(0\le i\le104\)）、判別式は \(-2^{70}\cdot199\cdot M\)。

整数判別式の再計算と素数証書により、\(199M\) が次の6素数の積であることを確認した。各指数は1。

| 素数 |
|---:|
| 199 |
| 11385628289870903 |
| 83743632872646893 |
| 278122000170586522903289 |
| 128315161223632986986799118753 |
| 14758359995285977308443723270301431340936632015367331820639800963 |

整数上で \(\operatorname{disc}F=-2^{7280}(199M)\)、\(\operatorname{disc}G=-2^{3640}(199M)\)。\([\mathcal O_K:\mathcal O']\) は奇数で、その平方は \(\operatorname{disc}\mathcal O'\) を割る。奇数部分が平方自由なので指数は1。従って上の基底は大域整数基底であり、\(\operatorname{disc}K=-2^{70}(199M)\)。

素数証書では、整数演算による9段の楕円曲線検査と、終端を含む小さい素数の完全 \(n-1\) 型Lucas検査を行った。楕円曲線の段では \(N+1-\tau=sq\)、\(q>(\lfloor\sqrt[4]{N}\rfloor+2)^2\)、良い判別式、\([s]P\) がアフィン、\([q]([s]P)=O\) を確認した。全ての非零分母が \(N\) と互いに素なので、各 \(p\mid N\) の有限体に同じ演算を還元できる。次段の素数 \(q\) が \(\#E(\mathbb F_p)\) を割り、合成 \(N\) の最小素因数 \(p\le\sqrt N\) ではHasse上界に矛盾する。証書の形式は [PARI primecert の仕様](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Arithmetic_functions.html#primecert)。

独立な局所形状の検算として、法 \(M\) と法199の多項式ユークリッド計算でも単元だけで除算し、\(\gcd(F,F')=X-r\) を得た。実際にBézout恒等式、\(F(r)=F'(r)=0\)、\(F''(r)\) の単元性をそれぞれ検算。従って全ての奇悪素数で重根はただ一つの二重根。

## 2. 全有限素点の偶付値とSelmerの大域候補

\(p\) を奇素数とする。§1から \(p^2\nmid\operatorname{disc}F\) なので、\(J(\mathbb Q_p)/2J(\mathbb Q_p)\) の真正 \(x-\theta\) 像は局所ノルム核の偶付値部分に一致する。\(p=2\) ではrow373の完全局所基底により両成分とも偶付値。従って全球候補は例外素数を付けない
\[
V=\{[\alpha]\in K^\times/K^{\times2}:\ 
(\alpha)\text{ は分数イデアルの平方},\quad
N_{K/\mathbb Q}(\alpha)\in\mathbb Q^{\times2}\}.
\]
この中でrow373の2進・実条件をともに満たすものが真の2-Selmer群。奇素数で残る追加条件はない。奇数次数曲線のSelmer同定と奇素数の局所条件は [Stoll, Implementing 2-descent for Jacobians of hyperelliptic curves, Proposition 4.2 と Proposition 4.6](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/98/3/83397/implementing-2-descent-for-jacobians-of-hyperelliptic-curves)。

\((\alpha)=\mathfrak a^2\) に \([\mathfrak a]\) を対応させると、次が完全。
\[
0\longrightarrow U^1\longrightarrow V\longrightarrow
\mathrm{Cl}(\mathcal O_K)[2]\longrightarrow0,\qquad
U^1=\ker\bigl(N:\mathcal O_K^\times/\mathcal O_K^{\times2}
                   \longrightarrow\mathbb Q^\times/\mathbb Q^{\times2}\bigr).
\]
任意の2ねじれイデアル類の平方は主イデアルなので全射であり、生成元のノルムは各有理素数で偶付値。符号が負なら \(-1\) 倍して正にできる。実埋込みがあるため根の単元は \(\{\pm1\}\)。署名 \((7,49)\) と奇数次数から \(\dim U^1=7+49-1=55\)。従って \(c=\dim_{\mathbb F_2}\mathrm{Cl}(\mathcal O_K)[2]\) と置くと \(\dim V=55+c\)。

## 3. 17個の独立な単元障害

Ward多項式の反転因子から整数多項式 \(h_i\) を選び、17個の単元を
\[
u_i=\varepsilon_i\, h_i(\theta)/t^{m_i},\qquad \varepsilon_i\in\{1,-1\}
\]
で構成した。選択後の証明には探索手順を必要としない。全ての \(h_i,m_i,\varepsilon_i\) を `unit_witnesses.json` に固定した。

各 \(i\) で整数終結式から
\[
N(t)=-G(1)=2^{35},\qquad
N(h_i(\theta))=\varepsilon_i\,N(t)^{m_i}
\]
を直接検算した。従って奇素点で \(h_i(\theta),t\) は単元。2進の両成分では、親と同じ \(\pi^3=2,\ \theta=-1+\pi^2\Theta\) を取り、\(t=\pi W\) を持ち上げる。\(G(1+\pi W)/\pi^{105}=0\) の単根を法 \(\pi^9\) で計算し、\(\Theta=-W^2-\pi^2W\) と \(W\) の単元性を照合した。

\(h_i(-1+X)=\sum_j b_{ij}X^j\) の非零係数は \(3v_2(b_{ij})+2j\ge m_i\)。このため \(\pi^{-m_i}h_i(-1+\pi^2\Theta)\) を分母なしで法 \(\pi^9\) で評価できる。両方で単元となり、\(W^{m_i}\) で割って \(\varepsilon_i\) を掛けると \(u_i\) の単元平方類を得る。全 \(u_i\) は大域単元でノルム1。

各 \(u_i\) に対し、row373の107ビット単元座標から54本の所属条件の値を計算した。17行の小行列式は \(1\bmod2\)。従って \(U^1\) 上でも \(V\) 上でも、この条件写像の階数は少なくとも17。全単元から来る2進適合部分は次元38以下であり、\(V\) を母空間とする真2-Selmer次元は \(38+c\) 以下。実条件を課すとこの上界以下になる。

## 4. 現在の障壁と再現

新規差分は奇判別式の完全分解、2極大から大域極大への昇格、全有限素点の偶付値と \(S=\varnothing\) による候補空間の同定、17単元の独立な2進障害。row370–373の既存の元source条件、条件付き階数下界5、2進53次元と実3次元の局所像は継承する。真2-Selmer次元4以下と元 \(\pm30\) の排除は未証明。LOW残9絶対指数・17 signed枠、P23 LOWとBranch BはOPEN。

次は明示最大整環で \(\mathrm{Cl}(\mathcal O_K)[2]\) とノルム1単元平方類の完全基底を認証し、row373の2進・実条件を全候補に適用する。2-Selmer次元4以下を認証できれば元の \(\pm30\) 両符号を排除できる。31進の全MW二座標射影上界も十分条件として残る。

証書の再現は `verify_row374.py`。素数証書、整数判別式、2つのBézout検査、17単元の整数ノルム、34局所平方類、17小行列式を再計算する。探索時の因数分解プログラムは再現に不要。

- [row373の証明](https://drive.google.com/file/d/186EMCRPpghJGC3vCCqjorZT321kggv7T/view)
- [row373独立数学監査](https://drive.google.com/file/d/1cFlvlHDseLuj-rUzJLOlCzZp1sJzEy4n/view)
