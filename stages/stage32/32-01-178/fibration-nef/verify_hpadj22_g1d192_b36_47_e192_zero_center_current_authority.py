#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
E192 = HERE / "verify_hpadj21_g1d192_b36_47_e192_zero_center_refinement.py"
E192_BLOB = "ed4094cc3e951cc6ad89ecc8b18be22c809bda5b"
DIRECT_REL = Path("stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py")
DIRECT_BLOB = "e965ab0a6ea51938006882ca2110016f48b3768e"
AGG_REL = Path("stages/stage32/management/hpadj22-direct-full178/HPADJ22-DIRECT-FULL178-RETAINED.json")
AGG_BLOB = "60ca65208b774cc79c646c46c6780e7028a29845"
HPADJ22_SOURCE_HEAD = "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
OLD_GLOBAL = 138652739800650593494
ROW_INDEX = 22
BAND = 3
TARGET = {"row_id": "g1-d192", "g": 1, "d": 192, "a": 45, "b": 45, "c": 60, "e": 192, "sa": 3, "sbc": 7}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def counter_from_tiers(tiers) -> Counter[int]:
    out: Counter[int] = Counter()
    for q, mult in tiers:
        out[int(q)] += int(mult)
    return out


def grouped_h(e192) -> tuple[Counter[int], Counter[int], Counter[tuple[int, int, int]]]:
    h = e192.unequal_positive_H_hist(b=TARGET["b"], c=TARGET["c"])
    by_r = (Counter(), Counter())
    for (t, q, r), mult in h.items():
        by_r[int(r)][int(q)] += int(mult)
    return by_r[0], by_r[1], h


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    direct_path = args.repo_root / DIRECT_REL
    agg_path = args.repo_root / AGG_REL
    req(direct_path.is_file() and blob(direct_path) == DIRECT_BLOB, "current direct-count source drift")
    req(E192.is_file() and blob(E192) == E192_BLOB, "retained e192 zero-center source drift")
    req(agg_path.is_file() and blob(agg_path) == AGG_BLOB, "V44/V45 HPADJ22 aggregate drift")

    agg = json.loads(agg_path.read_text())
    req(int(agg["result"]["direct_hpadj22_full178_upper_bound"]) == OLD_GLOBAL, "global HPADJ22 bound drift")
    req(agg["coverage"] == {
        "bands": 8, "cells": 1424, "gaps": 0,
        "new_direct_bands": [0,1,2,3,4,5,6], "overlaps": 0,
        "retained_complete_bands": [7], "rows_per_band": 178
    }, "FULL178 HPADJ22 coverage drift")
    req(agg["source_locks"]["hpadj22_source_head"] == HPADJ22_SOURCE_HEAD, "HPADJ22 source-head drift")

    direct = load_module(direct_path, "stage32_178_hpadj22_current_direct")
    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx

    row_id, g0, d0 = rows[ROW_INDEX]
    req((row_id, int(g0), int(d0)) == (TARGET["row_id"], TARGET["g"], TARGET["d"]), "row identity drift")
    req(tuple(old.PLANNED[BAND]) == (36, 47), "target b-band drift")

    joint = bc.build_joint_bc_shard(old.HMAX, 36, 47)
    got = direct.direct_count(old, ctx, joint, BAND, ROW_INDEX)
    req(got["row"] == {"index": ROW_INDEX, "row_id": TARGET["row_id"], "g": 1, "d": 192}, "direct row drift")

    e192 = load_module(E192, "stage32_178_e192_zero_center_for_hpadj22")
    fast = e192.load_module(e192.FAST, "stage32_178_e192_fast_for_hpadj22")
    cert = fast.load_certificate()

    ah = e192.positive_A_hist(TARGET["a"])
    aprof = counter_from_tiers(profiles[TARGET["a"]][TARGET["sa"]])
    req(ah == aprof, "A support-3 profile is not exactly the retained HPADJ22 qA profile")

    h0, h1, hh = grouped_h(e192)
    for r, subset in enumerate((h0, h1)):
        full = Counter({int(q): int(v) for q, v in joint[TARGET["b"]][TARGET["c"]][TARGET["sbc"]][r].items() if int(v)})
        req(all(int(mult) <= int(full.get(q, 0)) for q, mult in subset.items()),
            f"unequal H subset not embedded in HPADJ22 joint histogram parity={r}")

    g, d, e = TARGET["g"], TARGET["d"], TARGET["e"]
    h = d // 2
    K = counter.ceil_div(d - 16*g + 16, 4)
    ca = counter.component_a(d, TARGET["a"])
    c3 = counter.component3(d, TARGET["b"], TARGET["c"])
    srem = min(16, d) + ca + c3
    es = bnd.eligible_e(
        counter, d, g, h, TARGET["a"], TARGET["b"], TARGET["c"],
        TARGET["sa"] + TARGET["sbc"], srem, K
    )
    req(e in es, "e192 is not an HPADJ22 eligible-e member for target aggregate")

    caps = bnd.x4_caps(h16, h, g, TARGET["b"], TARGET["c"])
    xr = h16.a0_interval(h, g, TARGET["b"], TARGET["c"])
    req(xr is not None, "target has no x4 interval")
    threshold8 = d*d + 16*d
    genus_budget = Fraction(d*d, 16) + d + 2 - 2*g
    minpen = Fraction(3, 5)

    xcache: dict[tuple[int, int], tuple[int, ...]] = {}
    def current_x4(qa: int, r: int) -> tuple[int, ...]:
        key = (qa, r)
        if key not in xcache:
            xs = []
            for x4 in range(xr[0], xr[1] + 1):
                if (x4 & 1) != r:
                    continue
                room = -int(h16.f0(h, g, TARGET["b"], TARGET["c"], x4))
                req(room >= 0, "x4 interval contains negative room")
                if qa <= room // 138:
                    xs.append(x4)
            xcache[key] = tuple(xs)
            req(len(xcache[key]) == int(bnd.survivor_count(caps, r, qa)),
                f"x4 survivor-count adapter drift qa={qa} r={r}")
        return xcache[key]

    old_subset = 0
    refined_subset = 0
    accepted_prefixes = 0
    strict_prefixes = 0
    transition = Counter()

    for qa, ma in ah.items():
        for (t, qh, r), mh in hh.items():
            if 8 * (int(qa) + int(qh)) > threshold8:
                continue
            p = fast.parity_witness((TARGET["a"], TARGET["b"], TARGET["c"], int(t), 0, e, d))
            req(p == (1, 1, 0, 0, 0), f"zero-center parity drift t={t}: {p}")
            req(fast.membership_ok(cert, (TARGET["a"], TARGET["b"], TARGET["c"], int(t), 0, e, d) + p),
                f"Picard membership drift t={t}")

            xs = current_x4(int(qa), int(r))
            old_s = len(xs)
            new_s = 0
            for x4 in xs:
                static_rho = Fraction((d//2 - 2*x4 - int(t))**2, 12)
                exact_cut = 2 * (genus_budget - static_rho - minpen)
                qh_limit = exact_cut.numerator // exact_cut.denominator - int(qa)
                if int(qh) <= qh_limit:
                    new_s += 1
            req(0 <= new_s <= old_s, "zero-center refinement weakened HPADJ22 survivor set")
            mult = int(ma) * int(mh)
            old_subset += mult * old_s
            refined_subset += mult * new_s
            accepted_prefixes += mult
            if new_s < old_s:
                strict_prefixes += mult
            transition[(old_s, new_s)] += mult

    reduction = old_subset - refined_subset
    req(reduction > 0, "zero-center condition gives no strict HPADJ22 direct-count reduction")
    old_row = int(got["hpadj22_exact_survivors"])
    req(0 < old_subset <= old_row, "target HPADJ22 subset exceeds direct row count")
    new_row = old_row - reduction
    req(0 <= new_row < old_row, "refined row count did not strictly improve")
    new_global = OLD_GLOBAL - reduction
    req(0 <= new_global < OLD_GLOBAL, "refined global bound did not strictly improve")

    transitions = [
        {"old_x4_survivors": int(k[0]), "new_x4_survivors": int(k[1]), "prefix_multiplicity": str(v)}
        for k, v in sorted(transition.items())
    ]
    out = {
        "schema": "STAGE32_32_01_178_HPADJ22_E192_ZERO_CENTER_CURRENT_AUTHORITY_REFINEMENT_V1",
        "status": "EXACT_CURRENT_HPADJ22_SUBSET_STRICT_REFINEMENT__ZERO_MAIN_CREDIT__HOSTILE_AUDIT_REQUIRED",
        "source_locks": {
            "current_direct_count_blob_sha1": DIRECT_BLOB,
            "current_hpadj22_aggregate_blob_sha1": AGG_BLOB,
            "hpadj22_source_head": HPADJ22_SOURCE_HEAD,
            "historical_hpadj22_worker_blob_sha1": direct.OLD_BLOB,
            "e192_zero_center_refinement_blob_sha1": E192_BLOB
        },
        "target": {
            **TARGET,
            "row_index": ROW_INDEX,
            "band_position": BAND,
            "b_interval": [36, 47]
        },
        "embedding_checks": {
            "A_support3_exact_profile_match": True,
            "H_unequal_support7_pointwise_embedded_in_joint_qBC_parity_histogram": True,
            "e192_in_exact_eligible_e_set": True,
            "x4_survivor_count_exact_adapter": True,
            "hpadj22_joint_qA_qBC_threshold_preserved": True,
            "zero_center_picard_membership_replayed": True
        },
        "result": {
            "old_hpadj22_row_survivors": str(old_row),
            "old_subset_survivors": str(old_subset),
            "refined_subset_survivors": str(refined_subset),
            "exact_survivor_reduction": str(reduction),
            "refined_hpadj22_row_survivors": str(new_row),
            "current_v45_global_upper_bound": str(OLD_GLOBAL),
            "candidate_global_upper_bound_if_promoted": str(new_global),
            "accepted_subset_prefix_multiplicity": str(accepted_prefixes),
            "strict_subset_prefix_multiplicity": str(strict_prefixes),
            "transition_count": len(transitions)
        },
        "transitions": transitions,
        "semantics": {
            "same_current_hpadj22_pre_domain": True,
            "same_hpadj22_joint_qA_qBC_filter": True,
            "same_hpadj22_x4_survivor_rule_before_refinement": True,
            "only_one_exact_e192_unequal_subset_refined": True,
            "all_other_hpadj22_survivors_unchanged": True,
            "additive_cross_route_subtraction": False,
            "replacement_is_subset_refinement_of_current_hpadj22_direct_count": True,
            "main_bound_replacement_performed": False,
            "hostile_audit_required_before_consumption": True
        },
        "firewalls": {
            "main_credit_changed": False,
            "full178_complete": False,
            "theorem_credit_changed": False,
            "effectivity_credit_changed": False,
            "receiver_credit_changed": False,
            "endpoint_credit_changed": False,
            "stage32_closed": False,
            "merge": False
        }
    }
    out["canonical_sha256_without_this_field"] = canonical(out)

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")

    print("HPADJ22_E192_ZERO_CENTER_CURRENT_AUTHORITY=" + json.dumps({
        "row_index": ROW_INDEX,
        "old_row": str(old_row),
        "old_subset": str(old_subset),
        "refined_subset": str(refined_subset),
        "reduction": str(reduction),
        "old_global": str(OLD_GLOBAL),
        "candidate_global": str(new_global),
        "canonical": out["canonical_sha256_without_this_field"]
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
