# Stage35EX R3-07 row377 計算証拠

Python 3.12とSymPy 1.14.0で整数・有理数の証書を再現する。

    python -m pip install sympy==1.14.0
    python verify_row377.py > replay.json
    diff -u row377_exact.json replay.json

Windowsでは py -3.12 を python の位置に指定できる。改行形式が異なる環境ではJSONとして読み込んで比較できる。

再現対象は、二つの商とEAへの写像、EAの半分点、指定捻りの恒等式、(4096,9)の2-isogeny降下の合同証書、(5,2)の明示点の倍算。階数0証明は2-isogenyの標準公式と合同候補の全列挙を用いる。普遍的ねじれ定理と同一sourceへの接続は同日付の証明書に記載。
