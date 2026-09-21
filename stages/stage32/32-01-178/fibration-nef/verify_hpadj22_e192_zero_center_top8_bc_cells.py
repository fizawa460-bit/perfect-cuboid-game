#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE / "verify_hpadj22_e192_zero_center_all_a_all_unequal_support7_family.py"
PARENT_BLOB = "7d988aeb3c3895358d754d1dbb41cfd8a22668bd"
SINGLE = HERE / "verify_hpadj22_e192_zero_center_single_witness.py"
SINGLE_BLOB = "5e54175ac7ef5983d639f1657f7878142d3bd5dc"

EXPECTED = (
    {"b":49,"c":48,"amax":57,"H":5428920,"Hbins":60884,"Hsha":"5ea0967cd7a85711e357c04850bb6757324be224faea825e2d7775e872145655","Asha":"c5d92268c4ca4ce13ff5240a3e4f7bc80c2d90bfdf7e24b10431944291f49bcd","current":7199513851467,"refined":3344045626622,"reduction":3855468224845},
    {"b":49,"c":49,"amax":56,"H":5729300,"Hbins":64477,"Hsha":"9aab694aae14c6b223aacea2c0d62fd7ae7d03c7a58b378fc396c8568b8b1bc4","Asha":"56077f756478f00f4cc5ea5e87d8eb36ac7e264c110c04f6d0333fd49159ed2f","current":7194007715249,"refined":3329033081518,"reduction":3864974633731},
    {"b":48,"c":48,"amax":58,"H":5144755,"Hbins":58613,"Hsha":"1ac22dfc77f0247b9420c825377565ed427f2c0ae8ecdfa06b36be0d46fab082","Asha":"6a6247b8f6acebbb09848a06b715b9567773ed84ce308a992efd0c40957c6722","current":7215903746086,"refined":3370046144734,"reduction":3845857601352},
    {"b":48,"c":49,"amax":57,"H":5428920,"Hbins":60417,"Hsha":"8a5ee4714f7eb3a1b738b987283efc28d00020668e83ad8c3c7f0a659bc0c0b6","Asha":"d9974926d0a77a0f0ac0357c0de6e0d6774a8571b2d5ed4833f7cb6e9acf8f4d","current":7217664818085,"refined":3357209850390,"reduction":3860454967695},
    {"b":50,"c":48,"amax":56,"H":5720376,"Hbins":62506,"Hsha":"887f80605753a1e2a5f6cf6d9ac0caeb345e914ad99ed29b63ac376c7f7831d1","Asha":"3136c6f9d786306fbc4fb832426d370b46f5838809753366174211d09b695c4a","current":7164317025887,"refined":3310069332353,"reduction":3854247693534},
    {"b":48,"c":50,"amax":56,"H":5720376,"Hbins":62642,"Hsha":"9a7fd57ff213a2619efae9df67699a9ee95e8dd15b1b3ebf73c00be001459647","Asha":"2d6473fd6ba909da60a844f333a4c21e4a821ba4c3564cc6a7a9a364fc4a782b","current":7195962907123,"refined":3335627233972,"reduction":3860335673151},
    {"b":49,"c":47,"amax":58,"H":5136912,"Hbins":60350,"Hsha":"f033f09f57d2b34d41079643588bb9c7449152948054ccafd834cc3ba7241de2","Asha":"c38303cf0c91f70890c28d86f2b7685e496e64deef777db0918a310f41ad0c87","current":7190339753637,"refined":3352136864564,"reduction":3838202889073},
    {"b":47,"c":49,"amax":58,"H":5136912,"Hbins":60268,"Hsha":"f36960efc2dba0eacfcccaad8947de7a0e0d8f8cc5c2708db2c85d5c6e88c4ae","Asha":"ff3a5f2bd213f3e0d1bac3ebc1490b1d6cd40bd0aae25c2721dbc3295b1dd3eb","current":7221685750686,"refined":3376970327437,"reduction":3844715423249},
)

