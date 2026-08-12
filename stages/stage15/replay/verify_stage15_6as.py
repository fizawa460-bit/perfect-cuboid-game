import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "stages/stage15/scripts/stage15_6as_twist_height_audit.py"
EVIDENCE = ROOT / "stages/stage15/evidence/stage15_6as_twist_height_audit.json"

spec = importlib.util.spec_from_file_location("s6as", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

data = mod.audit()
assert data["delta"] == 64
assert data["nara_direct"] is False
frozen = json.loads(EVIDENCE.read_text())
assert frozen["audit_verdict"] == "BLOCK"
assert frozen["nara_theorem_1_1_directly_applicable"] is False
assert frozen["covering_map_height_adapter_proved"] is False
print("STAGE15_6AS_VERIFY=PASS")
print("AUDIT_VERDICT=BLOCK")
print("NARA_DIRECTLY_APPLICABLE=false")
