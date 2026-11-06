# MB104-F83：楕円共同像の 8-捩れ剰余類による排除と高種数共同像の Hermitian 有限篩

**一行要約。** 固定モデルの楕円商 \(E_s\) は \(\operatorname{End}E_s=\mathbf Z[i]\) を持ち、その8分岐値は \(P+E_s[(1+i)^3]\) である。この事実と F74 の既存局所公式を合わせると、**MB101 多枝条件を満たす正の欠損 \(\varepsilon>0\) の楕円共同像層は空**である。また F75 の高種数共同像は Gauss–Hermitian 型の有限数値クラスに還元でき、\(k=8\) なら共同像種数が奇数、像の総 \(\delta\) と Hermitian 行列式が偶数になる。

- 日付：2026-11-02。
- 基準：`fizawa460-bit/perfect-cuboid-game`、PR #1850 (draft)、**読み取り時点の固定 head** `33ef9d164684a655b97b5cb5e4d0d47a142e9938`。
- 研究ノートの状態：**NEW PROOF / CONDITIONAL ON F74, F75; UNREVIEWED; ZERO CREDIT**。
- 正本：GitHub のみ。Google Drive の独立読み出しは行わない。
- 対象：MB101 の非例外・非例外成分の既約曲線、\(g(E)\in\{0,1\}\)、箱の少なくとも1節点に2本以上の正規化枝、\(\varepsilon>0\)。完全直方体の存在性、MB104 全域の閉鎖、credit を主張しない。
- 新計算：`mb104_f74_f75_window.py`（同梱、Python 3 標準ライブラリのみ）。このコードは必要数値クラスを数えるだけで、実在曲線や線形系を判定しない。

## 1. 入力と依存関係

固定資料の再利用を明示する。

- **REUSE E01–E04**：等号面 \(\varepsilon=0\) の処理。再導出しない。今回の証明は両脚エタールに対する E01 の合同部分群の論法を使用しない。
- **REUSE F70 §2**：
  \[
  C_8:\quad a^2=c^2+d^2,\quad b^2=c^2-d^2,\quad e^2=2cd
  \]
  は滑らかな種数5曲線。\(G_8\) は \(a,b,e\) の独立符号反転である。各単独反転は8固定点を持ち、異なる単独反転の固定点は交わらない。
- **REUSE F72 §2、F74 §§3–6**：正の \(\varepsilon\) では \(k=|S|\in\{4,8\}\)、\(S\) は二つ以上の単独反転を含む。\(s\in S\) を単独反転として \(E_s=C_8/\langle s\rangle\)、\(B_s\subset E_s\) を被約8分岐値とする。\(Y=\mathrm{Norm}((\pi_s f_1,\pi_s f_2)(Z))\) が楕円なら、\(Y\subset E_s^2\) は滑らかな楕円部分群の平行移動で、二射影の次数は \(a_1,a_2\)、共同写像は一般次数1。\(\varepsilon>0\) のとき4-被覆枝 \(h=4\)。
- **REUSE F74 §§4,6**：\(T_i=u_i^{-1}(B_s)\)、\(I=|T_1\cap T_2|\)、\(b_\triangle=|T_1\triangle T_2|\) とすると
  \[
  |T_i|=8a_i,\qquad b_\triangle=k(g+1),\qquad
  d=\frac{16}{k}(a_1+a_2).\tag{F74}
  \]
  また、単独反転 \(v\in S\setminus\{s\}\) は \(E_s\) 上で反転 \(x\mapsto-x+c_v\) を誘導し、\(B_s\cap\mathrm{Fix}(v)=\varnothing\)。MB101 の多枝条件はこの楕円共同像層で \(I>0\) を必要とする。他型節点を多枝だと再計上しない。
- **REUSE F75 §§3–6**：高種数共同像 \(\gamma=g(Y)\ge2\)、\(h=2\) または4、\(r_0=g(Y/(S/\langle s\rangle))\le g\)、\(d=4h(a_1+a_2)/k\)、\(2\gamma-2=k(r_0-1)+F\)、\(F\le4k+\kappa_F\)。\(\mathcal B_s=0\) の10個の既存数値窓を入力とする。これらの監査を今回完成扱いにしない。

以下の補題2.1–2.4、命題3.1・4.1、有限数値篩は**本稿の新差分**である。新しい外部論文の未確認定理は導入せず、必要な楕円群の基礎事実は証明内で明示する。

## 2. \(E_s\) と分岐8点の正確な構造