EXPECTED_CURRENT = 57599395568220
EXPECTED_REFINED = 26775138461590
EXPECTED_REDUCTION = 30824257106630
EXPECTED_CANDIDATE = 138652708976393486864


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def evaluate_cell(*, p, single, direct, old, bnd, h16, p15, counter, fast, cert, rec: dict) -> dict:
    b, c = int(rec["b"]), int(rec["c"])
    d, g, e, h = 192, 1, 192, 96
    threshold_q = 4992
    amax = 154 - b - c
    req(amax == int(rec["amax"]) and amax >= 3, f"amax drift {(b,c,amax)}")

    hh, htotal = p.unequal_support7_hist(b=b, c=c)
    req(htotal == int(rec["H"]), f"H tuple drift {(b,c)}")
    req(len(hh) == int(rec["Hbins"]), f"H bin drift {(b,c)}")
    req(p.hist_sha(hh) == rec["Hsha"], f"H stream drift {(b,c)}")
    req(all(((c + int(t)) & 1) == 0 for (t,_q,_r) in hh), f"Picard static parity drift {(b,c)}")

    c3 = counter.component3(d, b, c)
    req(c3 == 9, f"component3 no longer maximal {(b,c,c3)}")
    interval = tuple(p15.shard_for_b(b))
    expected_interval = (36,47) if b <= 47 else (48,59)
    req(interval == expected_interval, f"current b-shard drift {(b,c,interval)}")
    req(b <= 59, f"selected b escaped intended bounded search {(b,c)}")

    by_a_hist: dict[int,Counter[int]] = {}
    for a in range(3, amax + 1):
        ah = p.positive_A_hist(a)
        req(sum(ah.values()) == counter.triple_free_count(a, 3), f"A support3 drift {(b,c,a)}")
        ca = counter.component_a(d, a)
        srem = min(16,d) + ca + c3
        es = bnd.eligible_e(counter,d,g,h,a,b,c,10,srem,counter.ceil_div(d-16*g+16,4))
        req(e in es, f"e192 eligibility drift {(b,c,a)}")

        R = e-a-b-c
        known = (b+c,a,0,0,0,0)
        caps = tuple(min(R,d-known[i]) for i in range(5))
        sum_lo = max(0,R-(d-known[5]))
        req(R >= 0 and caps == (R,R,R,R,R) and sum_lo == 0,
            f"residual simplex drift {(b,c,a,R,caps,sum_lo)}")
        by_a_hist[a] = ah

    t_values = sorted({int(t) for (t,_q,_r) in hh})
    for a in range(3, amax + 1):
        R = e-a-b-c
        for t in t_values:
            parity = fast.parity_witness((a,b,c,t,0,e,d))
            expected = ((b+t)&1, a&1, 0,0,0)
            req(parity == expected, f"Picard parity drift {(b,c,a,t,parity)}")
            req(sum(expected) <= R, f"minimal parity exceeds R {(b,c,a,t)}")
            req(fast.membership_ok(cert,(a,b,c,t,0,e,d)+expected),
                f"Picard membership drift {(b,c,a,t)}")

    caps_x4 = bnd.x4_caps(h16,h,g,b,c)
    xr = h16.a0_interval(h,g,b,c)
    req(xr is not None, f"missing x4 interval {(b,c)}")
    cap_by_x4: dict[int,int] = {}
    for x4 in range(xr[0],xr[1]+1):
        room = -int(h16.f0(h,g,b,c,x4))
        req(room >= 0, f"x4 room drift {(b,c,x4)}")
        cap_by_x4[x4] = room // 138

    all_qA = set()
    for ah in by_a_hist.values():
        all_qA.update(ah)
    for qA in all_qA:
        for r in (0,1):
            exact = sum(
                1 for x4 in range(xr[0],xr[1]+1)
                if (x4&1)==r and int(qA)<=cap_by_x4[x4]
            )
            req(exact == int(bnd.survivor_count(caps_x4,r,int(qA))),
                f"x4 adapter drift {(b,c,qA,r)}")

    current_limits: Counter[int] = Counter()
    refined_limits = (Counter(),Counter())
    for (t,qbc,r), hmult in hh.items():
        hmult = int(hmult)
        start = xr[0] + ((int(r)-xr[0])&1)
        r0 = (b+int(t))&1
        for x4 in range(start,xr[1]+1,2):
            cur_limit = min(cap_by_x4[x4], threshold_q-int(qbc))
            if cur_limit < 0:
                continue
            current_limits[cur_limit] += hmult
            z = 96 - 2*x4 - int(t)
            base_num = 149760 - 25*z*z - 30*r0
            cut0 = base_num // 30
            cut1 = (base_num - 6) // 30
            refined_limits[0][min(cur_limit,cut0-int(qbc))] += hmult
            refined_limits[1][min(cur_limit,cut1-int(qbc))] += hmult

    stream = hashlib.sha256()
    current = refined = 0
    by_a = []
    for a in range(3,amax+1):
        ah = by_a_hist[a]
        cur = p.eval_limit_hist(ah,current_limits,threshold_q)
        ref = p.eval_limit_hist(ah,refined_limits[a&1],threshold_q)
        req(0 <= ref <= cur, f"refinement weakened {(b,c,a)}")
        row = {
            "a":a,
            "A_support3_ordered_triples":sum(ah.values()),
            "current":cur,"refined":ref,"reduction":cur-ref,
        }
        by_a.append(row)
        stream.update(json.dumps(row,sort_keys=True,separators=(",",":")).encode()+b"\n")
        current += cur
        refined += ref

    reduction = current-refined
    req(stream.hexdigest() == rec["Asha"], f"per-a stream drift {(b,c)}")
    req(current == int(rec["current"]), f"current drift {(b,c,current)}")
    req(refined == int(rec["refined"]), f"refined drift {(b,c,refined)}")
    req(reduction == int(rec["reduction"]), f"reduction drift {(b,c,reduction)}")

    return {
        "b":b,"c":c,"a_interval":[3,amax],
        "H_unequal_support7_tuples":htotal,
        "H_histogram_bins":len(hh),
        "H_histogram_stream_sha256":rec["Hsha"],
        "per_a_stream_sha256":rec["Asha"],
        "current_hpadj22_survivors":current,
        "zero_center_survivors":refined,
        "exact_survivor_reduction":reduction,
        "x4_interval":[int(xr[0]),int(xr[1])],
        "by_a":by_a,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--output",type=Path)
    args = ap.parse_args()

    req(PARENT.is_file() and blob(PARENT)==PARENT_BLOB,"all-a parent drift")
    req(SINGLE.is_file() and blob(SINGLE)==SINGLE_BLOB,"single-witness parent drift")
    p = load_module(PARENT,"stage32_178_hpadj22_top8_parent")
    single = load_module(SINGLE,"stage32_178_hpadj22_top8_single")
    direct_path = args.repo_root / single.DIRECT_REL
    req(direct_path.is_file() and blob(direct_path)==single.DIRECT_BLOB,"current direct source drift")
    direct = load_module(direct_path,"stage32_178_hpadj22_top8_direct")
    old = direct.load_old(args.source_root)

    bc = old.load_bchunk()
    bnd = bc.load_bound()
    h21 = bnd.load_module(bnd.H21,bnd.H21_BLOB,"stage32_178_top8_h21")
    h20=h21.load_parent(); h19=h20.load_parent(); h18=h19.load_parent(); h17=h18.load_parent(); h16=h17.load_parent()
    p15 = h16.load_module(h16.PARENT,h16.PARENT_BLOB,"stage32_178_top8_h15")
    p14=p15.load_parent(); counter=p14.load_counter()
    manifest=counter.load_locked_json(p14.MANIFEST,p14.LOCKS["manifest_blob"],p14.LOCKS["manifest_canonical"],"FULL178 manifest")
    rows=counter.manifest_rows(manifest)
    row_id,g0,d0=rows[single.ROW_INDEX]
    req((row_id,int(g0),int(d0))==("g1-d192",1,192),"target row identity drift")
    req(bc.QCAP==4992 and bc.OVERFLOW==4993,"qBC cap drift")

    fast=load_module(single.FAST,"stage32_178_hpadj22_top8_fast")
    cert=fast.load_certificate()

    seen=set()
    cells=[]
    for rec in EXPECTED:
        key=(int(rec["b"]),int(rec["c"]))
        req(key not in seen,f"duplicate selected cell {key}")
        seen.add(key)
        cells.append(evaluate_cell(p=p,single=single,direct=direct,old=old,bnd=bnd,h16=h16,p15=p15,counter=counter,fast=fast,cert=cert,rec=rec))

    current=sum(int(x["current_hpadj22_survivors"]) for x in cells)
    refined=sum(int(x["zero_center_survivors"]) for x in cells)
    reduction=sum(int(x["exact_survivor_reduction"]) for x in cells)
    req(current==EXPECTED_CURRENT,"top8 current aggregate drift")
    req(refined==EXPECTED_REFINED,"top8 refined aggregate drift")
    req(reduction==EXPECTED_REDUCTION and current-refined==reduction,"top8 reduction aggregate drift")
    candidate=single.OLD_GLOBAL-reduction
    req(candidate==EXPECTED_CANDIDATE,"candidate global bound drift")

    out={
        "schema":"STAGE32_32_01_178_HPADJ22_E192_ZERO_CENTER_TOP8_BC_CELLS_V1",
        "status":"EXACT_CURRENT_HPADJ22_TOP8_DISJOINT_BC_CELL_REFINEMENT__ZERO_MAIN_CREDIT__HOSTILE_AUDIT_REQUIRED",
        "source_locks":{
            "all_a_parent_blob_sha1":PARENT_BLOB,
            "single_witness_parent_blob_sha1":SINGLE_BLOB,
            "current_direct_count_blob_sha1":single.DIRECT_BLOB,
            "hpadj22_source_head":single.HPADJ22_SOURCE_HEAD,
            "historical_hpadj22_worker_blob_sha1":direct.OLD_BLOB,
            "zero_center_picard_source_blob_sha1":single.FAST_BLOB,
        },
        "target":{
            "row_index":single.ROW_INDEX,"row_id":row_id,"g":1,"d":192,"e":192,
            "selected_bc_cells":[[int(x["b"]),int(x["c"])] for x in EXPECTED],
            "A_support":3,"H_support":7,"canonical_H_branch":"x0<x1",
        },
        "aggregate":{
            "selected_bc_cell_count":len(cells),
            "current_hpadj22_survivors":current,
            "zero_center_survivors":refined,
            "exact_survivor_reduction":reduction,
            "current_v45_global_upper_bound":str(single.OLD_GLOBAL),
            "candidate_global_upper_bound_if_promoted":str(candidate),
        },
        "cells":cells,
        "semantics":{
            "same_current_hpadj22_population":True,
            "bc_cells_pairwise_disjoint":True,
            "all_a_families_within_each_bc_cell_pairwise_disjoint":True,
            "canonical_unequal_H_coordinates_replayed_exactly":True,
            "all_A_support3_ordered_triples_replayed_exactly":True,
            "e192_current_eligibility_replayed_for_every_a":True,
            "residual_simplex_caps_proved_for_every_a":True,
            "zero_center_picard_closed_form_replayed_for_every_a_and_t":True,
            "hpadj22_qcap_survival_equivalence_used_only_below_exact_cutoff":True,
            "current_x4_survivor_adapter_crosschecked":True,
            "no_additive_cross_route_subtraction":True,
            "candidate_is_direct_same_population_upper_bound_refinement":True,
            "all_nonselected_current_hpadj22_survivors_left_unchanged":True,
            "main_bound_replacement_performed":False,
            "hostile_audit_required_before_consumption":True,
        },
        "firewalls":{
            "main_credit_changed":False,"full178_complete":False,
            "theorem_credit_changed":False,"effectivity_credit_changed":False,
            "receiver_credit_changed":False,"route_credit_changed":False,
            "endpoint_credit_changed":False,"stage32_closed":False,"merge":False,
        },
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    if args.output is not None:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("HPADJ22_E192_ZERO_CENTER_TOP8="+json.dumps({
        "cells":len(cells),"current":current,"refined":refined,"reduction":reduction,
        "old_global":str(single.OLD_GLOBAL),"candidate_global":str(candidate),
        "canonical":out["canonical_sha256_without_this_field"],
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
