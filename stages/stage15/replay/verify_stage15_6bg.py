from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from stages.stage15.scripts.stage15_6bg_support_gate import witness

w = witness()
r = w["receiver"]
f = w["flags"]
assert r["product_is_square"] is True
assert r["S"] == 1850
assert r["inside_physical_cutoff"] is True
assert f["chan_direct_reuse"] is False
assert f["choi_direct_reuse"] is False
assert f["alpoge_ho_direct_reuse"] is False
assert f["fixed_S_fiber_closed"] is True
assert f["weighted_twist_second_moment_gate_superseded"] is True
assert f["admissible_diagonal_support_bound_proved"] is False
print("Stage15-6bg PASS")
