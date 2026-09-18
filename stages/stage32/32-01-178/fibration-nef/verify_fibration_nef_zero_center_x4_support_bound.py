#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
GRF=ROOT/"stages/stage32/32-01-178/topdown-02/TD02-GRF04-FULL178-AGGREGATE-CHECKPOINT.json"
GRF_BLOB="4e2ccf5f9f8d25f117e4e9792d3b54ec31a0799b"


def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)


def git_blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def main()->None:
    req(GRF.is_file() and git_blob(GRF)==GRF_BLOB,"GRF04 source drift")
    grf=json.loads(GRF.read_text())
    req(grf["mathematical_adapter"]["rho"]=="q/2 + (d/2 - 2*x4 - t)^2/12","GRF04 rho drift")
    req(grf["mathematical_adapter"]["t"]=="x0+x1+x6+x9","GRF04 t drift")

    g,d,e=1,192,32
    genus_budget=Fraction(d*d,16)+d+2-2*g
    req(genus_budget==2496,"genus budget drift")

    # qexc>=0, residual Picard penalty>=0, t>=0.  Therefore any admissible
    # key must already satisfy the GRF04 static inequality at qexc=0:
    #   (96-2*x4-t)^2/12 <= 2496.
    # For x4>=135 and t>=0 the absolute value is at least 174, giving
    # 174^2/12 = 2523 > 2496.  At x4=134,t=0 it is 172^2/12 <2496,
    # so 134 is the sharp uniform nonnegative-t support boundary.
    rho_134_t0=Fraction((96-2*134)**2,12)
    rho_135_t0=Fraction((96-2*135)**2,12)
    req(rho_134_t0 < genus_budget,"x4=134 unexpectedly uniformly excluded")
    req(rho_135_t0 > genus_budget,"x4=135 not uniformly excluded")

    normal_budget=19*d-5*e
    req(normal_budget==3488,"normal budget drift")
    admissible=tuple(range(0,135))
    excluded=normal_budget-134

    out={
      "schema":"STAGE32_32_01_178_ZERO_CENTER_X4_SUPPORT_BOUND_V1",
      "purpose":"replace the nominal g1-d192/e32 x4 range 0..3488 by the exact GRF04 uniform support window 0..134 before any weighted replay",
      "source_locks":{"td02_grf04_blob_sha1":GRF_BLOB},
      "target":{"row_id":"g1-d192","g":g,"d":d,"e":e,"normal_budget_x4_upper":normal_budget},
      "exact_bound":{
        "genus_budget":str(genus_budget),
        "necessary_static_inequality":"(96-2*x4-t)^2/12 <= 2496",
        "t_nonnegative":True,
        "largest_x4_not_uniformly_excluded":134,
        "smallest_x4_uniformly_excluded":135,
        "rho_at_x4_134_t0":str(rho_134_t0),
        "rho_at_x4_135_t0":str(rho_135_t0),
        "admissible_x4_values":list(admissible),
        "nominal_x4_values_uniformly_excluded_count":excluded,
      },
      "next_exact_step":"run the zero-center closed-form weighted consumer only for x4=0..134, cache A/H polynomials across all slices, and freeze the resulting complete e32 row certificate if exact-head replay succeeds",
      "firewalls":{"full_row_census_claimed":False,"full178_census_claimed":False,
                   "main_credit_changed":False,"theorem_credit_changed":False,
                   "endpoint_credit_changed":False,"merge":False},
    }
    print("ZERO_CENTER_X4_SUPPORT_BOUND_SUMMARY="+json.dumps({
      "x4_min":0,"x4_max":134,"uniformly_excluded_from":135,
      "normal_budget_upper":normal_budget,"uniformly_excluded_count":excluded
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
