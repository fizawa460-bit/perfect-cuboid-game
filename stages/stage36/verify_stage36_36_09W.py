#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09W" / "variable-prime-six-reservoir-reciprocity-preflight.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09W" / "hilbert-reciprocity-source-lock.md"
V_CERT = ROOT / "stages" / "stage36" / "36-09V" / "gaussian-directional-prime-support-preflight.json"
V_VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09V.py"
U_CERT = ROOT / "stages" / "stage36" / "36-09U" / "qi-antiinvariant-rankjump-descent-preflight.json"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "f8522bd1a38fa551186ad370f51d17c73c7927e2"
V_HEAD = "117cdb991a29706b7b9e79485c5b9f19a6f09552"
CERT_BLOB = "ddeed22ffdad51e6ba409396f82026680c46e8ab"
SOURCE_BLOB = "52952e2afd1db636a236c6bd254acadc779fe09f"
V_CERT_BLOB = "9fdec16f920104cc6c1961fb092185a0371258d5"
V_VERIFIER_BLOB = "d7b497c1ae7e8a1d484084c6aa20d38b5bc09078"
U_CERT_BLOB = "a1f0c924d267ab4f45aaada6c9bcb3a5f544f284"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def vals(a: int, b: int) -> dict[str, int]:
    return {
        "B0": a,
        "BINF": b,
        "BPLUS": a - b,
        "BMINUS": a + b,
        "AMINUS": a * a - 2 * a * b - b * b,
        "APLUS": a * a + 2 * a * b - b * b,
    }


def C0(a: int, b: int) -> int:
    return a**4 - 6 * a * a * b * b + b**4


def D0(a: int, b: int) -> int:
    return a * b * (a - b) * (a + b)


def legendre(x: int, q: int) -> int:
    r = pow(x % q, (q - 1) // 2, q)
    if r == 1:
        return 1
    if r == q - 1:
        return -1
    return 0


def retained(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1 and b != 0 and a != 0 and a != b and a != -b


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(V_CERT) == V_CERT_BLOB
    assert blob(V_VERIFIER) == V_VERIFIER_BLOB
    assert blob(U_CERT) == U_CERT_BLOB
    assert git("merge-base", "--is-ancestor", BASE, "HEAD") == ""
    assert git("rev-parse", f"{V_HEAD}:stages/stage36/36-09V/gaussian-directional-prime-support-preflight.json") == V_CERT_BLOB
    assert git("rev-parse", f"{V_HEAD}:stages/stage36/verify_stage36_36_09V.py") == V_VERIFIER_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09W_VARIABLE_PRIME_SIX_RESERVOIR_RECIPROCITY_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["batch_parent"]["36_09V_exact_head"] == V_HEAD
    assert c["source_locks"]["hilbert_reciprocity"]["blob_sha"] == SOURCE_BLOB

    # Exact polynomial identities behind the six odd-place rows.
    # B0/BINF/BPLUS/BMINUS are direct substitutions.
    for b in range(-4, 5):
        if b:
            assert C0(0, b) == b**4
            assert C0(b, b) == -4 * b**4
            assert C0(-b, b) == -4 * b**4
    for a in range(-4, 5):
        if a:
            assert C0(a, 0) == a**4

    # Alpha rows: exact divisibility identities.
    for a in range(-6, 7):
        for b in range(-6, 7):
            am = a*a - 2*a*b - b*b
            ap = a*a + 2*a*b - b*b
            assert D0(a,b) - 2*a*a*b*b == a*b*am
            assert D0(a,b) + 2*a*a*b*b == a*b*ap
            assert (a*a+b*b)**2 - 8*a*a*b*b == am*ap

    # Every declared witness is primitive/retained, lies in exactly the named
    # q-reservoir, and flips the stated local unit Legendre character while
    # preserving that reservoir direction.
    ws = c["direction_internal_symbol_freedom"]["witnesses"]
    assert len(ws) == 6
    for w in ws:
        rid, q, unit = w["reservoir"], w["q"], w["unit"]
        got = []
        for pair in (w["plus_pair"], w["minus_pair"]):
            a, b = pair
            assert retained(a,b)
            rv = vals(a,b)
            assert rv[rid] % q == 0
            assert sum(1 for x in rv.values() if x % q == 0) == 1
            u = a if unit == "a" else b
            got.append(legendre(u,q))
        assert got == [1,-1]
        assert got == w["legendre_values"]

    # Fixed cross-sector congruences at odd reservoir primes, checked exhaustively
    # over residue pairs for a representative collection of odd primes. This is
    # a replay of the exact identities above, not a replacement for them.
    for q in [3,5,7,11,13,17,19,23,29,31]:
        for a in range(q):
            for b in range(q):
                if a == 0 and b == 0:
                    continue
                rv = vals(a,b)
                hits = [k for k,v in rv.items() if v % q == 0]
                if len(hits) != 1:
                    continue
                rid = hits[0]
                if rid == "B0":
                    assert (C0(a,b)-b**4) % q == 0
                elif rid == "BINF":
                    assert (C0(a,b)-a**4) % q == 0
                elif rid in ("BPLUS","BMINUS"):
                    assert (C0(a,b)+4*b**4) % q == 0
                elif rid == "AMINUS":
                    assert (D0(a,b)-2*(a*b)**2) % q == 0
                    assert legendre(2,q) == 1
                elif rid == "APLUS":
                    assert (D0(a,b)+2*(a*b)**2) % q == 0
                    assert legendre(2,q) == 1

    f = c["parameter_only_checksum_firewall"]
    assert f["holds_for_every_retained_parameter_pair"] is True
    assert f["depends_on_receiver_point"] is False
    assert f["depends_on_alpha_kummer_class_d"] is False
    assert f["depends_on_beta_kummer_class_e"] is False
    assert f["therefore_receiver_obstruction"] is False

    b11 = c["B11_preflight_result"]
    assert b11["coarse_parameter_only_multiplace_reciprocity"] == "BLOCKED_AS_TAUTOLOGICAL_CHECKSUM"
    assert b11["direction_only_fixed_sign_reciprocity"] == "BLOCKED_BY_EXACT_INTERNAL_LEGENDRE_FREEDOM"
    assert b11["multiplace_reciprocity_obstruction_proved"] is False
    assert c["next_leaf"] == "36-09X_KUMMER_CLASS_COUPLED_HILBERT_LOCAL_SOLVABILITY_PREFLIGHT"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V57_36_09W_BATCHED"
    assert st["base_main_sha"] == BASE
    w = st["authority_frontier"]["36-09W"]
    assert w["certificate_blob_sha"] == CERT_BLOB
    assert w["PARAMETER_ONLY_RECIPROCITY_BLOCKED"] is True
    assert w["DIRECTION_ONLY_RECIPROCITY_BLOCKED"] is True
    assert w["KUMMER_COUPLED_B11_REMAINS_LIVE"] is True
    assert w["MULTIPLACE_RECIPROCITY_OBSTRUCTION_PROVED"] is False
    assert w["CANDIDATE_SET_SHRUNK"] is False
    assert st["current"]["unit"] == "36-09X"
    assert st["current"]["36_09X_entry_allowed"] is True
    assert st["promotion_gates"]["36_09W_hostile_audit_passed"] is False
    assert st["promotion_gates"]["multiplace_reciprocity_obstruction_proved"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09W parameter-only Hilbert checksum and direction-sign freedom verified; coarse B11 blocked, Kummer-coupled B11 remains live; 36-09X unlocked")


if __name__ == "__main__":
    main()
