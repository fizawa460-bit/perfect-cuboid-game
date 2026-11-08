# Stage35EX R3-07 row379 計算証拠

Python 3とpython-flintで再現する。

    python -m pip install python-flint==0.9.0
    python verify_row379.py --workers 4 > replay.json

replay.json を row379_exact.json と比較する。Windowsで改行が異なる場合はJSONとして比較する。curve_factors.json と row378_exact.json は独立監査済み親データ。test_functions.json は四つの試験関数を定める固定整数列。探索器やSciPyは再現に不要。GRHは非自明普通類群二次Hecke L関数に対して仮定する。正の区間下界から排除するのは四つの指定分裂商の該当相対次数。
