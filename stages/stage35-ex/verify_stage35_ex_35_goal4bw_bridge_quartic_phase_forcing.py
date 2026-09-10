#!/usr/bin/env python3
"""Verify Goal4BW bridge-local quartic phase forcing boundary."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bw-bridge-quartic-phase-forcing.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bw-bridge-quartic-phase-forcing-source-lock.md")
BV = P("stages/stage35-ex/35ex-35/goal4bv-source-known-bridge-quartic-orientation.json")
EX03 = P("stages/stage35-ex/35ex-03/double-primitive-counterexample-normal-form.md")
EX08 = P("stages/stage35-ex/35ex-08/hypotenuse-bridge-triple.md")
EX10 = P("stages/stage35-ex/35ex-10/split-prime-obstruction.md")
EX11 = P("stages/stage35-ex/35ex-11/reciprocity-routing-and-local-route-freeze.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "c7a96543871cc6c22ad2785769f01fbfb7c4fd073e1cb7af4b747e0eb35c3285"
SRC_BLOB = "422d798b682c449d9440b0d52a46a35cc456f8f2"
BV_BLOB = "e93e6d11e9bcfb374552013b8219a0a19a2232d9"
EX03_BLOB = "af067616178b4b146265acc831ec5d0f2a380e23"
EX08_BLOB = "15c53ccd5317b6251a70a5f4bf78051a3bb4af1f"
EX10_BLOB = "a5761a883b3c50bbdad6a357241bba4b61e71c8a"
EX11_BLOB = "fc186e1a0b2134840135e67c29adb0e6bd9bf1a9"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def leg(a: int, ell: int) -> int:
    z = pow(a % ell, (ell - 1) // 2, ell)
    assert z in (1, ell - 1)
    return 1 if z == 1 else -1


def q4(a: int, ell: int) -> int:
    return pow(a % ell, (ell - 1) // 4, ell)


for path, expected in (
    (SRC, SRC_BLOB),
    (BV, BV_BLOB),
    (EX03, EX03_BLOB),
    (EX08, EX08_BLOB),
    (EX10, EX10_BLOB),
    (EX11, EX11_BLOB),
):
    assert blob(path) == expected, (path, blob(path), expected)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art = json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "90e281ee9aaba23a0bf4ed5a3f68f3fc19c8178a"
assert art["source_locks"]["goal4bw_source"]["blob_sha1"] == SRC_BLOB
assert art["result"]["e1_relative_bridge_root_orientation_source_fixed"] is True
assert art["result"]["both_branches_reduce_to_N_equals_omega_times_square"] is True
assert art["result"]["bridge_quartic_phase_reduces_to_one_legendre_bit"] is True
assert art["result"]["bridge_local_equations_force_fixed_quartic_phase"] is False
assert art["result"]["bridge_local_models_realize_both_real_phases"] is True
assert art["result"]["global_E1_system_permits_both_phases"] is False
assert art["result"]["global_bridge_quartic_product_relation_proved"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BX_BRIDGE_QUARTIC_GLOBAL_PRODUCT_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

# Exact bridge-local F_5 diagnostics. These are congruence models only.
ell = 5
iota = 2
omega = 1
q = 1
assert iota * iota % ell == ell - 1

phases_L = set()
for x in (1, 2):
    sigma = iota
    rho = omega * iota % ell
    p = omega * x * x % ell
    s, v = 1, x % ell
    r, u = rho, sigma * v % ell
    assert (r * r + s * s) % ell == 0
    assert (u * u + v * v) % ell == 0
    assert (p * r * s - q * u * v) % ell == 0
    assert p * pow(q, -1, ell) % ell == omega * x * x % ell
    N = p * q % ell
    z = q * x % ell
    assert N == omega * z * z % ell
    assert leg(N, ell) == 1
    phase = q4(N, ell)
    assert phase in (1, ell - 1)
    assert phase == q4(omega, ell) * (1 if leg(z, ell) == 1 else ell - 1) % ell
    phases_L.add(phase)
assert phases_L == {1, ell - 1}

phases_R = set()
for x in (1, 2):
    sigma = -iota % ell
    rho = omega * iota % ell
    p = omega * iota * x * x % ell
    s, v = 1, x % ell
    r, u = rho, sigma * v % ell
    assert (r * r + s * s) % ell == 0
    assert (u * u + v * v) % ell == 0
    assert (2 * p * r * s - q * (u * u - v * v)) % ell == 0
    assert p * pow(q, -1, ell) % ell == omega * iota * x * x % ell
    N = 2 * p * q % ell
    z = (1 + iota) * q * x % ell
    assert N == omega * z * z % ell
    assert leg(N, ell) == 1
    phase = q4(N, ell)
    assert phase in (1, ell - 1)
    assert phase == q4(omega, ell) * (1 if leg(z, ell) == 1 else ell - 1) % ell
    phases_R.add(phase)
assert phases_R == {1, ell - 1}

src = SRC.read_text()
for marker in (
    "(BW-omega)",
    "(BW-L-root)",
    "(BW-L-square)",
    "(BW-R-root)",
    "(BW-R-square)",
    "(BW-common)",
    "(BW-Q4)",
    "(BW-VERDICT)",
    "35EX-35_GOAL4BX_BRIDGE_QUARTIC_GLOBAL_PRODUCT_PREFLIGHT",
):
    assert marker in src, marker

print("STAGE35_EX_GOAL4BW_BRIDGE_QUARTIC_PHASE_FORCING=PASS")
print("relative_bridge_root_orientation_source_fixed=true")
print("bridge_quartic_phase_reduces_to_one_legendre_bit=true")
print("bridge_local_fixed_phase=false")
print("next=Goal4BX_bridge_quartic_global_product")
print("canonical_sha256=" + EXPECTED)
