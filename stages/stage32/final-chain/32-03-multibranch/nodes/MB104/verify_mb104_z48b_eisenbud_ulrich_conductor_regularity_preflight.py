#!/usr/bin/env python3
import json
from pathlib import Path

D=json.loads((Path(__file__).resolve().parent/"MB104-Z48B-EISENBUD-ULRICH-CONDUCTOR-REGULARITY-PREFLIGHT-CERTIFICATE.json").read_text())
assert D["schema"]=="STAGE32_MB104_Z48B_EISENBUD_ULRICH_CONDUCTOR_REGULARITY_PREFLIGHT_V1"
assert D["receiver"]["integral_cartier_curve_on_smooth_surface"] is True
assert D["receiver"]["locally_gorenstein"] is True
assert D["receiver"]["embedded_arithmetically_gorenstein_proved"] is False
assert D["receiver"]["embedded_ACM_proved"] is False
assert D["disposition"]["theorem_applied"] is False
assert D["disposition"]["invalid_transfer_blocked"] is True
for k,v in D["firewalls"].items():
    assert v is False, k
print("MB104 Z48B Eisenbud-Ulrich preflight verifier: PASS")
