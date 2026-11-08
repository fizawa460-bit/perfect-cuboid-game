# row384 再現

Python 3.10以降とpython-flint 0.9.0を使う。展開先で実行する。

```sh
sha256sum -c SHA256SUMS
python verify_average384.py --recount-tail 4 > replay_average.json
diff -u average384.json replay_average.json
python verify_four_lift_target384.py > replay_target.json
diff -u four_lift_target384.json replay_target.json
```

`--recount-tail 4` を省略すると監査済み親表のSHAを照合して使う。省略時もスコア・moment・全連続領域の厳密不等式を検査する。

`verify_average384.py` はrow383の区間検査器を再利用し、未知奇数べきの係数を3非自明指標平均の `-1/3` に変更した。試験関数と認証する領域は固定有理数データ `fixture384.json` にある。`row382_inputs.py` は監査済み親の入力・二元消去・有限体計算の再利用部分。`verify_four_lift_target384.py` は親の単元基底と局所符号を用いて、既知8有理類を補う明示Selmer類を固定する。122個の原多項式の抽出は親row381の索引から行った。

再現のPASSは零点の必要条件と4リフト対象の指定のPASS。無零性・4リフト不能の判定は未完。
