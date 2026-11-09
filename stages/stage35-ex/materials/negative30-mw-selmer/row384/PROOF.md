# Stage35EX R3-07 row384　二指標平均による2階数の条件付き上界と固定4リフト課題

2026-11-07 JST。P23 R3-07 LOW、同じ元 signed \(-30\) と \(J_{29}\)。著者厳密再現PASS。row383・384の独立数学監査待ち。

\[
 \Omega_2=\left\{s\ \middle|\ 
 0.63<\operatorname{Re}s\le1,\quad
 |\operatorname{Im}s|\in(0.26,0.77)\cup(1.03,1.46)\right\}.
\]
**通常類群の2階数 \(c_{\rm Cl}\ge2\) なら、非自明な通常類群二次指標に付随するHecke \(L\) 関数の少なくとも一つが \(\Omega_2\) に零点を持つ。** さらに、どの独立二指標を取っても、その2本と積の計3本の中に該当するものがある。GRHを使わない必要条件。

従って \(\Omega_2\) が全該当二次指標で無零なら \(c_{\rm Cl}\le1\)。その無零性の下で元 \(-30\) が存在すれば、\(c_{\rm Cl}=1\)、MW階数10、2-Selmer次元10が全て等号になる。特定した単元Selmer類 \(\delta_\star\) も4-Selmer類へリフトする必要がある。**本行は \(\Omega_2\) の無零性や \(\delta_\star\) のリフト不能性を証明していない。**

## 1. 二指標の平均

\(K=\mathbb Q(\theta)\) は \(F_{29}\) の根体で次数105、署名 \((7,49)\)。row381–382から、2上の両素イデアルは主、4,140本の主イデアル関係から2,492個の奇素イデアル類が通常類群の2倍商で消える。親の最大整環と全有限非分岐・実分裂の識別を継承する。

独立な二指標を \(\chi_1,\chi_2\) として \(X^\times=\{\chi_1,\chi_2,\chi_1\chi_2\}\) と置く。各素イデアル \(\mathfrak p\) で
\[
 \frac13\sum_{\chi\in X^\times}\chi(\mathfrak p)^m=
 \begin{cases}
 1 & m\ \text{が偶数},\\
 1 & m\ \text{が奇数で両指標が}\ \mathfrak p\ \text{に自明},\\
 -1/3 & m\ \text{が奇数でそれ以外}.
 \end{cases}
\]
値が \((1,1)\) 以外の二ビットでは、三つの値の和が \(-1\) になる。これにより、分裂未確定の素イデアルで奇数べきの一様下界が \(-1/3\) となる。2,492個の既知分裂では \(+1\)。これは指標を列挙する操作を要しない。

## 2. 固定した試験関数と厳密スコア

row383と同じ型の試験関数で、長さを
\[
 \mathcal L=\{91/10,\ 23/10,\ 23/10,\ 7/20,\ 7/20\},
 \qquad g=*_{\ell\in\mathcal L}B_\ell,\quad
 F_0=(g*g)/(g*g)(0)
\]
とした。支持半幅 \(T=72/5\)、区分多項式の次数は9。\(B_\ell=\ell^{-1}\mathbf 1_{[-\ell/2,\ell/2]}\)。\(F=F_0\sum_j\lambda_j\cos(v_jx)\) とし、固定有理数は `fixture384.json` に収録。検査器は \(\sum_j\lambda_j=1\)、\(v_0=0\)、\(\lambda_0>\sum_{j>0}|\lambda_j|\) を確認するので \(F(0)=1\)、\(F\ge0\)。

変換は \(z=s-1/2\) で
\[
 \phi_0(z)=\frac1{(g*g)(0)}
    \prod_{\ell\in\mathcal L}\left(\frac{\sinh(\ell z/2)}{\ell z/2}\right)^2,\qquad
 \phi(z)=\sum_j\frac{\lambda_j}{2}
            \bigl(\phi_0(z+iv_j)+\phi_0(z-iv_j)\bigr).
\]
Poitou明示公式の正規化を
\[
 \sum_{\rho_\chi}\phi(\rho_\chi-1/2)=-105\,\mathcal B_\chi(F)
\]
とする。\(\mathcal B_\chi\) の無限素点項と素数項はrow383と同じ式。3本で平均し、§1の下界を適用した。次数1の尾部は \(5003<p\le1{,}982{,}760\) の全147,058素数を再計数し、一次因子147,527個が親の表と全件一致。\(e^T<1{,}982{,}760<5003^2\) なので、尾部の次数2以上と高次項は支持外。小素数は法 \(p\) の因数分解を既存の順序と照合する。

