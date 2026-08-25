#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
D=HERE/'coordinate-sign-shards';rows=[];locks=[]
for i in range(16):
    x=json.loads((D/f'elementary-index512-q64-coordinate-sign-shard-{i}.json').read_text())
    if x['shard_index']!=i or x['shard_count']!=16 or x['candidate_count']!=4:raise SystemExit('coordinate-sign shard metadata regression')
    rows.extend(x['results']);locks.append(x['canonical_sha256'])
rows.sort(key=lambda r:int(r['index']))
if [int(r['index']) for r in rows]!=list(range(64,128)):raise SystemExit('coordinate-sign q64 coverage regression')
surv=[int(r['index']) for r in rows if r['simultaneous_q_cc_ct_7sign_conjugacy']]
cert={'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q64_COORDINATE_SIGN_CENSUS_V1','candidate_count_before':64,'simultaneous_q_cc_ct_7sign_survivor_count':len(surv),'rejected_count':64-len(surv),'survivor_indices':surv,'shard_certificate_sha256':locks,'results':rows,'actual_index512_glue_identified':False,'next_exact_leaf':'L33-07-CLASSIFY-COORDINATE-SIGN-SURVIVORS-AGAINST-INTEGRAL-ENDPOINT-T' if surv else 'L33-07-ELEMENTARY-ORDER512-GLUE-REJECTED-BY-FULL-RATIONAL-SIGN-ACTION','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-q64-coordinate-sign-census.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':64,'survivors':len(surv),'rejected':64-len(surv),'survivor_indices':surv,'certificate_sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
