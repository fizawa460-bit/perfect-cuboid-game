#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOP8 = HERE / "verify_hpadj22_e192_zero_center_top8_bc_cells.py"
TOP8_BLOB = "ea6d2b3f870afe28aa27ea3c813ae16670c0bbcc"

EXTRA = (
    {"b":50,"c":49,"amax":55,"H":6038604,"Hbins":65564,"Hsha":"0f06b878a43d6f7fbc4d34d0b8dbd0cdabdcd8a1c4e4344e5b4110f14aab8b22","Asha":"000491d51e03ff66c8bfb42c95dc7f245e29c0f5b1675b9d1b5a21b78656a450","current":7152696346801,"refined":3290472468631,"reduction":3862223878170},
    {"b":49,"c":50,"amax":55,"H":6038604,"Hbins":64954,"Hsha":"67e23667bcb3e0f4d887e79b8b2b88a81ce5d3db233bac73764bb5ba70118e3b","Asha":"3d8798cd6532499e1270dcf524dd25d4d2dd27443d1555c0c44f4cfa16163166","current":7166108692436,"refined":3302780800332,"reduction":3863327892104},
    {"b":50,"c":47,"amax":57,"H":5412176,"Hbins":61324,"Hsha":"0434cbeaf950b571936f55e0ad462048ec2f9298ed7b8299091160c12c1953d1","Asha":"b1b71bce274d8215f23f886e4c774d996f9bafb13574552c4f011f460a70d30c","current":7162336087130,"refined":3320441534983,"reduction":3841894552147},
    {"b":47,"c":50,"amax":57,"H":5412176,"Hbins":61406,"Hsha":"a71577cc5fc5b53b32901a872ca7cd9c22c271b47377c65b103725ea20bdfcf4","Asha":"8e0917f61163d458e0777b01d8f339078a9d27dd26a75e93f7b1500fab10eb93","current":7207321677520,"refined":3357621509402,"reduction":3849700168118},
    {"b":48,"c":47,"amax":59,"H":4869491,"Hbins":57097,"Hsha":"264e9b2e3edd4fe177cd62ab4834790b5acebe6a3f25ddd6058ac2a897d59494","Asha":"f5fa9d02fd398dc76117560358141074c942c58939f5ff3da497b0f7ae0a27aa","current":7201024461714,"refined":3373499979586,"reduction":3827524482128},
    {"b":47,"c":48,"amax":59,"H":4869491,"Hbins":56388,"Hsha":"56ba73eefcd9c9e9db7b157b2f03e2731383178dd46824166466ae4735e641c3","Asha":"31c3ce8ea26e369002c49cba884a3e02e125e5dae3c61cf3ccb88bc1160120b6","current":7214474973850,"refined":3385274414010,"reduction":3829200559840},
    {"b":51,"c":48,"amax":55,"H":6020779,"Hbins":65529,"Hsha":"4b775b0b060a85986b595d27fde3a3f42fdae08cbb410c905f6b1bf38feef9a2","Asha":"8d76a61f235e3a40a1e12392ca51d42988931123a566715e92c5ed8ef70a9b75","current":7111594276254,"refined":3266008764129,"reduction":3845585512125},
    {"b":48,"c":51,"amax":55,"H":6020779,"Hbins":65862,"Hsha":"cc515c8cb554c0d61a4a483945122af8d6e3907258864b593632604f5b5b1ea0","Asha":"a5c1527c232d643b03a4aee25b04b1867e8a16aacd5b0582d7004777cf17892f","current":7161623306615,"refined":3304993485258,"reduction":3856629821357},
)

