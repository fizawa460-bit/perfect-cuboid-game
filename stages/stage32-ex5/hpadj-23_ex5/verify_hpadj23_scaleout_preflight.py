#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PREFLIGHT=HERE/"HPADJ23-FULL178-SCALEOUT-PREFLIGHT.json"
RUNKEY=ROOT/"stages/stage32-ex5/runkeys/hpadj23-scaleout-measurement.json"
SHARD=HERE/"build_exact_t_joint_histogram_shard.py"
SHARD_EQ=HERE/"HPADJ23-SHARD-BOUNDED-EQUIVALENCE.json"
SHARD_EQ_VER=HERE/"verify_hpadj23_shard_bounded_equivalence.py"
HANDOFF=HERE/"HPADJ23-BOUNDED-PRODUCER-HANDOFF.json"
MANIFEST=ROOT/"stages/stage32/residual-32-01-production/full178-manifest.json"

LOCKS={
  "preflight_blob":"0b71f07f3bfbb0497ddb0be9a0b5ad28681780b6",
  "preflight_canon":"7c2422f74dd39a53be844468d738aa061d531409740af480998e62bc0fa04b3d",
  "runkey_blob":"2e47aae6c05d7e12d34be6cca482b747ac71f811",
  "runkey_canon":"cac4eaaad929420fa0bf98f8493c7a7c8ac18986b183fd11e13a9d3ed316e24a",
  "shard_blob":"25284ea56c0746912318ce3c0d0e75d50cf60458",
  "shard_eq_blob":"b1a0248926c176a31a57da0fbb97807c3bb0eeba",
  "shard_eq_canon":"5899b8eaac1cd6205d421d6f92874f4dbff47a31a00b37029cc84f9365c19a9b",
  "shard_eq_ver_blob":"6aea0f8c39ea0865fb3926aec55ba25582a31697",
  "handoff_blob":"f2c1d998cd1d2cf032bf1e56c94e710dbc80eddb",
  "handoff_canon":"d31608f8ab1aa9e0c9b11d71c4e560b1fa9f3eef6f26bb2b56145ca937d38615",
  "manifest_blob":"0a46b34e278688240656b4977e9cb7f589e90e06",
  "manifest_canon":"46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23",
}

def req(v: bool,msg: str)->None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canon(obj:dict)->str:
    body=dict(obj)
    body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def locked_json(path:Path,b:str,c:str,label:str)->dict:
    req(path.is_file(),f"missing {label}")
    req(blob(path)==b,f"{label} blob drift")
    obj=json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field")==c,f"{label} stored canonical drift")
    req(canon(obj)==c,f"{label} canonical drift")
    return obj

def main()->None:
    p=locked_json(PREFLIGHT,LOCKS["preflight_blob"],LOCKS["preflight_canon"],"scaleout preflight")
    r=locked_json(RUNKEY,LOCKS["runkey_blob"],LOCKS["runkey_canon"],"scaleout measurement runkey")
    e=locked_json(SHARD_EQ,LOCKS["shard_eq_blob"],LOCKS["shard_eq_canon"],"shard equivalence")
    h=locked_json(HANDOFF,LOCKS["handoff_blob"],LOCKS["handoff_canon"],"bounded producer handoff")
    m=locked_json(MANIFEST,LOCKS["manifest_blob"],LOCKS["manifest_canon"],"FULL178 manifest")
    req(blob(SHARD)==LOCKS["shard_blob"],"shard builder drift")
    req(blob(SHARD_EQ_VER)==LOCKS["shard_eq_ver_blob"],"shard equivalence verifier drift")

    rows=[]
    for arr in m["m_class_rows"].values():
        for row_id in arr:
            mm=re.fullmatch(r"g([01])-d(\d+)",row_id)
            req(mm is not None,"manifest row-id drift")
            rows.append((int(mm.group(1)),int(mm.group(2))))
    ds=sorted({d for _,d in rows})
    hs=sorted({d//2 for _,d in rows})
    req(len(rows)==178,"FULL178 row count drift")
    req(ds==list(range(8,193,2)),"FULL178 degree support drift")
    req(hs==list(range(4,97)),"FULL178 H support drift")

    req(p["full178_structure"]["row_count"]==178,"preflight row count")
    req(p["full178_structure"]["unique_H_count"]==93,"preflight H count")
    req(p["full178_structure"]["g_dependency_of_exact_t_BC_histogram"] is False,"unexpected g dependency")
    req(p["prefix_invariance"]["bounded_regression_pass"] is True,"prefix regression not retained")
    req(p["sharding"]["bounded_H16_four_shard_union_pass"] is True,"bounded shard union not retained")
    req(p["sharding"]["bounded_H16_union_bins"]==47667,"bounded shard bin count")
    req(p["sharding"]["bounded_H16_union_exact_t_entries"]==207474,"bounded shard t-entry count")
    req(e["bounded_test"]["shard_union_equals_full_builder"] is True,"equivalence result not exact")
    req(e["scaleout_semantics"]["universal_H96_can_supply_all_full178_rows"] is True,"universal H96 result drift")

    req(p["source_locks"]["bounded_handoff_canonical_sha256"]==LOCKS["handoff_canon"],"handoff lock drift")
    req(p["source_locks"]["shard_builder_blob_sha1"]==LOCKS["shard_blob"],"shard lock drift")
    req(p["source_locks"]["shard_equivalence_canonical_sha256"]==LOCKS["shard_eq_canon"],"equivalence lock drift")
    req(p["source_locks"]["full178_manifest_canonical_sha256"]==LOCKS["manifest_canon"],"manifest lock drift")

    req(r["generation"]==0 and r["mode"]=="COLD" and r["armed"] is False,"measurement runkey unexpectedly armed")
    req(r["authorized_operation"]=="NONE","measurement operation unexpectedly authorized")
    req(r["measurement_target"]=={"H":32,"b_start":0,"b_stop":11},"measurement target drift")
    req(r["source_locks"]["scaleout_preflight_canonical_sha256"]==LOCKS["preflight_canon"],"runkey preflight lock drift")
    req(r["authorization_contract"]["production_scaleout_not_authorized_by_measurement"] is True,"measurement promoted to production")

    a=p["authorization"]
    req(a["measurement_armed"] is False and a["full178_production_armed"] is False,"preflight unexpectedly armed")
    req(a["ordinary_mainbatch_may_arm"] is False,"ordinary mainbatch arm firewall drift")
    req(a["storage_preflight_complete"] is False,"storage preflight overclaim")
    req(all(v is False for v in p["firewalls"].values()),"scaleout preflight credit firewall raised")
    req(all(v is False for v in r["credit"].values()),"runkey credit firewall raised")
    req(h["scope"]["full178_producer_complete"] is False,"bounded handoff promoted to FULL178")

    print(json.dumps({
      "verdict":"PASS_HPADJ23_FULL178_SCALEOUT_PREFLIGHT_COLD",
      "full178_rows":178,
      "unique_H":93,
      "universal_HMAX":96,
      "provisional_bands":8,
      "measurement_target":[32,0,11],
      "measurement_armed":False,
      "production_armed":False,
      "main_credit":False,
    },sort_keys=True))

if __name__=="__main__":
    main()
