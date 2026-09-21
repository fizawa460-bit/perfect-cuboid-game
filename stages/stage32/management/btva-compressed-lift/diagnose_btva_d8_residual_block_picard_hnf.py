#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter, defaultdict
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
R2_RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-TIMEOUT-RESCUE-ROUND2-RETAINED.json"
R2_RETAINED_BLOB = "4330fde6607c5119806ed114b45362e9790dc247"
R2_RETAINED_CANON = "ae647aaecf768b74df2fb7be881ff7220867acc6700f9f8cae38dbdb7ff4e2fe"
STATIC_RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-STATIC7-PICARD-HNF-RETAINED.json"
STATIC_RETAINED_BLOB = "5fae19f1aec2eff43e47aea137f512d0a87a11e1"
STATIC_RETAINED_CANON = "a3ad76fb31a47ebabe0a820673ba0d3c8291384b6522163cfb7a98320031592c"
LANE_AGG_REL = Path("stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_aggregate_picard_lattice_preflight.py")
LANE_AGG_BLOB = "5fa9f1d67d6411cb550230b62398aff7bd6488ff"
LANE_HEAD = "e60f03cf5105bc6e26cb4615acabd6fe0c07625c"

DEGREE = 8
EXCEPTIONAL_MASS = 8
X4_VALUES = 113
FULL_OBSERVABLE_ORDER = ("a","b","c","t","x4","e","d","r0","r1","r2","r3","r4")


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def load_canonical(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path)==expected_blob,path.name+" blob drift")
    obj=json.loads(path.read_text(encoding="utf-8"))
    stored=obj.get("canonical_sha256_without_this_field")
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    req(stored==expected_canon and csha(body)==expected_canon,path.name+" canonical drift")
    return obj


