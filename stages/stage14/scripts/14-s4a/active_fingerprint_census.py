#!/usr/bin/env python3
"""Stage14-s4a: full arithmetic fingerprint census of all active first-face vertices.

This is an infrastructure/data stage. It regenerates the 490 active Stage14 vertices
through B=2,000,000, reconstructs each actual first-hit elliptic point using the
merged s3 map, and records a common arithmetic fingerprint:

- primitive oriented face F=(S,X,H) and first physical partner;
- first-hit height mu(F);
- Euclid half-angle parameter for the first face;
- omega(2*S*X*H);
- exact Kummer square classes of (Z, Z-S^2, Z+X^2);
- canonical height of the actual first-hit point;
- unconditional PARI ellrank lower/upper bounds, Cassels-pairing term s,
  full-2-torsion Selmer dimension r2+2+s, and root number.

No claim is made that Selmer rank equals Mordell--Weil rank, or that the first-hit
point is a Mordell--Weil generator/minimum.
"""
from fractions import Fraction
from math import gcd, isqrt, log
from pathlib import Path
import json, runpy, shutil, subprocess

ROOT=Path(__file__).resolve().parents[4]
GRAPH_SCRIPT=ROOT/'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
OUTPUT=ROOT/'stages/stage14/data/14-s4a/active_fingerprint_census.json'
MAX_B=2_000_000


def first_hits_with_partner():
    mod=runpy.run_path(str(GRAPH_SCRIPT))
    keep,_=mod['enumerate_multi'](MAX_B)
    object_edges=mod['object_edges']
    first={}
    for (a,b,c,d),(mask,ds) in keep.items():
        if d>MAX_B or mask.bit_count()<2: continue
        for f1,f2 in object_edges(a,b,c,mask,ds):
            for f,p in ((f1,f2),(f2,f1)):
                key=(d,p)
                old=first.get(f)
                if old is None or key<(old[0],old[1]): first[f]=key
    assert len(first)==490
    return first


def curve_coeff(face):
    S,X,H=face
    assert gcd(S,X)==1 and S*S+X*X==H*H
    return X*X-S*S,-S*S*X*X


def physical_point(face,partner,d):
    S,X,H=face; S2,X2,H2=partner; g=gcd(S,S2)
    q=Fraction(X2,H2+S2); rho=Fraction(X,H); s=Fraction(S,H)
    z=Fraction(g*d,H*H2); A=1-2*rho*rho
    Yq=z*(1+q*q); X0=(Yq+1)/(q*q); U=A+X0
    x=U/(2*s*s); V=q*(X0*X0-1)/2; y=V/(2*s*s*s)
    t=Fraction(X,S)
    assert y*y==x*(x-1)*(x+t*t)
    Z=S*S*x; W=S*S*S*y
    a2,a4=curve_coeff(face)
    assert W*W==Z*Z*Z+a2*Z*Z+a4*Z
    return {'q':q,'z':z,'x':x,'y':y,'Z':Z,'W':W}


def euclid_half_angle(face):
    # For primitive Pythagorean F=(S,X,H), r=X/(H+S) satisfies X/S=2r/(1-r^2).
    S,X,H=face
    r=Fraction(X,H+S)
    assert Fraction(X,S)==2*r/(1-r*r)
    return r


def omega(n):
    n=abs(n); c=0
    if n%2==0:
        c+=1
        while n%2==0:n//=2
    p=3
    while p*p<=n:
        if n%p==0:
            c+=1
            while n%p==0:n//=p
        p+=2
    if n>1:c+=1
    return c


def ratstr(x):
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'


def gp_audit(rows):
    gp=shutil.which('gp')
    if gp is None: raise SystemExit("PARI/GP executable 'gp' required")
    lines=['default(parisizemax,8G);']
    for r in rows:
        S,X,H=r['face']; a2,a4=curve_coeff(tuple(r['face'])); P=r['_point']
        z=ratstr(P['Z']); w=ratstr(P['W'])
        lines.append(
            f'E=ellinit([0,{a2},0,{a4},0]);P=[{z},{w}];R=ellrank(E,0);'
            f'k1=core(numerator(P[1]))*core(denominator(P[1]));'
            f'k2=core(numerator(P[1]-{S*S}))*core(denominator(P[1]-{S*S}));'
            f'k3=core(numerator(P[1]+{X*X}))*core(denominator(P[1]+{X*X}));'
            f'print("{r["id"]}|",ellheight(E,P),"|",R[1],"|",R[2],"|",R[3],"|",ellrootno(E),"|",k1,"|",k2,"|",k3);'
        )
    lines.append('quit;')
    p=subprocess.run([gp,'-q'],input='\n'.join(lines)+'\n',text=True,capture_output=True,check=True)
    out={}
    for line in p.stdout.splitlines():
        if '|' not in line: continue
        z=line.strip().split('|')
        if len(z)==10: out[z[0]]=z[1:]
    assert len(out)==len(rows),(len(out),len(rows),p.stderr[-2000:])
    return out


