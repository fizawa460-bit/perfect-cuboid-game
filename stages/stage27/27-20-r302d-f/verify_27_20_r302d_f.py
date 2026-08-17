#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]/'stages'/'stage27'
def t(p): return p.read_text(encoding='utf-8')
def has(s,x):
    if x not in s: raise RuntimeError('missing '+x)
pa=t(R/'27-20-r302a-c'/'audit.md')
for x in ['AUDIT_VERDICT=PASS','PR_MERGED=true','ADVANCE_ALLOWED=true','NEXT_DERIVED_ROUTE=27-20-r302d']: has(pa,x)
pr=json.loads(t(R/'27-20-r302a-c'/'batch-registry.json'))
if pr['status']!='AUDITED_PASS_MERGED' or pr['audit_status']!='PASS' or not pr['advance_allowed']: raise RuntimeError('parent lifecycle')
d=t(R/'27-20-r302d'/'result.md')
for x in ['PRIMITIVE_RECTANGLE_GCD_U_V_ONE_REUSED=true','CRT_COMPRESSION_NEW_INDEPENDENT_SUPPORT=false','NAIVE_CRT_COMPRESSION_ROUTE_CLOSED=true']: has(d,x)
e=t(R/'27-20-r302e'/'result.md')
for x in ['PHYSICAL_PRIMITIVE_PAIR_WEIGHT_DEFINED=true','UNWEIGHTED_RESIDUE_CLASS_COUNT_SUFFICIENT=false','PRIMITIVE_PAIR_OCCUPANCY_FIXED_POWER_DEFICIT_PROVED=false']: has(e,x)
f=t(R/'27-20-r302f'/'result.md')
for x in ['CRITICAL_THETA=1/4','CRITICAL_CHI=2phi-1/4','CRITICAL_PRIMITIVE_PAIR_HOST_EXPONENT=1/4','CRITICAL_TOTAL_HOST_EXPONENT=1/2','ACTUAL_PRIMITIVE_PAIR_SUPPORT_ASYMPTOTIC_CLAIMED=false']: has(f,x)
for s in [d,e,f]:
    for x in ['STRICT_SUB_SQRT_UPPER_PROVED=false','NEW_MU_LT_HALF_PROVED=false','TRUE_N2_EXPONENT_IDENTIFIED=false']: has(s,x)
reg=json.loads(t(R/'27-20-r302d-f'/'batch-registry.json'))
if reg['audit_status']!='PENDING' or reg['advance_allowed'] or reg['advance_to_checkpoint50']: raise RuntimeError('lifecycle')
print('Stage27-20-r302d-f verification: PASS')
