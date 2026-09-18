#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
H21 = ROOT / "stages/stage32-ex5/hpadj-21_ex5/strictness_pilot_bounded_exact.py"
H21_BLOB = "266c7eb92fc971df24733f651c245cd14a32e494"
H08_HEAD = "36eab50192cf80ec5ed48aba40f4a56076759fea"
H08_VERIFY_REL = "stages/stage32-ex5/hpadj-08_ex5/verify_hpadj08_ex5_exact_square_bounded.py"
H08_VERIFY_BLOB = "91020f335c416bf1265fd04b4571631cb6a0836c"
H08_PREFLIGHT_REL = "stages/stage32-ex5/hpadj-08_ex5/HPADJ08-EX5-EXACT-SQUARE-PREFLIGHT.json"
H08_PREFLIGHT_BLOB = "8ecc5ecd97838d4225de1d1163fd8843451b68e5"
MAX_D = 32
EXPECTED_H08_REJECTED = 25770706503487


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


def load_module(path: Path, blob_sha: str, name: str):
    req(path.is_file(), f"missing {name}")
    req(git_blob(path) == blob_sha, f"{name} blob drift")
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {name}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_joint_bc(H: int):
    # Joint refinement of the audited HPADJ08 qBC census and the HPADJ10
    # required-x4-parity census:
    # BC[b][c][support][r][qBC] = exact prefix multiplicity.
    B = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    C = [[[defaultdict(int) for _ in range(2)] for __ in range(4)] for ___ in range(H + 1)]
    for m in range(H + 1):
        for x9 in range(m + 1):
            x5 = m - x9
            B[m][int(x5 > 0) + int(x9 > 0)][x9 & 1][x5*x5 + x9*x9] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                C[m][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8 + x10) & 1][
                    x6*x6 + x8*x8 + x10*x10
                ] += 1

    BC = [[[[defaultdict(int) for _ in range(2)] for __ in range(8)]
           for ___ in range(H + 1)] for ____ in range(H + 1)]

    # Unequal x0<x1 branch.
    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        x0par = x0 & 1
        for x1 in range(x0 + 1, H + 1):
            x1par = x1 & 1
            q01 = x0*x0 + x1*x1
            for g2 in range(H - x1 + 1):
                b = x1 + g2
                for g3 in range(H - x0 + 1):
                    c = x0 + g3
                    dst = BC[b][c]
                    for sb in range(3):
                        for x9par in (0, 1):
                            left = B[g2][sb][x9par]
                            if not left:
                                continue
                            required_cpar = x9par ^ x1par
                            r = x0par ^ x1par ^ x9par
                            for sc in range(4):
                                right = C[g3][sc][required_cpar]
                                if not right:
                                    continue
                                out = dst[sb + sc + extra][r]
                                for ql, vl in left.items():
                                    for qr, vr in right.items():
                                        out[q01 + ql + qr] += vl * vr

    # Equal x0=x1=t branch, lex-strict x5<x8.
    for t in range(H + 1):
        extra = 2 * int(t > 0)
        terminal_parity = t & 1
        cap = H - t
        for x5 in range(cap + 1):
            for x8 in range(x5 + 1, cap + 1):
                for x9 in range(cap - x5 + 1):
                    b = t + x5 + x9
                    for x6 in range(cap - x8 + 1):
                        for x10 in range(cap - x8 - x6 + 1):
                            c = t + x8 + x6 + x10
                            if ((x8 + x9 + x10) & 1) != terminal_parity:
                                continue
                            vals = (t, t, x5, x6, x8, x9, x10)
                            support = sum(v > 0 for v in vals)
                            qbc = sum(v*v for v in vals)
                            r = (t + x8 + x10) & 1
                            BC[b][c][support][r][qbc] += 1

        # Equal first lex coordinate x5=x8; enforce x6<=x9.
        for x5 in range(cap + 1):
            x8 = x5
            for x6 in range(cap - x8 + 1):
                for x9 in range(x6, cap - x5 + 1):
                    b = t + x5 + x9
                    for x10 in range(cap - x8 - x6 + 1):
                        c = t + x8 + x6 + x10
                        if ((x8 + x9 + x10) & 1) != terminal_parity:
                            continue
                        vals = (t, t, x5, x6, x8, x9, x10)
                        support = sum(v > 0 for v in vals)
                        qbc = sum(v*v for v in vals)
                        r = (t + x8 + x10) & 1
                        BC[b][c][support][r][qbc] += 1
    return BC


