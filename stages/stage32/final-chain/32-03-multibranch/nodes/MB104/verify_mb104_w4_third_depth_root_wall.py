#!/usr/bin/env python3
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

CERT=Path(__file__).with_name('MB104-W4-THIRD-DEPTH-ROOT-WALL-CERTIFICATE.json')
MASK=int('000707000f0f',16)
SUPPORT={i for i in range(48) if (MASK>>i)&1}

def req(x,m):
    if not x: raise SystemExit('FAIL: '+m)

def canon(z):
    for x in z:
        if x!=0:
            s=x; break
    return tuple(complex(round((x/s).real),round((x/s).imag)) for x in z)

def nodes():
    out=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[0j]*7
                    z[j]=sa
                    o=[t for t in range(3) if t!=j]
                    z[3+o[0]]=s1
                    z[3+o[1]]=s2
                    z[6]=1
                    out.append(tuple(z))
    for j in range(3):
        o=[t for t in range(3) if t!=j]
        a,b=o
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[0j]*7
                    z[a]=1
                    z[b]=1j*sr
                    z[3+a]=1j*ep
                    z[3+b]=-eq*sr
                    out.append(tuple(z))
    req(len(out)==48 and len(set(out))==48,'48 nodes')
    return out

def sign_perm(V,k):
    cs=[canon(z) for z in V]
    idx={z:i for i,z in enumerate(cs)}
    out=[]
    for z in V:
        zz=list(z)
        zz[k]*=-1
        out.append(idx[canon(tuple(zz))])
    return tuple(out)

def cycles2(p):
    seen=set(); out=[]
    for i,j in enumerate(p):
        if i in seen: continue
        seen.add(i); seen.add(j)
        if i!=j: out.append((i,j))
    return out

def project(z,forget):
    return tuple(z[i] for i in range(7) if i!=forget)

def z0(x):
    return abs(x)<1e-9

def main():
    c=json.loads(CERT.read_text())
    req(c['schema']=='STAGE32_MB104_W4_THIRD_DEPTH_ROOT_WALL_V1','schema')

    sq={'a1':1344,'a2':1344,'a3':1376,'b1':1152,'b2':1152,'b3':736,'c':1312}
    expected={
      'a1':Fraction(8,3),'a2':Fraction(8,3),'a3':Fraction(96,43),
      'b1':Fraction(52,9),'b2':Fraction(52,9),'b3':Fraction(416,23),
      'c':Fraction(128,41)}
    for k,q in sq.items():
        M=1568-q
        bd=Fraction(16*M,q)
        req(bd==expected[k],f'root degree bound {k}')
        req(c['primitive_pushdowns'][k]['result']=='ROOT_WALL_NONNEGATIVE',f'result {k}')

    for k in ('a1','a2','a3','c'):
        req(expected[k]<4,f'Kc-type d<2 {k}')
    req(c['kc_type']['source_even_degree'] is True,'Kc parity')

    V=nodes()
    names=['a1','a2','a3','b1','b2','b3']
    perms={name:sign_perm(V,k) for k,name in enumerate(names)}
    perms['c']=sign_perm(V,6)

    weights={}
    for name,p in perms.items():
        vals=[]
        for a,b in cycles2(p):
            vals.append(len({a,b}&SUPPORT))
        weights[name]=sorted([x for x in vals if x])
    req(weights['b1']==[1,2,2,2],'b1 weights')
    req(weights['b2']==[1,2,2,2],'b2 weights')
    req(weights['b3']==[1,1,2,2,2,2,2,2],'b3 weights')

    req(expected['b1']<9 and expected['b2']<9,'b12 degree bound')
    req(sum(weights['b1'])==7 and sum(weights['b2'])==7,'b12 total weights')
    req(c['kb_type']['line_exists'] is False,'no-line lemma retained')

    p=perms['b3']
    wp=[]
    for a,b in cycles2(p):
        n=len({a,b}&SUPPORT)
        if not n: continue
        q=project(V[a],5)
        req(canon(q)==canon(project(V[b],5)),'b3 pair projection')
        wp.append((canon(q),n))
    req(len(wp)==8 and sum(n for _,n in wp)==14,'b3 weighted packet')
    for q,n in wp:
        a1,a2,a3,b1,b2,cc=q
        req(z0(cc-a1-a2-1j*a3),'b3 special hyperplane')

    massA=massB=0
    countA=countB=0
    for q,n in wp:
        a1,a2,a3,b1,b2,cc=q
        onA=z0(a1+1j*a3) and z0(b2) and z0(cc-a2)
        onB=z0(a2+1j*a3) and z0(b1) and z0(cc-a1)
        req(onA ^ onB,'weighted point on exactly one reduced conic')
        if onA:
            massA+=n; countA+=1
        if onB:
            massB+=n; countB+=1
    req((massA,massB)==(7,7),'b3 conic masses')
    req((countA,countB)==(4,4),'b3 conic point counts')
    req(28-4*massA==0 and 28-4*massB==0,'b3 conic pairings')

    req(c['disposition']=='CLOSED_NEGATIVE','W4 disposition')
    req(c['remaining_user_selected_solo_routes']==['W5','W20','W16'],'remaining solo routes')
    for k,v in c['credit_firewall'].items():
        req(v is False,'credit '+k)

    print('PASS STAGE32_MB104_W4_THIRD_DEPTH_ROOT_WALL_V1')
    print('W4=closed_negative all seven coordinate pushdown root walls nonnegative')
    print('remaining_solo=W5,W20,W16 no_credit')

if __name__=='__main__':
    main()
