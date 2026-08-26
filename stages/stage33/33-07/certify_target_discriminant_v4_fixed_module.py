#!/usr/bin/env python3
"""Exact fixed-subgroup inventory for the endpoint 2-primary discriminant module.

This is a finite diagnostic for the index-512 glue match.  It does not identify
Br(Sbar)[4] with the discriminant group and grants no global Q-lift credit.
"""
import hashlib, json, math
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_form

HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'picard-discriminant-compact.json').read_text())
claimed=src['canonical_sha256']
chk=dict(src); chk.pop('canonical_sha256',None)
raw=json.dumps(chk,sort_keys=True,separators=(',',':')).encode()
if hashlib.sha256(raw).hexdigest()!=claimed:
    raise SystemExit('compact discriminant canonical hash regression')
if claimed!='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0':
    raise SystemExit('compact discriminant source lock moved')
mods=[int(x) for x in src['discriminant_moduli']]
cc=[[int(x) for x in r] for r in src['cc_action_mixed_moduli']]
ct=[[int(x) for x in r] for r in src['ct_action_mixed_moduli']]
if mods != [2]*4+[4]*6+[8]*4:
    raise SystemExit('target discriminant group regression')

def v2(n):
    if n<=0 or n&(n-1): raise SystemExit(f'not a positive 2-power: {n}')
    return n.bit_length()-1

def restrict_action(M, oldmods, newmods):
    scales=[oldmods[i]//newmods[i] for i in range(len(oldmods))]
    out=[]
    for i in range(len(oldmods)):
        row=[]
        for j in range(len(oldmods)):
            num=scales[i]*M[i][j]
            if num%scales[j]:
                raise SystemExit('restricted action integrality failed')
            row.append((num//scales[j])%newmods[j])
        out.append(row)
    return out

def fixed_log2(oldmods, actions, exponent_cap):
    m=[min(x,exponent_cap) for x in oldmods]
    acts=[restrict_action(A,oldmods,m) for A in actions]
    n=len(m); r=len(acts)
    # f:A -> A^r, x |-> (x(g_1-I),...,x(g_r-I)).
    # Present coker(f) by the coordinate-order relations of A^r plus the n
    # image generators.  Since |coker f|=|A|^(r-1)|ker f|, the kernel order
    # follows from one bounded Smith form.
    Bmods=m*r
    relations=[]
    for i,mod in enumerate(Bmods):
        row=[0]*(n*r); row[i]=mod; relations.append(row)
    for i in range(n):
        row=[]
        for A in acts:
            row.extend([(A[i][j]-(1 if i==j else 0))%m[j] for j in range(n)])
        relations.append(row)
    D=smith_normal_form(sp.Matrix(relations),domain=ZZ)
    diag=[abs(int(D[i,i])) for i in range(n*r) if D[i,i]!=0]
    if len(diag)!=n*r:
        raise SystemExit('fixed-module quotient unexpectedly infinite')
    coker_log=sum(v2(x) for x in diag if x>1)
    Alog=sum(v2(x) for x in m)
    return coker_log-(r-1)*Alog

def type_from_logs(l1,l2,l3):
    c=l3-l2
    bc=l2-l1
    b=bc-c
    a=l1-b-c
    if min(a,b,c)<0 or a+b+c!=l1 or a+2*b+3*c!=l3:
        raise SystemExit(f'bad invariant reconstruction {(l1,l2,l3)} -> {(a,b,c)}')
    return {'z2_rank':a,'z4_rank':b,'z8_rank':c,
            'group':f'(Z/2)^{a} direct_sum (Z/4)^{b} direct_sum (Z/8)^{c}',
            'order_log2':l3}

def inventory(actions):
    l1=fixed_log2(mods,actions,2)
    l2=fixed_log2(mods,actions,4)
    l3=fixed_log2(mods,actions,8)
    out=type_from_logs(l1,l2,l3)
    out['two_torsion_order_log2']=l1
    out['four_torsion_order_log2']=l2
    return out

icc=inventory([cc]); ict=inventory([ct]); ij=inventory([cc,ct])
if (icc['z2_rank'],icc['z4_rank'],icc['z8_rank'])!=(5,2,3):
    raise SystemExit(f'cc fixed type regression {icc}')
if (ict['z2_rank'],ict['z4_rank'],ict['z8_rank'])!=(7,3,3):
    raise SystemExit(f'ct fixed type regression {ict}')
if (ij['z2_rank'],ij['z4_rank'],ij['z8_rank'])!=(5,3,1):
    raise SystemExit(f'joint fixed type regression {ij}')

cert={
 'schema':'STAGE33_07_TARGET_DISCRIMINANT_V4_FIXED_MODULE_V1',
 'source_locks':{'picard_discriminant_compact_sha256':claimed},
 'target_discriminant_group':src['picard_discriminant_group'],
 'cc_fixed_subgroup':icc,
 'ct_fixed_subgroup':ict,
 'joint_v4_fixed_subgroup':ij,
 'joint_v4_fixed_subgroup_exact':'(Z/2)^5 direct_sum (Z/4)^3 direct_sum Z/8',
 'joint_v4_fixed_order_log2':14,
 'role':'INDEX512_GLUE_MATCH_DIAGNOSTIC_ONLY',
 'proper_Br4_identification_claimed':False,
 'actual_index512_k3_glue_identified':False,
 'global_q_defined_boundary_lifts_complete':False,
 'next_exact_leaf':'L33-07-MATCH-INDEX512-GLUE-USING-TARGET-QUADRATIC-FORM-PLUS-V4-FIXED-TYPE',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
can=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/'target-discriminant-v4-fixed-module.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'cc_fixed':icc['group'],'ct_fixed':ict['group'],
 'joint_fixed':ij['group'],'joint_fixed_order_log2':14,'next':cert['next_exact_leaf'],
 'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
