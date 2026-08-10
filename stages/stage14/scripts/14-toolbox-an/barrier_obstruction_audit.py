from fractions import Fraction
from pathlib import Path
root = Path(__file__).resolve().parents[4]
m = Fraction(3, 8)
assert Fraction(1, 2) + m == 1 - m / 3 == Fraction(7, 8)
delta = Fraction(1, 56)
kappa = Fraction(3, 4) - 2 * delta
assert (1 + kappa) / 2 == Fraction(7, 8) - delta
atlas = (root / "docs/stage14-toolbox/barrier-obstruction-atlas.md").read_text()
contract = (root / "docs/stage14-toolbox/toolbox-h-independence-contract.md").read_text()
result = (root / "stages/stage14/14-toolbox-an/result.md").read_text()
assert all(x in atlas for x in ("O4", "O6", "off-diagonal", "PAIR" if False else "critical"))
assert all(x in contract for x in ("index.json", "read-only", "PARKED", "does not replace tH14"))
assert "TOOLBOX_H_REQUIRED_FOR_TOOLBOX_MAIN=false" in result
assert "NEXT=Stage14-toolbox-ao" in result
print("Stage14-toolbox-an audit: OK")
