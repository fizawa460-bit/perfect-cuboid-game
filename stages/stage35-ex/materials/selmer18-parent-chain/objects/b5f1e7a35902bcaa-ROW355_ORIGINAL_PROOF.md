# Stage35EX R3-07：固定C₂の真正2進Kummer像の完全生成

日付：2026-11-04 JST。対象：P23-LOW内の旧signed ±18に対応する同じ種数17曲線 C₂:Y²=h₂(X)。区分：新しい限定局所成果／内部厳密検算PASS／独立数学監査未実施。R0 formal C35-200不変、Branch B OPEN、元source新規排除0。

## 1. 結論と既往との差分

旧row345はdim J₂(Q₂)/2J₂(Q₂)=19を確定したが、埋め込まれた局所像の生成系は未構成だった。旧row353で五つの奇bad素数の真正生成系が得られた後も、2進側は未完として残っていた。

今回は同じ固定曲線について、旧六つの有理除数、**12個の明示的な局所除数**、旧無限遠差D∞からなる19個の類が、真正J₂(Q₂)/2J₂(Q₂)全体を生成することを示す。新しい局所除数は、三つの不分岐拡大上の点と、九つのe=3のtame拡大上の点のtraceから作り、必要な拡大次数は最大9である。

fakeの(x−θ)像は18次元。2進係数代数の単数平方類を38個のF₂座標で表し、18像と対角スカラー−1を合わせた行列のrankが19になる。旧D∞はfake像0で真正類が非零なので、合計19方向となる。旧次元上界19と一致し、生成が完全である。

この結果は新しい全球MW点、rank上界≤16、S類群2部分、全球Selmer交差、163進全MW消滅微分、signed ±18のsource排除を与えていない。rank下界7、上界32+c_S（c_S未確定）、P23-LOW全体OPENを保持する。

## 2. 凍結した対象と偏極・係数の混同防止

旧row342のh₂=A²−XB²、A次数18、B次数17、P₀=(0,1)を使う。h₂はmonic36次で、元の原始標識付きWard sourceからの必要写像・correct signed chamber・S243/S269/S270の条件を変更しない。今回の局所点を元sourceの解又は反例にしない。

旧row344に従い、係数代数K₂=Q₂[θ]/h₂を

\[
u=(\theta+3)/2,\qquad t=u^3/2,\qquad
\mathcal O=\bigoplus_{j=0}^{35}\mathbb Z_2\,u^j/2^{\lfloor j/3\rfloor}
\]

で表す。F(u)=2^−36 h₂(2u−3)はZ[u]のmonic36次式。各完備化でuはuniformizer、ramification e=3、residue degreeは4と8。residue algebraは

\[
\overline{\mathcal O}=\mathcal O/(u)=\mathbb F_2[t]/R(t)\simeq\mathbb F_{16}\times\mathbb F_{256},
\]

\[
R=1+t+t^2+t^4+t^5+t^7+t^8+t^{10}+t^{12}
=(1+t+t^2+t^3+t^4)(1+t^3+t^4+t^5+t^6+t^7+t^8).
\]

Rはsquarefree、R′=(1+t²+t³)²。この最大整環・分解自体は既存成果であり再creditしない。全h₂/F係数と親SHAは同梱JSONで固定した。

## 3. 二種類の実在局所点

### 3.1 不分岐単数の点

整数係数を直接比較すると

\[
F(z)\equiv z^{36}+4(z^{30}+z^{32}+z^{33}+z^{34})
\equiv(z^{18}+2z^{15}+2z^{16})^2\pmod8.
\]

従って任意の2進有限拡大Eと任意の単数z∈O_Eに対し、上の近似平方根は単数で、誤差のv₂≥3>2v₂(2)=2。HenselによりF(z)はEの平方である。これをX=−3+2z、Y=2¹⁸√F(z)へ戻すと実際のC₂(E)点になる。

今回使う三つは、monic不分岐多項式g(z)=z+1、z²+z+1、z³+z+1の根。各E/Q₂の次数は1,2,3で、zは単数。Hensel根を上記近似根のmod4の枝で指定すればGalois-equivariantであり、点のtraceはQ₂有理除数となる。

### 3.2 tame cubicの点