### 補題2.1［証明］：\(E_e\) の複素乗法と4冪捩れ8点

\(s\) が \(e\) の符号反転であるとする。このとき
\[
 E_e:\quad a^2=c^2+d^2,\quad b^2=c^2-d^2\ \subset\mathbf P^3_{a,b,c,d}
\]
は種数1の滑らかな四次完全交叉である。その8個の \(C_8\to E_e\) の分岐値は
\[
 B_e=\{c=0\}\sqcup\{d=0\}=P+K,\qquad
 \operatorname{End}(E_e)=\mathbf Z[i],\qquad
 K=E_e[(1+i)^3],\quad |K|=8.\tag{2.1}
\]
ここで \(P\in E_e\) はある点で、群法則の原点は以下で選ぶ。

**証明。** \(C_8\to E_e\) は \(e^2=2cd\) であり、\(c=0\)、\(d=0\) はそれぞれ4個の異なる点を切り、かつ互いに交わらない。各分岐指数は2である。

\(E_e\) の \((a,b,c,d)\) の符号反転を射影スカラー全体 \(-1\) で割った群は位数8。偶数個の座標を反転する部分群は位数4で、非自明な3元は全て固定点を持たない。実際、例えば \(a,b\) を同時反転する写像の固定点は \(a=b=0\) または \(c=d=0\) を要し、両方とも二次式と矛盾する。他の二重反転も、座標を組み替えた同じ検査で固定点を持たない。種数1曲線の固定点を持たない位数2自己同型は非零2捩れ点の平行移動である（任意の自己同型を \(z\mapsto uz+t\) と書けば、\(u\ne1\) の場合 \(1-u\) は全射なので固定点を持つ）。よってこの位数4群は全 \(E_e[2]\) の平行移動群である。

\(c=0\) と \(d=0\) の各4点集合はこの群で安定であり、自由作用だからそれぞれ \(P+E_e[2]\)、\(Q+E_e[2]\) である。両零因子は同じ超平面束 \(\mathcal O_{E_e}(1)\) の切断だから線形同値である。楕円曲線の \(\mathrm{Pic}^0(E_e)\simeq E_e\) の同定（差 \(\sum(P_j-Q_j)\) が零なら、かつそのときに限り次数0因子が主因子）を使うと
\[
 4P+\sum_{t\in E[2]}t=4Q+\sum_{t\in E[2]}t,
 \quad\text{したがって}\quad 4(Q-P)=0.
\]
二つの4点集合は異なるので \(Q-P\notin E[2]\)。したがって \(Q-P\) は**位数4**であり、
\[
 K=E[2]+\langle Q-P\rangle
\]
は \(E[4]\) に含まれる位数8部分群で、\(B_e=P+K\) となる。

次に
\[
 R:(a,b,c,d)\mapsto(a,ib,d,c)
\]
は二次式を保つ位数4の自己同型で、\(b=0,c=d,a=\pm\sqrt2 c\) の点を固定する。そのうち一つを原点に選ぶ。複素トーラス表示 \(E_e=\mathbf C/\Lambda\) で、原点を固定する位数4自己同型は線形写像 \(z\mapsto\pm iz\) である。よって \(\Lambda\) は \(\mathbf Z[i]\) の階数1有限生成捩れなし加群、\(\mathbf Z[i]\) はユークリッド整域なので \(\Lambda=\omega\mathbf Z[i]\)。従って \(\operatorname{End}(E_e)=\mathbf Z[i]\)。

\(R\) は \(c=0\) と \(d=0\) を交換し、\(R(B_e)=B_e\)。原点固定で \(R\) は \(\pm i\) 倍なので \(iK=K\) である。\(E_e[4]\simeq\mathbf Z[i]/(4)\simeq\mathbf Z[i]/((1+i)^4)\) の \(\mathbf Z[i]\)-部分加群はこの局所主イデアル環のイデアルに対応する。位数8のものは一意で、\(E_e[(1+i)^3]\) に等しい。以上で(2.1)。□

**注意。** この議論は任意の8点集合が捩れ点集合だという主張ではない。固定モデルの二次式、8個の特別な分岐値、原点を固定する位数4自己同型に依存する。

### 補題2.2［証明］：三つの単独反転に同じ結論が成立

\(s\in\{a,b,e\}\) のどれについても、適当な原点と \(P_s\) があり
\[
 \operatorname{End}(E_s)=\mathbf Z[i],\qquad
 B_s=P_s+E_s[(1+i)^3].\tag{2.2}
\]

