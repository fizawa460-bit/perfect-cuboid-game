#!/usr/bin/env python3
"""Stage14-num6 rolling exact observatory append through B=150m.

Fresh mode consumes raw Stage14-num3 chunk reports; replay mode consumes this
stage's compact bzip2+base64 object source.  The merged Stage14-num5 B<=100m
history is treated as an immutable prefix.  New fits/anomaly gates are finite
heuristics only and never theorem or perfect-cuboid existence claims.
"""
from __future__ import annotations

import argparse, base64, bz2, csv, hashlib, importlib.util, io, json, math
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
ANCHOR=100_000_000
BOUND=150_000_000
STEP=5_000_000
PRIMES=(2,3,5,7,11,13)
NUM3_PATH=ROOT/'stages/stage14/scripts/14-num3/extended_exact_census.py'
NUM5_PATH=ROOT/'stages/stage14/scripts/14-num5/scaling_anomaly_diagnostics.py'
ANCHOR_LOCK={
 'object_count':1875,
 'counts':{'a':729,'b':758,'c':388,'total':1875,'triple':0},
 'object_key_sha256':'b8151aedbf46f33700b213c79a5227fa62653d2279eed954103a2b9e768fff42',
 'object_key_mask_sha256':'2ac9a994f735d2d4f8f3c519145de17d920bdcf9841f32a73793cae3ec94e14f',
 'vertex_ledger_sha256':'99f9cf72d473df19a2fc27e04032095607995ea43d874afd08a15e7fc7e240f0',
 'edge_ledger_sha256':'c54aa6fea7971a44e317a041986ca1197671af2cab97825943ebb9d51cadd97e',
 'max_degree':11,
}

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

num3=load_module('stage14_num3',NUM3_PATH)
num5=load_module('stage14_num5',NUM5_PATH)

def sha(data:bytes): return hashlib.sha256(data).hexdigest()
def close(a,b,tol=1e-12):
    if a is None or b is None: return a is b
    return abs(float(a)-float(b)) <= tol*max(1.0,abs(float(a)),abs(float(b)))

def read_chunks(root:Path):
    paths=sorted(root.rglob('chunk-*.json'))
    if not paths: raise ArithmeticError('no chunk reports')
    reports=[json.loads(p.read_text()) for p in paths]
    meta=reports[0]['metadata']; C=int(meta['chunk_count']); B=int(meta['bound'])
    seen=sorted(int(r['metadata']['chunk_index']) for r in reports)
    if seen != list(range(C)): raise ArithmeticError(f'missing/duplicate chunks: {seen}')
    if any(int(r['metadata']['bound'])!=B or int(r['metadata']['chunk_count'])!=C for r in reports):
        raise ArithmeticError('chunk metadata mismatch')
    objects=sorted({tuple(map(int,row)) for r in reports for row in r['objects']})
    return objects,{'mode':'fresh_num3_chunks','bound':B,'chunk_count':C,
                    'chunk_sha256':[{'name':p.name,'sha256':sha(p.read_bytes())} for p in paths]}

def decode_source(path:Path):
    encoded=''.join(path.read_text(encoding='ascii').split())
    packed=base64.b64decode(encoded); raw=bz2.decompress(packed).decode()
    objects=[tuple(int(r[k]) for k in ('a','b','c','d','mask')) for r in csv.DictReader(io.StringIO(raw))]
    if len(objects)!=len(set(objects)): raise ArithmeticError('duplicate frozen object rows')
    return sorted(objects),{'mode':'frozen_bzip2_base64_replay','source_b64_sha256':sha(path.read_bytes()),
                            'source_bz2_sha256':sha(packed),'source_csv_sha256':sha(raw.encode())}

def encode_source(objects,path:Path):
    s=io.StringIO(newline=''); w=csv.writer(s,lineterminator='\n')
    w.writerow(('a','b','c','d','mask')); w.writerows(objects)
    raw=s.getvalue().encode(); packed=bz2.compress(raw,9); enc=base64.b64encode(packed).decode()
    wrapped='\n'.join(enc[i:i+76] for i in range(0,len(enc),76))+'\n'
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(wrapped,encoding='ascii')
    return {'object_source_rows':len(objects),'object_source_csv_sha256':sha(raw),
            'object_source_bz2_sha256':sha(packed),'object_source_b64_sha256':sha(wrapped.encode()),
            'object_source_csv_bytes':len(raw),'object_source_bz2_bytes':len(packed)}

