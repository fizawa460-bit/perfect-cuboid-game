# Stage37 — 振り返りと有望ルート検索

KEY: ROUTE-SEARCH-220-R1
TYPE: strategy/literature preflight; same-assistant review, not independent proof audit
MATHEMATICAL_LATEST: M3-T11-220
DECISION: HOLD automatic219/220 extensions. Prioritize a bounded feasibility/refutation test of215 off-value squareclass collisions; do not approve a generic large-sieve research chain.
GATE: OPEN; GLOBAL_CREDIT:0; independent186–220 audit NOT RUN;162–185 scope unchanged.

## 1. 判断

研究結果の蓄積はある。しかし固定条件での有限多重度と、その条件が動く集合全体の節約は別である。最近の216–218は実際の部分領域のcountを得たが、219はexact adapter、220のcounted cellsは204 small-edgeのsubsetであり、既存large-edge残差を追加処理していない。219/220の自動延長HOLDは維持する。

今回の検索では、そのまま採用して全残差を閉じる外部定理は確認できなかった。「有望」は成功確率の保証ではなく、次の有限な検討で採否を判定しやすい、という優先順位である。最優先は215の異値・同平方類collisionについて、既知のequal-value部分を除いた後に使える非循環な上界、またはその上界を否定する実raw familyを探すこと。新しいcount mechanismをまだ得たわけではない。

## 2. 振り返り：成果と残差

| 系統 | 保持する成果 | 残る障害／重複 |
|---|---|---|
|171/174/183|small Sigma、small D_min、fixed c_uのB^o fibers|moving supportは未処理。fixed q_minはB^oと扱えない|
|194–198|pair-phase/Phi/Kummerの正確な結合|同じ曲線・同じheightの再記述だけで新密度は生じない|
|200–206|small W、small physical/reduced edge、space-gap sectors|大labelのjoint occupancy。201/202 scale cancellation保持|
|209–215|endpoint-safe raw graph、正確なmissing-face selector、fixed integer MのB^o fiber|固定face完成和/L1完成、4bn再因数分解は既にblocked。同平方類内の異値collisionが未処理|
|216|tau_Q-heavy、small shared-gcd joint sector|large tau_Sはc_uに線形で入りfresh-S interiorが残る|
|217|row(B) cubefull divisor tail|closing threshold外のrow(C)/fresh-S|
|218|hidden tau_C radical-height tail|T>sqrt(B/L)の改善窓。fresh-Fには同じradical gainなし|
|219/220|元traceのsquare-gcd/cofactor productとedge lower budgets|n,b_phi,K_i,m_iが全て動く。220 transfersは204に包含|

これは検索対象とquantitative scopeのinventoryであり、全カードの証明監査や全残差のexhaustive cover証明ではない。単一のtailを処理してもK>1 low-median、large-W/unshared conductor等の別OPENを自動処理しない。

### Threshold compatibility

benchmark B^(1/3)に対して固定margin epsilon>0を置く。Z=B^z等、sectorの合法な上界指数が1/3-epsilon以下ならそのsectorを支払える。unionは加算し、包含sectorを別gainとして掛けない。

* 171/174/183/204/205のZ B^o sector: z<=1/3-epsilon。
*216 c_u<=Z,tau_Q>=T: z-2t<=1/3-epsilon。HQ>=Aを加えるとz-a-2t。
*216 c_u<=Z,tau_S<=G,DS>=L: min((z+g)/2,g+1-l)<=1/3-epsilon。
*217 PB>=Y: z-2y/3<=1/3-epsilon。
*218 tau_C>=T,A=q_phase*tau_B*tau_F>=L: z+min(0,(1-l)/2-t)<=1/3-epsilon。
*220 small cofactor/phase windowsは204 sectorへの転送であり、large-edge residualの新countとして加算しない。

STRATEGY-REVIEW-220の形式的balanced fresh-S予算（H=q_phase=tau_Q=tau_B=tau_C=1、R=c_u=DS=tau_F~B、m_i~B^(1/3)、e_min~B）はこの閾値群で自動除去されない。これは実integer endpoint witnessでも、route不可能の証明でもない。既存恒等式だけから閾値coverが閉じると主張できない、という限定的結論である。

## 3. 一次文献と既往の検索結果

### 曲面を上から見る方法