**証明。** \(C_8\) 上で次の射影線形変換を取る：
\[
 \begin{aligned}
 a'&=\sqrt2\,b, & b'&=\sqrt{-2i}\,e,&e'&=\sqrt2\,a,\\
 c'&=c-id, & d'&=c+id.
 \end{aligned}\tag{2.3}
\]
直接展開すると
\[
 a'^2=c'^2+d'^2,\quad b'^2=c'^2-d'^2,\quad e'^2=2c'd'
\]
である。変換は線形可逆であり、\(a,b,e\) の三つの単独符号反転を巡回置換する。よって対応する商と分岐値付き組 \((E_s,B_s)\) は互いに同型であり、補題2.1が移る。□

### 補題2.3［証明］：楕円部分群の Gaussian primitive parameterization

\(E=\mathbf C/\mathbf Z[i]\) とする。\(E^2\) の滑らかな楕円部分群とその平行移動 \(Y\) が両座標へ非定数に射影されるなら、ある \(\alpha,\beta\in\mathbf Z[i]\setminus\{0\}\) と \(p_1,p_2\in E\) により
\[
 Y=\{(\alpha z+p_1,\beta z+p_2):z\in E\},
 \qquad (\alpha,\beta)=\mathbf Z[i],\qquad
 a_1=N(\alpha),\ a_2=N(\beta).\tag{2.4}
\]
このパラメータ化は一般次数1である。

**証明。** 群部分 \(Y_0\) の普遍被覆での接線は \(\mathbf C^2\) の複素直線 \(L\)。\(L\cap\mathbf Z[i]^2\) は階数2格子なので、非零ベクトルの座標比は \(\mathbf Q(i)\) にある。分母を払い、共通 Gaussian 因子を除けば primitive ベクトル \((\alpha,\beta)\) で \(L=\mathbf C(\alpha,\beta)\) と書ける。Bezout の \(u\alpha+v\beta=1\)（\(u,v\in\mathbf Z[i]\)）により、\(t\alpha,t\beta\in\mathbf Z[i]\) なら \(t=u(t\alpha)+v(t\beta)\in\mathbf Z[i]\)。従って格子交差は正確に \(\mathbf Z[i](\alpha,\beta)\)。その商は \(E\) で、\(E\to Y_0\) は埋込みである。平行移動を足せば(2.4)。射影の次数は Gaussian norm。□

### 補題2.4［証明］：二つの分岐逆像の共通部分は「0または8」

補題2.3の \(u_1,u_2\) に対し \(K=E[(1+i)^3]\)、\(B=P+K\) とする。このとき
\[
 T_i=u_i^{-1}(B),\qquad
 \boxed{|T_1\cap T_2|\in\{0,8\}}.\tag{2.5}
\]

**証明。** 交わりが非空なら \(z_0\in T_1\cap T_2\) を取る。\(z\) が同じ交わりに属する条件は
\[
 \alpha(z-z_0)\in K,\qquad\beta(z-z_0)\in K.
\]
\(K\) は \(\mathbf Z[i]\)-部分加群だから Bezout 式より \(z-z_0\in K\)。逆に \(z-z_0\in K\) なら両条件を満たす。従って \(T_1\cap T_2=z_0+K\) であり、ちょうど8点。空の場合のみ0点。□

## 3. F74 楕円共同像の全4層を排除

### 命題3.1［**条件付き証明**］：MB101 の \(\varepsilon>0\) 楕円共同像層は空

**仮定。** F70 の固定モデル、F72 の安定化群区分、F74 §§3–6 にある「\(Y\) は楕円部分群の平行移動」「\(b_\triangle=k(g+1)\)」「\(I>0\) は多枝の必要条件」「\(S\) 内の他単独反転が \(Y\) に作用し、\(B_s\) 上に固定点を持たない」を使用する。F74 全文の独立監査が完了したとは仮定しない。

**主張。** この仮定の下では \(g\in\{0,1\}\)、\(k\in\{4,8\}\) の全組合せで実曲線が存在しない。

**証明。** MB101 の多枝条件から \(I>0\) なので補題2.4により \(I=8\)。F74 の式から
\[
 k(g+1)=b_\triangle=8(a_1+a_2)-2I
 =8(a_1+a_2)-16.
\]
従って
\[
 \boxed{N(\alpha)+N(\beta)=2+\frac{k(g+1)}8}.\tag{3.1}
\]
右辺を4層で評価する。

