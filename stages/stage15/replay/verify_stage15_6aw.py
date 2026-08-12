from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[3]
ns = runpy.run_path(str(root / "stages/stage15/scripts/stage15_6aw_nontorsion_audit.py"))
a = ns["audit"]()
assert a["half_plus_d_polynomial"] == [1, -4, 2, 4, 1]
assert a["half_minus_d_polynomial"] == [1, 4, 2, -4, 1]
assert a["division3_discriminant"] == 48
assert a["unit_ratio"] == [1, 1]
assert a["witness_ratio_gt_one"] is True
assert a["torsion_unit_branch"] is True
print("Stage15-6aw replay: PASS")
