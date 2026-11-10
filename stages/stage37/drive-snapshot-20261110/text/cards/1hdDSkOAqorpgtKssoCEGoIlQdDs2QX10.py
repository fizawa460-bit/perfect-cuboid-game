#!/usr/bin/env python3
import csv,json,math,hashlib,pathlib
p=pathlib.Path('M3-T11-207-raw-census.tsv')
rows=list(csv.DictReader(p.open(),delimiter='\t'));rows=[{k:int(v) for k,v in r.items()} for r in rows]
def sq(x):return math.isqrt(x)**2==x
keys=[]
for r in rows:
 e=[r['a'],r['b'],r['c']];R=r['R'];t=R*R
 assert 0<e[0]<e[1]<e[2] and R<=10**6 and math.gcd(*e)==1 and sum(x*x for x in e)==t
 h=[math.gcd(R,x) for x in e];eligible=[i for i in range(3) if sq(t-e[i]**2)]
 assert len(eligible)==r['integral_faces']>=2
 craw=max(h[i]*h[j] for i in eligible for j in eligible if i<j)
 assert craw==r['c_raw_max'] and sorted(h)==[r['h_min'],r['h_mid'],r['h_max']]
 assert sorted(h)[1]*sorted(h)[2]==r['c_max'] and craw<=r['c_max']
 keys.append(tuple(e))
assert len(keys)==len(set(keys))==255
independent=[tuple(map(int,l.split())) for l in pathlib.Path('M3-T11-207-euclid-keys.tsv').read_text().splitlines()]
assert sorted(keys)==sorted(independent)
exponents=[(3,16),(5,24),(11,48)];spectrum=[]
for B in [1000,10000,100000,1000000]:
 subset=[r for r in rows if r['R']<=B]
 for num,den in exponents:
  tail=[r for r in subset if r['c_max']**den>B**num]
  chart=[r for r in subset if r['c_raw_max']**den>B**num]
  spectrum.append(dict(B=B,exponent=f'{num}/{den}',threshold_display=B**(num/den),total=len(subset),content_tail=len(tail),chart_tail=len(chart),median1_content_tail=sum(r['h_mid']==1 for r in tail),median1_chart_tail=sum(r['h_mid']==1 for r in chart),median_gt1_chart_tail=sum(r['h_mid']>1 for r in chart),mismatches=sum(r['c_max']!=r['c_raw_max'] for r in subset),endpoints=sum(r['integral_faces']==3 for r in subset),chart_scaled_display=len(chart)*B**(num/den-.5)))
mismatch=[r for r in rows if r['c_max']!=r['c_raw_max']]
result=dict(card='M3-T11-207',scope='FINITE_ONLY; no asymptotic saving; Gate OPEN/global credit 0',B=10**6,objects=255,known_population_reproduced_from='M3-T11-160',independent_enumeration='divisors of a^2 versus primitive Euclid triples and all scales; exact key-set equality',boundary_rule='strict integer comparison c^den>B^num; decimals display only',mismatch_count=len(mismatch),mismatch_examples=mismatch[:5],spectrum=spectrum,files={f:hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest() for f in ['stage37_raw_tail_207.cpp','stage37_raw_tail_207_euclid.cpp','stage37_raw_tail_207_verify.py','M3-T11-207-raw-census.tsv','M3-T11-207-euclid-keys.tsv']})
pathlib.Path('M3-T11-207-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
