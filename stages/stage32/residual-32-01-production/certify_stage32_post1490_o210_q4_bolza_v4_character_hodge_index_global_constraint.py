#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
EXPECTED="b5d66b6adfe518880bc376825c4990197a8ba20786967ec260352346b06e7855"
NOTE_BLOB="4169c4fc0f1f44d9adea8df63b9985005a089cea"
LOCKS={
    "v4":("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-v4-deck-translate-defect-decomposition.json","cdc186f8da6eff760a79f98b50106de19d565ebf806dc58b00cc105e4d983af2"),
    "mult":("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-marked-multiplicity-only-boundary.json","29afae4e789522162374baeaca89c860a1c6dac21ce77059e7fe06988e43bfcf"),
    "wall":("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-global-or-carrier-local-jet-information-boundary.json","96e28e71b6b8236a62d221e3a5082d31a51ef8880851fa9c095123fe569cfed0"),
}

def csha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def blobsha(p):
    b=p.read_bytes()
    return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()

def load_rel(rel):
    p=ROOT/rel
    x=json.loads(p.read_text())
    claimed=x.pop("canonical_sha256_without_this_field")
    if csha(x)!=claimed:
        raise SystemExit(f"canonical mismatch: {rel}")
    return x,claimed

def req(cond,msg):
    if not cond:
        raise SystemExit(msg)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",type=Path,required=True)
    a=ap.parse_args()

    data={}
    for k,(p,h) in LOCKS.items():
        x,ch=load_rel(p)
        req(ch==h,f"source lock moved: {k}")
        data[k]=x

    note=HERE/"post1490-o210-q4-bolza-v4-character-hodge-index-source-note.md"
    req(blobsha(note)==NOTE_BLOB,"source note blob moved")

    ar=data["v4"]["intersection_arithmetic"]
    req(ar["D_square_formula"]=="D^2=-162+2*delta_D","D square formula moved")
    req(ar["exact_defect_decomposition"]=="delta_D+c_g1+c_g2+c_g1_plus_g2=8586","defect identity moved")
    req(data["mult"]["marked_intrinsic_delta_lower_bound"]==1046,"intrinsic delta lower bound moved")
    req(data["mult"]["marked_deck_collision_c_lower_bounds"]=={"u":680,"v":898,"uv":726},"old deck marked bounds moved")
    req(data["wall"]["decision"]["retained_source_search_for_this_leaf_exhausted"] is True,"prior information wall moved")

    p=a.check if a.check.is_absolute() else ROOT/a.check
    cert=json.loads(p.read_text())
    claimed=cert.pop("canonical_sha256_without_this_field")
    req(csha(cert)==claimed==EXPECTED,"Hodge certificate canonical moved")

    h=cert["hodge_character_argument"]
    req(h["orthogonal_to_H"] is True and h["hodge_square_nonpositive"] is True,"Hodge orthogonality/sign moved")
    req(h["lambda_mod4"]==2 and h["lambda_zero_impossible"] is True and h["lambda_upper_bound"]==-2,"character parity sharpening moved")

    n=cert["new_global_constraints"]
    req(n["delta_D_lower_bound_from_marked_intrinsic"]==1046,"delta lower moved")
    req(n["delta_D_upper_bound"]==2206,"delta upper moved")
    req(n["deck_half_intersection_universal_lower_bound"]==966,"deck universal lower moved")
    req(n["pair_sum_lower_bound"]==4253,"pair-sum lower moved")

    # Replay exact integer consequences of lambda_chi <= -2.
    # lambda_t = 4*(delta+c_t)-17334, so delta+c_t <= 4333.
    req((17334-2)//4==4333,"upper arithmetic")
    # Adding the other two character inequalities yields c_t >= delta-80.
    # At the retained delta floor, this makes every c_t at least 966.
    req(1046-80==966,"lower arithmetic")
    # Sum of three upper inequalities with delta+sum(c_t)=8586 gives 2*delta<=4413.
    req((3*4333-8586)//2==2206,"delta cap arithmetic")
    # Componentwise lower budget and residual slack.
    req(1046+3*966==3944 and 8586-3944==4642 and 5236-4642==594,"slack arithmetic")

    # Exact endpoint: delta=2206, each c_t in [2126,2127], sum=6380.
    d=2206
    lo=d-80
    hi=4333-d
    total=8586-d
    triples=[]
    for cu in range(lo,hi+1):
        for cv in range(lo,hi+1):
            cuv=total-cu-cv
            if lo<=cuv<=hi:
                triples.append([cu,cv,cuv])
    req(triples==n["delta_2206_endpoint_ordered_triples"],"endpoint triples moved")

    dec=cert["decision"]
    req(dec["independent_global_constraint_introduced"] is True,"new global constraint not recorded")
    req(dec["O210_excluded"] is False and dec["effectivity_proved"] is False and dec["local_jet_materialized"] is False,"credit firewall moved")
    print(json.dumps({"verdict":"PASS_EXACT_V4_CHARACTER_HODGE_GLOBAL_CONSTRAINT","canonical_sha256":claimed,"delta_D_range":[1046,2206],"universal_c_t_lower":966,"residual_slack":4642,"O210_excluded":False,"next_exact_leaf":dec["next_exact_leaf"]},sort_keys=True))

if __name__=="__main__":
    main()
