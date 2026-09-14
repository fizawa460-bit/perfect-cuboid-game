#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STAGE = ROOT / "stages/stage32"
V20_SNAPSHOT = STAGE / "management/MAIN-STATE-V20-N372-PRE-REBASE.json"
CUT196 = STAGE / "management/CUT196-AUDITED-RESULT.json"
N358 = STAGE / "management/post-n358-current-v18-composition-consumption-20260912.json"
STATE = STAGE / "MAIN-STATE.json"
RECEIPT = STAGE / "management/post-n372-current-v20-authority-rebase-20260913.json"

V20_HEAD = "b6c0a1e431ac04de5326a7c42af89a7b92423ed2"
V20_STATE_BLOB = "0886dc0c0a8b8960ca9b5cf8285801d4948de874"
V20_STATE_CANON = "5b087c68f0d81893c65c8210cca112e57d881bcb0713c6ed81ff46d300584cd2"
N372_HEAD = "9fb78a0e0c7b52baca84058dea69b8b083e33774"
N372_RESULT_BLOB = "c0267d903fd0b397fcd4766b03964bde788650e7"
N372_RESULT_CANON = "b9852fcfa926e77e8c51defe31002e0bf4b281dd1db4b5f320326166932fef48"
CUT196_BLOB = "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde"
CUT196_CANON = "194a37f87355f781f9aca341f9935645d818d5daa1c377883606627c80558a92"
N358_BLOB = "efa87a1b62cc698745f87814cd8f9eb9fe95dbd2"
N358_CANON = "27c50848e19c242389298b6a23d7c5b6a8ea86afd97c36ced16905adc66a5bdc"
STATE_BLOB = "64dc5523652f1bbe4f19456a6854a39cb3aec87a"
STATE_CANON = "739520f562fc445567969088bfea0dd9d87d85c11541d706e6f68748746e0fb7"
RECEIPT_BLOB = "3bba4c4a07f6fcae672e08f80096470297aded18"
RECEIPT_CANON = "c95c9a9fbe5ca1298e037d222dc595632a71806d98278df4e4dc6442c1820acc"
AUTH_TERMS = 47589703313957134886123

def req(v, msg):
    if not v: raise SystemExit("FAIL: " + msg)
