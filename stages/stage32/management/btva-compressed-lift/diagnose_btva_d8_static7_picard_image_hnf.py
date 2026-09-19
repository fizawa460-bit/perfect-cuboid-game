#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FULL_WORKER = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_base4_full343_shard.py"
FULL_WORKER_BLOB = "63321a54f565b2da38efbef756caf8db148f0063"
FULL_RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-FULL343-RETAINED-CHECKPOINT.json"
FULL_RETAINED_BLOB = "4ae970e17b0d7168f6d2ffd0644195f2ab57ae8d"
FULL_RETAINED_CANON = "5e111a460381d9df7662b7f552eadde68953ecee304cf7a47d4aa52d2a9ba776"
R1_RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-TIMEOUT-RESCUE-TOP16-RETAINED.json"
R1_RETAINED_BLOB = "e1c4b0e04fa7f291cdbb42b3aafd62c869f47220"
R1_RETAINED_CANON = "99b0294b87df9d6b41e52b186af0b079eda5c3f37f5d94fc215aca7d435b2ad4"
LANE_AGG_REL = Path("stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_aggregate_picard_lattice_preflight.py")
LANE_AGG_BLOB = "5fa9f1d67d6411cb550230b62398aff7bd6488ff"
LANE_HEAD = "e60f03cf5105bc6e26cb4615acabd6fe0c07625c"
RERUN_GENERATION = 2

DEGREE = 8
EXCEPTIONAL_MASS = 8
X4_VALUES = 113

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()

def load_module(path: Path, name: str):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

def load_canonical(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path)==expected_blob, path.name+" blob drift")
    obj=json.loads(path.read_text(encoding="utf-8"))
    stored=obj.get("canonical_sha256_without_this_field")
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    req(stored==expected_canon and csha(body)==expected_canon, path.name+" canonical drift")
    return obj

