# Stage35EX R3-07 row376 計算証拠

Python 3.12とpython-flint 0.9.0で著者の計算証拠を再現する。

    python -m pip install python-flint==0.9.0
    python verify_row376.py > replay.json
    diff -u row376_exact.json replay.json

Windows PowerShellでは最後の照合に Get-Content replay.json と Get-Content row376_exact.json を Compare-Object に渡せる。

- curve_factors.json はrow370の六因子と \(A_\star,B_\star\) の整数係数を昇べき順に収録。
- verify_row376.py は整数Ward漸化式、15終結式、2進の係数合同、根体の単元恒等式、実根の符号、Descartes変換、Ward符号、合同条件、素イデアル数を検算。
- row376_exact.json は厳密な有理端点、符号集計、指定した各奇素数の全生存傾きと剰余次数を収録。
- SHA256SUMS は以上のファイルとREADMEのチェックサム。

数学的な依存関係と類体論の適用は、同日付のrow376証明に記録した。親のrow370の六平方、row373の2進分解、row374の大域整数環と奇素点偶付値、row375の独立認証済み単元符号全射を入力とする。
