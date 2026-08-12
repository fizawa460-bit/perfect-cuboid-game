import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "stages/stage15/scripts/stage15_6ar_twist_adapter.py"
EVIDENCE = ROOT / "stages/stage15/evidence/stage15_6ar_twist_adapter.json"

spec = importlib.util.spec_from_file_location("s6ar", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

assert mod.verify_examples()
data = json.loads(EVIDENCE.read_text())
assert data["audit_verdict"] == "PASS"
assert data["binary_quartic_I"] == "12*(k*kappa)^2"
assert data["binary_quartic_J"] == 0
assert data["product_k_kappa_recoverable_from_d"] is True
assert data["point_count_proved"] is False
print("STAGE15_6AR_VERIFY=PASS")
print("AUDIT_VERDICT=PASS")
print("EXACT_TWIST_PARAMETER=true")
