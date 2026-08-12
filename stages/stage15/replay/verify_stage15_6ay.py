from fractions import Fraction
from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[3]
ns = runpy.run_path(str(root / "stages/stage15/scripts/stage15_6ay_complete_2descent.py"))
w = ns["witness"]()
assert w["lambda"] == 2 and w["d"] == 65
assert w["U"] == [185, 3]
assert w["V_minus"] == [58, 3]
assert w["V_plus"] == [59, 3]
assert w["X"] == [34225, 9]
X = Fraction(*w["X"])
assert X - 65 == 10 * Fraction(58, 3) ** 2
assert X + 65 == 10 * Fraction(59, 3) ** 2
print("Stage15-6ay replay: PASS")
