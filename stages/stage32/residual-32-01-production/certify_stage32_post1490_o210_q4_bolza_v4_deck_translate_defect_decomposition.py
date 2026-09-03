#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
DEFAULT=Path("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-v4-deck-translate-defect-decomposition.json")

def req(c,m):
    if not c: raise AssertionError(m)
def load(p):
    with (ROOT/p).open("r",encoding="utf-8") as f: return json.load(f)
def blob(p):
    b=(ROOT/p).read_bytes(); return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock(x):
    p=Path(x["path"]); req(blob(p)==x["blob_sha1"],f"blob {p}")
    o=load(p); req(o["canonical_sha256_without_this_field"]==x["canonical_sha256"],f"stored canonical {p}"); req(canon(o)==x["canonical_sha256"],f"canonical {p}"); return o

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",type=Path,default=DEFAULT); ns=ap.parse_args(); o=load(ns.check)
    req(o["schema"]=="STAGE32_POST1490_O210_Q4_BOLZA_V4_DECK_TRANSLATE_DEFECT_DECOMPOSITION_V1","schema")
    req(o["fixed_target"]=={"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32],"O":210,"qprime":4},"target")
    d4=lock(o["source_locks"]["d4d4_trace_reduction"]); common=lock(o["source_locks"]["common_double_cover"]); prod=lock(o["source_locks"]["product_cover_v4"]); pic=lock(o["source_locks"]["picard64_witness_adapter"])
    note=o["source_locks"]["source_note"]; req(blob(Path(note["path"]))==note["blob_sha1"],"source note")
    pm=d4["pair_map_birationality"]; req(pm["pair_map_birational"] is True and pm["finite_etale_degree"]==4 and pm["deck_group"]=="(H x H)/H_diag ~= V4","etale V4 quotient")
    req(pm["projection_degrees"]==[105,81] and pm["normalization_genus"]==106,"pair map numerical input")
    req(common["carrier_consequence"]["same_quadratic_extension"] is True,"common-cover source")
    dg=prod["deck_group_model"]; req(dg["group"]=="G=GammaPrime4/Gamma8 ~= F2^2","abstract V4 source"); req(set(dg["nonidentity_mod8_representatives"])=={"g1","g2","g1_plus_g2"},"three deck labels")
    req(pic["reconstruction"]["picard_rank"]==64 and len(pic["reconstruction"]["picard_coordinates"])==64,"Picard64 rank")
    ph=hashlib.sha256(json.dumps(pic["reconstruction"]["picard_coordinates"],separators=(",",":")).encode()).hexdigest(); pl=o["source_locks"]["picard64_witness_adapter"]
    req(ph==pic["reconstruction"]["picard_coordinates_sha256"]==pl["picard_coordinates_sha256"],"Picard coordinates hash")
    req(pic["quadratic"]["picard_self_square"]==858,"retained Picard square")
    q=o["quotient_geometry"]; req(q["finite_etale_degree"]==4 and q["deck_group"]=="V4" and q["bidegree"]==[105,81] and q["normalization_genus"]==106 and q["pair_map_birational"] is True,"stored quotient geometry")
    a,b=q["bidegree"]; g=q["normalization_genus"]; gamma_sq=2*a*b; kg=2*(a+b); pa=1+(gamma_sq+kg)//2; delta=pa-g
    ar=o["intersection_arithmetic"]; req((gamma_sq,kg,pa,delta)==(17010,372,8692,8586),"intersection arithmetic")
    req(ar["gamma_square"]==gamma_sq and ar["canonical_intersection_KQ_Gamma"]==kg and ar["gamma_arithmetic_genus"]==pa and ar["gamma_normalization_defect"]==delta,"stored intersection arithmetic")
    req(ar["D_square_formula"]=="D^2=-162+2*delta_D","adjunction formula")
    req(ar["deck_translate_intersection_sum_formula"]=="sum_{t!=1} D.t(D)=17172-2*delta_D","translate sum formula")
    req(ar["each_nontrivial_translate_intersection_even"] is True and ar["half_intersections_nonnegative_integers"] is True,"free involution parity")
    req(ar["exact_defect_decomposition"]=="delta_D+c_g1+c_g2+c_g1_plus_g2=8586","defect decomposition")
    gap=o["picard_action_gap"]; req(gap["retained_picard64_witness_source_locked"] is True and gap["retained_picard64_rank"]==64 and gap["retained_picard64_self_square"]==858,"Picard retained")
    req(gap["three_picard64_deck_action_matrices_source_locked_in_this_leaf"] is False and gap["abstract_V4_character_model_is_not_picard64_action"] is True and gap["do_not_infer_deck_action_from_two_character_torsor_matrix"] is True,"Picard action firewall")
    dec=o["decision"]; req(dec["O210_excluded"] is False and dec["deck_translate_total_geometry_reduced_exactly"] is True and dec["three_translate_pairings_individually_decided"] is False,"decision")
    req(dec["rosati_lattice_materialization_authorized"] is False and dec["next_exact_leaf"]=="O210_Q4_BOLZA_PICARD64_DECK_ACTION_SOURCE_LOCK","next leaf")
    req(canon(o)==o["canonical_sha256_without_this_field"],"canonical")
    print(json.dumps({"ok":True,"canonical_sha256":canon(o),"gamma_delta":delta,"translate_sum":"17172-2*delta_D","defect_decomposition":ar["exact_defect_decomposition"],"O210_excluded":False,"next_exact_leaf":dec["next_exact_leaf"]},sort_keys=True))
if __name__=="__main__": main()
