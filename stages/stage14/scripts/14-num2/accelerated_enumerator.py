#!/usr/bin/env python3
"""Stage14-num2 exact accelerated production enumerator.

The mathematical population is unchanged from num1.  The acceleration is purely
engineering:

* retain the Euclid scale k with every face triple, so primitiveness of a glue
  x^2+y^2=p^2, p^2+z^2=d^2 is tested as gcd(k,z)=1 before canonical sorting;
* build an exact set of Pythagorean leg pairs once, so the second integral face
  is detected by integer set membership instead of millions of square-root
  tests;
* validate all three face flags only after the two-face gate has passed;
* expose disjoint space-diagonal shells and deterministic p-mod-N chunks so a
  single generated index can feed incremental and parallel runs reproducibly.

No asymptotic claim is made.  The B=2,000,000 num1 object/graph hashes are the
hard regression contract.
"""
from __future__ import annotations

import argparse
import json
import time
from collections import defaultdict
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

DEFAULT_B = 2_000_000
ROOT = Path(__file__).resolve().parents[4]
NUM1_MANIFEST = ROOT / "stages/stage14/data/14-num1/baseline_manifest.json"
DEFAULT_OUTPUT = ROOT / "stages/stage14/data/14-num2/benchmark_after.json"
CUTS = (1_000,2_000,5_000,10_000,20_000,50_000,100_000,200_000,500_000,1_000_000,2_000_000)
EXPECTED = {
    1_000:(2,0,0), 2_000:(2,2,1), 5_000:(6,6,3), 10_000:(9,11,5),
    20_000:(16,16,10), 50_000:(24,24,14), 100_000:(33,33,23),
    200_000:(42,50,24), 500_000:(70,78,40), 1_000_000:(98,101,56),
    2_000_000:(142,134,80),
}
SHELLS = ((0,200_000),(200_000,500_000),(500_000,1_000_000),(1_000_000,2_000_000))
CHUNK_COUNT = 8


def pair_key(a:int,b:int,radix:int)->int:
    if a>b:
        a,b=b,a
    return a*radix+b


def build_index(bound:int):
    """Build exact hypotenuse/leg indexes plus a Pythagorean-leg-pair set.

    hyp[p] entries are (x,y,k) with gcd(x,y)=k.  This scale is the key num2
    optimization because gcd(x,y,z)=1 iff gcd(k,z)=1.
    """
    hyp=defaultdict(list)
    leg=defaultdict(list)
    mate_pairs=set()
    radix=bound+1
    triples=0
    m=2
    while m*m+1<=bound:
        for n in range(1,m):
            if ((m-n)&1)==0 or gcd(m,n)!=1:
                continue
            u=m*m-n*n; v=2*m*n; w=m*m+n*n
            if w>bound:
                continue
            if u>v:
                u,v=v,u
            k=1
            while k*w<=bound:
                x=k*u; y=k*v; h=k*w
                hyp[h].append((x,y,k))
                leg[x].append((y,h)); leg[y].append((x,h))
                mate_pairs.add(pair_key(x,y,radix))
                triples+=1; k+=1
        m+=1
    return {
        "bound":bound, "radix":radix, "hyp":hyp, "leg":leg, "mate_pairs":mate_pairs,
        "profile":{
            "integer_pythagorean_triples":triples,
            "hypotenuse_index_keys":len(hyp),
            "hypotenuse_index_entries":sum(map(len,hyp.values())),
            "leg_index_keys":len(leg),
            "leg_index_entries":sum(map(len,leg.values())),
            "mate_pair_keys":len(mate_pairs),
        },
    }


def face_mask(a:int,b:int,c:int):
    mask=0; ds=[]
    for i,v in enumerate((a*a+b*b,a*a+c*c,b*b+c*c)):
        r=isqrt(v); ok=r*r==v
        if ok: mask|=1<<i
        ds.append(r if ok else 0)
    return mask,tuple(ds)


def primitive_face(S:int,X:int,H:int):
    g=gcd(S,X)
    assert H%g==0
    return S//g,X//g,H//g


def object_edges(rec):
    a,b,c,_,mask=rec
    _,(dab,dac,dbc)=face_mask(a,b,c)
    out=[]
    if mask&1 and mask&2:
        out.append(tuple(sorted((primitive_face(a,b,dab),primitive_face(a,c,dac)))))
    if mask&1 and mask&4:
        out.append(tuple(sorted((primitive_face(b,a,dab),primitive_face(b,c,dbc)))))
    if mask&2 and mask&4:
        out.append(tuple(sorted((primitive_face(c,a,dac),primitive_face(c,b,dbc)))))
    return out


def digest_rows(rows):
    payload="".join(",".join(map(str,row))+"\n" for row in sorted(rows))
    return sha256(payload.encode("ascii")).hexdigest()


