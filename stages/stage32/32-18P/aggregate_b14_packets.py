#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

MAGIC=b'S32D16C1'
RECORD_SIZE=141
LOCK_KEYS=['aut_group_order','stable_aut_content_sha256','prepared_input_sha256','canonical_bundle_sha256','dfs_symmetry_breaker_count']
EXPECTED_B12_SHA='03616e7c03cdca9b4c8408cec671b0ef6bd26713fe5ca60e2021a7d6e897abd5'
EXPECTED_B12_COUNT=8697
EXPECTED_B12_HIST={'0':1,'2':1,'4':7,'6':28,'8':223,'10':1170,'12':7267}


def read_records(path:pathlib.Path):
    raw=path.read_bytes()
    if raw[:8]!=MAGIC: raise RuntimeError(f'bad dump magic: {path}')
    body=raw[8:]
    if len(body)%RECORD_SIZE: raise RuntimeError(f'truncated dump: {path}')
    return [body[i:i+RECORD_SIZE] for i in range(0,len(body),RECORD_SIZE)]


def sha(path:pathlib.Path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--packets',type=pathlib.Path,required=True)
    ap.add_argument('--manifest',type=pathlib.Path,required=True)
    ap.add_argument('--audited-b12-dump',type=pathlib.Path,required=True)
    ap.add_argument('--output-json',type=pathlib.Path,required=True)
    ap.add_argument('--output-dump',type=pathlib.Path,required=True)
    ap.add_argument('--certificate',type=pathlib.Path,required=True)
    a=ap.parse_args()
    manifest=json.loads(a.manifest.read_text())
    assert manifest['schema']=='STAGE32_18O_D16_B14_PACKET_MANIFEST_V1'
    assert manifest['bound']==14 and manifest['packet_count']==256
    assert manifest['coverage_exact'] is True and manifest['residues_exactly_once'] is True
    manifest_sha=sha(a.manifest)

    docs={}
    for p in a.packets.rglob('packet-certificate.json'):
        d=json.loads(p.read_text())
        pid=int(d['packet_id'])
        if pid in docs: raise RuntimeError(f'duplicate packet certificate {pid}')
        docs[pid]=(p,d)
    if set(docs)!=set(range(256)):
        missing=sorted(set(range(256))-set(docs)); extra=sorted(set(docs)-set(range(256)))
        raise RuntimeError(f'packet certificate coverage mismatch missing={missing} extra={extra}')
    walls={pid:d['status'] for pid,(p,d) in docs.items() if d.get('status')!='COMPLETE'}
    if walls: raise RuntimeError(f'production has unresolved packet resource walls: {walls}')

    all_records=[]; hist={}; residues=[]; lock=None; packet_inventory=[]
    for pid in range(256):
        p,d=docs[pid]
        expected=manifest['packets'][pid]
        if d.get('bound')!=14 or d.get('manifest_sha256')!=manifest_sha: raise RuntimeError(f'packet metadata mismatch {pid}')
        if d.get('residues')!=expected['residues']: raise RuntimeError(f'packet residue mismatch {pid}')
        if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True: raise RuntimeError(f'missing traversal certificate {pid}')
        if d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True: raise RuntimeError(f'missing exact symmetry certificate {pid}')
        here=tuple(d.get(k) for k in LOCK_KEYS)
        if lock is None: lock=here
        if here!=lock: raise RuntimeError(f'source-lock mismatch packet {pid}')
        bins=list(p.parent.glob('packet-canonical.bin'))
        if len(bins)!=1: raise RuntimeError(f'packet dump missing {pid}')
        bp=bins[0]; rs=read_records(bp)
        if len(rs)!=int(d['canonical_survivors_including_zero']): raise RuntimeError(f'packet record count mismatch {pid}')
        if sha(bp)!=d['canonical_dump_sha256']: raise RuntimeError(f'packet dump SHA mismatch {pid}')
        all_records.extend(rs); residues.extend(int(x) for x in d['residues'])
        for k,v in d['canonical_norm_histogram'].items(): hist[str(k)]=hist.get(str(k),0)+int(v)
        packet_inventory.append({'packet_id':pid,'tier':d['tier'],'residues':d['residues'],'canonical_survivors_including_zero':d['canonical_survivors_including_zero'],'canonical_dump_sha256':d['canonical_dump_sha256'],'packet_runtime_seconds':d.get('packet_runtime_seconds')})
    if sorted(residues)!=list(range(1024)): raise RuntimeError('logical h54 residue coverage is not exactly 0..1023')
    if len(all_records)!=len(set(all_records)): raise RuntimeError('duplicate canonical record across production packets')
    rec_hist={}
    for r in all_records: rec_hist[str(r[0])]=rec_hist.get(str(r[0]),0)+1
    if rec_hist!=hist: raise RuntimeError(f'global histogram mismatch records={rec_hist} certificates={hist}')

    b12sha=sha(a.audited_b12_dump)
    if b12sha!=EXPECTED_B12_SHA: raise RuntimeError(f'audited b12 dump SHA mismatch {b12sha}')
    b12=read_records(a.audited_b12_dump)
    if len(b12)!=EXPECTED_B12_COUNT: raise RuntimeError(f'audited b12 count mismatch {len(b12)}')
    b12hist={}
    for r in b12: b12hist[str(r[0])]=b12hist.get(str(r[0]),0)+1
    if b12hist!=EXPECTED_B12_HIST: raise RuntimeError(f'audited b12 histogram mismatch {b12hist}')
    predecessor=[r for r in all_records if r[0]<=12]
    if len(predecessor)!=len(b12) or set(predecessor)!=set(b12): raise RuntimeError('b14 norm<=12 predecessor set differs from hostile-audited b12')

    ordered=sorted(all_records)
    a.output_dump.parent.mkdir(parents=True,exist_ok=True)
    a.output_dump.write_bytes(MAGIC+b''.join(ordered))
    dump_sha=sha(a.output_dump)
    locks=dict(zip(LOCK_KEYS,lock))
    summary={
      'schema':'STAGE32_18P_D16_B14_EXACT_PACKET_AGGREGATE_V1','status':'COMPLETE','bound':14,
      'packet_count':256,'logical_parent_residue_count':1024,'packet_manifest_sha256':manifest_sha,
      'canonical_survivors_including_zero':len(ordered),'canonical_nonzero_survivors':len(ordered)-hist.get('0',0),
      'canonical_norm_histogram':hist,'new_norm14_canonical_survivors':hist.get('14',0),
      'canonical_dump_sha256':dump_sha,'canonical_pairings_unique':True,'logical_residue_partition_exact':True,
      'audited_b12_predecessor_set_identical':True,'audited_b12_predecessor_dump_sha256':b12sha,
      'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,'packet_inventory':packet_inventory,**locks,
      'D16_B14_NUMERICAL_CREDIT':False,'D16_B14_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT':True,
      'GLOBAL_B14_AGGREGATION_COMPLETE':True,'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,'CONTROLLER_MODIFIED':False
    }
    a.output_json.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    cert={
      'schema':'STAGE32_18P_D16_B14_PRODUCTION_CERTIFICATE_V1',
      'verdict':'PASS_EXACT_D16_B14_PACKET_PRODUCTION_PENDING_HOSTILE_AUDIT',
      'bound':14,'packet_count':256,'logical_residue_partition_exact':True,'audited_b12_predecessor_set_identical':True,
      'canonical_survivors_including_zero':len(ordered),'canonical_norm_histogram':hist,'new_norm14_canonical_survivors':hist.get('14',0),
      'canonical_dump_sha256':dump_sha,'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
      'D16_B14_NUMERICAL_CREDIT':False,'D16_B14_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT':True,
      'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,'CONTROLLER_MODIFIED':False
    }
    a.certificate.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'verdict':cert['verdict'],'canonical':len(ordered),'hist':hist,'new_norm14':hist.get('14',0),'dump_sha256':dump_sha},sort_keys=True))

if __name__=='__main__': main()
