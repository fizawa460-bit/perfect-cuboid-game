#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = ROOT / "stages/stage32/management/post-certlift03-current-v22-composition-consumption-20260913.json"

V22_HEAD = "f8039b4ce479a4b91f2f0547e7049f629e9be5f5"
V22_REVIEW = 5188224290
V22_STATE_BLOB = "80fb35c79854bfdf775dc5b94c331f5f8a535ced"
V22_STATE_CANON = "82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c"
CERT_REVIEWED_HEAD = "289437a4a97a814c2388133cbde0c794d9502e4b"
CERT_AUDIT_PASS_HEAD = "51c56b5c3ee15177c2975b966ab546d0b548c4af"
CERT_REVIEW_ID = 5188860951
CERT_ADAPTER_BLOB = "327aa601acad47bc1e486cccbbac3d3dee7c2681"
CERT_ADAPTER_CANON = "597fe83b10c7a23f1da9748423ea3f70a78d448991a253777b64cab554c7ffaf"
CERT_CANDIDATE_RECEIPT_BLOB = "291bb8b125566bb72c1caae0537dff2625219ffb"
CERT_CANDIDATE_RECEIPT_CANON = "983042fb058d60b9c2ab39ee24c7192d93fec92ab6c9b81c840c91903133c858"
CERT_AUDIT_RECEIPT_BLOB = "442f84b392254383736f1b695da7a9b2954c053d"
CERT_AUDIT_RECEIPT_CANON = "ceec3c102ad194c05e1429e7af293716a21993fb2dcfd531525c30c371bc2821"
V15_REVIEWED_HEAD = "7c3a9c301d9e1d98678fcd1532afce62c44d56e0"

RECEIPT_BLOB = "7a9d84f6ca137740aba01b6983a02a229dc13036"
RECEIPT_CANON = "4de6317e2bde395de5aaa58036148e8dc1df1330d614f2143d8e15e7ede2e935"
STATE_BLOB = "bead809db3a008dd35d664a8923f06fecb7de5bb"
STATE_CANON = "460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"

CUT_HEADS = {
    "CUT193":"5b2ebb3f67805eddefef835878ba4b9744bfdbd9",
    "CUT194":"847f3bff0c5e0d0530bfb8db406e955b2d231d9a",
    "CUT195":"2618f4dcd546d569b212753ac7abc10e07ee5828",
    "CUT196":"85f4e988acf6446fa0d472208e21990621a650b4",
    "CUT197":"adce53dc9004c24bffb3ba9f88e9d5d6e51cf6a5",
    "CUT198":"16e439bc65e723c9f2658c274d53fb839738dcd2",
}
PRE = 47589703313957134804198
INC_BLOCKS = 1369
INC_TERMINALS = 154697
POST = 47589703313957134649501
TARGET = 1677
OVERLAP = 308
WIDTH = 113
N372_RANK = 128820
N372_BLOCK = 1140
N372_BASE = (0,1,1,0,0,0,1,0,1,0,0)
ASSIGNMENT_ORDER = [95,99,103,102,49,97,94,101,93,98,96]
G3 = [93,94,95,96]

def req(v, m):
    if not v:
        raise SystemExit("FAIL: " + m)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()

def locked_json(path: Path, blob: str, canonical: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == canonical, f"stored canonical drift {path}")
    req(canon(obj) == canonical, f"canonical drift {path}")
    return obj

def head(root: Path) -> str:
    return subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"], text=True).strip()

