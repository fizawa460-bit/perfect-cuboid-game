#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648au-cusp-incidence-universal-bezout-wall.json"
NOTE = HERE / "post1648au-cusp-incidence-universal-bezout-wall-source-note.md"
DIAG = HERE / "diagnose_stage32_post1648au_cusp_incidence_low_bidegree_preflight.py"
EXPECTED = "6602faaadc6e97a114ac8b4f73bd286a5439a5d146d7fedacbebe094d239e541"


def canonical_sha(obj: dict) -> str:
    y=dict(obj); y.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(y,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def blob_sha(path: Path) -> str:
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()


def main() -> None:
    cert=json.loads(CERT.read_text())
    assert cert["canonical_sha256_without_this_field"]==EXPECTED
    assert canonical_sha(cert)==EXPECTED
    assert blob_sha(NOTE)==cert["source_locks"]["source_note_blob_sha1"]
    assert blob_sha(DIAG)==cert["source_locks"]["diagnostic_blob_sha1"]

    proc=subprocess.run([sys.executable,"-B",str(DIAG)],cwd=ROOT,check=True,capture_output=True,text=True)
    x=json.loads(proc.stdout)
    assert x["mode"]=="SCRATCH_POST1648AU_CUSP_INCIDENCE_LOW_BIDEGREE_PREFLIGHT_V2"
    assert x["parent"]["AT_canonical"]==cert["parent"]["at_canonical"]
    ci=cert["cusp_incidence"]
    assert x["cusp_incidence"]["component_type"]==ci["component_type"]=="3_disjoint_K2_2"
    assert [c["weight_sum"] for c in x["cusp_incidence"]["components"]]==ci["block_weights"]==[96,108,62]
    assert x["cusp_incidence"]["total_weight"]==ci["total_weight"]==266
    assert x["cusp_incidence"]["dir81_weight_sums"]==ci["dir81_weight_sums"]
    assert x["cusp_incidence"]["dir105_weight_sums"]==ci["dir105_weight_sums"]

    u=cert["universal_capacity"]; xu=x["universal_bezout_capacity"]
    assert xu["row_max_sum"]==u["row_max_sum"]==168
    assert xu["column_max_sum"]==u["column_max_sum"]==173
    assert xu["all_positive_bidegrees_excluded_from_cusp_weight_bezout_obstruction"] is True
    assert u["all_positive_bidegrees_safe_from_cusp_weight_bezout"] is True
    assert u["requirements_incompatible"] is True

    o=cert["one_one_check"]; xo=x["one_one_check"]
    assert xo["max_weight_matching"]==o["maximum_weight_matching"]==168
    assert xo["D_dot_1_1"]==o["D_dot_F81_plus_F105"]==186
    assert xo["margin"]==o["margin"]==-18

    assert cert["decision"]["v6_carrier_excluded"] is False
    assert cert["firewalls"]["Q602_excluded"] is False
    assert cert["firewalls"]["O210_excluded"] is False
    assert cert["firewalls"]["O212_plus_advance_allowed"] is False
    print("PASS stage32 post1648AU universal cusp-weight Bezout wall")
    print(json.dumps({
      "canonical":EXPECTED,
      "component_type":ci["component_type"],
      "row_max_sum":u["row_max_sum"],
      "column_max_sum":u["column_max_sum"],
      "one_one_margin":o["margin"],
      "v6_excluded":False,
    },sort_keys=True))


if __name__=="__main__":
    main()
