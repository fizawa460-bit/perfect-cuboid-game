#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
BCHUNK = HERE / "run_full_bchunk.py"
BCHUNK_BLOB = "3fc6e7e4aff539be5b60528d1d1b2e41529ddc03"
SCHEMA_ROW = "STAGE32EX5_HPADJ22_BAND_ROW_CELL_V1"
SCHEMA_COMPLETE = "STAGE32EX5_HPADJ22_BAND_COMPLETE_V1"
HMAX = 96
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


def load_bchunk():
    req(BCHUNK.is_file() and git_blob(BCHUNK) == BCHUNK_BLOB, "bchunk worker drift")
    spec = importlib.util.spec_from_file_location("hpadj22_bchunk_locked_for_band", BCHUNK)
    req(spec is not None and spec.loader is not None, "cannot load bchunk worker")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def source_context():
    bc = load_bchunk()
    bnd = bc.load_bound()
    h21 = bnd.load_module(bnd.H21, bnd.H21_BLOB, "hpadj21_locked_for_hpadj22_band")
    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_hpadj22_band")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178, "FULL178 row count drift")
    req(tuple(tuple(x) for x in p15.PLANNED) == PLANNED, "HPADJ15 band partition drift")
    rejected = p15.load_certificate(p14)
    req(len(rejected) == 178 * len(PLANNED), "HPADJ08 retained cell certificate coverage drift")
    profiles, classes_gt2, tuples_above_second = h21.full_profiles(HMAX, counter, h19)
    return bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second


def row_source_locks(bc, bnd, h21, p14):
    return {
        "bchunk_worker_git_blob": BCHUNK_BLOB,
        "bounded_gate_git_blob": bc.BOUND_BLOB,
        "hpadj21_bounded_git_blob": bnd.H21_BLOB,
        "hpadj20_parent_git_blob": h21.PARENT_BLOB,
        "full178_manifest_blob_sha1": p14.LOCKS["manifest_blob"],
        "hpadj10_counter_blob_sha1": p14.LOCKS["hpadj10_counter_blob"],
    }


def validate_row_obj(d: dict, band_position: int, row_index: int, rows, locks: dict) -> dict:
    req(d.get("schema") == SCHEMA_ROW, "row checkpoint schema drift")
    req(int(d.get("band_position", -1)) == band_position, "row checkpoint band drift")
    req(int(d.get("row", {}).get("index", -1)) == row_index, "row checkpoint index drift")
    row_id, g, degree = rows[row_index]
    req(d["row"] == {"index": row_index, "row_id": row_id, "g": int(g), "d": int(degree)},
        f"row identity drift {row_index}")
    req(d.get("b_interval") == list(PLANNED[band_position]), "row checkpoint interval drift")
    req(d.get("source_locks") == locks, "row checkpoint source-lock drift")
    req(d.get("canonical_sha256_without_this_field") == canonical(d), "row checkpoint canonical drift")
    req(all(v is False for v in d["credit_firewall"].values()), "row checkpoint credit firewall drift")
    t = d["totals"]
    req(int(t["pre_mass"]) - int(t["rejected_mass"]) == int(t["post_mass"]), "row checkpoint mass conservation")
    req(int(t["hpadj22_exact_survivors"]) <= int(t["hpadj21_floor"]), "row checkpoint HPADJ22 weakening")
    return d


def load_resume_rows(resume_dir: Path | None, band_position: int, rows, locks: dict) -> dict[int, dict]:
    out: dict[int, dict] = {}
    if resume_dir is None or not resume_dir.exists():
        return out
    for path in sorted(resume_dir.rglob("row-*.json")):
        try:
            raw = json.loads(path.read_text())
        except Exception:
            continue
        if raw.get("schema") != SCHEMA_ROW or int(raw.get("band_position", -1)) != band_position:
            continue
        idx = int(raw.get("row", {}).get("index", -1))
        req(0 <= idx < len(rows), f"resume row index out of range {idx}")
        req(idx not in out, f"duplicate resume row {idx}")
        out[idx] = validate_row_obj(raw, band_position, idx, rows, locks)
    return out


