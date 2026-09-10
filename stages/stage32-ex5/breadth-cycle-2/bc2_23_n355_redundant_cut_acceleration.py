#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat
import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18

HERE=Path(__file__).resolve().parent
P17=HERE/"bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
P18=HERE/"bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json"
P19=HERE/"bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json"
P22=HERE/"bc2-22-recheck-44-residual-unknown-checkpoint.json"
PF=HERE/"bc2-23-n355-redundant-cut-acceleration-preflight.json"
E17="a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
E18="b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
E19="62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
E22="e8151702d8386eeab44d9e9705abe7b4fa0e19dde96933ffdabdc56329f2fdc2"
EPF="680ea3df4f90402d6535066a67b40bc8b635f68aa2fe2ab76bd06d9aaff96495"
ED18="1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
ESTREAM="752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
PACKS=[[33,36,37,40,41,44],[34,35,38,39,42,43]]
N,E,D,R=92,8,8,64

def csha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def blob(path):
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def load(path,expected,replay=True):
    o=json.loads(path.read_text())
    if o.get("canonical_sha256_without_this_field")!=expected: raise ValueError(f"canonical field drift: {path.name}")
    if replay:
        q=dict(o); q.pop("canonical_sha256_without_this_field",None)
        if csha(q)!=expected: raise ValueError(f"canonical replay drift: {path.name}")
    return o
