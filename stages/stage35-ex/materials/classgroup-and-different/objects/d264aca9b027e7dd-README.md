# row393 再現一式

P23-R3-07 LOW / same original signed −30 / K degree105。

```
python verify_row393.py
python rebuild_new393.py
python verify_finite_bound393.py
python crosscheck_finite_bound393.py
```

最初は標準Python、次の二つはpython-flint（検証環境0.9）、最後はmpmathが必要。Python −Oは拒否する。親検証器のassert副作用を継承して成功扱いにしない。

主差分：有限有理重みから全通常イデアル類の代表ノルムB<2^94を無条件認証。新314整元/268独立主関係、12件の(α_P)=P I²、878小基底の個別Cl/2零628/形式残181。181は真の類群階数・上界ではない。

parent392/は76ファイルのSHA固定依存資料。全単元、最大整環、源のMW下界、原始算術等は依存入力。親の不同生成元も維持するが、新しい上界の証明に主不同性は必要ない。

discovery/README.mdに有限候補からの可搬全再生成。rerun/は作業用生成物で証拠ZIPに含めない。

新上界までの全素イデアルを列挙したわけではなく、6768基底のCl/2全尽生成は未証。c_Cl、q★、真Sel4、元−30未判定。AUTHOR_EXACT_REPLAY_PASS / INDEPENDENT_AUDIT_PENDING。新無条件排除0、LOW9絶対16signed、Branch B OPEN。
