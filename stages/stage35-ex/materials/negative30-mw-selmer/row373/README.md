# Stage35EX R3-07 row373 再現資料

Python 3.12 と python-flint 0.9.0 で再現した。ZIPを展開し、まずSHA256SUMSを照合する。次の3本はPythonから直接実行できる。

~~~sh
sha256sum -c SHA256SUMS
python verify_parent_dyadic.py
python verify_row373.py
python verify_global_preflight.py
~~~

親曲線の整数係数は curve_C29.json。verify_row373.py は local_basis.json の50件の固定証人を入力に、点の存在、全ノルム評価、平方類、53次元の小行列式を再計算する。乱数探索は不要。kummer2_membership.json は107単元ビット上の54本の所属条件。verify_global_preflight.py は有理Sturm列、整数判別式、2で極大な整数環の関係式を再生成する。

出力済みJSONと実行記録を同梱。著者厳密再現PASS、独立監査PENDING。全球2-Selmer上界と元signed±30の排除は未証明。
