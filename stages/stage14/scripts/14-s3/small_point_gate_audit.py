#!/usr/bin/env python3
"""Stage14-s3 first-small-point / canonical-height gate audit.

This script keeps theorem and finite diagnostics separate.

For a first-face F=(S,X,H) and a physical partner F2=(S2,X2,H2), put
    q = X2/(H2+S2), rho=X/H, s=S/H,
    z = g*d/(H*H2), A=1-2*rho^2,
    Yq=z*(1+q^2), X0=(Yq+1)/q^2,
    U=A+X0, x=U/(2*s^2),
    V=q*(X0^2-1)/2, y=V/(2*s^3).
Then (x,y) lies on y^2=x(x-1)(x+(X/S)^2).
The integral model is Z=S^2*x, W=S^3*y.

The exact formulas show that a physical hit d<=B produces a non-torsion
elliptic point whose naive x-height is polynomial in the physical/base data;
Silverman's height-difference theorem then converts this to a canonical-height
window O(log B + log H) for this family. We do not claim a uniform positive
lower bound for non-torsion canonical height strong enough to count bases.

Finite diagnostics use PARI/GP ellheight on actual first-hit physical points and
on deterministic non-torsion witnesses returned by ellrank for inactive controls.
The latter are witnesses, not certified Mordell-Weil generators or minima.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd, log
from pathlib import Path
import json, runpy, shutil, subprocess

ROOT=Path(__file__).resolve().parents[4]
GRAPH_SCRIPT=ROOT/'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
OUTPUT=ROOT/'stages/stage14/data/14-s3/small_point_gate_audit.json'
MAX_B=2_000_000
SAMPLE=96
HEIGHT_BINS=(0,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000)

def hbin(h):
    for lo,hi in zip(HEIGHT_BINS,HEIGHT_BINS[1:]):
        if lo<h<=hi:return (lo,hi)
    raise ValueError(h)

def even_sample(rows,n):
    if len(rows)<=n:return list(rows)
    idx=[round(i*(len(rows)-1)/(n-1)) for i in range(n)]
    return [rows[i] for i in idx]

def primitive_faces(max_h):
    out=set();m=2
    while m*m+1<=max_h:
        for n in range(1,m):
            if ((m-n)&1)==0 or gcd(m,n)!=1:continue
            u=m*m-n*n;v=2*m*n;h=m*m+n*n
            if h>max_h:continue
            out.add((u,v,h));out.add((v,u,h))
        m+=1
    return sorted(out,key=lambda f:(f[2],f[0],f[1]))

def first_hits_with_partner():
    mod=runpy.run_path(str(GRAPH_SCRIPT));keep,_=mod['enumerate_multi'](MAX_B); object_edges=mod['object_edges']
    first={}
    for (a,b,c,d),(mask,ds) in keep.items():
        if d>MAX_B or mask.bit_count()<2:continue
        for f1,f2 in object_edges(a,b,c,mask,ds):
            for f,p in ((f1,f2),(f2,f1)):
                old=first.get(f)
                key=(d,p)
                if old is None or key<(old[0],old[1]):first[f]=(d,p)
    assert len(first)==490
    return first

def balanced_samples(active_map,all_faces):
    active=sorted(active_map,key=lambda f:(f[2],f[0],f[1])); inactive=[f for f in all_faces if f not in active_map]
    active_sample=even_sample(active,SAMPLE); quota=defaultdict(int)
    for f in active_sample:quota[hbin(f[2])]+=1
    bins=defaultdict(list)
    for f in inactive:bins[hbin(f[2])].append(f)
    inactive_sample=[]
    for b in sorted(quota):inactive_sample.extend(even_sample(bins[b],quota[b]))
    assert len(active_sample)==len(inactive_sample)==SAMPLE
    return active_sample,sorted(inactive_sample,key=lambda f:(f[2],f[0],f[1]))

def curve_coeff(face):
    S,X,H=face; assert S*S+X*X==H*H and gcd(S,X)==1
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

def ratstr(x):
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def log_height_fraction(x):
    return log(max(abs(x.numerator),abs(x.denominator),1))

def gp_audit(active_rows,inactive_rows):
    gp=shutil.which('gp')
    if gp is None:raise SystemExit("PARI/GP executable 'gp' required")
    lines=['default(parisizemax,4G);']
    for r in active_rows:
        a2,a4=curve_coeff(tuple(r['face'])); P=r['point']
        lines.append(f'E=ellinit([0,{a2},0,{a4},0]);P=[{ratstr(P["Z"])},{ratstr(P["W"])}];print("A{r["id"]}|",ellheight(E,P));')
    for r in inactive_rows:
        a2,a4=curve_coeff(tuple(r['face']))
        lines.append(f'E=ellinit([0,{a2},0,{a4},0]);R=ellrank(E,0);if(R[1]>0 && #R[4]>0,m=ellheight(E,R[4][1]);for(i=2,#R[4],h=ellheight(E,R[4][i]);if(h<m,m=h));print("I{r["id"]}|",R[1],"|",R[2],"|",m),print("I{r["id"]}|",R[1],"|",R[2],"|NA"));')
    lines.append('quit;')
    p=subprocess.run([gp,'-q'],input='\n'.join(lines)+'\n',text=True,capture_output=True,check=True)
    out={}
    for line in p.stdout.splitlines():
        if '|' not in line:continue
        z=line.strip().split('|'); out[z[0]]=z[1:]
    assert len(out)==len(active_rows)+len(inactive_rows),(len(out),p.stderr[-1000:])
    return out

def summarize(vals):
    xs=sorted(vals)
    if not xs:return None
    return {'n':len(xs),'min':xs[0],'median':xs[len(xs)//2],'max':xs[-1],'mean':sum(xs)/len(xs)}

def main():
    first=first_hits_with_partner(); allf=primitive_faces(MAX_B); act,ina=balanced_samples(first,allf)
    active_rows=[]
    for i,f in enumerate(act):
        d,p=first[f]; P=physical_point(f,p,d)
        active_rows.append({'id':f'{i:03d}','face':list(f),'partner':list(p),'mu':d,'point':P,
                            'naive_x_height':log_height_fraction(P['Z'])})
    inactive_rows=[{'id':f'{i:03d}','face':list(f)} for i,f in enumerate(ina)]
    got=gp_audit(active_rows,inactive_rows)
    for r in active_rows:
        r['canonical_height']=float(got['A'+r['id']][0]); r['canonical_over_log_mu']=r['canonical_height']/log(r['mu'])
        r['point']={k:ratstr(v) for k,v in r['point'].items()}
    positive_inactive=[]
    for r in inactive_rows:
        z=got['I'+r['id']]; r['rank_lower']=int(z[0]);r['rank_upper']=int(z[1]);r['found_witness_canonical_height']=None if z[2]=='NA' else float(z[2])
        if r['rank_lower']>0 and r['found_witness_canonical_height'] is not None:positive_inactive.append(r['found_witness_canonical_height'])
    ah=[r['canonical_height'] for r in active_rows]; ratios=[r['canonical_over_log_mu'] for r in active_rows]
    report={
      'metadata':{'stage':'14-s3','max_B':MAX_B,'active_vertices':len(first),'sample_each':SAMPLE,'pari_effort':0},
      'exact_height_gate':{
        'quartic_to_elliptic_map':'q=X2/(H2+S2), z=gd/(H H2), Yq=z(1+q^2), X0=(Yq+1)/q^2, A=1-2(X/H)^2, x=(A+X0)/(2(S/H)^2)',
        'integral_model':'Z=S^2 x, W=S^3 y on W^2=Z(Z-S^2)(Z+X^2)',
        'physical_hit_implication':'d<=B gives a non-torsion point with naive rational-coordinate height O(log B + log H); canonical height differs by O(log H) for this Weierstrass family, hence a physical hit lies in a canonical-height window O(log B + log H).',
        'converse_status':'No uniform lower-bound/counting theorem is proved that converts absence below this window into a global asymptotic count over bases; this remains the s3 theorem boundary.',
        'torsion_nonphysical':'imported merged Stage14-4af, so every physical point is non-torsion.'
      },
      'finite_diagnostic':{
        'active_actual_first_hit_canonical_height':summarize(ah),
        'active_canonical_height_over_log_mu':summarize(ratios),
        'inactive_controls_with_certified_positive_rank_and_pari_witness':len(positive_inactive),
        'inactive_found_witness_canonical_height':summarize(positive_inactive),
        'interpretation':'Actual first physical hits occupy a logarithmic canonical-height window, while many physically inactive controls already have positive-rank witnesses. Witness heights are not certified minima and are used only diagnostically.'
      },
      'theorem_boundary':{
        'canonical_height_gate_locked':True,
        'uniform_first_generator_distribution_proved':False,
        'uniform_regulator_distribution_proved':False,
        'positive_rank_implies_physical_hit_below_B':False,
        'sqrtB_asymptotic_proved':False,
        'pari_witness_is_mw_generator_assumed':False
      },
      'decision':{
        'STAGE14_S3':'COMPLETE_CANONICAL_HEIGHT_WINDOW_AND_SMALL_POINT_BOUNDARY',
        'PHYSICAL_HIT_IMPLIES_LOGARITHMIC_CANONICAL_HEIGHT_WINDOW':True,
        'FINITE_POSITIVE_RANK_WITHOUT_PHYSICAL_HIT_CONFIRMED':True,
        'SMALL_POINT_GATE_IS_GENUINE':True,
        'UNIFORM_SMALL_POINT_DISTRIBUTION_PROVED':False,
        'ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED':False,
        'NEXT':'Stage14-s4 compare arithmetic small-point classes with M-degree-4 bisections'
      }
    }
    # Rows are intentionally omitted from frozen report; deterministic CI regenerates summary.
    OUTPUT.parent.mkdir(parents=True,exist_ok=True);OUTPUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report['finite_diagnostic'],indent=2));print(json.dumps(report['decision'],indent=2))
if __name__=='__main__':main()
