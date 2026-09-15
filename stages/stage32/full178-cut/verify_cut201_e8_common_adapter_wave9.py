#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
RESULT=HERE/'CUT201-e8-common-adapter-wave9-result.json'
HANDOFF=HERE/'CUT201-e8-common-adapter-wave9-audit-handoff.json'
ACTIVE_RUNKEY=HERE/'runkeys/CUT201-e8-wave9.json'
EXECUTED_RUNKEY=HERE/'CUT201-e8-wave9-executed-runkey.json'
EXECUTED_WORKFLOW=HERE/'CUT201-e8-wave9-executed-workflow.yml'
WORKER=HERE/'cut201_e8_common_adapter_wave9.py'
AGGREGATOR=HERE/'aggregate_cut201_e8_wave9.py'
G11_HELPER=HERE/'cut201_e8_wave9_g11_recover.py'
G11_PREFLIGHT=HERE/'CUT201-e8-wave9-recovery-g11-preflight.json'
CUT200_VERIFY=HERE/'verify_cut200_e8_common_adapter_wave8.py'
RESULT_CANONICAL='8f9ccc51046b9559d15ee5d64ef72be35f798a740a78a85df92d865286dbd467'
HANDOFF_CANONICAL='9f1b260883222441849f4f072f2959edab7ec28c309c9078508bd4a0c2b17b7a'
EXPECTED_CLOSED=226
EXPECTED_PRUNED=25538
EXPECTED_RESIDUAL=[2835, 2982, 3123, 3124, 3125, 3126, 3127, 3130, 3136, 3137, 3138, 3140, 3145, 3147, 3151, 3158, 3172, 3173, 3174, 3176, 3181, 3183, 3186, 3207, 3208, 3209, 3210, 3218, 3233]
PRIMES=[2,3,5,7,11,13,17,31,127]
LOCKS={
 RESULT:'ebdf1f741365f7403050f22b478eeea5a7a1d653',
 HANDOFF:'975144c49a3047f948714e7920bc5dc6487a56bc',
 ACTIVE_RUNKEY:'d78dacb5bb2d8fa90b11b087e76f0673d32bbc87',
 EXECUTED_RUNKEY:'d528b05bf01082cb3250e968f0c6276ee7e99d88',
 EXECUTED_WORKFLOW:'9ef1e95f50e5f9e78767b5807eecd64101a6773a',
 WORKER:'a8be279ebc3bca4a383d4a81e4c04de7413b17b8',
 AGGREGATOR:'6e41072243ff92eabae39f522398aed2fad8df7f',
 G11_HELPER:'f885933e2a63b45629e377339f7ee556bfd8d301',
 G11_PREFLIGHT:'626aed11c74e4ded2e19cd538ae517bdfbc7ae81',
 CUT200_VERIFY:'0cfce804fffac86d60300bcd99a25e366186936e',
}
def req(ok,msg):
 if not ok: raise SystemExit('FAIL: '+msg)
def blob(path):
 raw=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def csha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def checked(path,expected):
 o=json.loads(path.read_text()); q=dict(o); claimed=q.pop('canonical_sha256_without_this_field',None); req(claimed==expected and csha(q)==expected,'canonical drift: '+path.name); return o
def split_n1_unsat_fail_closed(cut,P,blocks,prime,fixed):
 attempts=[]; s,y,_=cut.core.make_solver(P,blocks,prime,10000)
 for label,value in fixed.items(): s.add(y[label-1]==int(value))
 n1=2*y[cut.core.PACKS[0][0]-1]+sum((y[j-1] for j in blocks[0][0]),0)
 for degree in range(cut.core.TARGET_D+1):
  s.push(); s.add(n1==degree); r=str(s.check()); reason=s.reason_unknown() if r=='unknown' else None; s.pop(); rec={'prime':prime,'n1':degree,'result':r}
  if reason: rec['reason_unknown']=reason
  if r=='sat': attempts.append(rec); return False,attempts
  if r=='unknown':
   s2,y2,_=cut.core.make_solver(P,blocks,prime,60000)
   for label,value in fixed.items(): s2.add(y2[label-1]==int(value))
   n1_2=2*y2[cut.core.PACKS[0][0]-1]+sum((y2[j-1] for j in blocks[0][0]),0); s2.add(n1_2==degree); r2=str(s2.check()); rec['retry_60s_result']=r2
   if r2=='unknown': rec['retry_60s_reason_unknown']=s2.reason_unknown()
   attempts.append(rec)
   if r2!='unsat': return False,attempts
  else: attempts.append(rec)
 return True,attempts