| \(g\) | \(k\) | 要求される \(N\alpha+N\beta\) | 結論 |
|---:|---:|---:|---|
| 0 | 4 | \(5/2\) | Gaussian norm の和は整数なので不可能 |
| 0 | 8 | \(3\) | 一方が単元、他方が norm 2。以下の反転障壁で不可能 |
| 1 | 4 | \(3\) | 同上 |
| 1 | 8 | \(4\) | primitive Gaussian pair は存在しない |

最後の行は、正の整数の平方和として Gaussian norm 3 が存在せず、和4となる非零 norm の組は \((2,2)\) のみで、norm 2 の両元は \(1+i\) で割れるため primitive に反する、という直接の整数論である。

残りの norm 和3では、射影を交換して \(Y\) を
\[
 Y=\{(x,\lambda x+t):x\in E_s\},\qquad
 N(\lambda)=2,\quad\lambda\in\mathbf Z[i] \tag{3.2}
\]
と書ける。\(\lambda\) は \(1+i\) の単元倍なので \(1-\lambda\) は \((1+i)\) と互いに素であり、\(K=E_s[(1+i)^3]\) 上の自己同型となる。

\(S\) は \(s\) 以外の単独反転 \(v\) を含む。\(E_s\) 上のその誘導作用を \(r(x)=-x+c\) とする。\(B=P+K\) は \(r\) で不変だから
\[
 \kappa:=c-2P\in K.\tag{3.3}
\]
しかし \(B\) は \(r\) の固定点を持たない。\(P+z\in B\) が固定点となる条件は \(2z=\kappa\) であるから、
\[
 \boxed{\kappa\notin2K}.\tag{3.4}
\]

\(v\in S\) により \(Y\) は対角作用 \((r,r)\) で不変。(3.2) に \((r,r)\) を代入して
\[
 2t=(1-\lambda)c.\tag{3.5}
\]
他方 \(I=8>0\) なので \(Y\cap(B\times B)\ne\varnothing\)。\(x=P+z\)、\(\lambda x+t=P+z'\)（\(z,z'\in K\)）を取り、\(\lambda K\subset K\) から
\[
 t=(1-\lambda)P+w\quad\text{となる } w\in K.\tag{3.6}
\]
(3.5)と(3.6)から
\[
 2w=(1-\lambda)(c-2P)=(1-\lambda)\kappa.\tag{3.7}
\]
左辺は \(2K\) にある。右辺の乗数 \(1-\lambda\) は \(K\) の自己同型であり、特性部分群 \(2K\) を自身へ写すため、(3.4)から右辺は \(2K\) に属さない。矛盾。norm 和3の両層も消える。□

**適用の境界。** これは F74 の既存の \(I>0\) 帰結に依存する。\(I=0\) の楕円像（多枝でないもの）や、\(Y_s\) の種数が2以上の場合を排除しない。F74 の同じ表を再度上限計算したのではなく、固定分岐8点の *Gaussian 4冪捩れ配置* を用いて元の有限窓の内部を排除した。

## 4. F75 高種数共同像の新フィルタ

### 命題4.1［証明］：\(k=8\) では \(\gamma\) が奇数、\(\delta_{\mathrm{img}}\) が偶数

\(Y\to D\subset E_s^2\) を F75 の正規化写像、\(\gamma=g(Y)\ge2\) とする。\(k=8\) なら \(S=G_8\) で、\(s\) と異なる二つの単独反転 \(v,w\) の積は \(E_s\) 上の非零2捩れ点 \(\tau\) による平行移動である（F74 §4.1／F75 §3）。その対角作用は
\[
 t_\tau:(x,y)\longmapsto(x+\tau,y+\tau),\qquad\tau\ne0,\quad2\tau=0,
\]
であり、\(D\) を保存する。

**証明。** \(t_\tau\) は全 \(E_s^2\) 上に固定点を持たないから、その正規化への引上げは \(Y\) 上の固定点なしの位数2自己同型である。\(Y\to Y/\langle t_\tau\rangle\) はエタール次数2であり、RHから
\[
 2\gamma-2=2(2g(Y/\langle t_\tau\rangle)-2),
 \qquad\boxed{\gamma\ \text{は奇数}}.\tag{4.1}
\]

