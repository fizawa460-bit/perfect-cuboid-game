#!/usr/bin/env bash
set -euo pipefail
ROOT="$RUNNER_TEMP/final"
mkdir -p "$ROOT/snapshot" "$ROOT/resume" "$ROOT/run14" "$ROOT/tail-summary" "$ROOT/tail"
gh run download 32972417382 -n stage32-18t-b14-source-snapshot-g2 -D "$ROOT/snapshot"
gh run download 32972417382 -n stage32-18t-b14-resume-summary-g2 -D "$ROOT/resume"
gh run download 32972417382 -p 'stage32-18t-b14-packet-*-g2' -D "$ROOT/run14"
gh run download 33003656883 -n stage32-18u-b14-tail-summary-g1 -D "$ROOT/tail-summary"
gh run download 33003656883 -p 'stage32-18t-b14-packet-*-g2' -D "$ROOT/tail"
python - <<'PY'
import json,os,pathlib,re,shutil
root=pathlib.Path(os.environ['RUNNER_TEMP'])/'final'
sp=root/'snapshot/source-completion.json'; snap=json.loads(sp.read_text())
resume=json.loads((root/'resume/resume-summary.json').read_text())
tail=json.loads((root/'tail-summary/tail-summary.json').read_text())
assert snap['schema']=='STAGE32_18T_B14_RESUME_UNION_SNAPSHOT_V3'
assert resume['schema']=='STAGE32_18T_B14_OPTIMIZED_RESUME_SUMMARY_V2'
assert tail['schema']=='STAGE32_18U_B14_THREE_RESIDUE_TAIL_SUMMARY_V1'
assert tail['status']=='COMPLETE' and tail['ready_for_final_18t_union'] is True
source=set(map(int,snap['source_complete_ids'])); complement=set(map(int,snap['source_missing_bulk_ids']))
carry=set(map(int,snap['carry_complete_packet_ids'])); remaining=set(map(int,snap['missing_bulk_ids']))
complete=set(map(int,resume['resume_complete_ids'])); missing=set(map(int,resume['resume_missing_ids']))
tail_ids={127,158,162}
assert (len(source),len(complement),len(carry),len(remaining))==(42,209,135,74)
assert missing==tail_ids and set(map(int,tail['packets']))==tail_ids
assert complete|missing==complement and not (complete&missing)
run14_expected=complete-carry
assert len(run14_expected)==71 and run14_expected|tail_ids==remaining

def scan(base):
    out={}
    for p in base.rglob('packet-certificate.json'):
        d=json.loads(p.read_text()); pid=int(d.get('packet_id',-1))
        if d.get('status')!='COMPLETE' or d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True: continue
        if pid in out: raise RuntimeError(f'duplicate COMPLETE packet {pid}')
        out[pid]=(p.parent,d)
    return out

def carry_pid(meta):
    name=str(meta.get('artifact_name',''))
    m=re.search(r'stage32-18t-b14-packet-(\d+)-g\d+$',name)
    if not m: raise RuntimeError(f'cannot derive carry packet id from artifact name: {name!r}')
    return int(m.group(1))

r14=scan(root/'run14'); tr=scan(root/'tail')
assert set(r14)==run14_expected, (sorted(run14_expected-set(r14)),sorted(set(r14)-run14_expected))
assert set(tr)==tail_ids
dstroot=root/'snapshot/carryover/packets'; dstroot.mkdir(parents=True,exist_ok=True)
ledger={carry_pid(x):x for x in snap.get('carry_packet_artifacts',[])}
assert set(ledger)==carry, (sorted(carry-set(ledger)),sorted(set(ledger)-carry))
audit=list(snap.get('carry_audit',[]))
for pid,(src,d) in sorted(r14.items()):
    dst=dstroot/str(pid)
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(src,dst)
    meta={'packet_id':pid,'run_id':32972417382,'job_id':None,'job_name':f'final-union-import packet {pid}',
          'artifact_id':None,'artifact_name':f'stage32-18t-b14-packet-{pid}-g2','artifact_digest':None}
    ledger[pid]=meta; audit.append({'kind':'packet-final-union-run14',**meta})
for pid,(src,d) in sorted(tr.items()):
    want=tail['packets'][str(pid)]
    assert d['canonical_dump_sha256']==want['dump_sha256']
    assert int(d['canonical_survivors_including_zero'])==int(want['canonical'])
    dst=dstroot/str(pid)
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(src,dst)
    meta={'packet_id':pid,'run_id':33003656883,'job_id':None,'job_name':f'18U tail rescue packet {pid}',
          'artifact_id':None,'artifact_name':f'stage32-18t-b14-packet-{pid}-g2','artifact_digest':None}
    ledger[pid]=meta; audit.append({'kind':'packet-final-union-18u-tail',**meta})
assert set(ledger)==complement
snap['carry_complete_packet_ids']=sorted(complement)
snap['carry_packet_artifacts']=[ledger[i] for i in sorted(ledger)]
snap['carry_audit']=audit
snap['missing_bulk_ids']=[]; snap['missing_hot_ids']=[]; snap['missing_regular_ids']=[]
snap['hot_matrix']=[]; snap['hot_compute_ids']=[]; snap['hot_packet_matrix']={'packet_id':[]}; snap['regular_matrix']={'packet_id':[]}
snap['final_union_handoff']=True
snap['final_union_counts']={'source':42,'carry':135,'run14':71,'tail':3,'bulk':251}
snap['final_union_source_runs']={'18T':32972417382,'18U':33003656883}
sp.write_text(json.dumps(snap,indent=2,sort_keys=True)+'\n')
out={'schema':'STAGE32_18T_B14_OPTIMIZED_RESUME_SUMMARY_V2','source_run_id':snap['source_run_id'],
     'carry_run_ids':snap['carry_run_ids']+[32972417382,33003656883],
     'source_complete_ids':snap['source_complete_ids'],'carry_complete_packet_ids':sorted(complement),
     'resume_expected_ids':sorted(complement),'resume_complete_ids':sorted(complement),
     'resume_missing_ids':[],'resume_extra_ids':[],'ready_for_18r':True,
     'final_union_handoff':True,'final_union_counts':snap['final_union_counts'],
     'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'AUDIT_STATUS':'PENDING'}
(root/'resume-summary-final.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'source':42,'carry':135,'run14':71,'tail':3,'bulk':251,'ready_for_18r':True},sort_keys=True))
PY
