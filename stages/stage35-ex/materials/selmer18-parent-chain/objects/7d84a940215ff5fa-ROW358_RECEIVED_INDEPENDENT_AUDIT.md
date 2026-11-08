# Stage35EX 独立数学監査：R3-07 row358

実施日：2026-11-05（日本時間）

## 判定

**PASS_SCOPED — 提出された新しい従属大域上界の限定監査合格。**

対象はP23-R3-LOW中の固定signed ±18、種数17の曲線 C₂:y²=h₂(x)、deg(h₂)=36 のみ。前提として既存 row353/355 の有限bad局所像完全生成、row356 の全球単数4証人、row351/352 の真正Selmer→fake像核次元≤1、row344/345 の整環/判別式を、それぞれ既存の成立範囲で継承した。本監査はそれらの旧成果について再度の全証明を宣言しない。

成立する限定結論：

- 通常類数 h_K=|Cl(O_K)|≤15、c_K=dim_F₂ Cl(O_K)[2]≤3 （c_S とは異なる）。
- 全fake Selmer像は、全有限素点偶付値の E の K*/(K*²Q*) への像 Ebar に入り、dim Ebar=19+c_K。
- 既存norm/実条件2本および2進条件の既存単数4証人により dim Sel_fake≤13+c_K≤16。
- 真正2-Selmerの核次元≤1を加えると dim Sel^(2)(J₂/Q)≤14+c_K≤17、7≤rank J₂(Q)≤17。

未証：真正≤16、rank<g=17、c_Kおよびc_Sの正確値、全MWに対する163進Colemanと積分的a₀単元、固定±18原source排除、LOW全域排除、Branch B閉鎖。

## 証拠と独立計算

対象証拠ZIP：STAGE35EX_R3_07_FINITE_EVEN_TRUE_SELMER17_EVIDENCE_20261104.zip

- ZIP SHA-256：5234e60bf2f3ca2865d56279b2a6f472d64bf5cfd582da37e52f5bdae9f3bf79
- SHA256SUMS.jsonで42/42ファイル整合。
- 通常実行・python -O：それぞれ298 checks、8 negative controls PASS。証明書一致。
- 本監査で別計算した高精度参考値：Δ=2.4617633432406766347…、E=39.1780662674591055728…、16Δ−E≈0.21014722439>0。高精度浮動小数は確認専用、厳密認証は提出物の有理数区間 Δ>49/20 と E<196/5 による。
- 4×4障害minorの整数行列式は独立に +1 と計算。

## 数学審査

1. **局所単数→全球付値貼合せ。** 2および5個の奇bad素数で完全fake像が単数代表を持つことを証明書・再演で照合。その他の奇素数は既知の良還元・不分岐像定理を適用。任意のfake Selmer代表αについて、各pの全𝔭|pで v_𝔭(α)≡δ_p e_𝔭 (mod2)。全有理素数pで少なくとも一つのe_𝔭が奇数だからδ_pが非零となるpは有限個。q=∏p^δ_p を掛けて全有限付値を偶数化できる。これは素イデアルの主イデアル性を仮定しない。

2. **通常理想平方完全列。** Eの（α）=𝔞²への対応から 0→O_K*/O_K*²→E→Cl(O_K)[2]→0。signature(4,16)より単数平方類次元20。E∩image(Q*)は±有理平方のみ（各p上に奇数e_𝔭がある）、Kに実埋め込みがあるため−1はKで非平方。従ってdim Ebar=20+c_K−1=19+c_K。

