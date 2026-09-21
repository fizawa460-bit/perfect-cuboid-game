#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIRECT_REL = Path("stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py")
DIRECT_BLOB = "e965ab0a6ea51938006882ca2110016f48b3768e"
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
HPADJ22_SOURCE_HEAD = "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
OLD_GLOBAL = 138652739800650593494
ROW_INDEX = 22
BAND = 3

# One explicit canonical unequal-branch survivor counted by current HPADJ22.
W = {
    "g": 1, "d": 192, "a": 45, "b": 45, "c": 60, "e": 192,
    "x2": 15, "x3": 15, "x7": 15,
    "x0": 10, "x1": 15, "x5": 15, "x6": 16, "x8": 17, "x9": 15, "x10": 17,
    "x4": 90,
}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    direct_path = args.repo_root / DIRECT_REL
    req(direct_path.is_file() and blob(direct_path) == DIRECT_BLOB, "current direct-count source drift")
    req(FAST.is_file() and blob(FAST) == FAST_BLOB, "zero-center Picard source drift")

    direct = load_module(direct_path, "stage32_178_hpadj22_witness_direct")
    old = direct.load_old(args.source_root)

    # Load only the exact source chain needed by this one witness.  Do not
    # call old.source_context(): that helper constructs the full HMAX=96 qA
    # profile table even though current HPADJ22's profile definition simply
    # enumerates every nonnegative (x2,x3,x7) triple at fixed a.
    bc = old.load_bchunk()
    bnd = bc.load_bound()
    h21 = bnd.load_module(bnd.H21, bnd.H21_BLOB, "stage32_178_witness_h21")
    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "stage32_178_witness_h15")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)

    row_id, g0, d0 = rows[ROW_INDEX]
    req((row_id, int(g0), int(d0)) == ("g1-d192", 1, 192), "target row identity drift")
    req(tuple(old.PLANNED[BAND]) == (36, 47), "target band drift")

    g, d = W["g"], W["d"]
    h = d // 2
    qA = W["x2"]**2 + W["x3"]**2 + W["x7"]**2
    req(W["x2"] + W["x3"] + W["x7"] == W["a"], "A mass drift")
    req(all(W[k] > 0 for k in ("x2","x3","x7")), "A support is not 3")
    # h21.full_profiles enumerates x2=0..a, x3=0..a-x2,
    # x7=a-x2-x3 and bins exactly by support and qA.  Therefore this
    # explicit positive triple is one exact member, without building the
    # whole FULL178 profile table.
    req(0 <= W["x2"] <= W["a"] and 0 <= W["x3"] <= W["a"]-W["x2"],
        "explicit A tuple outside full_profiles enumeration domain")
    req(W["x7"] == W["a"]-W["x2"]-W["x3"], "explicit A tuple reconstruction drift")

    # Exact canonical unequal x0<x1 branch used by build_joint_bc_shard.
    req(0 < W["x0"] < W["x1"], "not canonical unequal branch")
    req(all(W[k] > 0 for k in ("x0","x1","x5","x6","x8","x9","x10")), "H support is not 7")
    req(W["x1"] + W["x5"] + W["x9"] == W["b"], "H b-group drift")
    req(W["x0"] + W["x6"] + W["x8"] + W["x10"] == W["c"], "H c-group drift")
    req(((W["x8"] + W["x10"]) & 1) == ((W["x9"] & 1) ^ (W["x1"] & 1)),
        "HPADJ22 unequal-branch C parity drift")
    r = (W["x0"] ^ W["x1"] ^ W["x9"]) & 1
    req(r == ((W["x0"] + W["x8"] + W["x10"]) & 1), "required x4 parity identity drift")
    qBC = sum(W[k]**2 for k in ("x0","x1","x5","x6","x8","x9","x10"))
    req(bc.qcap(qBC) == qBC, "explicit qBC unexpectedly overflow-capped")

    supportA = 3
    supportH = 7
    support = supportA + supportH
    K = counter.ceil_div(d - 16*g + 16, 4)
    ca = counter.component_a(d, W["a"])
    c3 = counter.component3(d, W["b"], W["c"])
    srem = min(16, d) + ca + c3
    es = bnd.eligible_e(counter, d, g, h, W["a"], W["b"], W["c"], support, srem, K)
    req(W["e"] in es, "explicit e192 witness is not in current HPADJ22 eligible-e set")

    threshold8 = d*d + 16*d
    req(8 * (qA + qBC) <= threshold8, "explicit witness fails current HPADJ22 joint qA+qBC test")

    caps = bnd.x4_caps(h16, h, g, W["b"], W["c"])
    xr = h16.a0_interval(h, g, W["b"], W["c"])
    req(xr is not None and xr[0] <= W["x4"] <= xr[1], "explicit x4 outside current interval")
    req((W["x4"] & 1) == r, "explicit x4 parity drift")
    room = -int(h16.f0(h, g, W["b"], W["c"], W["x4"]))
    req(room >= 0 and qA <= room // 138, "explicit x4 fails current qA capacity")
    req(int(bnd.survivor_count(caps, r, qA)) > 0, "current HPADJ22 survivor count unexpectedly zero")

    # Replay the retained zero-center Picard necessary condition on exactly
    # the same explicit survivor.
    fast = load_module(FAST, "stage32_178_hpadj22_witness_fast")
    cert = fast.load_certificate()
    t = W["x0"] + W["x1"] + W["x6"] + W["x9"]
    req(((W["c"] - t) & 1) == 0, "retained terminal parity drift")
    p = fast.parity_witness((W["a"], W["b"], W["c"], t, 0, W["e"], d))
    req(p == (1,1,0,0,0), f"zero-center Picard parity drift: {p}")
    req(fast.membership_ok(cert, (W["a"], W["b"], W["c"], t, 0, W["e"], d) + p),
        "zero-center Picard membership drift")

    genus_budget = Fraction(d*d, 16) + d + 2 - 2*g
    static_rho = Fraction((d//2 - 2*W["x4"] - t)**2, 12)
    minpen = Fraction(3, 5)
    exact_cut = 2 * (genus_budget - static_rho - minpen)
    q_total = qA + qBC
    cut_floor = exact_cut.numerator // exact_cut.denominator
    req(q_total > cut_floor, "explicit current HPADJ22 survivor is not rejected by zero-center condition")

    candidate = OLD_GLOBAL - 1
    out = {
        "schema": "STAGE32_32_01_178_HPADJ22_E192_ZERO_CENTER_SINGLE_WITNESS_V1",
        "status": "EXACT_CURRENT_HPADJ22_STRICT_WITNESS__AT_LEAST_ONE_SURVIVOR_REMOVED__ZERO_MAIN_CREDIT__HOSTILE_AUDIT_REQUIRED",
        "source_locks": {
            "current_direct_count_blob_sha1": DIRECT_BLOB,
            "hpadj22_source_head": HPADJ22_SOURCE_HEAD,
            "historical_hpadj22_worker_blob_sha1": direct.OLD_BLOB,
            "zero_center_picard_source_blob_sha1": FAST_BLOB,
        },
        "target": {
            "row_index": ROW_INDEX, "row_id": row_id, "band_position": BAND,
            "b_interval": [36,47], **W,
        },
        "current_hpadj22_acceptance": {
            "qA": qA, "qBC": qBC, "q_total": q_total,
            "threshold8": threshold8, "threshold_q": threshold8 // 8,
            "required_x4_parity": r,
            "x4_room": room, "x4_qA_cap": room // 138,
            "eligible_e_contains_192": True,
            "explicit_survivor_counted_by_current_hpadj22": True,
        },
        "zero_center_rejection": {
            "t": t, "picard_parity": list(p),
            "picard_membership": True,
            "genus_budget": str(genus_budget),
            "static_rho": str(static_rho),
            "residual_min_penalty": str(minpen),
            "exact_q_total_cut": str(exact_cut),
            "exact_q_total_cut_floor": cut_floor,
            "q_total": q_total,
            "strictly_rejected": True,
        },
        "result": {
            "current_v45_global_upper_bound": str(OLD_GLOBAL),
            "certified_strict_reduction_lower_bound": 1,
            "candidate_global_upper_bound_if_promoted": str(candidate),
        },
        "semantics": {
            "same_current_hpadj22_population": True,
            "one_explicit_current_hpadj22_survivor_refined": True,
            "no_additive_cross_route_subtraction": True,
            "candidate_is_direct_same_population_upper_bound_refinement": True,
            "all_other_current_hpadj22_survivors_left_unchanged": True,
            "main_bound_replacement_performed": False,
            "hostile_audit_required_before_consumption": True,
        },
        "firewalls": {
            "main_credit_changed": False,
            "full178_complete": False,
            "theorem_credit_changed": False,
            "effectivity_credit_changed": False,
            "receiver_credit_changed": False,
            "endpoint_credit_changed": False,
            "stage32_closed": False,
            "merge": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")

    print("HPADJ22_E192_ZERO_CENTER_SINGLE_WITNESS=" + json.dumps({
        "qA": qA, "qBC": qBC, "q_total": q_total,
        "x4": W["x4"], "zero_center_cut_floor": cut_floor,
        "old_global": str(OLD_GLOBAL), "candidate_global": str(candidate),
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
