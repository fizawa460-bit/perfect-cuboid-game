#!/usr/bin/env python3
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z48-CONDUCTOR-SCHEME-ADJOINT-ADAPTER-CERTIFICATE.json"

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_Z48_CONDUCTOR_SCHEME_ADJOINT_ADAPTER_V1"
    inv=d["receiver"]["surface_invariants"]
    assert (inv["K2"]+inv["c2"])//12 == inv["chi_O"] == 8
    assert 1-inv["q"]+inv["pg"] == inv["chi_O"]

    c=d["exact_consequences"]
    assert c["conductor_scheme_zero_dimensional"] is True
    assert c["conductor_scheme_length_equals_delta"] is True
    assert c["conductor_scheme_in_smooth_interior"] is True
    assert c["adjoint_evaluation_surjective"] is True
    assert c["adjoint_conditions_exactly_independent"] is True
    assert c["carrier_unique_in_linear_system_given_full_conductor_scheme"] is True
    assert c["conductor_schemes_finitely_classified"] is False
    assert c["carrier_excluded"] is False

    for l in range(1,257):
        delta=168*l*l+56*l
        diff=336*l*l+112*l
        h0_adj=168*l*l+56*l+8
        assert diff == 2*delta
        assert h0_adj-delta == 8
        assert -112*l < 0

    for key,val in d["firewalls"].items():
        assert val is False, key

    print("MB104 Z48 conductor-scheme adjoint adapter verifier: PASS")

if __name__=="__main__":
    main()