def enumerate_fast(index, low_d=0, high_d=None, chunk_count=1, chunk_index=None, collect_partitions=False):
    bound=index["bound"]
    if high_d is None: high_d=bound
    hyp=index["hyp"]; leg=index["leg"]; mates=index["mate_pairs"]; radix=index["radix"]
    objects=set()
    chunk_sets=[set() for _ in range(CHUNK_COUNT)] if collect_partitions else None
    shell_sets=[set() for _ in SHELLS] if collect_partitions else None
    pstats={
        "candidate_glues":0,
        "early_nonprimitive_rejects_before_sort":0,
        "second_face_pair_membership_lookups":0,
        "reject_less_than_two_integral_faces":0,
        "sorts_after_two_face_gate":0,
        "face_mask_validation_tests":0,
        "retained_generation_records":0,
        "duplicate_two_plus_records_suppressed":0,
    }
    for p,faces in hyp.items():
        if chunk_index is not None and p%chunk_count!=chunk_index:
            continue
        exts=leg.get(p)
        if not exts:
            continue
        event_chunk=p%CHUNK_COUNT
        for x,y,scale in faces:
            for z,d in exts:
                if not (low_d < d <= high_d):
                    continue
                pstats["candidate_glues"]+=1
                if gcd(scale,z)!=1:
                    pstats["early_nonprimitive_rejects_before_sort"]+=1
                    continue
                # The base face x-y is already integral.  Any second face is
                # equivalent to x-z or y-z appearing in the exact Pythagorean
                # leg-pair set because its diagonal is < d <= bound.
                kxz=pair_key(x,z,radix); kyz=pair_key(y,z,radix)
                pstats["second_face_pair_membership_lookups"]+=2
                if kxz not in mates and kyz not in mates:
                    pstats["reject_less_than_two_integral_faces"]+=1
                    continue
                pstats["sorts_after_two_face_gate"]+=1
                a,b,c=sorted((x,y,z))
                if not (0<a<b<c):
                    continue
                mask,_=face_mask(a,b,c)
                pstats["face_mask_validation_tests"]+=1
                if mask.bit_count()<2:
                    raise ArithmeticError("exact membership gate disagrees with face-mask validation")
                rec=(a,b,c,d,mask)
                pstats["retained_generation_records"]+=1
                if rec in objects:
                    pstats["duplicate_two_plus_records_suppressed"]+=1
                objects.add(rec)
                if collect_partitions:
                    chunk_sets[event_chunk].add(rec)
                    for i,(lo,hi) in enumerate(SHELLS):
                        if lo < d <= hi:
                            shell_sets[i].add(rec); break
    return objects,pstats,chunk_sets,shell_sets


def summarize(objects):
    counts={"a":0,"b":0,"c":0,"total":0,"triple":0}
    edges=set(); vertices=set(); degree=defaultdict(int)
    for rec in sorted(objects):
        a,b,c,d,mask=rec
        assert 0<a<b<c and gcd(a,gcd(b,c))==1 and a*a+b*b+c*c==d*d
        check,_=face_mask(a,b,c); assert check==mask and mask.bit_count()>=2
        if mask==0b011: counts["a"]+=1; counts["total"]+=1
        elif mask==0b101: counts["b"]+=1; counts["total"]+=1
        elif mask==0b110: counts["c"]+=1; counts["total"]+=1
        elif mask==0b111: counts["triple"]+=1
        else: raise ArithmeticError(mask)
        for e in object_edges(rec):
            edges.add(e); u,v=e; vertices.add(u);vertices.add(v);degree[u]+=1;degree[v]+=1
    keys=[r[:4] for r in objects]
    graph={
        "raw_pair_edges":len(edges),
        "active_oriented_face_vertices":len(vertices),
        "max_degree":max(degree.values(),default=0),
        "vertex_ledger_sha256":digest_rows(vertices),
        "edge_ledger_sha256":digest_rows((u+v) for u,v in edges),
    }
    return {
        "counts":counts,
        "object_key_sha256":digest_rows(keys),
        "object_key_mask_sha256":digest_rows(objects),
        "graph":graph,
    }


def cutoff_rows(objects):
    rows=[]
    for B in CUTS:
        subset={r for r in objects if r[3]<=B}
        s=summarize(subset)
        want=EXPECTED[B]
        got=(s["counts"]["a"],s["counts"]["b"],s["counts"]["c"])
        if got!=want or s["counts"]["triple"]!=0:
            raise ArithmeticError(f"cutoff mismatch B={B}: got={got}, T={s['counts']['triple']}, want={want}")
        rows.append({"B":B,"a":got[0],"b":got[1],"c":got[2],"N2":sum(got),"T":0})
    return rows