def fresh_obstruction(cut,P,blocks,solvers,fixed):
 unknown=[]; unknown_count=0
 for p in PRIMES:
  s,y,_=solvers[p]; status,_=cut.core.check_with_fixed(s,y,fixed)
  if status=='unsat': return True,p,unknown_count,[]
  if status=='unknown': unknown_count+=1; unknown.append(p)
 fallback=[]
 for p in unknown:
  ok,attempts=split_n1_unsat_fail_closed(cut,P,blocks,p,fixed); fallback.extend(attempts)
  if ok: return True,p,unknown_count,fallback
 return False,None,unknown_count,fallback
def main():
 for path,expected in LOCKS.items(): req(path.exists() and blob(path)==expected,'source-lock drift '+path.name)
 result=checked(RESULT,RESULT_CANONICAL); handoff=checked(HANDOFF,HANDOFF_CANONICAL); rk=json.loads(ACTIVE_RUNKEY.read_text()); ex=json.loads(EXECUTED_RUNKEY.read_text())
 req(rk.get('generation')==11 and rk.get('armed') is False and rk.get('consumed') is True,'active runkey not consumed/disarmed')
 cb=rk.get('consumed_by',{}); req(cb.get('workflow_run_id')==34903959661 and cb.get('aggregate_job_id')==104184044890,'execution receipt drift'); req(cb.get('aggregate_artifact_id')==10372529550 and cb.get('aggregate_artifact_digest')=='sha256:5c2bc83a3274ae0c7e096c066afadda12ba25b38805c48e4d386c2f99f8157e0','aggregate artifact receipt drift')
 req(ex.get('generation')==11 and ex.get('armed') is True and ex.get('consumed') is False,'executed runkey snapshot drift')
 req(handoff['source']['predecessor_cut200_audited_exact_head']=='a1073508a33dac1001657554054a74d3cf47034a','CUT200 audited head drift'); req(handoff['source']['predecessor_cut200_hostile_audit_review']==5189541446,'CUT200 hostile review drift')
 req(result['credit']['stage32_main_pruning_credit'] is False and handoff['credit']['stage32_main_pruning_credit'] is False,'credit leak')
 sys.path.insert(0,str(HERE)); import cut201_e8_common_adapter_wave9 as cut; cut.preflight(); core=cut.core
 survivors=core.e8.current_main_survivor_block_indices(); wave=survivors[2041:2296]; req(len(wave)==255 and result['target']['block_indices']==wave,'wave9 population drift')
 closed=[int(v) for v in result['result']['candidate_closed_block_indices']]; closed_set=set(closed); residual=sorted(set(wave)-closed_set)
 req(len(closed)==EXPECTED_CLOSED and len(closed_set)==EXPECTED_CLOSED,'closed count/uniqueness drift'); req(residual==EXPECTED_RESIDUAL,'residual identity drift'); req(result['result']['candidate_pruned_terminals']==EXPECTED_PRUNED==113*EXPECTED_CLOSED,'terminal accounting drift')
 req(result['result']['method_counts']=={'ALL_HNF_PARENTS_FINITE_RING_UNSAT':9,'FINITE_RING_NONCLOSING_RESIDUAL_PARENTS':29,'HNF_PARENT_POPULATION_EMPTY':8,'WHOLE_BLOCK_FINITE_RING_UNSAT':209},'method provenance drift')
 P,blocks,g=core.load_picard_interface(); solvers={p:core.make_solver(P,blocks,p,5000) for p in PRIMES}; fresh_whole=[]; fresh_empty=[]; fresh_parent=[]; parent_checks=0; unknown_checks=0; fallback_checks=0; fallback_blocks=set()
 for block_index in closed:
  sig=core.e8.block_signature(block_index); req(sig['current_main_audited_prefix_survivor'] is True,f'block {block_index} lost audited prefix survival'); sums=[int(v) for v in sig['n355_known_group_sums']]; req(max(sums)<=4 and sums[1]-sums[2]<=4<=16,f'N356 bridge drift on block {block_index}')
  fixed_terminal={int(k):int(v) for k,v in sig['fixed_exceptional_pairings'].items()}; whole,_,u,fb=fresh_obstruction(cut,P,blocks,solvers,fixed_terminal); unknown_checks+=u; fallback_checks+=len(fb); fallback_blocks.add(block_index) if fb else None
  if whole: fresh_whole.append(block_index); continue
  parents=list(core.e8.iter_parent_population(block_index,g))
  if not parents: fresh_empty.append(block_index); continue
  for ordinal,rec in enumerate(parents):
   parent_checks+=1; fixed={int(label):int(value) for label,value in zip(g.exceptional_labels,rec['selected_exceptional_pairings'])}; ok,_,u,fb=fresh_obstruction(cut,P,blocks,solvers,fixed); unknown_checks+=u; fallback_checks+=len(fb); fallback_blocks.add(block_index) if fb else None; req(ok,f'credited block {block_index} parent {ordinal} unresolved')
  fresh_parent.append(block_index)
 replay=set(fresh_whole)|set(fresh_empty)|set(fresh_parent); req(replay==closed_set,'fresh replay did not recover exact credited candidate set')
 req(len(fresh_whole)+len(fresh_empty)+len(fresh_parent)==EXPECTED_CLOSED,'fresh replay closure accounting drift')
 req(handoff['result']['candidate_closed_block_count']==EXPECTED_CLOSED and handoff['result']['candidate_pruned_terminals']==EXPECTED_PRUNED and handoff['result']['residual_blocks']==EXPECTED_RESIDUAL,'handoff result drift'); req(handoff['audit']['hostile_audit_passed'] is False and handoff['audit']['required_command']=='stage32cut-audit','audit firewall drift')
 print(json.dumps({'status':'PASS_CUT201_EXACT_HEAD_AUDIT_VERIFIER','wave_blocks':255,'candidate_closed_blocks':EXPECTED_CLOSED,'candidate_pruned_terminals':EXPECTED_PRUNED,'fresh_whole_block_finite_ring_unsat':len(fresh_whole),'fresh_hnf_empty':len(fresh_empty),'fresh_all_hnf_parents_finite_ring_unsat_blocks':len(fresh_parent),'fresh_hnf_parents_checked':parent_checks,'timeout_partition_fallback_checks':fallback_checks,'timeout_partition_fallback_blocks':sorted(fallback_blocks),'unknown_checks_not_promoted':unknown_checks,'remaining_nonclosed_blocks':29,'stage32_main_pruning_credit':False,'hostile_audit_passed':False},sort_keys=True))

