# row383 再現手順

Python 3.10以降とpython-flint 0.9.0を使用した。展開先で実行する。

```sh
sha256sum -c SHA256SUMS
python verify_spectral383.py --recount-tail 4 > replay_spectral.json
diff -u spectral383.json replay_spectral.json
python verify_galois383.py > replay_galois.json
diff -u galois383.json replay_galois.json
```

`--recount-tail 4` は一次因子の完全再計数を4プロセスで行う。省略時はSHA固定の親の因子表を使い、同じ厳密不等式を検査する。版差でArbの区間表示が異なる場合は検査器の厳密不等式とJSONの有理端点を照合する。

`row382_inputs.py` はrow382検査器の再利用部分を含む親コード。現在の証書はその入力照合、有限体演算、関係の二元消去を使う。4,140本の主イデアル関係の実際の算術支持と親の最大整環は、row381およびrow374の監査を継承する。`fixture383.json` は固定有理数データ。`galois383.json` は群論の証明に使う有限体・判別式の入力照合結果。群論と明示公式を含む証明は `PROOF.md` に記載。
