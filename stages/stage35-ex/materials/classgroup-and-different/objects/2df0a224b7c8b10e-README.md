# row391 再現一式

対象：P23-R3-07 LOW / same original signed −30 / K degree105。

主結果と限界はPROOF.md、全帯一律非負法の解析的補題はSTRIP_POSITIVITY.md。

```
python verify_row391.py
python rebuild_new391.py
python verify_strip391.py
```

verify_row391.pyは標準Python、後二つはpython-flint (検証環境0.9)が必要。親390の選択済み算術資料はparent390/へSHA固定し、旧原始算術をここで全再生成したとはしない。

new_relations391.json：169個の整数元。norm_sign*h(rho)/2^denominator_exponentで正ノルム化。
relation_certificate391.json：12件の(α)=P I²、139新独立関係、454整数核、零類・残222形式基底。
unit_kernel391.json：単元局所rank55、399平方指数関係。
sample881.json：Norm27682624301の主イデアル分解。
fractional_sample391.json：b=a/67の真の奇分母関係。
strip_barrier391.json：全関数包絡を紙面証明に依存する厳密数値上界。

discovery/は発見の全有限チェックポイントで、完全列挙証明ではない。浮動小数点の候補は全て整数算術で再認証。

AUTHOR_EXACT_REPLAY_PASS / INDEPENDENT_AUDIT_PENDING。c_Clとq★は未判定。新規無条件指数排除0。LOW9絶対16signed、Branch B OPEN。
