# Stage35EX R3-07 row373 — \(C_{29}\) の全2進局所Kummer像

2026-11-06 JST。P23-R3-07 LOW、固定signed \(\pm30\)。row372の局所3類独立性を継承する。

**新結果。** \(J(\mathbb Q_2)/2J(\mathbb Q_2)\) の真正 \(x-\theta\) Kummer像を、既知3類と新たに構成した50個の局所除数から張った。53本の小行列式は \(1\bmod2\)。従って**53次元の全像**が確定し、両局所体で付値は偶数。単元座標107ビット上の54本の独立な所属条件を同梱した。実Kummer像も符号3次元で確定し、根体に対して2で極大な明示整数環を得た。著者厳密再現PASS、独立監査PENDING。新規signed指数排除0。

## 1. 入力と曲線の拡大体上での正規化

\(F=F_{29}\)、\(C_{29}:y^2=F(x)\)、\(J=\operatorname{Jac}(C_{29})\)、\(\deg F=105\)。\(K=\mathbb Q[\theta]\)、\(F(\theta)=0\)。親row371とrow372の限定監査を継承する。特に \(K\otimes\mathbb Q_2=K_{21}\times K_{84}\)、\(K_{3f}\simeq U_f(\pi)\)（\(f=7,28\)、\(U_f\) は不分岐次数 \(f\)、\(\pi^3=2\)）。\(J(\mathbb Q_2)/2J(\mathbb Q_2)\) の次元は \(52+1=53\)。奇数次数の \(x-\theta\) 写像はこの商からノルム核平方類への単射。次元公式と写像は [Stoll, Implementing 2-descent for Jacobians of hyperelliptic curves, §4](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/98/3/83397/implementing-2-descent-for-jacobians-of-hyperelliptic-curves)。

\(E=\mathbb Q_2(\pi)\) と置く。新変数 \(X,Y\) を
\[
x=-1+\pi^2X,\qquad y=2^{35}Y,\qquad
\mathcal F(X)=2^{-70}F(-1+\pi^2X)
\]
で定める。整数Taylor係数 \(c_i\) を \(F(-1+T)=\sum_i c_iT^i\) とすると、各非零 \(c_i\) で \(3v_2(c_i)+2i-210\ge0\) を検算した。従って \(\mathcal F\in\mathcal O_E[X]\)。剰余は親row371の既約 \(r_7,r_{28}\) による \(r_7(X^3)r_{28}(X^3)\) と一致し、平方自由。

各 \(U_f=\mathbb Q_2[z]/(r_f(z))\) では \(r_f\) を係数0,1の整数リフトに取る。剰余で \(w^3=z\) を満たす \(w\) を一つ定め、\(\mathcal F\) の単根 \(w^2\) を持ち上げて \(\Theta_f\) を得る。対応する元の根は \(\theta_f=-1+\pi^2\Theta_f\)。row371の二つの軌道への対応は \(\overline{\Theta_f}^{\,3}=\overline z^{\,2}\) と \(r_f\) の既約性で決まる。検証器は両根を \(\pi^9\) までHenselで求め、\(\mathcal F(\Theta_f)=0\bmod\pi^9\) と導関数の単元性を確認する。

## 2. 50個の真正局所除数とノルム

