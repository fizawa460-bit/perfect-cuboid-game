#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT = ROOT / "stages/stage32/scratch/ex1-h4-uniform-transvection-28-to-3-candidate-20260908.json"

EXPECTED_28 = [20,60,65,67,69,73,75,77,81,97,99,105,107,113,150,190,193,195,199,201,203,207,211,225,227,233,235,243]
EXPECTED_3 = [73,97,235]
EXPECTED_MATRIX = [
    [1,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,1,0,0,0],
    [0,1,0,0,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,1],
]
EXPECTED_CLASSIFICATION = {
    "non_symplectic":[67,75,99,107,193,201,225,233],
    "symplectic_rank0_identity":[65],
    "symplectic_rank1_image_in_W":[73,97,235],
    "symplectic_rank2_image_in_W":[105,195,203,227],
    "symplectic_rank2_image_not_in_W":[20,60,69,77,81,113,150,190,199,207,211,243],
}

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
    if "blob_sha1" in lock:
        assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text(encoding="utf-8"))
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
        assert doc.get("canonical_sha256_without_this_field") == lock["canonical_sha256"], path
    return doc

def load_locked_text(lock: dict) -> str:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    return path.read_text(encoding="utf-8")

def bits_to_vec(bits: int) -> list[int]:
    return [(bits >> i) & 1 for i in range(8)]

def t_matrix_mod2(bits: int) -> list[list[int]]:
    x = bits_to_vec(bits)
    entries = [(x[0],x[1]),(x[2],x[3]),(x[4],x[5]),(x[6],x[7])]
    out = [[0]*4 for _ in range(4)]
    for j in range(4):
        q = [0,0,0,0]
        q[j] = 1
        c,d = q[:2],q[2:]
        oc,od = [0,0],[0,0]
        for i in range(2):
            for k in range(2):
                a,b = entries[2*i+k]
                oc[i] ^= a & c[k]
                od[i] ^= (a & d[k]) ^ (b & c[k])
        col = [oc[0],oc[1],od[0],od[1]]
        for i in range(4):
            out[i][j] = col[i]
    return out

def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) & 1
             for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a):
    return [list(row) for row in zip(*a)]

def rank_mod2(a):
    m = [row[:] for row in a]
    r = 0
    for c in range(len(m[0])):
        p = next((i for i in range(r,len(m)) if m[i][c]), None)
        if p is None:
            continue
        m[r],m[p] = m[p],m[r]
        for i in range(len(m)):
            if i != r and m[i][c]:
                m[i] = [x^y for x,y in zip(m[i],m[r])]
        r += 1
    return r

def minus_identity(t):
    a = [row[:] for row in t]
    for i in range(4):
        a[i][i] ^= 1
    return a

def matvec(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(len(v))) & 1 for i in range(len(a)))

def image_nonzero(a):
    vals = set()
    for bits in range(16):
        v = tuple((bits >> i) & 1 for i in range(4))
        vals.add(matvec(a,v))
    return sorted(v for v in vals if any(v))

