#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
WORKER=HERE/"run_grf04_hpadj22_full178_parent_cshard.py"
MANIFEST=HERE/"GRF04-HPADJ22-V46-FULL178-LOCAL-ROWS-RETAINED.json"
WORKER_BLOB="611300610f8300f919c60ff1b0a234fd90d30ec3"
LEGACY_WORKER_BLOB="c9fbf71242581f096718ebf0dbc9ac88878c91f1"
MANIFEST_BLOB="df54d3a73fec673c926f23bc251756df299a2102"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_worker():
    req(blob(WORKER)==WORKER_BLOB,"current c-shard worker blob drift")
    spec=importlib.util.spec_from_file_location("v46_local_rows_worker",WORKER)
    req(spec and spec.loader,"cannot load current c-shard worker")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def main():
    req(blob(MANIFEST)==MANIFEST_BLOB,"retained local-row manifest blob drift")
    m=json.loads(MANIFEST.read_text())
    req(m.get("schema")=="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_LOCAL_ROWS_RETAINED_V1","manifest schema drift")
    req(m.get("status")=="EXACT_LOCAL_ROWS_RETAINED_ZERO_CREDIT","manifest status drift")
    req(m["coverage"]["certificate_count"]==6 and m["coverage"]["unique_accounting_key_count"]==6,"retained row count drift")
    req(m["coverage"]["all_complete_rows"] is True,"retained rows must be complete")
    f=m["firewalls"]
    req(all(f[k] is False for k in ("main_pruning_credit","full178_credit","theorem_credit","effectivity_credit","receiver_credit","route_credit","endpoint_credit","merge_authorized")),"credit firewall drift")
    req(f["hostile_audit_required_before_promotion"] is True,"hostile-audit gate drift")
    w=load_worker()
    seen=set();total=0
    for rec in m["rows"]:
        key=(rec["band_position"],rec["chunk_position"],rec["row_window_position"],rec["row_index"])
        req(key not in seen,f"duplicate retained identity {key}");seen.add(key)
        p=Path(rec["path"])
        req(p.is_file(),f"missing retained row {p}")
        req(blob(p)==rec["git_blob_sha1"],f"retained row blob drift {p}")
        d=json.loads(p.read_text())
        req(d.get("canonical_sha256_without_this_field")==rec["canonical_sha256"]==canon(d),f"retained row canonical drift {p}")
        t=d["target"];r=d["result"]
        req((t["band_position"],t["chunk_position"],t["row_index"],t["row_id"],int(t["g"]),int(t["d"]),t["b_chunk"])==
            (rec["band_position"],rec["chunk_position"],rec["row_index"],rec["row_id"],rec["g"],rec["d"],rec["b_chunk"]),f"target drift {p}")
        req(str(r["hpadj22_exact_survivors"])==rec["hpadj22_exact_survivors"],f"baseline drift {p}")
        req(str(r["joint_exact_survivors"])==rec["joint_exact_survivors"],f"joint drift {p}")
        req(str(r["exact_improvement"])==rec["exact_improvement"],f"improvement drift {p}")
        req(int(r["hpadj22_exact_survivors"])-int(r["joint_exact_survivors"])==int(r["exact_improvement"]),f"arithmetic drift {p}")
        b0,b1=(int(x) for x in rec["b_chunk"])
        accepted=w.validate_carry(
            p,worker_blob=WORKER_BLOB,worker_blobs=(LEGACY_WORKER_BLOB,),
            band=int(rec["band_position"]),chunk=int(rec["chunk_position"]),b0=b0,b1=b1,
            row_index=int(rec["row_index"]),row_id=str(rec["row_id"]),g=int(rec["g"]),d=int(rec["d"]))
        req(accepted is not None,f"production validate_carry rejected {p}")
        total+=int(rec["exact_improvement"])
    req(len(seen)==6,"retained identity cardinality drift")
    req(str(total)==m["result"]["selected_exact_improvement"]=="157151676541230906","retained exact total drift")
    req(str(138652739800650593494-total)==m["result"]["research_only_candidate_upper_bound_if_separately_audited"]=="138495588124109362588","research-only candidate arithmetic drift")
    print("PASS: 6 retained local FULL178 row certificates are canonical, source-locked, production-validate_carry accepted, pairwise distinct, and zero-credit")
    print("PASS: retained exact improvement sum = 157151676541230906; no MAIN/FULL178/downstream credit granted")

if __name__=="__main__":main()
