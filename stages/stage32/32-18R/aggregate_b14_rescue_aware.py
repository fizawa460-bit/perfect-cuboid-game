#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,pathlib
MAGIC=b'S32D16C1'; RECORD_SIZE=141
PACKET_SCHEMA='STAGE32_18O_D16_B14_PACKET_PILOT_V1'
HOT_SCHEMA='STAGE32_18Q_D16_B14_EXACT_LOGICAL_HOT_PARENT_V1'
LOCK_KEYS=['aut_group_order','stable_aut_content_sha256','prepared_input_sha256','canonical_bundle_sha256','dfs_symmetry_breaker_count']
BULK_EXCLUDED={0,15,63,64,173}; BULK_IDS=[i for i in range(256) if i not in BULK_EXCLUDED]; PILOT_IDS=[63,64,173]
HOT_PACKET_TO_PRIMARY={0:748,15:26}
ALLOWED_BULK_SOURCES={'18P_frozen_snapshot','18T_prior_success_carryover','18T_union_resume_current'}

def read_records(p:pathlib.Path):
    raw=p.read_bytes()
    if raw[:8]!=MAGIC: raise RuntimeError(f'bad dump magic {p}')
    body=raw[8:]
    if len(body)%RECORD_SIZE: raise RuntimeError(f'truncated dump {p}')
    return [body[i:i+RECORD_SIZE] for i in range(0,len(body),RECORD_SIZE)]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def packet_dir(root,pid): return root/str(pid)

def load_packet(root,pid,manifest,lock):
    ddir=packet_dir(root,pid); jp=ddir/'packet-certificate.json'; bp=ddir/'packet-canonical.bin'
    if not jp.exists() or not bp.exists(): raise RuntimeError(f'missing complete packet files {pid}')
    d=json.loads(jp.read_text())
    if d.get('schema')!=PACKET_SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=14: raise RuntimeError(f'bad packet cert {pid}')
    if int(d.get('packet_id',-1))!=pid: raise RuntimeError(f'packet id mismatch {pid}')
    expected=[int(x) for x in manifest['packets'][pid]['residues']]
    if [int(x) for x in d.get('residues',[])]!=expected: raise RuntimeError(f'packet residues mismatch {pid}')
    if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True or d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True: raise RuntimeError(f'missing exact cert {pid}')
    here=tuple(d.get(k) for k in LOCK_KEYS)
    if lock[0] is None: lock[0]=here
    if here!=lock[0]: raise RuntimeError(f'source lock mismatch packet {pid}')
    rs=read_records(bp)
    if len(rs)!=int(d.get('canonical_survivors_including_zero',-1)): raise RuntimeError(f'packet record count mismatch {pid}')
    if sha(bp)!=d.get('canonical_dump_sha256'): raise RuntimeError(f'packet dump SHA mismatch {pid}')
    rh={}
    for r in rs: rh[str(r[0])]=rh.get(str(r[0]),0)+1
    if rh!={str(k):int(v) for k,v in d.get('canonical_norm_histogram',{}).items()}: raise RuntimeError(f'packet hist mismatch {pid}')
    return d,rs,expected

