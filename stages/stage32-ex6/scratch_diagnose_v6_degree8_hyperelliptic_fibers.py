#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

FIXED_CONIC_ROWS = [17, 21, 24, 25, 26, 28, 30, 31]
FULL_INTERSECTION_SHA256 = "3e967406344d7b13027a25bafa832701f76f028a77f4a1dfa7bd0ebc0cdf1f4e"
V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
V6_ALL140_SHA256 = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module_payload(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load module {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--witness", type=Path, required=True)
    ap.add_argument("--adapter-dir", type=Path, required=True)
    args = ap.parse_args()

    sys.path.insert(0, str(args.adapter_dir))
    from hperp_integral_adapter import _parse_hperp, _recover_full_intersection, matrix_list
    from pairing_prefix_engine import close_permutation_group

    marking = load_module_payload(args.marking, "stage32ex6_hyp_marking")
    hperp_text = marking.get("hperp_text")
    if not isinstance(hperp_text, str):
        raise ValueError("retained marking missing hperp_text")
    q, degree, linear, _caps, hmeta = _parse_hperp(hperp_text)
    full = _recover_full_intersection(q, degree, linear)
    if full.rows != 140 or full.cols != 140 or full != full.T:
        raise ValueError(f"unexpected full intersection shape/symmetry: {full.shape}")
    full_sha = csha(matrix_list(full))
    if full_sha != FULL_INTERSECTION_SHA256:
        raise ValueError(f"full intersection hash moved: {full_sha}")
    if hmeta.get("upstream_git_blob_sha1") != UPSTREAM_BLOB:
        raise ValueError("upstream Stoll-Testa blob moved")

    witness = json.loads(args.witness.read_text())
    if witness.get("canonical_sha256_without_this_field") != V6_CANONICAL:
        raise ValueError("V6 witness canonical hash moved")
    vp = [int(x) for x in witness["witness"]["all140_pairings"]]
    if len(vp) != 140 or csha(vp) != V6_ALL140_SHA256:
        raise ValueError("V6 all140 pairings moved")

    raw_perms = marking["aut_action"]["permutations_1based"]
    group = close_permutation_group(raw_perms)
    if len(group) != 1536:
        raise ValueError(f"Aut(S) group order regression: {len(group)}")

    def pair(i1: int, j1: int) -> int:
        return int(full[i1 - 1, j1 - 1])

    # Last-four rank-4 fibration representative, source-locked by the existing
    # EX6 rank4 diagnostic. Its split bad fiber is two C3 components plus the
    # four exceptional components common to them.
    c3_rep = (87, 92)
    common_exc = tuple(e for e in range(93, 141) if pair(c3_rep[0], e) == pair(c3_rep[1], e) == 1)
    if common_exc != (133, 135, 137, 139):
        raise ValueError(f"last-four representative exceptional regression: {common_exc}")
    split_rep = tuple(sorted(c3_rep + common_exc))

    orbit_supports = {
        tuple(sorted(gp[i - 1] + 1 for i in split_rep))
        for gp in group
    }
    if len(orbit_supports) != 48:
        raise ValueError(f"expected 48 split supports, got {len(orbit_supports)}")

    def class_pairings(labels: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(sum(int(full[i - 1, j]) for i in labels) for j in range(140))

    by_class: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for support in sorted(orbit_supports):
        by_class[class_pairings(support)].append(support)
    if len(by_class) != 8 or any(len(v) != 6 for v in by_class.values()):
        raise ValueError(f"last-four fibration class regression: {[len(v) for v in by_class.values()]}")

    class_outputs = []
    all_candidate_keys = set()
    total_candidate_count = 0
    total_negative_d1 = 0

    for fpair, supports in sorted(by_class.items(), key=lambda kv: min(kv[1])):
        supports = sorted(supports)
        union_exc = sorted({i for s in supports for i in s if 93 <= i <= 140})
        if len(union_exc) != 24:
            raise ValueError(f"split exceptional union should have 24 rows: {union_exc}")
        remaining_exc = [i for i in range(93, 141) if i not in union_exc]
        if len(remaining_exc) != 24:
            raise ValueError("remaining exceptional count regression")

        # Any split support is the complete resolved fiber class.
        f_support = supports[0]
        f_self = sum(fpair[i - 1] for i in f_support)
        if f_self != 0:
            raise ValueError(f"fibration class should square to zero, got {f_self}")
        f_v6_degree = sum(vp[i - 1] for i in f_support)

        candidates = []
        for p, qrow in itertools.combinations(remaining_exc, 2):
            rpair = tuple(
                fpair[j] - int(full[p - 1, j]) - int(full[qrow - 1, j])
                for j in range(140)
            )
            r_self = (
                f_self
                - 2 * fpair[p - 1]
                - 2 * fpair[qrow - 1]
                + int(full[p - 1, p - 1])
                + int(full[qrow - 1, qrow - 1])
                + 2 * int(full[p - 1, qrow - 1])
            )
            f_dot_r = f_self - fpair[p - 1] - fpair[qrow - 1]
            if r_self != -4 or f_dot_r != 0:
                continue
            if rpair[p - 1] != 2 or rpair[qrow - 1] != 2:
                continue
            if min(rpair) < 0:
                continue

            c_dot_r = f_v6_degree - vp[p - 1] - vp[qrow - 1]
            fixed_conic_dot_r = sum(rpair[r - 1] for r in FIXED_CONIC_ROWS)
            # Source theorem: these candidates are degree-8 genus-3 cores, so K.R=8.
            d1_dot_r = c_dot_r - 8 - fixed_conic_dot_r
            key = rpair
            all_candidate_keys.add(key)
            candidates.append(
                {
                    "exceptional_pair": [p, qrow],
                    "C_dot_R": c_dot_r,
                    "fixed_eight_conics_dot_R": fixed_conic_dot_r,
                    "D1_dot_R": d1_dot_r,
                    "zero_known140_rows": [j + 1 for j, x in enumerate(rpair) if x == 0],
                }
            )

        total_candidate_count += len(candidates)
        total_negative_d1 += sum(c["D1_dot_R"] < 0 for c in candidates)
        pair_occ = Counter(i for c in candidates for i in c["exceptional_pair"])
        perfect_matching = (
            len(candidates) == 12
            and set(pair_occ) == set(remaining_exc)
            and all(pair_occ[i] == 1 for i in remaining_exc)
        )
        d1_hist = Counter(c["D1_dot_R"] for c in candidates)
        c_hist = Counter(c["C_dot_R"] for c in candidates)
        class_outputs.append(
            {
                "fibration_v6_degree": f_v6_degree,
                "split_supports": [list(s) for s in supports],
                "split_exceptional_union": union_exc,
                "remaining_exceptionals": remaining_exc,
                "candidate_pair_count": len(candidates),
                "candidate_pairs_form_perfect_matching": perfect_matching,
                "candidate_C_dot_R_histogram": {str(k): v for k, v in sorted(c_hist.items())},
                "candidate_D1_dot_R_histogram": {str(k): v for k, v in sorted(d1_hist.items())},
                "negative_D1_candidate_count": sum(c["D1_dot_R"] < 0 for c in candidates),
                "candidates": candidates,
            }
        )

    output = {
        "schema": "STAGE32EX6_SCRATCH_V6_DEGREE8_HYPERELLIPTIC_FIBER_RECONSTRUCTION_V1",
        "status": "EXPLORATORY_EXACT_LATTICE_RECONSTRUCTION_NO_ENDPOINT_CREDIT",
        "source_locks": {
            "full_intersection_sha256": full_sha,
            "hperp_text_sha256": hmeta.get("hperp_text_sha256"),
            "stoll_testa_upstream_git_blob_sha1": hmeta.get("upstream_git_blob_sha1"),
            "v6_canonical_sha256": V6_CANONICAL,
            "v6_all140_pairings_sha256": V6_ALL140_SHA256,
            "retained_aut_group_order": len(group),
        },
        "model": {
            "last_four_rank4_fibration_count": 8,
            "split_G3_fibers_per_fibration": 6,
            "hyperelliptic_degree8_genus3_fibers_per_fibration": 12,
            "expected_hyperelliptic_orbit_size": 96,
            "candidate_class_formula": "R = F - E_p - E_q",
            "canonical_degree_K_dot_R": 8,
        },
        "last_four_fibration_classes": class_outputs,
        "summary": {
            "fibration_class_count": len(class_outputs),
            "candidate_pair_total": total_candidate_count,
            "distinct_candidate_numerical_classes": len(all_candidate_keys),
            "all_classes_recover_12_pair_perfect_matching": all(
                c["candidate_pairs_form_perfect_matching"] for c in class_outputs
            ),
            "negative_D1_candidate_total": total_negative_d1,
            "D1_nonnegative_on_all_reconstructed_candidates": total_candidate_count > 0 and total_negative_d1 == 0,
            "global_nefness_proved": False,
            "O266_endpoint_excluded": False,
            "O264_descent_authorized": False,
            "stage32_main_advanced": False,
        },
        "firewalls": {
            "candidate_scan_claims_full_degree8_curve_classification": False,
            "hyperelliptic_lattice_candidates_promoted_to_geometric_curves_without_source_identification": False,
            "nonnegative_degree8_scan_promoted_to_global_nefness": False,
            "scratch_result_promoted_to_main": False,
        },
    }
    output["canonical_sha256_without_this_field"] = csha(output)
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
