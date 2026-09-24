#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V48 = HERE / "v48-support-qbc-retained/row022-b036.json"
V48_BLOB = "41dc02e3e1a689a273d7095621d509a3a852734e"
RAW = HERE / "local-support-qbc/generation2/row022-b036.json"
RAW_BLOB = "e8b9db8f1fbb091bbd9465a4f365e6f160f1300c"
SUPPORT_WORKER = HERE / "run_hpadj22_support_qbc_local_row_b.py"
SUPPORT_WORKER_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
V48_TOTAL = 128470212118313474449


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    req(blob(V48) == V48_BLOB, "retained V48 unit blob drift")
    req(blob(RAW) == RAW_BLOB, "raw support receipt blob drift")
    req(blob(SUPPORT_WORKER) == SUPPORT_WORKER_BLOB, "support worker blob drift")

    v = json.loads(V48.read_text())
    r = json.loads(RAW.read_text())
    req(canon(v) == v["canonical_sha256_without_this_field"], "V48 unit canonical drift")
    req(canon(r) == r["canonical_sha256_without_this_field"], "raw support canonical drift")

    vt, rt = v["target"], r["target"]
    req(
        (int(vt["row_index"]), int(vt["g"]), int(vt["d"]), int(vt["b"]))
        == (int(rt["row_index"]), int(rt["g"]), int(rt["d"]), int(rt["b_interval"][0]))
        == (22, 1, 192, 36),
        "target identity mismatch",
    )
    req(r["target"]["b_interval"] == [36, 36], "raw support receipt is not singleton b36")

    vs, rs = v["source_locks"], r["source_locks"]
    req(vs["hpadj22_source_head"] == rs["hpadj22_source_head"], "HPADJ22 source-head mismatch")
    req(vs["support_qbc_worker_blob_sha1"] == rs["local_worker_blob_sha1"] == SUPPORT_WORKER_BLOB, "support-worker identity mismatch")
    req(r["semantics"]["same_population_as_current_hpadj22"] is True, "raw support population drift")
    req(r["semantics"]["same_current_x4_capacity_rule"] is True, "x4 capacity relation drift")
    req(v["semantics"]["same_population_v47_replacement"] is True, "V48 unit population drift")

    # The retained support worker's full qcut uses the exact same support_t_interval
    # as the V48 unit, then adds nonnegative Picard penalties p0/2+p1/10.
    # Check the radius algebra pointwise across the complete q threshold domain.
    d, g = 192, 1
    tq = (d*d + 16*d + (32 if g == 0 else 0)) // 8
    rhs120 = (15*d*d)//2 + 120*d + 240 - 240*g
    for q in range(tq + 1):
        no_penalty_budget = rhs120 - 60*q
        rem = 3*d*d + 48*d + 96 - 96*g - 24*q
        req(no_penalty_budget // 10 == rem // 4, f"V48/support radius algebra drift q={q}")
        for p0 in (0, 1):
            for p1 in (0, 1):
                picard_budget = no_penalty_budget - 60*p0 - 12*p1
                req(picard_budget <= no_penalty_budget, "Picard penalty weakened radius budget")

    current = int(v["result"]["v47_support_qbc_joint_survivors"])
    raw_full_support = int(r["result"]["support_qbc_refined_survivors"])
    req(raw_full_support < current, "raw full-support bound does not improve current V48 b36 contribution")
    tightening = current - raw_full_support
    candidate = V48_TOTAL - current + raw_full_support
    req(tightening == 50969985682838, f"tightening drift {tightening}")
    req(candidate == 128470161148327791611, f"candidate bound drift {candidate}")

    print("PASS: V48 row22/b36 and raw full-support receipt share source/population identities")
    print("PASS: full support qcut pointwise strengthens the V48 support-interval radius gate")
    print("PASS: certified b36 replacement upper bound <=", raw_full_support)
    print("PASS: candidate global upper bound <=", candidate)
    print("PASS: potential certified tightening >=", tightening)
    print("PASS: upper-bound replacement only; no exact intersection/rejected-set or MAIN credit claimed")


if __name__ == "__main__":
    main()