像 \(D\) の特異点は \(t_\tau\) により異なる2点ずつへ移り、各対の局所解析芽は同型である。従って像の局所 \(\delta\)-不変量の総和は偶数：
\[
 \boxed{\delta_{\mathrm{img}}=p_a(D)-\gamma\equiv0\pmod2}.\tag{4.2}
\]
この結論は標識点での多枝 \(\mathcal B_s>0\) を**許したまま成立**する。特に **\(k=8,\gamma=2\) は、B_s の値や h2/h4 に関係なく非存在**。□

### 命題4.2［証明］：高種数共同像の有限 Hermitian 型

\(A=E_s^2\)、\(D=j(Y)\) を既約像曲線とする。\(a_i=\deg u_i\)。\(\gamma\ge2\) なら
\[
 \boxed{a_1\ge2,\quad a_2\ge2}.\tag{4.3}
\]
なぜなら \(a_i=1\) なら正規化 \(Y\to E_s\) は有限次数1、従って同型で \(\gamma=1\) となるからである。

補題2.2の \(E_s=\mathbf C/\mathbf Z[i]\) を用いる。\(A\) の数値因子類は product principal polarization に関して Gaussian 整数係数 Hermitian 行列で表示できる。二座標の順序を \(a_i=\deg(Y\to E_s)\) に合わせれば
\[
 \boxed{H_D=\begin{pmatrix}a_2&\xi\\\bar\xi&a_1\end{pmatrix},\quad
 \xi\in\mathbf Z[i],\quad
 \Delta:=\det H_D=a_1a_2-N(\xi)\ge1.}\tag{4.4}
\]

**証明（数値交差）。** \(A\) の格子は \(\mathbf Z[i]^2\)。第一Chern形式は格子上の積分値交代形式で、\((1,1)\) 条件を課すと \(\mathrm{Im}(\bar z^T H w)\) の形となり、\(H\) は Hermitian、対角成分整数、非対角成分 Gaussian 整数である。\(D\) と一方の座標ファイバーの交点数が他方への射影次数 \(a_i\) なので対角は(4.4)。格子基本領域でChern形式の2次外積を積分すると
\[
 \frac{D^2}{2}=\Delta,\qquad p_a(D)=1+\Delta,
 \qquad\delta_{\mathrm{img}}=1+\Delta-\gamma\ge0.\tag{4.5}
\]
最後は \(K_A=0\) による随伴と、正規化の \(\delta\) 会計である。\(\gamma\ge2\) だから \(\Delta\ge1\)、すなわち Hermitian 行列は正定値。□

命題4.1を(4.5)に代入すると、**新たに**
\[
 \boxed{k=8\quad\Longrightarrow\quad\gamma\equiv1\pmod2,
 \quad\Delta\equiv0\pmod2,
 \quad\delta_{\mathrm{img}}\equiv0\pmod2.}\tag{4.6}
\]

F75 の \(\mathcal B_s=0\) の既存上限と \(d=4h(a_1+a_2)/k\) を使用すると、\(a_1+a_2\le31\)。よって(4.3)(4.4)と(4.6)は**有限**の整数探索である。これは候補の存在ではなく、実現するなら必ず通過する必要篩である。

## 5. F75 の数値クラス列挙：実行済み

**入力。** F75 §5 の10細分窓。\(h\in\{2,4\}, k\in\{4,8\},r_0\in\{0,1\}\)、種数範囲 \(2\le\gamma\le\gamma_{\max}\)、\(d\le d_{\max}\)。条件
\[
 2\le a_1,a_2,\quad 4h(a_1+a_2)\le kd_{\max},\quad
 \xi=x+iy\in\mathbf Z[i],\quad
 1\le a_1a_2-x^2-y^2
\]
を厳密整数演算で列挙する。さらに \(k=8\) では \(\Delta\) 偶数、\(\gamma\) 奇数を課し、F75 §3 の \(F=2\gamma-2-k(r_0-1)\in[0,4k]\) と \(\gamma\le1+\Delta\) を課す。

**出力。** `NS` は順序つき \((a_1,a_2,\xi)\) の必要数値クラス数、`篩後 NS` は \(k=8\) 偶奇除去後、`(NS,γ)` は種数候補を付した組数である。同一クラスを複数の \(h,g,r_0\) の行で再計上するため、行間合計は**互いに異なる曲線数ではない**。

