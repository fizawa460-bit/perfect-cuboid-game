from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from stages.stage15.scripts.stage15_6bd_diagonal_product import witness

w = witness()
assert w["F1"] == 13690
assert w["F2"] == 250
assert w["k1"] == w["k2"] == 10
assert w["product_is_square"] is True
assert w["S"] == w["expected_S"] == 1850
assert w["S"] == w["k1"] * w["Z"] * w["W"]
assert w["S"] == w["gamma"] * w["physical_R"] // 2
print("Stage15-6bd PASS")
