#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CERT = Path("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-principal-polarization-rosati.json")

def load_json(rel):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)

def blob_sha1(rel):
    data = (ROOT / rel).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()

def canonical_sha256_obj(obj):
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    data = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()

def require(cond, message):
    if not cond:
        raise AssertionError(message)

def radd(x, y):
    return [x[0] + y[0], x[1] + y[1]]

def rmul(x, y):
    return [x[0]*y[0] - 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0]]

def rconj(x):
    return [x[0], -x[1]]

ZERO = [0, 0]
ONE = [1, 0]

def mtranspose_conj(A):
    return [[rconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]

def mmul(A, B):
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            v = ZERO
            for k in range(len(B)):
                v = radd(v, rmul(A[i][k], B[k][j]))
            row.append(v)
        out.append(row)
    return out

def identity(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]

def matrix_coords(A):
    v = []
    for row in A:
        for a, b in row:
            v.extend([a, b])
    return v

def coord_matrix_for_rosati(H, Hinv):
    cols = []
    for pos in range(4):
        i, j = divmod(pos, 2)
        for which in range(2):
            A = [[ZERO[:], ZERO[:]], [ZERO[:], ZERO[:]]]
            A[i][j] = [1, 0] if which == 0 else [0, 1]
            Adag = mmul(mmul(Hinv, mtranspose_conj(A)), H)
            cols.append(matrix_coords(Adag))
    return [[cols[c][r] for c in range(8)] for r in range(8)]

def imatmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path, default=DEFAULT_CERT)
    args = parser.parse_args()

    cert = load_json(args.check)
    require(cert["schema"] == "STAGE32_POST1490_O210_Q4_BOLZA_PRINCIPAL_POLARIZATION_ROSATI_LOCK_V1", "schema")
    require(cert["fixed_target"] == {
        "row_id":"g1-d186","d":186,"e":266,"genus":1,
        "z":[-15,62,-44,26,32],"O":210,"qprime":4
    }, "fixed target")

    front_lock = cert["source_locks"]["bolza_frontier"]
    require(blob_sha1(front_lock["path"]) == front_lock["blob_sha1"], "frontier blob lock")
    frontier = load_json(front_lock["path"])
    require(frontier["canonical_sha256_without_this_field"] == front_lock["canonical_sha256"], "frontier stored canonical")
    require(canonical_sha256_obj(frontier) == front_lock["canonical_sha256"], "frontier canonical replay")
    require(frontier["decision"]["next_exact_leaf"] == "O210_Q4_BOLZA_ROSATI_LATTICE_ENUMERATION", "frontier leaf")
    require(frontier["decision"]["rosati_matrix_source_locked"] is False, "frontier missing-input alignment")

    note_lock = cert["source_locks"]["source_note"]
    require(blob_sha1(note_lock["path"]) == note_lock["blob_sha1"], "source-note blob lock")

    ext = cert["source_locks"]["principal_polarization_external"]
    require(ext["arxiv"] == "1806.03826v2", "external arxiv")
    require(ext["doi"] == "10.2140/obs.2019.2.257", "external doi")
    require(ext["locators"] == ["Proposition 3.1", "Table 4, Delta=-8 row"], "external locators")
    require(ext["grh_used_for_this_instance"] is False, "GRH firewall")

    require(cert["ring_model"] == {
        "symbol":"s","relation":"s^2=-2","order":"Z[s]","conjugation":"s -> -s"
    }, "ring model")

    pol = cert["principal_polarization"]
    H = pol["H"]
    Hinv = pol["H_inverse"]
    expected_H = [[[2,0],[1,1]],[[1,-1],[2,0]]]
    expected_Hinv = [[[2,0],[-1,-1]],[[-1,1],[2,0]]]
    require(H == expected_H, "H")
    require(Hinv == expected_Hinv, "H inverse")
    require(mtranspose_conj(H) == H, "H Hermitian")
    require(mmul(H, Hinv) == identity(2) and mmul(Hinv, H) == identity(2), "H inverse exact")
    require(pol["determinant"] == 1 and pol["positive_definite"] is True, "principal positive unimodular")

    ros = cert["rosati_involution"]
    D = coord_matrix_for_rosati(H, Hinv)
    require(D == ros["z_linear_matrix"], "Rosati coordinate replay")
    require(imatmul(D, D) == [[1 if i == j else 0 for j in range(8)] for i in range(8)], "Rosati involution square")
    require(ros["involutive"] is True, "stored involutive flag")
    require(ros["formula"] == "T^dagger = H^{-1} * conjugate_transpose(T) * H", "Rosati formula")

    bnd = cert["correspondence_bound"]
    require(bnd["degrees"] == [105,81], "degree pair")
    require(bnd["scalar_bound"] == 105*81 == 8505, "scalar bound")
    require(bnd["integral_rank"] == 8 and bnd["finite_frontier"] is True, "finite rank-8 frontier")
    require(bnd["enumerated_here"] is False, "enumeration firewall")
    require(bnd["explicit"] == "8505*H - conjugate_transpose(T)*H*T is positive semidefinite", "explicit bound")

    dec = cert["decision"]
    require(dec["rosati_matrix_source_locked"] is True, "Rosati lock decision")
    require(dec["O210_excluded"] is False, "O210 remains open")
    require(dec["next_exact_leaf"] == "O210_Q4_BOLZA_ROSATI_BOUND_ENUMERATION", "next leaf")

    for key in [
        "O186_reopened","O188_reopened","abel_jacobi_zero_reopened","product_rosati_assumed",
        "integral_T_realization_proved","full178_authorized","receiver_credit","route_credit",
        "theorem_credit","endpoint_credit","perfect_cuboid_claim"
    ]:
        require(cert["firewalls"][key] is False, f"firewall {key}")

    actual = canonical_sha256_obj(cert)
    require(actual == cert["canonical_sha256_without_this_field"], "certificate canonical sha256")
    print(json.dumps({
        "ok": True,
        "canonical_sha256": actual,
        "H": "[[2,1+s],[1-s,2]]",
        "rosati_locked": True,
        "O210_excluded": False,
        "next_exact_leaf": dec["next_exact_leaf"]
    }, sort_keys=True))

if __name__ == "__main__":
    main()