def anchor_regression(objects):
    s=num3.summarize({r for r in objects if r[3]<=ANCHOR})
    got={'object_count':s['distinct_physical_cuboids'],'counts':s['counts'],
         'object_key_sha256':s['object_key_sha256'],'object_key_mask_sha256':s['object_key_mask_sha256'],
         'vertex_ledger_sha256':s['graph']['vertex_ledger_sha256'],
         'edge_ledger_sha256':s['graph']['edge_ledger_sha256'],'max_degree':s['graph']['max_degree']}
    if got!=ANCHOR_LOCK: raise ArithmeticError(f'B100m anchor regression: {got}')
    return got

def prefix_regression(num5m,cumulative,rolling,shells):
    if num5m['decision']['STAGE14_NUM5']!='COMPLETE_FINITE_SCALING_ANOMALY_DIAGNOSTICS':
        raise ArithmeticError('num5 completion lock missing')
    got=[r for r in cumulative if r[0]<=ANCHOR]; want=num5m['cumulative_grid']
    if len(got)!=len(want): raise ArithmeticError('num5 cumulative prefix length')
    for a,b in zip(got,want):
        if a[:6]!=b[:6] or a[7]!=b[7] or not close(a[6],b[6]): raise ArithmeticError('num5 cumulative prefix')
    got=[r for r in rolling if r[1]<=ANCHOR]; want=num5m['rolling_power_fits_5point']
    if len(got)!=len(want): raise ArithmeticError('num5 rolling prefix length')
    for a,b in zip(got,want):
        if a[:2]!=b[:2] or not close(a[2],b[2]) or not close(a[3],b[3]): raise ArithmeticError('num5 rolling prefix')
    got=[r for r in shells if r[1]<=ANCHOR]; want=num5m['half_range_shells']
    if len(got)!=len(want): raise ArithmeticError('num5 shell prefix length')
    for a,b in zip(got,want):
        if a[:3]!=b[:3] or any(not close(x,y) for x,y in zip(a[3:],b[3:])): raise ArithmeticError('num5 shell prefix')
    return {'cumulative_rows':len(num5m['cumulative_grid']),'rolling_rows':len(num5m['rolling_power_fits_5point']),
            'half_range_shell_rows':len(num5m['half_range_shells']),'prefix_exactly_reproduced':True}

