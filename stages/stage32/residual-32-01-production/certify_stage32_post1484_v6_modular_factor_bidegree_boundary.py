#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

V6_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
ALL140_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
INCIDENCE_BLOB = "b3f673aa73324ee731356eec2c0448592fd1e59b"
INCIDENCE_CANONICAL = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
SATAKE_BLOB = "83cb5e2019d1bf8a7bb98e7426c90f898cca56c3"
SATAKE_CANONICAL = "69a2a6d3cdf7b0d5c6162424a8102ec41cd09ac7e303469d30577d454363e31d"
SOURCE_NOTE_BLOB = "deeecac5599f3b542b445cd87c2070dae488bc85"
LOCAL_ADAPTER_BLOB = "dd5fdb8d2553d25a1479c1e5cff68a201c8396e3"
LOCAL_ADAPTER_CANONICAL = "318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328"

FIRST = [34, 35, 38, 39, 42, 43]
SECOND = [33, 36, 37, 40, 41, 44]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def locked_json(path: Path, blob: str) -> dict:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return json.loads(raw)


def locked_text(path: Path, blob: str) -> str:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return raw.decode()


def canonical_without_field(obj: dict, field: str) -> str:
    body = dict(obj)
    body.pop(field, None)
    return csha(body)


def local_cusp_ramification_delta(m: int) -> int:
    if m <= 0:
        raise ValueError("contact multiplicity must be positive")
    return m - 1 if m % 2 else m - 2


