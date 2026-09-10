#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import subprocess
import tempfile

AUDITED_HEAD = "e3c4a04d5010e6dca9428722e334890e2614297a"
BUILDER_PATH = "stages/stage32-ex1/verify_ex1_05af_s0_integral_ns_pullback_saturation.py"
BUILDER_BLOB = "8591e5e25743b32b6768022052ae59746269d17e"
ALIGN_PATH = "stages/stage32-ex1/ex1-05ac-fixed-x8-polarization-kernel-antiisometry-transvection-alignment-preflight.json"
ALIGN_BLOB = "74a9d76faf652b5f40eb6b5b1b3244071a0d24b5"


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_show(path: str, expected_blob: str) -> bytes:
    raw = subprocess.check_output(["git", "show", f"{AUDITED_HEAD}:{path}"])
    blob = git_blob_sha1(raw)
    if blob != expected_blob:
        raise ValueError(f"source-lock regression for {path}: {blob}")
    return raw


def load_builder():
    raw = git_show(BUILDER_PATH, BUILDER_BLOB)
    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(raw)
        f.flush()
        spec = importlib.util.spec_from_file_location("s32_old_smith_builder_all_prym", f.name)
        if spec is None or spec.loader is None:
            raise RuntimeError("cannot load audited builder")
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod


def gp_from_bits(bits: tuple[int, int, int]):
    # Parity representatives only: 0=id type (1,0), 1=i type (0,1).
    return tuple((0, 1) if b else (1, 0) for b in bits)


def main() -> None:
    m = load_builder()
    align = json.loads(git_show(ALIGN_PATH, ALIGN_BLOB))
    selected = {73: 0, 97: 1, 235: 2}
    if set(int(x) for x in align["q602_transvection_centers"]["actions_rows"]) != set(selected):
        raise ValueError("audited transvection residue set regression")

    totals = {
        "builds_checked": 0,
        "integral_builds": 0,
        "nonintegral_builds": 0,
        "integral_bit_one": 0,
        "integral_bit_zero": 0,
    }
    rows = []
    all_integral_gp = set()
    bit_zero_gp = set()

    for residue, aligned_factor in selected.items():
        base = m.bits(residue)
        aligned_bits = tuple(1 if j == aligned_factor else 0 for j in range(3))
        for gp_bits in itertools.product((0, 1), repeat=3):
            gp = gp_from_bits(gp_bits)
            local = {"checked": 0, "integral": 0, "nonintegral": 0, "bit1": 0, "bit0": 0}
            for lift_bits in itertools.product((0, 1), repeat=8):
                t = tuple(base[i] + 2 * lift_bits[i] for i in range(8))
                F, ok = m.build(t, gp, False)
                local["checked"] += 1
                totals["builds_checked"] += 1
                if not ok:
                    local["nonintegral"] += 1
                    totals["nonintegral_builds"] += 1
                    continue
                local["integral"] += 1
                totals["integral_builds"] += 1
                b40 = F[4][0] & 1
                b49 = F[4][9] & 1
                if b40 != b49:
                    raise ValueError("tracked Smith-source entries disagree mod 2")
                if b40:
                    local["bit1"] += 1
                    totals["integral_bit_one"] += 1
                else:
                    local["bit0"] += 1
                    totals["integral_bit_zero"] += 1
            if local["integral"]:
                all_integral_gp.add(gp_bits)
            if local["bit0"]:
                bit_zero_gp.add(gp_bits)
            rows.append({
                "residue": residue,
                "aligned_factor": aligned_factor,
                "aligned_gp_bits": list(aligned_bits),
                "gp_bits_i_type_by_factor": list(gp_bits),
                "is_audited_aligned_pattern": gp_bits == aligned_bits,
                **local,
            })

    if totals["builds_checked"] != 3 * 8 * 256:
        raise ValueError("all-Prym parity census size regression")
    if totals["integral_builds"] == 0:
        raise ValueError("all-Prym parity test vacuous")

    aligned_rows = [r for r in rows if r["is_audited_aligned_pattern"]]
    if len(aligned_rows) != 3 or any(r["integral"] != 256 or r["bit1"] != 256 for r in aligned_rows):
        raise ValueError("audited aligned parity replay regression")

    integrality_selects_alignment = all(
        (r["integral"] == 0) or r["is_audited_aligned_pattern"] for r in rows
    )
    every_integral_build_bit_one = totals["integral_bit_zero"] == 0

    out = {
        "schema": "STAGE32_32_01_178_SMITH_ALL_PRYM_PARITY_TRANSVECTION_GLUING_V1",
        "source_locks": {
            "source_pr": 1728,
            "hostile_review": 5147627146,
            "audited_exact_head": AUDITED_HEAD,
            "builder_blob_sha1": BUILDER_BLOB,
            "fixed_gluing_alignment_blob_sha1": ALIGN_BLOB,
        },
        "scope": {
            "transvection_residues": sorted(selected),
            "gaussian_parity_types_per_prym_factor": 2,
            "prym_factor_count": 3,
            "all_gp_patterns_per_residue": 8,
            "mod4_lifts_per_pattern": 256,
            "historical_gaussian_norm_magnitudes_used": False,
            "historical_projection_degrees_used": False,
        },
        "census": {
            **totals,
            "integral_gp_patterns_union": [list(x) for x in sorted(all_integral_gp)],
            "bit_zero_gp_patterns_union": [list(x) for x in sorted(bit_zero_gp)],
            "rows": rows,
        },
        "decision": {
            "integrality_alone_selects_audited_center_to_prym_alignment": integrality_selects_alignment,
            "all_integral_builds_across_all_prym_parities_force_smith_source_bit_one": every_integral_build_bit_one,
            "aligned_patterns_force_smith_source_bit_one": True,
            "prym_alignment_removable_from_smith_mod2_obstruction": every_integral_build_bit_one,
        },
        "interpretation": {
            "if_false": "If an integral non-aligned Prym parity pattern has Smith source bit 0, the fixed 05AC anti-isometry/center-to-Prym alignment remains a genuine hypothesis; transvection action alone is insufficient for the Smith obstruction.",
            "if_true": "If every integral pattern has bit 1, the Prym parity alignment can be removed at this mod-2 layer.",
            "current_full178_semantic_adapter_established": False,
            "main_pruning_credit": False,
        },
        "credit": {
            "main_pruning_credit": False,
            "full178_completion": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_claim": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