def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-main-v22-root", type=Path, required=True)
    ap.add_argument("--certlift-reviewed-root", type=Path, required=True)
    ap.add_argument("--certlift-audit-pass-root", type=Path, required=True)
    ap.add_argument("--audited-v15-adapter-root", type=Path, required=True)
    for name in CUT_HEADS:
        ap.add_argument("--" + name.lower() + "-root", type=Path, required=True)
    a = ap.parse_args()

    v22 = a.audited_main_v22_root.resolve()
    reviewed = a.certlift_reviewed_root.resolve()
    auditpass = a.certlift_audit_pass_root.resolve()
    v15 = a.audited_v15_adapter_root.resolve()
    roots = {name:getattr(a, name.lower().replace("-", "_") + "_root").resolve() for name in CUT_HEADS}

    req(head(v22) == V22_HEAD, "V22 exact head drift")
    req(head(reviewed) == CERT_REVIEWED_HEAD, "CERTLIFT reviewed head drift")
    req(head(auditpass) == CERT_AUDIT_PASS_HEAD, "CERTLIFT audit-pass receipt head drift")
    req(head(v15) == V15_REVIEWED_HEAD, "V15 semantic-provenance head drift")
    for name, expected in CUT_HEADS.items():
        req(head(roots[name]) == expected, f"{name} exact head drift")

    old = locked_json(v22 / "stages/stage32/MAIN-STATE.json", V22_STATE_BLOB, V22_STATE_CANON)
    of = old["current_exact_frontier"]
    req(of["authoritative_remaining_strata"] == 17128, "V22 strata drift")
    req(of["authoritative_remaining_terminals"] == PRE, "V22 terminal authority drift")
    for k in ("cut191_main_pruning_credit","cut193_main_pruning_credit","cut194_main_pruning_credit",
              "cut195_main_pruning_credit","cut196_main_pruning_credit","cut197_main_pruning_credit",
              "cut198_main_pruning_credit","n358_main_pruning_credit"):
        req(of.get(k) is True, f"V22 consumed-credit drift {k}")

    audit = locked_json(
        auditpass / "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-PASS.json",
        CERT_AUDIT_RECEIPT_BLOB, CERT_AUDIT_RECEIPT_CANON)
    req(audit["status"] == "HOSTILE_AUDIT_PASS", "CERTLIFT audit status drift")
    req(audit["review_id"] == CERT_REVIEW_ID, "CERTLIFT review id drift")
    req(audit["reviewed_pr_head"] == CERT_REVIEWED_HEAD, "CERTLIFT reviewed-head receipt drift")
    req(audit["adapter_blob_sha1"] == CERT_ADAPTER_BLOB, "CERTLIFT adapter blob receipt drift")
    req(audit["adapter_canonical_sha256"] == CERT_ADAPTER_CANON, "CERTLIFT adapter canonical receipt drift")

    req(git_blob(reviewed / "stages/stage32/cert-lift/certlift03_v22_consumption_adapter.py") == CERT_ADAPTER_BLOB,
        "CERTLIFT reviewed adapter blob drift")
    locked_json(reviewed / "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-RECEIPT.json",
                CERT_CANDIDATE_RECEIPT_BLOB, CERT_CANDIDATE_RECEIPT_CANON)

    env = os.environ.copy()
    env["CERTLIFT_V22_MAIN_ROOT"] = str(v22)
    env["CERTLIFT_ADAPTER_AUDITED_ROOT"] = str(v15)
    for name, root in roots.items():
        env[f"CERTLIFT_{name}_ROOT"] = str(root)
    replay = reviewed / "stages/stage32/cert-lift/verify_certlift03_v22_consumption_adapter_receipt.py"
    subprocess.run([sys.executable, str(replay)], cwd=reviewed, env=env, check=True)

    residual = v22 / "stages/stage32/residual-32-01-production"
    sys.path.insert(0, str(residual))
    idxmod = load_module(residual / "compressed_terminal_indexer.py", "s32_v23_indexer")
    idx = idxmod.CompressedTerminalIndexer(8,8)
    req(idx.normal_budget + 1 == WIDTH, "e8 block width drift")
    req(N372_RANK // WIDTH == N372_BLOCK and N372_RANK % WIDTH == 0, "N372 rank/block drift")
    base = tuple(int(v) for v in idx.unrank(N372_RANK))
    req(base == N372_BASE, f"N372 base drift: {base}")
    by = {label:int(value) for label,value in zip(ASSIGNMENT_ORDER, base)}
    fixed_mass = sum(value for label,value in by.items() if label != 49)
    g3 = sum(by[label] for label in G3)
    req(fixed_mass == 4 and g3 == 2, "N372 CERTLIFT feature drift")
    req(not (fixed_mass >= 7 and g3 == 3), "N372 unexpectedly matches CERTLIFT predicate")

    r = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    req(r["certlift03_external_audit"]["review_id"] == CERT_REVIEW_ID, "MAIN receipt review drift")
    c = r["composition"]
    req(c["symbolic_target_blocks"] == TARGET and c["prior_overlap_union_blocks"] == OVERLAP, "MAIN receipt target/overlap drift")
    req(c["incremental_blocks"] == INC_BLOCKS and c["incremental_rejected_terminals"] == INC_TERMINALS, "MAIN receipt increment drift")
    req(c["double_charge"] is False and c["cut199_main_pruning_credit"] is False, "MAIN receipt credit/double-charge drift")
    req(r["n372_firewall"]["certlift03_predicate_matches"] is False and r["n372_firewall"]["current_authority_witness_preserved"] is True, "N372 receipt firewall drift")
    req(PRE - INC_TERMINALS == POST, "authority arithmetic drift")
    req(r["authority"]["after_remaining_terminals"] == POST, "MAIN receipt post authority drift")

    s = locked_json(STATE, STATE_BLOB, STATE_CANON)
    sf = s["current_exact_frontier"]
    req(sf["authoritative_remaining_strata"] == 17128 and sf["authoritative_remaining_terminals"] == POST, "V23 authority drift")
    req(sf["certlift03_main_pruning_credit"] is True, "CERTLIFT MAIN credit missing")
    req(sf["certlift03_incremental_blocks"] == INC_BLOCKS and sf["certlift03_incremental_rejected_terminals"] == INC_TERMINALS, "V23 increment drift")
    req(sf["certlift03_prior_overlap_blocks"] == OVERLAP and sf["certlift03_double_charge"] is False, "V23 overlap drift")
    req(sf["cut199_main_pruning_credit"] is False, "CUT199 overcredit")
    req(sf["n372_current_authority_witness"] is True and sf["n372_survives_certlift03"] is True, "N372 lost")
    req(sf["n372_main_pruning_credit"] is False and sf["n372_full178_credit"] is False and sf["n372_effectivity_final_credit"] is False, "N372 overcredit")
    req(sf["full178_numerical_census_complete"] is False and sf["stage32_closed"] is False, "closure overcredit")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "replacement re-audit gate missing")
    for k in ("receiver_credit","theorem_credit","endpoint_credit","stage32_closed",
              "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(s["firewalls"][k] is False, f"firewall opened {k}")

    sync = r["claim_sync"]
    req(sync["semantic_claim_core_changed"] is False and sync["active_frontier_remap"] is False, "claim-sync semantic drift")
    req(sync["full178_claim_remains_incomplete"] is True and sync["claim_dag_verifiers_required"] is True, "claim-sync firewall drift")

    print(json.dumps({
        "verdict":"PASS_CERTLIFT03_CURRENT_V22_COMPOSITION_AND_MAIN_CONSUMPTION",
        "prior_authority":PRE,
        "incremental_blocks":INC_BLOCKS,
        "incremental_terminals":INC_TERMINALS,
        "remaining_terminals":POST,
        "prior_overlap_blocks":OVERLAP,
        "n372_preserved":True,
        "cut199_credit":False,
        "full178_complete":False,
        "replacement_head_hostile_reaudit_required":True,
        "merge_authorized":False
    }, sort_keys=True))

if __name__ == "__main__":
    main()
