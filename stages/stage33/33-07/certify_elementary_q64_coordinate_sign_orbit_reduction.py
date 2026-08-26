#!/usr/bin/env python3
"""Place the exact q+cc+ct+seven-sign survivors in integral Aut(L0) orbits."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
C=json.loads((HERE/'elementary-index512-q64-coordinate-sign-census.json').read_text())
O=json.loads((HERE/'elementary-index512-q64-integral-orbits.json').read_text())
O_LOCK='0b7a0846172706f831b030cb76984a50d47784ca1081fea99a7de65f10d27483'
if O.get('canonical_sha256')!=O_LOCK:raise SystemExit('integral-orbit source lock moved')
surv=sorted(int(x) for x in C['survivor_indices'])
if surv!=[120,121,122,123] or C['simultaneous_q_cc_ct_7sign_survivor_count']!=4:raise SystemExit('coordinate-sign survivor regression')
hit=[]
for orbit in O['orbits']:
    members=set(int(x) for x in orbit['members']);inside=sorted(members&set(surv))
    if inside:hit.append({'representative':int(orbit['representative']),'integral_orbit_size':int(orbit['size']),'surviving_labeled_embeddings':inside,'surviving_labeled_embedding_count':len(inside),'norm4_vector_count':int(orbit['norm4_vector_count'])})
if len(hit)!=1 or hit[0]['representative']!=88 or hit[0]['norm4_vector_count']!=0:raise SystemExit('coordinate-sign integral-orbit reduction regression')
cert={'schema':'STAGE33_07_ELEMENTARY_Q64_COORDINATE_SIGN_ORBIT_REDUCTION_V1',
 'source_coordinate_sign_census_sha256':C['canonical_sha256'],'source_integral_orbits_sha256':O_LOCK,
 'finite_compatible_embeddings_before':64,'integral_orbits_before':3,
 'simultaneous_q_cc_ct_seven_sign_embeddings_after':4,'surviving_labeled_embedding_indices':surv,
 'surviving_integral_orbit_count':1,'surviving_integral_orbits':hit,'rejected_integral_orbit_representatives':[64,68],
 'coordinate_sign_condition_not_constant_on_the_size_24_integral_orbit':True,
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-MATCH-FOUR-LABELED-ELEMENTARY-SIGN-EMBEDDINGS-TO-ENDPOINT-THETA-OR-REJECT',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-4-LABELED-EMBEDDINGS-IN-ONE-INTEGRAL-ORBIT-PLUS-NONELEMENTARY-1838020348224-Q4Q8-STRUCTURAL-CANDIDATES',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-q64-coordinate-sign-orbit-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':64,'surviving_labeled_embeddings':surv,'surviving_integral_orbits':[x['representative'] for x in hit],'certificate_sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
