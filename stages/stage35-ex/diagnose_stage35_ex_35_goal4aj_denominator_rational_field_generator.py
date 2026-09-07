#!/usr/bin/env python3
"""Goal4AJ diagnostic: full rational-field degree-19 denominator residual generator.

All seven extension-valued conjugate pairs in the 22-curve denominator residual have
now been compacted to Q-defined orbit ideals.  Build the six multiplicity-group
reflexive powers over Q, merge them in size-balanced fresh Singular processes, and
extract the unique degree-19 section.  Reattach the exact peeled factor c*b1^11 and,
when bounded in size, persist a literal degree-31 denominator polynomial.

Diagnostic/provisional only.  No F_B/E1/theorem credit and no state promotion here.
"""
from __future__ import annotations
from contextlib import redirect_stdout
import hashlib,io,json,runpy,subprocess,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
QPACK=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_q_orbit_packet.py'
ACTIVE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py'
QPACK_SHA='cd402f603bed75eb5521a568efc6c9767578dfa67948b5bf3a129b17ccafaab6'
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
DEN_RIGIDITY_SHA='e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc'
REFLEXIVE_PREFLIGHT_SHA='1d1395746942bd7d5748e408192761ebf6dce92eeb2760fd34fe9295d674db3b'
ONESHOT_SHA='da58a9c6b72a71d71c9af6f87fa987d2589b0fb3568918bc6994c3960de28a80'
QPEEL_SHA='c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba'
PEELED_FACTOR_SHA='8818b4e1f29359b6a5579ded427ba65ae1686d09c71b8772bf2b9934a41688a5'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'

# Replay compact packets and require exact locks.
def replay(path:Path,prefix:str):
    cp=subprocess.run(['python','-B',str(path)],text=True,capture_output=True,timeout=60)
    if cp.returncode!=0: raise SystemExit(f'replay failed: {path.name}')
    line=next(x for x in cp.stdout.splitlines() if x.startswith(prefix))
    return json.loads(line.split('=',1)[1])
qpack=replay(QPACK,'GOAL4AJ_DEN_Q_ORBIT_PACKET_JSON=')
active=replay(ACTIVE,'GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON=')
assert qpack['canonical_sha256']==QPACK_SHA and qpack['all_22_denominator_strict_components_representable_over_Q'] is True
assert active['canonical_sha256']==ACTIVE_SHA
assert active['denominator_residual']['homogeneous_degree_after_q_peel']==19
expected={int(k):int(v) for k,v in active['denominator_residual']['strict_multiplicities_1based'].items()}
assert len(expected)==22 and sum(expected.values())==102

PAIR={k:v['basis_text'] for k,v in qpack['pair_packet'].items()}
SINGLE={
 1:'a1,a2+b3,a3+b2,b1+c',8:'a1,a2-b3,a3-b2,b1-c',
 9:'a2,a3+b1,a1+b3,b2+c',17:'a3,a1+b2,a2+b1,b3+c',
 11:'a2,a3+b1,a1-b3,b2+c',21:'a3,a1-b2,a2+b1,b3+c',
 16:'a2,a3-b1,a1-b3,b2-c',24:'a3,a1-b2,a2-b1,b3-c',
}
GROUP_BASES={
 13:[('pair37_39',PAIR['37_39'])],
 9:[('pair26_31',PAIR['26_31']),('pair58_60',PAIR['58_60'])],
 7:[('pair25_32',PAIR['25_32'])],
 3:[('p1',SINGLE[1]),('p8',SINGLE[8]),('p9',SINGLE[9]),('p17',SINGLE[17])],
 2:[('p11',SINGLE[11]),('p21',SINGLE[21]),('pair33_35',PAIR['33_35'])],
 1:[('p16',SINGLE[16]),('p24',SINGLE[24]),('pair28_29',PAIR['28_29']),('pair65_67',PAIR['65_67'])],
}
# Check divisor multiplicities represented by the rational orbit packet.
represented={37:13,39:13,26:9,31:9,58:9,60:9,25:7,32:7,1:3,8:3,9:3,17:3,11:2,21:2,33:2,35:2,16:1,24:1,28:1,29:1,65:1,67:1}
assert represented==expected

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
    script=COMMON+body+f'\nprint("BASIS_{tag}_BEGIN"); print(string(OUT)); print("BASIS_{tag}_END"); quit;\n'
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/f'{tag}.sing'; p.write_text(script,encoding='utf-8')
        try: cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=timeout)
        except subprocess.TimeoutExpired: raise SystemExit(f'Goal4AJ rational denominator stage {tag} timed out; no mathematical obstruction credit')
    low=(cp.stdout+'\n'+cp.stderr).lower()
    if cp.returncode!=0 or any(s in low for s in ('error occurred','? error','? cannot','? wrong','? assign')):
        print(cp.stdout[-8000:]); print(cp.stderr[-4000:]); raise SystemExit(f'Goal4AJ rational denominator stage {tag} failed; no mathematical obstruction credit')
    lines=cp.stdout.splitlines(); a=lines.index(f'BASIS_{tag}_BEGIN'); b=lines.index(f'BASIS_{tag}_END')
    text='\n'.join(lines[a+1:b]).strip()
    if not text: raise SystemExit(f'empty basis at {tag}')
    if len(text.encode())>2_000_000: raise SystemExit(f'basis at {tag} exceeded 2MB resource guard')
    print(f'GOAL4AJ_DEN_Q_STAGE={tag}:bytes={len(text.encode())}:sha256={hashlib.sha256(text.encode()).hexdigest()}')
    return text

