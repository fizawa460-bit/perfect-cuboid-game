#!/usr/bin/env python3
"""Verify Goal4BX bridge quartic global-product congruence boundary."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bx-bridge-quartic-global-product.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bx-bridge-quartic-global-product-source-lock.md")
BW = P("stages/stage35-ex/35ex-35/goal4bw-bridge-quartic-phase-forcing.json")
EX08 = P("stages/stage35-ex/35ex-08/hypotenuse-bridge-triple.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "4cd2a6b59334e9f68c8cc46fa1a9c2555680de44708639f7ef645488b55d3fce"
SRC_BLOB = "f9c340f9014dfd390f1e6604951843b47965e501"
BW_BLOB = "fa374e351bdd42f1462be2b9e68a973b85aad123"
EX08_BLOB = "15c53ccd5317b6251a70a5f4bf78051a3bb4af1f"
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
    z = pow(a % ell, (ell - 1) // 4, ell)
    assert z in (1, ell - 1)
    return 1 if z == 1 else -1


for path, expected in ((SRC, SRC_BLOB), (BW, BW_BLOB), (EX08, EX08_BLOB)):
    assert blob(path) == expected, (path, blob(path), expected)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art = json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "34adeb61fcb4ec07f674be9e6a00639866969683"
assert art["stacked_parent"]["dedicated_run"] == 34420170653
assert art["source_locks"]["goal4bx_source"]["blob_sha1"] == SRC_BLOB
assert art["result"]["bridge_residual_phases_have_one_global_rational_carrier"] is True
assert art["result"]["oriented_bridge_kernel_sigma_e_defined"] is True
assert art["result"]["bridge_phase_product_compresses_to_one_jacobi_bit"] is True
assert art["result"]["two_prime_crt_models_realize_all_phase_patterns"] is True
assert art["result"]["bridge_congruence_layer_forces_global_product"] is False
assert art["result"]["full_integral_E1_global_jacobi_bit_free"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BY_BRIDGE_QUARTIC_INTEGER_GLOBAL_ADAPTER_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

E = 65
primes = ((5, 2), (13, 5))
iota = 57
omega = 1
q = 1
assert iota * iota % E == E - 1
assert all(iota % ell == ii for ell, ii in primes)

expected_all = {(1, 1), (1, -1), (-1, 1), (-1, -1)}

patterns_L = set()
for x in (1, 41, 27, 2):
    s = 1
    r = iota
    v = x
    u = iota * x % E
    p = x * x % E
    assert (r * r + s * s) % E == 0
    assert (u * u + v * v) % E == 0
    assert (p * r * s - q * u * v) % E == 0
    phases = tuple(q4((p * q) % ell, ell) for ell, _ in primes)
    for ell, _ in primes:
        assert q4((p * q) % ell, ell) == leg(x, ell)
    patterns_L.add(phases)
assert patterns_L == expected_all
assert {a * b for a, b in patterns_L} == {-1, 1}

patterns_R = set()
for x in (1, 41, 27, 2):
    s = 1
    r = iota
    v = x
    u = (-iota * x) % E
    p = iota * x * x % E
    assert (r * r + s * s) % E == 0
    assert (u * u + v * v) % E == 0
    assert (2 * p * r * s - q * (u * u - v * v)) % E == 0
    phases = tuple(q4((2 * p * q) % ell, ell) for ell, _ in primes)
    patterns_R.add(phases)
assert patterns_R == expected_all
assert {a * b for a, b in patterns_R} == {-1, 1}

src = SRC.read_text()
for marker in (
    "(BX-root)",
    "(BX-ZL)",
    "(BX-ZR)",
    "(BX-Sigma)",
    "(BX-product)",
    "(BX-CRT-L)",
    "(BX-CRT-R)",
    "(BX-VERDICT)",
    "35EX-35_GOAL4BY_BRIDGE_QUARTIC_INTEGER_GLOBAL_ADAPTER_PREFLIGHT",
):
    assert marker in src, marker

print("STAGE35_EX_GOAL4BX_BRIDGE_QUARTIC_GLOBAL_PRODUCT=PASS")
print("global_rational_phase_carrier=true")
print("phase_product_compresses_to_one_jacobi_bit=true")
print("bridge_congruence_global_product_forced=false")
print("next=Goal4BY_bridge_quartic_integer_global_adapter")
print("canonical_sha256=" + EXPECTED)
