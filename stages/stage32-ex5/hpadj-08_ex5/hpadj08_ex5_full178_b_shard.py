#!/usr/bin/env python3
from __future__ import annotations
import argparse, bisect, hashlib, json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / 'FULL178-SCALEOUT-CONTRACT.json'
CONTRACT_BLOB = 'fdc43237b84c00e615147b52f8a1f9d8d41ed5de'
CONTRACT_CANON = '23ab8ae0509754f94cdf7cc661e18e692ec2af3f20a2653d0d92c1a8ff5fa84b'
LOCKS = {
    'bounded_preflight': ('stages/stage32-ex5/hpadj-08_ex5/HPADJ08-EX5-EXACT-SQUARE-PREFLIGHT.json', '8ecc5ecd97838d4225de1d1163fd8843451b68e5'),
    'compressed_family': ('stages/stage32/residual-32-01-production/compressed_terminal_family.py', '90ff82ed312dcc0cb32cf207935945f550e29170'),
    'prefix_checkpoint': ('stages/stage32/residual-32-01-production/full178-prefix-indexed-compression-main-checkpoint.json', 'eb823cc2f99d74456d5701b4673f848f18ba3151'),
    'corrected_adjunction': ('stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json', 'c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e'),
}
HMAX=96
QCAP=4992
OVERFLOW=4993
PLANNED=((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))

def req(v,msg):
    if not v: raise SystemExit('FAIL: '+msg)

