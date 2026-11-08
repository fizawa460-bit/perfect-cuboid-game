# Stage35EX R3-07 row371 evidence

Python 3.12 と python-flint 0.9.0 で再現した。ZIPを展開して次を実行する。

~~~sh
sha256sum -c SHA256SUMS
python verify_row371.py
python verify_dyadic.py
~~~

`verify_row371.py` は `curve_C29.json` から法31²の対数計算、全52桁の照合、行列式20 mod31を再現して `logs_mod31.json` を再生成する。`verify_dyadic.py` は整数上のNewton多角形と残余因子を確認して `dyadic_local.json` を再生成する。実行記録は `REPLAY.log` と `DYADIC_REPLAY.log`。独立監査はPENDING。row370の前提を継承し、今回の結果は元の±30候補に必要な階数の下界を与える。
