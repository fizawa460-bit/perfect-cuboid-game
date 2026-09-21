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
PARENT = HERE / "verify_hpadj22_e192_zero_center_single_witness.py"
PARENT_BLOB = "5e54175ac7ef5983d639f1657f7878142d3bd5dc"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    req(PARENT.is_file() and blob(PARENT) == PARENT_BLOB, "single-witness parent drift")
    p = load_module(PARENT, "stage32_178_hpadj22_family_parent")

    direct_path = args.repo_root / p.DIRECT_REL
    req(direct_path.is_file() and blob(direct_path) == p.DIRECT_BLOB, "current direct-count source drift")
    direct = load_module(direct_path, "stage32_178_hpadj22_family_direct")
    old = direct.load_old(args.source_root)

    bc = old.load_bchunk()
    bnd = bc.load_bound()
    h21 = bnd.load_module(bnd.H21, bnd.H21_BLOB, "stage32_178_family_h21")
    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "stage32_178_family_h15")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    row_id, g0, d0 = rows[p.ROW_INDEX]
    req((row_id, int(g0), int(d0)) == ("g1-d192", 1, 192), "target row identity drift")

    W = dict(p.W)
    g, d = W["g"], W["d"]
    h = d // 2

    # One fixed canonical unequal H tuple.
    req(0 < W["x0"] < W["x1"], "H canonical branch drift")
    req(all(W[k] > 0 for k in ("x0","x1","x5","x6","x8","x9","x10")), "H support drift")
    req(W["x1"] + W["x5"] + W["x9"] == W["b"], "H b-group drift")
    req(W["x0"] + W["x6"] + W["x8"] + W["x10"] == W["c"], "H c-group drift")
    req(((W["x8"] + W["x10"]) & 1) == ((W["x9"] & 1) ^ (W["x1"] & 1)), "H parity drift")
    r = (W["x0"] ^ W["x1"] ^ W["x9"]) & 1
    qBC = sum(W[k]**2 for k in ("x0","x1","x5","x6","x8","x9","x10"))
    req((r, qBC) == (0, 1609), "fixed H invariant drift")

    support = 10
    K = counter.ceil_div(d - 16*g + 16, 4)
    ca = counter.component_a(d, W["a"])
    c3 = counter.component3(d, W["b"], W["c"])
    srem = min(16, d) + ca + c3
    es = bnd.eligible_e(counter, d, g, h, W["a"], W["b"], W["c"], support, srem, K)
    req(W["e"] in es, "e192 left current HPADJ22 eligible set")

    fast = load_module(p.FAST, "stage32_178_hpadj22_family_fast")
    cert = fast.load_certificate()
    t = W["x0"] + W["x1"] + W["x6"] + W["x9"]
    parity = fast.parity_witness((W["a"], W["b"], W["c"], t, 0, W["e"], d))
    req(parity == (1,1,0,0,0), f"Picard parity drift {parity}")
    req(fast.membership_ok(cert, (W["a"], W["b"], W["c"], t, 0, W["e"], d) + parity),
        "Picard membership drift")

    triples = []
    for x2 in range(1, W["a"]):
        for x3 in range(1, W["a"] - x2):
            x7 = W["a"] - x2 - x3
            if x7 <= 0:
                continue
            triples.append((x2, x3, x7, x2*x2 + x3*x3 + x7*x7))
    req(len(triples) == counter.triple_free_count(W["a"], 3) == 946, "A support-3 population drift")

    caps = bnd.x4_caps(h16, h, g, W["b"], W["c"])
    xr = h16.a0_interval(h, g, W["b"], W["c"])
    req(xr is not None, "target x4 interval disappeared")
    threshold8 = d*d + 16*d
    genus_budget = Fraction(d*d, 16) + d + 2 - 2*g
    minpen = Fraction(3, 5)

    current = 0
    refined = 0
    rejected = 0
    by_x4 = Counter()
    by_qA = Counter()
    for x2, x3, x7, qA in triples:
        for x4 in range(xr[0], xr[1] + 1):
            if (x4 & 1) != r:
                continue
            room = -int(h16.f0(h, g, W["b"], W["c"], x4))
            req(room >= 0, "x4 interval room drift")
            if qA > room // 138:
                continue
            if 8 * (qA + qBC) > threshold8:
                continue

            # This concrete (A tuple, fixed H tuple, x4, e192) is counted once
            # by the current HPADJ22 direct survivor count.
            current += 1
            static_rho = Fraction((d//2 - 2*x4 - t)**2, 12)
            exact_cut = 2 * (genus_budget - static_rho - minpen)
            cut_floor = exact_cut.numerator // exact_cut.denominator
            if qA + qBC <= cut_floor:
                refined += 1
            else:
                rejected += 1
                by_x4[x4] += 1
                by_qA[qA] += 1

    req(current == 41200, f"fixed-H current population drift {current}")
    req(refined == 38217, f"fixed-H refined population drift {refined}")
    req(rejected == 2983 and current - refined == rejected, "fixed-H strict reduction drift")
    expected_by_x4 = {68:3,70:9,72:30,74:60,76:102,78:165,80:318,82:567,84:736,86:595,88:337,90:61}
    req(dict(sorted(by_x4.items())) == expected_by_x4, f"x4 reduction histogram drift {dict(sorted(by_x4.items()))}")

    # Cross-check the current x4 capacity implementation for every qA class
    # actually used by this family.
    for qA in by_qA:
        exact_count = 0
        for x4 in range(xr[0], xr[1] + 1):
            if (x4 & 1) != r:
                continue
            room = -int(h16.f0(h, g, W["b"], W["c"], x4))
            if qA <= room // 138:
                exact_count += 1
        req(exact_count == int(bnd.survivor_count(caps, r, qA)),
            f"current x4 survivor adapter drift qA={qA}")

    candidate = p.OLD_GLOBAL - rejected
    out = {
        "schema": "STAGE32_32_01_178_HPADJ22_E192_ZERO_CENTER_FIXED_H_FAMILY_V1",
        "status": "EXACT_CURRENT_HPADJ22_FIXED_H_FAMILY_STRICT_REFINEMENT__ZERO_MAIN_CREDIT__HOSTILE_AUDIT_REQUIRED",
        "source_locks": {
            "single_witness_parent_blob_sha1": PARENT_BLOB,
            "current_direct_count_blob_sha1": p.DIRECT_BLOB,
            "hpadj22_source_head": p.HPADJ22_SOURCE_HEAD,
            "historical_hpadj22_worker_blob_sha1": direct.OLD_BLOB,
            "zero_center_picard_source_blob_sha1": p.FAST_BLOB,
        },
        "target": {
            "row_index": p.ROW_INDEX, "row_id": row_id, "band_position": p.BAND,
            "b_interval": [36,47],
            "fixed_H": {k: W[k] for k in ("x0","x1","x5","x6","x8","x9","x10")},
            "a": W["a"], "b": W["b"], "c": W["c"], "e": W["e"],
            "qBC": qBC, "t": t, "required_x4_parity": r,
        },
        "family": {
            "A_support3_ordered_triples": len(triples),
            "current_hpadj22_survivors": current,
            "zero_center_survivors": refined,
            "exact_survivor_reduction": rejected,
            "distinct_rejected_qA_values": len(by_qA),
            "rejected_by_x4": {str(k): int(v) for k,v in sorted(by_x4.items())},
        },
        "result": {
            "current_v45_global_upper_bound": str(p.OLD_GLOBAL),
            "certified_strict_reduction_lower_bound": rejected,
            "candidate_global_upper_bound_if_promoted": str(candidate),
        },
        "semantics": {
            "same_current_hpadj22_population": True,
            "fixed_H_tuple_is_one_exact_member_of_current_joint_qBC_histogram": True,
            "all_A_support3_ordered_triples_replayed_exactly": True,
            "current_x4_survivor_adapter_crosschecked": True,
            "zero_center_picard_condition_replayed": True,
            "no_additive_cross_route_subtraction": True,
            "candidate_is_direct_same_population_upper_bound_refinement": True,
            "all_nonfamily_current_hpadj22_survivors_left_unchanged": True,
            "main_bound_replacement_performed": False,
            "hostile_audit_required_before_consumption": True,
        },
        "firewalls": {
            "main_credit_changed": False, "full178_complete": False,
            "theorem_credit_changed": False, "effectivity_credit_changed": False,
            "receiver_credit_changed": False, "endpoint_credit_changed": False,
            "stage32_closed": False, "merge": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")
    print("HPADJ22_E192_ZERO_CENTER_FIXED_H_FAMILY=" + json.dumps({
        "current_family": current, "refined_family": refined, "reduction": rejected,
        "old_global": str(p.OLD_GLOBAL), "candidate_global": str(candidate),
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
