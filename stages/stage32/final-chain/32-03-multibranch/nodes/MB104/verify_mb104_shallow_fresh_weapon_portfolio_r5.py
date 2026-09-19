#!/usr/bin/env python3
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-SHALLOW-FRESH-WEAPON-PORTFOLIO-R5-CERTIFICATE.json"

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_SHALLOW_FRESH_WEAPON_PORTFOLIO_R5_V1"
    assert d["route_B_cosection"]["stable_map_vdim"]=="-112*l"
    c=d["route_C_gonality"]
    assert c["strict_transform_square"]=="-112*l-sum(m_q)"
    assert c["singular_curve_torsion_free_pencil_degree"]=="168*l^2+56*l+2"
    assert 2*168==336 and 2*56==112
    assert d["next_clue"]["equigeneric_normal_pullback_degree"]=="-112*l"
    assert d["firewalls"]["MB104_complete"] is False
    assert d["firewalls"]["merge_authorized"] is False
    print("PASS: MB104 shallow fresh-weapon portfolio R5")
    print("next clue: conductor-normal pullback degree = -112l")

if __name__=="__main__":
    main()