def diagnostics(objects,num5m):
    triples=[r for r in objects if r[4]==0b111]
    if triples: return None,triples
    states={r[:4]:num5.edge_states(r) for r in objects}
    cumulative=[]; graph=[]
    for B in range(STEP,BOUND+1,STEP):
        rows=[r for r in objects if r[3]<=B]; c=Counter(num5.direction(r[4]) for r in rows); N=c['a']+c['b']+c['c']
        g=num5.graph_at(rows)
        cumulative.append([B,N,c['a'],c['b'],c['c'],c['triple'],N/math.sqrt(B) if N else 0.0,g['max_degree']]); graph.append(g)
    rolling=[]
    for i in range(4,len(cumulative)):
        w=cumulative[i-4:i+1]; fit=num5.ols_power_fit([(r[0],r[1]) for r in w])
        rolling.append([w[0][0],w[-1][0],fit['alpha'],fit['r2']])
    shells=[]; prev=None
    for B in range(30_000_000,BOUND+1,STEP):
        lo=B//2; rows=[r for r in objects if lo<r[3]<=B]; c=Counter(num5.direction(r[4]) for r in rows); n=len(rows)
        local={str(p):Counter() for p in PRIMES}
        for r in rows:
            for p,s in states[r[:4]].items(): local[p][s]+=1
        vals=[None if prev is None else num5.tvd(prev[str(p)],local[str(p)]) for p in PRIMES]
        shells.append([lo,B,n,c['a']/n,c['b']/n,c['c']/n,*vals]); prev=local
    prefix=prefix_regression(num5m,cumulative,rolling,shells)
    ac=[r for r in cumulative if r[0]>ANCHOR]; ar=[r for r in rolling if r[1]>ANCHOR]; ash=[r for r in shells if r[1]>ANCHOR]
    degree=[]
    for prev,cur in zip(cumulative,cumulative[1:]):
        if cur[0]>ANCHOR and cur[7]>prev[7]: degree.append({'B':cur[0],'from':prev[7],'to':cur[7]})
    old_alpha=float(num5m['summary']['rolling_alpha_last']['alpha']); new_alpha=float(rolling[-1][2]); alpha_delta=new_alpha-old_alpha
    old_sqrt=[float(r[6]) for r in num5m['cumulative_grid']]; old_min=min(old_sqrt); old_max=max(old_sqrt); new_sqrt=float(cumulative[-1][6])
    finalN=cumulative[-1][1]; finalshare={q:cumulative[-1][i]/finalN for q,i in zip('abc',(2,3,4))}
    dmax={q:{'max_abs_deviation':0.0,'at_B':None} for q in 'abc'}
    for s in ash:
        for q,val in zip('abc',s[3:6]):
            d=abs(val-finalshare[q])
            if d>dmax[q]['max_abs_deviation']: dmax[q]={'max_abs_deviation':d,'at_B':s[1]}
    lmax={str(p):{'max_adjacent_shell_tvd':0.0,'at_B':None} for p in PRIMES}
    for s in ash:
        for j,p in enumerate(PRIMES):
            val=s[6+j]
            if val is not None and val>lmax[str(p)]['max_adjacent_shell_tvd']: lmax[str(p)]={'max_adjacent_shell_tvd':val,'at_B':s[1]}
    thresholds={'latest_alpha_abs_change_from_num5':0.03,
                'direction_new_shell_abs_share_deviation':float(num5m['thresholds']['direction_shell_abs_share_deviation']),
                'local_adjacent_shell_tvd':float(num5m['thresholds']['local_adjacent_shell_tvd']),
                'sqrt_band_decisive_relative_margin':0.05,'graph_new_max_degree_increase':1}
    reasons=[]
    if abs(alpha_delta)>=thresholds['latest_alpha_abs_change_from_num5']: reasons.append('LATEST_ROLLING_ALPHA_SHIFT')
    if new_sqrt<old_min*0.95 or new_sqrt>old_max*1.05: reasons.append('N2_OVER_SQRT_B_DECISIVE_HISTORICAL_BAND_EXIT')
    if any(v['max_abs_deviation']>=thresholds['direction_new_shell_abs_share_deviation'] for v in dmax.values()): reasons.append('NEW_SHELL_DIRECTION_DRIFT')
    if any(v['max_adjacent_shell_tvd']>=thresholds['local_adjacent_shell_tvd'] for v in lmax.values()): reasons.append('LOCAL_FINGERPRINT_INSTABILITY')
    if degree: reasons.append('NEW_GRAPH_MAX_DEGREE')
    summary={'anchor_latest_alpha':old_alpha,'latest_alpha':new_alpha,'latest_alpha_change_from_num5':alpha_delta,
             'anchor_N2_over_sqrt_B_band':{'min':old_min,'max':old_max},'latest_N2_over_sqrt_B':new_sqrt,
             'latest_N2_over_sqrt_B_fractional_change_from_B100m':new_sqrt/float(num5m['summary']['N2_over_sqrt_B_last_B100m'])-1,
             'new_shell_direction_max_deviation_from_B150m_cumulative_share':dmax,'new_shell_local_tvd_max':lmax,
             'new_graph_max_degree_jumps':degree,'material_change':bool(reasons),'material_change_reasons':reasons}
    return {'prefix_regression':prefix,'appended_cumulative_grid':ac,'appended_rolling_power_fits_5point':ar,
            'appended_half_range_shells':ash,'summary':summary,'thresholds':thresholds},[]

