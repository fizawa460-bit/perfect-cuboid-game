#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[2]
ST32R = ROOT / "stages" / "stage32" / "residual-32-01-production"
ST33 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"

sys.path.insert(0, str(ST32R))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402
from pairing_prefix_engine import close_permutation_group  # noqa: E402


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "ex6_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "ex6_base")
    gram = Matrix(bundle["picard_gram_64x64"])
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    if coords.shape != (140, 64):
        raise ValueError(f"all140 coordinate shape regression: {coords.shape}")

    raw_perms = marking["aut_action"]["permutations_1based"]
    group0 = close_permutation_group(raw_perms)
    if len(group0) != 1536:
        raise ValueError(f"Aut group order regression: {len(group0)}")

    def pair(i1: int, j1: int) -> int:
        x = Matrix([[int(coords[i1 - 1, k]) for k in range(64)]])
        y = Matrix([[int(coords[j1 - 1, k]) for k in range(64)]])
        return int((x * gram * y.T)[0, 0])

    v6 = json.loads(V6_PATH.read_text())
    if v6["canonical_sha256_without_this_field"] != "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8":
        raise ValueError("V6 canonical regression")
    vp = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(vp) != 140:
        raise ValueError("V6 all140 length regression")

    def analyze(name: str, c3_labels: tuple[int, int]) -> dict:
        common_exc = tuple(
            e for e in range(93, 141)
            if pair(c3_labels[0], e) == 1 and pair(c3_labels[1], e) == 1
        )
        if len(common_exc) != 4:
            raise ValueError(f"{name}: expected four common exceptional curves, got {common_exc}")
        if pair(*c3_labels) != 0:
            raise ValueError(f"{name}: resolved C3 components should be disjoint")
        support = tuple(sorted(c3_labels + common_exc))
        rep_degree = sum(vp[i - 1] for i in support)

        orbit_supports = {
            tuple(sorted(gp[i - 1] + 1 for i in support))
            for gp in group0
        }
        degrees = []
        for mapped in sorted(orbit_supports):
            normals = [x for x in mapped if 45 <= x <= 92]
            excs = [x for x in mapped if 93 <= x <= 140]
            if len(normals) != 2 or len(excs) != 4:
                raise ValueError(f"{name}: Aut support-type regression at {mapped}")
            degrees.append(sum(vp[i - 1] for i in mapped))
        counts = Counter(degrees)
        return {
            "c3_labels": list(c3_labels),
            "common_exceptional_labels": list(common_exc),
            "resolved_special_fiber_support": list(support),
            "representative_v6_degree": rep_degree,
            "distinct_special_fiber_supports": len(orbit_supports),
            "degree_min": min(degrees),
            "degree_max": max(degrees),
            "distinct_degrees": sorted(counts),
            "degree_multiplicities": {str(k): counts[k] for k in sorted(counts)},
            "supports_with_degree_at_least_133": sum(d >= 133 for d in degrees),
            "supports_with_degree_at_least_134": sum(d >= 134 for d in degrees),
        }

    # Representative of the orbit coming from the next six rank-4 quadrics:
    # fib3 at t=0 is a1+a2=b2-b1=0 and splits into C3 labels 46,48.
    next_six = analyze("NEXT_SIX_RANK4_FIB3_T0", (46, 48))

    # Representative of the last four rank-4 quadrics:
    # fib4 at t=0 is b1+i*b2=sqrt(2)c-b3=0. In the retained C3 ordering this
    # splits into the two family-6 curves with (e3,e2,e1)=(1,-1,1) and
    # (-1,-1,-1), namely labels 87 and 92.
    last_four = analyze("LAST_FOUR_RANK4_FIB4_T0", (87, 92))

    overall_max = max(next_six["degree_max"], last_four["degree_max"], 105)
    result = {
        "schema": "STAGE32_EX6_RANK4_FIBRATION_ORBIT_DEGREE_DIAGNOSTIC_V2",
        "status": "EXPLORATORY_EXACT_DIAGNOSTIC_NO_MAIN_CREDIT",
        "source_locks": {
            "stoll_testa_verification_repo_cuboids_magma_blob": "0422b69847f2afb97cb7b3ed02ebef91279f61b1",
            "stoll_testa_section5_log_blob": "9cfef75aa58335655d6ae3e78597f5924b6c2433",
            "v6_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "v6_all140_pairings_sha256": v6["witness"]["all140_pairings_sha256"],
            "hperp_adapter_canonical_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "retained_aut_group_order": len(group0),
        },
        "rank4_orbit_types": {
            "known_isotrivial_pair": {"degrees": [81, 105], "degree_max": 105},
            "next_six_quadrics": next_six,
            "last_four_quadrics": last_four,
        },
        "summary": {
            "largest_v6_fibration_degree_seen_across_all_rank4_types": overall_max,
            "new_rank4_type_beats_known_degree_105": overall_max > 105,
            "new_rank4_type_reaches_133": max(next_six["degree_max"], last_four["degree_max"]) >= 133,
            "new_rank4_type_reaches_134": max(next_six["degree_max"], last_four["degree_max"]) >= 134,
        },
        "firewalls": {
            "arbitrary_rank4_fibration_degree_implies_O_ge_2degree": False,
            "new_fibration_O_adapter_proved": False,
            "O266_excluded": False,
            "V6_carrier_excluded": False,
            "stage32_main_changed": False,
            "runner_side_giant_payload_import_only": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