def load_num1():
    return json.loads(NUM1_MANIFEST.read_text(encoding="utf-8"))


def build_report(bound:int):
    if bound!=DEFAULT_B:
        raise SystemExit("num2 validation stage is frozen at B=2,000,000; larger cutoffs begin at num3")
    num1=load_num1()
    t0=time.perf_counter(); index=build_index(bound); index_seconds=time.perf_counter()-t0
    t1=time.perf_counter(); objects,prof,chunks,shells=enumerate_fast(index,collect_partitions=True); kernel_seconds=time.perf_counter()-t1
    summary=summarize(objects)

    expected_hash=num1["hashes"]
    assert summary["object_key_sha256"]==expected_hash["object_key_sha256"]
    assert summary["object_key_mask_sha256"]==expected_hash["object_key_mask_sha256"]
    assert summary["graph"]["vertex_ledger_sha256"]==expected_hash["vertex_ledger_sha256"]
    assert summary["graph"]["edge_ledger_sha256"]==expected_hash["edge_ledger_sha256"]
    assert summary["counts"]==num1["counts"]
    assert {k:summary["graph"][k] for k in ("raw_pair_edges","active_oriented_face_vertices","max_degree")}==num1["graph"]

    chunk_union=set().union(*chunks)
    shell_union=set().union(*shells)
    assert chunk_union==objects
    assert shell_union==objects

    rows=cutoff_rows(objects)
    before=num1["deterministic_workload_profile"]["route_A_hypotenuse_glue"]
    face_test_reduction=1-prof["face_mask_validation_tests"]/before["face_mask_tests"]
    sort_avoidance=1-prof["sorts_after_two_face_gate"]/before["candidate_glues"]

    return {
        "metadata":{
            "stage":"14-num2",
            "bound":bound,
            "classification":"FINITE_ENGINEERING_VALIDATION",
            "method":"early scale-gcd primitive filter + exact Pythagorean mate-pair membership gate",
        },
        "num1_regression":{
            "all_four_sha256_match":True,
            "hashes":expected_hash,
            "counts_match":True,
            "graph_match":True,
            "all_11_cutoffs_match":True,
            "cutoff_rows":rows,
        },
        "index_profile":index["profile"],
        "optimized_kernel_profile":prof,
        "engineering_reduction":{
            "num1_candidate_glues":before["candidate_glues"],
            "num1_face_mask_tests":before["face_mask_tests"],
            "num2_face_mask_validation_tests":prof["face_mask_validation_tests"],
            "face_mask_test_fraction_removed":face_test_reduction,
            "sort_fraction_removed_before_two_face_gate":sort_avoidance,
            "note":"candidate-glue volume is unchanged in num2; expensive canonical sorting and full face-square validation are postponed until after exact arithmetic gates",
        },
        "incremental_shell_architecture":{
            "shells":[{"low_exclusive":lo,"high_inclusive":hi,"objects":len(s)} for (lo,hi),s in zip(SHELLS,shells)],
            "union_matches_full_ledger":True,
            "single_index_reused_across_shells":True,
        },
        "deterministic_chunk_architecture":{
            "partition":"shared face hypotenuse p modulo 8",
            "chunks":CHUNK_COUNT,
            "chunk_object_counts":[len(s) for s in chunks],
            "union_matches_full_ledger":True,
            "overlap_allowed_before_global_canonical_dedup":True,
        },
        "environment_specific_timing":{
            "index_build_seconds":index_seconds,
            "optimized_kernel_seconds":kernel_seconds,
            "total_python_seconds":index_seconds+kernel_seconds,
            "classification":"ENVIRONMENT_SPECIFIC_ENGINEERING_SAMPLE",
        },
        "decision":{
            "STAGE14_NUM2":"COMPLETE_EXACT_ENUMERATOR_ACCELERATION",
            "BASELINE_LEDGER_UNCHANGED":True,
            "ALL_11_FROZEN_CUTOFFS_UNCHANGED":True,
            "INCREMENTAL_CUTOFF_ARCHITECTURE":True,
            "PARALLEL_CHUNK_REPRODUCIBILITY":True,
            "FINITE_DIAGNOSTIC_ONLY":True,
            "ASYMPTOTIC_CLAIM":False,
            "NEXT":"Stage14-num3 extended exact census",
        },
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bound",type=int,default=DEFAULT_B)
    ap.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    args=ap.parse_args()
    report=build_report(args.bound)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({
        "regression":report["num1_regression"],
        "optimized_kernel_profile":report["optimized_kernel_profile"],
        "engineering_reduction":report["engineering_reduction"],
        "timing":report["environment_specific_timing"],
        "decision":report["decision"],
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
