#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
DIAG = HERE / "diagnose_stage32_post1648bi_cc_fixed_mass_partition.py"
RESULT = HERE / "post1648bi-cc-fixed-mass-partition-scratch-result.json"
NOTE = HERE / "post1648bi-cc-fixed-mass-partition-source-note.md"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"

EXPECTED_V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_FIXED_WITHIN_48 = [
    1,2,3,4,5,6,7,8,
    25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
]
EXPECTED_MOVING = [
    ((9,14),(8,5)),
    ((10,13),(4,9)),
    ((11,16),(7,10)),
    ((12,15),(2,1)),
    ((17,22),(5,1)),
    ((18,21),(11,3)),
    ((19,24),(7,1)),
    ((20,23),(1,13)),
    ((41,46),(5,4)),
    ((42,45),(11,2)),
    ((43,48),(4,13)),
    ((44,47),(10,3)),
]


def main() -> None:
    v6 = json.loads(V6.read_text())
    if v6["canonical_sha256_without_this_field"] != EXPECTED_V6_CANONICAL:
        raise ValueError("V6 canonical regression")
    masses = [int(x) for x in v6["witness"]["all140_pairings"]][92:]
    if len(masses) != 48 or sum(masses) != 266:
        raise ValueError("V6 exceptional mass regression")

    committed = json.loads(RESULT.read_text())
    rerun = json.loads(subprocess.check_output([sys.executable, "-B", str(DIAG)], text=True))
    if rerun != committed:
        raise ValueError("committed BI result is not exact replay of diagnostic")

    if committed["mode"] != "SCRATCH_POST1648BI_CC_FIXED_MASS_PARTITION":
        raise ValueError("BI mode regression")
    if committed["source_locks"]["v6_canonical_sha256"] != EXPECTED_V6_CANONICAL:
        raise ValueError("BI V6 source lock regression")
    if committed["source_locks"]["bh_distinct_cc_equivariant_node_bijections"] != 256:
        raise ValueError("BH ambiguity cardinality regression")

    cc = committed["retained_complex_conjugation"]
    if cc["fixed_exceptional_count"] != 24 or cc["moving_pair_count"] != 12:
        raise ValueError("retained exceptional cc orbit-count regression")
    if cc["fixed_exceptional_labels_1based_within_48"] != EXPECTED_FIXED_WITHIN_48:
        raise ValueError("retained cc-fixed exceptional-label regression")

    got_moving = [
        (tuple(r["exceptional_labels_1based_within_48"]), tuple(r["masses"]))
        for r in cc["moving_pairs"]
    ]
    if got_moving != EXPECTED_MOVING:
        raise ValueError("retained cc-moving pair/mass regression")
    if not all(r["equal"] is False for r in cc["moving_pairs"]):
        raise ValueError("expected all 12 moving pairs to have unequal V6 masses")

    q = committed["v6"]
    if q["exceptional_mass_total"] != 266:
        raise ValueError("BI exceptional total regression")
    if (q["mass_on_source_cc_fixed_Q_nodes"], q["mass_on_source_cc_moving_Qi_nodes"]) != (126, 140):
        raise ValueError("BI Q/Q(i) aggregate mass partition regression")
    if q["moving_cc_pair_mass_mismatch_count"] != 12:
        raise ValueError("BI moving-pair mismatch count regression")
    if q["picard64_cc_invariant"] is not False or q["all140_pairings_cc_invariant"] is not False:
        raise ValueError("fixed V6 class unexpectedly became cc-invariant")

    decision = committed["decision"]
    if decision["q_fixed_vs_qi_moving_total_mass_partition_is_adapter_independent"] is not True:
        raise ValueError("adapter-independent aggregate partition regression")
    if decision["node_by_node_source_adapter_still_nonunique"] is not True:
        raise ValueError("BI incorrectly promotes node adapter uniqueness")
    if decision["v6_gal_qi_over_q_invariance_obtained"] is not False:
        raise ValueError("BI incorrectly promotes Gal(Q(i)/Q) invariance")
    if decision["next_exact_route"] != "V6_CLASS_IS_NOT_CC_INVARIANT_SO_DO_NOT_PROMOTE_Q_DEFINED_CARRIER_CONSTRAINTS_WITHOUT_A_SEPARATE_GALOIS_CLASS_ARGUMENT":
        raise ValueError("BI next-route regression")

    fw = committed["firewalls"]
    required_false = [
        "node_by_node_adapter_uniqueness_claimed",
        "full_Q_definedness_beyond_Gal_Qi_over_Q_claimed",
        "v6_carrier_excluded",
        "Q602_excluded",
        "O210_excluded",
        "O212_plus_advance_allowed",
    ]
    for key in required_false:
        if fw[key] is not False:
            raise ValueError(f"BI firewall regression: {key}")
    if fw["scratch_only"] is not True or fw["runner_side_import_only"] is not True:
        raise ValueError("BI scratch/runner-side firewall regression")
    if fw["giant_retained_payload_whole_fetch_used"] is not False:
        raise ValueError("BI giant-payload firewall regression")

    note = NOTE.read_text()
    required_note_fragments = [
        "f(Fix(sigma)) = Fix(tau)",
        "mass on the 24 conjugation-fixed nodes = 126",
        "mass on the 24 moving nodes = 140",
        "fixed V6 Picard class is **not** invariant",
        "is invalid and must remain closed",
        "This does not exclude a V6 genus-1 carrier",
    ]
    for fragment in required_note_fragments:
        if fragment not in note:
            raise ValueError(f"BI source-note scope regression: {fragment}")

    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1648BI_CC_FIXED_MASS_PARTITION_BOUNDED_WALL",
        "bh_distinct_maps": 256,
        "fixed_exceptional_count": 24,
        "moving_pair_count": 12,
        "q_fixed_mass": 126,
        "qi_moving_mass": 140,
        "moving_pair_mismatches": 12,
        "v6_cc_invariant": False,
        "v6_carrier_excluded": False,
        "Q602_excluded": False,
        "O210_excluded": False,
        "O212_plus_advance_allowed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
