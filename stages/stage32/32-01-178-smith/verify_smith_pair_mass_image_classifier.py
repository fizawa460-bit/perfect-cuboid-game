#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
sys.path.insert(0, str(RESIDUAL))

import hperp_integral_adapter as hia

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_HPERP_ADAPTER_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
EXPECTED_INCIDENCE_CANONICAL = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
EXPECTED_WEIERSTRASS_ADAPTER_CANONICAL = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
CURRENT_EXCEPTIONAL_PREFIX = [93,94,95,96,97,98,99,101,102,103]
PAIR_GROUPS = [
    [93,94,95,96], [97,98,99,100], [101,102,103,104],
    [105,106,107,108], [109,110,111,112], [113,114,115,116],
    [117,118,123,124], [119,120,121,122], [125,126,131,132],
    [127,128,129,130], [133,134,139,140], [135,136,137,138],
]
PAIR_LABELS = [
    (43,41),(42,44),(39,37),(38,40),(35,33),(34,36),
    (35,36),(34,33),(38,37),(39,40),(43,44),(42,41),
]
WEIER = {33:6,34:6,35:1,36:1,37:5,38:3,39:5,40:3,41:4,42:4,43:2,44:2}
SELECTED_EXCEPTIONAL = [93,94,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135]
HISTORICAL_SIGNATURE = (1,1,1,1,0,0,1,1,0,0,0,0)


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained payload: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    payload = mod.load()
    if not isinstance(payload, dict):
        raise ValueError(f"retained payload is not dict: {path}")
    return payload


def gf2(v): return tuple(int(x) & 1 for x in v)


def rank(rows) -> int:
    a = [list(gf2(r)) for r in rows if any(int(x) & 1 for x in r)]
    if not a: return 0
    n = len(a[0]); r = 0
    for c in range(n):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None: continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x,y in zip(a[i],a[r])]
        r += 1
        if r == len(a): break
    return r


def xor(*rows):
    if not rows: return ()
    out = [0] * len(rows[0])
    for row in rows:
        for i,x in enumerate(row): out[i] ^= int(x) & 1
    return tuple(out)


def isum(P: Matrix, labels: list[int]) -> list[int]:
    return [sum(int(P[l-1,j]) for l in labels) for j in range(P.cols)]


def independent_basis(vectors):
    basis=[]
    for v in vectors:
        if rank(basis+[v]) > rank(basis): basis.append(gf2(v))
    return basis


def cycles_of_perm(p):
    seen=set(); cyc=[]
    for i in range(1,7):
        if i in seen: continue
        cur=[]; j=i
        while j not in seen:
            seen.add(j); cur.append(j); j=p[j-1]
        if len(cur)>1: cyc.append(cur)
    return cyc


def classify_signature(sig):
    B=[[0]*6 for _ in range(6)]
    for bit,(a,b) in zip(sig,PAIR_LABELS):
        B[WEIER[a]-1][WEIER[b]-1] = int(bit)
    rs=[sum(row) for row in B]
    cs=[sum(B[i][j] for i in range(6)) for j in range(6)]
    perm = all(x==1 for x in rs) and all(x==1 for x in cs)
    p=None; cycles=[]
    if perm:
        p=[row.index(1)+1 for row in B]
        cycles=cycles_of_perm(p)
    return {
        "signature": list(sig),
        "matrix_rows": B,
        "row_sums": rs,
        "column_sums": cs,
        "is_permutation": perm,
        "permutation_image_1based": p,
        "nontrivial_cycles": cycles,
        "single_transposition": perm and len(cycles)==1 and len(cycles[0])==2,
        "historical_signature": tuple(sig)==HISTORICAL_SIGNATURE,
    }


