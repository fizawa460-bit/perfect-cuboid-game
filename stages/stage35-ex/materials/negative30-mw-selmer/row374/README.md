# Stage35EX R3-07 row374 再現資料

Python 3.12 と python-flint 0.9.0 で再現。ZIPを展開し、SHA256SUMSを照合してから実行する。

~~~sh
sha256sum -c SHA256SUMS
python verify_row374.py
~~~

検証器は6素数の素数証書を整数演算で再計算し、奇数部平方自由、整数判別式、法199とMでのBézout恒等式を検査する。17本の固定単元証人について整数ノルム、2進平方類、障害行列のrank17を検査し、row374_results.jsonを再生成する。探索に使った因数分解環境は不要。

curve_C29.json、row373_local_arithmetic.py、row373_kummer2_membership.jsonはrow373の監査済みデータと局所演算を継承する。今回の成果は大域最大整環、全有限素点偶付値と大域単元の17障害まで。類群の2ねじれ、残りの単元条件、真2-Selmer次元4以下は未認証。独立監査PENDING。