def comps_at_most(total: int, parts: int):
    cur=[0]*parts
    def rec(pos: int, rem: int):
        if pos==parts:
            yield tuple(cur)
            return
        for v in range(rem+1):
            cur[pos]=v
            yield from rec(pos+1,rem-v)
    yield from rec(0,total)


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--lane178-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()

    full_ret=load_canonical(FULL_RETAINED,FULL_RETAINED_BLOB,FULL_RETAINED_CANON)
    r1=load_canonical(R1_RETAINED,R1_RETAINED_BLOB,R1_RETAINED_CANON)
    r2=load_canonical(R2_RETAINED,R2_RETAINED_BLOB,R2_RETAINED_CANON)
    static=load_canonical(STATIC_RETAINED,STATIC_RETAINED_BLOB,STATIC_RETAINED_CANON)
    req(full_ret["target"]["row_id"]=="g0-d008","full retained row")
    req(full_ret["result"]["survivor_terminal_mass"]==248374,"full survivor mass")
    req(r1["result"]["candidate_d8_survivor_terminal_mass_after_rescue"]==231424,"R1 survivor mass")
    req(r2["result"]["candidate_d8_survivor_terminal_mass_after_round2"]==231424,"R2 survivor mass")
    req(static["result"]["candidate_d8_survivor_terminal_mass_after_static_picard_hnf"]==231424,"static HNF survivor mass")

    req(blob(FULL_WORKER)==FULL_WORKER_BLOB,"full343 worker drift")
    full=load_module(FULL_WORKER,"stage32_main_btva_residual_hnf_full_worker")
    req(full.PARENT.is_file() and full.blob(full.PARENT)==full.PARENT_BLOB,"full343 parent drift")
    parent=full.load_module(full.PARENT,"stage32_main_btva_residual_hnf_parent")
    old=parent.load_module(parent.RELAXED,"stage32_main_btva_residual_hnf_relaxed")
    req(old.LANE178_HEAD==LANE_HEAD,"lane178 head identity drift")
    req(old.LANE178_AGG_BLOB==LANE_AGG_BLOB,"lane178 aggregate identity drift")

    lane_script=(args.lane178_root / LANE_AGG_REL).resolve()
    req(lane_script.is_file() and blob(lane_script)==LANE_AGG_BLOB,"lane178 aggregate script drift")
    proc=subprocess.run([sys.executable,str(lane_script)],cwd=lane_script.parent,check=True,capture_output=True,text=True)
    payload=json.loads(proc.stdout)
    req(payload["rule_is_exact_for_linear_picard_lattice_extendability"] is True,"lane Picard exactness lost")
    cert=payload["full_observable_image_lattice"]
    req(tuple(cert["observable_order"])==FULL_OBSERVABLE_ORDER,"full observable order drift")
    req(int(cert["rank"])==12,"full observable rank drift")
    q=int(cert["membership_modulus"])
    coeffs=[[int(v)%q if q>1 else 0 for v in row] for row in cert["membership_coefficients_mod_q"]]
    req(int(cert["active_congruence_rows"])==len(coeffs),"congruence row count drift")
    for row in coeffs:
        req(len(row)==12,"congruence row width")

    residual_supports=[tuple(int(x) for x in xs) for xs in payload["residual_supports_exceptional_labels_1based"]]
    req(len(residual_supports)==5 and all(residual_supports),"residual support count")
    observed={int(x) for x in old.ASSIGNMENT if int(x)>=93}
    universe=set(range(93,141))
    seen=set(observed)
    for support in residual_supports:
        req(not (seen & set(support)),"residual supports overlap observed/prior")
        seen.update(support)
    remainder=tuple(sorted(universe-seen))
    req(remainder,"implicit residual block is empty")
    req(seen | set(remainder)==universe,"exceptional block partition incomplete")

    syndrome_sets={}
    for slack in range(EXCEPTIONAL_MASS+1):
        vals=set()
        for r in comps_at_most(slack,5):
            if q==1 or not coeffs:
                syn=tuple(0 for _ in coeffs)
            else:
                syn=tuple(sum(row[7+j]*r[j] for j in range(5))%q for row in coeffs)
            vals.add(syn)
        syndrome_sets[slack]=vals

    v1=old.load_module(old.BASE,"stage32_main_btva_residual_hnf_base")
    indexer=v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS,DEGREE)
    req(indexer.normal_budget==112 and indexer.normal_budget+1==X4_VALUES,"x4 budget drift")
    counts: Counter[tuple[int,int,int,int]]=Counter()
    stride=X4_VALUES
    for erank in range(int(indexer.exceptional_count)):
        x=tuple(int(v) for v in indexer.unrank(erank*stride))
        req(x[4]==0,"x4 stride replay")
        counts[tuple(old.static_from_terminal(x)[:4])]+=1
    keys=sorted(counts)
    req(len(keys)==343,"base4 population drift")
    key_to_index={k:i for i,k in enumerate(keys)}

    original_survivors={int(i):int(m) for i,m in full_ret["result"]["survivor_index_mass_pairs"]}
    removed_r1=set(int(i) for i in r1["result"]["rescued_unsat_indices_0based"])
    survivors={i:m for i,m in original_survivors.items() if i not in removed_r1}
    req(len(survivors)==86 and sum(survivors.values())==231424,"current survivor reconstruction")

    groups=Counter()
    for erank in range(int(indexer.exceptional_count)):
        terminal=tuple(int(v) for v in indexer.unrank(erank*stride))
        base4=tuple(old.static_from_terminal(terminal)[:4])
        idx=key_to_index[base4]
        if idx not in survivors:
            continue
        observed_mass=sum(terminal[i] for i in range(11) if i!=4)
        req(0<=observed_mass<=EXCEPTIONAL_MASS,"observed exceptional mass")
        slack=EXCEPTIONAL_MASS-observed_mass
        groups[(idx,slack)]+=1

    req(sum(mult*X4_VALUES for mult in groups.values())==231424,"grouped source mass drift")
    for idx,mass in survivors.items():
        req(sum(mult for (i,_),mult in groups.items() if i==idx)*X4_VALUES==mass,f"base4 grouped mass {idx}")

    group_rows=[]
    allowed_total=0
    removed_total=0
    zero_groups=0
    partial_groups=0
    slack_source=defaultdict(int)
    slack_allowed=defaultdict(int)

    for (idx,slack),mult in sorted(groups.items()):
        base4=keys[idx]
        allowed=[]
        for x4 in range(X4_VALUES):
            static7=tuple(base4)+(x4,EXCEPTIONAL_MASS,DEGREE)
            if q==1 or not coeffs:
                target=tuple(0 for _ in coeffs)
            else:
                target=tuple((-sum(row[j]*static7[j] for j in range(7)))%q for row in coeffs)
            if target in syndrome_sets[slack]:
                allowed.append(x4)
        source_mass=mult*X4_VALUES
        allowed_mass=mult*len(allowed)
        removed=source_mass-allowed_mass
        allowed_total+=allowed_mass
        removed_total+=removed
        slack_source[slack]+=source_mass
        slack_allowed[slack]+=allowed_mass
        if not allowed:
            zero_groups+=1
        elif len(allowed)<X4_VALUES:
            partial_groups+=1
        group_rows.append({
            "global_base4_index":idx,
            "base4":list(base4),
            "unobserved_exceptional_mass_slack":slack,
            "prefix_multiplicity":mult,
            "source_terminal_mass":source_mass,
            "allowed_x4_count":len(allowed),
            "allowed_x4_values":allowed,
            "allowed_x4_values_sha256":csha(allowed),
            "allowed_terminal_mass":allowed_mass,
            "removed_terminal_mass":removed,
        })

    req(allowed_total+removed_total==231424,"residual HNF mass conservation")
    out={
      "schema":"STAGE32_MAIN_BTVA_D8_RESIDUAL_BLOCK_PICARD_HNF_DIAGNOSTIC_V1",
      "stage":32,
      "status":"EXACT_RESIDUAL_BLOCK_HNF_FILTER_COMPLETE_ZERO_CREDIT",
      "target":{
        "row_id":"g0-d008",
        "source_survivor_terminal_mass":231424,
        "source_base4_survivor_count":86,
        "x4_values_per_prefix":X4_VALUES,
      },
      "certificate":{
        "lane178_head":LANE_HEAD,
        "aggregate_preflight_blob_sha1":LANE_AGG_BLOB,
        "observable_order":cert["observable_order"],
        "rank":int(cert["rank"]),
        "image_lattice_index_in_Zm":int(cert["image_lattice_index_in_Zm"]),
        "membership_modulus":q,
        "active_congruence_rows":int(cert["active_congruence_rows"]),
        "membership_coefficients_mod_q":cert["membership_coefficients_mod_q"],
        "canonical_sha256_without_this_field":cert["canonical_sha256_without_this_field"],
        "rule_exact_for_linear_picard_lattice_extendability":True,
      },
      "exceptional_partition":{
        "observed_exceptional_labels_1based":sorted(observed),
        "residual_supports_r0_to_r4_1based":[list(x) for x in residual_supports],
        "implicit_remainder_support_1based":list(remainder),
        "r0_to_r4_nonnegative_sum_at_most_slack":True,
        "implicit_remainder_absorbs_unused_slack":True,
      },
      "groups":group_rows,
      "summary":{
        "group_count":len(group_rows),
        "zero_allowed_group_count":zero_groups,
        "partial_allowed_group_count":partial_groups,
        "removed_terminal_mass_by_residual_picard_hnf":removed_total,
        "candidate_d8_survivor_terminal_mass_after_residual_picard_hnf":allowed_total,
        "source_mass_by_slack":{str(k):slack_source[k] for k in sorted(slack_source)},
        "allowed_mass_by_slack":{str(k):slack_allowed[k] for k in sorted(slack_allowed)},
      },
      "semantics":{
        "filter_is_necessary_condition_only":True,
        "residual_block_sums_existentially_quantified":True,
        "each_removed_terminal_has_no_integral_Picard64_class_for_any_nonnegative_r0_to_r4_with_available_slack":True,
        "allowed_terminal_not_claimed_effective":True,
        "composition_with_full343_and_r1_is_set_intersection_not_additive_independence":True,
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
    print("BTVA_D8_RESIDUAL_HNF_SUMMARY="+json.dumps(out["summary"],sort_keys=True))
    print("BTVA_D8_RESIDUAL_HNF_CERT="+json.dumps({
      "modulus":q,"active_rows":cert["active_congruence_rows"],
      "index":cert["image_lattice_index_in_Zm"],"remainder_support_size":len(remainder)
    },sort_keys=True))
    print("BTVA_D8_RESIDUAL_HNF_CANONICAL="+out["canonical_sha256_without_this_field"])


if __name__=="__main__":
    main()