def summarize(rows):
    hs=sorted(r['canonical_height'] for r in rows)
    rs={}
    for r in rows:
        key=f"{r['rank_lower']}..{r['rank_upper']}"
        rs[key]=rs.get(key,0)+1
    sc={}
    for r in rows:
        key=','.join(r['kummer_square_classes'])
        sc[key]=sc.get(key,0)+1
    top=sorted(sc.items(),key=lambda kv:(-kv[1],kv[0]))[:20]
    return {
        'active_vertices':len(rows),
        'mu_min':min(r['mu'] for r in rows),
        'mu_max':max(r['mu'] for r in rows),
        'canonical_height':{
            'min':hs[0], 'median':hs[len(hs)//2], 'mean':sum(hs)/len(hs), 'max':hs[-1]
        },
        'mean_canonical_over_log_mu':sum(r['canonical_over_log_mu'] for r in rows)/len(rows),
        'omega_2SXH':{
            'min':min(r['omega_2SXH'] for r in rows),
            'mean':sum(r['omega_2SXH'] for r in rows)/len(rows),
            'max':max(r['omega_2SXH'] for r in rows),
        },
        'rank_bound_histogram':rs,
        'rank_positive_certified':sum(r['rank_lower']>0 for r in rows),
        'rank_exact_certified':sum(r['rank_lower']==r['rank_upper'] for r in rows),
        'selmer_rank_gt_torsion':sum(r['selmer_2_rank']>2 for r in rows),
        'distinct_kummer_square_class_triples':len(sc),
        'top_kummer_square_class_triples':top,
    }


def main():
    first=first_hits_with_partner()
    rows=[]
    for i,f in enumerate(sorted(first,key=lambda f:(f[2],f[0],f[1]))):
        mu,p=first[f]; P=physical_point(f,p,mu); r=euclid_half_angle(f)
        S,X,H=f
        rows.append({
            'id':f'A{i:03d}', 'face':list(f), 'partner':list(p), 'mu':mu,
            'euclid_half_angle_r':ratstr(r), 'omega_2SXH':omega(2*S*X*H),
            '_point':P,
        })
    got=gp_audit(rows)
    for rec in rows:
        z=got[rec['id']]
        rec['canonical_height']=float(z[0]); rec['canonical_over_log_mu']=rec['canonical_height']/log(rec['mu'])
        rec['rank_lower']=int(z[1]); rec['rank_upper']=int(z[2]); rec['sha_2_mod_4_rank_s']=int(z[3]); rec['root_number']=int(z[4])
        rec['selmer_2_rank']=rec['rank_upper']+2+rec['sha_2_mod_4_rank_s']
        rec['kummer_square_classes']=[z[5],z[6],z[7]]
        rec['first_hit_point']={k:ratstr(v) for k,v in rec.pop('_point').items()}
        # Physical points are non-torsion by merged Stage14-4af; active => rank upper >=1.
        assert rec['rank_upper']>=1
    report={
        'metadata':{
            'stage':'14-s4a','max_B':MAX_B,'active_vertices':len(rows),'pari_effort':0,
            'record_key':'primitive oriented face F=(S,X,H)'
        },
        'field_contract':{
            'mu':'first physical Stage14 height d for this active face through the exact graph census',
            'euclid_half_angle_r':'r=X/(H+S), so X/S=2r/(1-r^2)',
            'omega_2SXH':'number of distinct prime divisors of 2*S*X*H',
            'kummer_square_classes':'square classes of (Z, Z-S^2, Z+X^2) represented by signed squarefree integers',
            'selmer_2_rank':'PARI full-2-torsion identity rank_upper + 2 + sha_2_mod_4_rank_s',
            'canonical_height':'PARI ellheight of the actual first-hit physical point',
            'rank_bounds':'unconditional PARI ellrank(E,0) lower/upper bounds; no Selmer=MW equality assumed'
        },
        'summary':None,
        'rows':rows,
        'decision':{
            'STAGE14_S4A':'COMPLETE_FULL_ACTIVE_ARITHMETIC_FINGERPRINT_CENSUS',
            'ALL_ACTIVE_VERTICES_FINGERPRINTED':True,
            'ACTIVE_VERTEX_COUNT':490,
            'FIRST_HIT_POINTS_RECONSTRUCTED_EXACTLY':True,
            'KUMMER_SQUARE_CLASSES_RECORDED':True,
            'PARI_RANK_SELMER_ENVELOPE_RECORDED':True,
            'CANONICAL_HEIGHT_RECORDED':True,
            'BISECTION_CLASSIFICATION_REQUIRED':False,
            'SQRT_B_ASYMPTOTIC_PROVED':False,
            'NEXT':'Stage14-s4b cluster active arithmetic fingerprints / compare with higher-degree strata'
        }
    }
    report['summary']=summarize(rows)
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report['summary'],indent=2))
    print(json.dumps(report['decision'],indent=2))

if __name__=='__main__': main()
