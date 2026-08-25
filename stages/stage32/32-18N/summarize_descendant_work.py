#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,pathlib,statistics


def stats(xs):
    mean=sum(xs)/len(xs) if xs else 0.0
    sd=statistics.pstdev(xs) if xs else 0.0
    return {'mean':mean,'stdev':sd,'cv':sd/mean if mean else 0.0,'max':max(xs) if xs else 0,'max_to_mean':max(xs)/mean if mean else 0.0}


def rank(xs,r):
    order=sorted(range(len(xs)),key=lambda i:(-xs[i],i))
    return order.index(r)+1


def top(xs,n=20):
    order=sorted(range(len(xs)),key=lambda i:(-xs[i],i))
    return [{'residue':i,'value':xs[i]} for i in order[:n]]


def aggregate(xs,mod):
    out=[0]*mod
    for i,x in enumerate(xs): out[i%mod]+=x
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=pathlib.Path,required=True)
    ap.add_argument('--runtime',type=pathlib.Path,required=True)
    ap.add_argument('--tag',required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    args=ap.parse_args()
    d=json.loads(args.input.read_text())
    assert d['schema']=='STAGE32_18N_D16_EXACT_DESCENDANT_WORK_PROFILE_V1'
    assert d['status']=='COMPLETE' and d['descendant_work_profile_only'] is True
    assert d['DESCENDANT_WORK_PROFILE_COMPLETE'] is True
    assert d['FULL_BOUND_TRAVERSAL_COMPLETE'] is False
    keys=['descendant_nodes_by_residue','descendant_trials_by_residue','descendant_constraint_prunes_by_residue','descendant_symmetry_prunes_by_residue','descendant_probe_prefixes_by_residue']
    arrays={k:[int(x) for x in d[k]] for k in keys}
    assert all(len(v)==1024 for v in arrays.values())
    metrics={}
    for k,xs in arrays.items():
        metrics[k]={'stats':stats(xs),'rank26':rank(xs,26),'value26':xs[26],'top20':top(xs)}
    hierarchy={}
    for mod in (64,256,1024):
        hierarchy[str(mod)]={}
        for k,xs in arrays.items():
            ys=aggregate(xs,mod)
            target=26%mod
            hierarchy[str(mod)][k]={'stats':stats(ys),'rank_target26':rank(ys,target),'value_target26':ys[target],'top20':top(ys)}
    out={
      'schema':'STAGE32_18N_DESCENDANT_WORK_COMPACT_V1','tag':args.tag,
      'bound':d['bound'],'parent_coordinate':d['parent_coordinate'],'probe_coordinate':d['probe_coordinate'],'parent_modulus':d['parent_modulus'],
      'parent_prefixes':d['split_prefixes_seen'],'global_nodes_to_probe':d['nodes'],'global_trials_to_probe':d['coordinate_trials'],
      'runtime_seconds':float(args.runtime.read_text().strip()),'metrics':metrics,'hierarchical_modulus_views':hierarchy,
      'NUMERICAL_CREDIT':False,'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False
    }
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'tag':args.tag,'bound':d['bound'],'probe':d['probe_coordinate'],'nodes_rank26':metrics['descendant_nodes_by_residue']['rank26'],'trials_rank26':metrics['descendant_trials_by_residue']['rank26'],'probe_prefix_rank26':metrics['descendant_probe_prefixes_by_residue']['rank26'],'runtime_seconds':out['runtime_seconds']},sort_keys=True))

if __name__=='__main__': main()