指数核の1,024項と明示剰余上界を使う区間積分もrow383と同じ方式。次数9用に係数を自動再生成する。Arb 192-bit外向き丸めで
\[
 \frac13\sum_{\chi\in X^\times}\mathcal B_\chi(F)>1/25,\qquad
 \frac13\sum_{\chi\in X^\times}\sum_{\rho_\chi}
             \operatorname{Re}\phi(\rho_\chi-1/2)<-4.2
\]
を得た。使用した下界の式は \(0.0523946411808995\ldots\)。

## 3. \(\Omega_2\) の外の零点では不足

row383で構成した \(\sigma=7/5\) のHadamard重みを使う。
\[
 M_\chi=\sum_{\rho_\chi}\frac{\sigma-\operatorname{Re}\rho_\chi}{|\sigma-\rho_\chi|^2}<100.
\]
この上界は個別の全二次指標に対して有効。既知分裂点で \(L'/L\) の符号を使うこと、次数2以上の積分上界、\(\vartheta(x)\le(\log4)x\) の次数1尾部評価を継承した。上界の式は \(99.186384435239\ldots\)。平均も100未満。

\(u=|\operatorname{Re}\rho-1/2|\)、\(t=|\operatorname{Im}\rho|\)、\(a=\sigma-1/2\) とし
\[
 W(u,t)=\tfrac12\left(\frac{a-u}{(a-u)^2+t^2}
                        +\frac{a+u}{(a+u)^2+t^2}\right),\quad
 \sum_{\rho_\chi}W=M_\chi.
\]
\(\varepsilon=7/200\) とする。\(t\le1/10\) では支持上の余弦が非負。\(t\ge12\) では各変調項の \((t-v_j)^{-10}\) 上界を使う。\(|\phi|/W\) の上界は \(t=12\) で \(0.000352\) 未満で、その先は減少する。

中間では次の5閉矩形の全834小矩形を、次数7までのTaylor係数と半径 \(1/2\) のCauchy剰余を用いて検査した。

| \(t\) | \(u\) | 認証した小矩形 |
|---|---|---:|
| \([0.1,0.26]\) | \([0,0.5]\) | 9 |
| \([0.77,1.03]\) | \([0,0.5]\) | 20 |
| \([1.46,12]\) | \([0,0.5]\) | 786 |
| \([0.26,0.77]\) | \([0,0.13]\) | 13 |
| \([1.03,1.46]\) | \([0,0.13]\) | 6 |

全てで \(\operatorname{Re}\phi(u+it)+\varepsilon W(u,t)>0\)。境界は閉矩形に含めた。Cauchy剰余はrow383と同じ \((\sum|\lambda_j|)\phi_0(u_0+1/2)(2r)^8/(1-2r)\)。従って3本の全零点が \(\Omega_2\) の外なら
\[
 \frac13\sum_{\chi\in X^\times}\sum_{\rho_\chi}
     \operatorname{Re}\phi(\rho_\chi-1/2)
 \ge-\frac{\varepsilon}{3}\sum_{\chi\in X^\times}M_\chi>-3.5,
\]
§2と矛盾。これで冒頭の主張が従う。スコアとmomentの有理閾値での余裕は \(4.2-3.5=0.7\)。

## 4. 条件付きの次の算術課題を一つ固定する

次の無零性を \(\mathrm{ZF}_2\) と呼ぶ。

\[
 \mathrm{ZF}_2\quad
 \text{全非自明通常類群二次指標の }L(s,\chi)\text{ は }\Omega_2\text{ に零点を持たない}.
\]

§3より \(\mathrm{ZF}_2\Rightarrow c_{\rm Cl}\le1\)。元 \(-30\) なら、row382独立監査済みのsourceジェットと八有理類によりMW階数は10以上。row381の無条件上界 \(\dim\operatorname{Sel}^{(2)}\le9+c_{\rm Cl}\) を合わせると、\(\mathrm{ZF}_2\) の下では
\[
 c_{\rm Cl}=1,\quad \operatorname{rank}J_{29}(\mathbb Q)=10,\quad
 \dim\operatorname{Sel}^{(2)}=10,\quad \Sha(J_{29}/\mathbb Q)[2]=0.
\]
\(J_{29}(\mathbb Q)[2]=0\) は親の既約性による。従って2-Selmer群の全類が有理点のKummer像であり、全類は自然な写像
\[
 \operatorname{Sel}^{(4)}(J_{29}/\mathbb Q)\longrightarrow
 \operatorname{Sel}^{(2)}(J_{29}/\mathbb Q)
\]
でリフトする。これは \(J[4]\xrightarrow{[2]}J[2]\) と有理点のKummer写像の整合性による。

親の55本のノルム1単元平方類を、`unit_basis_witnesses.json` の零始まり順序で \(u_0,\ldots,u_{54}\) とする。9次元単元Selmer部分と既知8有理類の差の剰余類から次を選んだ。
\[
 \delta_\star=\prod_{i\in I}u_i,\qquad
 I=\{0,1,8,12,14,17,18,19,21,23,25,29,32,37,38,39,40,42,45,48,54\}.
\]
このマスクは \(\mathtt{0x4125e122ae5103}\)。2進平方類座標は
\(\mathtt{0x44b88774c94772d6bc5c8f05827}\)、2進所属障害0、実符号 \(\mathtt{0x1e}\) で実Kummer所属も満たす。既知8有理類の2進像の張る空間に入らないことを厳密検査した。親が認証した単元像の単射性により、これは大域でも異なるSelmer類。

選択は既知8類を加えた256個の代表の中で、親の生成多項式の奇数べき出現を最少にするもの。その数は122。`ninth_generator_inputs.json` に対象多項式を索引付きで収録し、`four_lift_target384.json` に正ノルム化する符号を記載した。各多項式の整数終結式を再計算し、平方類代表のノルムが正の平方であることも確認する。全有限付値の相殺と単元Selmer所属は親の55単元証書を継承する。

大域4リフト不能が証明できれば、無条件に
\[
 \operatorname{rank}J_{29}(\mathbb Q)
 \le\dim\operatorname{im}(\operatorname{Sel}^{(4)}\to\operatorname{Sel}^{(2)})
 \le8+c_{\rm Cl}.
\]
実際、有理点の全Kummer類はこの像に入り、像は \(\delta_\star\) を含まない真部分空間だから少なくとも一次元小さい。この場合、元 \(-30\) の必要階数10から \(c_{\rm Cl}\ge2\) へ進み、§3の二帯を必要条件にできる。この推論は \(\Sha\) の有限性を仮定しない。

従って
\[
 \boxed{\ \mathrm{ZF}_2
 \ \text{かつ}\ 
 \delta_\star\notin\operatorname{im}\bigl(\operatorname{Sel}^{(4)}
             \to\operatorname{Sel}^{(2)}\bigr)
 \quad\Longrightarrow\quad
 \text{元 }-30\text{ の全域排除}\ }.
\]
リフトの有無は未判定。局所所属と大域4リフトの違いを保ち、この含意を排除結果として集計しない。

## 5. 差分・記録・次の証明

row383は非自明指標1本の存在から三帯の必要零点を得た。本行は二指標独立の場合を平均で扱い、より狭い二帯の必要零点を証明し、その無零性から2階数上界1を得る。さらに無零性条件下の残る算術課題として、明示した \(\delta_\star\) の4リフト不能を十分条件にした。これは無条件の類群2階数上界や4リフト不能の証明を含まない。

無条件の新規signed排除0。LOW残9絶対指数・16 signed枠、元 \(-30\) とBranch BはOPEN。次は \(\mathrm{ZF}_2\) と \(\delta_\star\) の4リフトを具体的に検査する。row383三帯の全該当指標での無零性、または直接の無条件 \(c_{\rm Cl}=0\)・同じ \(J_{29}\) のMW階数上界9も引き続き十分。

- [Poitou明示公式 Belabas–Diaz y Diaz–Friedman、式(3)–(4)](https://doi.org/10.1090/S0025-5718-07-02003-0)
- [row383の三帯とガロア群](https://drive.google.com/file/d/104olY-E_uZ0drh_EkNt_EOLEo8J9fkic/view)
- [row382独立数学監査](https://docs.google.com/document/d/1gJ1KbYSF_AOaTu-d4nQYu_sIQoxU6rhfBpXKizDgEWU/edit)
- [row381の全単元とSelmer上界の独立監査](https://docs.google.com/document/d/1siQsZfW85ir4uLvAV9_uy7DVELHT1rrPXcyN5sbNUeE/edit)