def main():
    ap=argparse.ArgumentParser(); src=ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--chunk-dir',type=Path); src.add_argument('--objects-b64',type=Path)
    ap.add_argument('--num3-aggregate',type=Path); ap.add_argument('--num5-manifest',type=Path,required=True)
    ap.add_argument('--manifest-out',type=Path,required=True); ap.add_argument('--objects-b64-out',type=Path)
    a=ap.parse_args()
    if a.chunk_dir: objects,generation=read_chunks(a.chunk_dir); bound=generation['bound']
    else: objects,generation=decode_source(a.objects_b64); bound=BOUND
    if bound!=BOUND: raise ArithmeticError(f'num6 freezes B={BOUND}, got {bound}')
    full=num3.summarize(set(objects)); anchor=anchor_regression(objects)
    if a.num3_aggregate:
        n3=json.loads(a.num3_aggregate.read_text())
        if n3['extended_census']!=full or not n3['num1_regression']['all_four_sha256_match']: raise ArithmeticError('num3 aggregate cross-check')
        num3check={'checked':True,'exact_summary_match':True,'num1_regression_match':True}
    else: num3check={'checked':False}
    num5m=json.loads(a.num5_manifest.read_text()); diag,triples=diagnostics(objects,num5m)
    if a.objects_b64_out: source=encode_source(objects,a.objects_b64_out)
    else:
        tmp=Path(str(a.manifest_out)+'.tmp.b64'); source=encode_source(objects,tmp)
        if source['object_source_b64_sha256']!=sha(a.objects_b64.read_bytes()): raise ArithmeticError('source serialization mismatch')
        tmp.unlink()
    reasons=['PERFECT_CUBOID_EMERGENCY'] if triples else diag['summary']['material_change_reasons']
    handoff=None if not reasons else {'OBSERVATION_ID':'stage14-num6-b150m-material-change','CUTOFF_RANGE':'100000000<B<=150000000',
      'EXACT_OR_HEURISTIC':'EXACT + DERIVED_EXACT + FINITE_HEURISTIC_ONLY','OBJECT_COUNT':full['distinct_physical_cuboids'],
      'AFFECTED_TRACKS':'14-4 | 14-s | 14-t | 14-e','OBSERVATION':';'.join(reasons),
      'REPRODUCER':'stages/stage14/scripts/14-num6/rolling_observatory.py','THEOREM_CLAIM':False}
    manifest={'metadata':{'stage':'14-num6','classification':'ROLLING_EXACT_CENSUS_APPEND_WITH_FINITE_DIAGNOSTICS','anchor_bound':ANCHOR,
      'bound':BOUND,'grid_step':STEP,'append_only':True,'finite_diagnostic_only':True,'asymptotic_claim':False},
      'generation':generation,'object_source':source,'B100m_anchor_regression':anchor,'num3_aggregate_crosscheck':num3check,
      'exact_cutoff_B150m':full,'diagnostic_append':diag,'handoff':handoff,
      'decision':{'STAGE14_NUM6':'PAUSED_PERFECT_CUBOID_EMERGENCY_PROTOCOL' if triples else 'COMPLETE_ROLLING_EXACT_B150M_APPEND',
       'HISTORICAL_B100M_PREFIX_UNCHANGED':True,'B150M_EXACT_CENSUS_FROZEN':True,'APPEND_ONLY_HISTORY':True,
       'MATERIAL_CHANGE_HANDOFF':bool(handoff),'PERFECT_CUBOID_EMERGENCY':bool(triples),'FINITE_DIAGNOSTIC_ONLY':True,
       'ASYMPTOTIC_CLAIM':False,'PERFECT_CUBOID_EXISTENCE_CLAIM':False,'PERFECT_CUBOID_NONEXISTENCE_CLAIM':False,
       'NEXT':'independent perfect-cuboid candidate reproduction' if triples else 'Stage14-num7 rolling observatory / next materially larger exact cutoff'}}
    a.manifest_out.parent.mkdir(parents=True,exist_ok=True); a.manifest_out.write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'exact_cutoff_B150m':full,'diagnostic_summary':None if diag is None else diag['summary'],'handoff':handoff,'decision':manifest['decision']},indent=2,sort_keys=True))

if __name__=='__main__': main()
