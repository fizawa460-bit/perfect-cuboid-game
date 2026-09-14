#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
md = root / "stages/stage32/proof/LGS-MB101-102-REENTRY-PREFLIGHT.md"
contract = root / "stages/stage32/proof/LGS-MB101-102-REENTRY-CONTRACT.json"

data = json.loads(contract.read_text())
text = md.read_text()
assert data["schema"] == "STAGE32_LGS_MB101_MB102_REENTRY_PREFLIGHT_V1"
assert data["historical_blocker"] == "LGS_MISSING_POPULATION_WIDE_GLOBAL_TO_LOCAL_DEFECT_ADAPTER"
for token in ("DIRECT_RECONNECT", "FINITE_EXCEPTION_REDUCTION", "SEMANTIC_ADAPTER_GAP", "NO_NEW_INFORMATION"):
    assert token in data["allowed_outcomes"]
    assert token in text
assert "MB101" in text and "MB102" in text
assert "no new heavy compute" in text
assert "no Stage32 MAIN authority or pruning mutation" in text
assert all(data["forbidden"].values())
print("PASS_STAGE32_LGS_MB101_MB102_REENTRY_PREFLIGHT")
