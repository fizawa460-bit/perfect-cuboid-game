#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648x-florit-smith-richelot-e2-marking-nonadapter.json"
EXPECTED = "eacdd1f74d8d010136596c833c197f281e352890a3c0e768147046642dd62bf6"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def load_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file()
    assert blob_sha1(path) == lock["git_blob_sha1"]
    doc = json.loads(path.read_text())
    assert canonical(doc) == lock["canonical_sha256"]
    return doc


def perm_from_cycles(n: int, cycles: list[list[int]]) -> tuple[int, ...]:
    p = list(range(n + 1))
    for cyc in cycles:
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            p[a] = b
    return tuple(p)


def orbit(seed: int, perms: list[tuple[int, ...]]) -> set[int]:
    out = {seed}
    changed = True
    while changed:
        changed = False
        for p in perms:
            new = {p[x] for x in out}
            if not new <= out:
                out |= new
                changed = True
    return out


cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED

w = load_lock(cert["source_locks"]["post1648W"])
pr = load_lock(cert["source_locks"]["principal_rosati"])
source_note = cert["source_locks"]["source_note"]
assert blob_sha1(ROOT / source_note["path"]) == source_note["git_blob_sha1"]

assert w["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert w["decision"]["survivors_current_credit"] == [73, 97, 235]
assert pr["principal_polarization"]["principal"] is True
assert pr["principal_polarization"]["product_polarization"] is False

replay = cert["kernel_orbit_replay"]
perms = [perm_from_cycles(15, replay["generator_permutations"][name]) for name in ("sigma", "rho", "omega")]
got_orbit = sorted(orbit(1, perms))
assert got_orbit == [1, 4, 8, 9, 12, 13]
assert got_orbit == replay["orbit_of_K1"]
assert replay["orbit_size"] == 6
assert replay["single_kernel_selected_by_reduced_automorphism_group"] is False

sem = cert["semantic_nonadapter"]
assert sem["richelot_kernel_order"] == 4
assert sem["richelot_kernel_lies_in_source_J2"] is True
assert sem["restriction_to_source_J2_injective"] is False
assert sem["invertible_A2_marking_obtained"] is False
assert sem["atlas_target_is_product_ppas"] is True
assert sem["retained_stage32_principal_polarization_is_product"] is False
assert sem["underlying_E2_species_match_promoted_to_marked_ppav_identification"] is False
assert sem["actual_conjugating_g_matrix_or_A2_action_materialized"] is False

dec = cert["decision"]
assert dec["florit_smith_richelot_e2_route_materialized"] is True
assert dec["florit_smith_route_supplies_actual_marked_g"] is False
assert dec["florit_smith_route_selects_absolute_W_line"] is False
assert dec["absolute_delta0inf_retained_W_line_identified"] is False
assert dec["survivors_current_credit"] == [73, 97, 235]
assert dec["Q602_excluded"] is False
assert dec["O210_excluded"] is False
assert dec["O212_plus_advance_allowed"] is False
assert not any(cert["firewalls"].values())

ledger = cert["candidate_ledger_update"]
assert ledger["closed_this_leaf"]["status"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert len(ledger["remaining_untested"]) == 2
assert ledger["receiver_parked"] is False

print("POST1648X_FLORIT_SMITH_RICHELOT_E2_MARKING_NONADAPTER_COMPLETE")
print(f"certificate_canonical={EXPECTED}")
print("bolza_typeVI_to_E2=degree4_(2,2)_isogeny kernel_orbit=1,4,8,9,12,13")
print("kernel_order=4 restriction_on_J2_noninjective=true product_ppas_vs_retained_nonproduct_ppav=true")
print("actual_marked_g=false absolute_W_line=false survivors=73,97,235")
