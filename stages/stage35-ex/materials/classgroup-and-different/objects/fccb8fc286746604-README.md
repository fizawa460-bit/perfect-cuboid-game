# row385 再現

Python 3.10以降だけで有限証書を再現できる。

```sh
sha256sum -c SHA256SUMS
python verify_ct_reduction385.py > replay_ct.json
diff -u ct_reduction385.json replay_ct.json
```

検査器は、監査済み親の9単元Selmer基底と8有理類の座標、固定δ★、36変数の交代形式の制約、105次元根置換加群のGalois同変射影を照合する。Cassels–Tateの核・交代性と大域コホモロジーの議論は `PROOF.md` の原典と証明を使う。Hilbert記号の実際の数値から類群汎関数を計算したものではない。

`class_group_functional_value` と `delta_Sel4_membership` は `UNDETERMINED`。大域H1リフトの存在は証明したが、Selmer4条件の同時充足は未判定。