各証書に、モニックな既約剰余多項式を整数リフトした不分岐体 \(U_d\) と、\(M_d=U_d(\pi)\) の整数元 \(X\) を指定する。\(X\) は証書の整数係数をそのまま用いた元。有限環は
\[
(\mathbb Z/8)[z,\pi]/(h_d(z),\pi^3-2)=\mathcal O_{M_d}/\pi^9.
\]
50件のすべてで \(\mathcal F(X)\) は単元。45件は \(\mathcal F(X)\equiv Y_0^2\bmod\pi^9\) を収録した \(Y_0\) で検算し、残る5件は \(\overline{\mathcal F}'(\bar X)=0\) の円盤で平方類0を確認して \(Y_0^2\equiv\mathcal F(X)\bmod\pi^7\) の平方根を再構成した。いずれも \(v_\pi(2Y_0)=3\) なので、強いHensel条件 \(v_\pi(\mathcal F(X)-Y_0^2)>6\) から実際の \(Y\in M_d\) が存在する。

\(P=(-1+\pi^2X,2^{35}Y)\) とし、\(P-\infty\) の \(\mathbb Q_2\) へのノルムを取った局所除数類を使う。Kummer像は各根 \(\theta_f\) に対して
\[
\prod_{\sigma:M_d\hookrightarrow\overline{\mathbb Q}_2}\bigl(\sigma(x(P))-\theta_f\bigr)
\quad\bmod K_{3f}^{\times2}.
\]
\(P\) の最小定義体が \(M_d\) より小さい場合も、重複度付きのノルム除数として有効。

検証器は不分岐方向の全共役を \(h_d\) の単根のHensel持ち上げで求め、\(q(S)=\prod_{\sigma:U_d\hookrightarrow U_d}(S-\sigma X)\) を再計算する。ここでは \(\sigma\) を \(\pi\) に自明に延長する。分岐方向で \(\pi\mapsto\eta\pi\)（\(\eta^3=1\)）とし、\(q^\eta\) はこの置換を係数に適用したもの。平方 \(\pi^{6d}\) を除いた積は
\[
(-1)^d\prod_{\eta^3=1}\eta^{2d}q^\eta(\eta\Theta_f).
\]
実際 \(\sigma(x(P))-\theta_f=\pi^2(\eta^2\sigma X-\Theta_f)\)。積は \(\eta^3=1\) で各因子を \(a+b\eta+c\eta^2\) にまとめ、\(a^3+b^3+c^3-3abc\) で計算した。全100件の局所評価で \((a+b+c)((a-c)^2-(a-c)(b-c)+(b-c)^2)\) とも一致。正規化後はすべて単元であることを確認した。

既知の \(H,D_+,D_-\) の3類では、\(B_\star(\theta_f)/\pi^{104}\)、\(\pi-\Theta_f\)、\(-\Theta_f\) を使用。\(B_\star(-1+\pi^2X)/\pi^{104}\) の各係数が整数であることを直接確認した。除いた \(\pi^{104},\pi^2,\pi^2\) はいずれも平方。\(K_{21}\) の最初の \(U_1\) 係数はrow372の \(0x3c,0x77,0\) と一致する。

## 3. 平方類と全像への所属判定

各 \(U_f(\pi)\) で、単元平方類を \(\pi^7\) までで決める。残差の平方根を除いて剰余を1にした後、昇順に消去する。

- 奇数層 \(i=1,3,5\) は、残余体の \(z^j\) 基底ごとに \(1+\pi^iz^j\) を取り、その積の指数を記録する。
- 偶数層 \(i=2,4\) の先頭係数は、\(1+\pi^{i/2}b\) の平方で消す。
- 最終の \(i=6\) 層は \((1+\pi^3b)^2\equiv1+\pi^6(b^2+b)\bmod\pi^7\) なので、残余体から \(\mathbb F_2\) へのトレース1ビットを記録する。

\(1+\pi^7\mathcal O\) の元はHenselで平方。平方の最初の非零層は \(i<6\) なら偶数なので、選んだ奇数層の生成元は独立である。最終層の平方はトレース0に一致する。これで単元平方類に \(3f+1\) 個の線形座標を与える。符号化順は \(U_1,U_3,U_5\) の各 \(f\) ビット、次にトレース1ビット。積は座標のXOR。

\(K_{21}\) の22ビットを下位、\(K_{84}\) の85ビットを上位に置いた107ビット空間で、既知3行と新規50行を消去した。53列の小行列式を別に計算し \(1\bmod2\)。従って既知次元53をすべて実現する。今回の基底が全て単元で代表できることから、**真の2進Kummer像では両成分とも付値が偶数**。

\(\alpha=(\alpha_{21},\alpha_{84})\) の所属判定は、まず両付値の偶奇を確認し、偶数なら \(\pi\) の偶数冪を除いて単元座標 \(v\) にする。証書 `kummer2_membership.json` の54本のマスク \(m\) すべてで \(\operatorname{popcount}(v\mathbin{\&}m)\equiv0\bmod2\) が必要十分。54本の独立性と53行の消去を検証器で照合する。

| 由来 | 独立方向 |
|---|---:|
| 既知 \(H,D_+,D_-\) | 3 |
| \(\overline{\mathcal F}'(\bar X)\ne0\) の円盤からのノルム | 45 |
| \(\overline{\mathcal F}'(\bar X)=0\) の円盤からのノルム | 5 |
| 合計 | 53 |

## 4. 実Kummer像と2で極大な整数環

有理数演算のSturm列は無限遠での符号変化数 \((56,49)\) を与え、相異なる7実根 \(\alpha_1<\cdots<\alpha_7<0\) をそれぞれ有理区間に一意分離した。署名は \((7,49)\)。実点の \(x\) は \(F(x)>0\) の四つの開区間で \(x-\alpha_i\) の符号列を与える。分岐点を避けた実除数表示では非実閉点のノルムは各実成分で正。従って真正実Kummer像は次元3で、\(\alpha_1\) の座標が正、添字 \((2,3),(4,5),(6,7)\) の各対が同符号であることが必要十分。四つの区間の符号列から各対だけを反転する3方向を得る。

根体の別表示 \(G(T)=A_\star(-T^2)+T B_\star(-T^2)\)、\(G(\rho)=0\)、\(\theta=-\rho^2\) を使う。\(t=\rho-1,\ \beta=t^3/2\) とすると、row371の \(v_2(t)=1/3\) と奇素数で2が単元であることから、各 \(t^r\beta^q\)（\(0\le r\le2,\ 0\le q\le34\)）は大域整数。これらの張る格子 \(\mathcal O'\) は \(\mathbb Z[\rho]\) を指数 \(2^{1785}\) で含む。実際 \(i=3q+r\) とすると基底が \(t^i/2^q\) で、\(\sum_i q=1785\)。整数判別式の再計算は
\[
\operatorname{disc} F=2^{3640}\operatorname{disc}G,\qquad
\operatorname{disc}G=-2^{3640}\cdot199\cdot M
\]
を与えた。\(M\) は証書に収録した150桁の正の奇数で、\(199\nmid M\)。従って
\(\operatorname{disc}\mathcal O'=-2^{70}\cdot199\cdot M\)。
row371の体判別式の2付値70と一致するので \(\mathcal O'\otimes\mathbb Z_2=\mathcal O_K\otimes\mathbb Z_2\)。奇素数では \(\mathcal O'\otimes\mathbb Z_p=\mathbb Z_p[\rho]\) だから、\(\mathcal O'\) は局所化で積に閉じた整数環。\(t^3=2\beta\) と \(2^{-35}G(1+t)=0\) を \(t^r\beta^q\) で書いた整数関係もJSONに収録した。

奇素数 \(p\) で \(p^2\nmid\operatorname{disc}F\) なら局所Kummer条件は付値偶数に一致する（Stoll, Proposition 4.6）。これと今回の2進像から、大域2-Selmer類の奇付値があり得るのは \(p^2\mid M\) の奇素数の上だけ。199は付値支持から外れる。\(M\) の平方因子の有無は未確定。

## 5. 採否と次の計算

row370の元source条件、row371の条件付き階数下界5、row372の既知3類の局所独立を継承。今回の新規差分は50局所除数による全53次元の実現、2進所属条件と偶付値、実符号のKummer条件、2で極大な明示整数環。新規全域排除0。LOW残9絶対指数・17 signed枠。独立監査PENDING。

次は \(p^2\mid M\) の奇素数を確定し、その上の素イデアル集合を \(S\) として、\(S\) の外で偶付値を持つ大域平方類のノルム核を認証する。候補空間は \(S\)-単元平方類と \(S\)-類群の2-ねじれの完全性が必要。実・2進・必要な奇素数の局所像を交差し、真2-Selmer次元4以下が認証できた場合に元の \(\pm30\) を排除できる。全MWの31進射影上界も未証明。

- [row372の独立数学監査](https://docs.google.com/document/d/1fYswZfrNZaq4mOUJpnKcp3aDRBv9tZAGrNZF4hUeHnQ/edit)
- [row371の親証明](https://drive.google.com/file/d/1-9vBo6wLKkjPB3twoWt1MLcajDZjNwjJ/view)