3. **通常Hilbert類体によるh_K≤15。** 通常Hilbert類体H/Kは有限素点および実無限素点で不分岐、[H:K]=h_K、signature(H)=(4h_K,16h_K)、D_H=D_K^{h_K}。S素点の完全分裂は仮定しない。試験関数g(z)=3(sin z−z cos z)/z³は密度(3/4)(1−t²)1_{|t|≤1}の特性関数、f(x)=g(x/√27)²は非負かつFourier変換非負。Gaussian正則化f_η=e^{−ηx²}fに対し、Φ_η(s)=∫_{R} f_η(x)e^{(s−1/2)x}/cosh(x/2) dxは閉帯0≤Re s≤1で有界・正則。両境界のReΦ_ηはf_ηの非負Fourier変換に一致し、調和関数の最小原理で帯内も非負。零点を批判線上と仮定しない。素点項も非負で、明示公式からh_K Δ_K≤E_f。1−f≤x²/135、∫x²/sinh x=7ζ(3)/2、∫x²/(2cosh²(x/2))=π²/3によりΔ_K>49/20、E_f<196/5。h_K≥16ならh_KΔ_K>16×49/20=196/5>E_fと矛盾し、h_K≤15。計算用有理数区間と解析的理論の適用は分離して確認した。

4. **全球6制約の再利用と二重計上防止。** norm符号と実埋め込みpair条件の2本は既存単数の評価で独立。row356の全球単数4証人はこの新しいEbar全域に入り、前2本の核内で2進障害minor行列式+1なので追加rank4。したがって候補次元は19+c_K−2−4=13+c_K。真正Selmer→fakeの既存全球cohomology橋の核≤1を一度だけ加え、真正≤14+c_K≤17。fake≤16を真正≤16に取り違えない。

## 新規性・既出除外

新数学として認める差分は、同じ36次数体について**局所単数代表から全有限偶付値への大域還元を実装し、既存制約と合わせて真正Selmer上界17を得たこと**のみ。通常類数の次数16除外はrow357のTable4補助検算に既出であり、今回の表非依存の明示証書化を別の独立新定理として数えない。Tartar/Weil/類体法、row353/355の局所像、row356の4証人、row357のS類数13も再creditしない。

## 現行NEXT／引継ぎ

- **指定研究ルート：R3-07（P23-LOW）継続。** ユーザー固定のP23分担を変更しない。R2-01はMID/HIGH担当、代替先として自動切替しない。
- 証明する具体的OPEN：残余全域W=Ebar∩（norm/実条件）∩ker λ₂に**さらに1本の独立な制約**を証明するか、通常c_K≤2を認証して真正Selmer≤16へ。既存12単数部分群の同じ条件を新たなrankとして数えず、全域の未知単数・理想平方類方向を適切に扱う。
- 旧必須NEXT「S付値14方向を構成して追加15本の制約を探す」はrow358による代替上界から現行必須として失効。既存局所像・既存4証人・旧類群上界の再演を新成果にしない。
- 真正≤16または同等の十分な全MW情報が得られた後、163進Colemanの全MW消滅微分、積分的a₀単元、元の同一sourceに対応する非零円盤の排除を検討する。rank≤16だけでsource排除を認めない。
- signed ±18の物理source排除0、LOW全残余OPEN、Branch B OPEN、R0正式C35-200不変、S231正式監査HOLD、B_wide/E1は別問題。

監査種別：新提出に対する限定独立数学監査。コンピュータ証明支援系による全命題形式化を意味せず、旧親定理の再監査完了も意味しない。

## 原典

- 主証明：https://drive.google.com/file/d/1iprQvIDXgodniosJeFohMm-PcKXZl17p/view?usp=drivesdk
- 証拠ZIP：https://drive.google.com/file/d/10lKbDZO0HYIgP245Aq37G2NV59vw8qSz/view?usp=drivesdk
- R0：https://docs.google.com/document/d/1UKVlpL0CmAEAIpRN_eE63JllyN1RjqbBaGIG2o4UH4Q/edit
- R3索引：https://docs.google.com/spreadsheets/d/17BQc6iakGQ7tdxMAVORnOPGa6KjH0uiaiAbbVMO2kRs/edit
- P0/P2監査記録：https://docs.google.com/document/d/14TkdbXFBBtJmaJhFeSeEfOhx2G-DsTJTtoj9GSQKdHo/edit
