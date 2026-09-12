#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STAGE = ROOT / "stages/stage32"

V18 = STAGE / "management/MAIN-STATE-V18-N358-PRECONSUMPTION.json"
N358_SNAPSHOT = STAGE / "management/N358-AUDITED-RESULT.json"
CUT191 = STAGE / "management/post-cut191-hostile-pass-consumption-20260911.json"
CUT194 = STAGE / "management/post-cut194-hostile-pass-consumption-20260912.json"
CUT195 = STAGE / "management/post-cut195-current-v14-composition-consumption-20260912.json"
CUT196 = STAGE / "management/post-cut196-current-v16-composition-consumption-20260912.json"

V18_HEAD = "152e8f92346c038aed5628d7d70063cc5c8cd9d4"
V18_BLOB = "48a3b18671ddd85a8b0916a8be1d9f611c38b534"
V18_CANONICAL = "8590ba2d6a8d9e5250f5849a5052a3abeef43884eee2e237d5372dd61f841bef"
N358_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
N358_REVIEW = 5184322011
N358_CI = 34659319718
N358_RESULT_BLOB = "e42c2b6cc6128c4666372b0c3f3c172afc006d7f"
N358_RESULT_CANONICAL = "383921ed9387693a8cfa300a9629f629f3a20ed4272979508441c7b13af5a287"
N358_AUDIT_VERIFIER_BLOB = "78db45499a79438a4f01889012a358a39e43ea8c"
N358_EXACT_CENSUS_BLOB = "c07a7e358a6253919194189377d6ed56f95e047a"
N358_JOINT_BLOB = "63666cdb0f3d14676f0ab5dac561501279e8c2a0"

CUT_LOCKS = {
    "CUT191": (CUT191, "8bea39e443d7996a8958c95005206d6ff349fa52", "f1c59f708190f99ef87422eabc443a5c9df981438a5e647c93dc5052fc5fe6a2", 113),
    "CUT194": (CUT194, "775c7853de989ee92167269bf3be774bd1e984f3", "6e9711716358ff955fe3aac1fda9661a800f3f1e3d10286fa5127a4638efb568", 26442),
    "CUT195": (CUT195, "148ea573bb1f618baac33c0d1f8cc91678fbbca2", "e33fb30bef69ce3ef87f095b500ecd4a8a21b155a3d9c957836ed17c82ad6be9", 26216),
    "CUT196": (CUT196, "a45f27611d6d274e7e7e3ff65e8a75089e996596", "2c55ddd13f90068fc8383c755dcada07f265c40c6ff468709b0add12a390c0e2", 27346),
}

N357_SOURCE = 47598978285064933810198
V18_TERMINALS = 47598978285064933730081
N358_INCREMENT = 9274971107798843958
HISTORICAL_N358_POST = 47589703313957134966240
POST = 47589703313957134886123
STRATA = 17128

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def load_locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can, f"stored canonical drift {path}")
    req(canonical(obj) == can, f"canonical drift {path}")
    return obj

def exact_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()