| \(h,g,r_0,k\) | \(d_{\max}\) | \(a_1+a_2\) 上限 | 順序つき \((a_1,a_2)\) | NS | 篩後 NS | (NS,γ) |
|---|---:|---:|---:|---:|---:|---:|
| 2,0,0,4 | 42 | 21 | 171 | 26,191 | 26,191 | 149,316 |
| 2,1,1,4 | 46 | 23 | 210 | 37,794 | 37,794 | 284,216 |
| 2,0,0,8 | 27 | 27 | 300 | 71,844 | **35,726** | 200,452 |
| 2,1,1,8 | 31 | 31 | 406 | 124,862 | **62,223** | 461,920 |
| 4,0,0,4 | 88 | 22 | 190 | 31,550 | 31,550 | 180,846 |
| 4,1,0,4 | 92 | 23 | 210 | 37,794 | 37,794 | 217,102 |
| 4,1,1,4 | 92 | 23 | 210 | 37,794 | 37,794 | 284,216 |
| 4,0,0,8 | 58 | 29 | 351 | 95,679 | **47,625** | 269,030 |
| 4,1,0,8 | 60 | 30 | 378 | 109,498 | **54,523** | 309,266 |
| 4,1,1,8 | 62 | 31 | 406 | 124,862 | **62,223** | 461,920 |

**判定：証明（数学的な必要条件）＋実行済み（有限整数列挙）。** 10行の大量の数値クラスが残り、実在候補を全て解いたわけではない。\(\xi\) と \(-\xi\) を同一視する同型簡約も行っていない。

## 6. 各 F75 数値クラスで実曲線の存在を判定する具体的手順

以下は **設計／未実行**。必要条件を満たす行列を「曲線の存在」と呼ばない。

1. **曲面と標識を固定。** 補題2.1の \(E_e\subset\mathbf P^3\)、または(2.3)で同型化した \(E_s\) を固定する。標識点は方程式 \(c=0\) または \(d=0\) の8点で与えられる。\(E_s^2\) 上の標識格子 \(\mathcal G_B=B_s^2\)（64点）と \(\mathcal G_F\)（k4で16点／k8で32点）は方程式で既知である。
2. **各 Hermitian 型の線束。** \(H_D\) で定まる数値因子類を持つ代表線束 \(L_D\) を Appell–Humbert の因子（または積因子と Poincaré 線束）で構成する。正定値なので ample。複素トーラス格子上の theta 条件から \(h^0(A,L_D)=\Delta\)、従って \(|L_D|\simeq\mathbf P^{\Delta-1}\) の具体的基底を算出できる。全 \(\mathrm{Pic}^{[D]}(A)\) は \(\mathrm{Pic}^0(A)\) 上の \(L_D\) の捩りを走査して扱う（ample polarization の \(A\to\widehat A\) が全射なので、同値に平行移動パラメータを使える）。
3. **実安定化群を先に課す。** \(S/\langle s\rangle\) の座標変換が \(D\) を集合として保存することを課す。反転の固有切断条件と、k8の非零2捩れ対角平行移動による固有切断条件を theta 表現の線形代数として課す。必要なら \(\mathrm{Pic}^0\) パラメータを併用し、固定点集合の層別を取る。
4. **既約性・正規化。** 得られた切断 \(f=0\) を \(A\) の適切なアフィンチャートで方程式化し、既約性、\(Y=\mathrm{Norm}(D)\)、\(\gamma\)、\(\delta_{\mathrm{img}}\) を計算する。\(\Delta=\gamma-1+\delta_{\mathrm{img}}\) と k8偶奇を確認する。高種数のため両射影 \(u_i:Y\to E_s\) の有限次数を数え直し、\(a_i\) を照合する。
5. **標識点の多枝禁止を正規化上で検査。** 64個の \(q\in\mathcal G_B\) と \(16(k=4)\)／\(32(k=8)\) 個の \(q\in\mathcal G_F\) について \(\mu(q)=|j^{-1}(q)|\) を計算し、\(\mathcal B_s=0\) なら \(\mu(q)\le1\) を課す。**滑らかさを課してはいけない**。cusp は一枝で許され、Puiseux／局所正規化で枝を判定する。固有値条件だけでここを代用しない。
6. **二次拡大の連結性を判定。** \(s=e\) ならアフィン開集合 \(d\ne0\) で \(C_8/E_e\) の函数体は \(k(E_e)(\sqrt{2c/d})\)。\(Y\) 上の二つの平方類 \([u_1^*(2c/d)]\)、\([u_2^*(2c/d)]\in k(Y)^\times/k(Y)^{\times2}\) を求める。両方が非自明であり、かつ等しければ \(h=2\)、非自明かつ独立なら \(h=4\)。一方でも自明なら F75 の h2/h4 正規化配置と矛盾するため拒否する。元の \(C_8\) に戻した既約正規化 \(Z\)、その真の \(S\)-安定化群と \(E=Z/S\) の種数 \(g\) を計算する。
7. **箱曲面の局所条件に戻す。** \(q:C_8^2\to B\) と各節点の局所 A1 商で、個別正規化枝・接触指数 \(m_x\)、\(M\)、\(r\)、\(\varepsilon=M-d-4(1-g)>0\) と MB101 の多枝条件を検証する。他の対角移動成分との交点を無視しない。条件全てを通った場合に限り「実曲線候補」とする。

