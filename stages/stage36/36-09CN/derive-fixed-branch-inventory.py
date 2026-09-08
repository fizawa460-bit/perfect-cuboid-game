#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]

def load(path:Path,name:str):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

CK=load(ROOT/'stages/stage36/verify_stage36_36_09CK.py','ck')
CI=load(ROOT/'stages/stage36/verify_stage36_36_09CI.py','ci')
CH=load(ROOT/'stages/stage36/verify_stage36_36_09CH.py','ch')
CE=load(ROOT/'stages/stage36/verify_stage36_36_09CE.py','ce')
CF=load(ROOT/'stages/stage36/verify_stage36_36_09CF.py','cf')
CG=load(ROOT/'stages/stage36/verify_stage36_36_09CG.py','cg')
CC=load(ROOT/'stages/stage36/verify_stage36_36_09CC.py','cc')
BU=load(ROOT/'stages/stage36/verify_stage36_36_09BU.py','bu')


def parity_support(n:int):
    out=[]
    for q in BU.primes(abs(n)):
        if BU.vq(n,q)%2:
            out.append(q)
    return out


def main():
    a,b=1,2
    rows,kept,obs=CK.panel(a,b,CI,CE,CF,CG,CC,BU,CH)
    assert len(rows)==3 and len(kept)==3 and not obs
    i,row=kept[0]
    A,B,C,D,eta,e,f,mu,qok=row
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b); Q=a*a+b*b
    kappa=eta*(2**e)*C; rho=(2**f)*D
    xi=[A*B,kappa*A,rho*A]
    supports=[parity_support(x) for x in xi]
    finite=sorted(set(q for ss in supports for q in ss))
    payload={
        'selection':'p=1/2, first CK survivor in exact CK.panel order',
        'panel':{'a':a,'b':b,'P':P,'M':M,'D0':D0,'Q':Q,'row_index':i,'row':list(row),'all_CK_survivor_indices':[j for j,_ in kept]},
        'global_class':{'kappa':kappa,'rho':rho,'Xi_BT':xi,'coordinate_parity_supports':supports},
        'required_place_inventory':['2',*[str(q) for q in finite if q!=2],'infinity'],
        'real_signs':[1 if x>0 else -1 for x in xi],
    }
    print(json.dumps(payload,sort_keys=True))

if __name__=='__main__':
    main()
