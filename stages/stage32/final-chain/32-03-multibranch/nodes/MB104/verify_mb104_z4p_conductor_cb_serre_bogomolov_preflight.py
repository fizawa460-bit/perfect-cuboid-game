#!/usr/bin/env python3
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z4P-CONDUCTOR-CB-SERRE-BOGOMOLOV-PREFLIGHT-CERTIFICATE.json"

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_Z4P_CONDUCTOR_CB_SERRE_BOGOMOLOV_PREFLIGHT_V1"
    assert d["cayley_bacharach"]["intrinsic_exact_setting_source_locked"] is False
    assert d["cayley_bacharach"]["surjectivity_implies_CB"] is False
    assert d["best_case_serre"]["assumed_CB"] is True
    assert d["best_case_serre"]["instability_forced"] is False

    for l in range(1,257):
        delta=168*l*l+56*l
        c1sq=336*l*l
        disc=4*delta-c1sq
        assert disc==336*l*l+224*l
        assert disc>0

    assert d["alternate_determinant"]["source_valid_CB_available"] is False
    assert d["conclusions"]["standard_serre_reider_bogomolov_closer"] is False

    for key,val in d["firewalls"].items():
        assert val is False, key

    print("MB104 Z4' conductor CB/Serre/Bogomolov preflight verifier: PASS")

if __name__=="__main__":
    main()
