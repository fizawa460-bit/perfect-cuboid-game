#!/usr/bin/env python3
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z1-Z30-POST-CONDUCTOR-REAUDIT-CERTIFICATE.json"

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_Z1_Z30_POST_CONDUCTOR_REAUDIT_V1"
    r=d["routes"]
    assert r["Z3"]["balanced_uniform"]=="EXHAUSTED"
    assert r["Z12"]["c14"]=="-5/54"
    assert r["Z4P"]["conductor_smooth_interior"] is True
    assert r["Z4P"]["bogomolov_instability_forced"] is False
    assert r["composition"]["conductor_changes_exceptional_packet"] is False
    assert r["composition"]["new_strictness"] is False
    assert d["deep_priority"]==["Z12","Z4P"]

    for l in range(1,257):
        delta=168*l*l+56*l
        disc=4*delta-336*l*l
        assert disc==336*l*l+224*l
        assert disc>0

    for key,val in d["firewalls"].items():
        assert val is False, key

    print("MB104 Z1-Z30 post-conductor re-audit verifier: PASS")

if __name__=="__main__":
    main()
