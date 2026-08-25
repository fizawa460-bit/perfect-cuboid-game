#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, pathlib, statistics


def percentile(xs, q):
    if not xs:
        return 0
    ys=sorted(xs)
    k=(len(ys)-1)*q
    a=math.floor(k); b=math.ceil(k)
    if a==b: return ys[a]
    return ys[a]*(b-k)+ys[b]*(k-a)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', type=pathlib.Path, required=True)
    ap.add_argument('--runtime', type=pathlib.Path, required=True)
    ap.add_argument('--tag', required=True)
    ap.add_argument('--output', type=pathlib.Path, required=True)
    args=ap.parse_args()
    d=json.loads(args.input.read_text())
    counts=[int(x) for x in d['frontier_counts_by_residue']]
    assert d['schema']=='STAGE32_18M_D16_EXACT_FRONTIER_PROFILE_V1'
    assert d['status']=='COMPLETE'
    assert d['frontier_only'] is True
    assert d['FRONTIER_PREFIX_ENUMERATION_COMPLETE'] is True
    assert d['FULL_BOUND_TRAVERSAL_COMPLETE'] is False
    assert d['TRAVERSAL_COMPLETENESS_CERTIFICATE'] is False
    assert sum(counts)==int(d['frontier_total_prefixes'])==int(d['split_prefixes_seen'])
    mean=(sum(counts)/len(counts)) if counts else 0.0
    sd=statistics.pstdev(counts) if counts else 0.0
    ranked=sorted(range(len(counts)), key=lambda i:(-counts[i],i))
    hot26_rank=(ranked.index(26)+1) if len(counts)>26 else None
    out={
      'schema':'STAGE32_18M_FRONTIER_COMPACT_PROFILE_V1',
      'tag':args.tag,
      'bound':d['bound'],
      'frontier_coordinate':d['frontier_coordinate'],
      'frontier_modulus':d['frontier_modulus'],
      'frontier_total_prefixes':d['frontier_total_prefixes'],
      'nonzero_residue_buckets':sum(x>0 for x in counts),
      'mean_prefixes_per_bucket':mean,
      'stdev_prefixes_per_bucket':sd,
      'coefficient_of_variation':(sd/mean if mean else 0.0),
      'max_prefixes_in_bucket':max(counts) if counts else 0,
      'max_to_mean_ratio':((max(counts)/mean) if mean else 0.0),
      'p50':percentile(counts,.50),'p90':percentile(counts,.90),'p95':percentile(counts,.95),'p99':percentile(counts,.99),
      'top20_residues':[{'residue':i,'prefixes':counts[i]} for i in ranked[:20]],
      'historical_hot_residue_26_prefixes':counts[26] if len(counts)>26 else None,
      'historical_hot_residue_26_rank':hot26_rank,
      'nodes_to_frontier':d['nodes'],
      'coordinate_trials_to_frontier':d['coordinate_trials'],
      'exact_constraint_prunes_to_frontier':d['exact_constraint_prunes'],
      'exact_symmetry_prunes_to_frontier':d['exact_symmetry_prunes'],
      'runtime_seconds':float(args.runtime.read_text().strip()),
      'NUMERICAL_CREDIT':False,
      'FULL_D16_G0_ROW_COMPLETE':False,
      'THEOREM_CREDIT':False,
      'RECEIVER_CREDIT':False,
    }
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__': main()
