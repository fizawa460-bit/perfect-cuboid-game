# row386 再現

Python 3.12、python-flint 0.9.0で検算した。必要な外部Pythonライブラリはpython-flintだけである。

```sh
python -m pip install python-flint==0.9.0
sha256sum -c SHA256SUMS
python verify_row386.py > replay386.json
diff -u local_conics386.json replay386.json
```

検査器は7056個の明示二次ノルムを、2成分の二次体演算と共役の積から再計算する。84個の分岐二次拡大でそれぞれ84本の単元ノルム類が独立であることを検査し、85次元単元平方類上のHilbert行列を認証する。続いて次数84の2進根とFrobenius共役を法π²⁴で計算し、27個の補助二次曲線条件を9変数のF₂二次多項式にする。全512類の判定、δ★+既知8類の256代表の全失敗、7条件による有限被覆、実際の曲線点x=±1・0による対照を確認する。

local_ring.pyは監査済み親row373/381の有限局所環演算を継承し、精度をπ⁹からπ²⁴へ上げたもの。conic_arithmetic.pyはHilbert値と補助二次曲線の係数を組み立てる。Hilbertノルム証人はhilbert_norm_witnesses386.jsonに固定し、検査器が全件検証する。curve_C29.json、units381_exact.json、row375_results.json、four_lift_target384.jsonは親からの固定入力で、検査器内でもSHA256を照合する。

曲線点のKummer像への三類制約と補助conic法の適用限界を扱う証書である。全Jacobian有理類への三類制約、MW階数上界、新しい元signed排除、実際のCassels–Tate値やSelmer4所属の判定を行う証書ではない。q★の値と真Sel4所属はUNDETERMINEDである。

標準局所類体論と曲線点からの補助二次曲線の必要性はPROOF.mdの証明・原典を参照。著者再現PASS、独立数学監査はPENDING。
