from fractions import Fraction
from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[3]
ns = runpy.run_path(str(root / "stages/stage15/scripts/stage15_6av_covering_map.py"))

w = ns["witness"]()
assert w["K"] == [3, -1]
assert w["k"] == 10 and w["kappa"] == 13
assert w["f_g"] == [117, 1]
assert w["twist_d"] == 65
assert w["X"] == [34225, 9]
assert w["Y"] == [6330700, 27]

X = Fraction(*w["X"])
Y = Fraction(*w["Y"])
assert Y * Y == X**3 - 65**2 * X
assert X == Fraction(65 * (117**2 + 1), 2 * 117)
assert ns["hessian_value"](3, -1, 13, 6, 1) == 12 * 13**2 * 10**2 * 37**2
print("Stage15-6av replay: PASS")