def build_group(m:int,bases:list[tuple[str,str]])->str:
    chunks=[]
    for pos,(name,idealtext) in enumerate(bases):
        chunks.append(f'ideal B{pos}={idealtext};\n')
    chunks.append('ideal G=std(B0);\n')
    for pos in range(1,len(bases)): chunks.append(f'G=reflexiveProduct(G,std(B{pos}));\n')
    if m==1: chunks.append('ideal OUT=G;\n')
    elif m==2: chunks.append('ideal X2=reflexiveProduct(G,G); ideal OUT=X2;\n')
    elif m==3: chunks.append('ideal X2=reflexiveProduct(G,G); ideal OUT=reflexiveProduct(X2,G);\n')
    elif m==7: chunks.append('ideal X2=reflexiveProduct(G,G); ideal X3=reflexiveProduct(X2,G); ideal X6=reflexiveProduct(X3,X3); ideal OUT=reflexiveProduct(X6,G);\n')
    elif m==9: chunks.append('ideal X2=reflexiveProduct(G,G); ideal X4=reflexiveProduct(X2,X2); ideal X8=reflexiveProduct(X4,X4); ideal OUT=reflexiveProduct(X8,G);\n')
    elif m==13: chunks.append('ideal X2=reflexiveProduct(G,G); ideal X3=reflexiveProduct(X2,G); ideal X6=reflexiveProduct(X3,X3); ideal X12=reflexiveProduct(X6,X6); ideal OUT=reflexiveProduct(X12,G);\n')
    else: raise AssertionError(m)
    return run_basis(f'group{m}',''.join(chunks),600)

basis={m:build_group(m,GROUP_BASES[m]) for m in (13,9,7,3,2,1)}
# Size-balanced fresh-process merges; reflexive-product associativity is source-locked.
items=[(len(text.encode()),f'D{m}',text) for m,text in basis.items()]
merge_trace=[]; serial=0
while len(items)>1:
    items.sort(key=lambda x:(x[0],x[1])); a=items.pop(0); b=items.pop(0); serial+=1
    tag=f'merge{serial}_{a[1]}_{b[1]}'
    body=f'ideal A={a[2]};\nideal B={b[2]};\nideal OUT=reflexiveProduct(A,B);\n'
    text=run_basis(tag,body,600); merge_trace.append({'tag':tag,'left':a[1],'right':b[1],'left_bytes':a[0],'right_bytes':b[0],'out_bytes':len(text.encode()),'out_sha256':hashlib.sha256(text.encode()).hexdigest()})
    items.append((len(text.encode()),tag,text))
full_basis=items[0][2]

