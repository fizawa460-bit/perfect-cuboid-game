#!/usr/bin/env python3
from __future__ import annotations
import argparse, heapq, json, pathlib


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--p50',type=pathlib.Path,required=True)
    ap.add_argument('--p48',type=pathlib.Path,required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    args=ap.parse_args()
    a=json.loads(args.p50.read_text()); b=json.loads(args.p48.read_text())
    for d,probe in ((a,50),(b,48)):
        assert d['schema']=='STAGE32_18N_D16_EXACT_DESCENDANT_WORK_PROFILE_V1'
        assert d['status']=='COMPLETE' and d['bound']==14
        assert d['parent_coordinate']==54 and d['parent_modulus']==1024 and d['probe_coordinate']==probe
        assert d['DESCENDANT_WORK_PROFILE_COMPLETE'] is True
        assert d['FULL_BOUND_TRAVERSAL_COMPLETE'] is False
    p50=[int(x) for x in a['descendant_probe_prefixes_by_residue']]
    p48=[int(x) for x in b['descendant_probe_prefixes_by_residue']]
    assert len(p50)==len(p48)==1024
    m50=sum(p50)/1024; m48=sum(p48)/1024
    score=[max(p50[i]/m50,p48[i]/m48) for i in range(1024)]
    order=sorted(range(1024),key=lambda i:(-score[i],i))
    hot=order[:64]; mid=order[64:256]; low=order[256:]
    packets=[]
    for r in hot: packets.append({'tier':'hot-single','residues':[r]})
    for j in range(96): packets.append({'tier':'mid-pair','residues':[mid[j],mid[-1-j]]})
    heap=[(0.0,j,[]) for j in range(96)]; heapq.heapify(heap)
    for r in low:
        load,j,arr=heapq.heappop(heap)
        arr=arr+[r]
        heapq.heappush(heap,(load+score[r],j,arr))
    for _,_,arr in sorted(heap,key=lambda x:x[1]):
        assert len(arr)==8
        packets.append({'tier':'low-octet','residues':arr})
    assert len(packets)==256
    flat=[r for p in packets for r in p['residues']]
    assert sorted(flat)==list(range(1024)) and len(set(flat))==1024
    for pid,p in enumerate(packets):
        p['packet_id']=pid; p['residue_count']=len(p['residues'])
        p['hybrid_risk_sum']=round(sum(score[r] for r in p['residues']),12)
        p['p50_probe_prefix_sum']=sum(p50[r] for r in p['residues'])
        p['p48_probe_prefix_sum']=sum(p48[r] for r in p['residues'])
        p['residue_details']=[{'residue':r,'p50_probe_prefixes':p50[r],'p48_probe_prefixes':p48[r],'hybrid_risk':round(score[r],12)} for r in p['residues']]
    hist26=next(p['packet_id'] for p in packets if 26 in p['residues'])
    mid_ids=[p['packet_id'] for p in packets if p['tier']=='mid-pair']
    low_ids=[p['packet_id'] for p in packets if p['tier']=='low-octet']
    mid_worst=max(mid_ids,key=lambda i:packets[i]['hybrid_risk_sum'])
    low_sorted=sorted(low_ids,key=lambda i:packets[i]['hybrid_risk_sum'])
    low_worst=low_sorted[-1]; low_med=low_sorted[len(low_sorted)//2]
    pilot=[0,hist26,63,mid_worst,low_worst,low_med]
    assert pilot==[0,15,63,64,173,210], pilot
    doc={
      'schema':'STAGE32_18O_D16_B14_PACKET_MANIFEST_V1','bound':14,'parent_coordinate':54,'parent_modulus':1024,
      'risk_model':'max(p50_probe_prefixes/mean_p50, p48_probe_prefixes/mean_p48)',
      'p50_mean':m50,'p48_mean':m48,
      'partition_policy':{
        'hot_singletons':'hybrid ranks 1..64',
        'mid_pairs':'hybrid ranks 65..256 paired highest-with-lowest within tier',
        'low_octets':'hybrid ranks 257..1024 assigned by capacity-8 LPT over hybrid risk'
      },
      'packet_count':256,'tier_counts':{'hot-single':64,'mid-pair':96,'low-octet':96},
      'coverage_exact':True,'residues_exactly_once':True,
      'historical_residue26_packet_id':hist26,'historical_residue26_hybrid_rank':order.index(26)+1,
      'pilot_packet_ids':pilot,
      'pilot_roles':{
        '0':'highest hybrid-risk singleton','15':'historical b12 pathological residue singleton','63':'hot-single boundary',
        '64':'highest-risk mid pair','173':'highest-risk low octet','210':'median-risk low octet'
      },
      'packets':packets,
      'D16_B14_NUMERICAL_CREDIT':False,'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False
    }
    args.output.write_text(json.dumps(doc,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'packet_count':256,'pilot_packet_ids':pilot,'historical26_packet':hist26,'historical26_hybrid_rank':order.index(26)+1,'packet0':packets[0]['residues'],'packet15':packets[15]['residues'],'packet63':packets[63]['residues'],'packet64':packets[64]['residues'],'packet173':packets[173]['residues'],'packet210':packets[210]['residues']},sort_keys=True))

if __name__=='__main__': main()
