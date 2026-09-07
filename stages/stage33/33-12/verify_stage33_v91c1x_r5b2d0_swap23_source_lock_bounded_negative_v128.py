#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2d0-swap23-source-lock-bounded-negative.json"
R2 = HERE / "e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json"
C3 = HERE / "e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json"
MAIN_STATE = HERE.parent / "MAIN-STATE.json"

R2_SHA = "912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1"
C3_SHA = "a49f7a77ad9aad10714e556503dbd5a84585c8f1c92241b9213d3e439819ca50"
BLOCKER = "LITERAL_SOURCE_BOUND_SWAP23_ACTION_ON_AMBIENT_COORDINATES_OR_EQUIVALENT_SOURCE_SIDE_MARKING_DATA"


def csha(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def check_embedded(obj: dict, expected: str, label: str) -> None:
    claimed = obj.get("canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"{label} canonical lock moved: claimed={claimed} actual={actual}")


def apply_tau(poly: dict[str, int], tau: dict[str, str]) -> dict[str, int]:
    out: dict[str, int] = {}
    for x, coeff in poly.items():
        y = tau[x]
        out[y] = out.get(y, 0) + coeff
    return {k:v for k,v in out.items() if v}


def main() -> None:
    r2 = json.loads(R2.read_text(encoding="utf-8"))
    c3 = json.loads(C3.read_text(encoding="utf-8"))
    state = json.loads(MAIN_STATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))

    check_embedded(c3, C3_SHA, "C3")
    x_r2 = state["continuation_provenance"]["x_r2_chain_construction_contract"]
    if x_r2["certificate_sha256"] != R2_SHA:
        raise SystemExit("MAIN-STATE R2 canonical lock moved")

    claimed = cert.get("canonical_sha256")
    body = dict(cert)
    body.pop("canonical_sha256", None)
    if csha(body) != claimed:
        raise SystemExit("B2D0 canonical sha invalid")

    if cert["schema"] != "stage33.e3.v91c1x_r5b2d0.swap23_source_lock_bounded_negative.v1":
        raise SystemExit("B2D0 schema moved")
    if cert["candidate"] != "V91C1X_R5B2D0_SWAP23_SOURCE_LOCK_BOUNDED_NEGATIVE":
        raise SystemExit("B2D0 candidate moved")
    if cert["entry"]["authority"] != "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT":
        raise SystemExit("authority moved")
    if cert["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("Stage33 progress moved")
    if cert["source_locks"]["r2_contract_canonical_sha256"] != R2_SHA:
        raise SystemExit("B2D0 R2 lock moved")
    if cert["source_locks"]["r5b2c3_canonical_sha256"] != C3_SHA:
        raise SystemExit("B2D0 C3 lock moved")

    target = cert["target_side_candidate"]
    tau = target["tau_coordinate_map"]
    coords = target["coordinate_order"]
    quadrics = target["pinned_quadrics_square_term_coefficients"]
    for x in coords:
        if tau[tau[x]] != x:
            raise SystemExit("tau^2 != id")
    expected_action = {"F1":"F3", "F2":"F2", "F3":"F1", "F4":"F4"}
    recomputed_action = {}
    for name, poly in quadrics.items():
        acted = apply_tau(poly, tau)
        matches = [target_name for target_name, target_poly in quadrics.items() if acted == target_poly]
        if len(matches) != 1:
            raise SystemExit(f"independent target action unresolved for {name}: {matches}")
        recomputed_action[name] = matches[0]
    if recomputed_action != expected_action or target["quadric_action"] != expected_action:
        raise SystemExit("target quadric action moved")
    if target["ambient_surface_automorphism_exact"] is not True:
        raise SystemExit("target automorphism exactness lost")
    if target["source_bound_a2_02_action_identification"] is not False:
        raise SystemExit("target/source firewall violated")

    disc = cert["bounded_discovery"]
    if disc["literal_source_bound_swap23_action_locator_obtained"] is not False:
        raise SystemExit("source locator unexpectedly claimed")
    for key in [
        "repository_wide_absence_claim",
        "mathematical_nonexistence_claim",
        "search_miss_proves_repository_absence",
        "search_miss_proves_mathematical_nonexistence",
    ]:
        if disc[key] is not False:
            raise SystemExit(f"bounded-search firewall violated: {key}")
    if len(disc["queries"]) != 2:
        raise SystemExit("bounded discovery ledger moved")

    exact = cert["exact_consequence"]
    if exact["target_ambient_swap23_candidate_exact"] is not True:
        raise SystemExit("target candidate exactness lost")
    if exact["target_candidate_alone_satisfies_r2_source_transport_requirement"] is not False:
        raise SystemExit("R2 source-transport firewall violated")
    if exact["r5b2c3_all_double_overlap_atlas_available"] is not True:
        raise SystemExit("C3 infrastructure lost")
    if exact["r5b2d_cover_action_or_common_refinement_blocked"] is not True:
        raise SystemExit("B2D blocker lost")
    if exact["blocker"] != BLOCKER:
        raise SystemExit("blocker string moved")

    for key, value in cert["credit_firewall"].items():
        if value is not False:
            raise SystemExit(f"credit firewall violated: {key}")

    r2req = r2["swap23_action_requirements"]
    if not r2req["cover_action_or_common_refinement_explicit"]:
        raise SystemExit("R2 cover action requirement moved")
    if not r2req["same_representative_transport_explicit"]:
        raise SystemExit("R2 representative transport requirement moved")
    if not r2req["package_permutation_assumption_forbidden"]:
        raise SystemExit("R2 package-permutation firewall moved")
    if c3["construction_status"]["swap23_cover_action_or_common_refinement_materialized"] is not False:
        raise SystemExit("C3 source action unexpectedly promoted")

    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B2D0_SWAP23_SOURCE_LOCK_BOUNDED_NEGATIVE_VERIFIED",
        "certificate_sha256": claimed,
        "blocker": BLOCKER,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
