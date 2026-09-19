#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z49-SIZE48-FINITE-CANONICAL-ROOT-PLUMBING-CERTIFICATE.json"

def solve_discrepancy():
    # Symmetric system:
    # -4x+y=4, 2x-2y=0.
    x=Fraction(-4,3)
    y=x
    assert -4*x+y == 4
    assert 2*x-2*y == 0
    return x,y,x

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_Z49_SIZE48_FINITE_CANONICAL_ROOT_PLUMBING_V1"
    assert d["graph"]["tree"] is True
    assert d["graph"]["intersection_matrix"] == [[-4,1,0],[1,-2,1],[0,1,-4]]

    a=solve_discrepancy()
    assert [str(x) for x in a] == d["discrepancy"]["coefficients"]
    assert d["discrepancy"]["meridian_exponents_fixed"] is True

    assert d["plumbing"]["continuous_edge_scalars_absorbed"] is True
    assert d["plumbing"]["residual_continuous_edge_scalar_modulus"] is False

    t=d["torsion"]
    assert t["each_elliptic_3_torsion_order"] == 9
    assert t["candidate_upper_bound"] == 9*9 == 81
    assert t["higher_nilpotent_thickening_adds_mu3_torsors"] is False
    assert t["all_81_extend_claimed"] is False

    c=d["conclusions"]
    assert c["finite_canonical_root_receiver"] is True
    assert c["actual_root_class_identified"] is False
    assert c["complete_analytic_germ_classified"] is False
    assert c["canonical_cover_equation_known"] is False

    for key,val in d["firewalls"].items():
        assert val is False, key

    print("MB104 Z49 size48 finite canonical-root plumbing verifier: PASS")

if __name__=="__main__":
    main()
