#!/usr/bin/env python3
"""Exact coordinate-sign exponent reduction for non-elementary order-512 glue.

For the seven rank-two scaled K3 pieces of L0, the coordinate sign involution
sigma_i acts +1 on piece i and -1 on the other six.  If an isotropic glue H is
stable under every sigma_i, then for h=sum h_i in H,

    h + sigma_i(h) = 2 h_i in H.

The element 2h_i is supported on a single rank-two piece and is isotropic.
Direct exhaustive enumeration of each local discriminant form shows that its
only isotropic elements are the four 2-torsion elements.  Hence 4h_i=0 for all
i and all h, so exponent(H)<=4.  All LR-surviving types containing Z/8 are
therefore impossible before any endpoint finite-q matching.
"""
import hashlib,itertools,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
LR=json.loads((HERE/'index512-abstract-glue-types-lr-retained.json').read_text())
GLUE=json.loads((HERE/'coordinate-k3-transcendental-glue-index.json').read_text())
LR_LOCK='dd14ecc255244db71a0a1fdcc8af7a5d9a8e957857dec7c879ed8c51d756746a'
if LR['canonical_sha256']!=LR_LOCK:raise SystemExit('LR source lock moved')
if not GLUE['integral_glue']['required_condition'].startswith('identify the actual isotropic order-2^9 subgroup H') or 'coordinate-sign actions' not in GLUE['integral_glue']['required_condition']:
    raise SystemExit('coordinate-sign glue requirement moved')
# local q numerators modulo 2: Kb has q=(x^2+y^2)/8; Kc/Ka have q=x^2/8+y^2/16.
def order(a,m):
    import math
    return 1 if a%m==0 else m//math.gcd(a,m)
def lcm(a,b):
    import math
    return a*b//math.gcd(a,b)
def enum(mods,kind):
    out=[]
    for x,y in itertools.product(range(mods[0]),range(mods[1])):
        iso=((x*x+y*y)%16==0) if kind=='kb' else ((2*x*x+y*y)%32==0)
        if iso:out.append({'element':[x,y],'order':lcm(order(x,mods[0]),order(y,mods[1]))})
    return out
kb=enum((8,8),'kb');mix=enum((8,16),'mix')
if len(kb)!=4 or len(mix)!=4 or max(z['order'] for z in kb+mix)!=2:
    raise SystemExit('local isotropic enumeration regression')
all_types=[tuple(x) for x in LR['abstract_H_types_after_two_exact_sequence_LR_filter']]
elementary=(1,)*9
nonel=[x for x in all_types if x!=elementary]
rejected=[x for x in nonel if max(x)>=3]
surv=[x for x in nonel if max(x)<=2]
expected_rej=[(3,3,1,1,1),(3,2,2,1,1),(3,2,1,1,1,1),(3,1,1,1,1,1,1)]
expected_surv=[(2,2,2,2,1),(2,2,2,1,1,1),(2,2,1,1,1,1,1),(2,1,1,1,1,1,1,1)]
if rejected!=expected_rej or surv!=expected_surv:raise SystemExit('coordinate-sign type census regression')
cert={'schema':'STAGE33_07_INDEX512_NONELEMENTARY_COORDINATE_SIGN_EXPONENT_REDUCTION_V1','source_locks':{'LR_sha256':LR_LOCK,'coordinate_k3_glue_index_sha256':GLUE['canonical_sha256']},'local_piece_isotropic_enumeration':{'Kb_Z8xZ8':kb,'Kc_Ka_Z8xZ16':mix},'lemma':'coordinate-sign stability gives 2h_i=h+sigma_i(h) in H; local isotropy forces ord(2h_i)<=2; hence exponent(H)<=4','non_elementary_types_before':8,'rejected_Z8_types':[list(x) for x in rejected],'surviving_exponent_le4_types':[list(x) for x in surv],'non_elementary_types_after':4,'actual_index512_glue_identified':False,'next_exact_leaf':'L33-07-CLASSIFY-4-EXPONENT4-NONELEMENTARY-TYPES-BY-SIGN-STABLE-ISOTROPIC-EMBEDDING-ENDPOINT-Q-AND-ACTION','new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-COORDINATE-SIGN-CENSUS-PLUS-NONELEMENTARY-4-EXPONENT4-TYPES','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'index512-nonelementary-coordinate-sign-exponent-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':8,'after':4,'rejected_Z8_types':[list(x) for x in rejected],'survivors':[list(x) for x in surv],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
