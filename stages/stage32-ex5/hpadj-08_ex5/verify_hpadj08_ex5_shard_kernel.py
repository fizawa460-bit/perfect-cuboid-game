#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WORKER = HERE / "hpadj08_ex5_full178_b_shard.py"
CONTRACT = HERE / "FULL178-SCALEOUT-CONTRACT.json"
EXPECTED_WORKER_BLOB = "c5fc340ea734dfc54436f124bb302c1ec6c5677c"
EXPECTED_CONTRACT_BLOB = "fdc43237b84c00e615147b52f8a1f9d8d41ed5de"
EXPECTED_CONTRACT_CANON = "23ab8ae0509754f94cdf7cc661e18e692ec2af3f20a2653d0d92c1a8ff5fa84b"
EXPECTED_PARTITION = ((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))


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


def load_worker():
    spec = importlib.util.spec_from_file_location("stage32ex5_hpadj08_worker", WORKER)
    req(spec is not None and spec.loader is not None, "worker import spec")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def brute_bc(mod, H: int):
    out = [[[defaultdict(int) for _ in range(8)] for __ in range(H + 1)] for ___ in range(H + 1)]
    for x0 in range(H + 1):
        for x1 in range(x0, H + 1):
            for x5 in range(H + 1):
                for x6 in range(H + 1):
                    for x8 in range(H + 1):
                        for x9 in range(H + 1):
                            if x0 == x1 and (x5, x6) > (x8, x9):
                                continue
                            b = x1 + x5 + x9
                            if b > H:
                                continue
                            for x10 in range(H + 1):
                                c = x0 + x6 + x8 + x10
                                if c > H or ((x1 + x8 + x9 + x10) & 1):
                                    continue
                                vals = (x0, x1, x5, x6, x8, x9, x10)
                                s = sum(v > 0 for v in vals)
                                q = mod.qcap(sum(v * v for v in vals))
                                out[b][c][s][q] += 1
    return out


def check_small_h(mod) -> None:
    old_h = mod.HMAX
    try:
        mod.HMAX = 4
        fast = mod.build_bc_shard(0, 4)
        brute = brute_bc(mod, 4)
        for b in range(5):
            for c in range(5):
                for s in range(8):
                    req(dict(fast[b][c][s]) == dict(brute[b][c][s]), f"H4 BC-Q mismatch {(b,c,s)}")
    finally:
        mod.HMAX = old_h


def check_pairs_gt(mod) -> None:
    a = mod.hist({0: 2, 3: 4, mod.OVERFLOW: 5})
    b = mod.hist({1: 7, 4: 11, mod.OVERFLOW: 13})
    direct = 0
    for qa, ca in ((0,2),(3,4),(mod.OVERFLOW,5)):
        for qb, cb in ((1,7),(4,11),(mod.OVERFLOW,13)):
            if qa + qb > 4:
                direct += ca * cb
    req(mod.pairs_gt(a, b, 4) == direct, "pairs_gt exactness")


def main() -> None:
    req(git_blob(WORKER) == EXPECTED_WORKER_BLOB, "worker blob drift")
    req(git_blob(CONTRACT) == EXPECTED_CONTRACT_BLOB, "contract blob drift")
    co = json.loads(CONTRACT.read_text(encoding="utf-8"))
    req(co.get("canonical_sha256_without_this_field") == EXPECTED_CONTRACT_CANON, "contract stored canonical")
    req(canonical(co) == EXPECTED_CONTRACT_CANON, "contract canonical replay")
    planned = tuple(tuple(x) for x in co["execution_partition"]["planned_shards"])
    req(planned == EXPECTED_PARTITION, "planned shard partition")
    flat = [b for lo, hi in planned for b in range(lo, hi + 1)]
    req(flat == list(range(97)), "partition exact union 0..96")
    req(len(flat) == len(set(flat)), "partition overlap")

    mod = load_worker()
    req(tuple(mod.PLANNED) == EXPECTED_PARTITION, "worker partition drift")
    req(mod.HMAX == 96 and mod.QCAP == 4992 and mod.OVERFLOW == 4993, "worker H/Q constants")
    req((192 * 192 + 16 * 192) // 8 == mod.QCAP, "g1 d192 cutoff cap")
    req((176 * 176 + 16 * 176 + 32) // 8 < mod.QCAP, "g0 cutoff below cap")
    check_pairs_gt(mod)
    check_small_h(mod)
    print("PASS HPADJ-08_ex5 shard kernel: source locks, exact b-union, Q cap, pairs_gt, H=4 independent BC-Q replay")


if __name__ == "__main__":
    main()
