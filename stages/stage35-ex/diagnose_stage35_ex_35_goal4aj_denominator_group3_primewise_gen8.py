#!/usr/bin/env python3
'''Goal4AJ diagnostic: cross the current Q-denominator D3 merge bottleneck primewise.

The full rational-field generator at exact source lock successfully builds all six
multiplicity-group powers, then times out only at the balanced merge
D3 x (D13*D2). Replace the aggregated D3 basis by four independently cubed
Q-prime divisors and fold them one at a time into the already-computable D13*D2
basis. PASS means only that this exact resource bottleneck is crossed.

Diagnostic/provisional only. No literal denominator/F_B/E1/theorem credit.
'''
from __future__ import annotations
import hashlib,json,subprocess,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
PARENT=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_rational_field_generator.py'
QPACK=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_q_orbit_packet.py'
PARENT_BLOB='e368ff10951d2442c61f0660507d757d889c7c27'
QPACK_SHA='cd402f603bed75eb5521a568efc6c9767578dfa67948b5bf3a129b17ccafaab6'
FAILED_RUN=34121996664
FAILED_JOB=101742040606
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
DEN_RIGIDITY_SHA='e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc'
REFLEXIVE_PREFLIGHT_SHA='1d1395746942bd7d5748e408192761ebf6dce92eeb2760fd34fe9295d674db3b'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'

def git_blob(path:Path)->str:
    b=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert git_blob(PARENT)==PARENT_BLOB

def replay(path:Path,prefix:str):
    cp=subprocess.run(['python','-B',str(path)],text=True,capture_output=True,timeout=60)
    if cp.returncode!=0:
        raise SystemExit(f'replay failed: {path.name}')
    line=next(x for x in cp.stdout.splitlines() if x.startswith(prefix))
    return json.loads(line.split('=',1)[1])

qpack=replay(QPACK,'GOAL4AJ_DEN_Q_ORBIT_PACKET_JSON=')
assert qpack['canonical_sha256']==QPACK_SHA
assert qpack['all_22_denominator_strict_components_representable_over_Q'] is True
PAIR={k:v['basis_text'] for k,v in qpack['pair_packet'].items()}

SINGLE={
 1:'a1,a2+b3,a3+b2,b1+c',
 8:'a1,a2-b3,a3-b2,b1-c',
 9:'a2,a3+b1,a1+b3,b2+c',
 17:'a3,a1+b2,a2+b1,b3+c',
 11:'a2,a3+b1,a1-b3,b2+c',
 21:'a3,a1-b2,a2+b1,b3+c',
}
D3_INDICES=[1,8,9,17]

COMMON=r'''
option(redSB);
LIB "elim.lib";
ring r=0,(a1,a2,a3,b1,b2,b3,c),dp;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
matrix Jac=jacob(surf); ideal Sing=minor(Jac,4);
proc reflexiveProduct(ideal A,ideal B)
{
 ideal Candidate=surf+A*B; list L=sat(Candidate,Sing); return(std(L[1]));
}
'''

def run_basis(tag:str,body:str,timeout:int=600)->str:
    sc=COMMON+body+f'\nprint("BASIS_{tag}_BEGIN"); print(string(OUT)); print("BASIS_{tag}_END"); quit;\n'
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/(tag+'.sing')
        p.write_text(sc,encoding='utf-8')
        try:
            cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=timeout)
        except subprocess.TimeoutExpired:
            print('GOAL4AJ_DEN_D3_SPLIT_TIMEOUT_TAG='+tag,flush=True)
            raise SystemExit('Goal4AJ D3 primewise fold timed out; no mathematical obstruction credit')
    low=(cp.stdout+'\n'+cp.stderr).lower()
    if cp.returncode!=0 or any(s in low for s in ('error occurred','? error','? cannot','? wrong','? assign')):
        print('GOAL4AJ_DEN_D3_SPLIT_FAIL_TAG='+tag,flush=True)
        print('GOAL4AJ_DEN_D3_SPLIT_STDOUT_TAIL='+json.dumps(cp.stdout[-12000:]),flush=True)
        if cp.stderr:
            print('GOAL4AJ_DEN_D3_SPLIT_STDERR_TAIL='+json.dumps(cp.stderr[-12000:]),flush=True)
        raise SystemExit('Goal4AJ D3 primewise fold failed closed')
    lines=cp.stdout.splitlines()
    a=lines.index(f'BASIS_{tag}_BEGIN')
    b=lines.index(f'BASIS_{tag}_END')
    text='\n'.join(lines[a+1:b]).strip()
    if not text:
        raise SystemExit(f'empty basis at {tag}')
    if len(text.encode())>2_000_000:
        raise SystemExit(f'basis at {tag} exceeded 2MB resource guard')
    print(f'GOAL4AJ_DEN_D3_SPLIT_STAGE={tag}:bytes={len(text.encode())}:sha256={hashlib.sha256(text.encode()).hexdigest()}',flush=True)
    return text

