#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIAG = ROOT / "stages" / "stage32" / "residual-32-01-production" / "diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py"


def main() -> None:
    p = subprocess.run([sys.executable, "-B", str(DIAG)], cwd=ROOT, check=True, capture_output=True, text=True)
    x = json.loads(p.stdout)
    g = x["coordinate_W1_W2_W3_C_recovery"]
    covers = g["global_four_hyperplane_exact_covers"]
    profiles = Counter(tuple(sorted(int(v) for v in c["exceptional_mass_sums"])) for c in covers)
    all_masses = [int(v) for c in covers for v in c["exceptional_mass_sums"]]
    out = {
        "mode": "SCRATCH_POST1648AV_CANONICAL_COORDINATE_HYPERPLANE_COMPACT_SUMMARY",
        "single_hyperplane_candidate_count": int(g["single_hyperplane_candidate_count"]),
        "exact_cover_count": len(covers),
        "mass_profiles": [
            {"profile": list(k), "cover_count": v} for k, v in sorted(profiles.items())
        ],
        "distinct_mass_profile_count": len(profiles),
        "per_hyperplane_exceptional_mass_min": min(all_masses),
        "per_hyperplane_exceptional_mass_max": max(all_masses),
        "all_per_hyperplane_masses_lt_186": max(all_masses) < 186,
        "every_cover_mass_sum": sorted({sum(int(v) for v in c["exceptional_mass_sums"]) for c in covers}),
        "every_cover_normal_sum": sorted({sum(int(v) for v in c["rational_intersection_sums"]) for c in covers}),
        "firewalls": {"scratch_only": True, "v6_carrier_excluded": False},
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
