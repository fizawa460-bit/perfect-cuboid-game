#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib

from direct_picard_slice_quadratic_bound import DirectPicardSliceQuadraticBound

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
SCHEMA = "STAGE32_RESIDUAL32_01_DIRECT_PICARD_QUADRATIC_SLICE_CENSUS_V1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def load_module_payload(path: pathlib.Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def count_image_residues(bound: DirectPicardSliceQuadraticBound, d: int, e: int, lo: int, hi: int) -> int:
    if lo > hi:
        return 0
    bridge = bound.bridge
    q = int(bridge.target_image_modulus)
    if q == 1:
        return hi - lo + 1
    total = 0
    for r in range(q):
        if not bridge.target_in_image(d, e, r):
            continue
        first = lo + ((r - lo) % q)
        if first <= hi:
            total += (hi - first) // q + 1
    return total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=pathlib.Path, required=True)
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--marking", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    assert csha(manifest) == claimed == EXPECTED_MANIFEST_SHA256
    bundle = load_module_payload(args.retained, "stage32_direct_quadratic_picard")
    marking = load_module_payload(args.marking, "stage32_direct_quadratic_marking")
    bound = DirectPicardSliceQuadraticBound.from_retained(marking, bundle)

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    assert len(rows) == 178 and len(set(rows)) == 178

    total_raw = 0
    total_quadratic = 0
    total_image_quadratic = 0
    quadratic_empty_e = 0
    image_quadratic_empty_e = 0
    row_summaries = []
    stream_hash = hashlib.sha256()

    for row_id in rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_raw = row_quad = row_image_quad = 0
        row_quad_empty = row_image_empty = 0
        peak = None
        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            raw = upper + 1
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            if interval is None:
                qcount = 0
                iqcount = 0
                lo = hi = None
                row_quad_empty += 1
                row_image_empty += 1
                quadratic_empty_e += 1
                image_quadratic_empty_e += 1
            else:
                lo, hi = interval
                qcount = hi - lo + 1
                iqcount = count_image_residues(bound, d, e, lo, hi)
                if iqcount == 0:
                    row_image_empty += 1
                    image_quadratic_empty_e += 1
            total_raw += raw
            total_quadratic += qcount
            total_image_quadratic += iqcount
            row_raw += raw
            row_quad += qcount
            row_image_quad += iqcount
            rec = {
                "row_id": row_id,
                "e": e,
                "a_upper": upper,
                "continuous_selfsq_interval": None if interval is None else [lo, hi],
                "quadratic_feasible_a_count": qcount,
                "image_and_quadratic_feasible_a_count": iqcount,
            }
            stream_hash.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
            if peak is None or iqcount > peak[1]:
                peak = (e, iqcount, None if interval is None else [lo, hi])
        assert peak is not None
        row_summaries.append({
            "row_id": row_id,
            "degree": d,
            "genus": g,
            "raw_direct_slices": row_raw,
            "quadratic_feasible_slices": row_quad,
            "image_and_quadratic_feasible_slices": row_image_quad,
            "quadratic_empty_e_strata": row_quad_empty,
            "image_and_quadratic_empty_e_strata": row_image_empty,
            "peak_image_and_quadratic_e": peak[0],
            "peak_image_and_quadratic_count": peak[1],
            "peak_interval": peak[2],
        })

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "EXACT_CONTINUOUS_SELF_INTERSECTION_BOUND_PLUS_TARGET_IMAGE_GATE",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "quadratic_bound_certificate_sha256": bound.certificate["canonical_sha256_without_this_field"],
        "bridge_certificate_sha256": bound.bridge.certificate["canonical_sha256_without_this_field"],
        "row_count": len(rows),
        "e_strata": int(manifest["coarse_strata_count"]),
        "raw_direct_picard_slice_count": total_raw,
        "continuous_quadratic_feasible_slice_count": total_quadratic,
        "image_and_continuous_quadratic_feasible_slice_count": total_image_quadratic,
        "quadratic_empty_e_strata": quadratic_empty_e,
        "image_and_quadratic_empty_e_strata": image_quadratic_empty_e,
        "slice_stream_sha256": stream_hash.hexdigest(),
        "row_summaries": row_summaries,
        "semantics": {
            "quadratic_gate_is_safe_necessary_condition": True,
            "target_image_gate_is_exact": True,
            "closevectors_not_run": True,
            "all140_nonnegativity_not_yet_enumerated": True,
            "numerical_picard_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
        },
    }
    assert total_raw > 0 and total_image_quadratic <= total_quadratic <= total_raw
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_DIRECT_PICARD_QUADRATIC_CENSUS",
        "raw_direct_slices": total_raw,
        "continuous_quadratic_feasible_slices": total_quadratic,
        "image_and_continuous_quadratic_feasible_slices": total_image_quadratic,
        "quadratic_empty_e_strata": quadratic_empty_e,
        "image_and_quadratic_empty_e_strata": image_quadratic_empty_e,
        "bound_sha256": bound.certificate["canonical_sha256_without_this_field"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
