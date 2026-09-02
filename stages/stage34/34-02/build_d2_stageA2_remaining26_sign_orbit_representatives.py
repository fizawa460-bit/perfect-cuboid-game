#!/usr/bin/env python3
from __future__ import annotations

import collections
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SIGN = ROOT / "d2-stageA2-sign-involution-remaining30-pair-lock.json"
PROMO = ROOT / "d2-stageA2-two-orbit-audit-promotion-certificate.json"
OUT = ROOT / "d2-stageA2-remaining26-sign-orbit-representatives-lock.json"


def sha256(path: pathlib.Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


sign = json.loads(SIGN.read_text())
promo = json.loads(PROMO.read_text())

assert sign["schema"] == "STAGE34_02B_D2_STAGEA2_SIGN_INVOLUTION_REMAINING30_PAIR_LOCK_V1"
assert sign["branch_count"] == 30 and sign["pair_count"] == 15 and len(sign["pairs"]) == 15
assert promo["schema"] == "STAGE34_02B_D2_STAGEA2_TWO_ORBIT_AUDIT_PROMOTION_CERTIFICATE_V1"
assert promo["status"] == "PASS_HOSTILE_AUDIT_PROMOTED_EXACT_FOUR_BRANCH_CLOSURE"
assert promo["promoted_closures"]["count"] == 4
assert promo["promoted_authoritative_state"]["remaining_branches"] == 26
assert promo["promoted_authoritative_state"]["remaining_sign_orbits"] == 13

closed = set(promo["promoted_closures"]["all"])
assert len(closed) == 4

records = []
remaining_branches = set()
closed_pairs = []
branch_by_q = collections.Counter()
orbit_by_q = collections.Counter()
class_counts = collections.Counter()
seen = set()

for pair in sign["pairs"]:
    left, right = pair["left"], pair["right"]
    lid, rid = left["branch_id"], right["branch_id"]
    assert lid not in seen and rid not in seen
    seen.update([lid, rid])

    in_left, in_right = lid in closed, rid in closed
    assert in_left == in_right, "promotion must remove complete audited sign orbits"
    if in_left:
        closed_pairs.append(sorted([lid, rid]))
        continue

    representative, partner = (left, right) if lid < rid else (right, left)
    rb0, rb1 = representative.get("rank_bounds"), partner.get("rank_bounds")
    rs0, rs1 = representative.get("rank_status"), partner.get("rank_status")

    if rb0 == [0, 2] and rb1 == [0, 2] and rs0 == "PASS_RANK_BOUNDS" and rs1 == "PASS_RANK_BOUNDS":
        arithmetic_class = "KNOWN_SELECTED_GENUS2_RANK_BOUNDS_0_2"
    else:
        assert rb0 is None and rb1 is None
        assert rs0 == "UNRESOLVED" and rs1 == "UNRESOLVED"
        arithmetic_class = "RANK_CENSUS_EXTERNAL_RESPONSE_UNRESOLVED"

    q = pair["q"]
    record = {
        "orbit_id": representative["branch_id"] + "__" + partner["branch_id"],
        "representative": representative["branch_id"],
        "partner": partner["branch_id"],
        "q": q,
        "triple": pair["triple"],
        "arithmetic_class": arithmetic_class,
        "representative_model_id": representative["model_id"],
        "representative_rank_bounds": representative.get("rank_bounds"),
        "representative_rank_status": representative.get("rank_status"),
        "representative_squareclass": representative["squareclass"],
        "partner_model_id": partner["model_id"],
        "partner_rank_bounds": partner.get("rank_bounds"),
        "partner_rank_status": partner.get("rank_status"),
        "partner_squareclass": partner["squareclass"],
    }
    records.append(record)
    remaining_branches.update([lid, rid])
    branch_by_q[q] += 2
    orbit_by_q[q] += 1
    class_counts[arithmetic_class] += 1

assert seen == {x[side]["branch_id"] for x in sign["pairs"] for side in ("left", "right")}
assert len(closed_pairs) == 2
assert set(x for pair in closed_pairs for x in pair) == closed
assert len(records) == 13 and len(remaining_branches) == 26
assert len({r["representative"] for r in records}) == 13
assert len({r["orbit_id"] for r in records}) == 13
assert class_counts == {
    "KNOWN_SELECTED_GENUS2_RANK_BOUNDS_0_2": 4,
    "RANK_CENSUS_EXTERNAL_RESPONSE_UNRESOLVED": 9,
}

expected_branches_by_q = {"20/99": 6, "24/7": 0, "48/55": 2, "60/11": 6, "80/39": 4, "84/13": 8}
actual_branches_by_q = {q: branch_by_q.get(q, 0) for q in expected_branches_by_q}
assert actual_branches_by_q == expected_branches_by_q
assert actual_branches_by_q == promo["promoted_authoritative_state"]["remaining_by_q"]
expected_orbits_by_q = {"20/99": 3, "24/7": 0, "48/55": 1, "60/11": 3, "80/39": 2, "84/13": 4}
actual_orbits_by_q = {q: orbit_by_q.get(q, 0) for q in expected_orbits_by_q}
assert actual_orbits_by_q == expected_orbits_by_q

records.sort(key=lambda r: r["representative"])

payload = {
    "schema": "STAGE34_02B_D2_STAGEA2_REMAINING26_SIGN_ORBIT_REPRESENTATIVES_LOCK_V1",
    "status": "PASS_EXACT_REMAINING_26_TO_13_AUDITED_SIGN_ORBITS",
    "sources": {
        "sign_pair_lock": SIGN.name,
        "sign_pair_lock_sha256": sha256(SIGN),
        "audit_promotion_certificate": PROMO.name,
        "audit_promotion_certificate_sha256": sha256(PROMO),
        "hostile_audit_review_id": promo["hostile_audit_review"]["review_id"],
        "audited_head": promo["audited_head"],
    },
    "closed_audited_sign_orbits_removed": sorted(closed_pairs),
    "remaining_branch_count": 26,
    "remaining_orbit_count": 13,
    "remaining_branches_by_q": actual_branches_by_q,
    "remaining_orbits_by_q": actual_orbits_by_q,
    "arithmetic_class_orbit_counts": dict(sorted(class_counts.items())),
    "representative_selection_rule": "lexicographically smaller branch_id in each audited sign orbit",
    "orbits": records,
    "next_use": "Run arithmetic only on the 13 listed representatives. A representative result may transfer to its partner only through the already hostile-audited sign involution and only after the representative result itself receives the required proof/audit credit.",
    "credit": "Exact residual-population compression and representative selection only. This lock closes zero additional branches.",
    "firewalls": {
        "representative_selection_is_branch_closure": False,
        "rank_bound_0_2_is_complete_pointset": False,
        "external_response_unresolved_is_math_failure": False,
        "remaining_26_closed": False,
        "D2_all_factor_branches_closed": False,
        "all_multiples_closed": False,
        "R29_EXT_CHANG_C_closed": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}

OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "status": payload["status"],
    "remaining_branches": 26,
    "remaining_orbits": 13,
    "class_counts": payload["arithmetic_class_orbit_counts"],
    "orbits_by_q": actual_orbits_by_q,
}, sort_keys=True))
