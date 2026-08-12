from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from stages.stage15.scripts.stage15_6be_fixed_diagonal_fiber import witness

w = witness()
assert w["F_product_matches"] is True
assert w["tau_S2"] == 45
assert w["r2_F1"] == 24
assert w["r2_F2"] == 16
assert w["r2_F1_le_4tau"] is True
assert w["r2_F2_le_4tau"] is True
print("Stage15-6be PASS")
