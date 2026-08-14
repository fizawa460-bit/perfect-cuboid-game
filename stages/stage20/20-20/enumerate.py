#!/usr/bin/env python3
"""Stage20-20 deterministic primitive/canonical Euler-cuboid census."""
import argparse,csv
from collections import defaultdict
from math import gcd,isqrt
from pathlib import Path
DEFAULT=(50,100,200,400,800,1200,1600,2000)
def square(n):
 r=isqrt(n); return r*r==n
def face_count(a,b,c):
 return sum((square(a*a+b*b),square(a*a+c*c),square(b*b+c*c)))
def pythagorean_adjacency(B):
 adj=defaultdict(set); m=2
 while m*m+1<=B:
  for n in range(1,m):
   if ((m-n)&1)==0 or gcd(m,n)!=1: continue
   h=m*m+n*n
   if h>B: break
   u,v=m*m-n*n,2*m*n
   for k in range(1,B//h+1):
    x,y=k*u,k*v; adj[x].add(y); adj[y].add(x)
  m+=1
 return adj
def enumerate_fast(B):
 adj=pythagorean_adjacency(B); out={}; B2=B*B
 for e,partners in adj.items():
  ps=sorted(partners)
  for i,x in enumerate(ps):
   for y in ps[i+1:]:
    a,b,c=sorted((e,x,y))
    if a==b or b==c or gcd(gcd(a,b),c)!=1: continue
    r2=a*a+b*b+c*c
    if r2>B2: continue
    if face_count(a,b,c)==3: out[(a,b,c)]=r2
 return out
def enumerate_brute(B):
 out={}; B2=B*B
 for a in range(1,B):
  for b in range(a+1,B):
   ab=a*a+b*b
   if ab+(b+1)*(b+1)>B2: break
   for c in range(b+1,isqrt(B2-ab)+1):
    if gcd(gcd(a,b),c)!=1: continue
    if face_count(a,b,c)==3: out[(a,b,c)]=ab+c*c
 return out
def rows(records,thresholds): return [{"B":B,"M3":sum(r2<=B*B for r2 in records.values())} for B in thresholds]
def main():
 p=argparse.ArgumentParser(); p.add_argument('--output',type=Path); p.add_argument('--verify',type=Path); p.add_argument('--self-check-b',type=int,default=400); a=p.parse_args()
 if a.verify:
  with a.verify.open(newline='',encoding='utf-8') as f: frozen=[{"B":int(r['B']),"M3":int(r['M3'])} for r in csv.DictReader(f)]
  th=tuple(r['B'] for r in frozen); regen=rows(enumerate_fast(max(th)),th)
  if regen!=frozen: raise SystemExit(f'frozen census mismatch: {regen}')
  if enumerate_fast(a.self_check_b)!=enumerate_brute(a.self_check_b): raise SystemExit('small-cutoff set mismatch')
  print(f'SMALL_CUTOFF_CROSSCHECK_B={a.self_check_b}:PASS'); print(f'FROZEN_CENSUS_MAX_B={max(th)}:PASS'); print('STAGE20_20_VERIFY=PASS'); return
 data=rows(enumerate_fast(max(DEFAULT)),DEFAULT)
 if a.output:
  with a.output.open('w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=('B','M3')); w.writeheader(); w.writerows(data)
 else: print(data)
if __name__=='__main__': main()
