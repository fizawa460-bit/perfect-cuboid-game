#!/usr/bin/env python3
"""Network-free exact verifier: automorphisms of T(Kc)=<4>+<8> are trivial mod 2."""
from __future__ import annotations
import hashlib, itertools, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/'j2-kc-automorphism-mod2-marking-rejection.json'
TCERT=HERE/'j2-kc-transcendental-lattice-isometry.json'
CV=HERE/'j2-cv-to-discriminant-marking-obstruction.json'
EXPECTED_T='b7f2bcfa29c01731ea2f10d22db898ad57317f140b547f91e3d3a27a0faf1010'
EXPECTED_CV='1366726812db7828e14a6f5c40d862e16b08856ba8278c9c1781f0a3d40eb5dd'

def csha(d):
    d=dict(d); d.pop('canonical_sha256',None)
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def mtgm(M,G):
    # M^T G M, 2x2 exact integers
    GM=[[sum(G[i][k]*M[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return [[sum(M[k][i]*GM[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def det(M): return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def main():
    d=json.loads(CERT.read_text()); t=json.loads(TCERT.read_text()); cv=json.loads(CV.read_text())
    assert t['canonical_sha256']==EXPECTED_T==csha(t)
    assert cv['canonical_sha256']==EXPECTED_CV==csha(cv)
    G=t['transcendental_lattice_isometry_gram']; assert G==[[4,0],[0,8]]==d['transcendental_lattice_gram']

    # Exact finite enumeration: the first column has norm 4, so a^2+2c^2=1;
    # the second has norm 8, so b^2+2d^2=2. Hence every entry lies in {-1,0,1};
    # range(-2,3) is therefore exhaustive with margin.
    iso=[]
    for a,b,c,e in itertools.product(range(-2,3), repeat=4):
        M=[[a,b],[c,e]]
        if abs(det(M))==1 and mtgm(M,G)==G: iso.append(M)
    expected=[[[-1,0],[0,-1]],[[-1,0],[0,1]],[[1,0],[0,-1]],[[1,0],[0,1]]]
    assert iso==expected==d['integral_isometry_group_exact']
    assert all([[x%2 for x in row] for row in M]==[[1,0],[0,1]] for M in iso)
    assert d['all_integral_isometries_reduce_to_identity_mod2'] is True
    assert d['b1_sign_cv_side']['stoll_substsK_index_1based']==6
    assert d['b1_sign_cv_side']['substitution']=='B1 -> -B1'
    assert d['b1_sign_cv_side']['j2_branch_pointwise_fixed'] is True
    assert d['b1_sign_cv_side']['j2_three_named_supports_pointwise_fixed'] is True
    assert d['j2_coordinate_materialized'] is False
    assert d['stage33_12_closed_exact'] is False and d['stage33_13_released'] is False
    for k in ('theorem_credit','receiver_credit','endpoint_credit','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
        assert d[k] is False
    assert d['canonical_sha256']==csha(d)
    print(json.dumps({'status':'PASS_EXACT','isometry_group_size':len(iso),'mod2_action':'IDENTITY_FOR_ALL','canonical_sha256':d['canonical_sha256']},sort_keys=True))

if __name__=='__main__': main()