def n358_scope_empty_on_cut_target(d: int, e: int) -> bool:
    h = d // 2
    return h - 5 < 0

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-main-v18-root", type=Path, required=True)
    ap.add_argument("--audited-n358-root", type=Path, required=True)
    args = ap.parse_args()
    main_v18_root = args.audited_main_v18_root.resolve()
    n358_root = args.audited_n358_root.resolve()

    req(exact_head(main_v18_root) == V18_HEAD, "audited MAIN V18 exact head drift")
    audited_v18_state = main_v18_root / "stages/stage32/MAIN-STATE.json"
    v18 = load_locked(audited_v18_state, V18_BLOB, V18_CANONICAL)
    req(git_blob(V18) == V18_BLOB, "retained V18 snapshot blob drift")
    retained_v18 = load_locked(V18, V18_BLOB, V18_CANONICAL)
    req(retained_v18 == v18, "retained V18 snapshot differs from audited exact-head MAIN state")

    req(exact_head(n358_root) == N358_HEAD, "audited N358 exact head drift")
    external = n358_root / "stages/stage32/32-01-178/nodes/N358"
    req(git_blob(external / "RESULT.json") == N358_RESULT_BLOB, "audited N358 RESULT blob drift")
    req(git_blob(external / "verify_n358_audit_source_locks.py") == N358_AUDIT_VERIFIER_BLOB, "audited N358 audit verifier blob drift")
    req(git_blob(external / "verify_n358_exact_incremental_census.py") == N358_EXACT_CENSUS_BLOB, "audited N358 exact census blob drift")
    req(git_blob(external / "verify_n358_joint_transport_support_saturation.py") == N358_JOINT_BLOB, "audited N358 joint verifier blob drift")

    vf = v18["current_exact_frontier"]
    req(vf["authoritative_remaining_strata"] == STRATA, "V18 strata drift")
    req(vf["authoritative_remaining_terminals"] == V18_TERMINALS, "V18 authority drift")
    for key in ("cut191_main_pruning_credit", "cut194_main_pruning_credit", "n357_main_pruning_credit", "cut195_main_pruning_credit", "cut196_main_pruning_credit"):
        req(vf[key] is True, f"V18 consumed credit missing: {key}")
    req(vf["cut193_main_pruning_credit"] is False, "CUT193 gained credit")
    req(vf["cut197_main_pruning_credit"] is False, "CUT197 gained credit before N358 transition")

    n358 = load_locked(N358_SNAPSHOT, N358_RESULT_BLOB, N358_RESULT_CANONICAL)
    req(n358["schema"] == "STAGE32_32_01_178_N358_EXACT_INCREMENTAL_CENSUS_V1", "N358 schema drift")
    req(n358["audited_input"]["node"] == "N357", "N358 audited input is not N357")
    req(n358["audited_input"]["audited_exact_head"] == "0d787839b7e0dad4a42108c61d16e7849c50862f", "N358 N357 input head drift")
    req(n358["audited_input"]["review_id"] == 5183069892, "N358 N357 input review drift")
    req(n358["audited_input"]["remaining_terminals"] == N357_SOURCE, "N358 N357 source authority drift")
    req(n358["aggregate"]["incremental_rejected_terminals"] == N358_INCREMENT, "N358 audited increment drift")
    req(n358["aggregate"]["candidate_remaining_terminals"] == HISTORICAL_N358_POST, "N358 historical remainder drift")
    req(n358["necessary_cut"]["incremental_rejection_characterization"] == "b-c=3d-e; b<=h-5; s+Srem=K; e-M>=Srem", "N358 characterization drift")
    req(n358["necessary_cut"]["scope"] == "b>=c, h-b>=5, e=3d+c-b", "N358 scope drift")

    cuts = {}
    for cid, (path, blob, can, inc) in CUT_LOCKS.items():
        cuts[cid] = load_locked(path, blob, can)

    c191 = cuts["CUT191"]
    req(c191["n356_overlap_replay"]["target"] == {"row_id":"g1-d008","d":8,"e":8}, "CUT191 target drift")
    req(c191["authority"]["cut191_main_pruning_credit"] is True and c191["authority"]["cut191_incremental_rejected_terminals"] == 113, "CUT191 accounting drift")

    c194 = cuts["CUT194"]
    t194 = c194["cut194_external_audit"]["target"]
    req((t194["row_id"], t194["d"], t194["e"]) == ("g1-d008",8,8), "CUT194 target drift")
    req(c194["authority"]["cut194_main_pruning_credit"] is True and c194["authority"]["cut194_incremental_rejected_terminals"] == 26442, "CUT194 accounting drift")

    c195 = cuts["CUT195"]
    req(c195["current_v14_composition_replay"]["population"] == "g1-d008/e8 current-prefix survivor blocks", "CUT195 target population drift")
    req(c195["authority"]["cut195_main_pruning_credit"] is True and c195["authority"]["incremental_rejected_terminals"] == 26216, "CUT195 accounting drift")

    c196 = cuts["CUT196"]
    req(c196["current_v16_composition_replay"]["population"] == "g1-d008/e8 current-prefix survivor blocks", "CUT196 target population drift")
    req(c196["authority"]["cut196_main_pruning_credit"] is True and c196["authority"]["incremental_rejected_terminals"] == 27346, "CUT196 accounting drift")

    req(n358_scope_empty_on_cut_target(8,8), "N358 unexpectedly has support on g1-d008/e8")
    req(3*8-8 == 16 and 8//2-5 == -1, "N358/CUT domain arithmetic drift")

    cut_total = sum(v[3] for v in CUT_LOCKS.values())
    req(cut_total == 80117, "consumed CUT total drift")
    req(N357_SOURCE - cut_total == V18_TERMINALS, "historical N357/current-V18 composition drift")
    req(HISTORICAL_N358_POST - cut_total == POST, "historical N358/current-cut composition drift")
    req(V18_TERMINALS - N358_INCREMENT == POST, "current-V18 N358 subtraction drift")

    print(json.dumps({"verdict":"PASS_N358_CURRENT_V18_COMPOSITION_AND_MAIN_CONSUMPTION","audited_main_v18_exact_head":V18_HEAD,"audited_main_v18_state_blob":V18_BLOB,"n358_audited_exact_head":N358_HEAD,"n358_hostile_audit_review_id":N358_REVIEW,"n358_exact_head_ci_run":N358_CI,"n357_overlap_terminals":0,"cut191_overlap_terminals":0,"cut194_overlap_terminals":0,"cut195_overlap_terminals":0,"cut196_overlap_terminals":0,"already_consumed_cut_total_terminals":cut_total,"n358_incremental_rejected_terminals":N358_INCREMENT,"authoritative_remaining_strata":STRATA,"authoritative_remaining_terminals":POST,"double_charge":False,"full178_complete":False,"merge_authorized":False}, sort_keys=True))

if __name__ == "__main__":
    main()
