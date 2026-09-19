#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z57-A5-CURVETTE-MONOMIALS-SELECT-T0-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z57R_A5_LOCAL_ONLY_GLOBALIZATION_CORRECTION_V1"
a=d["local_a5"]
assert [a["val_u"][i]+a["val_v"][i] for i in range(7)]==[6*x for x in a["val_s"]]
assert d["endpoint"]["normal_bundle"]=="O_E(-2p)"
assert d["endpoint"]["transverse_parameter_globally_principal"] is False
assert d["endpoint"]["globalization_adapter_required"] is True
assert d["withdrawn"]["global_generators_from_us_vs_s2_s3"] is False
assert d["withdrawn"]["tangent_type_T0"] is False
assert d["retained"]["tangent_candidates"]==["T0","T1"]
assert d["retained"]["c_known"] is False
assert d["contradiction_check"]["naive_model_isolated"] is False
assert d["contradiction_check"]["actual_germ_isolated"] is True
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z57R_A5_LOCAL_ONLY_GLOBALIZATION_CORRECTION_V1")
print("T0 withdrawn: local A5 monomials require endpoint globalization")
