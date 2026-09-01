#!/usr/bin/env python3
"""Exact structural analysis of the tiny m=4 survivor sets.

This is the applicability gate for provisional Arsenal card S32-PW03.  It does
not assume that the nonlinear matching-x relation is an affine subgroup/coset.
It reconstructs each selected-prime intersection exactly, stores the <=16
survivor tuples, and tests affine-coset closure in the actual finite MW
coordinate group.
"""
import json, pathlib, runpy

ROOT=pathlib.Path(__file__).resolve().parent
# Execute the source-locked tailored sieve once in this process; it writes the
# parent certificate and returns the exact helper namespace/functions.
g=runpy.run_path(str(ROOT/"run_d2_fiber_product_mw_tailored.py"))
parent=json.loads((ROOT/"d2-fiber-product-mw-tailored.json").read_text())
projected_relation=g["projected_relation"]
ns=g["ns"]
j_map=g["j_map"]


def sub(a,b,mods): return tuple((x-y)%m for x,y,m in zip(a,b,mods))
def add(a,b,mods): return tuple((x+y)%m for x,y,m in zip(a,b,mods))

def affine_coset_test(states,mods):
    if not states:
        return {"is_affine_coset":True,"base":None,"subgroup_size":0,"difference_states":[]}
    S=set(states); base=min(S)
    D={sub(s,base,mods) for s in S}
    zero=tuple(0 for _ in mods)
    closed=(zero in D and len(D)==len(S))
    if closed:
        for x in D:
            for y in D:
                if add(x,y,mods) not in D:
                    closed=False; break
            if not closed: break
    return {
      "is_affine_coset":closed,
      "base":list(base),
      "subgroup_size":len(D) if closed else None,
      "difference_states":[list(x) for x in sorted(D)] if closed else []
    }

records=[]
for rec in parent["cases"]:
    name=rec["q"]; d=int(rec["d"]); m=int(rec["m"])
    rels=[]
    for p in rec["selected_primes"]:
        z=projected_relation(name,d,int(p),m)
        assert z is not None and not z.get("skip")
        rels.append(set(z["relation"]))
    inter=set.intersection(*rels)
    assert len(inter)==rec["intersection_survivors"]
    assert ns["canon_hash"](inter)==rec["intersection_sha256"]
    erank=int(rec["E_rank"]); jrank=int(rec["J_rank"])
    # State layout: E free, E torsion (r mod4,s mod2), J free,
    # J torsion (r mod4,s mod2).
    mods=[m]*erank+[4,2]+[m]*jrank+[4,2]
    assert all(len(s)==len(mods) for s in inter)
    struct=affine_coset_test(inter,mods)
    e_free={tuple(s[:erank]) for s in inter}
    j0=erank+2; j_free={tuple(s[j0:j0+jrank]) for s in inter}
    free_pairs={(tuple(s[:erank]),tuple(s[j0:j0+jrank])) for s in inter}
    records.append({
      "q":name,"d":d,"m":m,"state_moduli":mods,
      "survivor_count":len(inter),"survivor_sha256":ns["canon_hash"](inter),
      "survivor_states":[list(s) for s in sorted(inter)],
      "affine_coset":struct,
      "E_free_projection_count":len(e_free),
      "E_free_projection":[list(x) for x in sorted(e_free)],
      "J_free_projection_count":len(j_free),
      "J_free_projection":[list(x) for x in sorted(j_free)],
      "free_pair_projection_count":len(free_pairs),
      "all_E_free_zero_mod_m":e_free=={tuple(0 for _ in range(erank))},
      "all_J_free_zero_mod_m":j_free=={tuple(0 for _ in range(jrank))},
    })

payload={
  "schema":"STAGE34_02_D2_FIXED_QUOTIENT_SURVIVOR_STRUCTURE_V1",
  "status":"PASS_EXACT_SURVIVOR_STRUCTURE_ANALYSIS",
  "source":"d2-fiber-product-mw-tailored.json",
  "arsenal_gate":"S32-PW03 may be used only on cases whose survivor set is proved here to be an affine coset (or after a separately proved affine-coset decomposition).",
  "cases":records,
  "affine_coset_cases":[[r["q"],r["d"]] for r in records if r["affine_coset"]["is_affine_coset"]],
  "non_affine_cases":[[r["q"],r["d"]] for r in records if not r["affine_coset"]["is_affine_coset"]],
  "firewalls":{
    "affine_coset_structure_is_global_rational_point":False,
    "non_affine_relation_may_be_forced_into_HNF":False,
    "m4_free_zero_means_global_torsion":False,
    "receiver_closed":False
  }
}
(ROOT/"d2-fixed-quotient-survivor-structure.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"affine":len(payload["affine_coset_cases"]),"non_affine":len(payload["non_affine_cases"])},sort_keys=True))