この7段は、固定 \(a_1,a_2,\xi\) に対する線形系・平行移動・接触・正規化の問題を有限型の代数的パラメータ空間上の構成可能条件へ翻訳する**存在判定の設計**である。有限の「数値クラス」だけから有限個の「曲線」に自動的に還元されるわけではない。全 \(\mathbf C\) パラメータを扱うには、相対正規化と \(\delta\) 層別、標識点での枝数層別を実装し、消去計算で非空性を判定する必要がある。グレブナー基底の具体的実行、各数値クラスの線形系構成、候補の存在／非存在は**未実施**。

## 7. 検算器と実行ログ

**付属コード**：`mb104_f74_f75_window.py`。標準 Python 3 で

```bash
python mb104_f74_f75_window.py
python -O mb104_f74_f75_window.py
```

を実行する。Gaussian norm と Euclidean gcd を使って \(N\alpha+N\beta=2,3,4\) の primitive ordered pair を列挙する。また F75 の10窓について \(a_1,a_2\ge2\)、\(\Delta\ge1\)、k8偶奇条件、\(\gamma\le1+\Delta\)、\(0\le F\le4k\) を整数篩にかける。想定値と照合して不一致は例外を送出する。

実測した主要出力：

```text
F74 primitive Gaussian (alpha,beta) ordered counts by Nalpha+Nbeta:
  A=2: 16
  A=3: 32
  A=4: 0
F74 MB101 conditional: I=8; A=2+k*(g+1)/8
  (g,k)=(0,4): A=5/2, impossible
  (g,k)=(0,8): A=3, graph degree-2, reflection obstruction
  (g,k)=(1,4): A=3, graph degree-2, reflection obstruction
  (g,k)=(1,8): A=4, no primitive Gaussian pair
...
PASS: exact integer arithmetic and expected certificates match
```

F75 の全10行の実測値は §5 に掲載。通常実行で PASS。コード中の検査は理論証明、F74/F75 の独立監査、存在判定の代わりではない。

## 8. 既存との差分、残余、次に監査すべき点

### 差分

- **NEW** 固定 \((E_s,B_s)\) の Gaussian CM・位数8部分群剰余類構造、及び3つの単独反転に対する同型化（補題2.1–2.2）。F70 の曲線方程式は再利用。
- **NEW** 楕円共同像の primitive Gaussian 2成分表示、および \(|T_1\cap T_2|\in\{0,8\}\)（補題2.3–2.4）。F74 の64点や \(8k\) の一般上限の再計上ではない。
- **NEW / CONDITIONAL** MB101 の正の欠損・楕円共同像層の非存在（命題3.1）。\(d\le36\) の単なる改善ではなく、その層を空にする。
- **NEW** 高種数共同像 \(k=8\) の自由平行移動による \(\gamma\) 奇数・\(\delta_{\mathrm{img}}\) 偶数。\(\gamma=2\) の \(k=8\) 層を \(\mathcal B_s>0\) でも除外（命題4.1）。
- **NEW / NECESSARY** F75 の \(a_i\ge2\)、NS Hermitian 型の有限列挙、\(k=8\) で \(\Delta\) 偶数の篩、行別整数件数（命題4.2、§5）。線形系を実際に解いた件数は0。
- **REUSE** E01–E04、F70–F75 の定義・商・RH・枝分類・既存次数窓。F69 の解析的推定や E01 の両脚エタール合同論法は使わない。

### 未解決と次の一手

