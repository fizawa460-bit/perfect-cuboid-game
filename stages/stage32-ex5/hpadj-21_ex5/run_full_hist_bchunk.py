#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, importlib.util, json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIRECT = HERE / "run_full_hist_row.py"
DIRECT_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
SCHEMA = "STAGE32EX5_HPADJ21_FULL_QA_BCHUNK_CERT_V1"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj); body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_direct():
    req(DIRECT.is_file() and git_blob(DIRECT) == DIRECT_BLOB, "direct worker drift")
    spec = importlib.util.spec_from_file_location("hpadj21_direct_for_bchunk", DIRECT)
    req(spec is not None and spec.loader is not None, "cannot load direct worker")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def enc(caps):
    return [[int(s), int(B), int(m)] for (s, B), m in sorted(caps.items()) if int(m)]


def compute_chunk(row_index: int, b_start: int, b_stop: int) -> dict:
    direct = load_direct(); p = direct.load_pilot()
    h20 = p.load_parent(); h19 = h20.load_parent(); h18 = h19.load_parent(); h17 = h18.load_parent(); h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_for_hpadj21_bchunk")
    p14 = p15.load_parent(); counter = p14.load_counter()
    manifest = counter.load_locked_json(p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest")
    rows = counter.manifest_rows(manifest); req(len(rows) == 178, "FULL178 row coverage")
    req(0 <= row_index < 178, "row index out of range")
    row_id, g0, d0 = rows[row_index]; g, d = int(g0), int(d0); h = d // 2
    req(0 <= b_start <= b_stop <= h, "invalid b chunk")
    BC = counter.build_bc_exact_parity(h)
    two_profiles, _, _, _ = h20.build_two_tier_profiles(h, counter, h19)
    full_profiles, classes_gt2, tuples_above_second = p.full_profiles(h, counter, h19)
    legacy = 8 if g == 0 else 4; K = counter.ceil_div(d - 16*g + 16, 4)
    A = [[sum(mult for _, mult in full_profiles[a][sa]) for sa in range(4)] for a in range(h+1)]
    pos = {interval:i for i, interval in enumerate(p15.PLANNED)}
    two_caps = {i:defaultdict(int) for i in range(len(p15.PLANNED))}
    full_caps = {i:defaultdict(int) for i in range(len(p15.PLANNED))}
    for b in range(b_start, b_stop + 1):
        interval = p15.shard_for_b(b); ip = pos[interval]
        for c in range(h+1):
            bcv = BC[b][c]
            if not any(any(pair) for pair in bcv): continue
            c3 = counter.component3(d,b,c)
            if c3 < 0: continue
            two_surv, _ = h20.survivor_profiles(h16,h19,two_profiles,h,g,b,c)
            exact_surv = p.full_survivors(h16,full_profiles,h,g,b,c)
            for a in range(h+1):
                if not any(A[a]): continue
                M=a+b+c; ca=counter.component_a(d,a)
                if ca < 0: continue
                srem=min(16,d)+ca+c3
                for sbc,pair in enumerate(bcv):
                    for r in (0,1):
                        left=int(pair[r])
                        if not left: continue
                        for sa,right in enumerate(A[a]):
                            if not right: continue
                            ti=two_surv[a][sa]; fi=exact_surv[a][sa]
                            req(ti is not None and fi is not None, "missing q profile")
                            req(sum(x[2] for x in ti["tiers"]) == int(right), "two-tier population drift")
                            req(sum(x[2] for x in fi["tiers"]) == int(right), "full-hist population drift")
                            support=sbc+sa; qneed=K-support
                            if qneed>0 and srem<qneed: continue
                            lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed)); upper=min((19*d)//5,3*d,3*d-(b-c))
                            if lower>upper: continue
                            excluded=set(); e_n358=3*d-(b-c)
                            if b<=h-5 and support+srem==K and e_n358-M>=srem: excluded.add(e_n358)
                            if g==1 and d==8: excluded.add(8)
                            lo=lower if lower%2==0 else lower+1; hi=upper if upper%2==0 else upper-1
                            for e in range(lo,hi+1,2):
                                if e in excluded: continue
                                B=19*d-5*e+1; req(B>0 and B%2==1, f"normal block drift {(g,d,e,B)}")
                                for s0,s1,mult in ti["tiers"]: two_caps[ip][((s0 if r==0 else s1),B)] += left*int(mult)*B
                                for s0,s1,mult in fi["tiers"]: full_caps[ip][((s0 if r==0 else s1),B)] += left*int(mult)*B
    records=[]
    for i, interval in enumerate(p15.PLANNED):
        if two_caps[i] or full_caps[i]:
            records.append({"interval_position":i,"b_interval":list(interval),"two_caps":enc(two_caps[i]),"full_caps":enc(full_caps[i])})
    out={"schema":SCHEMA,"route_id":"HPADJ-21_ex5","status":"EXACT_BCHUNK_COMPLETE_NO_MATHEMATICAL_CREDIT",
         "row":{"index":row_index,"row_id":row_id,"g":g,"d":d,"h":h},"b_range":{"start":b_start,"stop":b_stop},
         "source_locks":{"direct_reference_worker_git_blob":DIRECT_BLOB,"bounded_pilot_git_blob":direct.PILOT_BLOB,"hpadj20_parent_git_blob":p.PARENT_BLOB,"full178_manifest_blob_sha1":p14.LOCKS["manifest_blob"],"hpadj10_counter_blob_sha1":p14.LOCKS["hpadj10_counter_blob"]},
         "profile":{"classes_with_more_than_two_qA_bins":classes_gt2,"tuples_above_second_qA_level":tuples_above_second},
         "interval_records":records,
         "semantics":{"exact_b_partition_only":True,"same_population_as_direct":True,"same_post_mass_constraints_deferred_to_row_assembler":True,"additive_subtraction_used":False,"statistical_independence_assumed":False},
         "credit_firewall":{"partial_output_credit":False,"stage32_main_credit":False,"full178_completion_credit":False,"theorem_credit":False,"effectivity_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_credit":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"] = canonical(out); return out


def validate(path: Path, row_index: int, b_start: int, b_stop: int) -> dict:
    req(path.is_file(), "missing chunk certificate"); d=json.loads(path.read_text())
    req(d.get("schema")==SCHEMA, "chunk schema drift"); req(int(d["row"]["index"])==row_index, "row index drift")
    req(int(d["b_range"]["start"])==b_start and int(d["b_range"]["stop"])==b_stop, "b range drift")
    req(d["source_locks"]["direct_reference_worker_git_blob"]==DIRECT_BLOB, "direct lock drift")
    req(d.get("canonical_sha256_without_this_field")==canonical(d), "chunk canonical drift")
    return d


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--row-index",type=int,required=True); ap.add_argument("--b-start",type=int,required=True); ap.add_argument("--b-stop",type=int,required=True); ap.add_argument("--output",type=Path); ap.add_argument("--verify-existing",type=Path); a=ap.parse_args()
    if a.verify_existing is not None: validate(a.verify_existing,a.row_index,a.b_start,a.b_stop); print("VALID_HPADJ21_BCHUNK"); return
    req(a.output is not None,"--output required"); d=compute_chunk(a.row_index,a.b_start,a.b_stop); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(d,sort_keys=True,separators=(",",":"))+"\n"); print(json.dumps({"row":a.row_index,"b_start":a.b_start,"b_stop":a.b_stop,"bytes":a.output.stat().st_size},sort_keys=True))

if __name__=="__main__": main()
