stage32audit — F63 範囲限定監査  
2026-10-29 JST / MB104 / Route F

判定  
F63は固定複素商モデル内の数学について条件付きPASS。凍結ZIPの一致と通常・python \-O再生はPASS。原典F12〜14/C16/Hから実担体へのadapterはHOLD。種数1、marked conductor、coreless/no-clumpは未証明。実候補排除0、一様m上限なし、MB104 OPEN、公式credit0。MAIN昇格・merge許可ではない。

凍結入力  
F63原本: https\://docs.google.com/document/d/1avqJ5oAJ6NbDRREilmvgbj25\_2nfv4Qp80PsjbuQfnk/edit  
再現ZIP: https\://drive.google.com/file/d/1oXtiO\_Ix8ByWs8nNIopJoJgEvChuAVyj/view  
SHA256: c84db83eced17f31fa8467c7c0f9a6bbab652ea569e5e94f0ea2bff7b899cd7c  
36ファイル。アーカイブをローカル解凍しハッシュ一致確認。verify\_f63.pyとpython \-O verify\_f63.pyは各PASS。既存F61/F62監査の2026-10-29条件付き境界を継承するが、旧原典の再監査には拡張しない。

局所jetと証人  
H\_diag不変の半次数切断の基底数は15²+2×13²+11²=684。τ-evenは344列、oddは340列。14代表節点にそれぞれ224行の次数8未満の局所jet条件を課す。4本のevenおよび2本のoddの厳密なQ(i)行関係が階数上界220/222を与え、mod97非零minor (55, 2\) から下界一致。核次元124+118=242、even拡張評価minor=89。再生成と厳密関係検査は正常終了。  
二証人の28 Y支持点で8次接線錐、norm側16次接線錐のsquarefree性、軸非接触・相互素性を検算。Xの残り34 A1節点でsとτsの非零評価を照合。非零unit minorと標数0の厳密行関係による持上げは、有限体解をそのまま複素解と誤認しない論証として有効。

4次消去normと整性  
係数関数f=A+BU+CV+DUVに対し、U²=a, V²=bとおく四共役積  
N4(f)=(A²+aB²−b(C²+aD²))²−4a(AB−bCD)²  
を検査。r=0およびR=0の2 sliceで次数56を保持し、norm同士のBézout恒等式1を照合。次数保持の下では正次数の因子が当該sliceで定数に退化できず、二方向を合わせて変数単独の因子も排除できる。従って共通曲線成分なしという推論に矛盾を認めない。  
28例外E\_jにおけるstrict M\_Y=7K−4ΣE\_jの制限はO(8)。F/GがE\_j上で非定数、全系の次元242\>h0(O(8))=9なので像が曲線に退化できない論証を確認。基点は有限。滑らかな基点自由開集合に対するJouanolou型Bertiniと標数0の一般被約性から、一般切断Dの整性を導く。全mはW\_m=im Sym^m Uで像次元2を保ち、pencil積が局所条件の非空開を保証する。ここは数学的演繹でありプログラムによる形式証明ではない。  
τ非不変な整D\_mを一般に選び、qが担体近傍でエタールな範囲では、b=sτsがXへ降下し、B\_m=q(D\_m)は整Cartier、q\*B\_m=D\_m+τD\_m。支持14点でYの8m枝がXの16m枝を8m+8mに均等分割しQ=0。任意の実source-fixed Bについてnorm判定が通ることは意味しない。

半ファイバーと種数会計  
2y²=x⁴+1、g=x²−x+1に対しg²−y²=(x−1)⁴/2。これにより(1,1)と(1,−1)の差が位数2のねじれ点となること、半次数切断tと値比3+2√2の整合を点検。奇数m一律排除は成立しない。  
D\_m²=672m²、K·D\_m=224m、p\_a(D\_m)=336m²+112m+1。種数1に必要なstrict δ(D\_m)=336m²+112m（m=1で448）。X側strictの必要δ=672m²+112m（m=1で784）。D\_m·τD\_m=672m²、混合シート寄与は336m²。14 A1の収縮に伴うδをstrict δへ混ぜない。一般D\_mが種数1という主張ではない。

検証器の限界と改変テスト  
verify\_f63.pyには通常・最適化の両モードで消えない明示例外がある。監査側で偽theorem\_creditと偽genus\_one\_provedの各証明書改変を両モードで拒否することを追加点検（4/4 PASS）。原パッケージには10種類×2モード計20の拒否試験記録があるが、今回はその20件の全独立再実行を完了していない。したがって負検査20件の「独立監査済み」認定はしない。改変検査で数学的なBertiniの仮定まで検証済みとは扱わない。

残る境界  
F63の成果は同時局所条件＋整性＋norm分裂＋Q=0だけによる全m不存在論法が、この固定複素モデルでは成立しないという限定NO-GO。実sourceの正規化種数1、必要strict δ、marked conductor、coreless/no-clumpを同時に満たすかは未評価。F48/F49の実B固定norm、F53循環訂正、原典adapter HOLDを維持。0候補排除、credit0、MB104 OPEN。

次回監査・研究への引継ぎ  
NEXTはF64以降の種数1 locus とδ(D\_m)=336m²+112mの実現可能性、および実marked conductor/corelessへのadapter検査。追加原典なしの同一局所計算の反復だけで排除を主張しない。

監査参照:  
F61/F62範囲限定監査 https\://docs.google.com/document/d/1T87xTQS8YgYpH3GoOYmCBUw3-lHOp6SvU9Vhp6w4FK4/edit  
Bertini原理 https\://stacks.math.columbia.edu/tag/0G4C

分類: SOURCE\_CONDITIONAL\_COMPLEX\_MODEL\_MATH / F63\_SCOPE\_AUDIT\_CONDITIONAL\_PASS / ZERO\_CREDIT  
