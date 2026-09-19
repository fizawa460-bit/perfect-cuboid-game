#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z57R-ENDPOINT-GLOBALIZATION-EXACT-RESTRICTIONS-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z57R_ENDPOINT_GLOBALIZATION_EXACT_RESTRICTIONS_V1"
e=d["endpoint"]
assert e["normal_bundle"]=="O_E(-2p)"
assert e["O_minus_F"]=="O_E"
assert e["O_minus_F_minus_D"]=="O_E(p)"
assert e["O_minus_2F"]=="O_E"
assert e["h0_first_normal"]==1
assert e["first_normal_section_zero_order_at_p"]==1
assert e["map_2F_to_FplusD_on_H0_isomorphism"] is True
assert d["cycles"]["support_of_2F_minus_FplusD"]=="A5 central chain Gamma"
c=d["consequence"]
assert c["endpoint_continuous_modulus_remaining"] is False
assert c["tangent_bit_detected_on_endpoint"] is False
assert c["tangent_bit_reduced_to_global_six_to_four_section_image"] is True
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z57R_ENDPOINT_GLOBALIZATION_EXACT_RESTRICTIONS_V1")
print("endpoint jets fixed; tangent bit lives in global six-to-four section image")
