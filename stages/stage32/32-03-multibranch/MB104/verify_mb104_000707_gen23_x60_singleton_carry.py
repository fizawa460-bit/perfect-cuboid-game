#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
INDEX=HERE/'MB104-000707-GEN23-X60-SINGLETON-CARRY-INDEX.json'
RESIDUAL=HERE/'MB104-000707-GEN24-X60-SINGLETON-RESIDUAL30.json'
SOURCE=HERE/'MB104-000707-GEN23-X60-SINGLETON-CARRY-SOURCE.json'
PACKET_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_X60_SINGLETON_PACKET_V1'
AGG_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_X60_SINGLETON_AGGREGATE_V1'
PAYLOAD_SCHEMA='STAGE32_MB104_000707_GEN23_X60_SINGLETON_PACKET_CARRY_BUNDLE_V1'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ck(r): return (int(r['primary_value']),int(r['secondary_residue']),int(r['fixed_x61_value']),int(r['x60_residue']),int(r['fixed_x60_value']))

def decode_carry(index_path=INDEX,residual_path=RESIDUAL,source_path=SOURCE,out_dir=None):
    idx=json.loads(Path(index_path).read_text()); res=json.loads(Path(residual_path).read_text()); src=json.loads(Path(source_path).read_text())
    assert idx['schema']=='STAGE32_MB104_000707_GEN23_X60_SINGLETON_DURABLE_PACKET_CARRY_CHUNK_INDEX_V1' and idx['encoding']=='gzip+base64-chunks' and idx['exact_bytes_not_regenerated'] is True
    assert idx['producing_generation']==23 and idx['producing_mode']=='RECOVERY' and idx['producing_execution_head']=='99601aef02a82858d32729dec344f103ae40af09' and idx['producing_workflow_run_id']==35663858139
    assert idx['source_materialization_head']=='f719debfb489f337ac8f6ea15f065bb7fb9e18f8' and idx['source_materialization_run_id']==35697313915 and idx['source_materialization_artifact_id']==10681410788
    assert idx['source_materialization_artifact_zip_sha256']=='efa82a817b0eab11c84dd2a170a01611902d9857b98ec664c750d7f226d02c14'
    assert all(v is False for v in idx['credit_firewall'].values())
    parts=[]
    for i,row in enumerate(idx['chunks']):
        assert int(row['order'])==i
        s=(HERE/row['filename']).read_text().strip(); assert len(s)==int(row['char_count']) and hashlib.sha256(s.encode()).hexdigest()==row['sha256']; parts.append(s)
    packed=base64.b64decode(''.join(parts),validate=True); assert len(packed)==int(idx['compressed_byte_length']) and hashlib.sha256(packed).hexdigest()==idx['gzip_sha256']=='ca41d5f6c019bc661aefea44f2df446905eb82ad16c8f9e7c6360f3fbb94fa9f'
    raw=gzip.decompress(packed); assert len(raw)==int(idx['byte_length']) and hashlib.sha256(raw).hexdigest()==idx['payload_sha256']=='ef24717dbe8c2987e7bee4892184988dbc1946b5593006fff21ad53466470504'; p=json.loads(raw)
    assert p['schema']==PAYLOAD_SCHEMA and p['producing_generation']==23 and p['producing_mode']=='RECOVERY' and p['producing_execution_head']==idx['producing_execution_head'] and p['producing_workflow_run_id']==idx['producing_workflow_run_id']
    assert p['packet_count']==idx['packet_count']==62 and p['singleton_child_count']==idx['singleton_child_count']==311 and p['complete_singleton_child_count']==idx['complete_singleton_child_count']==281 and p['incomplete_singleton_child_count']==idx['incomplete_singleton_child_count']==30
    assert len(p['certificates'])==62 and len(p['complete_children'])==281 and len(p['incomplete_children'])==30
    complete=[]; incomplete=[]; canon={}; seen=set()
    for rec in p['certificates']:
        rawc=base64.b64decode(rec['base64'],validate=True); assert hashlib.sha256(rawc).hexdigest()==rec['certificate_file_sha256']; d=json.loads(rawc)
        assert d['schema']==PACKET_SCHEMA and d['provenance']=={'producing_generation':23,'producing_mode':'RECOVERY'} and d['semantic_source_locks']==p['source_locks'] and all(v is False for v in d['credit_firewall'].values())
        cl=d['canonical_sha256_without_this_field']; b=dict(d); b.pop('canonical_sha256_without_this_field'); assert csha(b)==cl==rec['canonical_sha256']
        part=d['partition']; key=(int(part['primary_value']),int(part['secondary_residue']),int(part['fixed_x61_value']),int(part['x60_residue'])); assert key not in seen; seen.add(key); canon[f'{key[0]}:{key[1]}:{key[2]}:{key[3]}']=cl
        assert part['coverage_is_exact_disjoint'] is True and len(part['x60_singleton_values'])==len(d['children'])==int(d['result']['child_count'])
        cc=0
        for child in d['children']:
            cb=dict(child); ch=cb.pop('canonical_sha256_without_this_field'); assert csha(cb)==ch
            row={'primary_value':key[0],'secondary_residue':key[1],'fixed_x61_value':key[2],'x60_residue':key[3],'fixed_x60_value':int(child['fixed_x60_value']),'canonical_sha256':ch}
            if child['result']['complete']:
                assert child['status']=='COMPLETE_EXACT_X60_SINGLETON_ZERO_CREDIT' and child['solver']['final_solver_result']=='unsat' and child['solver']['reason'] is None and child['result']['integral_known140_nonnegative_solution_count']==0 and child['result']['primitive_known140_nonnegative_candidate_count']==0 and child['result']['primitive_known140_nonnegative_candidates']==[]; complete.append(row); cc+=1
            else:
                assert child['status']=='PARTIAL_UNKNOWN_NO_CREDIT' and child['solver']['final_solver_result']=='unknown' and child['solver']['reason']=='timeout'; row.update({'solver_result':'unknown','reason':'timeout'}); incomplete.append(row)
        assert cc==int(d['result']['complete_child_count']) and d['result']['complete'] is (cc==int(d['result']['child_count']))
        if out_dir is not None:
            out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); (out/rec['certificate_filename']).write_bytes(rawc)
    complete.sort(key=ck); incomplete.sort(key=ck); assert complete==p['complete_children'] and incomplete==p['incomplete_children']
    ar=p['aggregate_certificate']; araw=base64.b64decode(ar['base64'],validate=True); assert hashlib.sha256(araw).hexdigest()==ar['certificate_file_sha256']; ag=json.loads(araw); assert ag['schema']==AGG_SCHEMA and ag['complete'] is False and ag['status']=='PARTIAL_X60_SINGLETON_RECOVERY_NO_CREDIT'
    ac=ag['canonical_sha256_without_this_field']; ab=dict(ag); ab.pop('canonical_sha256_without_this_field'); assert csha(ab)==ac==ar['canonical_sha256']==idx['aggregate_canonical_sha256']==src['aggregate_canonical_sha256']; assert ag['packet_input_canonical_sha256']==canon and ag['coverage']['observed_packet_count']==62 and ag['coverage']['missing_packets']==[] and len(ag['coverage']['incomplete_packets'])==29
    assert res['schema']=='STAGE32_MB104_000707_GEN24_X60_SINGLETON_RESIDUAL30_V1' and res['source_generation']==23 and res['source_execution_head']==idx['producing_execution_head'] and res['source_workflow_run_id']==idx['producing_workflow_run_id'] and res['complete_singleton_child_count']==281 and res['residual_timeout_singleton_count']==30 and res['residual_singletons']==incomplete and res['credit'] is False
    expected=sorted(src['expected_residual_singletons'],key=ck); actual=[{k:r[k] for k in ('primary_value','secondary_residue','fixed_x61_value','x60_residue','fixed_x60_value')} for r in incomplete]; assert actual==expected
    assert src['expected_complete_singleton_child_count']==281 and src['expected_incomplete_singleton_child_count']==30 and src['packet_count']==62 and src['singleton_child_count']==311 and all(v is False for v in src['credit_firewall'].values())
    if out_dir is not None: (Path(out_dir)/ar['certificate_filename']).write_bytes(araw)
    return idx,p

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=Path,default=INDEX); ap.add_argument('--residual',type=Path,default=RESIDUAL); ap.add_argument('--source',type=Path,default=SOURCE); ap.add_argument('--out-dir',type=Path); a=ap.parse_args(); idx,p=decode_carry(a.index,a.residual,a.source,a.out_dir); print(json.dumps({'success':True,'packets':62,'singleton_children':311,'complete_singletons':281,'residual_timeout_singletons':30,'payload_sha256':idx['payload_sha256']},sort_keys=True))
if __name__=='__main__': main()