def run_v26_adapter_candidate():
 import subprocess,tempfile
 repo=HERE.parents[2]
 refs={
  'cut201':'8eed1449b325c3b990f90b61471bf7ecec0d89bc',
  'main_v12':'6d63d798adb50dd4efc5f0d5abc553b3dfa23060',
  'main':'409767d0d4e51366afe17fcb600220b1f7627733',
  'certlift':'51c56b5c3ee15177c2975b966ab546d0b548c4af',
  'n400':'b1a950cbc6edf3cb85e1ea79473105c6f1f67b03',
 }
 with tempfile.TemporaryDirectory(prefix='stage32-cut201-v26-') as td:
  roots={}
  try:
   for name,sha in refs.items():
    subprocess.run(['git','-C',str(repo),'fetch','--no-tags','--depth=1','origin',sha],check=True)
    p=Path(td)/name
    subprocess.run(['git','-C',str(repo),'worktree','add','--detach',str(p),sha],check=True)
    roots[name]=p
   cut_main_state=roots['cut201']/'stages/stage32/MAIN-STATE.json'
   v12_main_state=roots['main_v12']/'stages/stage32/MAIN-STATE.json'
   cut_main_state.write_bytes(v12_main_state.read_bytes())
   subprocess.run([
    sys.executable,str(HERE/'verify_cut201_v26_current_authority_adapter.py'),
    '--cut201-root',str(roots['cut201']),
    '--main-v26-root',str(roots['main']),
    '--certlift-root',str(roots['certlift']),
    '--n400-root',str(roots['n400']),
   ],check=True)
  finally:
   for p in roots.values():
    subprocess.run(['git','-C',str(repo),'worktree','remove','--force',str(p)],check=False)

if __name__=='__main__':
 main()
 if (HERE/'CUT201-V26-current-authority-adapter-handoff.json').is_file(): run_v26_adapter_candidate()