# Extract the minimum-degree canonical-ring generator and attach the exact Q peel factor.
extract=COMMON+f'''\nideal D={full_basis};\nideal SurfStd=std(surf);\nint j; int md=999; int n19=0; int dq; poly q; poly candidate=0;\nfor(j=1;j<=size(D);j++){{q=reduce(D[j],SurfStd); if(q!=0){{dq=deg(q); if(dq<md){{md=dq;}} if(dq==19){{n19++; if(candidate==0){{candidate=q;}}}}}}}}\nprint("MINDEG="+string(md)); print("N19="+string(n19));\nif(md!=19 || n19<1){{ERROR("rational denominator basis has no degree19 minimum generator");}}\npoly full=c*b1^11*candidate; if(deg(full)!=31){{ERROR("reattached denominator degree mismatch");}}\nprint("RES_BEGIN"); print(string(candidate)); print("RES_END");\nprint("FULL_BEGIN"); print(string(full)); print("FULL_END"); quit;\n'''
with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'extract.sing'; p.write_text(extract,encoding='utf-8'); cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=300)
if cp.returncode!=0: print(cp.stdout[-8000:]); print(cp.stderr[-4000:]); raise SystemExit('degree19 extraction failed')
ls=cp.stdout.splitlines(); md=int(next(x for x in ls if x.startswith('MINDEG=')).split('=',1)[1]); n19=int(next(x for x in ls if x.startswith('N19=')).split('=',1)[1])
def getblock(a,b):
    i=ls.index(a); j=ls.index(b); return '\n'.join(ls[i+1:j]).strip()
res=getblock('RES_BEGIN','RES_END'); full=getblock('FULL_BEGIN','FULL_END')
full_bytes=len(full.encode()); persisted=full_bytes<=60000
out={
 'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_RATIONAL_FIELD_GENERATOR_DIAGNOSTIC_V1',
 'source_locks':{
  'denominator_q_orbit_packet_canonical_sha256':QPACK_SHA,'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,
  'denominator_residual_rigidity_canonical_sha256':DEN_RIGIDITY_SHA,'reflexive_product_preflight_canonical_sha256':REFLEXIVE_PREFLIGHT_SHA,
  'oneshot_reflexive_hull_canonical_sha256':ONESHOT_SHA,'q_hyperplane_factor_peel_canonical_sha256':QPEEL_SHA,
  'peeled_q_factor_locator_canonical_sha256':PEELED_FACTOR_SHA,'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,
 },
 'coefficient_field':'Q','strict_component_count':22,'strict_total_multiplicity':102,
 'multiplicity_group_basis_sha256':{str(m):hashlib.sha256(basis[m].encode()).hexdigest() for m in sorted(basis)},
 'multiplicity_group_basis_bytes':{str(m):len(basis[m].encode()) for m in sorted(basis)},
 'balanced_merge_trace':merge_trace,'final_divisorial_basis_sha256':hashlib.sha256(full_basis.encode()).hexdigest(),'final_divisorial_basis_bytes':len(full_basis.encode()),
 'minimum_nonsurface_generator_degree':md,'degree19_generator_count_in_standard_basis':n19,
 'degree19_residual_candidate_materialized':bool(res),'degree19_residual_candidate_sha256':hashlib.sha256(res.encode()).hexdigest(),'degree19_residual_candidate_bytes':len(res.encode()),
 'peeled_degree12_q_factor_literal':'c*b1^11','peeled_degree12_q_factor_reattached':True,
 'degree31_denominator_candidate_sha256':hashlib.sha256(full.encode()).hexdigest(),'degree31_denominator_candidate_bytes':full_bytes,
 'degree31_denominator_candidate_text':full if persisted else None,'degree31_denominator_candidate_persisted_inline':persisted,
 'literal_degree31_denominator_materialized':persisted,'literal_denominator_coefficients_materialized':persisted,
 'literal_numerator_coefficients_materialized':False,'literal_F_B_materialized':False,'local_evaluations_computed':False,'brauer_manin_obstruction_obtained':False,'E1_proved':False,'stage35_closed':False,'theorem_credit':False,'endpoint_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_DEN_Q_GENERATOR_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
print('GOAL4AJ_DEN_Q_GENERATOR=PASS')
