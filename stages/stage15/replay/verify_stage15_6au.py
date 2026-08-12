import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "stages/stage15/scripts/stage15_6au_small_height_twist_audit.py"
EVIDENCE = ROOT / "stages/stage15/evidence/stage15_6au_small_height_twist_audit.json"

spec = importlib.util.spec_from_file_location("s6au", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

data = mod.audit()
assert data["audit_verdict"] == "NEW_GATE"
assert data["petit_species_match"] is True
assert data["twist_count_exponent"] == 0.5
frozen = json.loads(EVIDENCE.read_text())
assert frozen["petit_alpha_range"] == "(0,1/120)"
assert frozen["covering_map_adapter_proved"] is False
assert frozen["petit_theorem_applied_to_stage15"] is False
print("STAGE15_6AU_VERIFY=PASS")
print("AUDIT_VERDICT=NEW_GATE")
print("PETIT_STAGE15_ADAPTER_PROVED=false")