def nodewise_m1_m2_count(capacities: list[int], twos: int) -> int:
    dp = {0: 1}
    for t in capacities:
        nd: defaultdict[int, int] = defaultdict(int)
        for used, count in dp.items():
            for k2 in range(t // 2 + 1):
                nd[used + k2] += count
        dp = dict(nd)
    return dp.get(twos, 0)


def build(repo: Path) -> dict:
    here = repo / "stages/stage32/residual-32-01-production"
    v6 = locked_json(repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json", V6_BLOB)
    if v6.get("canonical_sha256_without_this_field") != V6_CANONICAL:
        raise ValueError("V6 canonical moved")
    all140 = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(all140) != 140 or csha(all140) != ALL140_SHA or v6["witness"].get("all140_pairings_sha256") != ALL140_SHA:
        raise ValueError("V6 all140 vector moved")
    capacities = all140[92:]
    if len(capacities) != 48 or sum(capacities) != 266:
        raise ValueError("V6 exceptional capacity vector moved")

    incidence = locked_json(here / "post1473-x8-marked-exceptional-incidence.json", INCIDENCE_BLOB)
    if incidence.get("canonical_sha256_without_this_field") != INCIDENCE_CANONICAL:
        raise ValueError("exceptional incidence canonical moved")
    inc_rows = incidence.get("rows", [])
    if len(inc_rows) != 48:
        raise ValueError("exceptional incidence row count moved")
    by_exc = {int(r["exceptional_label"]): r for r in inc_rows}
    if sorted(by_exc) != list(range(93, 141)):
        raise ValueError("exceptional incidence labels moved")

    satake = locked_json(here / "post1473-x8-satake-boundary-marking.json", SATAKE_BLOB)
    if satake.get("canonical_sha256") != SATAKE_CANONICAL:
        raise ValueError("Satake marking canonical moved")
    factor = satake["factor_marking"]
    if factor["first_factor_cusp_z_fixed_curves"] != FIRST or factor["second_factor_cusp_w_fixed_curves"] != SECOND:
        raise ValueError("Satake factor labels moved")

    note = locked_text(here / "post1484-v6-modular-factor-bidegree-source-note.md", SOURCE_NOTE_BLOB)
    required_note = (
        "div(x) = 2 L_p + E",
        "div(z) = 2 L_q + E",
        "8 n_i = 2 q' m_i",
        "`m_z=105`, `m_w=81`",
        "`O>=210`",
    )
    missing = [s for s in required_note if s not in note]
    if missing:
        raise ValueError(f"source note semantics moved: {missing}")

    # Hostile-audit repair: independently source-lock and replay the local
    # cusp/contact ramification lower-bound adapter used at O=210.  This is
    # an input lock only; the old O=188 search is not reopened.
    local_cert = locked_json(here / "post1473-o188-cusp-ramification-budget.json", LOCAL_ADAPTER_BLOB)
    claimed_local = local_cert.get("canonical_sha256_without_this_field")
    if claimed_local != LOCAL_ADAPTER_CANONICAL or canonical_without_field(local_cert, "canonical_sha256_without_this_field") != LOCAL_ADAPTER_CANONICAL:
        raise ValueError("local cusp lower-bound adapter canonical moved")
    if local_cert.get("source_lock", {}).get("arxiv") != "1303.6495":
        raise ValueError("local cusp lower-bound primary-source lock moved")
    if "Section 3 proof of Theorem 3.1" not in local_cert.get("source_lock", {}).get("locators", []):
        raise ValueError("local cusp lower-bound source locator moved")
    adapter = local_cert.get("local_adapter", {})
    expected_adapter = {
        "notation": "A_i=a_i/4 and m=min(A1,A2)=exceptional contact multiplicity.",
        "parity": "A1 and A2 have the same parity; hence their parity equals the parity of m.",
        "total_lower_bound": "R_i >= qprime * sum_P delta(m_P), where delta(m)=m-1 for odd m and m-2 for even m.",
    }
    for key, expected in expected_adapter.items():
        if adapter.get(key) != expected:
            raise ValueError(f"local cusp lower-bound adapter field moved: {key}")
    if adapter.get("odd_contact", {}).get("forced_ramification_on_D_per_N_branch") != "qprime*(A_i-1) >= qprime*(m-1)":
        raise ValueError("odd-contact local lower bound moved")
    if adapter.get("even_contact", {}).get("forced_ramification_on_D_per_N_branch") != "qprime*(A_i-2) >= qprime*(m-2)":
        raise ValueError("even-contact local lower bound moved")
    for m in range(1, 267):
        expected = m - 1 if m % 2 else m - 2
        if local_cusp_ramification_delta(m) != expected or expected < 0:
            raise ValueError(f"local cusp lower-bound replay moved at m={m}")
    zero_delta_contacts = [m for m in range(1, 267) if local_cusp_ramification_delta(m) == 0]
    if zero_delta_contacts != [1, 2]:
        raise ValueError(f"zero-defect contact set moved: {zero_delta_contacts}")

    incident_mass: defaultdict[int, int] = defaultdict(int)
    incident_labels: defaultdict[int, list[int]] = defaultdict(list)
    for label in range(93, 141):
        row = by_exc[label]
        cap = capacities[label - 93]
        a = int(row["first_factor_boundary_label"])
        b = int(row["second_factor_boundary_label"])
        if a not in FIRST or b not in SECOND:
            raise ValueError(f"factor incidence moved at exceptional {label}")
        for boundary in (a, b):
            incident_mass[boundary] += cap
            incident_labels[boundary].append(label)

    rows = []
    for boundary in FIRST + SECOND:
        excs = incident_labels[boundary]
        if len(excs) != 8:
            raise ValueError(f"boundary {boundary} no longer has eight exceptional incidences")
        c_dot_l = all140[boundary - 1]
        fiber_degree = 2 * c_dot_l + incident_mass[boundary]
        rows.append({
            "boundary_label": boundary,
            "factor": "first_z" if boundary in FIRST else "second_w",
            "C_dot_L": c_dot_l,
            "incident_exceptional_labels": excs,
            "incident_exceptional_mass": incident_mass[boundary],
            "C_dot_resolved_cusp_fiber": fiber_degree,
        })

    first_degrees = [r["C_dot_resolved_cusp_fiber"] for r in rows if r["factor"] == "first_z"]
    second_degrees = [r["C_dot_resolved_cusp_fiber"] for r in rows if r["factor"] == "second_w"]
    if first_degrees != [105] * 6 or second_degrees != [81] * 6:
        raise ValueError(f"resolved cusp-fiber bidegree moved: {first_degrees}, {second_degrees}")
    m_z, m_w = 105, 81

    q1 = [Fraction(m_z, 4), Fraction(m_w, 4)]
    q2 = [Fraction(m_z, 2), Fraction(m_w, 2)]
    q4 = [Fraction(m_z, 1), Fraction(m_w, 1)]
    if all(x.denominator == 1 for x in q1) or all(x.denominator == 1 for x in q2):
        raise ValueError("qprime 1/2 integrality obstruction disappeared")
    if [int(x) for x in q4] != [105, 81]:
        raise ValueError("qprime=4 degree transport moved")

    o_min = (8 * max(m_z, m_w) + 4 - 1) // 4
    if o_min != 210:
        raise ValueError(f"O lower wall moved: {o_min}")
    r_source = [4 * o_min - 8 * m_z, 4 * o_min - 8 * m_w]
    if r_source != [0, 192]:
        raise ValueError(f"O210 source ramification moved: {r_source}")
    if any(x % 4 for x in r_source):
        raise ValueError("V4 ramification descent divisibility moved")
    r_desc = [x // 4 for x in r_source]
    if r_desc != [0, 48]:
        raise ValueError("O210 descended ramification moved")

    # R=0 on the first projection and qprime=4 imply
    # sum_P delta(m_P)=0.  The exact replay above proves delta>=0 for all
    # positive m<=e and delta=0 exactly at m=1,2.  Since O counts odd
    # contacts, all O=210 odd contacts are m=1; the remaining exceptional
    # mass 266-210 must be carried by m=2 contacts.
    if r_source[0] != 0:
        raise ValueError("first projection ceased to be etale at O210")
    if [m for m in zero_delta_contacts if m % 2] != [1] or [m for m in zero_delta_contacts if m % 2 == 0] != [2]:
        raise ValueError("zero-defect odd/even contact classification moved")
    even_mass = 266 - o_min
    if even_mass < 0 or even_mass % 2:
        raise ValueError("O210 residual exceptional mass moved")
    even_contacts = even_mass // 2
    if o_min + 2 * even_contacts != 266 or even_contacts != 28:
        raise ValueError("O210 forced m1/m2 histogram moved")
    if o_min * local_cusp_ramification_delta(1) + even_contacts * local_cusp_ramification_delta(2) != 0:
        raise ValueError("O210 zero-defect histogram replay failed")
    assignment_count = nodewise_m1_m2_count(capacities, even_contacts)
    if assignment_count != 43949136035405189:
        raise ValueError(f"O210 nodewise count moved: {assignment_count}")

    result = {
        "schema": "STAGE32_POST1484_V6_MODULAR_FACTOR_BIDEGREE_BOUNDARY_V1",
        "stage": 32,
        "leaf": "POST1484_FIXED_V6_MODULAR_FACTOR_BIDEGREE_AND_O210_WALL",
        "status": "PROVISIONAL_EXACT_REPLAY_PENDING_HOSTILE_AUDIT",
        "fixed_target": {"row_id": "g1-d186", "d": 186, "e": 266, "z": [-15, 62, -44, 26, 32]},
        "source_locks": {
            "v6_witness": {
                "path": "stages/stage32/32-21/post1473-v6-witness-body-recovered.json",
                "blob_sha1": V6_BLOB,
                "canonical_sha256": V6_CANONICAL,
                "all140_pairings_sha256": ALL140_SHA,
            },
            "exceptional_incidence": {
                "path": "stages/stage32/residual-32-01-production/post1473-x8-marked-exceptional-incidence.json",
                "blob_sha1": INCIDENCE_BLOB,
                "canonical_sha256": INCIDENCE_CANONICAL,
            },
            "satake_boundary_marking": {
                "path": "stages/stage32/residual-32-01-production/post1473-x8-satake-boundary-marking.json",
                "blob_sha1": SATAKE_BLOB,
                "canonical_sha256": SATAKE_CANONICAL,
            },
            "source_note": {
                "path": "stages/stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-source-note.md",
                "blob_sha1": SOURCE_NOTE_BLOB,
            },
            "primary_source": {
                "authors": ["Eberhard Freitag", "Riccardo Salvati Manni"],
                "title": "Parametrization of the box variety by theta functions",
                "arxiv": "1303.6495v1",
                "doi": "10.1307/mmj/1480734014",
                "locators": [
                    "Section 2 Theorem 2.4",
                    "Section 2 Proposition 2.5",
                    "Section 2 Proposition 2.7",
                    "Section 4 Lemma 4.1",
                ],
            },
        },
        "resolved_cusp_fiber_intersections": rows,
        "modular_factor_bidegree": {"first_z": 105, "second_w": 81, "sum": 186, "both_nonconstant": True},
        "product_cover_degree_transport": {
            "formula": "8*n_i=2*qprime*m_i",
            "qprime_1": {"possible": False, "reason": "105/4 and 81/4 are nonintegral"},
            "qprime_2": {"possible": False, "reason": "105/2 and 81/2 are nonintegral"},
            "qprime_4": {"possible": True, "projection_degrees": [105, 81]},
        },
        "new_O_wall": {
            "qprime": 4,
            "riemann_hurwitz_inequality": "4*O >= 8*max(105,81)",
            "provisional_O_min": 210,
            "O188_all_product_cover_profiles_excluded": True,
            "prior_O188_named_B_C_frontier_superseded_as_active_leaf": True,
        },
        "O210_extremal_profile": {
            "source_projection_ramification_totals": [0, 192],
            "descended_projection_ramification_totals": [0, 48],
            "forced_contact_histogram": {"m1_odd": 210, "m2_even": 28, "all_other_contacts": 0, "B": 238},
            "nodewise_assignment_count": assignment_count,
            "nodewise_assignment_reachable": True,
            "semantics": "exact coarse nodewise nonexclusion only; not analytic branch realization",
        },
        "verdict": {
            "fixed_V6_qprime_1_excluded": True,
            "fixed_V6_qprime_2_excluded": True,
            "fixed_V6_qprime_4_requires_O_at_least_210": True,
            "fixed_V6_O188_closed_if_audited": True,
            "fixed_V6_all_integral_genus1_carriers_closed": False,
            "next_exact_leaf": "O210_Q4_FIRST_PROJECTION_ETALE_GEOMETRY",
        },
        "firewalls": {
            "O210_profile_is_not_analytic_realization": True,
            "provisional_is_not_audited": True,
            "full178_authorized": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_claim": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check", type=Path)
    args = ap.parse_args()
    result = build(args.repo)
    if args.check:
        committed = json.loads(args.check.read_text())
        if committed != result:
            raise ValueError("committed modular-factor bidegree certificate differs from replay")
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("STAGE32_POST1484_V6_MODULAR_FACTOR_BIDEGREE_BOUNDARY=PASS")
    print("LOCAL_CUSP_LOWER_BOUND_ADAPTER=SOURCE_LOCKED_REPLAY_PASS")
    print("LOCAL_CUSP_ZERO_DEFECT_CONTACTS=1,2")
    print("MODULAR_FACTOR_BIDEGREE=105,81")
    print("QPRIME1_2=EXCLUDED_BY_DEGREE_INTEGRALITY")
    print("QPRIME4_O_MIN=210")
    print("O210_CONTACT_HISTOGRAM=210x1+28x2")
    print(f"O210_NODEWISE_ASSIGNMENT_COUNT={result['O210_extremal_profile']['nodewise_assignment_count']}")
    print(f"CANONICAL={result['canonical_sha256_without_this_field']}")


if __name__ == "__main__":
    main()
