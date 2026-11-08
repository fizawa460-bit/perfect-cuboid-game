# Stage35EX R3-07 row378 計算証拠

Python 3とpython-flintで再現する。verify_row378.py をこのフォルダで実行すると row378_exact.json と同じJSONを標準出力に生成する。

    python -m pip install python-flint==0.9.0
    python verify_row378.py > replay.json

Windowsで行末形式が変わる場合は、JSONとして読み込んで比較する。curve_factors.json はrow376の親係数で、Artin表は次数、次いで昇べき係数配列で因子を整列している。分裂ビット0、非分裂ビット1。各素数の第1因子が最低位ビット。最大整環、親の非分岐性、各有限体判定の根拠は同日付の証明に記載。
