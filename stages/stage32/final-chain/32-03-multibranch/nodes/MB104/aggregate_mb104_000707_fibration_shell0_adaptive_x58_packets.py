#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_adaptive_x58_packet as packet
import verify_mb104_000707_fibration_shell0_adaptive_x58_packet as pv
import verify_mb104_000707_gen27_adaptive_x58_carry as carry
HERE=Path(__file__).resolve().parent; RUNKEY=HERE/'runkeys'/'000707-FIBRATION-ISOTROPIC-SHELLS-V1.json'; SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_SINGLETON_AGGREGATE_V1'

def pkey(d):
 q=d['partition']; return (int(q['primary_value']),int(q['secondary_residue']),int(q['fixed_x61_value']),int(q['x60_residue']),int(q['fixed_x60_value']),int(q['parent_x58_interval'][0]),int(q['parent_x58_interval'][1]))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); idx,p=carry.decode_carry(); rows=packet.residual_rows(); expected=set(rows); obs={}; integral=0; prim=[]; sx=set(); sf=set()
 for path in sorted(a.input_dir.glob('*.json')):
  raw=json.loads(path.read_text()); k=pkey(raw)
  if k not in expected or k in obs: continue
  d=pv.validate_certificate(path,*k); obs[k]=d; integral+=int(d['result']['integral_known140_nonnegative_solution_count'])
  for rec in d['result']['primitive_known140_nonnegative_candidates']:
   xk=tuple(rec['x_hperp_coordinates']); fk=tuple(rec['picard_basis_coordinates']); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); prim.append(rec)
 missing=sorted([list(k) for k in expected-set(obs)]); incomplete=sorted([list(k) for k,d in obs.items() if not d['result']['complete']]); complete=not missing and not incomplete and len(obs)==54; prim.sort(key=lambda r:tuple(r['picard_basis_coordinates'])); hashes={':'.join(map(str,k)):d['canonical_sha256_without_this_field'] for k,d in sorted(obs.items())}; k=json.loads(RUNKEY.read_text())
 out={'schema':SCHEMA,'status':'COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT' if complete else 'PARTIAL_X58_SINGLETON_RECOVERY_NO_CREDIT','complete':complete,'provenance':{'producing_execution_head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'semantic_source_locks':packet.semantic_source_locks(),'gen27_carry_payload_sha256':idx['payload_sha256'],'gen27_carry_gzip_sha256':idx['gzip_sha256'],'gen27_producing_execution_head':idx['producing_execution_head']},'packet_input_canonical_sha256':hashes,'coverage':{'prior_complete_x60_singletons':281,'necessary_condition_empty_leaf_count':14,'gen27_complete_x58_interval_count':74,'residual_timeout_x58_interval_count':54,'expected_packet_count':54,'observed_packet_count':len(obs),'expected_x58_singleton_child_count':160,'refinement_coordinate_0based':58,'refinement_is_exact_disjoint':True,'missing_packets':missing,'incomplete_packets':incomplete},'result':{'integral_known140_nonnegative_solution_count':integral if complete else None,'primitive_candidate_count':len(prim) if complete else None,'primitive_candidates':prim if complete else []},'credit_firewall':{'numerical_fibration_shell_credit':False,'effectivity_credit':False,'semiampleness_credit':False,'global_fibration_optimum_credit':False,'MB104_complete':False,'receiver_credit':False,'theorem_credit':False,'endpoint_credit':False,'merge_authorized':False}}
 out['canonical_sha256_without_this_field']=parent.csha(out); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({'success':True,'complete':complete,'observed_packets':len(obs),'missing':len(missing),'incomplete':len(incomplete),'canonical':out['canonical_sha256_without_this_field']},sort_keys=True)); raise SystemExit(0 if complete else 2)
if __name__=='__main__': main()