m(w)を次のmonic多項式の一つとする。

| f | m(w) | 拡大Eの次数 |
|---:|---|---:|
| 1 | w+1 | 3 |
| 2 | w²+w+1 | 6 |
| 3 | w³+w+1 | 9 |

不分岐拡大E₀/Q₂をm(w)=0で定義し、π³=2wを満たすE=E₀(π)を取る。この三次式はE₀上Eisensteinなので、E/Q₂はe=3、residue degree f、整数環基底はπ^r w^k（0≤r<3、0≤k<f）。

\[
G(Z)=F(\pi Z)/2^{12}\in\mathcal O_E[Z],\qquad
\overline G(Z)=R(\overline w Z^3).
\]

σ_fをR(w)のresidue平方根の0/1係数liftとする。mはR・R′を割らないため、σ_fは単数であり、G(1)−σ_f²≡0 modπ、G′(1)≡wR′(w)≠0 modπ。

Y₀=σ_f又はσ_f+π^j w^kを下表で指定する。どの場合もY₀≡σ_f modπなので、Henselにより

\[
G(\zeta)=Y_0^2,\qquad\zeta\equiv1\pmod\pi
\]

の根ζ∈O_Eが一意に存在する。従って

\[
X=-3+2\pi\zeta,\qquad Y=2^{24}Y_0
\]

はC₂(E)の実際の点である。有限精度で平方に見えたという主張ではなく、単元導関数を持つHensel根として点を定義している。局所除数はD=Tr_{E/Q₂}(P)−3fP₀である。

| ラベル | f | Y₀ |
|---|---:|---|
| TAME_1 | 1 | σ₁ |
| TAME_2 | 1 | σ₁+π |
| TAME_3 | 1 | σ₁+π² |
| TAME_4 | 2 | σ₂ |
| TAME_5 | 2 | σ₂+π |
| TAME_6 | 2 | σ₂+πw |
| TAME_7 | 2 | σ₂+π² |
| TAME_8 | 3 | σ₃ |
| TAME_9 | 3 | σ₃+π |

すべて局所Q₂除数であり、Q有理の新MW点ではない。

## 4. (x−θ)の正しい像

良い除数Dに対する標準的な(x−θ)写像をK₂*/(K₂*² Q₂*)へ取る。Poonen–Schaefer §5の定義により、有限拡大点のtraceにはnormを用いる。

旧h₂=A²−XB²からθ=(A(θ)/B(θ))²で、P₀による分母(−θ)^degreeは平方とQ₂スカラーで落ちる。不分岐の点はg(u)を像の代表に使える。

tameの点ではu_E=πζ、n=3f、g_E(S)=Norm_{E/Q₂}(S−u_E)。元のX=−3+2u_Eへの戻しによる2^nと符号はQ₂スカラーなので、fake像は[g_E(u)]。すべての共役u_Eのv₂が1/3であり、g_EのNewton slopeは−1/3。従って

\[
a_E=g_E(u)/2^f\in\mathcal O^\times,
\qquad\overline a_E=m(t),
\]

となる。mとRは互いに素なので、二成分のどちらでも単数である。g_Eの係数は明示したHensel根からの2進normであり、全球Z係数多項式とは主張しない。

計算精度は2^{f+9}。norm係数の有限精度とrational 2^f除去、πによる一回の除算を見込んでも、a_E mod2^8を正確に保持する。独立検証器は、発見時のmatrix-power/Newton trace方式を使わず、整数Bareiss determinantをn+1点で計算し、厳密有理補間でnorm多項式を再構成する。

旧六類については旧row342のG(θ)像を再利用する。D1bは [3θ+1]=[3t−2u²] modK₂*²Q₂*、F2は[(t−u)/t]と簡潔に正規化できる。他の四類は同梱の旧G(θ)をrational 2冪で正規化した単数を使用。これは旧全球rank6/7の再証明や新点追加ではない。

## 5. 38平方類座標とスカラー商

両完備化でv(u)=1、v(2)=3。U_i=1+u^i Oとする。単数のresidueを平方liftで除き、U₁へ正規化する。

