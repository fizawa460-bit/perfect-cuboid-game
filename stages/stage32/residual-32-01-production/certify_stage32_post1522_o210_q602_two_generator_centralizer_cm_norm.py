#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = "stages/stage32/residual-32-01-production/post1522-o210-q602-two-generator-centralizer-cm-norm.json"
EXPECTED_CANONICAL = "b45e8ea119ec5f6fe19c95e47316b102a95da896f90e843a199db720624d23de"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_lock(lock: dict):
    p = ROOT / lock["path"]
    assert p.is_file(), p
    assert blob_sha1(p) == lock["blob_sha1"], p
    if p.suffix == ".json":
        doc = json.loads(p.read_text())
        if "canonical_sha256" in lock:
            assert canonical_sha256(doc) == lock["canonical_sha256"], p
        return doc
    return p.read_text()


def rank_q(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    r = 0
    cols = len(a[0])
    for c in range(cols):
        pivot = next((j for j in range(r, len(a)) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][c]
        a[r] = [x / v for x in a[r]]
        for j in range(len(a)):
            if j != r and a[j][c]:
                v = a[j][c]
                a[j] = [x - v*y for x, y in zip(a[j], a[r])]
        r += 1
    return r


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    assert Path(args.check).as_posix() == CERT_PATH

    cert = json.loads((ROOT / CERT_PATH).read_text())
    assert cert["schema"] == "STAGE32_POST1522_O210_Q602_TWO_GENERATOR_CENTRALIZER_CM_NORM_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    locks = cert["source_locks"]
    prev = load_lock(locks["post1521_valence_route"])
    bolza_note = load_lock(locks["post1490_bolza_endomorphism_source_note"])
    repair_note = load_lock(locks["post1500_q602_repair_source_note"])
    route_note = load_lock(locks["source_note"])

    assert prev["decision"]["valence_proved_for_actual_Gamma"] is False
    assert prev["decision"]["Q602_excluded_unconditionally"] is False
    assert prev["arsenal_precheck"]["direct_applicable_card_found"] is False
    assert "C0" in bolza_note and "s^2 = x(x^4-1) = x^5-x" in bolza_note
    assert "End(J(C0)) ~= M_2(Z[sqrt(-2)])" in bolza_note
    assert "Tr_Q(T^dagger*T)=2*Q(T)" in repair_note
    assert "`Q(T)=602`" in repair_note

    fixed = cert["fixed_input"]
    assert fixed["O"] == 210 and fixed["Q"] == 602
    assert fixed["curve"] == "C0: y^2=x^5-x"
    assert fixed["endomorphism_ring"] == "End(J(C0)) ~= M_2(Z[sqrt(-2)])"
    assert fixed["retained_operator"] == "T=(f1)_*(f2)^*"
    assert fixed["rosati_trace_normalization"] == "Tr_Q(T^dagger*T)=2*Q(T)"

    f = {5: 1, 1: -1}
    alpha_f = {k: c*((-1)**k) for k, c in f.items()}
    assert alpha_f == {5: -1, 1: 1}
    beta_times_x6 = {1: 1, 5: -1}
    assert beta_times_x6 == {k: -c for k, c in f.items()}

    aut = cert["automorphisms"]
    assert aut["alpha"] == "(x,y)->(-x,i*y)"
    assert aut["beta"] == "(x,y)->(1/x,i*y/x^3)"
    assert aut["differential_basis"] == ["dx/y", "x*dx/y"]
    assert aut["alpha_matrix"] == [["i","0"],["0","-i"]]
    assert aut["beta_matrix"] == [["0","i"],["i","0"]]

    rows = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 1,-1, 0],
        [1, 0, 0,-1],
    ]
    assert rank_q(rows) == 3
    assert aut["joint_centralizer"] == "C*I"

    cm = cert["conditional_cm_scalar_math"]
    assert cm["hypothesis"] == "T commutes with alpha_* and beta_*"
    assert cm["analytic_conclusion"] == "T=lambda*I"
    assert cm["integral_cm_conclusion"] == "lambda=a+b*sqrt(-2), a,b in Z"
    assert cm["Q_formula"] == "Q(T)=2*(a^2+2*b^2)"
    assert cm["Q602_norm_equation"] == "a^2+2*b^2=301"

    residues = sorted({(a*a + 2*b*b) % 8 for a in range(8) for b in range(8)})
    assert residues == [0,1,2,3,4,6] == cm["norm_residues_mod8"]
    assert 301 % 8 == 5 == cm["target_residue_mod8"]
    assert cm["integer_solution_exists"] is False
    assert 301 % 8 not in residues
    assert cm["conditional_exclusion"] is True

    assert "No product-polarization assumption is needed." in route_note
    assert "conjugate(lambda)*I" in route_note
    assert "`Q(T)=2*(a^2+2*b^2)`" in route_note
    assert "`[T,alpha_*]=[T,beta_*]=0  =>  Q(T) != 602`" in route_note

    d = cert["decision"]
    assert d["two_generator_commutation_proved_for_actual_T"] is False
    assert d["actual_Gamma_valence_proved"] is False
    assert d["Q602_excluded_unconditionally"] is False
    assert d["O210_excluded_unconditionally"] is False
    assert d["conditional_Q602_exclusion_if_two_generator_commutation"] is True
    assert d["O212_plus_authorized"] is False
    assert "[T,alpha_*]=[T,beta_*]=0" in d["next_required_fact"]

    ctl = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert ctl["schema"] == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V247_POST1520_Q602_RETAINED_GEOMETRY_18_TO_18_AUDITED"
    assert ctl["stage"] == 32 and ctl["stage32_closed"] is False
    assert ctl["advance_allowed"] is True
    assert ctl["firewalls"]["O210_closed"] is False
    assert ctl["firewalls"]["Q602_excluded"] is False
    assert ctl["math_scope"]["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"

    fw = cert["firewalls"]
    assert all(fw[k] is False for k in [
        "conditional_implies_unconditional", "rosati_self_adjoint_assumed",
        "product_polarization_assumed", "scalar_complex_implies_integer_scalar",
        "q2_mod3_7adic_reopened", "geometric_realization_credit",
        "receiver_credit", "route_credit", "theorem_credit",
        "endpoint_credit", "perfect_cuboid_claim"
    ])

    print("PASS: two explicit Bolza automorphisms have scalar joint centralizer; if the actual T commutes with both, integrality puts the scalar in Z[sqrt(-2)] and Q602 would force norm 301, impossible mod 8. Actual commutation remains unproved; O210 stays open.")


if __name__ == "__main__":
    main()
