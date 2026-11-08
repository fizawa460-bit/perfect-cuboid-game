# Stage35EX R3-07 row371 — 既知3類の31進対数と \(\pm30\) の階数条件

2026-11-06 JST。P23 R3-07 LOW。row370の固定signed \(\pm30\)、同一の原始標識付き基底の続き。

**結論**。種数52の \(C_{29}:y^2=F_{29}(x)\) で、既知3類 \(H,D_+,D_-\) のアーベル対数を法 \(31^2\) で決定した。31で割って還元した3行と、元sourceが強制する \(e_0,e_1\) の計5行は独立。従って \(\pm30\) の元sourceが存在するなら \(\operatorname{rank}J(\mathbb Q)\ge5\)。**全MWの階数上界4を証明すれば、両符号を排除できる。** 著者厳密再現PASS、独立監査PENDING。今回は全域排除0枠。

## 1. 入力と還元を消す整数

\(F=F_{29}\)、\(J=\operatorname{Jac}(C_{29})\)。row370の有理類は

\[
P_0=(0,1),\qquad P_\pm=(\pm1,2^{35}),\qquad
D_0=[P_0-\infty],\quad D_\pm=[P_\pm-\infty],\quad 2H=D_0 .
\]

\(H\) のMumford形は \((b_\star,-a_\star\bmod b_\star)\)。入力JSONから \(F=a_\star^2+xb_\star^2\) と \(F(\pm1)=2^{70}\) を整数上で再検算した。 \(F\bmod31\) は平方自由。

前回の有限体Frobenius計算が与えた整数を \(N\) とする。

~~~text
393648362324456806647414264130928641711553162973261279756877858799612593368832
~~~

今回の証明に必要なのは \(N\equiv13\bmod31\) と \(N\overline D_0=N\overline D_+=N\overline D_-=N\overline H=0\) のみ。後者は通常のgcd付きCantor法で4件とも \((u,v)=(1,0)\) に到達することを直接検算した。位数候補を得たFrobenius計算は、この消去性の証明に使わない。

以下 \(p=31\)、\(g=52\)、\(\omega_j=x^j dx/(2y)\)（\(0\le j<g\)）。\(\log\) はこの順のヤコビアン対数ベクトル。

## 2. 法 \(p^2\) の群計算

補助因子 \(T=(u,v)\) は \(u\) モニック次数52、\(\bar u\) は26個の互いに異なる既約二次式の積、\(\bar v\) はその全根で単数。各二次剰余体で \(F\bmod u_i\) の非零平方根を選び、法 \(p^2\) へHensel持ち上げし、CRTで組み合わせる。使える二次円盤は226個。最終的に \(E=T+ND\) のMumford対 \((U,V)\) を法 \(p^2\) で計算し、\((\bar U,\bar V)=(\bar u,\bar v)\) を照合する。

演算の合成は \(\gcd(\bar u_1,\bar u_2)=1\) のときのCRT、または倍算で \(v+u c\)、\(2v c\equiv (F-v^2)/u\bmod u\) を使う。後者は \(2v\) が単元の場合だけ採用した。全ての逆元を法 \(p\) で検査し、法 \(p^2\) ではNewtonの一回補正と積の一致を検査する。

合成直後の半簡約形 \((u,v)\) の次数を \(m>g\) とする。\(r=m+g\) とし、次の条件で \(a(x)-b(x)y\) を一つ作る。

\[
u\mid a-bv,\qquad
\deg a\le\lfloor r/2\rfloor,\quad
\deg b\le\lfloor(r-(2g+1))/2\rfloor .
\]

極次数 \(r\) を持つ側の最高係数を1とする。\(r\) が偶数なら \(a\) の先頭、奇数なら \(b\) の先頭である。\(a=bv\bmod u\) と置けば、残りは \(b\) の小行列の線形系になる。法 \(p\) で正則な系だけ採用し、法 \(p^2\) へ持ち上げて等式を確認する。関数のノルム \(a^2-b^2F\) を \(u\) で割って符号を調整すると次数 \(g\) のモニック \(q\) になる。残余の点の \(y\) は \(a/b\) で、\(b\bmod q\) が単元の場合、新しい群の代表は \((q,-a/b\bmod q)\)。これは極次数 \(r\) と関数の主因子から従う。

この一段の簡約は最高係数・行列・逆元を単元の範囲に限定した群計算である。整数 \(N\) の二進桁を処理する間は \([m]D+T_i\) を保持し、倍算後に \(-2T_i+bD+T_j\)（\(b\) は次の桁）を足す。単元条件に失敗したら、先に既知の \(T_j-T_i\) で平行移動して別の補助因子を使う。最後は指定の \(T\) に戻す。この回避は群の等式で制御し、近似に頼らない。

