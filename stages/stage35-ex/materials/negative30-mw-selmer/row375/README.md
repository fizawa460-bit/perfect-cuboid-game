# Stage35EX R3-07 row375 再現資料

Python 3.12 と python-flint 0.9.0 で再現。ZIPを展開し、SHA256SUMSを照合してから実行する。

~~~sh
sha256sum -c SHA256SUMS
python verify_row375.py
~~~

固定した有理Mumford対の有理数合同式、Hの分解、8単元のノルム・2進平方類・非分岐対角との独立性、実単元符号全射、二組の31進補助チャートと10次小行列式を検算する。親row371の31進演算とrow373の2進演算を同梱。固定証人の探索に使ったPARIは検算に不要。

新規差分は有理5独立類、条件付き階数10、Selmer下界8+c、狭義と通常の類群の一致。c値、上界9、元signed±30排除は未認証。独立監査PENDING。
