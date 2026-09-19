#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).with_name("MB104-Z46-LOG-BOGOMOLOV-MIYAOKA-CORRECTION-PREFLIGHT-CERTIFICATE.json")
d=json.loads(p.read_text())
assert d["schema"]=="STAGE32_MB104_Z46_LOG_BOGOMOLOV_MIYAOKA_CORRECTION_PREFLIGHT_V1"
assert d["input"]["z45_size48_asymptotic_margin"]=="4/3"
assert d["input"]["canonical_cover_analytic_type_known"] is False
assert d["source_gate"]["arbitrary_nonlc_index3_correction_source_locked"] is False
assert d["source_gate"]["quotient_klt_lc_formula_import_authorized"] is False
assert d["result"]["signed_correction_exceeding_4_over_3_established"] is False
assert d["result"]["contraction_local_euler_route"]=="FROZEN"
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z46_LOG_BMY_CORRECTION_PREFLIGHT_V1")
print("route=FROZEN reason=source_class_mismatch")
print("next=MB104-Z47-POST-CONTRACTION-GLOBAL-RESCORE")