def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["schema"] == "STAGE32_MAIN_SCRATCH_EX1_H4_UNIFORM_TRANSVECTION_28_TO_3_CANDIDATE_V1"
    assert cert["status"] == "SCRATCH_EXACT_UNAUDITED_CROSS_LANE_ADAPTER_CANDIDATE"
    assert cert["decision"]["authority_changed"] is False
    assert cert["decision"]["claim_dag_changed"] is False

    locks = cert["source_locks"]
    ex1f = load_locked_json(locks["ex1_05f"])
    ex1g = load_locked_json(locks["ex1_05g"])
    fixed = load_locked_json(locks["fixed_v6_pair_mass_parity"])
    parity_note = load_locked_text(locks["arbitrary_contact_parity_lemma"])
    fixedpoint_note = load_locked_text(locks["boundary_fixed_point_accounting"])
    post1503 = load_locked_json(locks["post1503_28"])
    wadapter = load_locked_json(locks["retained_F2_4_W"])
    historical = load_locked_json(locks["historical_transvection"])
    principal = load_locked_json(locks["principal_rosati"])
    incidence = load_locked_json(locks["marked_incidence"])
    labels = load_locked_json(locks["label_adapter"])
    v6 = load_locked_json(locks["v6_witness"])

    qladder = ex1g["Q_defect_ladder"]
    assert qladder["EX1_Q_values"] == list(range(210,267,2))
    assert ex1g["fixed_correspondence_arithmetic"]["Q_Rosati"] == 602
    assert ex1g["fixed_correspondence_arithmetic"]["independent_of_EX1_Q_at_fixed_V6_h4_layer"] is True
    shell = ex1g["mod2_shell_replay_adapter"]
    assert shell["fixed_plane_survivor_count"] == 28
    assert shell["fixed_plane_survivors_decimal"] == EXPECTED_28
    assert post1503["q602_mod2_preflight"]["surviving_residue_classes_decimal"] == EXPECTED_28

    assert ex1f["local_base_change_adapter"]["node_parity"] == "k_i congruent m mod 2 for both factors, agreeing with the Beauville odd-contact ramification criterion."
    assert ex1f["fixed_v6_six_cusp_degree_replay"]["exceptional_mass"] == 266
    assert "does not require f_1 to be unramified" in parity_note
    assert "all ramification of this specified pullback is accounted for by\nodd exceptional contacts" in fixedpoint_note

    assert fixed["calculation_uses_O"] is False
    assert fixed["post1505_mass_and_matrix_match"] is True
    assert fixed["parity_matrix"] == EXPECTED_MATRIX
    assert incidence["checks"]["distinct_realized_boundary_pair_count"] == 12
    assert set(incidence["boundary_pair_counts"].values()) == {4}
    assert labels["cusp_pairs"]["Z3"] == [2,4]
    assert v6["target"]["row_id"] == "g1-d186"
    assert v6["target"]["e"] == 266

    W = wadapter["retained_F2_4_adapter"]
    assert W["ordered_basis"] == ["e1","e2","r*e1","r*e2"]
    assert W["W_basis_vectors"] == [[0,0,1,0],[0,0,0,1]]
    assert W["W_equals_kernel_r_mod2"] is True
    assert historical["weierstrass_parity_action"]["branch_permutation"] == "(2 4)"
    assert historical["basis_independent_predicate"]["individual_retained_W_line_identified"] is False

    e = [[int(x)&1 for x in row] for row in principal["principal_polarization"]["riemann_form_matrix"]
    classification = {k:[] for k in EXPECTED_CLASSIFICATION}
    survivors = []
    lines = []
    for z in EXPECTED_28:
        t = t_matrix_mod2(z)
        a = minus_identity(t)
        sym = matmul(matmul(transpose(t), e), t) == e
        rk = rank_mod2(a)
        ims = image_nonzero(a)
        inW = bool(ims) and all(v[0] == 0 and v[1] == 0 for v in ims)
        if not sym:
            classification["non_symplectic"].append(z)
        elif rk == 0:
            classification["symplectic_rank0_identity"].append(z)
        elif rk == 1 and inW:
            classification["symplectic_rank1_image_in_W"].append(z)
            survivors.append(z)
            assert len(ims) == 1
            lines.append(list(ims[0]))
        elif rk == 2 and inW:
            classification["symplectic_rank2_image_in_W"].append(z)
        elif rk == 2 and not inW:
            classification["symplectic_rank2_image_not_in_W"].append(z)
        else:
            raise AssertionError((z,sym,rk,ims,inW))

    assert classification == EXPECTED_CLASSIFICATION
    assert survivors == EXPECTED_3
    assert lines == [[0,0,1,0],[0,0,0,1],[0,0,1,1]]
    assert cert["direct_filter"]["classification"] == EXPECTED_CLASSIFICATION
    assert cert["direct_filter"]["surviving_residues_decimal"] == EXPECTED_3
    assert cert["direct_filter"]["surviving_image_lines"] == lines
    assert cert["coarse_joint_effect"] == {
        "old_cells_29_times_28":812,
        "new_cells_29_times_3":87,
        "removed_coarse_cells":725,
        "EX1_Q_states_excluded":0,
        "residue_classes_per_Q_state_after_candidate_filter":3,
    }

    print("PASS scratch EX1 h=4 direct transvection replay")
    print("EX1_states=29 input_residues=28 survivors=73,97,235 coarse_cells=87")
    print("authority=SCRATCH_UNAUDITED q_states_excluded=0 Q602_excluded=false Stage32_closed=false")

if __name__ == "__main__":
    main()
