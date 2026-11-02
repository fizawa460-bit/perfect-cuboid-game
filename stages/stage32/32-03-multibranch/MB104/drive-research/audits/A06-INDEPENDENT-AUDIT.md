MB104-F-AUDIT｜F66｜2026-10-29  
stage32audit / Route F / 2026-10-29 JST

判定  
F66の固定複素モデル内の数学は、明記された「整・横断・τ自由・支持外・シート標識付き混合節点」条件のもとで範囲限定の条件付きPASS。今回の新規数学差分は、同変Koszul列による混合節点評価kernelの同定、cokernel=6、norm像と混合節点保存germの一致である。  
原典F12〜14/C16/H→実担体adapter=HOLD。実source-fixed C・実混合節点標識Σ・実marked conductor/corelessは未入力。実候補排除0、一様m上限なし、MB104 OPEN、公式theorem/receiver/endpoint credit0。一般元・局所模型・toyのPASSは実候補排除としない。

凍結資料  
F66研究正本: https\://docs.google.com/document/d/1dlc5IRspSlomypZmCLzMvNkTjxWVZXgOdJKyN-628\_c/edit  
F66 ZIP: https\://drive.google.com/file/d/10qSBtEjRcBX-21MPGNiCX\_d7w39Cmf69/view  
SHA-256: 4093984e78d817e8dd32724a0054e814f116cf7782f5a81923c559f2e940c218。420126 bytes、19ファイル。  
F65同梱ZIP SHA-256: d52bf5d0adf5b150d3371a98d59a1b8d59901f2cfb46e53c6a1ea3dcefb529ae。  
依存するF65の範囲限定監査: https\://docs.google.com/document/d/1vO2S0DT2DNzkzzDq4zZEcZFMBNngkk-206HAeP-43PQ/edit

独立実行結果  
\- sha256sumでF66外側ZIPの固定SHA256一致PASS。  
\- python3 verify\_f66.py: PASS。  
\- python3 \-O verify\_f66.py: PASS。  
\- python3 verify\_f66.py \--replay-f65: PASS（F65の通常・-O再生を内包）。  
\- python3 negative\_tests.py: PASS（10種類×通常/-Oの20件すべて異常を拒否、元ファイル不変更）。  
検査対象は依存バイトの完全hash、F65内包依存hash、局所A1 chartの関係と自由次数2、同変Koszul符号、toyの有理数行列rank、全m多項式の一致と実候補0 credit0のscope。幾何学的exactness、nodal変形germ、source adapterをコードが形式証明するわけではない。

数学監査（1）：解消上の被覆と符号  
S\_Y上のτの16孤立固定点を吹上げπ:Ŷ→S\_Y、Ŷ/τ=S\_X、f:Ŷ→S\_Xは次数2有限平坦。局所chart b=at, τ(a,t)=(-a,t)から不変環C\[a²,t\]、A1最小解消chart (u,v,w)=(x,xt,xt²), uw=v²、f\*E\_T=2R。K\_Ŷ=π\*K\_SY+ΣR=f\*K\_SX+ΣRを照合し、f\*P=π\*Mを保持。全域をS\_Y→S\_Xの有限エタール写像とはしていない。支持外混合節点近傍のfはエタール。  
交差Ξ=D∩τDがゼロ次元complete intersection、D,τDが整で共通成分を持たないとき、0→O\_Ŷ^-→O\_Ŷ(A)⊕O\_Ŷ(A)→I\_Ξ(2A)→0が正確。α(c)=(sc,-τsc)、β(a,b)=τs a+s b。τ中項作用(a,b)→(τb,τa)に対し、左の定数の作用は-τである。ここを+τと誤るとkernel次元が1ずれる。h0(O\_Ŷ^-)^τ=0かつh1(O\_Ŷ^-)^τ=0（q(Ŷ)=0）。char0で不変部分を取る操作はexact、I\_Ξ=f\*I\_Σ（Σは分岐例外から離れたΞ/τ）なので、大域核空間H0(S\_X,I\_Σ(2mP))とV\_m=H0(S\_Y,mM)はt→τs t+sτtで同型。

