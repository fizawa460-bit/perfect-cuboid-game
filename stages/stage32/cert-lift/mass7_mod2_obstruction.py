#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5_HANDOFF = ROOT / "stages/stage32-ex5/cut-handoff"
sys.path.insert(0, str(EX5_HANDOFF))

import e8_terminal_population_adapter as e8

PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
NORMAL_COUNT = 92
TARGET_D = 8
TARGET_E = 8


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def row_sum(m: Matrix, labels: list[int]) -> Matrix:
    out = Matrix.zeros(1, m.cols)
    for label in labels:
        out += m.row(label - 1)
    return out


def load_picard_interface() -> tuple[Matrix, list[list[list[int]]]]:
    d18 = e8.d18
    bundle = d18.load_retained(d18.RETAINED, "s32certlift_mass7_bundle")
    marking = d18.load_retained(d18.MARKING, "s32certlift_mass7_marking")
    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    gram = Matrix(bundle["picard_gram_64x64"])
    req(P.shape == (140, 64), "Picard pairing shape drift")
    req(coords.shape == (140, 64) and gram.shape == (64, 64), "retained Picard shape drift")
    full = coords * gram * coords.T

    blocks: list[list[list[int]]] = []
    fibre_coeffs = []
    for pack in PACKS:
        seen: list[int] = []
        factor_blocks: list[list[int]] = []
        funcs = []
        for boundary in pack:
            inc = [j for j in range(93, 141) if int(full[boundary - 1, j - 1]) == 1]
            req(len(inc) == 8, f"incidence regression boundary {boundary}")
            seen.extend(inc)
            factor_blocks.append(inc)
            funcs.append(2 * P.row(boundary - 1) + row_sum(P, inc))
        req(sorted(seen) == list(range(93, 141)), "fibre exceptional partition regression")
        req(all(f == funcs[0] for f in funcs[1:]), "fibre functional regression")
        blocks.append(factor_blocks)
        fibre_coeffs.append(funcs[0])
    req(
        19 * (fibre_coeffs[0] + fibre_coeffs[1])
        == row_sum(P, list(range(1, 93))) + 5 * row_sum(P, list(range(93, 141))),
        "degree-sum functional regression",
    )
    return P, blocks


def left_kernel_mod2(P: Matrix) -> list[list[int]]:
    # Nullspace of P^T over F2. These rows are exact parity constraints on y in im(P mod 2).
    a = [[int(P[col, row]) & 1 for col in range(P.rows)] for row in range(P.cols)]
    nrows, ncols = len(a), len(a[0])
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(nrows):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == nrows:
            break
    pset = set(pivots)
    basis: list[list[int]] = []
    for free in (c for c in range(ncols) if c not in pset):
        v = [0] * ncols
        v[free] = 1
        for i, pc in enumerate(pivots):
            v[pc] = a[i][free]
        req(
            not any(sum(v[i] * int(P[i, j]) for i in range(P.rows)) & 1 for j in range(P.cols)),
            "left-kernel replay failed mod2",
        )
        basis.append(v)
    return basis


