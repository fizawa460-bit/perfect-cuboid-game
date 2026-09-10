#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from pathlib import Path

from sympy import Matrix

import verify_smith_current_factor_parity_reduction as fac
import verify_smith_pair_mass_image_classifier as cls


def nullspace_gf2(rows: list[tuple[int, ...]], n: int) -> list[tuple[int, ...]]:
    a = [list(int(v) & 1 for v in row) for row in rows]
    pivots: list[int] = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    free = [c for c in range(n) if c not in pivots]
    out = []
    for f in free:
        x = [0] * n
        x[f] = 1
        for i in range(len(pivots) - 1, -1, -1):
            p = pivots[i]
            x[p] = sum(a[i][j] * x[j] for j in free) & 1
        out.append(tuple(x))
    return out


def apply_forms(forms: list[tuple[int, ...]], x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(a * b for a, b in zip(row, x)) & 1 for row in forms)


def main() -> None:
    bundle = fac.load_retained(fac.RETAINED, "s32_smith_residual_bundle")
    marking = fac.load_retained(fac.MARKING, "s32_smith_residual_marking")
    if bundle.get("canonical_sha256") != fac.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("bundle regression")
    if marking.get("canonical_sha256") != fac.EXPECTED_MARKING_CANONICAL:
        raise ValueError("marking regression")

    adapter = fac.hia.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    # Exact first factor fibre functional, matching N352/factor-parity replay.
    pack = fac.BOUNDARY_PACKS[0]
    fibre_rows = []
    fibre_blocks = []
    for label in pack:
        inc = [j for j in range(93, 141) if int(full[label - 1, j - 1]) == 1]
        if len(inc) != 8:
            raise ValueError("special-fibre incidence regression")
        fibre_rows.append(2 * coords.row(label - 1) + fac.row_sum(coords, inc))
        fibre_blocks.append(inc)
    if any(F != fibre_rows[0] for F in fibre_rows[1:]):
        raise ValueError("factor fibre equivalence regression")
    f1 = fac.gf2_row([int(v) for v in list(fibre_rows[0] * gram)])

    _, degree_col, _, _, _ = fac.hia._parse_hperp(marking["hperp_text"])
    basis_labels = fac.hia.RETAINED_BASIS_KNOWN_LABELS_1BASED
    degree = [int(degree_col[label - 1, 0]) for label in basis_labels]
    e_total = fac.isum_rows(P, list(range(93, 141)))
    row_by_label = {label: [int(P[label - 1, j]) for j in range(64)] for label in range(1, 141)}
    obs = [fac.gf2_row(degree), fac.gf2_row(e_total), fac.gf2_row(row_by_label[49])]
    obs += [fac.gf2_row(row_by_label[label]) for label in fac.CURRENT_EXCEPTIONAL_PREFIX]
    obs_factor = obs + [f1]

    pair_rows = [fac.gf2_row(fac.isum_rows(P, fac.PAIR_EXCEPTIONAL_LABELS[key])) for key in fac.PAIR_KEYS]
    residual_rank = fac.gf2_rank(obs_factor + pair_rows) - fac.gf2_rank(obs_factor)
    if residual_rank != 1:
        raise ValueError(f"expected residual rank one, got {residual_rank}")

    # The uncertainty in the 12-bit signature at fixed current observables+factor parity
    # is T(ker O). It must be exactly one nonzero direction.
    kernel = nullspace_gf2(obs_factor, 64)
    deltas = {apply_forms(pair_rows, x) for x in kernel}
    deltas.discard((0,) * 12)
    if len(deltas) != 1:
        raise ValueError(f"expected one residual signature direction, got {len(deltas)}")
    delta = next(iter(deltas))

    # Enumerate the exact 8-signature image and quotient it by the residual direction.
    columns = [tuple(pair_rows[i][j] for i in range(12)) for j in range(64)]
    image_basis = cls.independent_basis(columns)
    if len(image_basis) != 3:
        raise ValueError("pair-signature image rank regression")
    signatures = sorted({
        cls.xor(*(image_basis[i] for i, b in enumerate(mask) if b)) if any(mask) else (0,) * 12
        for mask in itertools.product((0, 1), repeat=3)
    })
    if len(signatures) != 8:
        raise ValueError("pair-signature count regression")

    # Use one exact special-fibre decomposition to read factor parity from a signature.
    pair_by_set = {frozenset(v): i for i, v in enumerate(fac.PAIR_EXCEPTIONAL_LABELS.values())}
    first_block = set(fibre_blocks[0])
    factor_pair_indices = sorted(idx for s, idx in pair_by_set.items() if s.issubset(first_block))
    if len(factor_pair_indices) != 2:
        raise ValueError("factor block / pair-group split regression")

    seen = set()
    fibres = []
    for sig in signatures:
        if sig in seen:
            continue
        mate = tuple(a ^ b for a, b in zip(sig, delta))
        if mate not in signatures:
            raise ValueError("residual mate leaves exact signature image")
        seen.add(sig)
        seen.add(mate)
        members = sorted([sig, mate])
        classes = [cls.classify_signature(s) for s in members]
        forbidden = [bool(c["single_transposition"]) for c in classes]
        fbits = [s[factor_pair_indices[0]] ^ s[factor_pair_indices[1]] for s in members]
        if fbits[0] != fbits[1]:
            raise ValueError("residual direction changed fixed factor parity")
        fibres.append({
            "members": [list(s) for s in members],
            "factor_parity": fbits[0],
            "single_transposition_flags": forbidden,
            "single_transpositions": [c["nontrivial_cycles"] if c["single_transposition"] else [] for c in classes],
            "forbidden_member_count": sum(forbidden),
            "all_members_smith_forbidden": all(forbidden),
        })

    fibres.sort(key=lambda x: (x["factor_parity"], x["members"]))
    counts = {k: sum(1 for f in fibres if f["forbidden_member_count"] == k) for k in (0, 1, 2)}

    # Equality strata have n1=n2=d/2. Count rows by forced parity only; this is not
    # a prefix-coset census and grants no pruning credit.
    manifest = json.loads((fac.ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json").read_text())
    row_ids = [str(v) for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])) for v in ids]
    if len(row_ids) != 178 or len(set(row_ids)) != 178:
        raise ValueError("FULL178 row population regression")
    equality_parity_counts = {0: 0, 1: 0}
    for row_id in row_ids:
        d = int(row_id.split("-d", 1)[1])
        equality_parity_counts[(d // 2) & 1] += 1

    out = {
        "schema": "STAGE32_32_01_178_SMITH_FACTOR_PARITY_RESIDUAL_SIGNATURE_FIBRES_V1",
        "status": "PROVISIONAL_EXACT_LINEAR_ALGEBRA_NO_MAIN_CREDIT",
        "exact": {
            "pair_signature_image_rank": 3,
            "pair_signature_count": 8,
            "residual_rank_after_current_plus_factor_parity": residual_rank,
            "residual_signature_delta": list(delta),
            "residual_fibre_count": len(fibres),
            "fibre_forbidden_member_count_distribution": counts,
            "all_forbidden_fibre_count": counts[2],
            "mixed_fibre_count": counts[1],
            "all_allowed_fibre_count": counts[0],
            "factor_pair_indices_0based_used": factor_pair_indices,
            "fibres": fibres,
        },
        "hurwitz_equality": {
            "equality_strata_count": 178,
            "forced_factor_parity_counts": {str(k): v for k, v in equality_parity_counts.items()},
            "this_is_not_prefix_coset_census": True,
        },
        "interpretation": {
            "last_pair_group_bit_globally_necessary_for_exact_signature": counts[1] > 0,
            "some_observable_fibres_are_prunable_without_last_bit": counts[2] > 0,
            "next_route_if_all_forbidden_fibres_exist": "Census current prefix+factor-parity observable cosets and prune only cosets landing in an all-forbidden residual fibre; otherwise materialize the last pair-group bit.",
            "next_route_if_none": "Materialize one true pair-group parity on the Hurwitz-equality subfrontier before exact Smith pruning census.",
        },
        "credit": {
            "main_pruning_credit": False,
            "n350_producer_registration": False,
            "full178_completion": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_claim": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = fac.csha(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
