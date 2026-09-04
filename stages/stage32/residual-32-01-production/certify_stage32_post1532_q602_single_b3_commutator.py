#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = "stages/stage32/residual-32-01-production/post1532-q602-single-b3-commutator.json"
EXPECTED_CANONICAL = "a374defb3a888c131ce92db9416702f34a03eb780b76d1dd6c26ab019f3c5064"
EXPECTED_RESIDUES = [73, 97, 235]


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_locked_json(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text())
    assert canonical_sha256(doc) == lock["canonical_sha256"], path
    return doc


def bits_to_vec(bits: int, n: int = 8) -> list[int]:
    return [(bits >> i) & 1 for i in range(n)]


def t_matrix_mod2(bits: int) -> list[list[int]]:
    x = bits_to_vec(bits)
    entries = [(x[0], x[1]), (x[2], x[3]), (x[4], x[5]), (x[6], x[7])]
    out = [[0] * 4 for _ in range(4)]
    # Retained module order: e1,e2,eps*e1,eps*e2, eps=r mod 2, eps^2=0.
    for j in range(4):
        q = [0, 0, 0, 0]
        q[j] = 1
        c, d = q[:2], q[2:]
        oc, od = [0, 0], [0, 0]
        for i in range(2):
            for k in range(2):
                aa, bb = entries[2 * i + k]
                oc[i] ^= aa & c[k]
                od[i] ^= (aa & d[k]) ^ (bb & c[k])
        col = [oc[0], oc[1], od[0], od[1]]
        for i in range(4):
            out[i][j] = col[i]
    return out


def parse_zr(expr: str) -> tuple[int, int]:
    table = {
        "-1": (-1, 0),
        "0": (0, 0),
        "1": (1, 0),
        "1+r": (1, 1),
    }
    if expr not in table:
        raise AssertionError(f"unexpected Z[r] expression: {expr}")
    return table[expr]


def zr_matrix_mod2(m: list[list[str]]) -> list[list[int]]:
    pairs = [[parse_zr(x) for x in row] for row in m]
    out = [[0] * 4 for _ in range(4)]
    for j in range(4):
        c, d = [0, 0], [0, 0]
        if j < 2:
            c[j] = 1
        else:
            d[j - 2] = 1
        oc, od = [0, 0], [0, 0]
        for i in range(2):
            for k in range(2):
                aa, bb = pairs[i][k]
                aa &= 1
                bb &= 1
                oc[i] ^= aa & c[k]
                od[i] ^= (aa & d[k]) ^ (bb & c[k])
        col = [oc[0], oc[1], od[0], od[1]]
        for i in range(4):
            out[i][j] = col[i]
    return out


def matmul_mod2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) & 1
             for j in range(len(b[0]))] for i in range(len(a))]


def commutator_mod2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    ab = matmul_mod2(a, b)
    ba = matmul_mod2(b, a)
    return [[ab[i][j] ^ ba[i][j] for j in range(len(ab[0]))] for i in range(len(ab))]


