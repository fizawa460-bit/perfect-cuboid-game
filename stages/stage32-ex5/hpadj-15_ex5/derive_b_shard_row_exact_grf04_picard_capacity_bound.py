#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import importlib.util
import json
import zlib
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "stages/stage32-ex5/hpadj-14_ex5/derive_row_exact_grf04_picard_capacity_bound.py"
CERT = HERE / "HPADJ08-B-SHARD-ROW-MASS-CERTIFICATE.json"

PARENT_BLOB = "16051646826c452d4385e49f2643ac0b394af3e0"
CERT_BLOB = "8342939205aababa6f082c647dd14bc080131f62"
CERT_CANON = "efc03af770867cfab81ead20f189af30c5dc28a5a4e7dd8af7e28af06fa35efc"
CERT_PAYLOAD_SHA = "f47da29590aaf4141516593867c14d48c51703503f107825a9ee4f04231cad2e"
SOURCE_RUN_ID = 34935380596
SOURCE_HEAD = "b11a9820af4a02148112a6ae235bc3a51d134ef2"
AUDITED_HPADJ08_HEAD = "36eab50192cf80ec5ed48aba40f4a56076759fea"
V35_SOURCE_HEAD = "a01dfd4173ae46c7d51e4f6f9ecdad8b4755f90c"
V35_BLOB = "a203df7b15a9cc655b78aa70b849933b98404a2d"
V35_CANON = "221f7bc44989130de39b639d4a0a0af85a056ea0ab9461e61a1cb24be907d5b5"
HPADJ14_BENCHMARK = 463577241806597722598
PLANNED = ((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_parent():
    req(PARENT.is_file(), "missing HPADJ14 parent")
    req(git_blob(PARENT) == PARENT_BLOB, "HPADJ14 parent blob drift")
    spec = importlib.util.spec_from_file_location("hpadj14_locked_for_hpadj15", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ14 parent")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_certificate(parent) -> dict[tuple[tuple[int,int], int, int], int]:
    req(CERT.is_file() and git_blob(CERT) == CERT_BLOB, "HPADJ08 b-shard certificate blob drift")
    cert = json.loads(CERT.read_text())
    req(cert.get("canonical_sha256_without_this_field") == CERT_CANON, "certificate stored canonical drift")
    req(canonical(cert) == CERT_CANON, "certificate canonical drift")
    req(cert.get("source_run_id") == SOURCE_RUN_ID, "certificate source run drift")
    req(cert.get("source_exact_head") == SOURCE_HEAD, "certificate source head drift")
    req(cert.get("audited_hpadj08_head") == AUDITED_HPADJ08_HEAD, "certificate audited head drift")
    req(cert.get("aggregate_rejected_terminals") == parent.EXPECTED_HPADJ08_REJECTED,
        "certificate rejected aggregate drift")
    payload = cert.get("payload", {})
    req(payload.get("encoding") == "zlib+base64", "certificate payload encoding drift")
    raw = zlib.decompress(base64.b64decode(payload["data"]))
    req(hashlib.sha256(raw).hexdigest() == CERT_PAYLOAD_SHA, "certificate payload sha drift")
    req(payload.get("json_sha256") == CERT_PAYLOAD_SHA, "certificate stored payload sha drift")
    data = json.loads(raw)
    row_keys = [tuple(map(int, x)) for x in data["row_keys"]]
    req(len(row_keys) == 178 and len(set(row_keys)) == 178, "certificate row-key coverage")
    out = {}
    shard_totals = {}
    for shard in data["rejected_by_shard"]:
        interval = tuple(map(int, shard["b_interval"]))
        req(interval in PLANNED, f"unexpected certificate shard {interval}")
        vals = [int(v) for v in shard["rejected_terminals"]]
        req(len(vals) == len(row_keys), f"certificate row count {interval}")
        shard_totals[interval] = sum(vals)
        for (g,d), value in zip(row_keys, vals):
            key = (interval, g, d)
            req(key not in out, f"duplicate certificate key {key}")
            out[key] = value
    req(set(shard_totals) == set(PLANNED), "certificate shard coverage")
    metadata = {tuple(map(int, x["b_interval"])): int(x["rejected_terminals"])
                for x in cert["coverage"]["shard_metadata"]}
    req(metadata == shard_totals, "certificate shard metadata totals")
    req(sum(out.values()) == parent.EXPECTED_HPADJ08_REJECTED, "certificate payload aggregate")
    return out


def shard_for_b(b: int) -> tuple[int,int]:
    if b <= 83:
        lo = (b // 12) * 12
        return (lo, lo + 11)
    return (84, 96)


def exact_pre_shard_caps(parent, counter):
    manifest = counter.load_locked_json(
        parent.MANIFEST, parent.LOCKS["manifest_blob"], parent.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    H = max(d // 2 for _, _, d in rows)
    BC = counter.build_bc_exact_parity(H)
    result = []
    total_terms = total_blocks = 0

    for row_id, g, d in rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = counter.ceil_div(d - 16*g + 16, 4)
        A = [[counter.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
        diffs = {interval: defaultdict(int) for interval in PLANNED}
        for b in range(h + 1):
            diff = diffs[shard_for_b(b)]
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv):
                    continue
                c3 = counter.component3(d, b, c)
                if c3 < 0:
                    continue
                for a in range(h + 1):
                    avec = A[a]
                    if not any(avec):
                        continue
                    M = a + b + c
                    ca = counter.component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3
                    scount = [0 for _ in range(11)]
                    for sbc, pair in enumerate(bcv):
                        left = int(pair[0]) + int(pair[1])
                        if not left:
                            continue
                        for sa, right in enumerate(avec):
                            if right:
                                scount[sbc + sa] += left * right
                    for support, count in enumerate(scount):
                        if not count:
                            continue
                        qneed = K - support
                        if qneed > 0 and srem < qneed:
                            continue
                        lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
                        upper = min((19*d)//5, 3*d, 3*d - (b-c))
                        if lower > upper:
                            continue
                        excluded = set()
                        e_n358 = 3*d - (b-c)
                        if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                            excluded.add(e_n358)
                        if g == 1 and d == 8:
                            excluded.add(8)
                        lo = lower if lower % 2 == 0 else lower + 1
                        hi = upper if upper % 2 == 0 else upper - 1
                        if lo > hi:
                            continue
                        diff[lo] += count
                        diff[hi + 2] -= count
                        for ex in excluded:
                            if lo <= ex <= hi and ex % 2 == 0:
                                diff[ex] -= count
                                diff[ex + 2] += count
        for interval in PLANNED:
            diff = diffs[interval]
            caps = {}
            running = 0
            if diff:
                for e in range(min(diff), max(diff) + 1, 2):
                    running += diff.get(e, 0)
                    if running:
                        B = 19*d - 5*e + 1
                        req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,interval,e,B)}")
                        caps[e] = running
            pre_blocks = sum(caps.values())
            pre_terms = sum(n * (19*d - 5*e + 1) for e, n in caps.items())
            total_blocks += pre_blocks
            total_terms += pre_terms
            result.append({"row_id":row_id,"g":g,"d":d,"b_interval":interval,
                           "pre_blocks":pre_blocks,"pre_terms":pre_terms,"caps":caps})
    req(len(result) == 178 * len(PLANNED), "pre shard-row count")
    req(total_terms == parent.EXPECTED_PRE_TERMS, "pre terminal aggregate")
    req(total_blocks == parent.EXPECTED_PRE_BLOCKS, "pre block aggregate")
    return result


def main() -> None:
    parent = load_parent()
    req(parent.V35_BENCHMARK == 511195899564352597589, "HPADJ14 V35 benchmark drift")
    req(parent.LOCKS["v35_blob"] == V35_BLOB, "HPADJ14 V35 blob lock drift")
    req(parent.LOCKS["v35_canonical"] == V35_CANON, "HPADJ14 V35 canonical lock drift")
    rejected = load_certificate(parent)
    counter = parent.load_counter()
    pre = exact_pre_shard_caps(parent, counter)

    survivor_mass = block_upper = greedy_total = removed_total = candidate = 0
    strict_greedy = strict_removed = nonempty = 0
    diagnostic = hashlib.sha256()
    seen = set()
    for rec in pre:
        g, d = int(rec["g"]), int(rec["d"])
        interval = tuple(rec["b_interval"])
        key = (interval, g, d)
        req(key in rejected, f"missing rejection certificate key {key}")
        seen.add(key)
        R = int(rejected[key])
        pre_terms, pre_blocks = int(rec["pre_terms"]), int(rec["pre_blocks"])
        req(0 <= R <= pre_terms, f"rejection exceeds pre mass {key}")
        M = pre_terms - R
        survivor_mass += M
        if pre_blocks == 0:
            req(R == 0 and M == 0 and not rec["caps"], f"empty shard mismatch {key}")
            greedy = removed = upper = 0
        else:
            nonempty += 1
            greedy, used = parent.greedy_max_blocks_for_mass(rec["caps"], d, M)
            req(used <= M, f"greedy mass overflow {key}")
            bmax = max(19*d - 5*int(e) + 1 for e, cap in rec["caps"].items() if int(cap) > 0)
            removed = pre_blocks - (R + bmax - 1) // bmax
            req(removed >= 0, f"negative removed-block cap {key}")
            upper = min(greedy, removed)
            strict_greedy += int(greedy < removed)
            strict_removed += int(removed < greedy)
        c = parent.block_survivor_count(g, d)
        row_candidate = c * upper
        candidate += row_candidate
        block_upper += upper
        greedy_total += greedy
        removed_total += removed
        compact = {"b_interval":list(interval),"g":g,"d":d,"pre_terms":pre_terms,
                   "pre_blocks":pre_blocks,"rejected_terms":R,"survivor_mass":M,
                   "greedy_block_upper":greedy,"removed_terminal_block_upper":removed,
                   "combined_block_upper":upper,"grf04_picard_survivors_per_block_upper":c,
                   "candidate_upper":row_candidate}
        diagnostic.update(json.dumps(compact, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(seen == set(rejected), "certificate/pre key-set mismatch")
    req(survivor_mass == parent.EXPECTED_SURVIVOR_ENVELOPE, "post-HPADJ08 survivor aggregate")
    req(candidate <= HPADJ14_BENCHMARK, "b-shard refinement weakened HPADJ14")
    out = {
        "schema":"STAGE32EX5_HPADJ15_B_SHARD_ROW_EXACT_GRF04_PICARD_CAPACITY_BOUND_V1",
        "status":"B_SHARD_ROW_EXACT_GRF04_PICARD_CAPACITY_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "route_id":"HPADJ-15_ex5",
        "source_locks":{"hpadj14_parent_blob_sha1":PARENT_BLOB,
                        "hpadj08_b_shard_certificate_blob_sha1":CERT_BLOB,
                        "hpadj08_b_shard_certificate_canonical_sha256":CERT_CANON,
                        "hpadj08_source_run_id":SOURCE_RUN_ID,"hpadj08_source_exact_head":SOURCE_HEAD,
                        "hpadj08_hostile_audited_head":AUDITED_HPADJ08_HEAD,
                        "main_v35_exact_source_head":V35_SOURCE_HEAD,"main_v35_candidate_blob_sha1":V35_BLOB,
                        "main_v35_candidate_canonical_sha256":V35_CANON},
        "exact_population_adapter":{"full178_rows":178,"historical_b_shards":len(PLANNED),
                                    "row_shard_cells":178*len(PLANNED),"nonempty_pre_shard_cells":nonempty,
                                    "pre_hpadj08_replay_domain_terminals":parent.EXPECTED_PRE_TERMS,
                                    "pre_hpadj08_x4_complete_blocks":parent.EXPECTED_PRE_BLOCKS,
                                    "hpadj08_exact_square_rejected_terminals":parent.EXPECTED_HPADJ08_REJECTED,
                                    "post_hpadj08_x4_complete_survivor_mass":survivor_mass,
                                    "rejection_mass_known_exactly_by_g_d_and_b_shard":True,
                                    "pre_hpadj08_g_d_bshard_e_capacities_recomputed_exactly":True},
        "optimization":{"aggregate_greedy_mass_block_upper":greedy_total,
                        "aggregate_removed_terminal_block_upper":removed_total,
                        "aggregate_combined_block_upper":block_upper,
                        "cells_where_greedy_mass_is_stricter":strict_greedy,
                        "cells_where_removed_terminal_cap_is_stricter":strict_removed,
                        "diagnostic_stream_sha256":diagnostic.hexdigest()},
        "candidate_bound":{"current_audited_main_upper_bound":parent.V34_AUDITED_MAIN,
                           "main_v35_candidate_upper_bound":parent.V35_BENCHMARK,
                           "hpadj14_candidate_upper_bound":HPADJ14_BENCHMARK,
                           "hpadj15_candidate_upper_bound":candidate,
                           "improvement_vs_hpadj14":HPADJ14_BENCHMARK-candidate,
                           "strict_improvement_vs_hpadj14":candidate<HPADJ14_BENCHMARK,
                           "composition_if_consumed":"MIN_OF_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_SUBTRACTION"},
        "semantics":{"same_x4_direct_grf04_picard_intersection":True,"statistical_independence_assumed":False,
                     "hpadj08_rejection_used_as_whole_x4_blocks":True,
                     "b_shard_rejection_mass_is_historical_exact_evidence":True,
                     "e_level_rejection_identity_claimed":False,"surviving_identity_set_claimed":False,
                     "main_consumption_performed":False,"hostile_audit_required_before_main_handoff_or_consumption":True,
                     "heavy_run_required":False,"new_heavy_run_used":False},
        "firewalls":{"stage32_main_pruning_credit":False,"current_main_incremental_credit":False,
                     "full178_complete":False,"effectivity_credit":False,"receiver_credit":False,
                     "theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_credit":False,
                     "heavy_run_armed":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


if __name__ == "__main__":
    main()
