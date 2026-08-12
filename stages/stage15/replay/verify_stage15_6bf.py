from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from stages.stage15.scripts.stage15_6bf_denominator_rigidity import witness

w = witness()
o = w["odd_kappa_state"]
e = w["even_kappa_state"]
assert o["U"] == [185, 3]
assert o["expected_denominator"] == 3
assert o["odd_denominator_coprime"] is True
assert e["U"] == [5, 2]
assert e["expected_denominator"] == 2
assert e["odd_denominator_coprime"] is True
print("Stage15-6bf PASS")