def brute_joint_bc(H: int):
    out = [[[[defaultdict(int) for _ in range(2)] for __ in range(8)]
            for ___ in range(H + 1)] for ____ in range(H + 1)]
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
                                r = (x0 + x8 + x10) & 1
                                q = sum(v*v for v in vals)
                                out[b][c][s][r][q] += 1
    return out


def merge_r(hist_by_r):
    out = defaultdict(int)
    for r in (0, 1):
        for q, v in hist_by_r[r].items():
            out[q] += int(v)
    return dict(out)


def crosscheck_joint(joint, old_q, parity, H: int) -> dict:
    q_cells = parity_cells = 0
    for b in range(H + 1):
        for c in range(H + 1):
            for s in range(8):
                req(merge_r(joint[b][c][s]) == dict(old_q[b][c][s]),
                    f"HPADJ08 qBC marginal mismatch {(b,c,s)}")
                got_pair = [sum(joint[b][c][s][r].values()) for r in (0, 1)]
                req(got_pair == [int(v) for v in parity[b][c][s]],
                    f"HPADJ10 parity marginal mismatch {(b,c,s)}")
                q_cells += 1
                parity_cells += 1

    fast4 = build_joint_bc(4)
    brute4 = brute_joint_bc(4)
    for b in range(5):
        for c in range(5):
            for s in range(8):
                for r in (0, 1):
                    req(dict(fast4[b][c][s][r]) == dict(brute4[b][c][s][r]),
                        f"joint brute-force mismatch {(b,c,s,r)}")
    return {
        "qbc_marginal_cells_checked": q_cells,
        "parity_marginal_cells_checked": parity_cells,
        "joint_bruteforce_H": 4,
        "joint_bruteforce_pass": True,
    }


