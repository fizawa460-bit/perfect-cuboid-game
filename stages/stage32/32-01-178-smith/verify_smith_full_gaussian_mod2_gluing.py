#!/usr/bin/env python3
"""Exhaust all Gaussian mod-2 Prym actions against the three fixed-X8 transvections.

The previous all-Prym replay only used the odd-norm unit parity types {1,i}.
For a current FULL178 reuse that restriction could be an old V6 artifact.
Here each of the three Gaussian Prym factors ranges over all four residues
0, 1, i, 1+i in Z[i]/2.  For every one of the three audited invariant
transvection residues and all 256 mod-4 lifts, test the fixed integral gluing
matrix directly and inspect the Smith-source bit F[4,0]=F[4,9] mod 2.

No current-carrier semantic lift or MAIN credit is asserted.
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import subprocess
import tempfile
from collections import Counter, defaultdict

AUDITED_HEAD = "e3c4a04d5010e6dca9428722e334890e2614297a"
BUILDER_PATH = "stages/stage32-ex1/verify_ex1_05af_s0_integral_ns_pullback_saturation.py"
BUILDER_BLOB = "8591e5e25743b32b6768022052ae59746269d17e"
TRANSVECTIONS = (73, 97, 235)
GAUSSIAN_MOD2 = ((0, 0), (1, 0), (0, 1), (1, 1))


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_builder():
    raw = subprocess.check_output(["git", "show", f"{AUDITED_HEAD}:{BUILDER_PATH}"])
    if git_blob_sha1(raw) != BUILDER_BLOB:
        raise ValueError("audited builder blob drift")
    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(raw)
        f.flush()
        spec = importlib.util.spec_from_file_location("s32_old_smith_builder_full_gaussian_mod2", f.name)
        if spec is None or spec.loader is None:
            raise RuntimeError("cannot load audited builder")
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod


def main() -> None:
    m = load_builder()
    totals = Counter()
    pattern_stats: dict[tuple[tuple[int,int], ...], Counter] = defaultdict(Counter)
    per_residue = {r: Counter() for r in TRANSVECTIONS}
    integral_patterns = set()
    bit_zero_patterns = set()
    disagreement = 0

    # Unlike the old norm-602 receiver, use *all* 256 mod-4 lifts of each
    # transvection residue.  This is a gluing-parity test, not a Q-shell test.
    for residue in TRANSVECTIONS:
        base = m.bits(residue)
        for gp in itertools.product(GAUSSIAN_MOD2, repeat=3):
            for lift_bits in itertools.product((0, 1), repeat=8):
                t = tuple(base[i] + 2 * lift_bits[i] for i in range(8))
                F, ok = m.build(t, gp, False)
                totals["checked"] += 1
                pattern_stats[gp]["checked"] += 1
                per_residue[residue]["checked"] += 1
                if not ok:
                    totals["nonintegral"] += 1
                    pattern_stats[gp]["nonintegral"] += 1
                    per_residue[residue]["nonintegral"] += 1
                    continue
                totals["integral"] += 1
                pattern_stats[gp]["integral"] += 1
                per_residue[residue]["integral"] += 1
                integral_patterns.add(gp)
                b40 = F[4][0] & 1
                b49 = F[4][9] & 1
                if b40 != b49:
                    disagreement += 1
                if b40:
                    totals["bit1"] += 1
                    pattern_stats[gp]["bit1"] += 1
                    per_residue[residue]["bit1"] += 1
                else:
                    totals["bit0"] += 1
                    pattern_stats[gp]["bit0"] += 1
                    per_residue[residue]["bit0"] += 1
                    bit_zero_patterns.add(gp)

    expected = 3 * 64 * 256
    if totals["checked"] != expected:
        raise ValueError(f"census size {totals['checked']} != {expected}")
    if disagreement:
        raise ValueError(f"F[4,0]/F[4,9] mod2 disagreement on {disagreement} integral builds")
    if totals["integral"] == 0:
        raise ValueError("vacuous full Gaussian mod2 census")

    def enc(gp):
        return [list(x) for x in gp]

    rows = []
    for gp in sorted(pattern_stats):
        c = pattern_stats[gp]
        if c["integral"]:
            rows.append({
                "gaussian_mod2_by_prym_factor": enc(gp),
                "integral": c["integral"],
                "bit1": c["bit1"],
                "bit0": c["bit0"],
            })

    out = {
        "schema": "STAGE32_32_01_178_SMITH_FULL_GAUSSIAN_MOD2_GLUING_V1",
        "source_locks": {
            "source_pr": 1728,
            "hostile_review": 5147627146,
            "audited_exact_head": AUDITED_HEAD,
            "builder_blob_sha1": BUILDER_BLOB,
        },
        "scope": {
            "invariant_absolute_transvection_residues": list(TRANSVECTIONS),
            "gaussian_mod2_actions_per_prym_factor": ["0", "1", "i", "1+i"],
            "prym_factor_count": 3,
            "prym_action_patterns_per_residue": 64,
            "mod4_lifts_per_pattern": 256,
            "builds_checked": expected,
            "historical_Q602_norm_shell_used": False,
            "historical_prym_norms_9_137_9_used": False,
            "historical_projection_degrees_105_81_used": False,
        },
        "census": {
            "integral_builds": totals["integral"],
            "nonintegral_builds": totals["nonintegral"],
            "integral_smith_source_bit_one": totals["bit1"],
            "integral_smith_source_bit_zero": totals["bit0"],
            "integral_prym_pattern_count": len(integral_patterns),
            "bit_zero_prym_pattern_count": len(bit_zero_patterns),
            "integral_prym_patterns": [enc(x) for x in sorted(integral_patterns)],
            "bit_zero_prym_patterns": [enc(x) for x in sorted(bit_zero_patterns)],
            "integral_pattern_rows": rows,
            "per_residue": {str(r): dict(per_residue[r]) for r in TRANSVECTIONS},
        },
        "decision": {
            "all_integral_full_gaussian_mod2_builds_force_smith_source_bit_one": totals["bit0"] == 0,
            "old_odd_norm_unit_parity_restriction_needed_for_bit_one": totals["bit0"] != 0,
            "transvection_plus_integral_fixed_X8_gluing_suffices_at_mod2_layer": totals["bit0"] == 0,
        },
        "interpretation": {
            "if_bit_zero_exists": "The old odd-norm Prym parity restriction is load-bearing; a current carrier needs an additional character-Prym condition before Smith0 can be forced.",
            "if_no_bit_zero": "The old 9/137/9 odd-norm restriction is not load-bearing at the mod-2 gluing layer: among all Gaussian mod-2 Prym actions, every integral fixed-X8 gluing over an absolute transvection forces Smith0=1.",
            "current_full178_common_cover_semantic_lift_established": False,
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