成功した法 \(p^2\) 演算4,406件は、全件の法 \(p\) 還元を通常のCantor法で別算した。補助因子を選ぶ二つの異なる組で、3類の全52成分が一致。\(H\) については \(\log D_0/2\) に加えて、Mumford形の \(H\) を直接計算しても一致した。

## 3. 微小積分の最初の桁

\(T=(u,v)\)、\(E=(U,V)\) は各同一剰余円盤に点を一つずつ持つ。 \(\delta=(U-u)/p\bmod p\) と置く。 \(\bar u\) の根 \(\alpha\) に対応する二点の \(x\) の差は、法 \(p^2\) で

\[
x_E-x_T\equiv -p\,\delta(\alpha)/\bar u'(\alpha).
\]

\(\bar v(\alpha)\ne0\) なので、\(\omega_j\) の微小積分を \(p\) で割って還元した値は

\[
 -\frac{\alpha^j\delta(\alpha)}{2\bar v(\alpha)\bar u'(\alpha)}.
\]

高次項の付値は2以上。例えば \(x_E-x_T\in p\mathcal O\) の \(k\) 乗を \(k\) で割る項は \(k-v_p(k)\ge2\)（\(k\ge2\)）。各成分を加えると

\[
\frac{\log(ND)_j}{p}\bmod p
= [x^{g-1}]\left(-\frac{x^j\delta(x)}{2\bar v(x)}\bmod\bar u(x)\right).
\]

この係数式は平方自由モニック \(\bar u\) に対するLagrange補間の恒等式 \(\sum h(\alpha)/\bar u'(\alpha)=[x^{g-1}](h\bmod\bar u)\)。26二次成分それぞれで分母 \(\bar u'\) を含む元の式の有限体トレースを計算し、係数式と全成分で一致させた。ヤコビアン対数と同円盤微小積分の対応は [Balakrishnan–Bradshaw–Kedlaya, Explicit Coleman integration for hyperelliptic curves](https://arxiv.org/abs/1004.4936)。

\(N\) は31進単数なので \(N^{-1}\bmod31\) を掛けると \(\log(D)/p\bmod p\) を得る。\(D_0\) の行はさらに2で割る。52成分はJSONに収録。最初の5成分は次の通り。

| \(\log(D)/31\bmod31\) | \(\omega_0\) | \(\omega_1\) | \(\omega_2\) | \(\omega_3\) | \(\omega_4\) |
|---|---:|---:|---:|---:|---:|
| \(H\) | 13 | 16 | 17 | 13 | 15 |
| \(D_+\) | 6 | 0 | 13 | 14 | 9 |
| \(D_-\) | 5 | 13 | 24 | 17 | 16 |

## 4. 元sourceに対する帰結

\(L_{\mathrm{MW}}=(\operatorname{span}_{\mathbb Q_{31}}\log J(\mathbb Q))\cap\mathbb Z_{31}^{52}\)。元の \(\pm30\) 候補が存在するなら row370 により \(e_0,e_1\in L_{\mathrm{MW}}\bmod31\)。今回の三行もこの還元に入る。三行の後に \(e_0,e_1\) を足した行列の列 \(0,1,2,3,4\) の行列式は \(20\bmod31\)。従って \(\dim L_{\mathrm{MW}}/31L_{\mathrm{MW}}\ge5\)、つまり \(\operatorname{rank}J(\mathbb Q)\ge5\)。

また、次の線形形式は**既知3行**を消す。添字は0から始まる。

\[
\lambda_0(z)=z_0+25z_2+20z_3+z_4,\qquad
\lambda_1(z)=z_1+30z_2+19z_3+27z_4 \quad(\bmod31).
\]

\((\lambda_0,\lambda_1)\) は \(e_0,e_1\) を標準基底に送る。全MWの還元のこの2座標像が次元1以下であると認証できれば、階数上界に代わる排除証明になる。今回の二形式が全MWを消すとはまだ言えない。

## 5. 2進分解と局所Kummer像

階数上界のための2-descentに向け、根体 \(K=\mathbb Q[\theta]\)、\(F(\theta)=0\) の2進成分を決定した。row370の \(a_\star,b_\star\) から

\[
G(t)=a_\star(-t^2)+t b_\star(-t^2),\qquad
F(-t^2)=G(t)G(-t).
\]

\(G\) はモニック次数105。根を \(\rho\) とすると \(\theta=-\rho^2\) で、\(F\) の既約性から \(\mathbb Q(\rho)=K\)。\(G(1+T)=\sum c_iT^i\) の整数係数は \(3v_2(c_i)+i\ge105\) を満たし、両端 \(i=0,105\) で等号。従ってNewton多角形は傾き \(-1/3\) の一辺で、全ての根について \(v_2(\rho-1)=1/3\)。残余多項式は

\[
R(Z)=\sum_{i=0}^{35}\left(c_{3i}/2^{35-i}\bmod2\right)Z^i .
\]

\(R\) は定数項1で、相異なる二つの既約因子 \(r_7=Z^7+Z+1\) と

\[
\begin{aligned}
r_{28}={}&Z^{28}+Z^{24}+Z^{22}+Z^{21}+Z^{20}+Z^{17}+Z^{16}+Z^{14}\\
         &+Z^{13}+Z^{12}+Z^{11}+Z^9+Z^8+Z^7+Z^6+Z^4+1
\end{aligned}
\]

の積。剰余多項式の積とFrobenius冪・gcdによる既約性判定を同梱検証器で再現する。

\(\pi^3=2\) とすると \(2^{-35}G(1+\pi T)\) の \(\pi\) 還元は平方自由な \(R(T^3)\)。よってHenselにより \(\beta=(\rho-1)^3/2\) の還元が \(r_d\) の根となる \(\rho\) は、各 \(d=7,28\) についてちょうど \(3d\) 個。各集合は \(\mathbb Q_2\) のGalois作用で安定で、各軌道は分岐指数が3の倍数、剰余次数が \(d\) の倍数なので大きさ \(3d\) 以上。従って各集合は一軌道で、\(K\otimes\mathbb Q_2\) は \((e,f)=(3,7),(3,28)\) の二体の積。分岐は tame で \(v_2(\operatorname{disc}K)=70\)。

各成分で \(\overline\beta\) は立方。\(d=7\) では剰余体の位数から、\(d=28\) では \(Z^{(2^{28}-1)/3}\equiv1\bmod r_{28}\) の厳密計算から従う。よってHenselにより \(\beta=w^3\) となる単元 \(w\) があり、\((\rho-1)/w\) は2の立方根。次数 \(d\) の不分岐拡大 \(U_d\) を用いると、二体はそれぞれ \(U_7(\sqrt[3]2)\), \(U_{28}(\sqrt[3]2)\) と書ける。

この分解から \(\dim_{\mathbb F_2}J(\mathbb Q_2)[2]=1\)。また \(K\otimes\mathbb Q_2\) の平方類空間の次元は \((21+2)+(84+2)=109\)、ノルムは奇数次数なので全射。従ってノルム核は次元106、局所Kummer像は \(\dim J(\mathbb Q_2)/2J(\mathbb Q_2)=52+1=53\)。次元には [Stoll, Implementing 2-descent for Jacobians of hyperelliptic curves, Lemma 4.4](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/98/3/83397/implementing-2-descent-for-jacobians-of-hyperelliptic-curves) を用いた。2進局所像の基底と大域2-Selmer上界は今後の課題。

## 6. 採否と再現

row338の「補助因子への平行移動と微小積分」の考え方とrow370の二方向必要条件を継承。今回の差分は \(C_{29}\) の3有理類の対数52成分、次数52での法 \(31^2\) の単元検査付き計算、階数5という元sourceの必要下界、および根体の2進分解。階数上界4または全MW射影の上界は未証明。研究残表は9絶対指数・17 signed枠。次は2進局所Kummer像の基底と大域平方類の有限候補空間を計算し、2-Selmer次元4以下または全MW射影の次元1以下を認証する。

同梱の検証器は曲線係数、半分点恒等式、有限体での消去、二組の補助因子を使った演算、直接の \(H\) と二次体トレース、行列式、2進のNewton多角形と残余因子を再現する。

- [row370の証明](https://drive.google.com/file/d/1DHS6puK_KMW5xY77dikQDECv1j-AYKAU/view) · [row370の独立監査](https://docs.google.com/document/d/1aV7X2-A8DzRq1XjuogBRA1JSYnnu616DygbO4Vv9A6s/edit)
- [row338の既存微小積分法](https://docs.google.com/spreadsheets/d/17BQc6iakGQ7tdxMAVORnOPGa6KjH0uiaiAbbVMO2kRs/edit#gid=1884882255&range=A338:J338)
