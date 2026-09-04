#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECTED_CANONICAL = "83fd16fdaac674a3f63b4b2dac498136f1bc584c9e06d89f1aa1a7bdc4c30386"
EXPECTED_16 = [65,67,73,75,97,99,105,107,193,195,201,203,225,227,233,235]
EXPECTED_3 = [73,97,235]
EXPECTED_LINES = [(0,0,1,0),(0,0,0,1),(0,0,1,1)]


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


def load_locked_text(lock: dict) -> str:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    return path.read_text()


def bits_to_vec(bits: int, n: int = 8) -> list[int]:
    return [(bits >> i) & 1 for i in range(n)]


def t_matrix_mod2(bits: int) -> list[list[int]]:
    x = bits_to_vec(bits)
    entries = [(x[0], x[1]), (x[2], x[3]), (x[4], x[5]), (x[6], x[7])]
    out = [[0] * 4 for _ in range(4)]
    # Retained module order: e1,e2,eps*e1,eps*e2 with eps=r mod 2, eps^2=0.
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


def matmul_mod2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) & 1
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def rank_mod2(a: list[list[int]]) -> int:
    m = [row[:] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        for i in range(rows):
            if i != r and m[i][c]:
                m[i] = [x ^ y for x, y in zip(m[i], m[r])]
        r += 1
    return r


def minus_identity(t: list[list[int]]) -> list[list[int]]:
    out = [row[:] for row in t]
    for i in range(len(out)):
        out[i][i] ^= 1
    return out


def matvec_mod2(a: list[list[int]], v: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(a[i][j] * v[j] for j in range(len(v))) & 1 for i in range(len(a)))


def image_nonzero(a: list[list[int]]) -> list[tuple[int, ...]]:
    values = set()
    for bits in range(1 << len(a[0])):
        v = tuple((bits >> i) & 1 for i in range(len(a[0])))
        values.add(matvec_mod2(a, v))
    return sorted(v for v in values if any(v))


def canonical_even_subset(bits: int) -> int:
    assert bits.bit_count() % 2 == 0
    # Quotient even subsets of six branch points by complements.  Choose the
    # unique representative that does not contain branch point 6 (bit 5).
    if bits & (1 << 5):
        bits ^= 0b111111
    assert not (bits & (1 << 5))
    return bits


def j2_classes() -> list[int]:
    reps = {canonical_even_subset(bits) for bits in range(64) if bits.bit_count() % 2 == 0}
    assert len(reps) == 16
    return sorted(reps)


def apply_branch_permutation(bits: int, perm: dict[int, int]) -> int:
    out = 0
    for old in range(1, 7):
        if bits & (1 << (old - 1)):
            out |= 1 << (perm[old] - 1)
    return canonical_even_subset(out)


def weil_pairing(a: int, b: int) -> int:
    return (a & b).bit_count() & 1


def xor_class(a: int, b: int) -> int:
    return canonical_even_subset(a ^ b)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()

    cert = json.loads((ROOT / args.check).read_text())
    assert cert["schema"] == "STAGE32_POST1505_O210_Q602_WEIERSTRASS_PARITY_TRANSVECTION_REFINEMENT_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    # Historical audited-bundle replay must remain valid under successor
    # controllers.  Validate only the retained bundle identity and permanent
    # safety firewalls; do not pin the active controller leaf, verifier, or
    # checkpoint merge-release state.
    controller = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    bundle = controller["post1505_q602_weierstrass_parity_transvection_provisional"]
    assert bundle["certificate_path"] == args.check
    assert bundle["canonical_sha256"] == EXPECTED_CANONICAL
    assert bundle["q602_residue_pruning"] == "16 -> 3"
    assert bundle["surviving_residues_decimal"] == EXPECTED_3
    assert controller["operations"]["heavy_compute_authorized"] is False
    assert controller["firewalls"]["O210_closed"] is False
    assert controller["math_scope"]["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"

    locks = cert["source_locks"]
    adapter16 = load_locked_json(locks["audited_16_adapter"])
    frontier = load_locked_json(locks["correspondence_frontier"])
    common = load_locked_json(locks["common_double_cover"])
    label_adapter = load_locked_json(locks["boundary_label_weierstrass_adapter"])
    incidence = load_locked_json(locks["marked_exceptional_incidence"])
    collision = load_locked_json(locks["weierstrass_collision"])
    collision_note = load_locked_text(locks["weierstrass_collision_source_note"])
    principal = load_locked_json(locks["principal_rosati"])
    note = load_locked_text(locks["source_note"])

    # Preserve the exact hostile-audited 16-residue input.
    assert locks["audited_16_adapter"]["hostile_reaudit_review"] == 5100346603
    old_test = adapter16["q602_pointwise_exact_W_test"]
    assert old_test["surviving_residue_count"] == 16
    assert old_test["surviving_residues_decimal"] == EXPECTED_16
    assert cert["audited_input"]["residue_count"] == 16
    assert cert["audited_input"]["residues_decimal"] == EXPECTED_16
    w_basis = cert["audited_input"]["W_basis_vectors"]
    assert w_basis == [[0,0,1,0],[0,0,0,1]]

    # Correspondence orientation and common hyperelliptic double cover.
    corr = frontier["correspondence_endomorphism"]
    assert corr["definition"] == "T=(f1)_*(f2)^* in End(J(C0))"
    assert frontier["fixed_correspondence"]["maps"]["f1"]["degree"] == 105
    assert frontier["fixed_correspondence"]["maps"]["f2"]["degree"] == 81
    consequence = common["carrier_consequence"]
    assert consequence["first_factor"] == "Y is the normalization of N x_{z,X4} C0."
    assert consequence["second_factor"] == "Y is the normalization of N x_{w,X4} C0."
    assert consequence["same_quadratic_extension"] is True
    for needle in [
        "ramified at exactly the\n210 odd exceptional contacts",
        "The unique point of `Y` over an odd `m1`\ncontact maps under `(f1,f2)` to the corresponding pair of ramification points",
        "`n_p = M_p - 2*y_p`",
    ]:
        assert needle in collision_note, needle
    for needle in [
        "f1 o tau = iota o f1",
        "f2 o tau = iota o f2",
        "Q + iota(Q)",
        "n_p mod 2 = M_p mod 2",
    ]:
        assert needle in note, needle

    # Reconstruct the exact realized pairs and their mass parities.
    pair_counts = incidence["boundary_pair_counts"]
    assert len(pair_counts) == 12
    assert set(pair_counts.values()) == {4}
    label_map = {int(k): int(v) for k, v in label_adapter["boundary_label_to_weierstrass_id"].items()}
    expected_label_map = {33:6,34:6,35:1,36:1,37:5,38:3,39:5,40:3,41:4,42:4,43:2,44:2}
    assert label_map == expected_label_map

    capacities = collision["weierstrass_support"]["pair_mass_capacity"]
    assert len(capacities) == 12
    matrix = [[0] * 6 for _ in range(6)]
    reconstructed_pairs = []
    for row in capacities:
        a = int(row["first_factor_boundary_label"])
        b = int(row["second_factor_boundary_label"])
        key = f"{a}:{b}"
        assert pair_counts[key] == 4
        mass = int(row["exceptional_mass"])
        reconstructed_pairs.append({"pair":[a,b],"M":mass})
        i, j = label_map[a] - 1, label_map[b] - 1
        matrix[i][j] ^= mass & 1
    expected_matrix = [
        [1,0,0,0,0,0],
        [0,0,0,1,0,0],
        [0,0,1,0,0,0],
        [0,1,0,0,0,0],
        [0,0,0,0,1,0],
        [0,0,0,0,0,1],
    ]
    action = cert["weierstrass_parity_action"]
    assert reconstructed_pairs == action["ordered_pair_masses"]
    assert matrix == action["parity_matrix_rows_first_cols_second"] == expected_matrix
    # Every column contains exactly one 1; read the branch permutation from columns.
    perm = {}
    for col in range(6):
        rows = [row for row in range(6) if matrix[row][col]]
        assert len(rows) == 1
        perm[col + 1] = rows[0] + 1
    assert perm == {1:1,2:4,3:3,4:2,5:5,6:6}
    assert action["branch_permutation"] == "(2 4)"
    assert action["transvection_direction_abstract"] == "delta_0inf=[P_0-P_infinity]"
    assert action["transvection_direction_in_W"] is True

    # Recompute the hyperelliptic J[2] quotient and transvection formula from finite sets.
    classes = j2_classes()
    direction = canonical_even_subset((1 << (2-1)) | (1 << (4-1)))
    assert direction != 0
    image_differences = set()
    fixed = 0
    for q in classes:
        tq = apply_branch_permutation(q, perm)
        diff = xor_class(tq, q)
        image_differences.add(diff)
        if tq == q:
            fixed += 1
        # Exact transvection relation tau(Q)+Q=e(direction,Q)*direction.
        expected = direction if weil_pairing(direction, q) else 0
        assert diff == expected
    assert image_differences == {0, direction}
    assert fixed == 8  # kernel dimension 3 in a four-dimensional F2-space, hence rank one.
    # The intersection-parity Weil pairing is preserved on all 16 x 16 pairs.
    for a in classes:
        for b in classes:
            assert weil_pairing(apply_branch_permutation(a, perm), apply_branch_permutation(b, perm)) == weil_pairing(a, b)

    pred = cert["basis_independent_predicate"]
    assert pred == {
        "nonidentity": True,
        "rank_T_minus_I": 1,
        "preserves_weil_pairing": True,
        "image_T_minus_I_nonzero": True,
        "image_T_minus_I_subset_W": True,
        "individual_retained_W_line_identified": False,
    }

    # Recompute the retained-basis symplectic filter from the exact principal Riemann form.
    e_int = principal["principal_polarization"]["riemann_form_matrix"]
    e = [[int(x) & 1 for x in row] for row in e_int]
    assert principal["principal_polarization"]["riemann_form_basis"] == ["e1","e2","r*e1","r*e2"]
    survivors = []
    image_lines = []
    for bits in EXPECTED_16:
        t = t_matrix_mod2(bits)
        a = minus_identity(t)
        symplectic = matmul_mod2(matmul_mod2(transpose(t), e), t) == e
        rank = rank_mod2(a)
        nonzero_image = image_nonzero(a)
        image_in_w = bool(nonzero_image) and all(v[0] == 0 and v[1] == 0 for v in nonzero_image)
        if symplectic and rank == 1 and image_in_w:
            assert len(nonzero_image) == 1
            survivors.append(bits)
            image_lines.append(nonzero_image[0])
    assert survivors == EXPECTED_3
    assert image_lines == EXPECTED_LINES
    filt = cert["retained_residue_filter"]
    assert filt["input_residue_count"] == 16
    assert filt["surviving_residue_count"] == 3
    assert filt["surviving_residues_decimal"] == EXPECTED_3
    assert filt["surviving_residues_hex"] == ["0x49","0x61","0xeb"]
    assert [tuple(v) for v in filt["image_lines_in_W"]] == EXPECTED_LINES
    assert filt["removed_residue_count"] == 13
    assert filt["Q602_excluded"] is False

    decision = cert["decision"]
    assert decision["result"] == "WEIERSTRASS_ODD_CONTACT_PARITY_FORCES_TRANSVECTION_AND_PRUNES_16_TO_3"
    assert decision["mathematical_credit"] == "PROVISIONAL_PENDING_HOSTILE_AUDIT"
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert decision["O212_plus_authorized"] is False
    assert decision["promotion_requires_hostile_audit"] is True

    fire = cert["firewalls"]
    assert fire["g12_equivariance_assumed"] is False
    assert fire["arbitrary_W_line_identification_used"] is False
    assert fire["integral_endomorphism_is_geometric_correspondence"] is False
    assert fire["three_to_one_pruning_authorized"] is False
    assert fire["heavy_compute_authorized"] is False
    assert fire["full178_authorized"] is False

    print(json.dumps({
        "schema": cert["schema"],
        "canonical": EXPECTED_CANONICAL,
        "controller": controller["schema"],
        "branch_permutation": "(2 4)",
        "j2_transvection_rank": 1,
        "Q602_residues": {"input":16,"output":3,"values":EXPECTED_3},
        "image_lines_in_W": [list(v) for v in EXPECTED_LINES],
        "Q602_excluded": False,
        "O210_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
