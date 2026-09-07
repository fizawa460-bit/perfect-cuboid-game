#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
AO = HERE / "post1648ao-special-fibre-hurwitz-budget.json"
sys.path.insert(0, str(HERE))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402


def load_retained(path: Path, name: str) -> dict:
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod.load()


def subset_xor(bits, mask):
    x=0; i=0
    while mask:
        if mask&1: x ^= bits[i]
        mask >>= 1; i += 1
    return x


def main():
    v6=json.loads(V6.read_text()); ao=json.loads(AO.read_text())
    assert v6['canonical_sha256_without_this_field']=='d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8'
    assert ao['canonical_sha256_without_this_field']=='39e217c7223732b1834b7e9b96b4361807227f823a5624842a97eddf71390378'
    marking=load_retained(ST33/'stage32_picard_marking_retained.py','s32_av_marking2')
    bundle=load_retained(ST33/'picard_base_rows_retained.py','s32_av_bundle2')
    adapter=HperpIntegralPairingAdapter.from_retained(marking,bundle)
    coords=adapter.class_coordinates_in_retained_basis
    gram=Matrix(bundle['picard_gram_64x64'])
    full=coords*gram*coords.T
    if full.shape!=(140,140): raise ValueError('full intersection shape')

    # AM source-lock: labels 1..32 are the rational normal orbit; 93..140 are exceptional.
    R=list(range(32)); E=list(range(92,140))
    inc=[]; bits=[]
    for r in R:
        row=[]; bit=0
        for j,e in enumerate(E):
            val=int(full[r,e])
            if val not in (0,1): raise ValueError(f'unexpected rational-exceptional incidence {r+1},{e+1}:{val}')
            if val:
                row.append(e); bit |= 1<<j
        inc.append(row); bits.append(bit)
    incidence_counts=[len(x) for x in inc]

    # Meet-in-middle weight-8 parity-zero subsets. Coordinate hyperplane groups must
    # have each exceptional incidence count 0 or 2 (two local branches through a node).
    left=bits[:16]; right=bits[16:]
    L=defaultdict(list); RR=defaultdict(list)
    for k in range(0,9):
        for comb in itertools.combinations(range(16),k):
            m=sum(1<<i for i in comb); x=0
            for i in comb: x ^= left[i]
            L[(k,x)].append(m)
        for comb in itertools.combinations(range(16),k):
            m=sum(1<<i for i in comb); x=0
            for i in comb: x ^= right[i]
            RR[(k,x)].append(m)

    groups=[]; seen=set()
    for (k,x), lms in L.items():
        rms=RR.get((8-k,x),[])
        for lm in lms:
            for rm in rms:
                labels=[i for i in range(16) if (lm>>i)&1] + [16+i for i in range(16) if (rm>>i)&1]
                key=tuple(labels)
                if key in seen: continue
                counts=[0]*48
                for r in labels:
                    for e in inc[r]: counts[e-92]+=1
                if set(counts).issubset({0,2}) and counts.count(2)==24:
                    # strict transforms in one coordinate hyperplane should be pairwise disjoint
                    pairints=[int(full[a,b]) for a,b in itertools.combinations(labels,2)]
                    if any(x!=0 for x in pairints):
                        continue
                    seen.add(key)
                    selected=[92+j for j,c in enumerate(counts) if c==2]
                    groups.append((labels,selected))
    groups.sort()

    pairings=[int(x) for x in v6['witness']['all140_pairings']]
    out_groups=[]
    for labels,selected in groups:
        nsum=sum(pairings[i] for i in labels)
        esum=sum(pairings[i] for i in selected)
        out_groups.append({
          'rational_labels_1based':[i+1 for i in labels],
          'exceptional_labels_1based':[i+1 for i in selected],
          'rational_C_intersection_sum':nsum,
          'exceptional_mass_sum':esum,
          'canonical_hyperplane_total':nsum+esum,
          'node_count':len(selected),
        })

    partition=Counter(i for g,_ in groups for i in g)
    ecover=Counter(i for _,s in groups for i in s)
    out={
      'mode':'SCRATCH_POST1648AV_CANONICAL_COORDINATE_HYPERPLANE_RECOVERY',
      'parents':{'AO_canonical':ao['canonical_sha256_without_this_field'],'V6_canonical':v6['canonical_sha256_without_this_field']},
      'retained_incidence':{
        'rational_labels_1based':[i+1 for i in R],
        'exceptional_labels_1based':[i+1 for i in E],
        'rational_exceptional_incidence_count_profile':dict(sorted(Counter(incidence_counts).items())),
      },
      'coordinate_W1_W2_W3_C_recovery':{
        'candidate_group_count':len(groups),
        'groups':out_groups,
        'rational_partition_exact':len(groups)==4 and partition==Counter({i:1 for i in R}),
        'each_exceptional_in_exactly_two_coordinate_hyperplanes':len(groups)==4 and ecover==Counter({i:2 for i in E}),
        'semantic_identification':'unordered {W1=0,W2=0,W3=0,C=0}; individual names not assigned',
      },
      'AO_pressure':{
        'minimum_node_preimages':int(ao['exact_results']['minimum_total_normalization_preimages_over_met_surface_nodes']),
        'canonical_degree':186,
      },
      'firewalls':{'scratch_only':True,'retained_payload_emitted':False,'v6_carrier_excluded':False,'Q602_excluded':False,'O210_excluded':False},
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