def pow_body(base:str,m:int)->str:
    if m not in (2,3,13):
        raise AssertionError(m)
    chunks=[f'ideal G={base};\n']
    if m==2:
        chunks.append('ideal OUT=reflexiveProduct(G,G);\n')
    elif m==3:
        chunks.append('ideal X2=reflexiveProduct(G,G); ideal OUT=reflexiveProduct(X2,G);\n')
    else:
        chunks.append('ideal X2=reflexiveProduct(G,G); ideal X3=reflexiveProduct(X2,G); ideal X6=reflexiveProduct(X3,X3); ideal X12=reflexiveProduct(X6,X6); ideal OUT=reflexiveProduct(X12,G);\n')
    return ''.join(chunks)

def d2_body()->str:
    return (
        f'ideal B0={SINGLE[11]}; ideal B1={SINGLE[21]}; ideal B2={PAIR["33_35"]};\n'
        'ideal G=std(B0); G=reflexiveProduct(G,std(B1)); G=reflexiveProduct(G,std(B2)); '
        'ideal OUT=reflexiveProduct(G,G);\n'
    )

def merge_body(A:str,B:str)->str:
    return f'ideal A={A};\nideal B={B};\nideal OUT=reflexiveProduct(A,B);\n'

D13=run_basis('group13',pow_body(PAIR['37_39'],13))
D2=run_basis('group2',d2_body())
D=run_basis('merge_D13_D2',merge_body(D13,D2))
stage={'group13':D13,'group2':D2,'merge_D13_D2':D}

for idx in D3_INDICES:
    P3=run_basis(f'prime{idx}_pow3',pow_body(SINGLE[idx],3))
    stage[f'prime{idx}_pow3']=P3
    D=run_basis(f'fold_prime{idx}_pow3',merge_body(D,P3))
    stage[f'fold_prime{idx}_pow3']=D

out={
 'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_GROUP3_PRIMEWISE_BOTTLENECK_PREFLIGHT_V8',
 'source_locks':{
   'rational_field_generator_blob_sha1':PARENT_BLOB,
   'rational_field_generator_failed_run':FAILED_RUN,
   'rational_field_generator_failed_job':FAILED_JOB,
   'denominator_q_orbit_packet_canonical_sha256':QPACK_SHA,
   'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,
   'denominator_rigidity_canonical_sha256':DEN_RIGIDITY_SHA,
   'reflexive_product_preflight_canonical_sha256':REFLEXIVE_PREFLIGHT_SHA,
   'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,
 },
 'observed_parent_failure_stage':'merge3_D3_merge1_D13_D2 timeout at 600 seconds',
 'constructor':'Q-defined D13 and D2 powers, then four independent multiplicity-3 Q-prime powers folded sequentially into D13*D2 in fresh Singular processes',
 'group3_prime_indices':D3_INDICES,
 'stage_basis_sha256':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in stage.items()},
 'stage_basis_bytes':{k:len(v.encode()) for k,v in stage.items()},
 'crossed_current_D3_merge_bottleneck':True,
 'final_folded_basis_sha256':hashlib.sha256(D.encode()).hexdigest(),
 'final_folded_basis_bytes':len(D.encode()),
 'literal_degree19_denominator_residual_materialized':False,
 'literal_degree31_denominator_materialized':False,
 'literal_F_B_materialized':False,
 'local_evaluations_computed':False,
 'brauer_manin_obstruction_obtained':False,
 'E1_proved':False,
 'stage35_closed':False,
 'theorem_credit':False,
 'endpoint_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_DEN_D3_SPLIT_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')),flush=True)
print('GOAL4AJ_DEN_D3_SPLIT=PASS',flush=True)