数学監査（2）：階数・射影微分  
F65入力 h0\_X(2mP)=672m²-112m+12、h0\_Y(mM)=336m²-112m+18、\|Σ\|=336m²。  
ゆえにev\_Σ:H0\_X(2mP)→H0(Σ,O\_Σ(2mP)) のkernel次元336m²-112m+18、rank=336m²-6、cokernel=6。  
m=1では336×572の評価行列についてkernel242・rank330・cokernel6。m=2なら節点1344・rank1338。同じ数を独立の336節点制約と誤計上しない。  
norm微分dN\_s(t)=τs t+sτtがaffineで単射、射影ではb=sτsに対応するs方向を除いてやはり単射。dim tangent norm=336m²-112m+17。この同型はF65の次元差からの推測だけでなく、実際の横断混合節点に対するKoszul exactnessを要する。

数学監査（3）：局所複素解析germの範囲  
一般条件下でD≠τDは整、同じnormの因子分解はDとτDのみを許すためNのfiberは\[s\]と\[τs\]の2点。τは二点を交換、射影Nはproper、両点でimmersion。従ってnorm像のbにおけるgermは滑らか、dim=336m²-112m+17。  
互いに離れたΣのordinary nodeを近傍で移動しながら保存する各局所条件の一次線形化は、式xy+εhのh(0)評価。330相当（全mで336m²−6）の独立な局所方程式を選ぶと、陰関数定理により滑らかなdim=336m²−112m+17の上位節点保存germを得る。norm像germはそこに含まれ次元が等しく、局所的に一致する。残り6方程式もこのgerm上で消える。これを指定節点以外の特異点の保存や、実Bがnormに属することの十分条件へ拡張しない。  
Stacks Projectのregular sequence→Koszul正確性（Section15.31 https\://stacks.math.columbia.edu/tag/062D）と整合。解析germの等号は本文の有限写像と陰関数定理を使う幾何学的論証であり、toyの計算だけの証明ではない。

数学監査（4）：条件付きnodal種数1会計  
さらにDの自己特異点が全ordinary nodesで、τDを避け、Dの正規化が種数1である仮定下、自己節点δ\_D=336m²+112m、混合節点δ\_mix=336m²、C全節点δ\_C=672m²+112m。  
F65のintrinsic平滑化写像cokernel=224m−17、Cを全\|2mP\|で変形する写像cokernel=224m−11、差は6。短完全列0→C^(224m−17)→C^(224m−11)→C^6→0に整合。  
m=1は207→213→6、全線形系接571→節点784、norm接241→内在節点448。norm内の全節点cokernelは336+207=543。F37の導手降下rank548とは別写像なので加算しない。この会計は種数1特殊Dの存在を証明せず、非nodalなDには適用しない。

監査境界・NEXT  
F66の階数必要条件は実sourceからm、C∈\|2mP\|、真の混合節点の完全なシート標識Σ、横断・例外回避・固定class・norm lift必須性が得られたときのみ使える。仮にm1の実Σでrank331が証明されれば「指定norm liftの不存在」となるが、現時点のrank331は単なる仮定例で実結果ではない。Σ不明の任意336点のrankを実候補排除へ使わない。  
新規候補排除0。F66の6次元依存をnorm余次元330へ加算しない。非普通交差・共通成分・分岐上の交差・D自身の特異点と混合点の重なりは局所intersection scheme版の新監査が必要。  
次は実source-completeなΣでの評価、実marked conductor/corelessと種数1特殊locusへの独立制約。GitHub・STATE・A〜E・公式credit・raw DRIVE-WORK-HANDOFF.jsonは不変更。詳細証拠は本報告、F66研究文書と保存済みZIPを参照。

分類  
SOURCE\_CONDITIONAL\_COMPLEX\_MODEL\_MATH / F66\_SCOPE\_AUDIT\_CONDITIONAL\_PASS / VERIFIED\_NORMAL\_OPTIMIZED\_PRIOR\_REPLAY / NEGATIVE\_20\_PASS / SOURCE\_ADAPTER\_HOLD / ZERO\_CREDIT。  
