#!/usr/bin/env python3
"""Network-free exact verifier for the Stage33-12 semantic PicK certificate."""

from __future__ import annotations
import hashlib, itertools, json
from pathlib import Path

CERT = Path(__file__).with_name("j2-semantic-kc-picard-basis.json")
EXPECTED_SOURCE = ("MichaelStollBayreuth/Verification",
                   "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
                   "Cuboids/cuboids.magma")
EXPECTED_INDLISTK = [2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54,64,67,72]

def det_bareiss(a):
    n=len(a); m=[r[:] for r in a]; sign=1; prev=1
    for k in range(n-1):
        if m[k][k]==0:
            p=next((r for r in range(k+1,n) if m[r][k]),None)
            if p is None: return 0
            m[k],m[p]=m[p],m[k]; sign=-sign
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                m[i][j]=(m[i][j]*pivot-m[i][k]*m[k][j])//prev
        prev=pivot
        for i in range(k+1,n): m[i][k]=0
        for j in range(k+1,n): m[k][j]=0
    return sign*m[-1][-1]

def gram(g17, inc, triple):
    g=[r[:] + [inc[i][c] for c in triple] for i,r in enumerate(g17)]
    for a,c in enumerate(triple):
        row=[inc[i][c] for i in range(17)]+[0,0,0]
        row[17+a]=-2
        g.append(row)
    assert all(g[i][j]==g[j][i] for i in range(20) for j in range(20))
    return g

def canonical_sha(d):
    d=dict(d); d.pop("canonical_sha256",None)
    raw=json.dumps(d,sort_keys=True,separators=(",",":")).encode()
    return hashlib.sha256(raw).hexdigest()

def main():
    c=json.loads(CERT.read_text())
    s=c["upstream_source_lock"]
    assert (s["repo"],s["commit"],s["path"])==EXPECTED_SOURCE
    assert s["indlistK_1based"]==EXPECTED_INDLISTK
    assert s["load_bearing_assertion"]=="sub<PicK | [qPicK(BigK.j) : j in indlistK]> eq PicK"
    assert c["curve_slots_1based"]==EXPECTED_INDLISTK[:17]
    assert len(c["semantic_point_order"])==12
    g17=c["gram17"]; inc=c["incidence17x12"]
    assert len(g17)==17 and all(len(r)==17 for r in g17)
    assert len(inc)==17 and all(len(r)==12 for r in inc)

    counts={}
    for t in itertools.combinations(range(12),3):
        d=det_bareiss(gram(g17,inc,t))
        counts[d]=counts.get(d,0)+1
    assert counts=={0:120,-32:64,-128:32,-512:4}
    assert c["triple_determinant_distribution"]=={str(k):v for k,v in counts.items()}
    assert c["minimum_nonzero_abs_triple_determinant"]==32

    t=tuple(c["semantic_exceptional_indices_0based"])
    sg=gram(g17,inc,t)
    assert det_bareiss(sg)==-32==c["semantic_gram20_determinant"]
    assert c["picK_abs_discriminant"]==32
    assert c["semantic_basis_index_in_picK"]==1

    e8=[0]*20; e8[7]=1
    e18=[0]*20; e18[17]=1
    assert c["j2_branch_carrier"]["marked_semantic_picK_coords"]==e8
    assert c["j2_branch_carrier"]["same_picK_class_as"]=="CsK[21]"
    assert c["j2_infinity_exceptional"]["marked_semantic_picK_coords"]==e18
    assert c["j2_infinity_exceptional"]["point"]=="[1:0:0:0:-1:-1]"
    assert c["ptsk_order_dependency"]=="ELIMINATED"
    assert c["magma_qPicK_coordinate_dependency"]=="ELIMINATED_BY_SEMANTIC_UNIMODULAR_BASIS"
    assert c["stage33_12_visible_progress_after_certificate"]=="4/5"
    assert c["stage33_12_closed_exact"] is False and c["stage33_13_released"] is False
    assert c["canonical_sha256"]==canonical_sha(c)
    print(json.dumps({"status":"PASS_EXACT","canonical_sha256":c["canonical_sha256"],
                      "semantic_det":-32,"picK_abs_discriminant":32,
                      "j2_branch_carrier_coords":e8,"j2_infinity_exceptional_coords":e18},
                     sort_keys=True))

if __name__=="__main__":
    main()
