# Stage35EX R3-07 row363 証拠一式

固定signed ±18のC2、種数17、同じ36次数体Kのみを対象とする。

内部認証結果：通常類数1、c_K=0、同じKの通常S類群も自明。19通常単数＋−1が全単数平方類の基底（有限指標行列式699）。全域2進条件rank11、小行列式−1。fake Selmer≤8、真正2-Selmer≤9、MW階数7〜9。旧6fake像以外の全球候補は明示κ1・κ2の2方向、全MW残余163進対数の次元上界は2。

**全MW残余空間Uの方向・具体的な全MW消滅微分・a0単元は未証明。新MW点0、元source排除0。row363の独立数学監査はPENDING。** 既存row361の限定監査PASSとrow362の従属163飽和性は別の親記録として保存している。

## 再演

Python3.12を使用した。まず配布時のSHA256を確認する。

```bash
python verify_manifest.py
python -m pip install -r requirements.txt
python math/verify_principal_class_one.py
python -O math/verify_principal_class_one.py
python math/verify_global_residual_cover.py --precision=12
python -O math/verify_global_residual_cover.py --precision=12
python math/verify_global_residual_cover.py --precision=10
```

類群は通常・最適化とも24,490検査と5負例、全球被覆は各865検査と8負例。精度10・12で同じ凍結証書を再生する。実行ログは再生成されるので、SHA確認後に作業コピーで再演できる。

任意の別backend照合：

```bash
python -m pip install cypari2==2.2.4
python math/crosscheck_norms_with_pari.py
```

3,204主素イデアル生成元＋19単数、計3,223個の整数ノルム恒等式をPARIでも確認する。この検証にBNFやGRHを使わない。

## 内容

- 主証明Markdown：数学的証明、親成果と今回の差分、成立条件、監査範囲、未解決NEXT。
- `math/principal_prime_generators.json`：3,204個の主素イデアル生成元、ノルム、残余因子。全小素点の列挙ではなく、この明示集合だけで類数1を証明する。
- `math/class_one_certificate.json`：Gaussian明示公式の有理数評価。
- `math/full_unit_basis_definitions.json`：19単数の全係数と20有限素点指標。
- `math/global_residual_cover_certificate.json`：全候補8次元、旧6方向・具体κ1κ2・局所行列・新旧rank上界。
- `math/parents`：使用した凍結親証書。親証書内の監査欄は作成当時の履歴であり、現在の監査状態は`record_updates/sources`に保存した正本から判定する。
- `parent_evidence`：旧row359とrow361の原証拠ZIP。旧row361の163進対数コードを再実装せず、認証済み入力として利用した。
- `exploratory`：今回の有限探索コードと範囲・結果。有限探索をMW完全性の証明に使用しない。
- `record_updates`：R3担当欄・経緯363、R5、R0 ACTIVEの差分、応答、保存後再読の照合。古いrow361・362や他ルート・正式C35-200を変更しない。

主証明はBNFの暫定類数、単数指数1、未知平方類のゼロ扱い、未構成の163進MW方向を前提にしない。主素イデアルの整数恒等式、単数の平方類完全性、既存の全有限偶付値還元を用いる。
