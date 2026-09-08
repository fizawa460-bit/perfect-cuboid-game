#!/usr/bin/env python3
"""Goal4AJ gen25-g4: artifact-direct exact replay of all 27 strict conditions.

Consumes the immutable successful gen24 compact artifact directly instead of the
later malformed repo transport copy. The artifact certificate, gzip bytes, and
decompressed Q candidate are all hash-checked before any exact condition runs.
No finite-field or CRT computation is replayed.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout
import gzip
import hashlib
import io
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
BASE = HERE / "diagnose_stage35_ex_35_goal4aj_numerator_degree31_all27_exact_strict_gen25.py"
BASE_BLOB = "5920842a35877245bcb01a457882674d2b891340"
LOCATOR = HERE / "diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"
GEN24_RUN = 34202980219
GEN24_JOB = 101990701963
GEN24_ARTIFACT_ID = 10047165607
GEN24_ARTIFACT_ZIP_SHA256 = "30ed893acb8be4574838dd37242da3ba2659fdabe7f557b9efe0c62108d7d930"
GEN24_CANONICAL = "9463e3ca0431fbb8310c139481873ddf98122136f360cdac58ecf35eaa325e26"
GZIP_SHA256 = "4758734a80f4ec5c0444acf9b97d0edcbb00a6ee26f1b59c622c711a5d20be8b"
GZIP_BYTES = 45022
Q_SHA = "358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb"
Q_BYTES = 208802
SHARD_COUNT = 9
PROCESS_ORDER = [2,7,13,38,40,15,18,19,22,10,12,23,58,60,14,9,17,3,4,5,6,16,24,27,30,65,67]
MULTIPLICITIES = [21,21,18,13,13,12,12,12,12,10,10,10,9,9,4,3,3,1,1,1,1,1,1,1,1,1,1]
EXPECTED = list(zip(PROCESS_ORDER, MULTIPLICITIES))


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def csha(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_artifact_candidate(artifact_dir: Path) -> str:
    cert_path = artifact_dir / "certificate.json"
    gz_path = artifact_dir / "qcandidate.txt.gz"
    cert = json.loads(cert_path.read_text(encoding="utf-8"))
    assert cert["schema"] == "STAGE35_EX_GOAL4AJ_GEN24_PARALLEL_FOUR_PRIME_MATERIALIZATION_V1"
    assert cert["canonical_sha256"] == GEN24_CANONICAL
    tmp = dict(cert); tmp.pop("canonical_sha256")
    assert csha(tmp) == GEN24_CANONICAL
    assert cert["q_candidate_sha256"] == Q_SHA and cert["q_candidate_text_bytes"] == Q_BYTES
    assert cert["reconstructed_count"] == 5924
    assert cert["reproduces_gen23_first_strict_pass_candidate_exactly"] is True
    gz = gz_path.read_bytes()
    assert len(gz) == GZIP_BYTES and hashlib.sha256(gz).hexdigest() == GZIP_SHA256
    raw = gzip.decompress(gz)
    assert len(raw) == Q_BYTES and hashlib.sha256(raw).hexdigest() == Q_SHA
    actual = {"artifact_id": GEN24_ARTIFACT_ID, "gen24_run": GEN24_RUN,
              "gzip_bytes": len(gz), "gzip_sha256": hashlib.sha256(gz).hexdigest(),
              "raw_bytes": len(raw), "raw_sha256": hashlib.sha256(raw).hexdigest()}
    print("GOAL4AJ_GEN25_G4_ARTIFACT_ACTUAL=" + json.dumps(actual, sort_keys=True, separators=(",", ":")), flush=True)
    return raw.decode("utf-8")


def source_locks() -> dict:
    return {"gen24_run": GEN24_RUN, "gen24_job": GEN24_JOB,
            "gen24_artifact_id": GEN24_ARTIFACT_ID,
            "gen24_artifact_zip_sha256": GEN24_ARTIFACT_ZIP_SHA256,
            "gen24_canonical_sha256": GEN24_CANONICAL,
            "gen24_gzip_sha256": GZIP_SHA256, "candidate_sha256": Q_SHA,
            "locator_blob_sha1": LOCATOR_BLOB,
            "locator_canonical_sha256": LOCATOR_CANONICAL,
            "strict_curve_packet_sha256": STRICT_PACKET}


def shard_mode(shard: int, artifact_dir: Path, outdir: Path) -> None:
    if not 0 <= shard < SHARD_COUNT:
        raise SystemExit("invalid shard")
    assert git_blob(BASE) == BASE_BLOB and git_blob(LOCATOR) == LOCATOR_BLOB
    base = runpy.run_path(str(BASE))
    qrat = load_artifact_candidate(artifact_dir)
    buf = io.StringIO()
    with redirect_stdout(buf):
        locns = runpy.run_path(str(LOCATOR))
    loc = locns["out"]; curves = locns["curves"]
    assert loc["canonical_sha256"] == LOCATOR_CANONICAL
    assert loc["strict_curve_packet_sha256"] == STRICT_PACKET
    selected = [pair for pos, pair in enumerate(EXPECTED) if pos % SHARD_COUNT == shard]
    assert len(selected) == 3
    rows = [base["run_condition"](qrat, curves, idx, mult) for idx, mult in selected]
    all_pass = all(r["exact_check_pass"] for r in rows)
    report = {"schema":"STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_ALL27_EXACT_STRICT_GEN25_G4_SHARD_V1",
              "source_locks":source_locks(), "shard_index":shard, "shard_count":SHARD_COUNT,
              "expected_condition_count":3, "conditions":rows,
              "all_shard_conditions_pass":all_pass,
              "literal_q_numerator_materialized":False, "literal_F_B_materialized":False,
              "local_evaluations_computed":False, "brauer_manin_obstruction_obtained":False,
              "E1_proved":False, "stage35_closed":False, "theorem_credit":False, "endpoint_credit":False}
    report["canonical_sha256"] = csha(report)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir/"shard.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("GOAL4AJ_GEN25_G4_SHARD_JSON="+json.dumps(report,sort_keys=True,separators=(",",":")),flush=True)
    print("GOAL4AJ_GEN25_G4_SHARD=DONE",flush=True)
    if not all_pass:
        raise SystemExit("gen25-g4 exact strict FAIL")


def aggregate_mode(indir: Path, outdir: Path) -> None:
    reports=[json.loads(p.read_text(encoding="utf-8")) for p in indir.rglob("shard.json")]
    if len(reports)!=SHARD_COUNT: raise SystemExit(f"expected {SHARD_COUNT} shard reports, got {len(reports)}")
    by={int(r["shard_index"]):r for r in reports}
    if set(by)!=set(range(SHARD_COUNT)): raise SystemExit("gen25-g4 shard coverage mismatch")
    observed=[]
    for s in range(SHARD_COUNT):
        r=by[s]
        if r["schema"]!="STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_ALL27_EXACT_STRICT_GEN25_G4_SHARD_V1": raise SystemExit("shard schema mismatch")
        if r["source_locks"]!=source_locks(): raise SystemExit("shard source-lock mismatch")
        for row in r["conditions"]: observed.append((int(row["strict_index_1based"]),int(row["multiplicity"]),bool(row["exact_check_pass"])))
    pairs=[(i,m) for i,m,_ in observed]
    coverage=len(observed)==27 and len(set(pairs))==27 and set(pairs)==set(EXPECTED)
    all_pass=coverage and all(p for _,_,p in observed)
    route="ALL_27_STRICT_EXACT_PASS_DIVISOR_TARGET_REPLAY_READY" if all_pass else "ALL_27_STRICT_EXACT_REPLAY_NOT_CLOSED"
    report={"schema":"STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_ALL27_EXACT_STRICT_GEN25_G4_AGGREGATE_V1",
            "source_locks":source_locks(), "shard_count":SHARD_COUNT,
            "strict_condition_count":27, "strict_total_multiplicity":202,
            "exact_condition_coverage":coverage, "all_27_strict_exact_pass":all_pass,
            "ordered_conditions":[{"strict_index_1based":i,"multiplicity":m} for i,m in EXPECTED],
            "route_result":route, "literal_q_numerator_materialized":False,
            "literal_F_B_materialized":False, "local_evaluations_computed":False,
            "brauer_manin_obstruction_obtained":False, "E1_proved":False,
            "stage35_closed":False, "theorem_credit":False, "endpoint_credit":False}
    report["canonical_sha256"]=csha(report)
    outdir.mkdir(parents=True,exist_ok=True)
    (outdir/"certificate.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("GOAL4AJ_GEN25_G4_AGGREGATE_JSON="+json.dumps(report,sort_keys=True,separators=(",",":")),flush=True)
    print("GOAL4AJ_GEN25_G4_AGGREGATE=DONE",flush=True)
    if not all_pass: raise SystemExit("gen25-g4 aggregate not all-pass")


def main() -> None:
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="mode",required=True)
    s=sub.add_parser("shard"); s.add_argument("--shard",type=int,required=True); s.add_argument("--artifact-dir",type=Path,required=True); s.add_argument("--output-dir",type=Path,required=True)
    a=sub.add_parser("aggregate"); a.add_argument("--input-dir",type=Path,required=True); a.add_argument("--output-dir",type=Path,required=True)
    ns=ap.parse_args()
    if ns.mode=="shard": shard_mode(ns.shard,ns.artifact_dir,ns.output_dir)
    else: aggregate_mode(ns.input_dir,ns.output_dir)

if __name__=="__main__": main()
