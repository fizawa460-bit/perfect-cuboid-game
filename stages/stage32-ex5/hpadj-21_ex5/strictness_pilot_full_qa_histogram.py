#!/usr/bin/env python3
from __future__ import annotations

import bisect
import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "stages/stage32-ex5/hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py"
PARENT_BLOB = "837d647cfcbc96bbe384e564f449cd7042a46d48"
MAX_PILOT_D = 32


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
    req(PARENT.is_file() and git_blob(PARENT) == PARENT_BLOB, "HPADJ20 parent blob drift")
    spec = importlib.util.spec_from_file_location("hpadj20_locked_for_hpadj21", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ20 parent")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_full_profiles(H: int, counter, h19):
    profiles = [[[] for _ in range(4)] for __ in range(H + 1)]
    classes_gt_two = 0
    tuples_above_second = 0
    for a in range(H + 1):
        hist = [defaultdict(int) for _ in range(4)]
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                s = int(x2 > 0) + int(x3 > 0) + int(x7 > 0)
                qA = x2 * x2 + x3 * x3 + x7 * x7
                hist[s][qA] += 1
        for s in range(4):
            expected = int(counter.triple_free_count(a, s))
            got = sum(hist[s].values())
            req(got == expected, f"A histogram multiplicity drift {(a,s)}")
            if not expected:
                continue
            keys = sorted(hist[s])
            req(keys[0] == int(h19.qa_min_for_mass_support(a, s)), f"A qA minimum drift {(a,s)}")
            profiles[a][s] = [(int(q), int(hist[s][q])) for q in keys]
            if len(keys) > 2:
                classes_gt_two += 1
                tuples_above_second += sum(int(hist[s][q]) for q in keys[2:])
    return profiles, classes_gt_two, tuples_above_second


def survivor_profiles_full(h16, profiles, h: int, g: int, b: int, c: int):
    caps = [[], []]
    xr = h16.a0_interval(h, g, b, c)
    if xr is not None:
        left, right = xr
        for x4 in range(left, right + 1):
            room = -h16.f0(h, g, b, c, x4)
            req(room >= 0, "full-hist q interval construction regression")
            caps[x4 & 1].append(room // 138)
    caps[0].sort()
    caps[1].sort()

    out = [[None for _ in range(4)] for __ in range(h + 1)]
    for a in range(h + 1):
        for s in range(4):
            tiers = profiles[a][s]
            if not tiers:
                continue
            grouped = defaultdict(int)
            for qexact, mult in tiers:
                surv = tuple(len(caps[r]) - bisect.bisect_left(caps[r], int(qexact)) for r in (0, 1))
                grouped[surv] += int(mult)
            out[a][s] = {
                "tiers": [(int(k[0]), int(k[1]), int(v)) for k, v in sorted(grouped.items())],
            }
    return out


def main() -> None:
    h20 = load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    cells, p14 = h17.exact_cells(h16)
    counter = p14.load_counter()

    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    pilot_rows = [(row_id, int(g), int(d)) for row_id, g, d in rows if int(d) <= MAX_PILOT_D]
    req(pilot_rows, "no pilot rows")
    H = max(d // 2 for _, _, d in pilot_rows)
    BC = counter.build_bc_exact_parity(H)
    two_profiles, _, _, _ = h20.build_two_tier_profiles(H, counter, h19)
    full_profiles, classes_gt_two, tuples_above_second = build_full_profiles(H, counter, h19)
    req(classes_gt_two > 0 and tuples_above_second > 0, "pilot range does not contain genuine >2-bin qA classes")

    strict = []
    tested_cells = 0
    no_weaker_cells = 0

    for row_id, g, d in pilot_rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = counter.ceil_div(d - 16 * g + 16, 4)
        A = [[sum(mult for _, mult in full_profiles[a][sa]) for sa in range(4)] for a in range(h + 1)]
        two_caps = {interval: defaultdict(int) for interval in h18.PLANNED}
        full_caps = {interval: defaultdict(int) for interval in h18.PLANNED}

        for b in range(h + 1):
            interval = h16.shard_for_b(b)
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv):
                    continue
                c3 = counter.component3(d, b, c)
                if c3 < 0:
                    continue
                two_surv, _ = h20.survivor_profiles(h16, h19, two_profiles, h, g, b, c)
                full_surv = survivor_profiles_full(h16, full_profiles, h, g, b, c)

                for a in range(h + 1):
                    avec = A[a]
                    if not any(avec):
                        continue
                    M = a + b + c
                    ca = counter.component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3

                    for sbc, pair in enumerate(bcv):
                        for r in (0, 1):
                            left_count = int(pair[r])
                            if not left_count:
                                continue
                            for sa, right_total in enumerate(avec):
                                if not right_total:
                                    continue
                                tinfo = two_surv[a][sa]
                                finfo = full_surv[a][sa]
                                req(tinfo is not None and finfo is not None, f"missing profile {(a,sa)}")
                                req(sum(v[2] for v in tinfo["tiers"]) == int(right_total), "two-tier population drift")
                                req(sum(v[2] for v in finfo["tiers"]) == int(right_total), "full-hist population drift")

                                support = sbc + sa
                                qneed = K - support
                                if qneed > 0 and srem < qneed:
                                    continue
                                lower = max(legacy, K, d - 4 * g + 4, M, M + max(0, qneed))
                                upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
                                if lower > upper:
                                    continue
                                excluded = set()
                                e_n358 = 3 * d - (b - c)
                                if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                                    excluded.add(e_n358)
                                if g == 1 and d == 8:
                                    excluded.add(8)

                                lo = lower if lower % 2 == 0 else lower + 1
                                hi = upper if upper % 2 == 0 else upper - 1
                                for e in range(lo, hi + 1, 2):
                                    if e in excluded:
                                        continue
                                    B = 19 * d - 5 * e + 1
                                    req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,e,B)}")
                                    two_count = 0
                                    for s0, s1, mult in tinfo["tiers"]:
                                        q_s = s0 if r == 0 else s1
                                        count = left_count * int(mult)
                                        two_count += count
                                        two_caps[interval][(int(q_s), B)] += count * B
                                    full_count = 0
                                    for s0, s1, mult in finfo["tiers"]:
                                        q_s = s0 if r == 0 else s1
                                        count = left_count * int(mult)
                                        full_count += count
                                        full_caps[interval][(int(q_s), B)] += count * B
                                    req(two_count == full_count == left_count * int(right_total), "block population drift")

        row_keys = [key for key in cells if int(key[1]) == g and int(key[2]) == d]
        req(row_keys, f"no exact LP cells for row {(row_id,g,d)}")
        for key in row_keys:
            interval = key[0]
            info = cells[key]
            Mpost = int(info["post_mass"])
            Pexact = int(info["pre_mass"])
            req(sum(two_caps[interval].values()) == Pexact, f"two-tier pre-mass mismatch {key}")
            req(sum(full_caps[interval].values()) == Pexact, f"full-hist pre-mass mismatch {key}")
            tobj, _, _, _ = h18.optimize_cell_exact_predomain(two_caps[interval], Mpost)
            fobj, _, _, _ = h18.optimize_cell_exact_predomain(full_caps[interval], Mpost)
            req(fobj <= tobj, f"full histogram weakened HPADJ20 {key}")
            tested_cells += 1
            no_weaker_cells += 1
            if fobj < tobj:
                strict.append({
                    "row_id": row_id,
                    "g": g,
                    "d": d,
                    "b_interval": list(interval),
                    "post_mass": Mpost,
                    "hpadj20_num": tobj.numerator,
                    "hpadj20_den": tobj.denominator,
                    "full_hist_num": fobj.numerator,
                    "full_hist_den": fobj.denominator,
                    "hpadj20_floor": tobj.numerator // tobj.denominator,
                    "full_hist_floor": fobj.numerator // fobj.denominator,
                    "rational_improvement": {
                        "num": (tobj - fobj).numerator,
                        "den": (tobj - fobj).denominator,
                    },
                })

    out = {
        "schema": "STAGE32EX5_HPADJ21_FULL_QA_HISTOGRAM_STRICTNESS_PILOT_V1",
        "route_id": "HPADJ-21_ex5",
        "status": "STRICT_WITNESS_FOUND" if strict else "NO_STRICT_WITNESS_IN_BOUNDED_PILOT",
        "source": {
            "hpadj20_parent_blob_sha1": PARENT_BLOB,
            "max_pilot_d": MAX_PILOT_D,
            "pilot_row_count": len(pilot_rows),
            "pilot_rows": [[r, g, d] for r, g, d in pilot_rows],
        },
        "full_histogram": {
            "classes_with_more_than_two_qA_bins_in_pilot_profile": classes_gt_two,
            "tuples_above_second_qA_level_in_pilot_profile": tuples_above_second,
            "population_preserved_exactly": True,
            "refinement_rule": "Replace HPADJ20 common second tier by every exact qA bin with exact multiplicity.",
        },
        "lp_check": {
            "tested_exact_cells": tested_cells,
            "no_weaker_exact_cells": no_weaker_cells,
            "strict_exact_cell_count": len(strict),
            "strict_witnesses": strict[:16],
        },
        "semantics": {
            "same_pre_domain_population_as_hpadj20": True,
            "same_post_mass_constraint_as_hpadj20": True,
            "same_picard_character_as_hpadj20": True,
            "additive_subtraction_used": False,
            "statistical_independence_assumed": False,
            "bounded_pilot_is_not_full178_numeric_replay": True,
            "strict_global_numeric_bound_claimed": False,
            "main_consumption_performed": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


if __name__ == "__main__":
    main()
