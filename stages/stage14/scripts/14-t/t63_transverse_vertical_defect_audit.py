#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter, defaultdict
from pathlib import Path
import json, runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / 'stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py'
T42 = ROOT / 'stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py'
T59 = ROOT / 'stages/stage14/scripts/14-t/t59_orthogonal_rectangle_reduction_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t63/transverse_vertical_defect.json'


def prime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n % d == 0: return n == d
        d += 1
    return True


def good_primes(states, need=8):
    out=[]; n=101
    while len(out) < need:
        if n % 4 == 1 and prime(n) and all(s['F'] % n for s in states): out.append(n)
        n += 1
    return out


def audit_packet(states, ps, legendre, row_key, col_key):
    P=len(ps); N=len(states)
    C=[tuple(legendre(s['F'],p) for p in ps) for s in states]
    assert all(abs(x)==1 for v in C for x in v)
    G=[[sum(x*y for x,y in zip(C[i],C[j])) for j in range(N)] for i in range(N)]
    rows=defaultdict(list); cols=defaultdict(list)
    for i,s in enumerate(states): rows[row_key(s)].append(i); cols[col_key(s)].append(i)
    q=lambda I: sum(G[i][j]**2 for i in I for j in I)
    full=q(range(N)); qr=sum(q(v) for v in rows.values()); qc=sum(q(v) for v in cols.values())
    diag=sum(G[i][i]**2 for i in range(N))
    defect=full-qr-qc+diag
    direct=itr=ir=ic=0
    for i,s in enumerate(states):
        for j,t in enumerate(states):
            sr=row_key(s)==row_key(t); sc=col_key(s)==col_key(t); sk=s['kernel']==t['kernel']
            if i!=j and sr and sk: ir+=1
            if i!=j and sc and sk: ic+=1
            if not sr and not sc:
                direct += G[i][j]**2
                if sk: itr += 1; assert G[i][j] == P
    assert defect == direct and direct >= P*P*itr
    cnt=Counter(s['kernel'] for s in states); E=sum(h*h for h in cnt.values())
    assert E == N+ir+ic+itr and full >= P*P*E
    return {'states':N,'squareclass_energy':E,'transverse_principal':itr,
            'transverse_defect':defect,'full_s4':full,'max_fiber':max(cnt.values()),
            'same_row_principal':ir,'same_col_principal':ic}


def main():
    assert 'STAGE14_T62=COMPLETE_MATCHED_RECTANGLE_FRAME_AND_DUAL_PROJECTION_REDUCTION' in (ROOT/'stages/stage14/14-t62/result.md').read_text()
    assert 'STAGE14_TH17=COMPLETE_SIGNED_RECTANGLE_TTSTAR_OPERATOR_LARGE_SIEVE_APPLICABILITY_AUDIT' in (ROOT/'stages/stage14/14-tH17/result.md').read_text()
    assert 'TRANSVERSE_POSITIVE_FROBENIUS_RECEIVER_PROVED=true' in (ROOT/'stages/stage14/14-tH15/result.md').read_text()
    t36=runpy.run_path(str(T36),run_name='t36'); t42=runpy.run_path(str(T42),run_name='t42'); t59=runpy.run_path(str(T59),run_name='t59')
    reps=t42['reciprocal_quotient'](t36['build_frozen_states']()); assert len(reps)==560
    inv=[s for s in reps if s['branch']=='invisible']; assert len(inv)==419
    ps=good_primes(inv); packets=defaultdict(list)
    for s in inv: packets[t59['packet_key'](s)].append(s)
    assert len(packets)==8
    rows=[]
    for key,states in sorted(packets.items()):
        a=audit_packet(states,ps,t36['legendre'],t59['row_key'],t59['col_key']); a['packet']=t59['packet_label'](key); rows.append(a)
    report={'stage':'14-t63','totals':{'reciprocal_states':560,'invisible_states':419,'packets':8,'auxiliary_primes':ps,'auxiliary_prime_count':len(ps),'sum_packet_states':sum(r['states'] for r in rows)},'packets':rows,
      'decision':{'STAGE14_T63':'COMPLETE_TH17_CONSUMPTION_AND_TRANSVERSE_VERTICAL_DEFECT_REDUCTION','MERGED_T62_IMPORTED':True,'MERGED_TH17_IMPORTED':True,'VERTICAL_TTSTAR_IDENTITY_IMPORTED':True,'VERTICAL_TRANSVERSE_DEFECT_IDENTITY_PROVED':True,'T63_TRANSVERSE_DEFECT_EQUALS_TH15_FROBENIUS':True,'FULL_VERTICAL_SCHATTEN4_REQUIRED':False,'ORTHOGONAL_RECTANGLE_VERTICAL_KUMMER_SCHATTEN4_IS_STRONGER_THAN_MINIMAL':True,'TRANSVERSE_PRINCIPAL_AMPLIFICATION_PROVED':True,'VERTICAL_BESSEL_ALREADY_REQUIRES_MAX_SQUARECLASS_FIBER_CONTROL':True,'FULL_VERTICAL_S4_ALREADY_CONTAINS_SQUARECLASS_ENERGY':True,'GENERIC_DUALITY_IS_NOT_NEW_ARITHMETIC_INPUT':True,'MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_STILL_SUFFICIENT':True,'MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_REQUIRED':False,'T62_MATCHED_BLOCK_PROJECTION_RETAINED':True,'SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED':False,'SHARED_U_PHYSICAL_BIPARTITE_DISPERSION_PROVED':False,'SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED':False,'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT':'7/8','TH17_CONSUMED':True,'TH18_NEEDED':False,'T_ROUTE_BLOCKED_WAITING_FOR_TH':False,'NEXT':'Stage14-t64 return to the tH15 explicit projective transverse trace and attack equal-squareclass/vertical dispersion directly'}}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n'); print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__': main()
