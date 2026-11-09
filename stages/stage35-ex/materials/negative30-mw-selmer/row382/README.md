# row382 再現手順

Python 3.10以降、python-flint 0.9.0、SymPy 1.14.0、C++17を使用した。以下は展開先で実行する。

```sh
sha256sum -c SHA256SUMS
python verify_zero_window.py --recount-tail 4 > replay_zero.json
diff -u zero_window382.json replay_zero.json
python verify_rational_inputs.py > replay_inputs.txt
diff -u rational_inputs382.txt replay_inputs.txt
python verify_chain_expressions.py > replay_scalar.json
diff -u rank31_expressions382.json replay_scalar.json
g++ -std=c++17 -O2 -o verify_rank_tape verify_rank_tape.cpp
./verify_rank_tape rank31_trace382.txt replay_inputs.txt > replay_rank.json
diff -u rank31_tape_check.json replay_rank.json
python - <<'PY'
import json
from pathlib import Path
old = json.loads(Path("rank31_exact.json").read_text())
new = json.loads(Path("replay_rank.json").read_text())
assert old["first_log_coordinates"] == new["log_coordinates"]
assert old["augmented_minor_det_mod31"] == new["determinant_mod31"] == 6
PY
```

Arbの版によって区間の文字列表現が異なる場合は、検査器の厳密な不等式とJSONの有理閾値を確認する。尾部を再計数しない通常実行でも同じ区間証書を得る。これはSHAで固定したrow379の独立尾部表を使う。関係表 mod2_supports382.json はrow381独立監査が算術的に検証した4,140本から奇素イデアル支持だけを抽出したもの。支持を与える原多項式・終結式の検証は親監査を継承する。31進の証書は成功した経路を入力とし、群演算を行った元のコードを読み込まない。

証明と依存関係は PROOF.md に記載した。
