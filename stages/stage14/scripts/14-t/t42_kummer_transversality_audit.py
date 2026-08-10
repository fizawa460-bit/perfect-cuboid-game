#!/usr/bin/env python3
"""Stage14-t42: reciprocal quotient, off-direction blocks, twisted Kummer energy audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
OUT = ROOT / "stages/stage14/data/14-t42/kummer_transversality.json"


def common_packet_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    assert k * s["delta"] == s["n"]
    assert h * k == s["eps"] * s["m"]
    return (s["eps"], s["delta"], h, s["branch"])


def gaussian_unit_key(z):
    x, y = z
    orbit = ((x,y),(-y,x),(-x,-y),(y,-x))
    return min(orbit)


def square_ratio(F1, F2):
    g = gcd(F1, F2)
    a, b = F1 // g, F2 // g
    ra, rb = isqrt(a), isqrt(b)
    assert ra * ra == a and rb * rb == b
    return ra, rb


def cross_kernel(a, b):
    g = gcd(a, b)
    return (a // g) * (b // g)


def reciprocal_quotient(states):
    groups = defaultdict(list)
    for s in states:
        key = (s["a"], s["b"], min(s["p"],s["q"]), max(s["p"],s["q"]))
        groups[key].append(s)
    assert len(groups) == 560
    reps = []
    for key, members in groups.items():
        assert len(members) == 2
        a, b, p0, q0 = key
        assert {(s["p"],s["q"]) for s in members} == {(p0,q0),(q0,p0)}
        assert len({s["F"] for s in members}) == 1
        assert len({s["kernel"] for s in members}) == 1
        rep = min(members, key=lambda s:(s["p"],s["q"]))
        reps.append(rep)
    return reps


def block_audit(reps):
    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)
    hist = Counter(len(v) for v in by_kernel.values())
    assert hist == Counter({1:528, 2:16})

    blocks=[]
    summary=Counter()
    for kernel, members in sorted(by_kernel.items()):
        if len(members)!=2:
            continue
        x,y=members
        assert (x["a"],x["b"]) != (y["a"],y["b"])
        r1,r2=square_ratio(x["F"],y["F"])
        same_ell=x["ell"]==y["ell"]
        same_branch=x["branch"]==y["branch"]
        same_common=common_packet_key(x)==common_packet_key(y)
        same_u=gaussian_unit_key(x["U"])==gaussian_unit_key(y["U"])
        same_v=gaussian_unit_key(x["V"])==gaussian_unit_key(y["V"])
        same_cover=(min(x["p"],x["q"]),max(x["p"],x["q"]))==(min(y["p"],y["q"]),max(y["p"],y["q"]))
        exact_f=x["F"]==y["F"]
        summary["blocks"] += 1
        for name,val in (("same_ell",same_ell),("same_branch",same_branch),("same_common_packet",same_common),("same_U_unit",same_u),("same_V_unit",same_v),("same_cover",same_cover),("same_exact_F",exact_f)):
            if val: summary[name]+=1
        blocks.append({
            "kernel":kernel,
            "square_ratio_root_reduced":[r1,r2],
            "same_ell":same_ell,
            "same_branch":same_branch,
            "same_common_packet":same_common,
            "same_U_unit":same_u,
            "same_V_unit":same_v,
            "same_cover":same_cover,
            "same_exact_F":exact_f,
            "direction_det":x["a"]*y["b"]-y["a"]*x["b"],
            "direction_dot":x["a"]*y["a"]+x["b"]*y["b"],
            "cover_det":x["p"]*y["q"]-y["p"]*x["q"],
            "cover_dot":x["p"]*y["p"]+x["q"]*y["q"],
            "left":{k:x[k] for k in ("a","b","p","q","ell","m","n","delta","branch","F","U","V")},
            "right":{k:y[k] for k in ("a","b","p","q","ell","m","n","delta","branch","F","U","V")},
        })
    assert summary["blocks"]==16
    return dict(summary),blocks


def convolution_audit(reps):
    r=Counter(s["kernel"] for s in reps)
    H=len(reps)
    A1=sum(v*v for v in r.values())
    assert H==560 and A1==592
    conv=Counter()
    items=list(r.items())
    for a,ra in items:
        for b,rb in items:
            conv[cross_kernel(a,b)] += ra*rb
    E4=sum(v*v for v in conv.values())
    assert E4==21_193_216//16
    assert conv[1]==A1
    non=[(k,v) for k,v in conv.items() if k!=1]
    top=sorted(non,key=lambda kv:(-kv[1],kv[0]))[:20]
    return {
        "H_reciprocal_orbits":H,
        "A1_quotient":A1,
        "A1_excess_over_diagonal":A1-H,
        "distinct_squareclasses":len(r),
        "squareclass_multiplicity_histogram":dict(sorted(Counter(r.values()).items())),
        "E4_quotient":E4,
        "E4_over_H2":E4/(H*H),
        "principal_E4":A1*A1,
        "nonprincipal_E4":E4-A1*A1,
        "distinct_cross_kernels":len(conv),
        "max_nonprincipal_cross_kernel_multiplicity":top[0][1],
        "top_nonprincipal_cross_kernels":[[k,v] for k,v in top],
        "trivial_upper_A1_H2":A1*H*H,
        "observed_to_trivial_upper_ratio":E4/(A1*H*H),
    }


def main():
    t36=runpy.run_path(str(T36_SCRIPT),run_name="stage14_t36_import")
    states=t36["build_frozen_states"]()
    reps=reciprocal_quotient(states)
    summary,blocks=block_audit(reps)
    conv=convolution_audit(reps)
    report={
        "stage":"14-t42-probe",
        "reciprocal_quotient":{
            "ordered_states":len(states),
            "orbits":len(reps),
            "exact_scaling":"H=2H*, A1=4A1*, E4=16E4* for the frozen p<->q double cover",
        },
        "off_direction_blocks":{"summary":summary,"blocks":blocks},
        "cross_kernel_convolution":conv,
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
