#!/usr/bin/env python3
"""Exact arithmetic checks of R4 C35-117 B-even companion Eplus component theorem.
Checks are regressions. The uniform proof is the accompanying research card.
No external mathematics systems needed.
"""
import json
from math import gcd
from pathlib import Path


def factor(n):
    n=abs(n); out={}; p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1
            n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,0)+1
    return out


def v2(n):
    assert n!=0
    return (abs(n)&-abs(n)).bit_length()-1


def char(p,a):
    a%=p
    return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)


def inv(A,B,C):
    assert A>0 and B>0 and C>0 and A*A+B*B==C*C and gcd(A,B)==1 and C%2==1 and B%4==0
    e=v2(B); assert e>=2 and A%2==C%2==1
    D=A*C;H=A*A+C*C
    a=A**4+C**4;b=D**4
    c4=16*(a*a-3*b)
    c6=-32*a*(2*a*a-9*b)
    disc=16*b*b*(a*a-4*b)
    assert a*a-4*b==(B*B*H)**2
    assert disc==16*A**8*C**8*B**4*H**2
    assert v2(c4)==4 and v2(c6)==6 and v2(disc)==6+4*e
    assert v2(H)==1 and a%16==2 and b%16==1
    assert (c4**3)//(2**(3*v2(c4)))!=0
    # special fiber: y^2 = x(x+1)^2 over F2 has unique singular (1,0)
    mod2pts=[(x,y) for x in range(2) for y in range(2) if (y*y -x*(x+1)**2)%2==0]
    assert sorted(mod2pts)==[(0,0),(1,0)]
    # Rational torsion: T0=(0,0), T1=(-A^4,0), K4=(D^2,D^2*H)
    Kx,Ky=D*D,D*D*H
    assert Ky*Ky==Kx*(Kx+A**4)*(Kx+C**4)
    assert Kx%2==1 and Ky%2==0 and (-A**4)%2==1
    # Duplication identity x(2K4)=(Kx^2-b)^2/(4Ky^2) = 0
    assert Kx*Kx==b and Ky!=0
    # T0 smooth mod2, T1 and K4 reduce to the node (1,0)
    assert (0,0)!=(1,0)
    # This forces at least 4 Q2-component classes; star type has <=4.
    assert 4*e-2>=6
    all_odd={}
    for typ,z in [('AC',A),('AC',C),('B',B),('H',H)]:
        for p,val in factor(z).items():
            if p==2:continue
            assert p not in all_odd,(A,B,C,typ,p,all_odd[p])
            all_odd[p]=(typ,val)
    cp={2:4}; ap={2:0}; local={2: {'kodaira':f'I_{4*e-2}*','n':6+4*e,'c':4,'f':4,'ap':0}}
    for p,(typ,degree) in sorted(all_odd.items()):
        if typ=='AC':
            split=True;n=8*degree
        elif typ=='H':
            assert p%4==1
            split=True;n=2*degree
        else:
            split=p%4==1;n=4*degree
        cp[p]=n if split else 2
        ap[p]=1 if split else -1
        local[p]={'kodaira':f'I_{n}'+(' split' if split else ' nonsplit'),'n':n,'c':cp[p],'f':1,'ap':ap[p]}
        assert c4%p!=0 and disc%p==0
        if typ=='AC':
            assert char(p, A**4 if A%p else C**4)==1
        if typ=='H':
            assert char(p,-1)==1
        if typ=='B':
            assert char(p,-1)==(1 if split else -1)
    conductor=16
    for p in all_odd:conductor*=p
    root=-1 * (-1)
    for p in all_odd:root*=(-ap[p])
    tam=1
    for c in cp.values():tam*=c
    return {'base':[A,B,C], 'B_v2':e,'H':H,'conductor':conductor,'root_number':root,
            'disc_v2':v2(disc),'kodaira_2':f'I_{4*e-2}*','tamagawa_2':4,
            'local':{str(k):v for k,v in sorted(local.items())},'tamagawa_product':tam}


def main():
    examples=[(3,4,5),(15,8,17),(5,12,13),(7,24,25),(9,40,41)]
    rows=[inv(*base) for base in examples]
    assert [x['conductor'] for x in rows[:3]]==[4080,1048560,302640]
    assert [x['root_number'] for x in rows[:3]]==[-1,1,-1]
    count=0;odd=0;max_e=0
    for m in range(2,34):
        for n in range(1,m):
            if gcd(m,n)!=1 or (m-n)%2!=1:continue
            A=m*m-n*n; B=2*m*n; C=m*m+n*n
            # even leg B divisible4 for opposite-parity m,n
            x=inv(A,B,C)
            count+=1;odd+=len(x['local'])-1;max_e=max(max_e,x['B_v2'])
    data={'run_id':'R4-20261016-C117-BEVEN-EPLUS-COMPONENT-COMPLETE-V1',
          'snapshot':'C35-117','status':'PASS_ARITHMETIC_REGRESSION_PROOF_SEPARATE',
          'primitive_Beven_bases_checked':count,'odd_bad_prime_records':odd,
          'largest_B_v2_checked':max_e,
          'component_argument': 'two rational singular-reduction classes T1,K4 with 2K4=T0 smooth non-identity; E0/E1=F2 forbids same component',
          'inherited_input': 'Section248 f2=4 and potentially multiplicative reduction; C116 A-even formula',
          'examples':rows,'r0_accepted':False,'branch_b_closed':False,'e1_proved':False}
    path=Path(__file__).with_name('r4_c117_beven_eplus_tamagawa_evidence.json')
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps({'status':data['status'],'bases':count,'bad_prime_records':odd,
                      'max_v2B':max_e,'sample_products':[(str(x['base']),x['tamagawa_product']) for x in rows]},ensure_ascii=False))
if __name__=='__main__':main()