Stoll–Testa, [Curves on the surface of cuboids, arXiv:1009.0388v3](https://arxiv.org/html/1009.0388v3), accepted version last revised2026-09-24。§1/§7を確認。四quadricsのP6曲面、48nodes、Picard構造、次数6以下の曲線の分類が得られている。曲線の分類は全有理点がその曲線集合に入るという定理ではない。

Stage37へのheight adapterは直接的：a_i=e_i,b_i=対応するface diagonal,c=R。primitive physical tupleのprojective heightはmax(|a_i|,|b_i|,|c|)=R。全辺が正ならface diagonalも正でRより小さい。primitive規約で共通scaleを除く。符号・辺の並べ替えは有限個。原方程式のJacobianでは最初の三行がそれぞれ非零b_i座標を持つため独立で、第4行も独立となり、positive locusはsmoothである。

Source Corollary7.4/§1の既知曲線集合を受け入れると、次数6以下のcurve上にpositive rational endpointはない：conicsはa_i=0又はc=0、elliptic curvesはb_i=0、a_j=±a_k又はa_j=±icのhyperplanesにある。前二者はpositivityに反する。a_j=±a_kなら残りface equationがb_l^2=2a_j^2となり非零有理数では不可能。a_j=±icも有理実数の非零座標では不可能。例外divisorはnodes上でpositive locusと交わらない。

このsource-dependent低次数filterは有用な全体像だが、孤立的に残る有理点や次数8以上を数えない。分類sourceのCAS計算は今回独立再検証していない。一般typeや高genusだけで必要countを得たと扱わない。

Salberger, [Counting rational points on projective varieties, PLMS2023, DOI10.1112/plms.12508](https://research.chalmers.se/publication/535246/file/535246_Fulltext.pdf), Theorems0.8–0.9を確認。d=16への一般surface curve-cover estimateはcurve数B^(3/8+o(1))、cover外B^(3/4+o(1))。既存B^(1/2+o(1)) hostより弱く、低次数filterを足すだけでは1/3未満にならない。P3/P4 smooth theoremを48nodesのP6曲面へ無条件転用しない。高degree embeddingに変更してもheightの冪変化を同時に支払う。

新しい論文タイトル／versionが見つかったことを新しい数学機構と同一視しない。Driveのtesta-stoll-source-noteは2025-02-24版を既に使用し、Stage35はQ-defined rank3 genus5 fibrationを正確にcovered済み。28 geometric fibrations全てをQ-definedと扱えない。今回のv3再確認は既往を再開させる理由にはならない。

### 固定fiber・有限branchへの下降

Dujella, [Uniform bounds … certain elliptic curves, arXiv:2312.03655v1](https://arxiv.org/html/2312.03655v1), Theorem1.1：固定number fieldでprime-order torsionを持つelliptic curveについて、canonical-height countはB^(C/log log B)、B>=exp(max(h(E),e))。既存polynomial-height adapterと適切な大きいB冪を使うfixed-fiber方針に対応する。moving labelsの数には上界を与えない。既存036/183等の証明を再監査したとは主張しない。

Stage34 S34-W01/W02/W03/WF01には、finite exhaustive squareclass descent、full MW congruence exclusion、receiver-restricted intersectionという実際に閉じた手法がある。ただしStage34の七fiber closureは全parameter familyへ転用できない。Stage35 provisional harvestはdynamic reservoirが残ればfinite squareclass enumerationを認めない。fresh-Sのm_i/K_i/n/b_phiが動いたまま同方法へ投げることは不採用。新しいfinite support theoremが出た場合のみ再評価する。

Stage14 arsenal AR-009等のdeterminant/root-line、AR-020/025–027の量化・measure制約、INDEXのcross-gcd density negatives、q13旧literature near-missも確認。指数zeroのorientation節約、ambient lattice density、平均定理をevery physical cellへ転用する方法は採用しない。固定prime overlap sieveの順序付きlimitsも固定power savingとは別である。

## 4. 優先順位

| 候補 | 未処理領域へ効く条件 | 判定 |
|---|---|---|
|215異値・同平方類collision|actual raw X*上で全moving dilation費用を支払い独立off-value上界を得る、又は反証familyを作る|最優先のbounded mechanism test。count攻撃のGOは未承認|
|219元phase joint factor receiver|finite shared-prime support又は新joint occupancy theoremを証明|第二候補。恒等式追加だけのchainはHOLD|
|K>1 content/median tail|fixed-q費用、moving median、原endpoint masksを全て支払う|別残差として継続候補。K1 chain自動再開なし|
|global曲面＋determinant|既存1/2 hostを実際に改善するspecialized count theorem|現確認文献は不足。補助filterとして保持|
|高genus fibration/MW総当たり|moving familyをfinite exhaustive枝へ落とす新定理|既往の再実行は非推奨。有限例の成功だけで再開しない|

## 5. 次の作業を具体化：off-value collisionの採否テスト

215のX*(B,C)をそのまま使用する。canonical physical raw edges、R<=B、c_chart>C、M_2R等の既存masksを保存し、endpoint条件M squareを母集団定義へ追加しない。c_chartとintrinsic c_uを混同しない。

M_x=R^2-a^2=b^2+c^2、nu(m)=#{x:M_x=m}、mu(kappa)=sum_y nu(kappa*y^2)。

E_sq=sum_kappa mu(kappa)^2 = E_equal + E_off,
E_equal=sum_m nu(m)^2 <= |X*| B^o <= B^(1/2+o(1)),
E_off=sum_{sf(m)=sf(n),m!=n} nu(m)nu(n).

215よりmu(1)=このX*内のendpoint tail。従って independently proved E_off<=B^(1-2gamma-eta+o(1))なら、0<eta<1/2-2gammaの窓でtail<=B^(1/2-gamma-eta/2+o(1))。gamma=1/6ではoff-value targetはB^(2/3-eta)、tailはB^(1/3-eta/2)。これは条件付きsufficiency計算であり、その上界を今回証明したわけではない。X*外の別OPENへのcreditはない。

検討対象はm=kappa*y1^2,n=kappa*y2^2,y1!=y2となるactual raw pair。共通squarefree kappa、coprimeに縮約したy1/y2、各raw側のcontent/Euclid liftを固定した際の独立なdivisor/incidence estimateを探し、dyadic boxesの全外和を明示する。fixed M boundをfixed kappa boundへ置き換えることは禁止。

最初にrich-squareclass反証を探す：実primitive raw familyを構成し、全heightとX* masks込みでE_offの下界が上のtargetを超えるなら、そのenergy routeは当該閾値で不採用。形式的label tupleやfinite255例のuniquenessでは反証にも証明にもならない。κ=1を除いたenergyだけではendpoint tailを抑えられない。

採用条件：既存215と異なる具体的pair estimate＋moving-cost和の閉鎖、又は合法な反証family。満たさなければNO_GOとして短く記録し、このrouteを恒等式生成chainにしない。終わらない一般large-sieve探索は行わない。generic coefficient energyを前提にするのは循環だが、raw equationsから直接energy上界を証明する行為そのものは循環ではない。

## 6. Drive-only handoff

MAIN/INDEX/short LEDGERへ本KEYと判定を同期する。数学latest220、次math番号221は予約したまま。次はOFF_VALUE_SQUARECLASS_COLLISION_FEASIBILITY_TESTであり、新しい研究成果が出る前にM3-T11-221のPROVEDカードを作らない。219/220自動延長HOLD、TI parked、120 retracted、147–149 frozen、audit scopeを維持。

先にMAIN、本report、INDEX215/220とstrategy220を読む。次に215本文と必要な212/214人口契約だけを読む。全履歴を最初から読み直さない。今回の結果はstrategy/source applicability/conditional targetであり、新global counting theorem・perfect cuboid結論・独立audit PASSではない。

Drive sources: strategy220=1x-LPlwMt4shqeN7Md_Q6PhygnDiWtV7r;215=1VaPpB1NJkRXuFYAgkhtYBiD7BqOnGS7on9IUpkjBBxg;Stage14 arsenal=1c2jysSaidmMV-Hryc6_rXe0qD2A4xEOi;Stage34 promotion=15ATioKjIPAM0smBoy_T7HoIozQCfLail;Stage35 promotion=1_N64I61rGEPHsK6cfM4T3m0JT8kGwk4V;Testa–Stoll old source note=1n1Pw8yaoNVXAk2r8AGcu9u2uyVLyq0PG。検索はtargeted、global Drive全corpusのexhaustive theorem scanではない。
