#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "stages/stage33/33-07"
sys.path.insert(0, str(HELPER))
from stage32_picard_marking_retained import load as load_marking  # type: ignore

CERT_PATH = "stages/stage32/residual-32-01-production/post1536-b3-cusp-orbit-ambient-equivariance-negative.json"
EXPECTED_CANONICAL = "3637db0c1e2acda7132b5b4fdc8ba4ee731230c160fa599dbdfeae993fb9e8ba"
EXPECTED_SECOND_TO_WEIERSTRASS = {33: 6, 36: 1, 37: 5, 40: 3, 41: 4, 44: 2}
SECOND_BOUNDARIES = list(EXPECTED_SECOND_TO_WEIERSTRASS)
EXPECTED_PROFILE = [11, 22, 16, 11, 28, 22]


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
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
    return doc


def compose(p: list[int], q: list[int]) -> list[int]:
    return [q[p[j] - 1] for j in range(len(p))]


def inverse(p: list[int]) -> list[int]:
    out = [0] * len(p)
    for j, value in enumerate(p, start=1):
        out[value - 1] = j
    return out


def transform(pairings: list[int], perm: list[int]) -> list[int]:
    pinv = inverse(perm)
    return [pairings[pinv[j] - 1] for j in range(len(pairings))]


def perm_for_word(word: str, perms: list[list[int]]) -> list[int]:
    out = list(range(1, 141))
    if word == "1":
        return out
    for token in word.split("*"):
        assert token.startswith("g") and token[1:].isdigit(), token
        idx = int(token[1:])
        assert 1 <= idx <= len(perms), token
        out = compose(out, perms[idx - 1])
    return out


def matmul2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matrix_order(a: list[list[int]], bound: int = 24) -> int:
    cur = [[1, 0], [0, 1]]
    for n in range(1, bound + 1):
        cur = matmul2(cur, a)
        if cur == [[1, 0], [0, 1]]:
            return n
    raise AssertionError("order exceeds bound")


def cycle_lengths(p: tuple[int, ...]) -> list[int]:
    seen: set[int] = set()
    out: list[int] = []
    for i in range(len(p)):
        if i in seen:
            continue
        j = i
        n = 0
        while j not in seen:
            seen.add(j)
            n += 1
            j = p[j]
        out.append(n)
    return sorted(out)


