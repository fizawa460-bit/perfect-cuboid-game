#!/usr/bin/env python3
"""Materialize the exact 256 elementary H surviving the q-filtration census."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
import certify_elementary_index512_q_filtration_reduction as QF
Q2=QF.Q2
records=[];seen=set()
for H,b,t,dm in QF.iter_joint_survivors():
    if QF.twoq_dist(H)!=QF.target_2q: continue
    if QF.q2_dist(H)!=QF.target_q2: continue
    Hc=Q2.canon(H)
    if Hc in seen: raise SystemExit('duplicate q256 H')
    seen.add(Hc)
    records.append({'index':len(records),'b':int(b),'t':int(t),'delta_mask':int(dm),'H_basis_bits':[int(x) for x in Hc]})
if len(records)!=256: raise SystemExit(f'q256 materialization regression {len(records)}')
if any(len(r['H_basis_bits'])!=9 or Q2.rank(r['H_basis_bits'])!=9 for r in records): raise SystemExit('q256 rank regression')
qcert=json.loads((HERE/'elementary-index512-q-filtration-reduction.json').read_text())
if qcert['canonical_sha256']!='1e9999ab0b150803d77da0271ef5c6b87eccb353701220c7565a5fddff8c6edc': raise SystemExit('q filtration source lock moved')
cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q256_SURVIVORS_V1',
 'source_q_filtration_sha256':qcert['canonical_sha256'],
 'ambient_A2_dimension':14,'H_dimension':9,'candidate_count':256,
 'ordering':'deterministic invariant_P / even-t / delta-mask enumeration inherited from locked exact census',
 'records':records,
 'actual_index512_glue_identified':False,'full_finite_quadratic_form_isometry_certified_for_all':False,
 'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-q256-survivors.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'candidate_count':256,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