def is_zero(a: list[list[int]]) -> bool:
    return all(x == 0 for row in a for x in row)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    assert Path(args.check).as_posix() == CERT_PATH

    cert = json.loads((ROOT / CERT_PATH).read_text())
    assert cert["schema"] == "STAGE32_POST1532_Q602_SINGLE_B3_COMMUTATOR_REDUCTION_V1"
    assert cert["status"] == "EXACT_CONDITIONAL_SINGLE_B3_COMMUTATOR_EXCLUSION_PENDING_HOSTILE_AUDIT"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    locks = cert["source_locks"]
    trans = load_locked_json(locks["audited_transvection"])
    gauge = load_locked_json(locks["audited_marked_gauge"])
    note_path = ROOT / locks["source_note"]["path"]
    assert blob_sha1(note_path) == locks["source_note"]["blob_sha1"]
    note = note_path.read_text()

    # Bind the historical audit promotions through the live controller rather than
    # trusting the old provisional lifecycle strings inside the immutable assets.
    ctl = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert ctl["stage"] == 32 and ctl["stage32_closed"] is False
    ft = ctl["fixed_target"]
    assert (ft["row_id"], ft["O"], ft["qprime"], ft["Q"]) == ("g1-d186", 210, 4, 602)
    assert ctl["post1505_q602_weierstrass_transvection_hostile_reaudit_pass"]["review_id"] == 5102652713
    pred = ctl["audited_predecessor"]
    assert pred["hostile_reaudit_review_id"] == 5108049622
    assert pred["canonical_gauge_representative"] == 73
    assert pred["coordinate_orbit"] == EXPECTED_RESIDUES
    assert ctl["firewalls"]["O210_closed"] is False
    assert ctl["math_scope"]["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"

    # Exact audited residue set and retained basis.
    filt = trans["retained_residue_filter"]
    assert filt["surviving_residues_decimal"] == EXPECTED_RESIDUES
    assert trans["basis_independent_predicate"]["rank_T_minus_I"] == 1
    assert trans["audited_input"]["W_basis_vectors"] == [[0,0,1,0],[0,0,0,1]]
    assert gauge["audited_input"]["residues_decimal"] == EXPECTED_RESIDUES
    assert gauge["audited_input"]["retained_basis"] == cert["retained_basis"] == ["e1","e2","r*e1","r*e2"]
    assert gauge["residue_conjugation"]["orbit"] == EXPECTED_RESIDUES
    assert gauge["residue_conjugation"]["single_orbit"] is True

    # Source-locked principal Bolza matrices, same Z[r]^2 coordinates used by the gauge certificate.
    aut = gauge["principal_automorphisms"]
    assert aut["r_square"] == -2
    assert aut["b3"] == [["-1","-1"],["1","0"]]
    assert aut["b4"] == [["1","1+r"],["0","-1"]]
    assert aut["exact_unitary_checks"] == {"b3": True, "b4": True}
    ext = gauge["source_locks"]["external_bolza_g12"]
    assert ext["arxiv"] == "2509.24605v1"
    assert ext["locator"] == "Appendix B, equations (B.1)-(B.6)"

    b3 = zr_matrix_mod2(aut["b3"])
    b4 = zr_matrix_mod2(aut["b4"])
    assert b3 == cert["principal_automorphisms"]["b3_mod2_4x4"]
    assert b4 == cert["principal_automorphisms"]["b4_mod2_4x4"]

    got_mats = {str(q): t_matrix_mod2(q) for q in EXPECTED_RESIDUES}
    assert got_mats == cert["finite_mod2_check"]["residue_matrices"]

    b3_comms = {str(q): commutator_mod2(got_mats[str(q)], b3) for q in EXPECTED_RESIDUES}
    assert b3_comms == cert["finite_mod2_check"]["b3_commutators"]
    assert all(not is_zero(b3_comms[str(q)]) for q in EXPECTED_RESIDUES)
    assert cert["finite_mod2_check"]["b3_commuting_residues"] == []
    assert cert["finite_mod2_check"]["all_audited_q602_residues_fail_b3_commutation"] is True

    b4_hits = [q for q in EXPECTED_RESIDUES if is_zero(commutator_mod2(got_mats[str(q)], b4))]
    assert b4_hits == cert["finite_mod2_check"]["b4_commuting_residues"] == [73]

    # Exact integral commutation implies commutation after reduction mod 2. Since
    # every audited Q602 residue fails the latter for b3, one b3 commutator is enough.
    dec = cert["decision"]
    assert dec["conditional_implication"] == "[T,b3]=0 => Q(T)!=602"
    assert dec["single_commutator_sufficient_condition"] is True
    assert dec["b3_equivariance_proved_for_actual_correspondence"] is False
    assert dec["Q602_excluded_unconditionally"] is False
    assert dec["O210_excluded_unconditionally"] is False
    assert dec["O212_plus_authorized"] is False

    fw = cert["firewalls"]
    assert all(v is False for v in fw.values())
    assert "This leaf does not prove that the carrier or correspondence is `b3`-equivariant." in note
    assert "`[T,b3]=0  =>  Q(T) != 602`" in note
    assert "residue `73` commutes with `b4 mod 2`" in note

    print("PASS STAGE32_POST1532_Q602_SINGLE_B3_COMMUTATOR_REDUCTION_V1")
    print("canonical_sha256=" + EXPECTED_CANONICAL)
    print("q602_residues=[73,97,235] b3_commuting=[] b4_commuting=[73]")
    print("conditional: [T,b3]=0 => Q(T)!=602")
    print("actual b3-equivariance remains unproved; O210/Q602 OPEN; O212+ blocked; controller unchanged")


if __name__ == "__main__":
    main()
