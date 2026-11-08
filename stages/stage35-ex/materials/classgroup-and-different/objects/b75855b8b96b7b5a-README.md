# row392 再現一式

P23-R3-07 LOW / same original signed −30 / K degree105。

```
python verify_row392.py
python verify_different392.py
python rebuild_new392.py
python rebuild_different392.py
python verify_generation392.py
```

最初の二つは標準Python、後三つはpython-flintが必要（検証環境0.9）。発見スクリプトにはNumPyも必要。親の最大整環・全単元・Selmer/尾部表はparent391/以下のSHA固定資料を継承する。

主結果：新594整元・535独立主関係、21件の(α_P)=P I²、878基底の個別零616・形式193。さらに不同主生成元δ=G'(ρ)/(ρ−1)^102と全トレース双対の整数行列式1証書。193は真の類群階数/上界ではない。

new_relations392.json / factorizations392.json / relation_certificate392.json / unit_kernel392.json は数値関係群Γ392の証書。不同δはdifferent392.jsonの別証書で、数値行列の594元数に混ぜない。δを追加してもV/H_nr交差は変わらないことをdifferent_extension392.jsonで認証する。

sample5483.json は5素点の主関係。prime_power_samples392.json はP827³の2元。
generation_result392.json は既知Minkowski有限上界と親障壁の現行資料への継承であり、小基底の全尽認証ではない。

discovery/README.md に発見と全再生成パイプライン。有限探索であり完全列挙ではない。

AUTHOR_EXACT_REPLAY_PASS / INDEPENDENT_AUDIT_PENDING。新規無条件指数排除0、LOW9絶対16signed、Branch B OPEN。