def consistency_masks(kernel: list[list[int]], unknown_normal_labels: list[int]) -> list[int]:
    # A*x=b is consistent iff every zero row of an RREF transform annihilates b.
    m = len(kernel) + 1
    rows: list[list[int]] = []
    for eq, h in enumerate(kernel):
        abit = 0
        for j, label in enumerate(unknown_normal_labels):
            if h[label - 1] & 1:
                abit |= 1 << j
        rows.append([abit, 1 << eq])
    total_abit = (1 << len(unknown_normal_labels)) - 1
    rows.append([total_abit, 1 << (m - 1)])

    pivot_row = 0
    for col in range(len(unknown_normal_labels)):
        bit = 1 << col
        pivot = next((i for i in range(pivot_row, m) if rows[i][0] & bit), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        for i in range(m):
            if i != pivot_row and (rows[i][0] & bit):
                rows[i][0] ^= rows[pivot_row][0]
                rows[i][1] ^= rows[pivot_row][1]
        pivot_row += 1
    masks = [transform for abit, transform in rows if abit == 0]
    req(masks, "projected mod2 system unexpectedly has no consistency equations")
    return masks


def parity_system_consistent(
    kernel: list[list[int]],
    masks: list[int],
    exceptional: dict[int, int],
    boundary_normal: dict[int, int],
) -> bool:
    bmask = 0
    for eq, h in enumerate(kernel):
        rhs = 0
        for label, value in exceptional.items():
            rhs ^= (h[label - 1] & 1) & (int(value) & 1)
        for label, value in boundary_normal.items():
            rhs ^= (h[label - 1] & 1) & (int(value) & 1)
        if rhs:
            bmask |= 1 << eq
    # Normal total is 112, hence parity zero.
    total_rhs = sum(int(v) for v in boundary_normal.values()) & 1
    if total_rhs:
        bmask |= 1 << len(kernel)
    return all(((mask & bmask).bit_count() & 1) == 0 for mask in masks)


def exceptional_completions(fixed: dict[int, int]):
    mass = sum(fixed.values())
    residual = TARGET_E - mass
    req(residual in (0, 1), "MASS7 extractor only accepts fixed mass 7 or 8")
    free = [label for label in range(93, 141) if label not in fixed]
    if residual == 0:
        y = {label: 0 for label in range(93, 141)}
        y.update(fixed)
        yield None, y
        return
    for label in free:
        y = {j: 0 for j in range(93, 141)}
        y.update(fixed)
        y[label] = 1
        yield label, y


def boundary_candidates(
    exceptional: dict[int, int], blocks: list[list[list[int]]]
):
    sums = [[sum(exceptional[j] for j in inc) for inc in pack] for pack in blocks]
    for n1 in range(TARGET_D + 1):
        n2 = TARGET_D - n1
        ns = [n1, n2]
        boundary: dict[int, int] = {}
        ok = True
        for pack_index, pack in enumerate(PACKS):
            n = ns[pack_index]
            for boundary_label, s in zip(pack, sums[pack_index]):
                if s > n or ((n - s) & 1):
                    ok = False
                    break
                boundary[boundary_label] = (n - s) // 2
            if not ok:
                break
        if not ok:
            continue
        # This is the exact CUT pairwise incidence inequality.
        if any(a + b > TARGET_D for a in sums[0] for b in sums[1]):
            continue
        yield n1, n2, boundary, sums


def block_mod2_obstructed(
    block_index: int,
    idx,
    blocks: list[list[list[int]]],
    kernel: list[list[int]],
    masks: list[int],
) -> tuple[bool, dict | None, int]:
    sig = e8.block_signature(block_index, idx)
    fixed = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
    mass = int(sig["fixed_exceptional_mass"])
    req(mass >= 7, "block_mod2_obstructed called below MASS7")
    attempted = 0
    for residual_label, exceptional in exceptional_completions(fixed):
        for n1, n2, boundary, sums in boundary_candidates(exceptional, blocks):
            attempted += 1
            if parity_system_consistent(kernel, masks, exceptional, boundary):
                return False, {
                    "block_index": block_index,
                    "fixed_exceptional_mass": mass,
                    "residual_exceptional_label": residual_label,
                    "fibre_degrees": [n1, n2],
                    "boundary_normal_pairings": {str(k): v for k, v in sorted(boundary.items())},
                    "incidence_sums": sums,
                    "meaning": "survives exact exceptional/fibre constraints and the projected Picard64 mod2 relaxation; this is not an integral completion witness",
                }, attempted
    return True, None, attempted


def run(scope: str) -> dict:
    P, blocks = load_picard_interface()
    kernel = left_kernel_mod2(P)
    boundary_labels = sorted({b for pack in PACKS for b in pack})
    unknown_normal_labels = [label for label in range(1, NORMAL_COUNT + 1) if label not in boundary_labels]
    masks = consistency_masks(kernel, unknown_normal_labels)
    idx = e8.indexer()
    current_main = set(e8.current_main_survivor_block_indices())
    universe = (
        sorted(current_main)
        if scope == "current-main"
        else list(range(e8.UNFILTERED_BLOCK_COUNT))
    )

    targeted = 0
    obstructed = 0
    attempted_completions = 0
    counterexamples = []
    h = hashlib.sha256()
    by_mass = {"7": {"targeted": 0, "obstructed": 0}, "8": {"targeted": 0, "obstructed": 0}}
    for block_index in universe:
        sig = e8.block_signature(block_index, idx)
        mass = int(sig["fixed_exceptional_mass"])
        if mass < 7:
            continue
        targeted += 1
        by_mass[str(mass)]["targeted"] += 1
        blocked, witness, attempts = block_mod2_obstructed(block_index, idx, blocks, kernel, masks)
        attempted_completions += attempts
        if blocked:
            obstructed += 1
            by_mass[str(mass)]["obstructed"] += 1
            h.update(f"{block_index}\n".encode())
        elif len(counterexamples) < 32:
            counterexamples.append(witness)

    status = (
        "PASS_MASS7_EXACT_MOD2_OBSTRUCTION"
        if targeted > 0 and obstructed == targeted
        else "COUNTEREXAMPLE_MASS7_NOT_PROVED_BY_THIS_MOD2_PROJECTION"
    )
    out = {
        "schema": "STAGE32_CERTLIFT_MASS7_MOD2_OBSTRUCTION_V1",
        "stage": "32",
        "node": "CERTLIFT-02",
        "status": status,
        "scope": scope,
        "target": {
            "row_id": "g1-d008",
            "g": 1,
            "d": 8,
            "e": 8,
            "predicate": "fixed_exceptional_mass >= 7",
            "population_kind": "current-MAIN N220/N355 prefix survivors" if scope == "current-main" else "entire compressed e8 terminal block universe before current-MAIN prefix filtering",
        },
        "method": {
            "z3_or_cp_sat_used": False,
            "finite_ring": 2,
            "picard_condition": "exact membership in im(P mod 2) via the full left kernel of P^T",
            "exceptional_completion": "exact because e=8 and fixed mass 7/8 leaves residual exceptional mass 1/0",
            "fibre_constraints": "exactly enumerate n1+n2=8 and solve 2*y_boundary+incidence_sum=n_pack before parity projection",
            "normal_projection": "eliminate the 80 non-boundary normal parities; retained consistency masks are necessary conditions only, hence any contradiction is a sound UNSAT certificate",
        },
        "matrix": {
            "picard_pairing_shape": [P.rows, P.cols],
            "left_kernel_dimension_mod2": len(kernel),
            "unknown_nonboundary_normal_count": len(unknown_normal_labels),
            "projected_consistency_mask_count": len(masks),
            "projected_consistency_masks_sha256": csha(masks),
        },
        "result": {
            "targeted_blocks": targeted,
            "mod2_obstructed_blocks": obstructed,
            "counterexample_count": targeted - obstructed,
            "first_counterexamples": counterexamples,
            "attempted_exact_exceptional_fibre_completions": attempted_completions,
            "obstructed_block_stream_sha256": h.hexdigest(),
            "by_fixed_exceptional_mass": by_mass,
        },
        "credit": {
            "certlift_l2_candidate": status.startswith("PASS_"),
            "stage32_main_pruning_credit": False,
            "theorem_credit": False,
            "stage32_closure_credit": False,
            "merge_authorized": False,
        },
        "firewalls": {
            "no_cross_e_extrapolation": True,
            "no_timeout_semantics": True,
            "no_unknown_relabel": True,
            "bounded_e8_family_only": True,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", choices=["current-main", "unfiltered"], default="current-main")
    ap.add_argument("--output", type=Path)
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()
    out = run(args.scope)
    text = json.dumps(out, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    if args.self_check:
        print(json.dumps({
            "status": out["status"],
            "targeted_blocks": out["result"]["targeted_blocks"],
            "obstructed_blocks": out["result"]["mod2_obstructed_blocks"],
            "counterexamples": out["result"]["counterexample_count"],
            "canonical": out["canonical_sha256_without_this_field"],
        }, sort_keys=True))
    elif not args.output:
        print(text, end="")


if __name__ == "__main__":
    main()
