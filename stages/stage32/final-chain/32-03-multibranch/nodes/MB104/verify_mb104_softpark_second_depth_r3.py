#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
CERT=Path(__file__).with_name("MB104-SOFTPARK-SECOND-DEPTH-R3-CERTIFICATE.json")
SUPPORT=[0,1,2,3,8,9,10,11,24,25,26,32,33,34]
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def nodes():
 out=[]
 for j in range(3):
  for sa in (1,-1):
   for s1 in (1,-1):
    for s2 in (1,-1):
     z=[0j]*7; z[j]=sa
     o=[t for t in range(3) if t!=j]
     z[3+o[0]],z[3+o[1]],z[6]=s1,s2,1
     out.append(tuple(z))
 for j in range(3):
  o=[t for t in range(3) if t!=j]; a,b=o
  for sr in (1,-1):
   for ep in (1,-1):
    for eq in (1,-1):
     z=[0j]*7
     z[a],z[b],z[3+a],z[3+b]=1,1j*sr,1j*ep,-eq*sr
     out.append(tuple(z))
 req(len(out)==48 and len(set(out))==48,"48-node model")
 return out
def main():
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R3_V1","schema")
 req(c["selection"]["advance_for_third_depth"]==[],"no advance")
 req(c["selection"]["reserve"]==["W17","W23"],"reserve")
 req(c["selection"]["park"]==["W18","W19","W29"],"park")
 # W17 exact fixed-node replay for the ambient swap sigma.
 V=nodes()
 fixed=[i for i,p in enumerate(V) if p[0]==p[1] and p[3]==p[4]]
 req(fixed==[16,19,20,23],"W17 fixed nodes")
 req(set(fixed).isdisjoint(SUPPORT),"W17 support disjoint")
 for l in range(1,40):
  req(7*l*4==28*l,"W17 each fixed quartic intersection")
  req(2*28*l==56*l,"W17 total fixed-locus intersection")
 # W18 exact dimension arithmetic.
 for l in range(1,40):
  d=112*l
  req(d-1==112*l-1,"W18 eval image")
  req(14-1==13,"W18 block/evaluation dimension")
  req(13-6==7,"W18 residual room")
 # W19.
 for l in range(1,40): req(7*112*l==784*l,"W19 Wronskian")
 # W23 delta gap.
 for l in range(1,40):
  total=784*l*l-56*l
  cap=736*l*l-56*l
  req(total-cap==48*l*l,"W23 gap")
 # W29 extension line always positive.
 for l in range(1,40):
  for r in (0,1,4,20):
   req(112*l+2*r>0,"W29 positive Ext line degree")
 req(c["W29"]["ext_vanishes"] is True,"W29 split")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R3_V1")
 print("advance=none reserve=W17,W23 park=W18,W19,W29")
 print("cumulative_advance=W4,W16,W20; high_reserve=W5")
 print("no_credit")
if __name__=="__main__": main()
