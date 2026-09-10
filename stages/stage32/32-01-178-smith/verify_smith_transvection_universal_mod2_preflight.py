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
        spec = importlib.util.spec_from_file_location("s32_old_smith_builder", f.name)
        if spec is None or spec.loader is None:
            raise RuntimeError("cannot load audited builder")
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod


def mod2_matrix(A):
    return tuple(tuple(int(x) & 1 for x in row) for row in A)


def main() -> None:
    m = load_builder()
    align = json.loads(git_show(ALIGN_PATH, ALIGN_BLOB))
    actions = {
        int(k): tuple(tuple(int(x) for x in row) for row in v)
        for k, v in align["q602_transvection_centers"]["actions_rows"].items()
    }
    selected = {73: 0, 97: 1, 235: 2}

    # First source-lock that the retained ring-coordinate action TA is in the
    # same A[2] basis as the three fixed-gluing transvection matrices in 05AC.
    for r in (73, 97, 235):
        if mod2_matrix(m.TA(m.bits(r))) != actions[r]:
            raise ValueError(f"A[2] action basis mismatch for residue {r}")

    action_to_factor = {actions[r]: selected[r] for r in selected}
    if len(action_to_factor) != 3:
        raise ValueError("three transvection actions unexpectedly collide")

    # Enumerate the *entire* retained 8-bit ring-coordinate cube, not just
    # Q(T)=602 residues.  Keep exactly those whose A[2] action equals one of
    # the three nonzero center transvections fixed by 05AC.  This isolates the
    # mod-2 action type from the historical Rosati norm/Q602 shell.
    compatible = []
    by_factor = {0: [], 1: [], 2: []}
    for r in range(256):
        action = mod2_matrix(m.TA(m.bits(r)))
        if action not in action_to_factor:
            continue
        factor = action_to_factor[action]
        b = m.bits(r)
        middle_gaussian_b = int(factor == 1)
        smith_source_bit = (b[2] + b[3] + middle_gaussian_b) & 1
        compatible.append((r, factor, smith_source_bit))
        by_factor[factor].append(r)

    if not compatible:
        raise ValueError("no transvection-compatible ring residues found")
    if any(bit != 1 for _, _, bit in compatible):
        bad = [(r, f, bit) for r, f, bit in compatible if bit != 1]
        raise ValueError(f"transvection action does not force Smith source bit: {bad[:20]}")

    # The quotient gluing integrality test depends only on parity of the four
    # blocks.  Use norm-1 representatives id=(1,0), i=(0,1): exactly one Prym
    # block is i-type, the factor dictated by the fixed anti-isometry in 05AC.
    # We do not claim these synthetic blocks have the historical V6 norms.
    # We check every mod-4 lift of every compatible 8-bit invariant action.
    integral_builds = 0
    nonintegral_builds = 0
    checked_lifts = 0
    for r, factor, _ in compatible:
        b = m.bits(r)
        gp = tuple((0, 1) if j == factor else (1, 0) for j in range(3))
        for s in itertools.product((0, 1), repeat=8):
            t = tuple(b[i] + 2 * s[i] for i in range(8))
            F, ok = m.build(t, gp, False)
            checked_lifts += 1
            if not ok:
                nonintegral_builds += 1
                continue
            integral_builds += 1
            if (F[4][0] & 1) != 1 or (F[4][9] & 1) != 1:
                raise ValueError("integral fixed-gluing build lost the Smith source bit")

    if integral_builds == 0:
        raise ValueError("conditional adapter vacuous: no integral parity-compatible build")

    historical = {r: f for r, f, _ in compatible if r in selected}
    if historical != selected:
        raise ValueError("historical residue/factor alignment regression")

    out = {
        "schema": "STAGE32_32_01_178_SMITH_TRANSVECTION_UNIVERSAL_MOD2_PREFLIGHT_V1",
        "source_locks": {
            "source_pr": 1728,
            "hostile_review": 5147627146,
            "audited_exact_head": AUDITED_HEAD,
            "builder_blob_sha1": BUILDER_BLOB,
            "fixed_gluing_alignment_blob_sha1": ALIGN_BLOB,
        },
        "fixed_x8_gluing_input": {
            "transvection_action_count": 3,
            "center_to_prym_factor_alignment": {"73": 0, "97": 1, "235": 2},
            "historical_q602_norms_used_in_this_test": False,
            "historical_projection_degrees_used_in_this_test": False,
            "historical_Q_state_used_in_this_test": False,
        },
        "full_ring_mod2_replay": {
            "ambient_ring_residue_count": 256,
            "transvection_compatible_residue_count": len(compatible),
            "counts_by_selected_prym_factor": {str(k): len(v) for k, v in by_factor.items()},
            "all_transvection_compatible_residues_force_source_bit_one": True,
            "source_bit_formula": "a12+b12+indicator(selected_prym_factor==middle) mod2",
        },
        "integral_gluing_parity_replay": {
            "gaussian_parity_representatives": {"identity_type": [1, 0], "i_type": [0, 1]},
            "mod4_lifts_checked": checked_lifts,
            "integral_builds": integral_builds,
            "nonintegral_builds": nonintegral_builds,
            "all_integral_builds_have_F40_eq_F49_eq_1_mod2": True,
            "why_norm_independent_at_this_layer": "The fixed-gluing divisibility and the Smith source bit depend only on the block entries modulo two; odd Gaussian norm magnitudes are not used.",
        },
        "smith_consequence": {
            "certified_smith_coordinate": 0,
            "coordinate_formula": "B[4,4] mod2",
            "conditional_value": 1,
            "conditional_nonzero_cokernel_class": True,
            "scope": "Any integral fixed-X8 H-equivariant assembly in the audited cellular basis whose invariant A[2] action is one of the three 05AC transvections and whose Prym action is aligned by the fixed anti-isometry has nonzero Smith coordinate 0.",
        },
        "interpretation": {
            "v6_specific_norm_137_9_9_is_needed_for_this_mod2_obstruction": False,
            "q602_numeric_shell_is_needed_after_transvection_type_is_supplied": False,
            "current_full178_semantic_adapter_established": False,
            "remaining_bridge": "Show that a current FULL178 carrier supplies the same fixed-X8 common-cover/H-equivariant assembly and one of the three audited transvection action types. Pair-mass parity alone is not yet that semantic lift.",
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
