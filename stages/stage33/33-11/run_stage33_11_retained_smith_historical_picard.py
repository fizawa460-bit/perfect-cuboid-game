#!/usr/bin/env python3
"""Replay the retained q256 Smith basis from the historical Picard basis.

Stage33-09 certified the actual coordinate swaps in the historical q256
64-dimensional Picard basis.  The dormant Stage33-07 replay helper instead
reconstructed a different current marking and correctly failed its historical
Gram lock.  This runner leaves the byte-identical Smith replay/verifier intact
but replaces only that input block with the source-locked historical Picard
Gram, cc/ct, seven signs, and Stage33-09 actual swaps.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
LEGACY = STAGE33 / "33-07"
TARGET = LEGACY / "materialize_retained_common_smith_transport_actual_swaps.py"
BRIDGE = STAGE33 / "33-09" / "marked-picard-basis-bridge-certified.json"
OLD_BASE = LEGACY / "picard_base_rows_retained.py"
OLD_SIGNS = LEGACY / "picard_coordinate_sign_rows_retained.py"
OUT = LEGACY / "retained-common-smith-transport-actual-swaps.json"
EXPECTED_BRIDGE = "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92"

src = TARGET.read_text(encoding="utf-8")
old = '''gal = runpy.run_path(str(GAL_SCRIPT))
at2 = gal["base"]
pic = at2["ns"]
gram = [[int(x) for x in row] for row in at2["gram"]]
if csha(gram) != EXPECTED_GRAM_MATRIX_SHA256:
    raise SystemExit("locally reconstructed Picard Gram differs from the historical q256 Gram")
if pic["det_bareiss"](gram) != -268435456:
    raise SystemExit("Picard Gram determinant regression")

all_picard = at2["all_picard"]
swap12_pic = all_picard[0]
swap13_pic = all_picard[1]
six_sign_pic = all_picard[3:9]
c_sign_pic = [[int(i == j) for j in range(64)] for i in range(64)]
for G in six_sign_pic:
    c_sign_pic = pic["mm"](c_sign_pic, G)
sign_pic = six_sign_pic + [c_sign_pic]
cc_pic = gal["cc_pic"]
ct_pic = gal["ct_pic"]
'''
new = '''gal = runpy.run_path(str(GAL_SCRIPT))
at2 = gal["base"]
pic = at2["ns"]
old_base = runpy.run_path(str(HERE / "picard_base_rows_retained.py"))["load"]()
old_signs = runpy.run_path(str(HERE / "picard_coordinate_sign_rows_retained.py"))["load"]()
bridge = json.loads((HERE.parent / "33-09" / "marked-picard-basis-bridge-certified.json").read_text(encoding="utf-8"))
bridge_body = dict(bridge); bridge_claimed = bridge_body.pop("canonical_sha256", None)
bridge_actual = csha(bridge_body)
if bridge_claimed != "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92" or bridge_actual != bridge_claimed:
    raise SystemExit("Stage33-09 marked Picard bridge lock moved")
locks09 = bridge["source_locks"]
if old_base["canonical_sha256"] != locks09["retained_old_picard_base_sha256"]:
    raise SystemExit("historical Picard base differs from Stage33-09 source lock")
if old_signs["canonical_sha256"] != locks09["retained_old_picard_signs_sha256"]:
    raise SystemExit("historical Picard signs differ from Stage33-09 source lock")
gram = [[int(x) for x in row] for row in old_base["picard_gram_64x64"]]
if csha(gram) != EXPECTED_GRAM_MATRIX_SHA256:
    raise SystemExit("source-locked historical Picard Gram differs from q256 producer Gram")
if pic["det_bareiss"](gram) != -268435456:
    raise SystemExit("Picard Gram determinant regression")
swaps = bridge["actual_coordinate_swaps_in_historical_magma_picard_basis"]
swap12_pic = [[int(x) for x in row] for row in swaps["swap12_action_64x64"]]
swap13_pic = [[int(x) for x in row] for row in swaps["swap13_action_64x64"]]
order = list(old_signs["coordinate_order"])
if order != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
    raise SystemExit("historical coordinate-sign order moved")
sign_pic = [[[int(x) for x in row] for row in old_signs["picard_actions_64x64"][name]] for name in order]
cc_pic = [[int(x) for x in row] for row in old_base["picard_action_cc_64x64"]]
ct_pic = [[int(x) for x in row] for row in old_base["picard_action_ct_64x64"]]
'''
if src.count(old) != 1:
    raise SystemExit("Stage33-07 retained-Smith input patch anchor moved")
src = src.replace(old, new)

g = {"__name__": "__main__", "__file__": str(TARGET)}
exec(compile(src, str(TARGET), "exec"), g, g)

# Harden provenance of the generated compact transport without changing any
# mathematical matrices.  The downstream verifier accepts self-locked extras.
obj = json.loads(OUT.read_text(encoding="utf-8"))
obj["source_locks"]["stage33_09_marked_picard_bridge_sha256"] = EXPECTED_BRIDGE
body = dict(obj)
body.pop("canonical_sha256", None)
obj["canonical_sha256"] = hashlib.sha256(
    json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
OUT.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "transport_sha256": obj["canonical_sha256"],
    "stage33_09_bridge_sha256": EXPECTED_BRIDGE,
    "historical_picard_basis_used": True,
    "byte_identical_historical_smith_program": obj["common_smith_replay"]["submitted_code_byte_identical_to_historical_producer"],
}, indent=2, sort_keys=True))