def git_blob(path):
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def canonical(obj):
    cp=dict(obj); cp.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(cp,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def locked(path, blob, can):
    req(path.is_file(), f"missing {path}")
    req(git_blob(path)==blob, f"blob drift {path}")
    obj=json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field")==can, f"stored canonical drift {path}")
    req(canonical(obj)==can, f"canonical drift {path}")
    return obj
def head(root):
    return subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--audited-main-v20-root",type=Path,required=True)
    ap.add_argument("--audited-n372-root",type=Path,required=True)
    ap.add_argument("--audited-cut196-root",type=Path,required=True)
    a=ap.parse_args()
    v20root=a.audited_main_v20_root.resolve()
    n372root=a.audited_n372_root.resolve()
    cut196root=a.audited_cut196_root.resolve()

    req(head(v20root)==V20_HEAD,"V20 exact head drift")
    audited_v20=locked(v20root/"stages/stage32/MAIN-STATE.json",V20_STATE_BLOB,V20_STATE_CANON)
    local_v20=locked(V20_SNAPSHOT,V20_STATE_BLOB,V20_STATE_CANON)
    req(audited_v20==local_v20,"local V20 snapshot differs from audited exact head")
    audited_n358=locked(v20root/"stages/stage32/management/post-n358-current-v18-composition-consumption-20260912.json",N358_BLOB,N358_CANON)
    local_n358=locked(N358,N358_BLOB,N358_CANON)
    req(audited_n358==local_n358,"local N358 receipt differs from hostile-audited V20 exact head")
    vf=audited_v20["current_exact_frontier"]
    req(vf["authoritative_remaining_terminals"]==AUTH_TERMS,"V20 authority drift")
    req(vf["n372_current_authority_rebased"] is False,"V20 already self-awarded rebase")

    req(head(n372root)==N372_HEAD,"N372 exact head drift")
    n372=locked(n372root/"stages/stage32/32-01-178/nodes/N372/RESULT.json",N372_RESULT_BLOB,N372_RESULT_CANON)
    w=n372["witness"]
    req(w["terminal_identity"]=="g1-d008|e=8|rank=128820","N372 terminal drift")
    req(w["block_index"]==1140 and w["survivor_offset"]==797 and w["parent_ordinal"]==290,"N372 address drift")
    req(w["self_square"]==-4 and w["negative_hperp_square_N"]==32,"N372 invariant drift")

    req(head(cut196root)=="85f4e988acf6446fa0d472208e21990621a650b4","CUT196 audited exact head drift")
    audited_cut=locked(cut196root/"stages/stage32/full178-cut/CUT196-e8-common-adapter-wave4-result.json",CUT196_BLOB,CUT196_CANON)
    cut=locked(CUT196,CUT196_BLOB,CUT196_CANON)
    req(audited_cut==cut,"retained CUT196 result differs from hostile-audited exact head")
    target=cut["target"]; result=cut["result"]
    req(target["row_id"]=="g1-d008" and target["d"]==8 and target["e"]==8,"CUT196 target drift")
    req(target["survivor_offset_range"]==[766,1020],"CUT196 offset range drift")
    req(1140 in target["block_indices"],"N372 block absent from CUT196 target")
    req(1140 not in result["candidate_closed_block_indices"],"N372 block closed by CUT196")
    req(result["remaining_nonclosed_block_count"]==13,"CUT196 nonclosed count drift")
    req(766 <= 797 <= 1020,"N372 offset outside CUT196 target range")

    zr=audited_n358["current_v18_composition_replay"]["zero_overlap_reason"]
    req(zr["consumed_cut_d"]==8 and zr["consumed_cut_e"]==8,"N358 d/e zero-overlap drift")
    req(zr["h"]==4 and zr["h_minus_5"]==-1,"N358 h bound drift")
    req(zr["nonnegative_b_cannot_satisfy_b_le_h_minus_5"] is True,"N358 nonnegative-b proof drift")
    req(zr["equivalently_n358_incremental_domain_empty_on_g1_d008_e8"] is True,"N358 e8 emptiness drift")

    receipt=locked(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON)
    state=locked(STATE,STATE_BLOB,STATE_CANON)
    req(receipt["current_authority_rebase"]["n372_survives_current_v20_authority"] is True,"receipt survival false")
    req(receipt["current_authority_rebase"]["numerical_authority_changed"] is False,"receipt changed authority")
    req(receipt["authority"]["after_remaining_terminals"]==AUTH_TERMS,"receipt authority drift")
    sf=state["current_exact_frontier"]
    req(sf["n372_current_authority_rebased"] is True and sf["n372_current_authority_witness"] is True,"state rebase missing")
    req(sf["n372_survives_cut196"] is True and sf["n372_survives_n358"] is True,"state survival proof missing")
    for k in ("n372_main_pruning_credit","n372_full178_credit","n372_effectivity_final_credit","full178_numerical_census_complete","stage32_closed"):
        req(sf[k] is False,f"unauthorized credit opened: {k}")
    req(sf["authoritative_remaining_terminals"]==AUTH_TERMS,"state authority changed")
    req(state["firewalls"]["merge_authorized"] is False,"merge authorized")
    print(json.dumps({"verdict":"PASS_N372_CURRENT_V20_AUTHORITY_REBASE","terminal":"g1-d008|e=8|rank=128820","survives_cut196":True,"survives_n358":True,"n358_dependency_bound_to_audited_v20":True,"current_authority_witness":True,"numerical_authority_changed":False,"main_pruning_credit":False,"full178_complete":False,"effectivity_credit":False,"merge_authorized":False},sort_keys=True))
if __name__=="__main__": main()
