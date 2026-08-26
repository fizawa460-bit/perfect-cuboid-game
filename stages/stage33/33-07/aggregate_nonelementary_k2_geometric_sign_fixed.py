#!/usr/bin/env python3
"""Aggregate the exact 64-shard k=2 geometric-sign fixed-filtration census."""
import hashlib,json
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
SD=HERE/'k2-geometric-sign-fixed-shards';MAN=HERE/'nonelementary-k2-geometric-sign-fixed-manifest.json';OUT=HERE/'nonelementary-k2-geometric-sign-fixed-census.json'
man=json.loads(MAN.read_text());mu=dict(man);ms=mu.pop('canonical_sha256',None);mh=hashlib.sha256(json.dumps(mu,sort_keys=True,separators=(',',':')).encode()).hexdigest()
if ms!=mh:raise SystemExit('manifest hash regression')
files=sorted(SD.glob('nonelementary-k2-geometric-sign-fixed-shard-*.json'))
if len(files)!=64:raise SystemExit(f'expected 64 shard files, got {len(files)}')
seen=set();checked=weighted=surv=wsurv=0;rej=Counter();shas={}
for p in files:
 d=json.loads(p.read_text());u=dict(d);s=u.pop('canonical_sha256',None);h=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 if s!=h or d.get('manifest_sha256')!=ms or d.get('arithmetic_generators_used')!=[]:raise SystemExit(f'shard hash/firewall regression {p.name}')
 i=int(d['shard_index'])
 if i in seen or int(d['shard_count'])!=64:raise SystemExit('shard identity regression')
 seen.add(i);shas[str(i)]=s;checked+=int(d['representative_sections_checked']);weighted+=int(d['weighted_H_checked']);surv+=int(d['representative_section_survivors']);wsurv+=int(d['weighted_H_survivors']);rej.update({k:int(v) for k,v in d['rejection_layers'].items()})
if seen!=set(range(64)):raise SystemExit('missing shard')
if checked!=int(man['representative_section_count']) or weighted!=int(man['weighted_H_count']):raise SystemExit(f'global coverage regression {(checked,weighted)}')
if sum(rej.values())+surv!=checked:raise SystemExit('rejection/survivor partition regression')
zero=(surv==0 and wsurv==0)
cert={
 'schema':'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_SIGN_FIXED_CENSUS_V1','manifest_sha256':ms,'shard_certificate_sha256':shas,
 'arithmetic_generators_used':[],'geometric_coordinate_signs_used':7,
 'family_count':867,'representative_sections_checked':checked,'weighted_H_checked':weighted,'rejection_layers':dict(sorted(rej.items())),
 'representative_section_survivors':surv,'weighted_H_survivors':wsurv,
 'all_2183168_Q2_affine_sections_checked_exactly_once':checked==2183168,
 'all_129468416_weighted_H_covered_exactly':weighted==129468416,
 'full_affine_fixed_filtration_census_certified':True,
 'k2_nonelementary_type_rejected_by_geometric_sign_fixed_filtration':zero,
 'k2_nonelementary_type_rejected':zero,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'checked':checked,'weighted_H':weighted,'survivors':surv,'weighted_survivors':wsurv,'k2_rejected':zero,'rejections':dict(rej),'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