1. **F74 の独立監査（最優先）。** 新補題の正しさとともに、F74 の \(h=4\)、\(b_\triangle=k(g+1)\)、\(I>0\iff\)（少なくとも必要方向）多枝の局所分類、他反転の固定点回避を確認する。これが通れば正の楕円共同像層の「条件付き」を解除できる。
2. **F75 の実線形系へ移行。** まず \(a_1+a_2\) の最小層（\(a_i\ge2\) なので4）と \(\Delta\) 小の順に、\(S\)-不変 theta 切断を明示し、標識点上一枝と \(h\) の平方類条件を検査する。大きな NS リストを全部「曲線候補」と呼ばない。
3. **\(B_s>0\) への接続。** \(k=8,\gamma\) 奇数の制約は標識枝超過に依存しない。F76–F82 の \(\gamma=2,k=8\) 分岐を先に除外し、残る \(k=4\) と奇数 \(\gamma\ge3\) に対して線束上の平行移動・特異点軌道を利用する。\(\mathcal B_s\) の一様上限を得たとは主張しない。

### 監査用チェックポイント

- 符号反転した \(E_e\) の「二重反転」が本当に固定点なしの \(E[2]\) 平行移動群になること、\(c=0,d=0\) の因子の被約性と4点ずつの軌道。
- 位数4自己同型 \(R\) が原点固定であること、\(B_e\) 保存から \(K=E[(1+i)^3]\) が出ること、(2.3) が単独反転を巡回させること。
- \(Y\) が **像として**楕円 subgroup translate であるときだけ Gaussian primitive に落とすこと。高種数 \(Y\) や \(Z/\langle s\rangle\) に誤転用しない。
- \(I=8\) は \(I>0\) と \(\alpha,\beta\) の primitive 性を両方使う。\(I=0\) の型を無条件排除しない。
- 反転の \(c-2P\notin2K\) は固定点回避が必要。\(1-\lambda\) の \((1+i)\)-互除性は \(N\lambda=2\) を使用。
- F75 で \(\delta_{\mathrm{img}}\) と箱上の \(\delta\)、例外接触 \(M\) を混同しない。NS 篩の数値クラス数を実曲線の存在件数・新規除外件数に換算しない。

**終了状態：** F74 は既存の未監査幾何学補題に条件付けた *EMPTY* の新証明。F75 は数値候補の有限化と \(k=8\) 奇数種数フィルタを取得したが、個々の線形系の実在性判定は未着手。\(\varepsilon>0\) 全体と MB104 は **OPEN**。GitHub の既存台帳・STATE・PR head は変更していない。**credit 0**。


## 9. 固定 GitHub 参照パス

以下のリンクは指定 head `33ef9d164684a655b97b5cb5e4d0d47a142e9938` に固定され、Google Drive に依存しない。

- [MB104 status map](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/33ef9d164684a655b97b5cb5e4d0d47a142e9938/stages/stage32/32-03-multibranch/MB104/MB104-STATUS-MAP-20261102.md) — 認定地図であって結果の正本ではない。
- [F70](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/33ef9d164684a655b97b5cb5e4d0d47a142e9938/stages/stage32/32-03-multibranch/MB104/drive-research/research/MB104-F70.md) — 商モデルと固定点。
- [F71](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/33ef9d164684a655b97b5cb5e4d0d47a142e9938/stages/stage32/32-03-multibranch/MB104/drive-research/research/MB104-F71.md) — 欠損恒等式。
- [F72](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/33ef9d164684a655b97b5cb5e4d0d47a142e9938/stages/stage32/32-03-multibranch/MB104/drive-research/research/MB104-F72.md) — 安定化群区分。
- [F73](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/33ef9d164684a655b97b5cb5e4d0d47a142e9938/stages/stage32/32-03-multibranch/MB104/drive-research/research/MB104-F73.md) — 局所接触と分岐因子。
- [F74](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/33ef9d164684a655b97b5cb5e4d0d47a142e9938/stages/stage32/32-03-multibranch/MB104/drive-research/research/MB104-F74.md) — 本稿が条件付きで閉じる楕円共同像層。
- [F75](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/33ef9d164684a655b97b5cb5e4d0d47a142e9938/stages/stage32/32-03-multibranch/MB104/drive-research/research/MB104-F75.md) — 本稿の Hermitian 数値篩が対象とする高種数共同像層。
- [E04](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/33ef9d164684a655b97b5cb5e4d0d47a142e9938/stages/stage32/32-03-multibranch/MB104/route-E/E04-EQUALITY-FACE-CLASSIFICATION.md) — 等号面の既存結果。

**文献注意。** 新規の主張のために現代論文の外部定理を引用していない。使用した標準的な楕円曲線・複素トーラス・交差理論の事実については、適用条件と導出を補題の証明に明記した。F74/F75 については上記 GitHub 固定稿の該当節に依存する。
