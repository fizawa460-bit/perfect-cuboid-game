#!/usr/bin/env python3
from __future__ import annotations

import base64, bz2, csv, io, json, math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
S13 = ROOT / 'stages/stage13/data/13-3/raw_incidence_report.json'
S14 = ROOT / 'stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64'
CHECKPOINTS = (100_000, 200_000, 300_000, 400_000, 500_000, 750_000, 1_000_000)
FACES = ('ab','ac','bc')
STAGE13_LIMIT = {'ab':0.5347369332313988,'ac':0.24535917783225203,'bc':0.21990388893634913}
ENDPOINT_433 = {'ab':0.4,'ac':0.3,'bc':0.3}


def is_square(n:int)->bool:
    r=math.isqrt(n); return r*r==n


def generate_indexes(bound:int):
    hyp=defaultdict(list); leg=defaultdict(list); triples=0
    for m in range(2, math.isqrt(bound)+1):
        for n in range(1,m):
            if (m-n)%2==0 or math.gcd(m,n)!=1: continue
            u=m*m-n*n; v=2*m*n; w=m*m+n*n
            if w>bound: continue
            if u>v: u,v=v,u
            k=1
            while k*w<=bound:
                x,y,d=k*u,k*v,k*w
                hyp[d].append((x,y)); leg[x].append((y,d)); leg[y].append((x,d))
                triples+=1; k+=1
    return hyp,leg,triples


def enumerate_objects(bound:int):
    hyp,leg,triples=generate_indexes(bound)
    masks={}; glued=0
    for p,face_pairs in hyp.items():
        ext=leg.get(p)
        if not ext: continue
        for x,y in face_pairs:
            for z,d in ext:
                glued+=1
                a,b,c=sorted((x,y,z))
                if not (a<b<c) or math.gcd(math.gcd(a,b),c)!=1: continue
                key=(a,b,c,d)
                if key in masks: continue
                vals=(a*a+b*b,a*a+c*c,b*b+c*c)
                mask=sum((1<<i) for i,v in enumerate(vals) if is_square(v))
                if mask==0 or a*a+b*b+c*c!=d*d: raise ArithmeticError(key)
                masks[key]=mask
    return masks, {'integer_pythagorean_triples':triples,'glued_records_before_filters':glued,'distinct_primitive_canonical_objects_with_at_least_one_face':len(masks)}


def load_frozen_pairs():
    raw=bz2.decompress(base64.b64decode(''.join(S14.read_text(encoding='ascii').split()))).decode()
    rows=[{k:int(r[k]) for k in ('a','b','c','d','mask')} for r in csv.DictReader(io.StringIO(raw))]
    return rows


def counts_at(masks,bound):
    raw=[0,0,0]; one=[0,0,0]; pair=[0,0,0]; triple=0
    for (a,b,c,d),mask in masks.items():
        if d>bound: continue
        for i in range(3):
            if mask&(1<<i): raw[i]+=1
        if mask.bit_count()==1: one[mask.bit_length()-1]+=1
        elif mask==0b011: pair[0]+=1
        elif mask==0b101: pair[1]+=1
        elif mask==0b110: pair[2]+=1
        elif mask==0b111: triple+=1
    return raw,one,pair,triple


def frozen_pair_at(rows,bound):
    p=[0,0,0]; t=0
    for r in rows:
        if r['d']>bound: continue
        m=r['mask']
        if m==0b011:p[0]+=1
        elif m==0b101:p[1]+=1
        elif m==0b110:p[2]+=1
        elif m==0b111:t+=1
    return p,t


def norm(d):
    s=sum(d.values()); return {k:d[k]/s for k in d}


def required_survival():
    q={k:ENDPOINT_433[k]/STAGE13_LIMIT[k] for k in FACES}
    z=q['bc']; return {k:q[k]/z for k in FACES}


def main():
    masks,diag=enumerate_objects(max(CHECKPOINTS))
    frozen=load_frozen_pairs()
    rows=[]
    s13=json.loads(S13.read_text())['rows'][-1]
    target=required_survival()
    for B in CHECKPOINTS:
        raw,one,pair,t=counts_at(masks,B)
        fp,ft=frozen_pair_at(frozen,B)
        if pair!=fp or t!=ft: raise ArithmeticError(f'frozen pair mismatch B={B}: {pair,t} vs {fp,ft}')
        if B==100_000:
            exp_raw=[s13['raw_incidence'][q] for q in FACES]
            exp_one=[s13['exact_one'][q] for q in FACES]
            if raw!=exp_raw or one!=exp_one: raise ArithmeticError(f'Stage13 lock failed: {raw,one}')
        endpoint=[pair[0]+pair[1]+2*t,pair[0]+pair[2]+2*t,pair[1]+pair[2]+2*t]
        removed=[raw[i]-one[i] for i in range(3)]
        if endpoint!=removed: raise ArithmeticError(f'endpoint identity B={B}: {endpoint} != {removed}')
        surv=[endpoint[i]/raw[i] for i in range(3)]
        rel=[x/surv[2] for x in surv]
        shape=[x/sum(surv) for x in surv]
        target_shape=list(norm(target).values())
        rows.append({'B':B,'raw':raw,'exactly_one':one,'pair_a_b_c':pair,'triple':t,'endpoint':endpoint,
                     'N2_exactly_two':sum(pair),'survival':surv,'survival_rel_bc':rel,
                     'survival_shape_L1_to_stage13limit_plus_221_target':sum(abs(shape[i]-target_shape[i]) for i in range(3))})
    report={'stage':'14-num-alpha11-diag8','classification':'EXTENDED_RAW_FACE_DENOMINATOR_CENSUS',
            'checkpoints':list(CHECKPOINTS),'enumeration_diagnostics':diag,
            'required_relative_survival_if_stage13_limit_plus_hypothetical_221':target,
            'rows':rows,
            'decision':{
                'EXTENDED_DENOMINATOR_CENSUS_COMPLETE':True,
                'STAGE13_B100K_LOCK_REPRODUCED':True,
                'FROZEN_STAGE14_PAIR_COUNTS_MATCH_AT_ALL_CHECKPOINTS':True,
                'RAW_MINUS_EXACT_ONE_ENDPOINT_IDENTITY_AT_ALL_CHECKPOINTS':True,
                'SURVIVAL_PROFILE_PERSISTENCE_IS_FINITE_DIAGNOSTIC_ONLY':True,
                'ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM':False,
                'ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM':False,
                'NEXT':'Stage14-num-alpha11-diag9 test shell-wise survival drift and extrapolation against Stage13 theorem bridge using the extended denominator panel'
            }}
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__': main()
