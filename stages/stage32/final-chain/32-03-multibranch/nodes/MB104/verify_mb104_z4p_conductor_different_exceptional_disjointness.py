#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "MB104-Z4P-CONDUCTOR-DIFFERENT-EXCEPTIONAL-DISJOINTNESS-CERTIFICATE.json"

def main():
    data = json.loads(CERT.read_text())
    assert data["schema"] == "STAGE32_MB104_Z4P_CONDUCTOR_DIFFERENT_EXCEPTIONAL_DISJOINTNESS_V1"
    assert data["assumptions"]["supported_exceptional_contact_multiplicity"] == 1

    c = data["exact_consequences"]
    assert c["supported_exceptional_contacts_smooth"] is True
    assert c["different_support_intersects_B_node"] is False
    assert c["e4_different_support_intersects_Bz_or_Bw"] is False
    assert c["positive_support_localized"] is False
    assert c["different_degree_formula"] == "336*l^2+112*l"
    assert c["different_abel_class_formula"] == "(3*l+1)*[B_node]"

    r = data["route_disposition"]
    assert r["support_subset_B_node_impossible"] is True
    assert r["supported_contacts_chargeable_as_singularity_scheme"] is False

    fw = data["firewalls"]
    for key in (
        "e4_excluded",
        "finite_degree_window_proved",
        "MB104_complete",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "merge_authorized",
    ):
        assert fw[key] is False

    # Exact arithmetic checksum for the retained genus-defect package:
    # deg Delta = 2*delta(C), delta(C)=168*l^2+56*l.
    for l in range(1, 129):
        deg_delta = 336*l*l + 112*l
        delta = 168*l*l + 56*l
        assert deg_delta == 2*delta
        assert deg_delta > 0

    print("MB104 Z4P conductor/different exceptional-disjointness verifier: PASS")

if __name__ == "__main__":
    main()
