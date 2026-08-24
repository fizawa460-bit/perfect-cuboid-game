#!/usr/bin/env python3
"""Execute the Q-unit materializer with the correct blow-up exceptional order.

For a linear Cartier factor through an ordinary double point of the cuboid
surface, the total transform has exceptional coefficient one.  The previous
pilot incorrectly used Multiplicity(C,pt), which is a scheme-curve
multiplicity and is not the exceptional valuation of the linear function.
"""
from pathlib import Path

root = Path(__file__).resolve().parent
src = (root / "materialize_q_units.py").read_text(encoding="utf-8")
old = 'pm := [pt in C select Multiplicity(C, pt) else 0 : pt in pts];'
new = 'pm := [pt in C select 1 else 0 : pt in pts];'
if src.count(old) != 1:
    raise SystemExit("expected exactly one superseded exceptional-coefficient line")
src = src.replace(old, new)
exec(compile(src, str(root / "materialize_q_units.py") + "[exceptional-order-v2]", "exec"), {"__name__": "__main__", "__file__": str(root / "materialize_q_units.py")})