def preserves(values: list[int], p: tuple[int, ...]) -> bool:
    return all(values[i] == values[p[i]] for i in range(len(values)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    assert Path(args.check).as_posix() == CERT_PATH

    cert = json.loads((ROOT / CERT_PATH).read_text())
    assert cert["schema"] == "STAGE32_POST1536_B3_CUSP_ORBIT_AMBIENT_EQUIVARIANCE_NEGATIVE_V1"
    assert cert["status"] == "EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert cert["arsenal_routing"]["primary"] == "S30-W01"
    assert cert["arsenal_routing"]["auxiliary_not_used_for_semantic_credit"] == "S32-PW05"

    ctl = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert ctl["stage"] == 32 and ctl["stage32_closed"] is False
    ft = ctl["fixed_target"]
    assert (ft["row_id"], ft["O"], ft["qprime"], ft["Q"]) == ("g1-d186", 210, 4, 602)
    assert ctl["firewalls"]["O210_closed"] is False
    assert ctl["math_scope"]["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"

    locks = cert["source_locks"]
    witness = load_locked_json(locks["recovered_v6_witness"])
    hdeck = load_locked_json(locks["h_deck"])
    gauge = load_locked_json(locks["marked_gauge"])
    predecessor = load_locked_json(locks["single_b3_predecessor"])
    transvection = load_locked_json(locks["audited_weierstrass_transvection"])
    assert locks["audited_weierstrass_transvection"]["hostile_reaudit_review"] == 5102652713
    assert locks["audited_weierstrass_transvection"]["audited_exact_head"] == "efb26374a5d46dd6118428306ae6dcee417a1041"

    boundary_map = {
        int(label): int(wid)
        for label, wid in transvection["weierstrass_parity_action"]["boundary_label_to_weierstrass_id"].items()
    }
    second_to_weierstrass = {label: boundary_map[label] for label in SECOND_BOUNDARIES}
    assert second_to_weierstrass == EXPECTED_SECOND_TO_WEIERSTRASS
    assert set(second_to_weierstrass.values()) == set(range(1, 7))
    assert len(set(second_to_weierstrass.values())) == 6
    semantic = cert["semantic_anchor"]
    assert {int(k): int(v) for k, v in semantic["second_boundary_to_weierstrass_id"].items()} == EXPECTED_SECOND_TO_WEIERSTRASS
    assert semantic["weierstrass_id_set"] == [1, 2, 3, 4, 5, 6]
    assert semantic["bijection_verified"] is True

    diag_path = ROOT / locks["diagnostic"]["path"]
    assert blob_sha1(diag_path) == locks["diagnostic"]["blob_sha1"]
    marking_path = ROOT / locks["retained_picard_stoll_action"]["path"]
    assert blob_sha1(marking_path) == locks["retained_picard_stoll_action"]["blob_sha1"]
    note_path = ROOT / locks["source_note"]["path"]
    assert blob_sha1(note_path) == locks["source_note"]["blob_sha1"]
    note = note_path.read_text()

    assert predecessor["decision"]["conditional_implication"] == "[T,b3]=0 => Q(T)!=602"
    assert predecessor["decision"]["b3_equivariance_proved_for_actual_correspondence"] is False

    ext = gauge["source_locks"]["external_bolza_g12"]
    assert ext["arxiv"] == cert["bolza_order3_input"]["external_source"]["arxiv"] == "2509.24605v1"
    assert ext["locator"] == cert["bolza_order3_input"]["external_source"]["locator"] == "Appendix B, equations (B.1)-(B.6)"
    b3 = [[int(x) for x in row] for row in gauge["principal_automorphisms"]["b3"]]
    assert b3 == cert["bolza_order3_input"]["b3"] == [[-1, -1], [1, 0]]
    assert matrix_order(b3) == cert["bolza_order3_input"]["exact_order"] == 3
    assert cert["bolza_order3_input"]["required_branch_permutation_cycle_type"] == [3, 3]

    pairings = [int(x) for x in witness["witness"]["all140_pairings"]]
    assert len(pairings) == 140
    assert [pairings[i - 1] for i in SECOND_BOUNDARIES] == EXPECTED_PROFILE

    marking = load_marking()
    aut = marking["aut_action"]
    assert aut["schema"] == locks["retained_picard_stoll_action"]["schema"] == "STAGE32_AUT_PERM_SOURCELOCK_V1"
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    assert len(perms) == 9 and all(len(p) == 140 for p in perms)

    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    assert hwords == {"u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"}
    expected_h = {"id": "1", "u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"}
    assert cert["finite_result"]["h_deck_words"] == expected_h

    cycle33 = [p for p in itertools.permutations(range(6)) if cycle_lengths(p) == [3, 3]]
    assert len(cycle33) == cert["finite_result"]["two_3cycle_permutation_count"] == 40

    rows = []
    for name, word in expected_h.items():
        moved = transform(pairings, perm_for_word(word, perms))
        values = [moved[i - 1] for i in SECOND_BOUNDARIES]
        hits = sum(preserves(values, p) for p in cycle33)
        rows.append({
            "H_member": name,
            "word": word,
            "second_boundary_values": values,
            "preserving_two_3cycle_permutation_count": hits,
        })
    assert rows == cert["finite_result"]["h_orbit_rows"]
    assert all(row["second_boundary_values"] == EXPECTED_PROFILE for row in rows)
    assert all(row["preserving_two_3cycle_permutation_count"] == 0 for row in rows)
    assert cert["finite_result"]["all_h_translates_reject_two_3cycle_invariance"] is True
    assert cert["finite_result"]["second_factor_boundary_labels"] == SECOND_BOUNDARIES

    dec = cert["decision"]
    assert dec["result"] == "EXACT_BOUNDED_NEGATIVE"
    assert dec["closed_subroute"] == "DIRECT_AMBIENT_B3_CUSP_PROFILE_EQUIVARIANCE_FOR_V6_H_ORBIT"
    assert dec["closed_subroute_only"] is True
    assert dec["actual_T_commutation_proved"] is False
    assert dec["actual_T_noncommutation_proved"] is False
    assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
    assert dec["O212_plus_advance_allowed"] is False
    assert dec["controller_change_authorized"] is False
    assert all(v is False for v in cert["firewalls"].values())

    assert "does **not** prove or refute the actual Jacobian commutator `[T,b3]`" in note
    assert "33 -> 6" in note and "44 -> 2" in note
    assert "map bijectively onto the six Weierstrass ids `{1,2,3,4,5,6}`" in note
    assert "There are exactly 40 permutations of six labels with cycle type `(3,3)`" in note
    assert "DIRECT_AMBIENT_B3_CUSP_PROFILE_EQUIVARIANCE_FOR_V6_H_ORBIT" in note
    assert "`O210/Q602` remain OPEN and `O212+` remains blocked" in note

    print("PASS STAGE32_POST1536_B3_CUSP_ORBIT_AMBIENT_EQUIVARIANCE_NEGATIVE_V1")
    print("canonical_sha256=" + EXPECTED_CANONICAL)
    print("audited cusp adapter: 33->6 36->1 37->5 40->3 41->4 44->2; bijection={1,...,6}")
    print("b3_order=3 cycle_type=(3,3) permutations=40")
    print("H={id,u,v,uv}; profile=[11,22,16,11,28,22]; preserving_counts=[0,0,0,0]")
    print("closed only: DIRECT_AMBIENT_B3_CUSP_PROFILE_EQUIVARIANCE_FOR_V6_H_ORBIT")
    print("actual [T,b3] unresolved; Q602/O210 OPEN; O212+ blocked; controller unchanged")


if __name__ == "__main__":
    main()
