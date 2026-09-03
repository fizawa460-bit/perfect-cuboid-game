#!/usr/bin/env python3
"""V41: materialize e3 independently in the retained10/proper14 source interface.

This replay does not use J2=e2+e3 to solve for e3. It recomputes the exact
V4-fixed proper Br[2] nullspace from the locked 14D actions, checks that this is
the retained 10D basis used by the Kummer target, and selects its third standard
basis row because V34 defines adapted source 2 as standard e3 (mask 4).
No H2(mu2) lift or Kummer column is claimed here.
"""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
BR2 = STAGE33 / "33-07" / "proper-brauer2-from-discriminant.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
V34 = HERE / "j2-adapted-first-kummer-column-v34.json"
OUT = HERE / "e3-independent-proper14-source-v41.json"
LOCKS = {
    BR2: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    TARGET: "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
    V34: "eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e",
}
EXPECTED_OUT = "04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj

def xor(a,b): return [int(x)^int(y) for x,y in zip(a,b)]
def identity(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def transpose(a): return [list(row) for row in zip(*a)]
def rref(rows,ncols):
    a=[[int(x)&1 for x in row] for row in rows if any(int(x)&1 for x in row)]
    pivots=[]; r=0
    for c in range(ncols):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(len(a)):
            if i!=r and a[i][c]: a[i]=xor(a[i],a[r])
        pivots.append(c); r+=1
        if r==len(a): break
    return a[:r],pivots

def nullspace(rows,ncols):
    red,piv=rref(rows,ncols); free=[c for c in range(ncols) if c not in piv]; out=[]
    for f in free:
        v=[0]*ncols; v[f]=1
        for i,p in enumerate(piv): v[p]=red[i][f]
        out.append(v)
    return out

def rank(rows): return len(rref(rows,len(rows[0]))[0]) if rows else 0

def bits(mask,n): return [(mask>>i)&1 for i in range(n)]

def main():
    br2=locked(BR2); target=locked(TARGET); v34=locked(V34)
    n=14; eye=identity(n)
    cc=br2["proper_Br2_cc_action_f2"]; ct=br2["proper_Br2_ct_action_f2"]
    nc=[xor(r,e) for r,e in zip(cc,eye)]; nt=[xor(r,e) for r,e in zip(ct,eye)]
    basis=nullspace(transpose(nc)+transpose(nt),n)
    assert len(basis)==10 and rank(basis)==10
    retained=target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
    assert basis==retained
    change=v34["source_basis_change"]
    assert change["adapted_basis_labels"]==["J2=e2+e3","e3","e1","e4","e5","e6","e7","e8","e9","e10"]
    assert change["adapted_basis_masks_decimal"]==[6,4,1,8,16,32,64,128,256,512]
    e3=basis[2]
    assert e3==[0,0,1,0,1,0,0,0,0,0,0,0,0,0]
    assert sum((bit<<i) for i,bit in enumerate(e3))==20
    out={
      "schema":"STAGE33_12_E3_INDEPENDENT_PROPER14_SOURCE_V41","stage":"33-12",
      "status":"PASS_EXACT_E3_INDEPENDENT_PROPER14_SOURCE_MATERIALIZED_H2_MU2_LIFT_OPEN",
      "source_locks":{"proper_brauer2_from_discriminant_sha256":LOCKS[BR2],"full_surface_pic2_kummer_target_sha256":LOCKS[TARGET],"v34_j2_adapted_basis_sha256":LOCKS[V34]},
      "e3_source":{"adapted_basis_label":"e3","adapted_basis_position_1based":2,"standard_retained10_basis_position_1based":3,"retained10_standard_mask_decimal":4,"retained10_standard_coordinate_f2":bits(4,10),"proper14_mask_decimal":20,"proper14_coordinate_f2":e3,"derivation":"third row of the exact V4-fixed proper Br2 nullspace used by full-surface-pic2-kummer-target.json","source_coordinate_materialized":True,"derived_from_j2_xor_split":False},
      "basis_replay":{"proper_invariant_dimension_f2":10,"basis_rows_original_proper_br2_coordinates_f2":basis,"basis_rank_f2":10,"e3_row_index_zero_based":2,"e3_row_replayed_from_br2_actions":True},
      "construction_boundary":{"genuine_full_surface_h2_mu2_lift_materialized":False,"explicit_geometric_or_cech_representative_for_e3_materialized":False,"kummer_column_for_e3_materialized":False,"minimal_missing_interface":"GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_EXACT_E3_PROPER14_MASK20","next_exact_leaf":"CONSTRUCT_GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_EXACT_E3_PROPER14_MASK20_WITHOUT_USING_J2_XOR_SPLIT"},
      "anti_inference":{"j2_equals_e2_plus_e3_used_to_derive_e3":False,"standard_col2_col3_split_from_xor":False,"remaining_kummer_column_guessed":False,"locator_miss_used_as_repository_absence":False,"broad_history_or_origin_search_restarted":False},
      "promotion_firewall":{"stage33_progress":"6/11","stage33_12_closed_exact":False,"stage33_13_released":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False,"merge_allowed":False},
    }
    out["canonical_sha256"]=csha(out)
    assert out["canonical_sha256"]==EXPECTED_OUT
    if "--check" in sys.argv:
        got=json.loads(OUT.read_text(encoding="utf-8")); assert got==out
    else:
        OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"success":True,"canonical_sha256":EXPECTED_OUT,"retained10_mask":4,"proper14_mask":20,"genuine_h2_mu2_lift_materialized":False,"next_exact_leaf":out["construction_boundary"]["next_exact_leaf"],"marker":"PROOF_REPLAY_COMPLETE"},sort_keys=True))

if __name__=="__main__": main()
