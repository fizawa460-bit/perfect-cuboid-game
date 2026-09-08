#!/usr/bin/env python3
"""Goal4AJ gen25: exact replay of all 27 strict divisor conditions.

This consumes only the permanent repo-locked degree-31 Q candidate produced by
gen24 and the source-locked retained-140 locator.  It does not rerun any finite
field or CRT computation.  Nine deterministic shards each check three strict
conditions over Q(i,sqrt(2)); aggregate mode verifies exact one-time coverage.

Even all-27 PASS remains diagnostic until the target divisor/no-extra-component
replay is complete.  No literal numerator/F_B/local/BM/E1/Stage35/theorem or
endpoint credit is granted here.
"""
from __future__ import annotations

import argparse
import base64
import bz2
from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import runpy
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24.txt.bz2.b64"
LOCK = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24-materialization.json"
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"

CANDIDATE_BLOB = "9d8b934961f03a423cf940bc95efdffe8e28e0fd"
LOCK_BLOB = "1bc208ed5010ec2d3f50d90b70db3698f860a134"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCK_CANONICAL = "b341897f941e7237f2769e0a94bc906b959f346bde753dcd4d15cbc5e3985e5f"
GEN24_CANONICAL = "9463e3ca0431fbb8310c139481873ddf98122136f360cdac58ecf35eaa325e26"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"
COMPRESSED_SHA = "8ee85c2134e25f3ef2e20ca6d4c71dbb454cb6e95b59e79e668579f659be79e3"
COMPRESSED_BYTES = 31582
Q_SHA = "358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb"
Q_BYTES = 208802
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
SHARD_COUNT = 9
PROCESS_ORDER = [2,7,13,38,40,15,18,19,22,10,12,23,58,60,14,9,17,3,4,5,6,16,24,27,30,65,67]
MULTIPLICITIES = [21,21,18,13,13,12,12,12,12,10,10,10,9,9,4,3,3,1,1,1,1,1,1,1,1,1,1]
EXPECTED = list(zip(PROCESS_ORDER, MULTIPLICITIES))
assert len(EXPECTED) == 27 and sum(MULTIPLICITIES) == 202


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def csha(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_q_candidate() -> str:
    assert git_blob(CANDIDATE) == CANDIDATE_BLOB
    assert git_blob(LOCK) == LOCK_BLOB
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    assert lock["schema"] == "STAGE35_EX_GOAL4AJ_GEN24_PARALLEL_FOUR_PRIME_MATERIALIZATION_REPO_LOCK_V2"
    assert lock["repo_lock_canonical_sha256"] == LOCK_CANONICAL
    assert lock["gen24_canonical_sha256"] == GEN24_CANONICAL
    assert lock["q_candidate_sha256"] == Q_SHA and lock["q_candidate_text_bytes"] == Q_BYTES
    payload = base64.b64decode("".join(CANDIDATE.read_text(encoding="utf-8").split()))
    assert len(payload) == COMPRESSED_BYTES and hashlib.sha256(payload).hexdigest() == COMPRESSED_SHA
    raw = bz2.decompress(payload)
    assert len(raw) == Q_BYTES and hashlib.sha256(raw).hexdigest() == Q_SHA
    return raw.decode("utf-8")


def ffrac(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"({x.numerator}/{x.denominator})"


def kexpr(x) -> str:
    a, b, c, d = x.coeffs()
    parts = []
    for q, u in ((a, ""), (b, "ii"), (c, "ss"), (d, "isv")):
        if q == 0:
            continue
        qs = ffrac(q)
        parts.append(qs if not u else f"({qs})*{u}")
    return "+".join(parts).replace("+-", "-") if parts else "0"


def row_expr_exact(row) -> str:
    parts = []
    for name, x in zip(NAMES, row):
        ex = kexpr(x)
        if ex != "0":
            parts.append(f"({ex})*{name}")
    return "+".join(parts).replace("+-", "-")


def singular_prelude(qrat: str) -> str:
    return r'''option(redSB);
LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
number ss=u-u^3;
number isv=ii*ss;
ideal surf=
  a1^2+a2^2-b3^2,
  a2^2+a3^2-b1^2,
  a1^2+a3^2-b2^2,
  a1^2+a2^2+a3^2-c^2;
matrix J=jacob(surf);
ideal Sing=minor(J,4);
proc contained(ideal A, ideal B)
{
  ideal G=std(B); int j;
  for (j=1; j<=size(A); j++) { if (reduce(A[j],G)!=0) { return(0); } }
  return(1);
}
proc equalideal(ideal A, ideal B) { return(contained(A,B)==1 && contained(B,A)==1); }
proc sympow(ideal P, int m)
{
  ideal Sk=std(surf+P); ideal Candidate; ideal Sn; list SatL; int kk;
  for (kk=2; kk<=m; kk++)
  {
    Candidate=surf+Sk*P; SatL=sat(Candidate,Sing); Sn=std(SatL[1]); Sk=Sn;
  }
  list StableL=sat(Sk,Sing); ideal Stable=std(StableL[1]);
  if (equalideal(Sk,Stable)!=1) { ERROR("symbolic power not saturation-stable"); }
  return(Sk);
}
ideal SurfStd=std(surf);
''' + "\npoly qNum=" + qrat + ";\nqNum=reduce(qNum,SurfStd);\n"


def run_condition(qrat: str, curves, strict_index: int, mult: int) -> dict:
    eqs = ",".join(row_expr_exact(r) for r in curves[strict_index - 1])
    tag = f"S{strict_index}_M{mult}"
    sing = singular_prelude(qrat)
    sing += f"ideal P={eqs};\nideal T=std(sympow(P,{mult}));\npoly rr=reduce(qNum,T);\n"
    sing += f'if (rr==0) {{ print("GOAL4AJ_GEN25_{tag}=PASS"); }} else {{ print("GOAL4AJ_GEN25_{tag}=FAIL"); }}\nquit;\n'
    started = time.perf_counter()
    with tempfile.TemporaryDirectory() as td:
        sf = Path(td) / f"gen25-{tag}.sing"
        sf.write_text(sing, encoding="utf-8")
        try:
            cp = subprocess.run(["Singular", "-q", str(sf)], text=True, capture_output=True, timeout=2400)
            sout, serr, rc, timed_out = cp.stdout, cp.stderr, cp.returncode, False
        except subprocess.TimeoutExpired as exc:
            sout = exc.stdout or ""; serr = exc.stderr or ""; rc = None; timed_out = True
            if isinstance(sout, bytes): sout = sout.decode("utf-8", errors="replace")
            if isinstance(serr, bytes): serr = serr.decode("utf-8", errors="replace")
    elapsed = round(time.perf_counter() - started, 3)
    error_marker = any(t in sout.lower() for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"))
    marker = f"GOAL4AJ_GEN25_{tag}="
    completed = (not timed_out and rc == 0 and not error_marker and marker in sout)
    if not completed:
        print("GOAL4AJ_GEN25_SINGULAR_STDOUT_TAIL=" + json.dumps(sout[-6000:]), flush=True)
        print("GOAL4AJ_GEN25_SINGULAR_STDERR_TAIL=" + json.dumps(serr[-3000:]), flush=True)
        raise SystemExit(f"gen25 exact strict check did not complete: {tag}")
    passed = f"{marker}PASS" in sout
    return {"strict_index_1based": strict_index, "multiplicity": mult, "exact_check_completed": True,
            "exact_check_pass": passed, "elapsed_seconds": elapsed}


def shard_mode(shard: int, outdir: Path) -> None:
    if not 0 <= shard < SHARD_COUNT:
        raise SystemExit("invalid shard")
    assert git_blob(LOCATOR) == LOCATOR_BLOB
    qrat = load_q_candidate()
    buf = io.StringIO()
    with redirect_stdout(buf):
        ns = runpy.run_path(str(LOCATOR))
    loc = ns["out"]; curves = ns["curves"]
    assert loc["canonical_sha256"] == LOCATOR_CANONICAL
    assert loc["strict_curve_packet_sha256"] == STRICT_PACKET
    selected = [pair for pos, pair in enumerate(EXPECTED) if pos % SHARD_COUNT == shard]
    assert len(selected) == 3
    rows = [run_condition(qrat, curves, idx, mult) for idx, mult in selected]
    all_pass = all(r["exact_check_pass"] for r in rows)
    report = {
        "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_ALL27_EXACT_STRICT_GEN25_SHARD_V1",
        "source_locks": {"candidate_blob_sha1": CANDIDATE_BLOB, "candidate_sha256": Q_SHA,
                         "materialization_lock_blob_sha1": LOCK_BLOB, "materialization_lock_canonical_sha256": LOCK_CANONICAL,
                         "locator_blob_sha1": LOCATOR_BLOB, "locator_canonical_sha256": LOCATOR_CANONICAL,
                         "strict_curve_packet_sha256": STRICT_PACKET},
        "shard_index": shard, "shard_count": SHARD_COUNT, "expected_condition_count": 3,
        "conditions": rows, "all_shard_conditions_pass": all_pass,
        "literal_q_numerator_materialized": False, "literal_F_B_materialized": False,
        "local_evaluations_computed": False, "brauer_manin_obstruction_obtained": False,
        "E1_proved": False, "stage35_closed": False, "theorem_credit": False, "endpoint_credit": False,
    }
    report["canonical_sha256"] = csha(report)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "shard.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("GOAL4AJ_GEN25_SHARD_JSON=" + json.dumps(report, sort_keys=True, separators=(",", ":")), flush=True)
    print("GOAL4AJ_GEN25_SHARD=DONE", flush=True)
    if not all_pass:
        raise SystemExit("gen25 exact strict FAIL")


def aggregate_mode(indir: Path, outdir: Path) -> None:
    reports = []
    for p in indir.rglob("shard.json"):
        reports.append(json.loads(p.read_text(encoding="utf-8")))
    if len(reports) != SHARD_COUNT:
        raise SystemExit(f"expected {SHARD_COUNT} shard reports, got {len(reports)}")
    by_shard = {int(r["shard_index"]): r for r in reports}
    if set(by_shard) != set(range(SHARD_COUNT)):
        raise SystemExit("gen25 shard coverage mismatch")
    observed = []
    for s in range(SHARD_COUNT):
        r = by_shard[s]
        if r["schema"] != "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_ALL27_EXACT_STRICT_GEN25_SHARD_V1":
            raise SystemExit("shard schema mismatch")
        for row in r["conditions"]:
            observed.append((int(row["strict_index_1based"]), int(row["multiplicity"]), bool(row["exact_check_pass"])))
    pairs = [(i, m) for i, m, _ in observed]
    expected_set = set(EXPECTED)
    exact_coverage = len(observed) == 27 and len(set(pairs)) == 27 and set(pairs) == expected_set
    all_pass = exact_coverage and all(p for _, _, p in observed)
    route = "ALL_27_STRICT_EXACT_PASS_DIVISOR_TARGET_REPLAY_READY" if all_pass else "ALL_27_STRICT_EXACT_REPLAY_NOT_CLOSED"
    report = {
        "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_ALL27_EXACT_STRICT_GEN25_AGGREGATE_V1",
        "source_locks": {"candidate_blob_sha1": CANDIDATE_BLOB, "candidate_sha256": Q_SHA,
                         "materialization_lock_blob_sha1": LOCK_BLOB, "materialization_lock_canonical_sha256": LOCK_CANONICAL,
                         "locator_blob_sha1": LOCATOR_BLOB, "locator_canonical_sha256": LOCATOR_CANONICAL,
                         "strict_curve_packet_sha256": STRICT_PACKET},
        "shard_count": SHARD_COUNT, "strict_condition_count": 27, "strict_total_multiplicity": 202,
        "exact_condition_coverage": exact_coverage, "all_27_strict_exact_pass": all_pass,
        "ordered_conditions": [{"strict_index_1based": i, "multiplicity": m} for i, m in EXPECTED],
        "route_result": route,
        "literal_q_numerator_materialized": False, "literal_F_B_materialized": False,
        "local_evaluations_computed": False, "brauer_manin_obstruction_obtained": False,
        "E1_proved": False, "stage35_closed": False, "theorem_credit": False, "endpoint_credit": False,
    }
    report["canonical_sha256"] = csha(report)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "certificate.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("GOAL4AJ_GEN25_AGGREGATE_JSON=" + json.dumps(report, sort_keys=True, separators=(",", ":")), flush=True)
    print("GOAL4AJ_GEN25_AGGREGATE=DONE", flush=True)
    if not all_pass:
        raise SystemExit("gen25 aggregate not all-pass")


def main() -> None:
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="mode", required=True)
    s = sub.add_parser("shard"); s.add_argument("--shard", type=int, required=True); s.add_argument("--output-dir", type=Path, required=True)
    a = sub.add_parser("aggregate"); a.add_argument("--input-dir", type=Path, required=True); a.add_argument("--output-dir", type=Path, required=True)
    ns = ap.parse_args()
    if ns.mode == "shard": shard_mode(ns.shard, ns.output_dir)
    else: aggregate_mode(ns.input_dir, ns.output_dir)

if __name__ == "__main__":
    main()
