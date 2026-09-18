#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CHECKPOINT=HERE/"ZERO-CENTER-E32-FULL-X4-ROW-CHECKPOINT.json"
CHECKPOINT_BLOB="18ddff73af80d750f4087008dd1e3941b2bee989"
CONSUMER=HERE/"verify_fibration_nef_zero_center_e32_full_x4_row.py"
CONSUMER_BLOB="225b1e847dc44646df4ff6fb3f80babd9db58479"


def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)


def git_blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def main()->None:
    req(CHECKPOINT.is_file() and git_blob(CHECKPOINT)==CHECKPOINT_BLOB,"checkpoint drift")
    req(CONSUMER.is_file() and git_blob(CONSUMER)==CONSUMER_BLOB,"consumer drift")
    cp=json.loads(CHECKPOINT.read_text())

    req(cp["schema"]=="STAGE32_32_01_178_ZERO_CENTER_E32_FULL_X4_ROW_CHECKPOINT_V1","schema drift")
    req(cp["status"]=="EXACT_HEAD_REPLAY_SUCCESS__HOSTILE_AUDIT_REQUIRED__ZERO_MAIN_CREDIT","status drift")
    req(cp["producer"]["consumer_blob_sha1"]==CONSUMER_BLOB,"producer blob binding drift")
    req(cp["exact_head_ci"]["conclusion"]=="SUCCESS","retained CI conclusion drift")
    req(cp["exact_head_ci"]["replay_head"]=="bd87cb1f077502ebb536268d59e2cefd0a8c493e","retained replay head drift")
    req(int(cp["exact_head_ci"]["workflow_run_id"])==35317802658,"retained run id drift")
    req(int(cp["exact_head_ci"]["job_id"])==105513202953,"retained job id drift")

    flat=cp["exact_x4_partition"]["flat_full_pass"]
    tail=cp["exact_x4_partition"]["tail_exact"]
    zero=cp["exact_x4_partition"]["uniform_zero"]
    req(flat["range"]==[0,109] and int(flat["slice_count"])==110,"flat range drift")
    req(tail["range"]==[110,134] and int(tail["slice_count"])==25,"tail range drift")
    req(zero["range"]==[135,3488] and int(zero["slice_count"])==3354,"zero range drift")
    req(110+25+3354==3489,"x4 partition cardinality")
    req(int(flat["total_exact_weighted_mass"])+int(tail["total_exact_weighted_mass"])
        ==int(cp["result"]["complete_e32_x4_exact_weighted_mass"]),"mass accounting mismatch")
    req(cp["result"]["complete_e32_x4_exact_weighted_mass"]=="41498727425","full-row mass drift")
    req(flat["one_slice_exact_weighted_mass"]=="324815269","flat-slice mass drift")
    req(tail["summary_stream_sha256"]=="6a727ea13e0ae2e2aeb49682ddad502f775cd94f3795620a95aa5030897dd793",
        "tail stream drift")

    req(cp["firewalls"]["hostile_audit_pass"] is False,"audit credit prematurely granted")
    req(cp["firewalls"]["main_credit_changed"] is False,"MAIN credit changed")
    req(cp["firewalls"]["full178_census_claimed"] is False,"FULL178 claimed")
    req(cp["firewalls"]["merge"] is False,"merge firewall changed")

    print("ZERO_CENTER_E32_FULL_X4_CHECKPOINT_SUMMARY="+json.dumps({
      "checkpoint_blob":CHECKPOINT_BLOB,
      "consumer_blob":CONSUMER_BLOB,
      "full_row_mass":cp["result"]["complete_e32_x4_exact_weighted_mass"],
      "x4_partition":[110,25,3354],
      "hostile_audit_required":True
    },sort_keys=True))


if __name__=="__main__":
    main()
