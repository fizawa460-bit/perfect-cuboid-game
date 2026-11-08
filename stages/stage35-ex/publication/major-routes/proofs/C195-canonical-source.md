# 保存した主要証明本文

出典：[C35-195-R0-PROOF.md](https://drive.google.com/file/d/1qI7lyiiJF_5Mf7mevzInxG-HZGRQzqUF/view?usp=drivesdk)

2026-11-09 JSTに取得した歴史的原著本文。本文中の採否・NEXTは執筆時点の記録である。[現在の整理と訂正](../README.md)を優先する。この保存で新しい独立監査や正式採択は付与しない。

取得形式：Drive上の保存済みMarkdownのreadable text。原ZIPへのバイト同一性は主張しない。

---

# C35-195 — 実際のWard軌道の補平方からcanonical整数ソースを再構成する

RUN_ID=R0-20261028-C35-195-EXACT-SIGMA-CANONICAL-SOURCE
BASE_HEAD=C35-194 COMPLETE
AUTHORITY=V74_GOAL4AK_SECTION334 / INTERNAL_PROVISIONAL
ACTIVATION=共有4文書のrevision-guarded prepend、旧全文保持readback、paired COMPLETE receiptの読み戻し後。それまではC35-194。
BranchA=USER_PAUSED; indexed BranchB/Bwide/Stage35=OPEN; E1=UNPROVEN。
新規の完全物理解の排除=0。独立の一般的方法=0。external_hostile_audit=false。

## 1. 今回の前提を減らした定理

正の原始LABELLED A²+B²=C², C odd, D=AC を固定する。元の曲線と点は

    E:y²=x(x−A²)(x+C²), P=(D,BD), T0=(0,0),
    D_n=T0+2nP。

signed |n|>=6 で、実際の点 D_n が −B²<x(D_n)<0, y(D_n)<0 を満たすとする。S268の実際のreduced normから

    r=BZ/b>0, Z=|Z_n|, b=b_|n|,
    gcd(Z,b)=1, gcd(b,2ABC)=1, b odd

を取る。この正確な原軌道上では、次が同値である。

1. T_n=b²−Z² が正の整数平方（同値にsigma_n=B²−r²が正の有理平方）。
2. SAME actual b,Z と正しいindex parityを持つ、primitive integer Gaussian F>G>0 と奇数coprime役割 M>N>1 が存在し、MN=b、S269のnorm/quartic、正しいnegative-y POINT一致を全て満たす。

前向きでは役割M,NとGaussian対はcanonicalで一意である。H_n=b²(pq+rs)/D=M⁴ とproper divisor条件は、別の未証明の仮定ではなく、今回の前提から再構成される。

現行残存帯は全て |n|>=12 なので、そこでは旧S289とC174/S290によって四つのGLOBAL正整数S243根/common c、代数的Kummer、およびSAME Qの無限商類も従う。

これはT_nが平方にならないことを証明した結果ではない。数学的差分は、S233/S237の証明を必要な前提だけで再構成し、実際のWard軌道上の正の補平方からcanonicalソースへのsufficiencyを明示したことと、役割1の例外を一様高さで除いたことである。旧norm/valuation/Gaussian/height理論は新しい独立方法として再計上しない。

S270のTRUE FOUR GOOD/actual-critical-H TOPとALL PROPER ordinary beta uncapped、他のhalf/order/原始性HOLD/NEGATIVE/撤回、Bwideのforward coverageは別途保持する。元の軌道条件を持たないR3のrelaxed pointやnorm-onlyデータには適用しない。

## 2. r,p,qは元の倍算点から既に有理である

S240のduplication adapterを用いる。nP=(u,v) とし、2nP のx座標をXとする。Pは旧formal-group証明でnon-torsionなので、n≠0では必要な分母は消えない。

    X=((u²+D²)/(2v))²,
    X−A²=((u²−2A²u−D²)/(2v))²,
    X+C²=((u²+2C²u−D²)/(2v))²。

T0 translationでx(D_n)=−D²/X。従ってr,p,qは全て正の有理数であり、p²=A²+r², q²=C²−r²を満たす。negative-y chamberにより y(D_n)=−rpq。残る条件はs²=B²−r²である。

ここはQの無限商類、S243根、役割分解、Gaussian四次式を仮定していない。actual signed nPであることが重要で、同じ曲線上の任意の点ではduplicationの三平方を流用しない。

T_n=Y²>0と仮定すると、s=BY/b。整数の有理平方根は整数なのでYは正整数。S268よりZ²+Y²=b²はprimitiveなPythagorean tripleで、bは奇数である。

## 3. 共通整数分子を作る

次を定義する。

    R=b*r=BZ, S=b*s=BY, U=b*p, V=b*q。

p²=A²+r²から (bp)²=A²b²+R² は整数の有理平方なので、Uは正整数。同様にVも正整数である。従って

    R²+S²=B²b²,
    U²−R²=A²b²,
    V²+R²=C²b²。

J_int=UV+RS, K_int=UV−RSと置く。正のD²のnorm identityから

    J_int*K_int=(D*b²)²,
    J_int>K_int>0。

任意のp|bについて、gcd(R,b)=1、上の三平方式によりS,U,Vもp-unitである。bは奇数、Dとcoprimeなので、J_int+K_int=2UVはp-unitで、productのvaluationは4v_p(b)。従って正確に

    {v_p(J_int),v_p(K_int)}={4v_p(b),0}。     (195.1)

これはS233の旧algebraを、元の点と補平方だけの前提から再実行した証明である。Q∞、既成のS243根、未確定の役割は使わない。

## 4. Dの全素数での付値固定にも余分な前提はない

S237のformal-depth議論を必要な前提だけで使う。4P=Wとすると

    x(W)=(D²+B⁴)²/(4D²B²)。

ell|D, e=v_ell(D)とするとBはunit。Wのformal depth t0はodd ellでe、ell=2ではe+1。整数係数のformal groupにより全signed multiples jWの深さtはt>=t0である。

odd n=2j+1ではD_n=S*+jW, S*=T0+2P=(-B²,-BD)。S237のexact chord identityから

    v_ell(s²)>=2e (odd ell),
    v2(s²)>=2e+2 (ell2),

かつrはell-unit。globalにsが有理であることを用いてsのdepthはそれぞれe以上/e+1以上になる。

ell|Aではpはunit、q²=A²+s²よりqのdepth>=e。ell|Cではqがunit、p²=C²−s²よりpのdepth>=e。従ってpqとrsの両方のdepth>=e。積(pq+rs)(pq−rs)=D²なので両方のdepthが正確にeとなる。

even n=2jではD_n=T0+jW、x(D_n)=−D²/x(jW)。従ってrのdepth>=2e（ell2では2e+1）。sはunitで、pqのdepthは正確にe、rsはそれより深い。やはりpq±rsのdepthは正確にeとなる。

bがDとcoprimeなので、全てのell|Dについて

    v_ell(J_int)=v_ell(K_int)=v_ell(D)。       (195.2)

A evenの場合v2(A)>=2で上記dyadic formal-depthを満たす。A oddで2∤Dの場合はb,Dが奇数なのでproductからJ_int,K_intも奇数。dyadicな抜けを作らない。

## 5. canonical役割と四乗は自動的に構成される

J_int,K_intは正整数。productと(195.1),(195.2)を全素数で比較すると

    J_int=D*M⁴, K_int=D*N⁴,
    MN=b, gcd(M,N)=1, M>N>=1,
    gcd(MN,2ABC)=1。

M,Nは一意で、bの各prime-powerはJ/Kのちょうど一方に割り当てられる。この段階でH_n=J_int/D=M⁴は正整数四乗。S233だけでDによる可除性を仮定したのではなく、actual orbit depthから(195.2)を証明した上で割っている。

未解決だった可能性はN=1である。これを次の一様boundで除く。positive rsとr²+s²=B²からrs<B²/2（等号はr=s=B/sqrt2で有理性に反する）。w=pqならw²=D²+(rs)²であり、

    D<J=w+rs<C²,
    1<M/N<sqrt(C/A)。                       (195.3)

## 6. 役割N=1を全原始基底で除く一様高さ

C174の有効な旧証明は、元のPのcanonical heightに対するlambdaを全原始基底で与え、

    hat_h(P)>=lambda>0, 432lambda>=c_E,
    c_E=bit_length(R_E), R_E=256D⁸(A²+C²)⁴。

このlambdaはP自身のheightで、2Pにすり替えない。今回、(4,3,5),(12,5,13),(3,4,5)のexact16Pからlambda4を独立に照合した。旧20,856基底証明は有効なdependencyとして再利用し、全再実行しない。

S290/S252のheight規約で |h_x(T)−2hat_h(T)|<=c_E/3。実際のD_nにはhat_h(D_n)=4n²hat_h(P)が成り立つ。またreduced numeratorにより

    h_x(D_n)=2log b+2log max(r,1)<2log b+2log B。

従って

    log b>4n²lambda−c_E/6−log B。

R_E>=256*C^16なので log C<c_E/16、またB<C、A>=1。これらを使うと

    log b−(1/2)log(C/A)
      >4n²lambda−25c_E/96
      >=c_E*(n²/108−25/96)。                 (195.4)

|n|>=6では右辺は少なくとも7c_E/96>0。現行|n|>=12では少なくとも103c_E/96>0。従って、補平方の有無を仮定せず、strict original chamber上では全基底で

    b>sqrt(C/A), つまり A*b²>C。             (195.5)

もしN=1ならM=bで(195.3)からb<sqrt(C/A)となり矛盾する。従って|n|>=6でM>N>1。

新しい具体的な高さの差分は(195.4)-(195.5)とこのproper-role例外排除である。新しいcanonical-height理論や新たな20,856基底計算を主張しない。

## 7. SAME primitive Gaussianとsigned POINTが再構成される

Z²+Y²=b²はprimitiveで、b odd、Z,Y>0。旧S269のindex parityよりeven nではZ even、odd nではZ odd。primitive Pythagorean parametrizationから一意のF>G>0, gcd(F,G)=1, opposite parityがあり、

    b=F²+G²=MN,
    even n: Z=2FG,Y=F²−G²,
    odd n: Z=F²−G²,Y=2FG。

J_int−K_int=2RS=2B²ZY とcanonical四乗から

    4B²FG(F²−G²)=D(M⁴−N⁴)。

これが同じF,G,M,Nの正確なS269 quarticである。元の負yは最初から y(D_n)=−rpq、同じr=BZ/bなので、S269 sourceのPOINT=(-r²,-rpq)はactual signed D_nそのもの。x座標だけの一致ではない。

逆向きは同じpoint/legを持つS269 sourceのnormからT_n=Y²>0なので明らか。従って冒頭の同値が成り立つ。

|n|>=12なら、このactual primitive sourceとPOINT一致に旧S289/C174を適用でき、四つのGLOBAL正整数S243根/common c、Q-Kummer、同じQのinfinite quotientが得られる。従ってrankE(Q)=1の基底では、|n|>=12のstrict original orbitでsigmaが正の有理平方になること自体が不可能、という条件付きcorollaryも得られる。新たなrank計算や新しい基底排除数は主張しない。

## 8. R1-223の訂正は撤回しない

R1-223 corrigendumは「actual sigma-squareと任意に選んだb=MN、abstract4roots」から、その与えられたM,NにS268 quarticを押し付ける推論を禁止している。今回もこの禁止を維持する。

今回作るM,NはJ_int,K_intから一意に決まるcanonical rolesである。任意のfactorizationをcanonicalと呼ばない。結論は、base×signed-indexへ射影したexistential source layerについて、correct actual sigmaが成立すればcanonical witnessが作れるというもの。W4_weakの全labelled tupleがW4_linkedに含まれると主張していない。

同様に、単にbがGaussian normであること、p-adic squareがあること、R3の自由なrational pointがあることだけでは前提を満たさない。negative control (A,B,C)=(3,4,5), b=5,Z=4,Y=3 はprimitiveなnormとsigmaを持つが、p²のnumerator481、q²のnumerator369はどちらも平方でない。actual orbitがないため本adapterの対象外である。

R1-228/C174のH_n四乗検査は正しいnormal formのまま。今回の前提が全て確認された後にこれを別の独立した除外gateとして扱うことはできず、再構成のassertion/実装検証として使う。Gaussian quarticを使ってglobal sigma-squareを矛盾させる研究自体は依然有効だが、二つの独立savingとして数えない。

## 9. 実際の新しいR0 receiver

現行残存帯でGaussian/role/POINT層を狙う主目標を、正確に

    T_n=−W_(n−1)W_(n+1)/D^(2ceil(n²/2))
       =b_n²−Z_n²

がstrict negative-y original orbit上で正の整数平方になれないこと、と表す。これを全原始基底×明示的なsigned-index域で証明すれば、その域のcanonical S269 sourceも排除できる。T_nの全域nonsquareは今回未証明。

S270 TRUE FOUR GOOD/actual-critical-H TOP+ALL PROPER ordinary beta uncapped upperは別の有効な方向として残す。S251/253、order/half、S193 d1 scope、S231/R4 ANY-index HOLD、原始性、全NEGATIVE/撤回を維持する。index bandsはLOW12..154/MID156..196/HIGH>=198、signed odd n1mod32 abs>=7199。nominal indicesを解の生存数と呼ばない。

C194のgeneric C_G→固定W_fg/Hc no-mapはそのまま正しい。今回の原軌道の離散的なnと実際のsquare rootからの再構成は、C_G全曲線に定義された非定数写像を作るものではない。両者を混同しない。R3のrelaxed D_m pointには、元の基底・n・actual scalar/pointを本当に復元するadapterがなお必要。

## 10. 検証・重複・credit

fresh shared head C194を読み、5指定owner foldersのmodifiedTime>2026-10-28T05:30:00Zを全MIMEで検索して0件を観測。全archiveや将来提出がないという意味ではない。owner STATE/MISSION/Sheetsは変更しない。

全INDEX履歴をsigma→quartic/Gaussian、canonical roles、H_n、proper role、single sigma、integralityの仮定・結論で検索し、S233,S237,S240,S268,S269,R1-223訂正,R1-228,C174,S289/S290の原証明を読んだ。旧theoremの完全packetという表題だけで前提を流用せず、証明の各段階でQ∞/四根/Gaussian roleを使っていないことを確認し、必要な部分を本稿で再証明した。新しい独立方法や未検索archive/文献における絶対的新規性は主張しない。

新規stdlib verifierは12 labelled bases×9 indices=108のactual original orbitを独立Fraction群法とactual W recurrenceの両方で照合する。strict negative-y60行で新しいA*b²>Cを正確な整数比較で確認し、全108行でp,qのrationality、同一signed POINT、common b、index parity、M_n=D^K*b、実際のadjacent normを確認した。C174のheight scaleは3基底だけで差分照合。

この有限panelにはglobal sigma-squareの成功例が0なので、canonical reconstructionの成功branchを実物理例で実行したとは主張しない。0件を全域nonsquareの証明にも使わない。canonical四乗の全域結論は(195.1)-(195.2)とinteger UFDの証明、proper-roleは一様height不等式による。旧duplicate scriptや20,856-base scriptの全面再実行はしていない。

## 11. 見方の台帳と次の研究

receiverの等式から、共通整数分子/UFD、formal depths、一様height、actual norm square、global point/descent、真のmass相関を生成し、旧台帳と比較した。生成した見方の分類であり、全ての数学的可能性を尽くしたという意味ではない。

| 候補 | 判定 | 次の扱い |
|---|---|---|
| actual strict T_nのglobal nonsquare | LIVE | Gaussian/role/POINT層と同値な主receiver。 |
| canonical source成立後のH_n四乗・proper roleを独立に落とす | DOMINATED | 本証明で自動成立。assertionとしてのみ保持。 |
| 任意のb分解をcanonical roleとみなす | BLOCKED | R1-223訂正を維持。今回のexistential theoremとは別。 |
| TRUE FOUR TOP+ALL PROPER correlated UPPER | LIVE | 別の保持された物理mask。今回上界なし。 |
| relaxed D_m/auxiliary pointのactual scalar/source復元 | UNTESTED | 元のn/base/pointのadapterを示す必要がある。 |
| generic C_G→固定W/Hc転送 | BLOCKED | C194の全原始基底定理を維持。 |
| finite-prime/finite-boxだけでglobal T_n nonsquareを宣言 | BLOCKED | 旧method ceiling。有限panelを閉鎖に使わない。 |

CYCLE_ROUTE_STATUS=PASS_NEW_GATE_FROM_STRONGER_VIEW
CYCLE_ACTIVE_RECEIVER=actual positive integer square T_n on strict signed original orbit over explicit moving-base/index domains, with remaining full masks retained
CYCLE_LIVE_CANDIDATES=2
CYCLE_UNTESTED_CANDIDATES=1
CYCLE_EXHAUSTIVE_VIEW_AUDIT=true (generated set only)
CYCLE_BLIND_REDISCOVERY=true
CYCLE_SPLIT_TRIGGERED=false
CYCLE_PARKING_AUDIT_COMPLETE=false (receiver全体をparkしない)
CYCLE_NEW_VIEW=premise-reduced canonical role reconstruction plus uniform no-single-role height
CYCLE_NEW_VIEW_SOURCE=INTERNAL_DERIVATION

共有4文書はprependとrevision guard、全旧本文のexact text suffix readbackを実施する。paired COMPLETE後にMISSIONをUTF8/history保存で同じIDへ同期し、raw bytesを読み戻す。外部敵対的監査、BranchB/Stage35閉鎖、E1証明、全source cutは主張しない。

## 原資料

- S233: https://docs.google.com/document/d/1ysl-pqDyr2o5IilzfyFAfdvApP-V_420JW7MTgHCBzw/edit
- S237: https://docs.google.com/document/d/1HjJ9JuFzA6rzZWqZwgbab6jgc68z-Rr9fZQeWpBkSfI/edit
- S240: https://docs.google.com/document/d/14sUCv_TuH0tbRwiFuqbljgzIWv7UNbLEnKrYbbPzvJA/edit
- S268: https://drive.google.com/file/d/1QFsK3SpT-L9xfAiVOeAzV-qhlAoDfw9o/view
- S269: https://drive.google.com/file/d/1OxBV_bGXt76EFfGJ_uRSaYVmZNBjb-aR/view
- R1-223 controlling corrigendum: https://docs.google.com/document/d/1W83hY5jc2xhM2YqVqcSU4dG2OVWtmIGtRbCmQYQVODw/edit
- R1-228: https://docs.google.com/document/d/1WCR3at4AirqmSP54k5oY8WkYulD9YN9lfCjo-quFGig/edit
- C174 controlling proof: https://docs.google.com/document/d/1zHn8L4jcwOhnsAlN4UAK_mZ3ro8RiLHhy0mSHt4Cj_c/edit
- S289: https://drive.google.com/file/d/1FuKZDx_iMrqQ8yx4465e6jPIq81RZFyz/view
- S290: https://drive.google.com/file/d/1obvVmuO1Rl-0dbxYcNPpsynVE9iLVDvE/view
- C194 proof: https://drive.google.com/file/d/1MCyen8Hv9WdJ69fvb6fIwM9EpwURPuzg/view
- C194 COMPLETE: https://drive.google.com/file/d/1hAgtjUB1fsC5YLaCcoBG2AvkJbrQDYLI/view

END_C35_195_PROOF
