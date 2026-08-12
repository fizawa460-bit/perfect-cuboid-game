import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "stages/stage15/scripts/stage15_6at_branch_memory_audit.py"
EVIDENCE = ROOT / "stages/stage15/evidence/stage15_6at_branch_memory_audit.json"

spec = importlib.util.spec_from_file_location("s6at", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

data = mod.audit(10000)
assert data["scale_compatible_k_count"] == 5000
assert data["subpolynomial_forced"] is False
frozen = json.loads(EVIDENCE.read_text())
assert frozen["audit_verdict"] == "BLOCK"
assert frozen["size_only_norm_core_summability"] is False
assert frozen["ar009_recharge"] is False
print("STAGE15_6AT_VERIFY=PASS")
print("AUDIT_VERDICT=BLOCK")
print("SIZE_ONLY_NORM_CORE_SUMMABILITY=false")