def compute_row_cell(ctx, joint, band_position: int, row_index: int) -> dict:
    bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx
    row_id, g0, d0 = rows[row_index]
    g, d = int(g0), int(d0)
    h = d // 2
    interval = PLANNED[band_position]
    b0, b1 = interval
    K = counter.ceil_div(d - 16*g + 16, 4)
    threshold8 = d*d + 16*d + (32 if g == 0 else 0)
    pre = reject = h22 = 0
    h21_caps = defaultdict(int)

    for b in range(b0, min(b1, h) + 1):
        for c in range(h + 1):
            jbc = joint[b][c]
            if not any(any(bool(jbc[s][r]) for r in (0, 1)) for s in range(8)):
                continue
            c3 = counter.component3(d, b, c)
            if c3 < 0:
                continue
            x4caps = bnd.x4_caps(h16, h, g, b, c)
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
                            es = bnd.eligible_e(counter, d, g, h, a, b, c, support, srem, K)
                            if not es:
                                continue
                            normal_sum = sum(19*d - 5*e + 1 for e in es)
                            ne = len(es)
                            a_total = sum(mult for _, mult in tiers)
                            pre += left_total * a_total * normal_sum
                            for qa, va in tiers:
                                s = bnd.survivor_count(x4caps, r, qa)
                                for e in es:
                                    B = 19*d - 5*e + 1
                                    req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,e,B)}")
                                    h21_caps[(s, B)] += left_total * int(va) * B
                                survive_bc = sum(
                                    vb for qb, vb in qbc_hist.items()
                                    if 8 * (qa + qb) <= threshold8
                                )
                                reject_bc = left_total - survive_bc
                                reject += reject_bc * int(va) * normal_sum
                                h22 += survive_bc * int(va) * s * ne

    retained_reject = int(rejected[(interval, g, d)])
    req(reject == retained_reject,
        f"HPADJ08 retained rejected-mass mismatch {(interval,g,d)}: {reject} != {retained_reject}")
    req(sum(h21_caps.values()) == pre, f"HPADJ21 capacity/pre mismatch {(interval,g,d)}")
    post = pre - reject
    req(post >= 0, f"negative post mass {(interval,g,d)}")
    if pre == 0:
        req(reject == 0 and post == 0 and h22 == 0 and not h21_caps, f"zero-cell drift {(interval,g,d)}")
        h21_obj = Fraction(0, 1)
    else:
        h21_obj, _, _, _ = h18.optimize_cell_exact_predomain(h21_caps, post)
    h21_floor = h21_obj.numerator // h21_obj.denominator
    req(h22 <= h21_floor, f"HPADJ22 weakened HPADJ21 {(interval,g,d)}")

    out = {
        "schema": SCHEMA_ROW,
        "route_id": "HPADJ-22_ex5",
        "band_position": band_position,
        "b_interval": list(interval),
        "row": {"index": row_index, "row_id": row_id, "g": g, "d": d},
        "source_locks": row_source_locks(bc, bnd, h21, p14),
        "totals": {
            "pre_mass": pre,
            "rejected_mass": reject,
            "post_mass": post,
            "hpadj21_num": h21_obj.numerator,
            "hpadj21_den": h21_obj.denominator,
            "hpadj21_floor": h21_floor,
            "hpadj22_exact_survivors": h22,
            "strict": h22 < h21_floor,
            "improvement": h21_floor - h22,
        },
        "profile": {
            "classes_with_more_than_two_qA_bins": classes_gt2,
            "tuples_above_second_qA_level": tuples_above_second,
        },
        "semantics": {
            "one_exact_hpadj15_b_shard_cell": True,
            "joint_qA_qBC_picard_parity_used": True,
            "retained_hpadj08_rejected_mass_replayed_exactly": True,
            "same_population_as_hpadj21": True,
            "same_picard_qA_rule_as_hpadj21": True,
            "additive_subtraction_used": False,
        },
        "credit_firewall": {
            "partial_output_credit": False,
            "stage32_main_credit": False,
            "full178_completion_credit": False,
            "theorem_credit": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    return out


def complete_marker(out_dir: Path, band_position: int, rows_data: dict[int, dict], locks: dict) -> dict:
    req(set(rows_data) == set(range(178)), f"band {band_position} row coverage incomplete: {len(rows_data)}")
    stream = hashlib.sha256()
    summaries = []
    pre = reject = post = h21_floor = h22 = strict = 0
    for idx in range(178):
        d = rows_data[idx]
        t = d["totals"]
        summary = {
            "row_index": idx,
            "row_id": d["row"]["row_id"],
            "canonical": d["canonical_sha256_without_this_field"],
            "hpadj21_floor": int(t["hpadj21_floor"]),
            "hpadj22_exact": int(t["hpadj22_exact_survivors"]),
            "improvement": int(t["improvement"]),
            "strict": bool(t["strict"]),
        }
        summaries.append(summary)
        stream.update(json.dumps(summary, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        pre += int(t["pre_mass"]); reject += int(t["rejected_mass"]); post += int(t["post_mass"])
        h21_floor += int(t["hpadj21_floor"]); h22 += int(t["hpadj22_exact_survivors"])
        strict += int(bool(t["strict"]))
    req(pre - reject == post, "band aggregate mass conservation")
    req(h22 <= h21_floor, "band aggregate weakened HPADJ21")
    marker = {
        "schema": SCHEMA_COMPLETE,
        "route_id": "HPADJ-22_ex5",
        "status": "EXACT_BAND_COMPLETE_HOSTILE_AUDIT_REQUIRED",
        "band_position": band_position,
        "b_interval": list(PLANNED[band_position]),
        "row_count": 178,
        "source_locks": locks,
        "row_stream_sha256": stream.hexdigest(),
        "totals": {
            "pre_mass": pre,
            "rejected_mass": reject,
            "post_mass": post,
            "hpadj21_cellwise_floor_sum": h21_floor,
            "hpadj22_exact_survivor_sum": h22,
            "strict_cell_count": strict,
            "improvement": h21_floor - h22,
        },
        "row_summaries": summaries,
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "full178_complete": False,
            "hostile_audit_required": True,
            "merge_authorized": False,
        },
    }
    marker["canonical_sha256_without_this_field"] = canonical(marker)
    (out_dir / "BAND-COMPLETE.json").write_text(json.dumps(marker, sort_keys=True, separators=(",", ":")) + "\n")
    return marker


def validate_complete_dir(path: Path, band_position: int, ctx) -> tuple[dict, dict[int, dict]]:
    bc, bnd, h21, _, _, _, p14, _, rows, _, _, _, _ = ctx
    locks = row_source_locks(bc, bnd, h21, p14)
    marker_path = path / "BAND-COMPLETE.json"
    req(marker_path.is_file(), f"missing complete marker band {band_position}")
    marker = json.loads(marker_path.read_text())
    req(marker.get("schema") == SCHEMA_COMPLETE, "band marker schema drift")
    req(int(marker.get("band_position", -1)) == band_position, "band marker position drift")
    req(marker.get("b_interval") == list(PLANNED[band_position]), "band marker interval drift")
    req(marker.get("source_locks") == locks, "band marker source-lock drift")
    req(marker.get("canonical_sha256_without_this_field") == canonical(marker), "band marker canonical drift")
    rows_data: dict[int, dict] = {}
    for idx in range(178):
        rp = path / "rows" / f"row-{idx:03d}.json"
        req(rp.is_file(), f"missing band row {band_position}/{idx}")
        d = validate_row_obj(json.loads(rp.read_text()), band_position, idx, rows, locks)
        rows_data[idx] = d
    rebuilt = complete_marker(path, band_position, rows_data, locks)
    req(rebuilt == marker, "band marker rebuild mismatch")
    return marker, rows_data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--band-position", type=int, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--resume-dir", type=Path)
    ap.add_argument("--verify-complete", type=Path)
    args = ap.parse_args()
    req(0 <= args.band_position < len(PLANNED), "band position out of range")
    ctx = source_context()
    bc, bnd, h21, _, _, _, p14, _, rows, _, _, _, _ = ctx
    locks = row_source_locks(bc, bnd, h21, p14)

    if args.verify_complete is not None:
        marker, _ = validate_complete_dir(args.verify_complete, args.band_position, ctx)
        print("VALID_HPADJ22_BAND=" + marker["canonical_sha256_without_this_field"])
        return

    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows_dir = args.output_dir / "rows"
    rows_dir.mkdir(parents=True, exist_ok=True)

    carried = load_resume_rows(args.resume_dir, args.band_position, rows, locks)
    for idx, d in carried.items():
        (rows_dir / f"row-{idx:03d}.json").write_text(json.dumps(d, sort_keys=True, separators=(",", ":")) + "\n")
    print(f"CARRIED_ROWS={len(carried)}")
    if len(carried) == 178:
        marker = complete_marker(args.output_dir, args.band_position, carried, locks)
        print(json.dumps({
            "band_position": args.band_position,
            "b_interval": list(PLANNED[args.band_position]),
            "rows": marker["row_count"],
            "hpadj21": marker["totals"]["hpadj21_cellwise_floor_sum"],
            "hpadj22": marker["totals"]["hpadj22_exact_survivor_sum"],
            "gain": marker["totals"]["improvement"],
            "canonical": marker["canonical_sha256_without_this_field"],
            "resume_complete_no_recompute": True,
        }, sort_keys=True))
        return

    b0, b1 = PLANNED[args.band_position]
    joint = bc.build_joint_bc_shard(HMAX, b0, b1)
    rows_data = dict(carried)
    for idx in range(178):
        if idx in rows_data:
            continue
        d = compute_row_cell(ctx, joint, args.band_position, idx)
        (rows_dir / f"row-{idx:03d}.json").write_text(json.dumps(d, sort_keys=True, separators=(",", ":")) + "\n")
        rows_data[idx] = d
        print(json.dumps({
            "band": args.band_position,
            "row_index": idx,
            "row_id": d["row"]["row_id"],
            "gain": d["totals"]["improvement"],
            "completed_rows": len(rows_data),
        }, sort_keys=True), flush=True)

    marker = complete_marker(args.output_dir, args.band_position, rows_data, locks)
    print(json.dumps({
        "band_position": args.band_position,
        "b_interval": list(PLANNED[args.band_position]),
        "rows": marker["row_count"],
        "hpadj21": marker["totals"]["hpadj21_cellwise_floor_sum"],
        "hpadj22": marker["totals"]["hpadj22_exact_survivor_sum"],
        "gain": marker["totals"]["improvement"],
        "canonical": marker["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
