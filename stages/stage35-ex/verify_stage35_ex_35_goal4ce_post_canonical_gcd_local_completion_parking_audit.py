#!/usr/bin/env python3
"""Verify Goal4CE post-canonical-gcd parking audit."""
from __future__ import annotations

import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s
ART = P("stages/stage35-ex/35ex-35/goal4ce-post-canonical-gcd-local-completion-parking-audit.json")
SRC = P("stages/stage35-ex/35ex-35/goal4ce-post-canonical-gcd-local-completion-parking-audit-source-lock.md")
CD = P("stages/stage35-ex/35ex-35/goal4cd-canonical-e1-cross-gcd-p-d-local-square.json")
BS = P("stages/stage35-ex/35ex-35/goal4bs-post-boundary-derived-backup-parking-audit-source-lock.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "38852995a1f6d7a3a24a45443e07f243201217dc8572102ce013a2158e11174e"
SRC_BLOB = "f193c5eac223894292bc3ce653ca895e544228de"
CD_BLOB = "d5e3c335cfd715ddf07bb7c7ee0e8d3b905318f3"
BS_BLOB = "374a30ad8b69610120ee79ab40a8a517814a091c"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def euclid(a: int, b: int) -> tuple[int, int, int]:
    return a*a-b*b, 2*a*b, a*a+b*b


def data(tup: tuple[int, int, int, int]) -> dict:
    a, b, m, n = tup
    U1, V1, W1 = euclid(a, b)
    U2, V2, W2 = euclid(m, n)
    M = (V1*U2)**2 + (U1*V2)**2
    S = isqrt(M)
    assert S*S == M
    c = gcd(U1, U2)
    p = gcd(W1, V2)
    d = gcd(V1, W2)
    q = gcd(V1, V2)
    H = S // (c*q)
    e = gcd(c, H)
    D, T = U1//c, U2//c
    X, Y = q*H//e, c*D*T//e
    Be = X*X + Y*Y
    Fp = (W1*U2)**2 + (U1*V2)**2
    Fd = (U1*W2)**2 + (V1*U2)**2
    assert Fp == Fd == (c*e)**2 * Be
    return locals()


assert blob(SRC) == SRC_BLOB
assert blob(CD) == CD_BLOB
assert blob(BS) == BS_BLOB
state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art = json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "2d9380224f70f24530799f6d9fd6b5693351b0d4"
assert art["stacked_parent"]["goal4cd_run"] == 34425516973
assert art["stacked_parent"]["goal4cd_success"] is True
assert art["stacked_parent"]["aggregate_run"] == 34425516998
assert art["stacked_parent"]["aggregate_success"] is True
assert art["last_hostile_checkpoint"]["review"] == 5151846948
assert art["last_hostile_checkpoint"]["commits_to_parent"] == 49
assert art["source_locks"]["goal4ce_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4cd"]["blob_sha1"] == CD_BLOB
assert art["source_locks"]["goal4bs_source"]["blob_sha1"] == BS_BLOB

cc = art["common_leg_gcd_classification"]
assert cc["E1_orientation_p"]["gcd"] == "c*p"
assert cc["E1_orientation_d"]["gcd"] == "c*d"
assert cc["complete_common_leg_family"] == ["c", "p", "d"]
assert cc["q_is_E1_common_leg_channel"] is False
assert cc["c_nontrivial_local_content_exactly_e_family"] is True
assert cc["all_source_selected_E1_common_gcd_local_families_complete"] is True

# Classical joint survivor: common-leg gcd identities, c/e neutrality, and fresh support.
z = data((4, 3, 16, 5))
assert (z["c"], z["p"], z["d"], z["q"], z["H"], z["e"]) == (7, 5, 1, 8, 101, 1)
assert gcd(z["W1"]*z["U2"], z["U1"]*z["V2"]) == z["c"]*z["p"]
assert gcd(z["U1"]*z["W2"], z["V1"]*z["U2"]) == z["c"]*z["d"]
assert z["Be"] == 706225 == 5**2 * 13 * 41 * 53
assert z["H"] % 7 != 0
assert z["Be"] % 7 == (z["X"] % 7) ** 2 % 7
assert isqrt(z["Be"])**2 != z["Be"]
assert art["fresh_prime_boundary"]["fresh_odd_exponent_primes"] == [13, 41, 53]

# q-neutral witness: an odd q-prime loads one E1 summand only.
z = data((13, 4, 96, 91))
ell = 13
assert z["q"] % ell == 0
assert z["W1"] % ell != 0 and z["U2"] % ell != 0
assert z["V2"] % ell == 0
assert z["Fp"] % ell == ((z["W1"]*z["U2"]) % ell) ** 2 % ell
assert z["Fp"] % ell != 0

cd = json.loads(CD.read_text())
assert cd["result"]["canonical_source_gcd_local_family_complete"] is True
assert cd["result"]["universal_bad_prime_in_p_d_e"] is False

cy = art["cycle"]
assert cy["route_status"] == "BLOCKED_NO_NEW_INFORMATION"
assert cy["live_candidates"] == 0
assert cy["untested_candidates"] == 0
assert cy["exhaustive_view_audit"] is True
assert cy["blind_rediscovery"] is True
assert cy["parking_audit_complete"] is True
assert cy["return_to_goal4bs_parking_boundary"] is True
assert art["ledger"]["LIVE"] == []
assert art["ledger"]["UNTESTED_IMMEDIATELY_ACTIONABLE"] == []
assert all(v is False for v in art["credit_firewall"].values())

src = SRC.read_text()
for marker in (
    "(CE-Fp)", "(CE-Fd)", "(CE-gp)", "(CE-gd)", "(CE-common)",
    "(CE-q-neutral)", "(CE-Be)", "(CE-c=e)", "(CE-pd-complete)",
    "(CE-local-complete)", "(CE-Lpm)", "(CE-fresh)"
):
    assert marker in src, marker
for phrase in (
    "CYCLE_ROUTE_STATUS=BLOCKED_NO_NEW_INFORMATION",
    "CYCLE_PARKING_AUDIT_COMPLETE=true",
    "RETURN_TO_GOAL4BS_PARKING_BOUNDARY=true",
    "ALL_SOURCE_SELECTED_E1_COMMON_GCD_LOCAL_FAMILIES_COMPLETE=true"
):
    assert phrase in src, phrase

print("STAGE35_EX_GOAL4CE_POST_CANONICAL_GCD_LOCAL_COMPLETION_PARKING_AUDIT=PASS")
print("all_source_selected_E1_common_gcd_local_families_complete=true")
print("fresh_norm_prime_factoring=endpoint_equivalent_dynamic_support")
print("return_to_goal4bs_parking_boundary=true")
print("live_candidates=0")
print("canonical_sha256=" + EXPECTED)
