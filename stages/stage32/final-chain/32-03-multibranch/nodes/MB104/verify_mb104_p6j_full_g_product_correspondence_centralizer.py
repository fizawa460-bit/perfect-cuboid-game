#!/usr/bin/env python3
from __future__ import annotations

import json
from itertools import product
from pathlib import Path

def req(c:bool,m:str)->None:
 if not c: raise SystemExit('FAIL: '+m)

def dot(a,b): return sum(x*y for x,y in zip(a,b))%2

def main()->None:
 c=json.loads(Path(__file__).with_name('MB104-P6J-FULL-G-PRODUCT-CORRESPONDENCE-CENTRALIZER-CERTIFICATE.json').read_text())
 G=list(product((0,1),repeat=3))
 singular={(1,0,0),(0,1,0),(0,0,1)}
 def tr(g):
  if g==(0,0,0): return 5
  return -3 if g in singular else 1
 mult={}
 for chi in G:
  num=sum((1 if dot(chi,g)==0 else -1)*tr(g) for g in G)
  req(num%8==0,'Fourier integrality')
  mult[chi]=num//8
 by_weight={w:sorted(v for k,v in mult.items() if sum(k)==w) for w in range(4)}
 req(by_weight[0]==[0],'weight0')
 req(by_weight[1]==[0,0,0],'weight1')
 req(by_weight[2]==[1,1,1],'weight2')
 req(by_weight[3]==[2],'weight3')
 dim=sum(v*v for v in mult.values())
 req(dim==7,'centralizer dimension')
 req(c['complex_centralizer']['dimension']==7,'certificate dimension')
 req(c['findings']['historical_e2_PhiZ_zero_imported'] is False,'no e2 import')
 req(c['findings']['integral_algebraic_centralizer_classified'] is False,'interface wall')
 req(c['next_leaf']=='MB104-P6K-FULL-G-CHARACTER-SQUARE-CLASS-COUPLING','next leaf')
 req(all(v is False for v in c['firewalls'].values()),'credit firewall')
 print('PASS: P6J full-G complex centralizer')
 print('multiplicities weight0/1/2/3 = 0 / 0,0,0 / 1,1,1 / 2')
 print('End_C(H0(K))^G = C^3 x M2(C), dimension 7')
 print('integral algebraic centralizer remains an interface')

if __name__=='__main__':
 main()
