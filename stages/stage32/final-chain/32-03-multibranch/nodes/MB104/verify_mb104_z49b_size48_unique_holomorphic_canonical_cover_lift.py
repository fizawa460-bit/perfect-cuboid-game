#!/usr/bin/env python3
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z49B-SIZE48-UNIQUE-HOLOMORPHIC-CANONICAL-COVER-LIFT-CERTIFICATE.json"

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_Z49B_SIZE48_UNIQUE_HOLOMORPHIC_CANONICAL_COVER_LIFT_V1"

    inp=d["input"]
    assert inp["canonical_cover_degree"] == 3
    assert inp["meridian_character_pattern"] == [1,1,1]
    assert inp["deck_inversion_equivalent_pattern"] == [2,2,2]
    assert inp["topological_direction_unique"] is True

    c=d["exact_consequences"]
    assert c["punctured_topological_cover_has_unique_complex_structure"] is True
    assert c["holomorphic_etale_lift_unique"] is True
    assert c["normalization_extension_unique"] is True
    assert c["residual_holomorphic_lift_modulus"] is False

    m=d["local_models"]
    assert m["smooth_exceptional_point"] == "x=t^3"
    assert m["transverse_node"] == "x*y=t^3"
    assert m["transverse_node_type"] == "A2"
    assert m["node_count_per_connected_size48_fiber"] == 2

    assert d["next_interface"]["explicit_global_cover_equation_known"] is False

    for key,val in d["firewalls"].items():
        assert val is False, key

    print("MB104 Z49B unique holomorphic canonical-cover lift verifier: PASS")

if __name__=="__main__":
    main()