def member(cert: dict, values: tuple[int,...]) -> bool:
    q=int(cert["membership_modulus"])
    req(q>=1,"invalid membership modulus")
    rows=cert["membership_coefficients_mod_q"]
    if q==1 or not rows:
        return True
    for row in rows:
        req(len(row)==len(values),"membership row width")
        if sum(int(c)*int(v) for c,v in zip(row,values)) % q:
            return False
    return True

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--lane178-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()

    full_ret=load_canonical(FULL_RETAINED,FULL_RETAINED_BLOB,FULL_RETAINED_CANON)
    r1=load_canonical(R1_RETAINED,R1_RETAINED_BLOB,R1_RETAINED_CANON)
    req(full_ret["target"]["row_id"]=="g0-d008","full retained row")
    req(full_ret["result"]["survivor_terminal_mass"]==248374,"full retained survivor mass")
    req(r1["result"]["candidate_d8_survivor_terminal_mass_after_rescue"]==231424,"R1 survivor mass")

    req(blob(FULL_WORKER)==FULL_WORKER_BLOB,"full343 worker drift")
    full=load_module(FULL_WORKER,"stage32_main_btva_static_hnf_full_worker")
    req(full.PARENT.is_file() and full.blob(full.PARENT)==full.PARENT_BLOB,"full343 parent drift")
    parent=full.load_module(full.PARENT,"stage32_main_btva_static_hnf_parent")
    old=parent.load_module(parent.RELAXED,"stage32_main_btva_static_hnf_relaxed")
    req(old.LANE178_HEAD==LANE_HEAD,"lane178 head identity drift")
    req(old.LANE178_AGG_BLOB==LANE_AGG_BLOB,"lane178 aggregate identity drift")

    lane_script=(args.lane178_root / LANE_AGG_REL).resolve()
    req(lane_script.is_file() and blob(lane_script)==LANE_AGG_BLOB,"lane178 aggregate script drift")
    proc=subprocess.run(
        [sys.executable,str(lane_script)],
        cwd=lane_script.parent,
        check=True,capture_output=True,text=True,
    )
    payload=json.loads(proc.stdout)
    req(payload["rule_is_exact_for_linear_picard_lattice_extendability"] is True,"lane Picard rule lost exactness")
    profiles=payload["prefix_image_lattice_profiles"]
    certs=[p for p in profiles if tuple(p["observable_order"])==("a","b","c","t","x4","e","d")]
    req(len(certs)==1,"missing unique 7-observable Picard certificate")
    cert=certs[0]

    v1=old.load_module(old.BASE,"stage32_main_btva_static_hnf_base")
    indexer=v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS,DEGREE)
    req(indexer.normal_budget==112,"normal budget drift")
    counts: Counter[tuple[int,int,int,int]]=Counter()
    stride=X4_VALUES
    for erank in range(int(indexer.exceptional_count)):
        x=tuple(int(v) for v in indexer.unrank(erank*stride))
        req(x[4]==0,"x4 stride replay")
        counts[tuple(old.static_from_terminal(x)[:4])]+=1
    keys=sorted(counts)
    req(len(keys)==343,"base4 key count drift")
    req(sum(int(counts[k])*X4_VALUES for k in keys)==1278934,"terminal mass drift")

    original_survivors={int(i):int(m) for i,m in full_ret["result"]["survivor_index_mass_pairs"]}
    r1_unsat=set(int(i) for i in r1["result"]["rescued_unsat_indices_0based"])
    current_survivors={i:m for i,m in original_survivors.items() if i not in r1_unsat}
    req(sum(current_survivors.values())==231424,"R1 survivor reconstruction")

    rows=[]
    total_allowed_mass=0
    total_removed_mass=0
    zero_x4=[]
    partial=[]
    for i,mass in sorted(current_survivors.items()):
        base4=keys[i]
        multiplicity=int(counts[base4])
        req(multiplicity*X4_VALUES==mass,f"mass reconstruction {i}")
        allowed=[x4 for x4 in range(X4_VALUES) if member(cert,tuple(base4)+(x4,EXCEPTIONAL_MASS,DEGREE))]
        allowed_mass=multiplicity*len(allowed)
        removed=mass-allowed_mass
        req(0<=allowed_mass<=mass,"allowed mass range")
        total_allowed_mass+=allowed_mass
        total_removed_mass+=removed
        if not allowed:
            zero_x4.append(i)
        elif len(allowed)<X4_VALUES:
            partial.append(i)
        rows.append({
            "global_base4_index":i,
            "base4":list(base4),
            "exceptional_multiplicity_per_x4":multiplicity,
            "source_terminal_mass":mass,
            "allowed_x4_count":len(allowed),
            "allowed_x4_values":allowed,
            "allowed_terminal_mass":allowed_mass,
            "removed_terminal_mass":removed,
        })

    req(total_allowed_mass+total_removed_mass==231424,"static HNF mass conservation")
    out={
      "schema":"STAGE32_MAIN_BTVA_D8_STATIC7_PICARD_IMAGE_HNF_DIAGNOSTIC_V1",
      "stage":32,
      "status":"EXACT_STATIC7_PICARD_IMAGE_FILTER_COMPLETE_ZERO_CREDIT",
      "target":{"row_id":"g0-d008","source_after_r1_survivor_terminal_mass":231424,"source_base4_survivor_count":len(current_survivors),"x4_values_per_base4":X4_VALUES},
      "certificate":{
        "lane178_head":LANE_HEAD,
        "aggregate_preflight_blob_sha1":LANE_AGG_BLOB,
        "observable_order":cert["observable_order"],
        "rank":int(cert["rank"]),
        "image_lattice_index_in_Zm":int(cert["image_lattice_index_in_Zm"]),
        "membership_modulus":int(cert["membership_modulus"]),
        "active_congruence_rows":int(cert["active_congruence_rows"]),
        "membership_coefficients_mod_q":cert["membership_coefficients_mod_q"],
        "canonical_sha256_without_this_field":cert["canonical_sha256_without_this_field"],
        "rule_exact_for_linear_picard_lattice_extendability":True,
      },
      "rows":rows,
      "summary":{
        "zero_allowed_x4_base4_count":len(zero_x4),
        "zero_allowed_x4_base4_indices":zero_x4,
        "partial_allowed_x4_base4_count":len(partial),
        "partial_allowed_x4_base4_indices":partial,
        "removed_terminal_mass_by_static_picard_hnf":total_removed_mass,
        "candidate_d8_survivor_terminal_mass_after_static_picard_hnf":total_allowed_mass,
      },
      "semantics":{
        "filter_is_necessary_condition_only":True,
        "each_removed_x4_has_no_integral_Picard64_class_with_same_a_b_c_t_x4_e_d":True,
        "allowed_x4_not_claimed_effective":True,
        "composition_with_r1_is_set_intersection_not_additive_independence":True,
      },
      "firewalls":{
        "main_pruning_credit":False,"receiver_credit":False,"effectivity_credit":False,
        "theorem_credit":False,"endpoint_credit":False,"full178_complete":False,
        "stage32_closed":False,"merge_authorized":False,
      },
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("BTVA_D8_STATIC_HNF_SUMMARY="+json.dumps(out["summary"],sort_keys=True))
    print("BTVA_D8_STATIC_HNF_CERT="+json.dumps({
      "modulus":cert["membership_modulus"],
      "active_rows":cert["active_congruence_rows"],
      "index":cert["image_lattice_index_in_Zm"],
    },sort_keys=True))
    print("BTVA_D8_STATIC_HNF_CANONICAL="+out["canonical_sha256_without_this_field"])

if __name__=="__main__":
    main()
