#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

def req(c: bool,m: str)->None:
    if not c: raise SystemExit('FAIL: '+m)

def involution(n:int, edges:list[list[int]])->list[int]:
    p=list(range(n)); used=set()
    for a,b in edges:
        req(a!=b,'loop edge')
        req(0<=a<n and 0<=b<n,'edge range')
        req(a not in used and b not in used,'not a matching')
        used.add(a); used.add(b); p[a]=b; p[b]=a
    return p

def connected(n:int, groups:list[list[list[int]]])->bool:
    adj=[[] for _ in range(n)]
    for edges in groups:
        for a,b in edges:
            adj[a].append(b); adj[b].append(a)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==n

def compose(p:list[int],q:list[int])->list[int]:
    return [p[q[i]] for i in range(len(p))]

def build(c:dict,l:int):
    req(l>=1,'l>=1')
    A0=c['base_involutions']['A_transpositions']
    B0=c['base_involutions']['B_transpositions']
    C0=c['base_involutions']['C_transpositions']
    cut=tuple(c['designated_nonbridge_A_edge'])
    A=[]; B=[]; C=[]
    if l==1:
        A=[e[:] for e in A0]
    else:
        for k in range(l):
            off=56*k
            for a,b in A0:
                if tuple(sorted((a,b)))==tuple(sorted(cut)): continue
                A.append([a+off,b+off])
        for k in range(l):
            A.append([32+56*k,30+56*((k+1)%l)])
    for k in range(l):
        off=56*k
        B.extend([[a+off,b+off] for a,b in B0])
        C.extend([[a+off,b+off] for a,b in C0])
    return 56*l,A,B,C

def verify_l(c:dict,l:int)->None:
    n,A,B,C=build(c,l)
    pa,pb,pc=involution(n,A),involution(n,B),involution(n,C)
    req(len(A)==16*l and len(B)==24*l and len(C)==16*l,'transposition counts')
    req(sum(x==i for i,x in enumerate(pa))==24*l,'A fixed')
    req(sum(x==i for i,x in enumerate(pb))==8*l,'B fixed')
    req(sum(x==i for i,x in enumerate(pc))==24*l,'C fixed')
    req(connected(n,[A,B,C]),'transitivity graph')
    prod=list(range(n))
    for p in (pa,pa,pb,pb,pc,pc): prod=compose(p,prod)
    req(prod==list(range(n)),'product one')
    total_index=2*(len(A)+len(B)+len(C))
    req(total_index==112*l,'total index')
    two_g_minus_two=-2*n+total_index
    req(two_g_minus_two==0,'genus one')

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--l',type=int,default=7)
    a=ap.parse_args()
    c=json.loads(Path(__file__).with_name('MB104-P6G-SIX-VALUE-HURWITZ-FEASIBILITY-CERTIFICATE.json').read_text())
    # Base graph and the designated cut edge are checked independently.
    n,A,B,C=build(c,1)
    req(connected(n,[A,B,C]),'base graph connected')
    cut=tuple(c['designated_nonbridge_A_edge'])
    Aminus=[e for e in A if tuple(sorted(e))!=tuple(sorted(cut))]
    req(len(Aminus)==len(A)-1,'cut edge present once')
    req(connected(n,[Aminus,B,C]),'designated A edge must be nonbridge')
    # Check the user-selected l and several boundary samples of the general construction.
    for l in sorted(set([1,2,3,a.l])):
        verify_l(c,l)
    req(c['per_l']['fixed_counts']==[24,24,8,8,24,24],'passport fixed counts')
    req(c['per_l']['unramified_pair_totals']==[48,16,48],'passport pair totals')
    req(c['conclusion']=='ONE_FACTOR_SIX_VALUE_SCALAR_PASSPORT_REALIZABLE_FOR_EVERY_L','conclusion')
    req(all(v is False for v in c['firewalls'].values()),'credit firewall')
    print('PASS: P6G abstract Hurwitz passport construction')
    print('verified construction at l =',a.l)
    print('general construction: cyclic rewiring of one certified nonbridge A-edge per block')
    print('one-factor scalar passport is not an exclusion mechanism')

if __name__=='__main__':
    main()
