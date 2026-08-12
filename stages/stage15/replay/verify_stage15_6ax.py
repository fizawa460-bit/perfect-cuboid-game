from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[3]
ns = runpy.run_path(str(root / "stages/stage15/scripts/stage15_6ax_height_bridge_audit.py"))
a = ns["formal_scale_countermodel"](10**6)
assert a["physical_product_inequality"] is True
assert a["small_kappa_inequality"] is True
assert a["naive_x_height_upper"] > a["petit_threshold_alpha_1_over_240"]
print("Stage15-6ax replay: PASS (BLOCK verdict reproduced)")
