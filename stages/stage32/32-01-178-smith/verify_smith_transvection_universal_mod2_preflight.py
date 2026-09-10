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
AA_PATH = "stages/stage32-ex1/verify_ex1_05aa_q602_mod4_isotropic_glue_kernel_action.py"
AA_BLOB = "60fe8ae8624986c3f36f4e7e11db3dd141695854"
ALIGN_PATH = "stages/stage32-ex1/ex1-05ac-fixed-x8-polarization-kernel-antiisometry-transvection-alignment-preflight.json"
ALIGN_BLOB = "74a9d76faf652b5f40eb6b5b1b3244071a0d24b5"

A2_GENS = [(2,0,0,0),(0,2,0,0),(0,0,1,0),(0,0,0,1)]


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


def matvec(M, v, mod=None):
    out = [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]
    return out if mod is None else [x % mod for x in out]


def rlinear_matrix_mod4(t):
    a11,b11,a12,b12,a21,b21,a22,b22 = t
    return [
        [a11,a12,-2*b11,-2*b12],
        [a21,a22,-2*b21,-2*b22],
        [b11,b12,a11,a12],
        [b21,b22,a21,a22],
    ]


def encode_A2(x):
    x = tuple(a % 4 for a in x)
    return ((x[0] // 2) & 1, (x[1] // 2) & 1, x[2] & 1, x[3] & 1)


def action_A2(t):
    # Exact 05AA quotient model:
    # A[2]={x in J[4]: 2x in W}/W, basis [2e1,2e2,r e1,r e2].
    M = rlinear_matrix_mod4(t)
    cols = [encode_A2(matvec(M, g, 4)) for g in A2_GENS]
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))


def main() -> None:
    m = load_builder()
    # Source-lock the exact verifier from which action_A2 above is copied.
    git_show(AA_PATH, AA_BLOB)
    align = json.loads(git_show(ALIGN_PATH, ALIGN_BLOB))
    actions = {
        int(k): tuple(tuple(int(x) for x in row) for row in v)
        for k, v in align["q602_transvection_centers"]["actions_rows"].items()
    }
    selected = {73: 0, 97: 1, 235: 2}

    for r in (73, 97, 235):
        if action_A2(m.bits(r)) != actions[r]:
            raise ValueError(f"audited A[2] quotient action regression for residue {r}")

    action_to_factor = {actions[r]: selected[r] for r in selected}
    if len(action_to_factor) != 3:
        raise ValueError("three transvection actions unexpectedly collide")

    # Enumerate the entire retained 8-bit ring-coordinate cube, not just Q(T)=602.
    # Matching is done in the audited quotient A[2] basis, not in the integral
    # H1 basis used by the later 05AF builder.
    compatible = []
    by_factor = {0: [], 1: [], 2: []}
    for r in range(256):
        b = m.bits(r)
        action = action_A2(b)
        if action not in action_to_factor:
            continue
        factor = action_to_factor[action]
        middle_gaussian_b = int(factor == 1)
        smith_source_bit = (b[2] + b[3] + middle_gaussian_b) & 1
        compatible.append((r, factor, smith_source_bit))
        by_factor[factor].append(r)

    if not compatible:
        raise ValueError("no transvection-compatible ring residues found")
    if any(bit != 1 for _, _, bit in compatible):
        bad = [(r, f, bit) for r, f, bit in compatible if bit != 1]
        raise ValueError(f"transvection action does not force Smith source bit: {bad[:20]}")

    # The 05AF quotient-gluing integrality condition and the tracked Smith source
    # entries depend only on block parity.  Use odd-norm parity representatives
    # id=(1,0) and i=(0,1), with the i-type factor fixed by the audited 05AC
    # anti-isometry.  These are parity probes only; no historical norm is claimed.
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
        "schema": "STAGE32_32_01_178_SMITH_TRANSVECTION_UNIVERSAL_MOD2_PREFLIGHT_V2",
        "source_locks": {
            "source_pr": 1728,
            "hostile_review": 5147627146,
            "audited_exact_head": AUDITED_HEAD,
            "builder_blob_sha1": BUILDER_BLOB,
            "a2_quotient_action_verifier_blob_sha1": AA_BLOB,
            "fixed_gluing_alignment_blob_sha1": ALIGN_BLOB,
        },
        "fixed_x8_gluing_input": {
            "A2_basis": ["2e1","2e2","r*e1","r*e2"],
            "transvection_action_count": 3,
            "center_to_prym_factor_alignment": {"73": 0, "97": 1, "235": 2},
            "historical_q602_norms_used_in_this_test": False,
            "historical_projection_degrees_used_in_this_test": False,
            "historical_Q_state_used_in_this_test": False,
        },
        "full_ring_mod2_replay": {
            "ambient_ring_residue_count": 256,
            "transvection_compatible_residue_count": len(compatible),
            "compatible_residues": [r for r,_,_ in compatible],
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
            "why_norm_independent_at_this_layer": "The fixed-gluing divisibility and tracked Smith source entries are tested on all mod-4 lifts with the same block parities; historical odd Gaussian norm magnitudes are not used.",
        },
        "smith_consequence": {
            "certified_smith_coordinate": 0,
            "coordinate_formula": "B[4,4] mod2",
            "conditional_value": 1,
            "conditional_nonzero_cokernel_class": True,
            "scope": "Any integral fixed-X8 H-equivariant assembly in the audited cellular basis whose invariant A[2] action equals one of the three 05AC absolute transvections and whose Prym action is aligned by the fixed anti-isometry has nonzero Smith coordinate 0.",
        },
        "interpretation": {
            "v6_specific_norm_137_9_9_is_needed_for_this_mod2_obstruction": False,
            "q602_numeric_shell_is_needed_after_absolute_transvection_action_is_supplied": False,
            "absolute_transvection_action_alone_selects_historical_three_ring_residues": len(compatible) == 3 and set(r for r,_,_ in compatible) == set(selected),
            "current_full178_semantic_adapter_established": False,
            "remaining_bridge": "Show that a current FULL178 carrier supplies the same fixed-X8 common-cover/H-equivariant assembly and one of the three audited absolute A[2] transvection actions. Pair-mass parity alone is not yet that semantic lift.",
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
