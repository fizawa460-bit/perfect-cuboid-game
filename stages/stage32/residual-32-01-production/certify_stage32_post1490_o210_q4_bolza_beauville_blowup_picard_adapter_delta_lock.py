#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical_sha256(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    cert = json.loads((ROOT / args.check).read_text())

    assert cert["schema"] == "STAGE32_POST1490_O210_Q4_BOLZA_BEAUVILLE_BLOWUP_PICARD_ADAPTER_DELTA_LOCK_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    locks = cert["source_locks"]

    witness_path = ROOT / locks["exact_v6_witness"]["path"]
    witness = json.loads(witness_path.read_text())
    assert blob_sha1(witness_path) == locks["exact_v6_witness"]["blob_sha1"]
    assert canonical_sha256(witness) == locks["exact_v6_witness"]["canonical_sha256"]
    assert witness["witness"]["picard_coordinates_sha256"] == locks["exact_v6_witness"]["picard_coordinates_sha256"]
    assert witness["witness"]["all140_pairings_sha256"] == locks["exact_v6_witness"]["all140_pairings_sha256"]

    note_path = ROOT / locks["beauville_odd_branch_wall"]["path"]
    assert blob_sha1(note_path) == locks["beauville_odd_branch_wall"]["blob_sha1"]
    note = note_path.read_text()
    for needle in [
        "the induced map `Xtilde -> Btilde` is a double cover ramified along the 48 exceptional curves",
        "exceptional intersection vector: the locked last 48 entries of the all-140 vector",
        "total exceptional intersection `e=C.E=266`",
    ]:
        assert needle in note

    mismatch_path = ROOT / locks["deck_object_mismatch"]["path"]
    mismatch = json.loads(mismatch_path.read_text())
    assert blob_sha1(mismatch_path) == locks["deck_object_mismatch"]["blob_sha1"]
    assert canonical_sha256(mismatch) == locks["deck_object_mismatch"]["canonical_sha256"]
    assert "including exceptional/branch corrections" in mismatch["open_bridge"]["next_target"]

    defect_path = ROOT / locks["v4_defect"]["path"]
    defect = json.loads(defect_path.read_text())
    assert blob_sha1(defect_path) == locks["v4_defect"]["blob_sha1"]
    assert canonical_sha256(defect) == locks["v4_defect"]["canonical_sha256"]
    ia = defect["intersection_arithmetic"]
    assert ia["D_square_formula"] == "D^2=-162+2*delta_D"
    assert ia["exact_defect_decomposition"] == "delta_D+c_g1+c_g2+c_g1_plus_g2=8586"

    hodge_path = ROOT / locks["hodge_constraint"]["path"]
    hodge = json.loads(hodge_path.read_text())
    assert canonical_sha256(hodge) == locks["hodge_constraint"]["canonical_sha256"]
    assert hodge["new_global_constraints"]["delta_D_upper_bound"] == 2206

    source_note_path = ROOT / locks["source_note"]["path"]
    assert blob_sha1(source_note_path) == locks["source_note"]["blob_sha1"]

    w = witness["witness"]
    assert w["self_intersection"] == 758
    pairings = w["all140_pairings"]
    assert len(pairings) == 140
    exc = pairings[-48:]
    assert exc == cert["exact_v6_inputs"]["exceptional_pairings_last48"]
    assert sum(exc) == 266 == cert["exact_v6_inputs"]["exceptional_mass"]
    sumsq = sum(m*m for m in exc)
    assert sumsq == 2358 == cert["exact_v6_inputs"]["exceptional_square_sum"]
    marked_delta = sum(m*(m-1)//2 for m in exc)
    assert marked_delta == 1046 == cert["exact_v6_inputs"]["marked_intrinsic_delta_from_multiplicity"]

    d2 = 2*w["self_intersection"] + sumsq
    assert d2 == 3874 == cert["x_side_exact_lock"]["D_square"]
    delta = (d2 + 162) // 2
    assert 2*delta == d2 + 162
    assert delta == 2018 == cert["x_side_exact_lock"]["delta_D"]
    assert delta - marked_delta == 972 == cert["x_side_exact_lock"]["intrinsic_delta_beyond_marked_multiplicity"]

    csum = 8586 - delta
    lo = delta - 80
    hi = 4333 - delta
    assert (csum, lo, hi) == (6568, 1938, 2315)
    hc = cert["hodge_corridor_collapse"]
    assert hc["deck_half_intersection_sum"] == csum
    assert hc["for_each_t_bounds"] == [lo, hi]
    assert hc["componentwise_lower_budget"] == delta + 3*lo == 7832
    assert hc["residual_slack_above_individual_hodge_floors"] == 8586 - (delta + 3*lo) == 754
    assert hc["additional_slack_reduction"] == 4642 - 754 == 3888

    rsum = 3*hi - csum
    assert rsum == 377 == hc["simplex_reparameterization"]["r_sum"]
    assert 4*(delta + hi) - 17334 == -2

    dec = cert["decision"]
    assert dec["delta_D_exactly_locked"] is True
    assert dec["O210_excluded"] is False
    assert dec["effectivity_proved"] is False
    assert cert["firewalls"]["arbitrary_B_picard64_promoted_to_picX"] is False
    assert cert["firewalls"]["post21bl_representative_sample_substituted"] is False

    print("PASS_EXACT_BEAUVILLE_BLOWUP_PICARD_ADAPTER_DELTA_LOCK")


if __name__ == "__main__":
    main()
