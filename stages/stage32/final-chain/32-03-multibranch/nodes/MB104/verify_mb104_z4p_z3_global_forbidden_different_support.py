#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "MB104-Z4P-Z3-GLOBAL-FORBIDDEN-DIFFERENT-SUPPORT-CERTIFICATE.json"

def main():
    data=json.loads(CERT.read_text())
    assert data["schema"]=="STAGE32_MB104_Z4P_Z3_GLOBAL_FORBIDDEN_DIFFERENT_SUPPORT_V1"
    i=data["inputs"]
    assert i["supported_exceptional_curves"] + i["unsupported_exceptional_curves"] == i["total_exceptional_curves"] == 48
    assert i["supported_contact_multiplicity"] == 1
    assert i["complete_null_locus_known"] is True

    c=data["exact_consequences"]
    assert c["carrier_meets_unsupported_exceptionals"] is False
    assert c["supported_exceptional_contacts_are_smooth"] is True
    assert c["different_meets_supported_exceptional_contacts"] is False
    assert c["carrier_meets_null_elliptic_quartics"] is False
    assert c["different_meets_any_exceptional_curve"] is False
    assert c["different_lies_over_original_surface_smooth_locus"] is True
    assert c["positive_singularity_locus_finitely_localized"] is False

    r=data["route_consequences"]
    assert r["exceptional_node_local_algebra_can_carry_quadratic_different_mass"] is False
    assert r["supported_contacts_chargeable_as_singularity_length"] is False

    for key,value in data["firewalls"].items():
        assert value is False, key

    print("MB104 Z4P+Z3 global forbidden different support verifier: PASS")

if __name__=="__main__":
    main()
