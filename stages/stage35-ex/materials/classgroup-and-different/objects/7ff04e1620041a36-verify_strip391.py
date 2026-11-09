#!/usr/bin/env python3
import json,sys,hashlib
from pathlib import Path
from math import isqrt
from collections import Counter
from flint import arb,ctx
ctx.prec=128
HERE=Path(__file__).resolve().parent
fs_path=HERE/'factorizations391.json'
fs={int(p):d for p,d in json.loads(fs_path.read_text()).items()}
tail_path=HERE/'tail_roots_independent.csv';raw=tail_path.read_bytes();assert hashlib.sha256(raw).hexdigest()=='572183b2eccf59e0d6327834b5dc957c6bcdffb37aecabf4a637574ac595bee7'
tail=[tuple(map(int,line.split(','))) for line in raw.decode().splitlines()];assert len(tail)==147058 and sum(k for p,k in tail)==147527
cut=1982760;sieve=bytearray(b'\x01')*(cut+1);sieve[:2]=b'\x00\x00'
for p in range(2,isqrt(cut)+1):
 if sieve[p]:sieve[p*p::p]=b'\x00'*((cut-p*p)//p+1)
assert [p for p,k in tail]==[p for p in range(5004,cut+1) if sieve[p]]
assert all(p in fs for p in range(3,5004,2) if sieve[p])
limit=10**12;atoms=Counter({2**7:1,2**28:1});high=0
for p,(ds,es) in fs.items():
 for d in ds:
  N=p**d
  if N<=limit:atoms[N]+=1
  else:high+=1
for p,k in tail:
 if p in fs:assert fs[p][0].count(1)==k
 elif k:atoms[p]+=k
n=105;r1=7;D=117981248819779519774066150957208102315271607402605667641283959829993045399028658031316657246104332689903983273746149168969341985775210396795186114853102963382274291541213184
A=arb.const_euler()+(4*arb.pi()).log()+arb(r1)/n-arb(D).log()/n
P=arb(0);Plow=arb(0)
for N,k in sorted(atoms.items()):
 a=arb(N);w=4*arb(k)*a.log()/n
 P+=w*(1/(a+1)+1/(a*(a-1)))
 Plow+=w/(a+1)
P+=high*4*arb(limit).log()/(n*(limit-1))
score=A+P;extra_weight=4*arb(cut+1).log()/(n*cut)
assert A<arb(-31)/50 and P<arb(99)/250 and score<-arb(28)/125
assert extra_weight<arb(7)/25000000
assert score+800000*extra_weight<0
out={'source_factorizations':'factorizations391.json','factorizations_sha256':hashlib.sha256(fs_path.read_bytes()).hexdigest(),'distinct_rational_primes':len(fs),
 'exact_norm_atoms_below_1e12':len(atoms),'multiplicity_below_1e12':sum(atoms.values()),'coarsely_bounded_high_norm_ideals':high,
 'complete_low_norm_cutoff':cut,'tail_csv_sha256':hashlib.sha256(raw).hexdigest(),
 'archimedean_limit_A':str(A),'available_prime_envelope_upper_expression':str(P),
 'available_score_upper_expression':str(score),'safe_upper_score_rational':'-28/125',
 'one_new_atom_weight_cap':str(extra_weight),'score_plus_800000_maximal_new_atoms':str(score+800000*extra_weight),
 'scope':'All real even continuous compactly supported normalized F with Re Phi(s)>=0 throughout the critical strip, using only the supplied finite prime corpus and no positive lower bound from omitted terms. The Fourier envelope is proved in STRIP_POSITIVITY.md, not by numerical sampling.',
 'no_global_Cl2_conclusion':True}
example=-arb(1)/(2*(arb(1)/2).cosh());assert example<-arb(2)/5
out['sign_changing_example_F_at_1']=str(example)
out['analytic_envelope_paper_proof_required']=True
print(json.dumps(out,indent=2))