def git_blob(path: Path) -> str:
    raw=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def canon(obj):
    cp=dict(obj); cp.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(cp,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

def qcap(q): return q if q<=QCAP else OVERFLOW

def ceil_div(a,b): return -((-a)//b)

def component_a(d,a):
    h=d//2; return min(13,d-a,d-2*a+4,h+5)

def component3(d,b,c): return min(9,d-b-c,d-2*b,d-2*c+1)

def even_interval_normal_sum(d,lower,upper,excluded):
    lo=lower if lower%2==0 else lower+1; hi=upper if upper%2==0 else upper-1
    if lo>hi: return 0,0
    n=(hi-lo)//2+1; total=n*(19*d+1)-5*(n*(lo+hi)//2); count=n
    for e in sorted(excluded):
        if lo<=e<=hi and e%2==0:
            total-=19*d-5*e+1; count-=1
    return count,total

def build_a():
    A=[[defaultdict(int) for _ in range(4)] for __ in range(HMAX+1)]
    for a in range(HMAX+1):
        for x2 in range(a+1):
            for x3 in range(a-x2+1):
                x7=a-x2-x3; s=sum(v>0 for v in (x2,x3,x7))
                A[a][s][qcap(x2*x2+x3*x3+x7*x7)]+=1
    return A

def build_bc_shard(b0,b1):
    BC=[None]*(HMAX+1)
    for b in range(HMAX+1):
        if b0<=b<=b1: BC[b]=[[defaultdict(int) for _ in range(8)] for __ in range(HMAX+1)]
    B=[[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(HMAX+1)]
    C=[[[defaultdict(int) for _ in range(2)] for __ in range(4)] for ___ in range(HMAX+1)]
    for m in range(HMAX+1):
        for x9 in range(m+1):
            x5=m-x9; B[m][int(x5>0)+int(x9>0)][x9&1][qcap(x5*x5+x9*x9)]+=1
        for x8 in range(m+1):
            for x10 in range(m-x8+1):
                x6=m-x8-x10
                C[m][int(x6>0)+int(x8>0)+int(x10>0)][(x8+x10)&1][qcap(x6*x6+x8*x8+x10*x10)]+=1
    for x0 in range(HMAX+1):
        for x1 in range(x0+1,HMAX+1):
            extra=int(x0>0)+1; q01=x0*x0+x1*x1
            for b in range(max(b0,x1),min(b1,HMAX)+1):
                g2=b-x1
                for c in range(x0,HMAX+1):
                    g3=c-x0; dst=BC[b][c]
                    for sb in range(3):
                        for pb in (0,1):
                            left=B[g2][sb][pb]
                            if not left: continue
                            pc=pb^(x1&1)
                            for sc in range(4):
                                right=C[g3][sc][pc]
                                if not right: continue
                                out=dst[sb+sc+extra]
                                for ql,vl in left.items():
                                    for qr,vr in right.items(): out[qcap(q01+ql+qr)]+=vl*vr
    P=[[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(HMAX+1)]
    for m in range(HMAX+1):
        for x10 in range(m+1):
            x6=m-x10; P[m][int(x6>0)+int(x10>0)][x10&1][qcap(x6*x6+x10*x10)]+=1
    for t in range(HMAX+1):
        et=2*int(t>0)
        for x5 in range(HMAX-t+1):
            for x9 in range(HMAX-t-x5+1):
                b=t+x5+x9
                if not (b0<=b<=b1): continue
                for x8 in range(x5+1,HMAX-t+1):
                    qbase=2*t*t+x5*x5+x8*x8+x9*x9
                    sbase=et+int(x5>0)+1+int(x9>0); need=(t+x8+x9)&1
                    for m in range(HMAX-t-x8+1):
                        c=t+x8+m; dst=BC[b][c]
                        for sp in range(3):
                            pd=P[m][sp][need]
                            if not pd: continue
                            out=dst[sbase+sp]
                            for qp,vp in pd.items(): out[qcap(qbase+qp)]+=vp
    for t in range(HMAX+1):
        et=2*int(t>0)
        for u in range(HMAX-t+1):
            eu=2*int(u>0)
            for x9 in range(HMAX-t-u+1):
                b=t+u+x9
                if not (b0<=b<=b1): continue
                for x6 in range(min(x9,HMAX-t-u)+1):
                    max10=HMAX-t-u-x6; sbase=et+eu+int(x6>0)+int(x9>0)
                    qbase=2*t*t+2*u*u+x6*x6+x9*x9; need=(t+u+x9)&1
                    for x10 in range(max10+1):
                        if (x10&1)!=need: continue
                        c=t+u+x6+x10
                        BC[b][c][sbase+int(x10>0)][qcap(qbase+x10*x10)]+=1
    return BC

def hist(d):
    if not d: return ((),(),0)
    keys=sorted(d); pref=[]; s=0
    for k in keys: s+=d[k]; pref.append(s)
    return tuple(keys),tuple(pref),s

def pairs_gt(ha,hb,cut):
    ka,pa,ta=ha; kb,pb,tb=hb
    if not ka or not kb: return 0
    total=0; prev=0
    for i,qa in enumerate(ka):
        ca=pa[i]-prev; prev=pa[i]
        j=bisect.bisect_right(kb,cut-qa)
        le=pb[j-1] if j else 0
        total+=ca*(tb-le)
    return total

def census(b0,b1):
    A=build_a(); BC=build_bc_shard(b0,b1)
    AH=[[hist(A[a][s]) for s in range(4)] for a in range(HMAX+1)]
    records=[]; old_total=exact_total=0
    for g,dmax in ((0,176),(1,192)):
        for d in range(8,dmax+1,2):
            h=d//2; legacy=8 if g==0 else 4; K=ceil_div(d-16*g+16,4)
            cutoff=(d*d+16*d+(32 if g==0 else 0))//8
            ro=re=0
            for b in range(max(b0,0),min(b1,h)+1):
                for c in range(h+1):
                    c3=component3(d,b,c)
                    if c3<0: continue
                    for a in range(h+1):
                        ca=component_a(d,a)
                        if ca<0: continue
                        M=a+b+c; srem=min(16,d)+ca+c3
                        old_reject=8*a*a+8*b*b+6*c*c > 3*d*d+48*d+(96 if g==0 else 0)
                        for sbc in range(8):
                            bd=BC[b][c][sbc]
                            if not bd: continue
                            hb=hist(bd); btot=hb[2]
                            for sa in range(4):
                                ha=AH[a][sa]; atot=ha[2]
                                if not atot: continue
                                support=sbc+sa; qneed=K-support
                                if qneed>0 and srem<qneed: continue
                                lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))
                                upper=min((19*d)//5,3*d,3*d-(b-c))
                                if lower>upper: continue
                                excluded=set(); en=3*d-(b-c)
                                if b<=h-5 and support+srem==K and en-M>=srem: excluded.add(en)
                                if g==1 and d==8: excluded.add(8)
                                ne,norm=even_interval_normal_sum(d,lower,upper,excluded)
                                if ne<=0: continue
                                ex=pairs_gt(ha,hb,cutoff)
                                if old_reject: req(ex==atot*btot,f'Cauchy subset regression {(g,d,a,b,c,sa,sbc)}')
                                if old_reject: ro+=atot*btot*norm
                                re+=ex*norm
            records.append({'g':g,'d':d,'old_group_cauchy_candidate_rejected_terminals':ro,'stored_exact_square_candidate_rejected_terminals':re,'incremental_candidate_over_group_cauchy':re-ro})
            old_total+=ro; exact_total+=re
    stream=hashlib.sha256()
    for r in records: stream.update(json.dumps(r,sort_keys=True,separators=(',',':')).encode()+b'\n')
    return records,old_total,exact_total,stream.hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--b-start',type=int,required=True); ap.add_argument('--b-end',type=int,required=True); ap.add_argument('--output',required=True)
    ns=ap.parse_args(); b0,b1=ns.b_start,ns.b_end
    req((b0,b1) in PLANNED,'b interval is not a planned exact shard')
    req(git_blob(CONTRACT)==CONTRACT_BLOB,'scaleout contract blob drift')
    co=json.loads(CONTRACT.read_text()); req(co.get('canonical_sha256_without_this_field')==CONTRACT_CANON and canon(co)==CONTRACT_CANON,'scaleout contract canonical drift')
    for name,(rel,sha) in LOCKS.items(): req(git_blob(ROOT/rel)==sha,f'source drift {name}')
    records,old,exact,stream=census(b0,b1)
    out={'schema':'STAGE32EX5_HPADJ08_FULL178_B_SHARD_RESULT_V1','route_id':'HPADJ-08_ex5','b_interval':[b0,b1],'q_cap':QCAP,'row_count':len(records),'old_group_cauchy_candidate_rejected_terminals':old,'stored_exact_square_candidate_rejected_terminals':exact,'incremental_candidate_over_group_cauchy':exact-old,'row_stream_sha256':stream,'records':records,'firewalls':{'stage32_main_pruning_credit':False,'current_main_incremental_credit':False,'full178_complete':False,'merge_authorized':False}}
    out['canonical_sha256_without_this_field']=canon(out)
    Path(ns.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('b_interval','row_count','old_group_cauchy_candidate_rejected_terminals','stored_exact_square_candidate_rejected_terminals','incremental_candidate_over_group_cauchy','row_stream_sha256','canonical_sha256_without_this_field')},sort_keys=True))
if __name__=='__main__': main()
