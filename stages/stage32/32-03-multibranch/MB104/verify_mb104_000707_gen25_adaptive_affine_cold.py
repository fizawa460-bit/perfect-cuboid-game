#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[5]
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
DERIVE=HERE/"derive_mb104_000707_gen25_adaptive_affine_cold.py"
SPEC=HERE/"MB104-000707-GEN25-SUCCESSOR-REDESIGN-COLD-SPEC.json"
RESIDUAL=HERE/"MB104-000707-GEN24-X60-SINGLETON-RESIDUAL30.json"
SCHEMA="STAGE32_MB104_000707_GEN25_ADAPTIVE_AFFINE_COLD_V1"
def blob(p): return subprocess.check_output(["git","hash-object",str(p)],cwd=REPO,text=True).strip()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); a=ap.parse_args()
    k=json.loads(RUNKEY.read_text()); sl=k["source_locks"]
    for f,p in {
      "gen25_successor_design_spec_git_blob":SPEC,
      "gen25_successor_cold_diagnostic_git_blob":DERIVE,
      "gen24_residual_git_blob":RESIDUAL,
    }.items():
        got=blob(p)
        if got!=sl[f]: raise SystemExit(f"source-lock mismatch: {f}: {got} != {sl[f]}")
    if int(k["generation"])!=25 or k["mode"]!="COLD" or k["armed"] is not False: raise SystemExit("Gen25 COLD/unarmed contract drift")
    d=json.loads(a.certificate.read_text())
    if d["schema"]!=SCHEMA or d["status"]!="COLD_ADAPTIVE_AFFINE_SUCCESSOR_DESIGNED_NO_HEAVY_EXECUTION_NO_CREDIT": raise SystemExit("certificate identity")
    if int(d["carried_complete_x60_singletons"])!=281 or int(d["residual_timeout_leaf_count"])!=30 or d["recompute_carried_complete_regions"] is not False: raise SystemExit("population drift")
    if d["forbidden_split_coordinates_0based"]!=[59,60,61,62] or len(d["leaves"])!=30: raise SystemExit("partition contract")
    if d["heavy_surface_present"] or d["heavy_armed"] or d["execution_authorized"] or any(bool(v) for v in d["credit_firewall"].values()): raise SystemExit("firewall")
    total=0; hist={}; identities=set()
    for leaf in d["leaves"]:
        ident=(int(leaf["primary_value"]),int(leaf["secondary_residue"]),int(leaf["fixed_x61_value"]),int(leaf["x60_residue"]),int(leaf["fixed_x60_value"]),leaf["source_canonical_sha256"])
        if ident in identities: raise SystemExit("duplicate residual leaf")
        identities.add(ident)
        if leaf["status"]=="ADAPTIVE_AFFINE_CONDITIONED_SPLIT":
            sel=leaf["selected_coordinate"]; j=int(sel["coordinate_0based"])
            if j in {59,60,61,62}: raise SystemExit("forbidden successor coordinate")
            lo,hi=map(int,sel["bound"])
            if int(sel["domain_size"])!=hi-lo+1: raise SystemExit("domain mismatch")
            ints=leaf["intervals"]
            if not ints or int(ints[0][0])!=lo or int(ints[-1][1])!=hi: raise SystemExit("endpoint coverage")
            for left,right in zip(ints,ints[1:]):
                if int(left[1])+1!=int(right[0]): raise SystemExit("gap/overlap")
            total+=len(ints); hist[str(j)]=hist.get(str(j),0)+1
        else:
            if leaf["selected_coordinate"] is not None or leaf["intervals"] or int(leaf["interval_child_count"])!=0: raise SystemExit("empty-leaf encoding")
    s=d["summary"]
    if int(s["total_interval_child_count"])!=total or total>240: raise SystemExit("child budget")
    if s["selected_coordinate_histogram"]!=hist or int(s["split_leaf_count"])+int(s["necessary_condition_empty_leaf_count"])!=30: raise SystemExit("summary mismatch")
    replay=subprocess.run([sys.executable,str(DERIVE)],cwd=HERE,text=True,capture_output=True,check=True)
    if d!=json.loads(replay.stdout): raise SystemExit("deterministic exact replay mismatch")
    print(json.dumps({"success":True,"generation":25,"carried_complete":281,"residual_timeout":30,"split_leaf_count":s["split_leaf_count"],"necessary_condition_empty_leaf_count":s["necessary_condition_empty_leaf_count"],"selected_coordinate_histogram":s["selected_coordinate_histogram"],"total_interval_child_count":total,"maximum_conditional_domain":s["maximum_conditional_domain"],"median_conditional_domain":s["median_conditional_domain"],"heavy_authorized":False,"credit":False},sort_keys=True))
if __name__=="__main__": main()