- i=1,3,5の各商はresidue algebraの12方向を保つ。i=2,4の項は単数の平方で除く。
- i=6では、(1+u³b)²の先頭係数がb²+t^−1 b。従って残る二bitは、F₁₆とF₂₅₆のそれぞれのabsolute trace Tr(t²c)である。
- U₇は平方。v(1−a)>2v(2)を用いるHensel判定で閉じる。

したがって単数平方類の座標は12+12+12+2=38方向。独立性も上の付値の最小項から分かる。平方(1+b)²−1=2b+b²は深さ6未満では偶数深さを先頭に持ち、深さ6だけArtin–Schreierのtrace商が残る。

各完備化の不分岐次数は4/8で偶数なので、双方にQ₂(√5)が含まれ、5は平方。一方−1は平方でない。rational 2は両成分で付値3を持つので、単数平方類内の対角Q₂スカラー像はちょうど−1の一方向である。このため単数像18本がfake商で独立なことは、**18本と−1を合わせた38×19行列のrank19**で判定する。Q₂の三つの平方類を形式的に三方向すべて引いてはいけない。

この座標法のほかに、独立のmod2→mod4→mod8平方根liftを実装した。mod2の平方写像はrank24・kernel12、mod4の補正はrank12、mod8のArtin–Schreier補正はrank34。生成系38方向と無作為に固定seedで作る単数の積・平方で、座標法とこの平方判定が一致することを検証した。

## 6. 18 fake方向＋真正核1方向

下表の単数座標を−1と一緒に並べるとrank19。旧六つの有理除数だけの局所fake rankは6で、残る12方向が新しい局所除数により補われる。

| 類 | 出所 | 38座標（hex） |
|---|---|---|
| OLD_D1a | 旧Q有理除数 | `31faadb001` |
| OLD_D1b | 旧Q有理除数 | `3f85728405` |
| OLD_D2 | 旧Q有理除数 | `0000001001` |
| OLD_D4 | 旧Q有理除数 | `31cd2d4003` |
| OLD_D9 | 旧Q有理除数 | `036e788425` |
| OLD_F2 | 旧Q有理除数 | `1263e0eadb` |
| UNRAM_1 | 新Q₂局所除数・不分岐 | `0000000001` |
| UNRAM_3 | 新Q₂局所除数・不分岐 | `0adb001001` |
| UNRAM_5 | 新Q₂局所除数・不分岐 | `3ada001001` |
| TAME_1 | 新Q₂局所除数・e3 | `3c6ac3cb6b` |
| TAME_2 | 新Q₂局所除数・e3 | `36d3ae5b6b` |
| TAME_3 | 新Q₂局所除数・e3 | `35ddc3cb6b` |
| TAME_4 | 新Q₂局所除数・e3 | `1dbf24636e` |
| TAME_5 | 新Q₂局所除数・e3 | `1752d2936e` |
| TAME_6 | 新Q₂局所除数・e3 | `1b2e3f236e` |
| TAME_7 | 新Q₂局所除数・e3 | `21be24636e` |
| TAME_8 | 新Q₂局所除数・e3 | `1165f4c6de` |
| TAME_9 | 新Q₂局所除数・e3 | `18a11956de` |
| 対角スカラー−1 | 商で除く一方向 | `0b21adb000` |


旧row352のD∞=[∞₊−∞₋]はfake像0。真正Kummerの核が高々1次元であることは既存の完全列／Poonen–Schaefer Thm11.3による。本曲線は種数17が奇数で、Q₂上のbranch orbit次数は12,24の偶数のみなので、この核は非自明である。同じ定理でD∞が生成元になる。従って上表の18類を真正Kummerへ持ち上げ、D∞を加えると19方向が独立になる。

旧row345のdim J₂(Q₂)/2J₂(Q₂)=17+dim J₂(Q₂)[2]=17+2=19と一致するので、**これら19個は真正局所像の完全な生成系**。単にfake像のrankを真正像のrankと同一視した証明ではない。

## 7. 全球交差へ渡す明示的な条件と数え過ぎ防止

局所像はすべて単数代表を持つ。従って一般のK₂の平方類αが局所Kummer像に入るには、二成分の付値が

\[
v_{\mathfrak p_4}(\alpha)\equiv v_{\mathfrak p_8}(\alpha)\pmod2
\]

