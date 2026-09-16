#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
PILOT = HERE / "strictness_pilot_bounded_exact.py"
PILOT_BLOB = "266c7eb92fc971df24733f651c245cd14a32e494"
SCHEMA = "STAGE32EX5_HPADJ21_FULL_QA_ROW_CERT_V1"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_pilot():
    req(PILOT.is_file() and git_blob(PILOT) == PILOT_BLOB, "HPADJ21 bounded-pilot blob drift")
    spec = importlib.util.spec_from_file_location("hpadj21_pilot_locked_for_row", PILOT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ21 bounded pilot")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compute_row(row_index: int) -> dict:
    p = load_pilot()
    h20 = p.load_parent(); h19 = h20.load_parent(); h18 = h19.load_parent(); h17 = h18.load_parent(); h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_hpadj21_row")
    p14 = p15.load_parent(); counter = p14.load_counter()
    manifest = counter.load_locked_json(p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest")
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178, "FULL178 row coverage")
    req(0 <= row_index < 178, "row index out of range")
    row_id, g0, d0 = rows[row_index]
    g, d = int(g0), int(d0)
    selected = [(row_id, g, d)]
    cells, BC = p.exact_pilot_cells(p15, p14, counter, selected)
    h = d // 2
    two_profiles, _, _, _ = h20.build_two_tier_profiles(h, counter, h19)
    full_profiles, classes_gt2, tuples_above_second = p.full_profiles(h, counter, h19)

    legacy = 8 if g == 0 else 4
    K = counter.ceil_div(d - 16*g + 16, 4)
    A = [[sum(mult for _, mult in full_profiles[a][sa]) for sa in range(4)] for a in range(h+1)]
    two_caps = {interval: defaultdict(int) for interval in p15.PLANNED}
    full_caps = {interval: defaultdict(int) for interval in p15.PLANNED}

    for b in range(h+1):
        interval = p15.shard_for_b(b)
        for c in range(h+1):
            bcv = BC[b][c]
            if not any(any(pair) for pair in bcv):
                continue
            c3 = counter.component3(d,b,c)
            if c3 < 0:
                continue
            two_surv, _ = h20.survivor_profiles(h16,h19,two_profiles,h,g,b,c)
            exact_surv = p.full_survivors(h16,full_profiles,h,g,b,c)
            for a in range(h+1):
                if not any(A[a]):
                    continue
                M=a+b+c; ca=counter.component_a(d,a)
                if ca < 0:
                    continue
                srem=min(16,d)+ca+c3
                for sbc,pair in enumerate(bcv):
                    for r in (0,1):
                        left=int(pair[r])
                        if not left:
                            continue
                        for sa,right in enumerate(A[a]):
                            if not right:
                                continue
                            ti=two_surv[a][sa]; fi=exact_surv[a][sa]
                            req(ti is not None and fi is not None, "missing q profile")
                            req(sum(x[2] for x in ti["tiers"]) == int(right), "two-tier population drift")
                            req(sum(x[2] for x in fi["tiers"]) == int(right), "full-hist population drift")
                            support=sbc+sa; qneed=K-support
                            if qneed>0 and srem<qneed:
                                continue
                            lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed)); upper=min((19*d)//5,3*d,3*d-(b-c))
                            if lower>upper:
                                continue
                            excluded=set(); e_n358=3*d-(b-c)
                            if b<=h-5 and support+srem==K and e_n358-M>=srem:
                                excluded.add(e_n358)
                            if g==1 and d==8:
                                excluded.add(8)
                            lo=lower if lower%2==0 else lower+1; hi=upper if upper%2==0 else upper-1
                            for e in range(lo,hi+1,2):
                                if e in excluded:
                                    continue
                                B=19*d-5*e+1
                                req(B>0 and B%2==1, f"normal block drift {(g,d,e,B)}")
                                for s0,s1,mult in ti["tiers"]:
                                    two_caps[interval][((s0 if r==0 else s1),B)] += left*int(mult)*B
                                for s0,s1,mult in fi["tiers"]:
                                    full_caps[interval][((s0 if r==0 else s1),B)] += left*int(mult)*B

    two_total=Fraction(0,1); full_total=Fraction(0,1)
    two_floor=full_floor=pre_total=post_total=strict_cells=0
    records=[]
    for interval_pos, interval in enumerate(p15.PLANNED):
        key=(interval,g,d); info=cells[key]; P=int(info["pre_mass"]); Mpost=int(info["post_mass"])
        req(sum(two_caps[interval].values())==P, f"two-tier pre-mass mismatch {key}")
        req(sum(full_caps[interval].values())==P, f"full-hist pre-mass mismatch {key}")
        tobj,_,_,_=h18.optimize_cell_exact_predomain(two_caps[interval],Mpost)
        fobj,_,_,_=h18.optimize_cell_exact_predomain(full_caps[interval],Mpost)
        req(fobj<=tobj, f"full histogram weakened HPADJ20 {key}")
        strict = fobj<tobj
        strict_cells += int(strict)
        two_total += tobj; full_total += fobj
        tf=tobj.numerator//tobj.denominator; ff=fobj.numerator//fobj.denominator
        req(ff<=tf, "cell floor weakened HPADJ20")
        two_floor += tf; full_floor += ff; pre_total += P; post_total += Mpost
        records.append({"interval_position":interval_pos,"b_interval":list(interval),"pre_mass":P,"post_mass":Mpost,"hpadj20_num":tobj.numerator,"hpadj20_den":tobj.denominator,"hpadj20_floor":tf,"hpadj21_num":fobj.numerator,"hpadj21_den":fobj.denominator,"hpadj21_floor":ff,"strict":strict})

    req(full_total<=two_total and full_floor<=two_floor, "row aggregate weakened HPADJ20")
    out={
      "schema":SCHEMA,"route_id":"HPADJ-21_ex5","status":"EXACT_FULL_QA_ROW_COMPLETE_HOSTILE_AUDIT_REQUIRED",
      "row":{"index":row_index,"row_id":row_id,"g":g,"d":d},
      "source_locks":{"bounded_pilot_git_blob":PILOT_BLOB,"hpadj20_parent_git_blob":p.PARENT_BLOB,"full178_manifest_blob_sha1":p14.LOCKS["manifest_blob"],"hpadj10_counter_blob_sha1":p14.LOCKS["hpadj10_counter_blob"]},
      "profile":{"classes_with_more_than_two_qA_bins":classes_gt2,"tuples_above_second_qA_level":tuples_above_second,"exact_qA_multiplicity_preserved":True},
      "totals":{"pre_mass":pre_total,"post_mass":post_total,"hpadj20_rational_num":two_total.numerator,"hpadj20_rational_den":two_total.denominator,"hpadj21_rational_num":full_total.numerator,"hpadj21_rational_den":full_total.denominator,"hpadj20_cellwise_floor_sum":two_floor,"hpadj21_cellwise_floor_sum":full_floor,"strict_cell_count":strict_cells,"floor_improvement":two_floor-full_floor},
      "cell_records":records,
      "semantics":{"same_population_as_hpadj20":True,"same_post_mass_constraints_as_hpadj20":True,"full_qA_histogram_exact_multiplicity":True,"additive_subtraction_used":False,"statistical_independence_assumed":False},
      "credit_firewall":{"partial_output_credit":False,"stage32_main_credit":False,"full178_completion_credit":False,"theorem_credit":False,"effectivity_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_credit":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canonical(out)
    return out


def validate(path: Path, row_index: int) -> dict:
    req(path.is_file(), "missing row certificate")
    d=json.loads(path.read_text())
    req(d.get("schema")==SCHEMA, "row schema drift")
    req(int(d.get("row",{}).get("index",-1))==row_index, "row index drift")
    req(d.get("source_locks",{}).get("bounded_pilot_git_blob")==PILOT_BLOB, "pilot source lock drift")
    req(d.get("canonical_sha256_without_this_field")==canonical(d), "row canonical drift")
    f=d.get("credit_firewall",{})
    req(f.get("partial_output_credit") is False and f.get("stage32_main_credit") is False and f.get("full178_completion_credit") is False, "row credit firewall drift")
    return d


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--row-index",type=int,required=True); ap.add_argument("--output",type=Path); ap.add_argument("--verify-existing",type=Path)
    args=ap.parse_args()
    if args.verify_existing is not None:
        d=validate(args.verify_existing,args.row_index); print("VALID_HPADJ21_ROW="+d["canonical_sha256_without_this_field"]); return
    req(args.output is not None, "--output required")
    d=compute_row(args.row_index); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(d,sort_keys=True,separators=(",",":"))+"\n")
    print(json.dumps({"row_index":args.row_index,"row_id":d["row"]["row_id"],"d":d["row"]["d"],"strict_cells":d["totals"]["strict_cell_count"],"floor_improvement":d["totals"]["floor_improvement"],"canonical":d["canonical_sha256_without_this_field"],"bytes":args.output.stat().st_size},sort_keys=True))


if __name__=="__main__": main()
