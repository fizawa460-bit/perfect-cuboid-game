# stage32audit — F35前提確認＋F57〜F60

2026-10-28 JST / MB104 / Route F

# 判定

固定商モデル内の数学は条件付きPASS。直接依存証拠の修復版はPASS。原典から実担体への全対応はHOLD。実候補排除0、一様m上限なし、MB104 OPEN、公式credit0。

# 対象と境界

F35のC8積商、Hと残余τ、支持マスク適用の前提、F57〜F60の式と演繹・検証器を対象とした。元ノートのIDと正規化exportのSHA256を凍結した。Git HEADへのMAIN監査、F36〜56の全監査、F12〜14/C16全原典、実B/Eやmarked conductorの認証は含めない。

# F35

保持H商原文はblob d2e3056137360a9e15ae7c820088d2977a5eb137と一致。T'=h\_v、TT'R=h\_uを照合した。無限遠を含めh\_u,h\_v,Tの固定点は各8、他4元は0。積の対角G商は16+16+16の48 A1、qの非エタール像はT型16点のみ。固定群の軌道は別実装で全列挙した。実担体のT型回避にはsupport maskの網羅性と実対象との同定がなお必要である。

# F57・F58

積被覆の射影公式から、正規化E上のσ\_z=r\_z²、σ\_w=r\_w²は各次数112m、t=r⁴は224m。14点各16m枝という前提のもとで、四つの有効因子包含・残余112m、対角残余16m(14−n\_ε)を確認した。

48点生成と箱の二次方程式、対象16節点のBZ1〜5と分母を厳密照合。Q0(h\_v型7点)のσ\_w=2、Q1(h\_u型7点)のσ\_z=2iは各112mファイバーを飽和する。対角符号は+7/−7。P25/P27はU、P33/P35はVを加えて初めて分離できる。実枝のsheetや導手対は未評価。

# F59・F60

二つのreduced half-fiberは楕円曲線。各制限因子は七点各8m、線束次数56mとなる。点差の4捩れ、f²−((x⁴+1)/2)g²=(x−1)^8/16、除外点の非零値−131072、二交点の値比17+12√2を確認した。Abel・値接合だけでは排除できない。

横断二曲線の接合は値の一致で足り、異なる接方向の微分を等置しない。積被覆の両脚の次数112m−4\>8、曲線双対性・Künneth・G平均化から、全mの大域延長全射が従う。厚みk\_z,k\_w≤28m−3は既に両立するjetに対する十分範囲である。

群のtraceによる別計算でh⁰(X,L)=1568m²−112m+8、核次元1568m²−224m+10、制限先112m−2を確認した。m=1は1464→110、核1354。110項をQ\[t\]/(t⁴+1)で読み直し、二制限・不変性・重み・局所混合項を検算した。元のQ(√2,i)実装はimportしていない。具体延長のP0被覆重複度は2で、必要な16枝に達しない。

# 検証器の不備と修復

歴史node検証器はSATURATION\_CERTに旧blob 1f51cf157b3de6db393049af41fda0843e0f2068を要求するが、指定commitの実体はfcdfeaddbe0da190c2210ad271d26f611956f32a。7個の直接依存を配置し、原版のFAILを再現した。

旧blobを回収して比較すると、新版はevidence欄を追加しただけで、旧版の全数学データ・source locksは同一だった。意味同一性adapterを明示して参照を更新した。

さらにlockだけの修正では、証明書のtriplesを999に変えても旧検証器はPASSした。元証明書blobを固定baselineとする全項目比較を加え、座標・式・過大status・欄欠損・証明書欠損の5負検査を全拒否した。F60の5負検査も元版と独立版で全拒否。入力は不変。

修復検証器blob: 1eabd21ac95ae9d573d2c80bbd4fda3f9d3b2e97

修復証明書blob: 442ec43261ae88a91189025a2d15d05a85403c97

修復版は証拠パッケージへ保存。GitHub原版は未変更。直接依存boundaryのPASSを、上流原典の全数学や実担体adapterのPASSとは扱わない。

# 残る監査と研究

監査の残りはF12〜14/C16/Hから000707の14支持・各16m枝・同じ正規化E・e=2/K=Hへの対応。古いSATURATION\_CERT lockは今回の修復版で解消し、数学的差異として反復しない。GitHubへの正式同期は未実施。

研究の残りは、固定制限を保つ核での16m異方向枝jet、既約性・種数1、norm分裂、marked conductor、coreless/no-clump。実B/EがないためNOT\_EVALUATED。F59旧NEXTの接方向微分一致はF60で更新済み。単なるAbel存在・値接合・延長存在を候補排除に数えない。

# 再現資料と参照

詳細: STAGE32AUDIT-F35-F57-F60-20261028.md

検算: python3 verify\_stage32audit\_f35\_f57\_f60.py（Python標準ライブラリのみ）

凍結: STAGE32AUDIT-FROZEN-SOURCES.json

標準定理: https\://stacks.math.columbia.edu/tag/0BEC 、https\://stacks.math.columbia.edu/tag/0BS2 、https\://stacks.math.columbia.edu/tag/0E39

台帳: https\://docs.google.com/document/d/10QAZSl5Qjic\_gnsGzpRtNaD1TmG7JNZlau7gzQTu3vs/edit

台帳のF監査状態・残余・NEXTのみ更新。A〜E、STATE、GitHub、公式credit不変更。