でなければならない。rational 2と局所平方で単数代表を選び、その38座標へ、同梱JSONの19個の線形形式を適用するとすべて0になることが必要十分である。

この19形式には、既存のrational norm平方条件の二形式が含まれる。従ってnorm後の単数部分で新たに残る余次元は17、付値の一条件を加えるとfull fake norm空間に対する局所余次元は18。全fake ambientは38、norm kernelは36、局所像は18次元である。

**これを全球候補空間で18個独立な新制約が得られた、と読み替えない。** 全球像を共通座標へ写した後の制約rankは未計算。c_Sと全球の欠けた平方類方向も未取得のため、真Sel²≤16やrank≤16はまだ導かれていない。

## 8. 内部厳密検証と監査境界

NumPyは固定サイズの整数演算だけに使い、int64の上限を式で検査する。浮動小数点・数値p進log・GRH仮定は使用しない。標準Pythonによる旧row342/345の親検証器も再演し、旧h₂の恒等式・六有理除数・既存局所次元を確認した。これら旧成果の再creditは0。

新検証器は、親SHA、二通りのh₂(2u−3)展開、正確な整数環の積、Hensel導関数と近似誤差、独立determinantによるnorm、多段平方根判定、38座標と18+1のrank、直交制約とnorm形式、破損行列の負検査を行う。通常実行とpython -Oの両方を記録する。

通常／最適化実行はともに1769検査・20負検査PASS。fake rank18、真正rank19、normの二条件を含む単数19制約のrankを照合。全球での制約rankは未計算。

これは同一担当による内部検算であって、独立hostile数学監査ではない。Hensel根・除数trace・even-degree (x−θ)のkernel・次元公式の幾何学的適用は、上記の証明と一次資料を根拠にし、プログラムだけで形式証明したとはしない。

## 9. 重複判定・失効する旧NEXT・次に必要な証明

着手前にP23方式見直し、R0 ACTIVE、R3の現行方式・339–354行、旧row342/344/345/352/353の親証書を照合。F₂次元19、五奇bad生成系、旧六有理除数、D∞、固定36次数体・整数環はREUSE。新しい差分は、残っていた2進局所像の**実生成と埋め込み座標、全球交差用の局所線形条件**。新しい独立ルートや一般的2-descent理論を作ったわけではなく、既存R3-07へ限定局所完成として登録する。世界的な新規性は主張しない。

旧NEXT「2進19次元の局所像の生成系を構成する」は、本固定C₂では解消し失効。次は、今回の2進像と旧五奇素数・実局所像を、全域を含む認証された全球平方類／cohomology座標へ組み込み、c_Sを含む安全な上界と制約の実rankを認証すること。前回の最小証明書方針を維持し、通常類群全体や指数1単数群の完成を一律の必須手順へ戻さない。

その後も全MWへの163進消滅微分・a₀単元・元source円盤との非交差が必要。今回の局所除数を新しいJ₂(Q)点として加算しない。固定±18が未排除で、残る全LOWの完了、R2 MID/HIGH、S231 formal release、B_wide境界はそれぞれ別に未完である。

## 10. 一次資料・凍結親資料

- Poonen–Schaefer, Explicit descent for Jacobians of cyclic covers of the projective line, J.Reine Angew.Math.488 (1997),141–188。[著者版](https://math.mit.edu/~poonen/papers/descent.pdf)、§5の(x−T)定義・norm、Thm11.3のeven-degree kernel。奇数次数のinjectivityをそのまま使わない。
- 旧row342の実除数とh₂=A²−XB²、row344の最大整環、row345のe3/f4,f8と次元19、row352のD∞、row353の五奇bad生成系をSHA固定で同梱。
- 運用上の位置づけ：[P23方式見直し](https://chatgpt.com/library?file_id=libfile_2f11fbedf9508191a52f72e9b037e66b&account_id=personal)。[R3正本](https://docs.google.com/spreadsheets/d/17BQc6iakGQ7tdxMAVORnOPGa6KjH0uiaiAbbVMO2kRs/edit)、[R0正本](https://docs.google.com/document/d/1UKVlpL0CmAEAIpRN_eE63JllyN1RjqbBaGIG2o4UH4Q/edit)。
