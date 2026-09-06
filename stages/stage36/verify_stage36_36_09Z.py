#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09Z" / "explicit-mw-rankjump-witness-preflight.json"
Y_CERT = ROOT / "stages" / "stage36" / "36-09Y" / "kummer-complement-prime-2adic-hilbert-preflight.json"
Y_VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09Y.py"
U_CERT = ROOT / "stages" / "stage36" / "36-09U" / "qi-antiinvariant-rankjump-descent-preflight.json"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "714bd143f0c20082edcbb81c3905a86b1a56b4bf"
Y_HEAD = "9816546d9f7148b8b3e347f2000308ee3597a582"
CERT_BLOB = "6a3b05e70fb146eff576df17142547b11679cf65"
Y_CERT_BLOB = "20c6d782e59bff820392731ec81653d15b2d1921"
Y_VERIFIER_BLOB = "63b4cc43e91c18a8ff295b288995e23395de8539"
U_CERT_BLOB = "a1f0c924d267ab4f45aaada6c9bcb3a5f544f284"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def vals(a: int, b: int) -> tuple[int, int, int]:
    S = a * a + b * b
    C = a**4 - 6 * a * a * b * b + b**4
    D = a * b * (a - b) * (a + b)
    return S, C, D


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(Y_CERT) == Y_CERT_BLOB
    assert blob(Y_VERIFIER) == Y_VERIFIER_BLOB
    assert blob(U_CERT) == U_CERT_BLOB
    assert git("merge-base", "--is-ancestor", BASE, "HEAD") == ""
    assert git("merge-base", "--is-ancestor", Y_HEAD, "HEAD") == ""
    assert git("rev-parse", f"{Y_HEAD}:stages/stage36/36-09Y/kummer-complement-prime-2adic-hilbert-preflight.json") == Y_CERT_BLOB
    assert git("rev-parse", f"{Y_HEAD}:stages/stage36/verify_stage36_36_09Y.py") == Y_VERIFIER_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09Z_EXPLICIT_MW_RANKJUMP_WITNESS_PREFLIGHT_V1"

    # Alpha witness: rational point on the homogeneous quartic and on E_minus.
    a, b, d, z, w = 14, 13, 337, 17, 1632
    S, C, D = vals(a, b)
    assert (S, C, D) == (365, -131767, 4914)
    assert C % d == 0
    assert w * w == d * z**4 - 2 * S * S * z * z + C * C // d
    x, y = d * z * z, d * z * w
    assert (x, y) == (97393, 9349728)
    assert y * y == x**3 - 2 * S * S * x * x + C * C * x
    assert d != 1

    # Beta witness: rational point on the dual homogeneous quartic and E_minus'.
    a, b, e, z, w = 5, 2, 5, 7, 861
    S, C, D = vals(a, b)
    assert (S, C, D) == (29, 41, 210)
    assert (64 * D * D) % e == 0
    assert w * w == e * z**4 + 4 * S * S * z * z + 64 * D * D // e
    X, Y = e * z * z, e * z * w
    assert (X, Y) == (245, 30135)
    assert Y * Y == X**3 + 4 * S * S * X * X + 64 * D * D * X
    # beta torsion baseline squareclasses at D=210 are [1],[-1],[105],[-105].
    assert e not in (1, -1, 105, -105)

    # Exact rank consequence from U's retained 2-isogeny index formula.
    u = json.loads(U_CERT.read_text())
    gb = u["generic_kummer_baseline"]
    assert gb["beta_baseline_size"] == 4
    assert gb["generic_exact_alpha_image"] == ["[1]"]
    assert gb["rank_formula"] == "2^r=|Im(alpha)|*|Im(beta)|/4"
    zc = c["qi_rankjump_consequence"]
    assert zc["Qi_rankjump_locus_nonempty"] is True
    assert zc["Qi_rankjump_locus_empty"] is False
    assert c["cassels_route_boundary"]["uniform_rankjump_locus_emptiness_via_Cassels_impossible"] is True
    assert c["next_leaf"] == "36-09AA_RECEIVER_COUPLED_RANKJUMP_LOCUS_INTERSECTION_PREFLIGHT"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V60_36_09Z_BATCHED"
    assert st["base_main_sha"] == BASE
    zz = st["authority_frontier"]["36-09Z"]
    assert zz["QI_RANKJUMP_LOCUS_NONEMPTY"] is True
    assert zz["GLOBAL_CASSELS_RANKJUMP_EMPTY_ROUTE_BLOCKED"] is True
    assert zz["RECEIVER_RANKJUMP_INTERSECTION_EMPTY"] is False
    assert st["current"]["unit"] == "36-09AA"
    assert st["current"]["36_09AA_entry_allowed"] is True
    assert st["promotion_gates"]["36_09Z_hostile_audit_passed"] is False
    assert st["claims"]["Qi_rankjump_locus_nonempty_provisional"] is True
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09Z explicit alpha/beta rational Kummer witnesses verified; Q(i) rankjump locus is nonempty; global Cassels-elimination route blocked; receiver-coupled intersection unlocked")


if __name__ == "__main__":
    main()
