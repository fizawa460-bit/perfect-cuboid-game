#!/usr/bin/env python3
"""Direct exact finite-group-type filter for k=1 discriminant quotients."""
from nonelementary_k1_geometric_sign_fixed_common import MODS0,QDIAG,A0_LOG2,H_LOG2,subgroup_log2
TARGET_POWER_LOG2={2:14,4:24,8:28}

def quotient_power_log2_direct(Hrows,power):
    """Exact log2 |(H^perp/H)[power]| without Smith decomposition."""
    if power not in (2,4,8):raise ValueError(power)
    n=len(Hrows)
    if n!=8:raise SystemExit('k1 finite-group-type H row regression')
    codmods=(16,)*n+tuple(MODS0);width=n+14;gens=[]
    for j,m in enumerate(MODS0):
        row=[0]*width
        for i,h in enumerate(Hrows):row[i]=(QDIAG[j]*int(h[j]))%16
        row[n+j]=int(power)%int(m);gens.append(tuple(row))
    for h in Hrows:
        row=[0]*width
        for j,m in enumerate(MODS0):row[n+j]=(-int(h[j]))%int(m)
        gens.append(tuple(row))
    kernel_log=A0_LOG2+H_LOG2-subgroup_log2(gens,codmods);qpower_log=kernel_log-H_LOG2
    if not 0<=qpower_log<=28:raise SystemExit('quotient power-torsion log regression')
    return qpower_log

def classify_endpoint_group_type(Hrows):
    q4=quotient_power_log2_direct(Hrows,4)
    if q4!=TARGET_POWER_LOG2[4]:return False,f'GROUP_TYPE_Q4_LOG2_{q4}',{2:None,4:q4,8:None}
    q2=quotient_power_log2_direct(Hrows,2)
    if q2!=TARGET_POWER_LOG2[2]:return False,f'GROUP_TYPE_Q2_LOG2_{q2}',{2:q2,4:q4,8:None}
    q8=quotient_power_log2_direct(Hrows,8)
    if q8!=TARGET_POWER_LOG2[8]:return False,f'GROUP_TYPE_Q8_LOG2_{q8}',{2:q2,4:q4,8:q8}
    return True,'MATCH',{2:q2,4:q4,8:q8}