def x4_caps(h16, h: int, g: int, b: int, c: int):
    caps = [[], []]
    xr = h16.a0_interval(h, g, b, c)
    if xr is not None:
        left, right = xr
        for x4 in range(left, right + 1):
            room = -h16.f0(h, g, b, c, x4)
            req(room >= 0, f"x4 q-capacity regression {(g,h,b,c,x4)}")
            caps[x4 & 1].append(room // 138)
    caps[0].sort()
    caps[1].sort()
    return caps


def survivor_count(caps, r: int, qa: int) -> int:
    arr = caps[r]
    return len(arr) - bisect.bisect_left(arr, qa)


def eligible_e(counter, d: int, g: int, h: int, a: int, b: int, c: int,
               support: int, srem: int, K: int):
    legacy = 8 if g == 0 else 4
    qneed = K - support
    if qneed > 0 and srem < qneed:
        return []
    M = a + b + c
    lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
    upper = min((19*d)//5, 3*d, 3*d - (b-c))
    if lower > upper:
        return []
    excluded = set()
    e_n358 = 3*d - (b-c)
    if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
        excluded.add(e_n358)
    if g == 1 and d == 8:
        excluded.add(8)
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return []
    return [e for e in range(lo, hi + 1, 2) if e not in excluded]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hpadj08-root", type=Path, required=True)
    args = ap.parse_args()

    h21 = load_module(H21, H21_BLOB, "hpadj21_bounded_locked")
    h08_path = args.hpadj08_root / H08_VERIFY_REL
    h08 = load_module(h08_path, H08_VERIFY_BLOB, "hpadj08_audited_bounded_locked")
    preflight = args.hpadj08_root / H08_PREFLIGHT_REL
    req(preflight.is_file() and git_blob(preflight) == H08_PREFLIGHT_BLOB,
        "HPADJ08 preflight blob drift")
    p08 = json.loads(preflight.read_text())
    req(p08.get("canonical_sha256_without_this_field") == h08.PREFLIGHT_CANON,
        "HPADJ08 preflight stored canonical drift")
    req(h08.canonical(p08) == h08.PREFLIGHT_CANON,
        "HPADJ08 preflight canonical drift")

    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_hpadj22")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    pilot_rows = [(row_id, int(g), int(d)) for row_id, g, d in rows if int(d) <= MAX_D]
    req(len(pilot_rows) == 26, "expected 26 bounded rows through d<=32")
    H = max(d//2 for _, _, d in pilot_rows)
    req(H == 16, "bounded H drift")

    cells, parity_bc = h21.exact_pilot_cells(p15, p14, counter, pilot_rows)
    profiles, classes_gt2, tuples_above_second = h21.full_profiles(H, counter, h19)
    joint = build_joint_bc(H)
    old_q_bc = h08.build_bc_q(H)
    cross = crosscheck_joint(joint, old_q_bc, parity_bc, H)

    aggregate_h21 = 0
    aggregate_h22 = 0
    aggregate_h08_rejected = 0
    strict_cells = tested_cells = strict_rows = 0
    row_records = []

    for row_id, g, d in pilot_rows:
        h = d // 2
        K = counter.ceil_div(d - 16*g + 16, 4)
        threshold8 = d*d + 16*d + (32 if g == 0 else 0)
        acc = {
            interval: {
                "pre": 0,
                "reject": 0,
                "h22": 0,
                "h21_caps": defaultdict(int),
            }
            for interval in p15.PLANNED
        }

        for b in range(h + 1):
            interval = p15.shard_for_b(b)
            dst = acc[interval]
            for c in range(h + 1):
                jbc = joint[b][c]
                if not any(any(bool(jbc[s][r]) for r in (0, 1)) for s in range(8)):
                    continue
                c3 = counter.component3(d, b, c)
                if c3 < 0:
                    continue
                caps = x4_caps(h16, h, g, b, c)

                for a in range(h + 1):
                    ca = counter.component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3
                    for sbc in range(8):
                        for r in (0, 1):
                            qbc_hist = jbc[sbc][r]
                            left_total = sum(qbc_hist.values())
                            if not left_total:
                                continue
                            for sa in range(4):
                                tiers = profiles[a][sa]
                                if not tiers:
                                    continue
                                support = sbc + sa
                                es = eligible_e(counter, d, g, h, a, b, c, support, srem, K)
                                if not es:
                                    continue
                                normal_sum = sum(19*d - 5*e + 1 for e in es)
                                ne = len(es)
                                a_total = sum(mult for _, mult in tiers)
                                dst["pre"] += left_total * a_total * normal_sum

                                for qa, va in tiers:
                                    s = survivor_count(caps, r, qa)
                                    for e in es:
                                        B = 19*d - 5*e + 1
                                        req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,e,B)}")
                                        dst["h21_caps"][(s, B)] += left_total * int(va) * B

                                    survive_bc = sum(vb for qb, vb in qbc_hist.items()
                                                     if 8 * (qa + qb) <= threshold8)
                                    reject_bc = left_total - survive_bc
                                    dst["reject"] += reject_bc * int(va) * normal_sum
                                    dst["h22"] += survive_bc * int(va) * s * ne

        row_h21 = row_h22 = row_reject = row_strict_cells = 0
        for interval in p15.PLANNED:
            key = (interval, g, d)
            info = cells[key]
            P = int(info["pre_mass"])
            R = int(info["rejected_mass"])
            Mpost = int(info["post_mass"])
            got = acc[interval]
            req(got["pre"] == P, f"pre-mass identity drift {key}: {got['pre']} != {P}")
            req(got["reject"] == R, f"HPADJ08 rejected-mass identity drift {key}: {got['reject']} != {R}")
            req(got["pre"] - got["reject"] == Mpost, f"post-mass conservation drift {key}")
            req(sum(got["h21_caps"].values()) == P, f"HPADJ21 capacity mass drift {key}")

            h21_obj, _, _, _ = h18.optimize_cell_exact_predomain(got["h21_caps"], Mpost)
            h21_floor = h21_obj.numerator // h21_obj.denominator
            h22_exact = int(got["h22"])
            req(h22_exact <= h21_floor,
                f"HPADJ22 weakened HPADJ21 {key}: {h22_exact} > {h21_floor}")
            tested_cells += 1
            is_strict = h22_exact < h21_floor
            strict_cells += int(is_strict)
            row_strict_cells += int(is_strict)
            row_h21 += h21_floor
            row_h22 += h22_exact
            row_reject += R

        req(row_h22 <= row_h21, f"row weakened HPADJ21 {row_id}")
        strict_row = row_h22 < row_h21
        strict_rows += int(strict_row)
        aggregate_h21 += row_h21
        aggregate_h22 += row_h22
        aggregate_h08_rejected += row_reject
        row_records.append({
            "row_id": row_id,
            "g": g,
            "d": d,
            "hpadj21_floor_sum": row_h21,
            "hpadj22_exact_survivor_sum": row_h22,
            "improvement": row_h21 - row_h22,
            "strict_cells": row_strict_cells,
            "strict": strict_row,
            "hpadj08_exact_square_rejected_terminals": row_reject,
        })

    req(aggregate_h08_rejected == EXPECTED_H08_REJECTED,
        f"HPADJ08 bounded rejection drift: {aggregate_h08_rejected}")
    req(aggregate_h08_rejected == int(p08["bounded_diagnostic"]["stored_exact_square_candidate_rejected_terminals"]),
        "HPADJ08 preflight bounded total mismatch")
    req(strict_rows > 0 and strict_cells > 0, "no strict HPADJ22 bounded witness")
    req(aggregate_h22 < aggregate_h21, "no aggregate HPADJ22 bounded improvement")

    out = {
        "schema": "STAGE32EX5_HPADJ22_BOUNDED_EXACT_DELETION_CORRELATION_V1",
        "route_id": "HPADJ-22_ex5",
        "status": "STRICT_BOUNDED_REFINEMENT_FOUND__FULL178_NOT_RUN",
        "source_locks": {
            "hpadj21_bounded_pilot_blob_sha1": H21_BLOB,
            "hpadj08_audited_exact_head": H08_HEAD,
            "hpadj08_bounded_verifier_blob_sha1": H08_VERIFY_BLOB,
            "hpadj08_preflight_blob_sha1": H08_PREFLIGHT_BLOB,
            "hpadj10_counter_blob_sha1": p14.LOCKS["hpadj10_counter_blob"],
            "full178_manifest_blob_sha1": p14.LOCKS["manifest_blob"],
        },
        "bounded_scope": {
            "max_d": MAX_D,
            "H": H,
            "row_count": len(pilot_rows),
            "tested_exact_cells": tested_cells,
        },
        "joint_histogram_crosscheck": cross,
        "exact_identity_checks": {
            "hpadj08_exact_square_rejected_terminals": aggregate_h08_rejected,
            "expected_hpadj08_exact_square_rejected_terminals": EXPECTED_H08_REJECTED,
            "every_cell_pre_mass_matches_hpadj21": True,
            "every_cell_hpadj08_rejected_mass_matches_retained_post_mass_certificate": True,
            "every_cell_post_mass_conservation_exact": True,
        },
        "candidate": {
            "hpadj21_bounded_cellwise_floor_sum": aggregate_h21,
            "hpadj22_bounded_exact_survivor_sum": aggregate_h22,
            "strict_improvement": aggregate_h21 - aggregate_h22,
            "strict_row_count": strict_rows,
            "strict_cell_count": strict_cells,
            "all_rows_strict": strict_rows == len(pilot_rows),
            "all_cells_no_weaker": True,
        },
        "profile": {
            "classes_with_more_than_two_qA_bins": classes_gt2,
            "tuples_above_second_qA_level": tuples_above_second,
        },
        "rows": row_records,
        "semantics": {
            "same_pre_domain_population_as_hpadj21": True,
            "same_picard_qA_survivor_rule_as_hpadj21": True,
            "hpadj08_deletion_location_recomputed_exactly": True,
            "hpadj08_condition": "8*(qA+qBC) <= d^2+16*d+(32 if g=0 else 0)",
            "whole_x4_block_deletion": True,
            "direct_refinement_not_additive_subtraction": True,
            "bounded_pilot_is_not_full178_numeric_replay": True,
            "main_consumption_performed": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "exact_incremental_rejected_identity_set_claimed": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