def load_hot(root,packet_id,primary,manifest,lock):
    ddir=root/str(primary); jp=ddir/f'd16-b14-logical-primary-{primary}-of1024.json'; bp=ddir/f'd16-b14-logical-primary-{primary}-of1024.bin'
    if not jp.exists() or not bp.exists(): raise RuntimeError(f'missing logical hot parent {primary}')
    d=json.loads(jp.read_text())
    if d.get('schema')!=HOT_SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=14: raise RuntimeError(f'bad hot cert {primary}')
    if (d.get('shard_id'),d.get('shard_count'),d.get('split_coordinate'))!=(primary,1024,54): raise RuntimeError(f'bad hot logical partition {primary}')
    if d.get('two_stage_partition_certificate') is not True or d.get('secondary_partition_complete') is not True or d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True: raise RuntimeError(f'incomplete hot logical parent {primary}')
    expected=[int(x) for x in manifest['packets'][packet_id]['residues']]
    if expected!=[primary]: raise RuntimeError(f'manifest hot packet {packet_id} is not singleton {primary}: {expected}')
    here=tuple(d.get(k) for k in LOCK_KEYS)
    if lock[0] is None: lock[0]=here
    if here!=lock[0]: raise RuntimeError(f'source lock mismatch hot {primary}')
    rs=read_records(bp)
    if len(rs)!=int(d.get('canonical_survivors_including_zero',-1)): raise RuntimeError(f'hot record count mismatch {primary}')
    if sha(bp)!=d.get('canonical_dump_sha256'): raise RuntimeError(f'hot dump SHA mismatch {primary}')
    rh={}
    for r in rs: rh[str(r[0])]=rh.get(str(r[0]),0)+1
    if rh!={str(k):int(v) for k,v in d.get('canonical_norm_histogram',{}).items()}: raise RuntimeError(f'hot hist mismatch {primary}')
    return d,rs,expected

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--bulk',type=pathlib.Path,required=True); ap.add_argument('--pilot',type=pathlib.Path,required=True); ap.add_argument('--hot',type=pathlib.Path,required=True); ap.add_argument('--manifest',type=pathlib.Path,required=True); ap.add_argument('--audited-b12-dump',type=pathlib.Path,required=True); ap.add_argument('--inventory',type=pathlib.Path,required=True); ap.add_argument('--output-json',type=pathlib.Path,required=True); ap.add_argument('--output-dump',type=pathlib.Path,required=True); ap.add_argument('--certificate',type=pathlib.Path,required=True)
    a=ap.parse_args(); manifest=json.loads(a.manifest.read_text()); inv=json.loads(a.inventory.read_text())
    if manifest.get('schema')!='STAGE32_18O_D16_B14_PACKET_MANIFEST_V1' or manifest.get('packet_count')!=256 or manifest.get('coverage_exact') is not True or manifest.get('residues_exactly_once') is not True: raise RuntimeError('bad packet manifest')
    if inv.get('schema')!='STAGE32_18R_B14_INPUT_ARTIFACT_INVENTORY_V4' or inv.get('handoff_exact') is not True: raise RuntimeError('bad 18R union input inventory')

    legacy_n=int(inv.get('legacy_packet_count',-1)); resume_n=int(inv.get('resume_complement_packet_count',-1))
    carry_n=int(inv.get('carryover_packet_count',-1)); current_n=int(inv.get('current_resume_packet_count',-1))
    if legacy_n+resume_n!=len(BULK_IDS) or carry_n+current_n!=resume_n: raise RuntimeError('bad union handoff counts')
    bulk_sources={int(k):v for k,v in inv.get('bulk_packet_sources',{}).items()}
    if set(bulk_sources)!=set(BULK_IDS): raise RuntimeError('bulk source provenance incomplete')
    if any(v not in ALLOWED_BULK_SOURCES for v in bulk_sources.values()): raise RuntimeError('unknown bulk source provenance')
    if sum(v=='18P_frozen_snapshot' for v in bulk_sources.values())!=legacy_n: raise RuntimeError('legacy provenance count mismatch')
    if sum(v=='18T_prior_success_carryover' for v in bulk_sources.values())!=carry_n: raise RuntimeError('carry provenance count mismatch')
    if sum(v=='18T_union_resume_current' for v in bulk_sources.values())!=current_n: raise RuntimeError('current resume provenance count mismatch')

    lock=[None]; records=[]; hist={}; residues=[]; packet_sources={}; packet_counts={}
    for pid in BULK_IDS:
        d,rs,rids=load_packet(a.bulk,pid,manifest,lock); records.extend(rs); residues.extend(rids); packet_sources[str(pid)]=bulk_sources[pid]; packet_counts[str(pid)]=len(rs)
    for pid in PILOT_IDS:
        d,rs,rids=load_packet(a.pilot,pid,manifest,lock); records.extend(rs); residues.extend(rids); packet_sources[str(pid)]='18O_pilot_reuse'; packet_counts[str(pid)]=len(rs)
    for pid,primary in HOT_PACKET_TO_PRIMARY.items():
        d,rs,rids=load_hot(a.hot,pid,primary,manifest,lock); records.extend(rs); residues.extend(rids); packet_sources[str(pid)]=f'18S_hostile_audited_logical_primary_{primary}'; packet_counts[str(pid)]=len(rs)
    if set(map(int,packet_sources))!=set(range(256)): raise RuntimeError('logical packet coverage incomplete')
    if sorted(residues)!=list(range(1024)) or len(residues)!=1024: raise RuntimeError('logical residue coverage not exactly once')
    if len(records)!=len(set(records)): raise RuntimeError('duplicate canonical records across logical packets')
    for r in records: hist[str(r[0])]=hist.get(str(r[0]),0)+1
    b12=read_records(a.audited_b12_dump)
    if sha(a.audited_b12_dump)!='03616e7c03cdca9b4c8408cec671b0ef6bd26713fe5ca60e2021a7d6e897abd5': raise RuntimeError('audited b12 SHA mismatch')
    predecessor=sorted(r for r in records if r[0]<=12)
    if predecessor!=sorted(b12): raise RuntimeError('norm<=12 predecessor set differs from hostile-audited b12')
    expected_lower={'0':1,'2':1,'4':7,'6':28,'8':223,'10':1170,'12':7267}
    lower={k:v for k,v in hist.items() if int(k)<=12}
    if lower!=expected_lower: raise RuntimeError(f'lower histogram mismatch {lower}')
    records=sorted(records); a.output_dump.parent.mkdir(parents=True,exist_ok=True); a.output_dump.write_bytes(MAGIC+b''.join(records)); dump_sha=sha(a.output_dump)
    aut,stable,inputsha,bundle,breakers=lock[0]
    if aut!=1536 or breakers!=256: raise RuntimeError('bad final group/breaker lock')
    out={'schema':'STAGE32_18R_D16_B14_RESCUE_AWARE_GLOBAL_AGGREGATE_V3','status':'COMPLETE','bound':14,
        'aut_group_order':1536,'stable_aut_content_sha256':stable,'prepared_input_sha256':inputsha,'canonical_bundle_sha256':bundle,
        'dfs_symmetry_breaker_count':256,'logical_packet_count':256,'logical_packet_partition_exact':True,
        'logical_residue_count':1024,'logical_residue_partition_exact':True,'hot_rescue_primary_residues':[26,748],
        'reused_pilot_packet_ids':PILOT_IDS,'bulk_packet_count':len(BULK_IDS),
        'legacy_frozen_packet_count':legacy_n,'resume_complement_packet_count':resume_n,
        'carryover_packet_count':carry_n,'current_resume_packet_count':current_n,
        'canonical_survivors_including_zero':len(records),'canonical_nonzero_survivors':len(records)-hist.get('0',0),
        'canonical_norm_histogram':hist,'new_norm14_canonical_survivors':hist.get('14',0),'canonical_dump_sha256':dump_sha,
        'audited_b12_predecessor_set_identical':True,'audited_b12_predecessor_count':len(b12),
        'audited_b12_dump_sha256':'03616e7c03cdca9b4c8408cec671b0ef6bd26713fe5ca60e2021a7d6e897abd5',
        'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,'all_symmetry_branch_rejections_exact_rational_cauchy_schwarz':True,
        'telemetry_semantics':'No hypothetical single-run global nodes/trials total is claimed; packet and nested-rescue executions repeat pre-split work.',
        'packet_sources':packet_sources,'packet_record_counts':packet_counts,'artifact_inventory':inv,
        'GLOBAL_B14_AGGREGATION_COMPLETE':True,'D16_B14_NUMERICAL_CREDIT':False,'D16_B14_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT':True,
        'AUDIT_STATUS':'PENDING','FULL_D16_G0_ROW_COMPLETE':False,'FULL_D176_D192_NUMERICAL_ORBIT_CENSUS':False,
        'R29_LG2_NUMERICAL_COMPONENT_COMPLETE':False,'R29_LG2':'NOT_DISCHARGED','THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,'CONTROLLER_MODIFIED':False}
    a.output_json.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    cert={'schema':'STAGE32_18R_D16_B14_RESCUE_AWARE_CERTIFICATE_V3',
        'verdict':'PASS_EXACT_RESCUE_AWARE_D16_B14_PRODUCTION_PENDING_HOSTILE_AUDIT',
        'canonical_survivors_including_zero':len(records),'canonical_nonzero_survivors':out['canonical_nonzero_survivors'],
        'canonical_norm_histogram':hist,'new_norm14_canonical_survivors':hist.get('14',0),'canonical_dump_sha256':dump_sha,
        'logical_packet_partition_exact':True,'logical_residue_partition_exact':True,
        'legacy_frozen_packet_count':legacy_n,'resume_complement_packet_count':resume_n,
        'carryover_packet_count':carry_n,'current_resume_packet_count':current_n,
        'hot_rescue_primary_residues':[26,748],'audited_b12_predecessor_set_identical':True,
        'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,'GLOBAL_B14_AGGREGATION_COMPLETE':True,
        'D16_B14_NUMERICAL_CREDIT':False,'D16_B14_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT':True,
        'AUDIT_STATUS':'PENDING','FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,'CONTROLLER_MODIFIED':False}
    a.certificate.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n'); print(json.dumps(cert,sort_keys=True))
if __name__=='__main__': main()