def main() -> None:
    raw=(RESIDUAL / "hperp_integral_adapter.py").read_bytes()
    blob=hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()
    if blob != EXPECTED_HPERP_ADAPTER_BLOB: raise ValueError("hperp adapter regression")
    bundle=load_retained(RETAINED,"s32_smith_classifier_bundle")
    marking=load_retained(MARKING,"s32_smith_classifier_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL: raise ValueError("bundle regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL: raise ValueError("marking regression")

    inc=json.loads((RESIDUAL / "post1473-x8-marked-exceptional-incidence.json").read_text())
    wei=json.loads((RESIDUAL / "post1473-boundary-label-weierstrass-adapter.json").read_text())
    if inc.get("canonical_sha256_without_this_field") != EXPECTED_INCIDENCE_CANONICAL: raise ValueError("incidence regression")
    if wei.get("canonical_sha256_without_this_field") != EXPECTED_WEIERSTRASS_ADAPTER_CANONICAL: raise ValueError("weierstrass adapter regression")
    if {int(k):int(v) for k,v in wei["boundary_label_to_weierstrass_id"].items()} != WEIER: raise ValueError("weierstrass map mismatch")

    adapter=hia.HperpIntegralPairingAdapter.from_retained(marking,bundle)
    P=adapter.pairing_matrix
    if P.shape != (140,64): raise ValueError("pairing shape regression")
    row={l:[int(P[l-1,j]) for j in range(64)] for l in range(1,141)}
    pair_rows=[isum(P,g) for g in PAIR_GROUPS]
    if rank(pair_rows) != 3: raise ValueError("pair-mass image rank regression")

    # Image of Picard64 -> F2^12 is the column span of the 12x64 parity matrix.
    cols=[tuple(pair_rows[i][j]&1 for i in range(12)) for j in range(64)]
    image_basis=independent_basis(cols)
    if len(image_basis)!=3: raise ValueError("image basis dimension regression")
    signatures=sorted({xor(*(image_basis[i] for i,b in enumerate(mask) if b)) if any(mask) else (0,)*12
                       for mask in itertools.product((0,1),repeat=3)})
    if len(signatures)!=8: raise ValueError("expected eight parity signatures")
    classified=[classify_signature(s) for s in signatures]

    # Add current scalar/prefix observables and find a concrete minimum set of
    # already-selected Picard exceptional rows whose exposure determines all12 M_p parities.
    _, degree_col, _, _, _=hia._parse_hperp(marking["hperp_text"])
    degree=[int(degree_col[l-1,0]) for l in hia.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    e_total=isum(P,list(range(93,141)))
    obs=[gf2(degree),gf2(e_total),gf2(row[49])]+[gf2(row[l]) for l in CURRENT_EXCEPTIONAL_PREFIX]
    target=[gf2(r) for r in pair_rows]
    base_rank=rank(obs)
    candidates=[l for l in SELECTED_EXCEPTIONAL if l not in CURRENT_EXCEPTIONAL_PREFIX]
    min_k=None; subsets=[]
    for k in range(len(candidates)+1):
        for sub in itertools.combinations(candidates,k):
            rr=obs+[gf2(row[l]) for l in sub]
            if rank(rr+target)==rank(rr):
                min_k=k; subsets.append(list(sub))
        if min_k is not None: break

    # Row/column parity forms are intrinsic consequences of the 12-group map.
    row_forms=[]; col_forms=[]
    for rid in range(1,7):
        inds=[i for i,(a,_) in enumerate(PAIR_LABELS) if WEIER[a]==rid]
        row_forms.append(xor(*(gf2(pair_rows[i]) for i in inds)))
    for cid in range(1,7):
        inds=[i for i,(_,b) in enumerate(PAIR_LABELS) if WEIER[b]==cid]
        col_forms.append(xor(*(gf2(pair_rows[i]) for i in inds)))
    all_rows_equal=all(x==row_forms[0] for x in row_forms)
    all_cols_equal=all(x==col_forms[0] for x in col_forms)

    out={
      "schema":"STAGE32_32_01_178_SMITH_PAIR_MASS_IMAGE_CLASSIFIER_V1",
      "source_locks":{
        "retained_bundle_canonical":EXPECTED_BUNDLE_CANONICAL,
        "retained_marking_canonical":EXPECTED_MARKING_CANONICAL,
        "hperp_adapter_blob_sha1":blob,
        "marked_exceptional_incidence_canonical":EXPECTED_INCIDENCE_CANONICAL,
        "weierstrass_adapter_canonical":EXPECTED_WEIERSTRASS_ADAPTER_CANONICAL,
        "old_smith_hostile_review":5147627146,
      },
      "linear_image":{
        "pair_mass_parity_rank":3,
        "signature_count":8,
        "basis_signatures":[list(x) for x in image_basis],
        "classified_signatures":classified,
        "permutation_signature_count":sum(x["is_permutation"] for x in classified),
        "single_transposition_signature_count":sum(x["single_transposition"] for x in classified),
      },
      "fibre_parity_structure":{
        "all_six_first_factor_row_sum_forms_equal":all_rows_equal,
        "all_six_second_factor_column_sum_forms_equal":all_cols_equal,
        "first_row_sum_form_equals_second_column_sum_form":row_forms[0]==col_forms[0],
        "common_row_form_in_span_degree_e_total":rank([gf2(degree),gf2(e_total),row_forms[0]])==rank([gf2(degree),gf2(e_total)]),
      },
      "current_prefix_extension":{
        "current_observable_rank":base_rank,
        "candidate_selected_exceptional_labels":candidates,
        "minimal_additional_individual_exceptional_pairings":min_k,
        "minimal_subset_count":len(subsets),
        "minimal_subsets_first50":subsets[:50],
      },
      "interpretation":{
        "pair_mass_parity_to_weierstrass_matrix_exact":True,
        "pair_mass_parity_alone_proves_current_common_cover":False,
        "pair_mass_single_transposition_alone_proves_current_H_equivariant_assembly":False,
        "next_gate":"Intersect current FULL178 carrier semantics with the fixed-X8/common-cover hypotheses; only on that source-compatible subpopulation may a single-transposition parity signature feed the audited absolute A[2] transvection/Smith adapter.",
      },
      "credit":{"main_pruning_credit":False,"full178_completion":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_claim":False,"merge_authorized":False},
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__": main()