EXPECTED_CURRENT = 114976575390540
EXPECTED_REFINED = 53376231417921
EXPECTED_REDUCTION = 61600343972619
EXPECTED_CANDIDATE = 138652678200306620875


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None:
        raise SystemExit("FAIL: cannot load "+str(path))
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()

    # Lock the already self-audited top8 implementation before importing it.
    raw=TOP8.read_bytes()
    import hashlib
    got=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    if got != TOP8_BLOB:
        raise SystemExit("FAIL: top8 verifier source drift")
    top8=load(TOP8,"stage32_178_hpadj22_top16_top8")

    if not top8.PARENT.is_file() or top8.blob(top8.PARENT) != top8.PARENT_BLOB:
        raise SystemExit("FAIL: all-a parent drift")
    if not top8.SINGLE.is_file() or top8.blob(top8.SINGLE) != top8.SINGLE_BLOB:
        raise SystemExit("FAIL: single-witness parent drift")
    p=top8.load_module(top8.PARENT,"stage32_178_hpadj22_top16_parent")
    single=top8.load_module(top8.SINGLE,"stage32_178_hpadj22_top16_single")

    direct_path=args.repo_root/single.DIRECT_REL
    if not direct_path.is_file() or top8.blob(direct_path)!=single.DIRECT_BLOB:
        raise SystemExit("FAIL: current direct source drift")
    direct=top8.load_module(direct_path,"stage32_178_hpadj22_top16_direct")
    old=direct.load_old(args.source_root)

    bc=old.load_bchunk()
    bnd=bc.load_bound()
    h21=bnd.load_module(bnd.H21,bnd.H21_BLOB,"stage32_178_top16_h21")
    h20=h21.load_parent(); h19=h20.load_parent(); h18=h19.load_parent(); h17=h18.load_parent(); h16=h17.load_parent()
    p15=h16.load_module(h16.PARENT,h16.PARENT_BLOB,"stage32_178_top16_h15")
    p14=p15.load_parent(); counter=p14.load_counter()
    manifest=counter.load_locked_json(p14.MANIFEST,p14.LOCKS["manifest_blob"],p14.LOCKS["manifest_canonical"],"FULL178 manifest")
    rows=counter.manifest_rows(manifest)
    row_id,g0,d0=rows[single.ROW_INDEX]
    if (row_id,int(g0),int(d0)) != ("g1-d192",1,192):
        raise SystemExit("FAIL: target row identity drift")
    if not (bc.QCAP==4992 and bc.OVERFLOW==4993):
        raise SystemExit("FAIL: qBC cap drift")

    fast=top8.load_module(single.FAST,"stage32_178_hpadj22_top16_fast")
    cert=fast.load_certificate()

    expected=tuple(top8.EXPECTED)+EXTRA
    seen=set()
    cells=[]
    for rec in expected:
        key=(int(rec["b"]),int(rec["c"]))
        if key in seen:
            raise SystemExit("FAIL: duplicate selected bc cell")
        seen.add(key)
        cells.append(top8.evaluate_cell(
            p=p,single=single,direct=direct,old=old,bnd=bnd,h16=h16,p15=p15,
            counter=counter,fast=fast,cert=cert,rec=rec
        ))

    current=sum(int(x["current_hpadj22_survivors"]) for x in cells)
    refined=sum(int(x["zero_center_survivors"]) for x in cells)
    reduction=sum(int(x["exact_survivor_reduction"]) for x in cells)
    if current != EXPECTED_CURRENT:
        raise SystemExit(f"FAIL: top16 current aggregate drift {current}")
    if refined != EXPECTED_REFINED:
        raise SystemExit(f"FAIL: top16 refined aggregate drift {refined}")
    if reduction != EXPECTED_REDUCTION or current-refined != reduction:
        raise SystemExit(f"FAIL: top16 reduction aggregate drift {reduction}")

    candidate=single.OLD_GLOBAL-reduction
    if candidate != EXPECTED_CANDIDATE:
        raise SystemExit(f"FAIL: candidate global bound drift {candidate}")

    out={
        "schema":"STAGE32_32_01_178_HPADJ22_E192_ZERO_CENTER_TOP16_BC_CELLS_V1",
        "status":"EXACT_CURRENT_HPADJ22_TOP16_DISJOINT_BC_CELL_REFINEMENT__ZERO_MAIN_CREDIT__HOSTILE_AUDIT_REQUIRED",
        "source_locks":{
            "top8_verifier_blob_sha1":TOP8_BLOB,
            "all_a_parent_blob_sha1":top8.PARENT_BLOB,
            "single_witness_parent_blob_sha1":top8.SINGLE_BLOB,
            "current_direct_count_blob_sha1":single.DIRECT_BLOB,
            "hpadj22_source_head":single.HPADJ22_SOURCE_HEAD,
            "historical_hpadj22_worker_blob_sha1":direct.OLD_BLOB,
            "zero_center_picard_source_blob_sha1":single.FAST_BLOB,
        },
        "target":{
            "row_index":single.ROW_INDEX,"row_id":row_id,"g":1,"d":192,"e":192,
            "selected_bc_cells":[[int(x["b"]),int(x["c"])] for x in expected],
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
    out["canonical_sha256_without_this_field"]=top8.canon(out)
    if args.output is not None:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("HPADJ22_E192_ZERO_CENTER_TOP16="+json.dumps({
        "cells":len(cells),"current":current,"refined":refined,"reduction":reduction,
        "old_global":str(single.OLD_GLOBAL),"candidate_global":str(candidate),
        "canonical":out["canonical_sha256_without_this_field"],
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