def rowsum(M,labels):
    z=Matrix.zeros(1,M.cols)
    for l in labels: z+=M.row(l-1)
    return z

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--per-parent-timeout-ms",type=int,default=5000); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args()
    if a.per_parent_timeout_ms<=0: raise ValueError("timeout")
    if blob(Path(d18.__file__).resolve())!=ED18: raise ValueError("BC2-18 source blob regression")

    c17=load(P17,E17); c18=load(P18,E18,replay=False); c19=load(P19,E19); c22=load(P22,E22); pf=load(PF,EPF)
    targets=[int(v) for v in c22["result"]["residual_unknown_parent_indices"]]
    if targets!=[int(v) for v in pf["target"]["retained_unknown_parent_indices"]] or len(targets)!=36: raise ValueError("target list regression")
    if c22["interpretation"]["known_parent_unsat_count_lower_bound"]!=7128: raise ValueError("BC2-22 lower bound regression")
    if c22["target"]["other_unretained_unknown_identity_count"]!=172: raise ValueError("unretained count regression")
    if c18["exact_decomposition"]["enumerated_parent_count"]!=177100: raise ValueError("enum count regression")
    if c18["exact_decomposition"]["mod8_extendable_parent_count"]!=7336: raise ValueError("parent count regression")
    if c18["exact_decomposition"]["feasible_stream_sha256"]!=ESTREAM: raise ValueError("stream regression")
    if (c19["result"]["unsat_count"],c19["result"]["unknown_count"],c19["result"]["sat_count"])!=(7100,236,0): raise ValueError("BC2-19 partition regression")

    fixed={int(k):int(v) for k,v in c17["retarget"]["fixed_exceptional_pairings"].items()}
    if len(fixed)!=10 or sum(fixed.values())!=2: raise ValueError("fixed exceptional regression")
    bundle=d18.load_retained(d18.RETAINED,"s32ex5_bc223_bundle"); marking=d18.load_retained(d18.MARKING,"s32ex5_bc223_marking")
    if bundle.get("canonical_sha256")!=d18.EXPECTED_BUNDLE_CANONICAL: raise ValueError("bundle regression")
    if marking.get("canonical_sha256")!=d18.EXPECTED_MARKING_CANONICAL: raise ValueError("marking regression")
    adapter=d18.HperpIntegralPairingAdapter.from_retained(marking,bundle); P=Matrix(adapter.pairing_matrix); coords=Matrix(adapter.class_coordinates_in_retained_basis); gram=Matrix(bundle["picard_gram_64x64"])
    if P.shape!=(140,R) or coords.shape!=(140,R) or gram.shape!=(R,R): raise ValueError("shape regression")
    full=coords*gram*coords.T

    blocks=[]; fcoefs=[]; geometry=[]
    for fi,pack in enumerate(PACKS,1):
        seen=[]; bs=[]; fs=[]; desc=[]
        for b in pack:
            inc=[j for j in range(93,141) if int(full[b-1,j-1])==1]
            if len(inc)!=8: raise ValueError(f"incidence regression {b}")
            seen+=inc; bs.append(inc); f=2*P.row(b-1)+rowsum(P,inc); fs.append(f); desc.append({"boundary_label":b,"exceptional_labels":inc})
        if sorted(seen)!=list(range(93,141)): raise ValueError(f"partition regression factor {fi}")
        if any(f!=fs[0] for f in fs[1:]): raise ValueError(f"fibre functional regression factor {fi}")
        blocks.append(bs); fcoefs.append(fs[0]); geometry.append({"factor":fi,"boundary_pack":pack,"blocks":desc})
    if 19*(fcoefs[0]+fcoefs[1])!=rowsum(P,list(range(1,93)))+5*rowsum(P,list(range(93,141))): raise ValueError("N352 mass functional regression")
    if 112+5*E!=19*D: raise ValueError("mass-degree substitution regression")

    labels=[int(v) for v in d18.INDLIST]; Ps=P.extract([l-1 for l in labels],list(range(R))); inv=Ps.inv(); den=d18.lcm_denominator(inv)
    if den!=8: raise ValueError("denominator regression")
    Bq=inv*den
    if any(q.q!=1 for q in Bq): raise ValueError("inverse scaling regression")
    B=Matrix([[int(Bq[i,j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    npos=[j for j,l in enumerate(labels) if l<=N]; epos=[j for j,l in enumerate(labels) if l>N]; elabels=[labels[j] for j in epos]; free=[l for l in elabels if l not in fixed]
    if len(free)!=19: raise ValueError("free selected exceptional regression")
    hfull=d18.build_hnf_extension_check(B,den,epos,npos); x4pos=labels.index(49); hx4=d18.build_hnf_extension_check(B,den,epos+[x4pos],[j for j in npos if j!=x4pos])
    parents=[]; stream=hashlib.sha256(); enum=0
    for comp in d18.weak_compositions_at_most(6,len(free)):
        enum+=1; by=dict(fixed); by.update({l:int(v) for l,v in zip(free,comp)}); y=[int(by[l]) for l in elabels]
        allowed=[r for r in range(den) if d18.feasible(hx4,y+[r])]; ok=d18.feasible(hfull,y)
        if ok!=bool(allowed): raise ValueError("HNF/x4 regression")
        if not ok: continue
        rec={"selected_exceptional_pairings":y,"selected_residual_mass":sum(comp),"x4_allowed_residues_mod8":allowed}; stream.update(json.dumps(rec,sort_keys=True,separators=(",",":")).encode()+b"\n"); parents.append((y,allowed))
    if enum!=177100 or len(parents)!=7336 or stream.hexdigest()!=ESTREAM: raise ValueError("parent ordering regression")

    x=[Int(f"x_{j}") for j in range(R)]; p=[sum(int(P[i,j])*x[j] for j in range(R)) for i in range(140)]; s=SolverFor("QF_LIA"); s.set(timeout=a.per_parent_timeout_ms)
    for i in range(N): s.add(p[i]>=0,p[i]<=112)
    for i in range(N,140): s.add(p[i]>=0,p[i]<=E)
    s.add(sum(p[:N])==112,sum(p[N:])==E)
    for l,v in fixed.items(): s.add(p[l-1]==v)
    fexpr=[]
    for pack,bs in zip(PACKS,blocks):
        vals=[2*p[b-1]+sum(p[j-1] for j in block) for b,block in zip(pack,bs)]
        for v in vals[1:]: s.add(v==vals[0])
        fexpr.append(vals[0])
    s.add(fexpr[0]+fexpr[1]==D,fexpr[0]>=0,fexpr[0]<=D,fexpr[1]>=0,fexpr[1]<=D)
    for l in range(93,141): s.add(p[l-1]<=D//2)
    for b1 in blocks[0]:
        q1=sum(p[j-1] for j in b1)
        for b2 in blocks[1]: s.add(q1+sum(p[j-1] for j in b2)<=D)

    records=[]; newly=[]; residual=[]; witness=None
    for pi in targets:
        y,allowed=parents[pi]; s.push()
        for l,v in zip(elabels,y): s.add(p[l-1]==v)
        r=s.check(); rec={"parent_index":pi,"result":str(r)}
        if r==unsat: newly.append(pi)
        elif r==unknown: rec["reason_unknown"]=s.reason_unknown(); residual.append(pi)
        elif r==sat:
            m=s.model(); xv=[int(m.eval(q,model_completion=True).as_long()) for q in x]; pv=[sum(int(P[i,j])*xv[j] for j in range(R)) for i in range(140)]
            if min(pv)<0 or sum(pv[:N])!=112 or sum(pv[N:])!=E: raise ValueError("SAT base regression")
            if any(pv[l-1]!=v for l,v in zip(elabels,y)): raise ValueError("SAT parent regression")
            if max(pv[92:])>D//2: raise ValueError("SAT diagonal regression")
            for b1 in blocks[0]:
                for b2 in blocks[1]:
                    if sum(pv[j-1] for j in b1)+sum(pv[j-1] for j in b2)>D: raise ValueError("SAT block regression")
            if pv[48]%den not in allowed: raise ValueError("SAT x4 regression")
            rec["x4"]=pv[48]; rec["all140_pairings_sha256"]=csha(pv)
            if witness is None: witness={"parent_index":pi,"picard64_coordinates":xv,"all140_pairings":pv,"all140_pairings_sha256":csha(pv)}
        else: raise ValueError("unexpected solver result")
        records.append(rec); s.pop()

    u=len(newly); q=len(residual); t=sum(r["result"]=="sat" for r in records); lower=7128+u
    if t: status="PASS_N355_REDUNDANT_CUT_PICARD64_FEASIBLE_WITNESS_FOUND_NO_CURVE_CREDIT"; nxt="BC2_24_ANALYZE_REDUNDANT_CUT_SAT_WITNESS"
    elif q==0: status="PASS_ALL_36_RETAINED_BC2_22_UNKNOWN_EXACT_UNSAT_WITH_N355_REDUNDANT_CUT_ACCELERATION"; nxt="BC2_24_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else: status="BLOCKED_N355_REDUNDANT_CUT_ACCELERATION_LEAVES_RETAINED_UNKNOWN"; nxt="BC2_24_PARTITION_REMAINING_RETAINED_UNKNOWN_BY_EXPLICIT_FIBRE_DEGREE"
    body={"schema":"STAGE32EX5_BC2_23_N355_REDUNDANT_CUT_ACCELERATION_V1","stage":"32EX5","unit":"BC2_23_TEST_N355_STRUCTURAL_INEQUALITIES_ON_36_RETAINED_UNKNOWN_PARENTS","status":status,
      "source_locks":{"bc2_17":E17,"bc2_18":E18,"bc2_19":E19,"bc2_22":E22,"preflight":EPF,"bc2_18_enumerator_git_blob_sha":ED18,"bc2_18_feasible_stream_sha256":ESTREAM,"retained_bundle":d18.EXPECTED_BUNDLE_CANONICAL,"retained_marking":d18.EXPECTED_MARKING_CANONICAL,"n355_full_prefix_hostile_audit_review_id":pf["source_locks"]["n355_full_prefix_hostile_audit_review_id"],"n355_full_prefix_hostile_audit_exact_head":pf["source_locks"]["n355_full_prefix_hostile_audit_exact_head"],"stage32_main_head_observed":pf["source_locks"]["stage32_main_head_observed"]},
      "geometry_replay":{"boundary_packs":PACKS,"pack_data":geometry,"each_boundary_incident_exceptional_count":8,"each_pack_partitions_all_48_exceptionals":True,"fibre_functionals_constant_within_each_pack":True,"degree_sum_mass_functional_identity_replayed":True,"target_mass_substitution":{"normal_mass":112,"exceptional_mass":E,"project_degree":D,"identity":"112+5*8=19*8"}},
      "redundant_cut_certificate":{"feasible_set_preserved":True,"reason":"All added constraints follow from exact retained Picard64 fibre functionals, BC2-19 all140 nonnegativity, and BC2-19 mass equations.","explicit_fibre_equalities":10,"explicit_degree_sum_equality":1,"explicit_fibre_degree_box_constraints":4,"explicit_exceptional_diagonal_caps":48,"explicit_full_block_pair_cuts":36,"diagonal_cap":4,"block_pair_cap":8},
      "target":{"row_id":"g1-d008","g":1,"d":D,"e":E,"checked_parent_indices":targets,"checked_count":36,"unretained_bc2_19_unknown_identity_count":172,"unretained_bc2_19_unknown_identities_inferred":False},
      "result":{"unsat_count":u,"unknown_count":q,"sat_count":t,"newly_unsat_parent_indices":newly,"residual_unknown_parent_indices":residual,"records":records,"per_parent_timeout_ms":a.per_parent_timeout_ms,"solver":"Z3_QF_LIA_WITH_LOGICALLY_REDUNDANT_N355_PICARD_CUTS","z3_version":get_version_string()},"sat_witness":witness,
      "interpretation":{"known_parent_unsat_count_lower_bound":lower,"known_retained_unknown_identity_count_after_this_run":q,"unretained_unknown_identity_count":172,"whole_first_block_unsat_proved":False,"n355_added_new_mathematical_feasible_set_restriction":False,"n355_used_as_solver_acceleration":True},
      "credit":{"this_36_parent_slice_exact_unsat":t==0 and q==0,"whole_first_block_unsat":False,"whole_stratum_closed":False,"full178_complete":False,"stage32_main_credit":False,"effectivity_or_actual_curve_existence_proved":False,"theorem_credit":False,"endpoint_credit":False},
      "firewalls":{"unretained_172_parent_identities_inferred":False,"unknown_relabelled_unsat":False,"redundant_cut_relabelled_new_main_theorem":False,"sat_relabelled_actual_curve":False,"main_promotion":False,"merge_authorized":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False},"next_exact_unit":{"id":nxt,"main_promotion_authorized":False}}
    body["canonical_sha256_without_this_field"]=csha(body); a.output.write_text(json.dumps(body,indent=2,sort_keys=True)+"\n"); print(json.dumps({"canonical":body["canonical_sha256_without_this_field"],"status":status,"unsat":u,"unknown":q,"sat":t,"known_unsat_lower_bound":lower,"next":nxt},sort_keys=True))
if __name__=="__main__": main()
