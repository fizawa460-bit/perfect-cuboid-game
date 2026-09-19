#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PARENT = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_base4_normalmass_bounded_panel.py"
PARENT_BLOB = "29114c0cd8a2c604d24b2a9ad3418fc2b5200171"
CENSUS = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-STATIC7-KEY-CENSUS-RECEIPT.json"
CENSUS_CANON = "b975417fe28296a53f7877e9a02ce230a8852dfbc26fe29c428aeddff209719c"

DEGREE = 8
E = 8
NORMAL_COUNT = 92
TOTAL_KNOWN = 140
X4_VALUES = 113


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--retained",type=Path,required=True)
    ap.add_argument("--marking",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()

    req(blob(PARENT)==PARENT_BLOB,"parent drift")
    census=json.loads(CENSUS.read_text())
    stored=census.pop("canonical_sha256_without_this_field")
    req(stored==CENSUS_CANON and csha(census)==stored,"census receipt canonical drift")
    req(census["result"]["base4_key_count"]==343,"base4 count drift")

    parent=load_module(PARENT,"stage32_btva_d8_known_parent")
    old=parent.load_module(parent.RELAXED,"stage32_btva_d8_known_relaxed")
    v1=old.load_module(old.BASE,"stage32_btva_d8_known_base")

    bundle=v1.load_retained(args.retained,"stage32_btva_d8_known_bundle")
    marking=v1.load_retained(args.marking,"stage32_btva_d8_known_marking")
    data=v1.reconstruct_translation_data(marking,bundle)
    adapter=data["adapter"]
    bridge=data["bridge"]
    coords=adapter.class_coordinates_in_retained_basis
    P=adapter.pairing_matrix
    req(coords.shape==(TOTAL_KNOWN,64),"known coordinate shape")
    req(P.shape==(TOTAL_KNOWN,64),"pairing matrix shape")

    indexer=v1.CompressedTerminalIndexer(E,DEGREE)
    stride=indexer.normal_budget+1
    req(stride==X4_VALUES,"x4 range drift")
    base4_counts=Counter()
    for erank in range(int(indexer.exceptional_count)):
        x=tuple(int(v) for v in indexer.unrank(erank*stride))
        base4_counts[tuple(old.static_from_terminal(x)[:4])]+=1
    req(len(base4_counts)==343,"reconstructed base4 population drift")

    degree_hist=Counter()
    rows=[]
    overlap_rows=[]
    for i in range(TOTAL_KNOWN):
        x=coords.row(i).T
        degree=int(v1.linear_expr(bridge.degree_functional,[int(v) for v in x]))
        degree_hist[degree]+=1
        if degree!=DEGREE:
            continue
        all140=tuple(int(v) for v in (P*x))
        assignment=tuple(all140[label-1] for label in old.ASSIGNMENT)
        base4=tuple(
            sum(int(old.L[r][j])*assignment[j] for j in range(len(old.ASSIGNMENT)))
            for r in range(4)
        )
        row={
            "known_curve_index_0based":i,
            "known_curve_label_1based":i+1,
            "family":"normal" if i<NORMAL_COUNT else "exceptional",
            "degree":degree,
            "self_intersection":all140[i],
            "minimum_all140_pairing":min(all140),
            "assignment11":list(assignment),
            "base4":list(base4),
            "base4_in_g0_d008_e8_population":base4 in base4_counts,
            "base4_exceptional_multiplicity_per_x4":int(base4_counts.get(base4,0)),
        }
        rows.append(row)
        if row["base4_in_g0_d008_e8_population"]:
            overlap_rows.append(row)

    payload={
        "schema":"STAGE32_MAIN_BTVA_D8_KNOWN_CURVE_OVERLAP_DIAGNOSTIC_V1",
        "stage":32,
        "status":"EXACT_DIAGNOSTIC_ZERO_CREDIT",
        "target":{"row_id":"g0-d008","degree":8,"exceptional_mass":8,"base4_population":343},
        "source_locks":{
            "parent_blob_sha1":PARENT_BLOB,
            "census_receipt_canonical_sha256":CENSUS_CANON,
            "base_picard_solver_blob_sha1":old.BASE_BLOB,
        },
        "known_curve_degree_histogram":[{"degree":d,"count":degree_hist[d]} for d in sorted(degree_hist)],
        "degree8_known_curves":rows,
        "summary":{
            "degree8_known_curve_count":len(rows),
            "degree8_normal_count":sum(1 for r in rows if r["family"]=="normal"),
            "degree8_exceptional_count":sum(1 for r in rows if r["family"]=="exceptional"),
            "degree8_known_curve_base4_overlap_count":len(overlap_rows),
            "overlap_labels_1based":[r["known_curve_label_1based"] for r in overlap_rows],
        },
        "interpretation":{
            "if_overlap_count_zero":"every g0-d008,e8 target base4 is distinct from every known degree-8 curve; known-curve negative self-intersection cannot invalidate all140 nonnegativity on this receiver via equality with a known curve",
            "if_overlap_nonzero":"exclude or separately model the listed known-curve-compatible base4 fibers before promoting all140 nonnegativity as a receiver-wide necessary condition",
        },
        "firewalls":{
            "main_pruning_credit":False,
            "receiver_credit":False,
            "effectivity_credit":False,
            "theorem_credit":False,
            "endpoint_credit":False,
            "full178_complete":False,
            "stage32_closed":False,
            "merge_authorized":False,
        }
    }
    payload["canonical_sha256_without_this_field"]=csha(payload)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    print("BTVA_D8_KNOWN_CURVE_OVERLAP_SUMMARY="+json.dumps(payload["summary"],sort_keys=True))
    print("BTVA_D8_KNOWN_CURVE_OVERLAP_CANONICAL="+payload["canonical_sha256_without_this_field"])


if __name__=="__main__":
    main()
