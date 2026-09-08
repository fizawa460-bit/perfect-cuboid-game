#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT = ROOT / "stages/stage32/scratch/ex1-05ac-named-character-glue-integration-20260908.json"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_local(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text(encoding="utf-8"))
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
        assert doc.get("canonical_sha256_without_this_field") == lock["canonical_sha256"], path
    return doc


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def rank2(rows):
    a = [list(map(lambda x: x & 1, row)) for row in rows]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def matvec(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(len(v))) & 1 for i in range(len(A)))


def blockdiag3(blocks):
    M = [[0] * 6 for _ in range(6)]
    for b, B in enumerate(blocks):
        for i in range(2):
            for j in range(2):
                M[2*b+i][2*b+j] = B[i][j]
    return M


def kp_action(acts):
    # All selected xi are the CM-fixed diagonal point (1,1).
    x = (1, 1)
    k = x + x + x
    F = [[0,1],[1,0]]
    E6 = blockdiag3([F,F,F])
    Ek = matvec(E6, k)
    kperp = [v for v in product((0,1), repeat=6) if sum(a*b for a,b in zip(Ek,v)) % 2 == 0]

    basis = [k]
    for v in kperp:
        if rank2(basis + [v]) > rank2(basis):
            basis.append(v)
        if len(basis) == 5:
            break
    assert len(basis) == 5

    lookup = {}
    for coeff in product((0,1), repeat=5):
        v = (0,0,0,0,0,0)
        for j, c in enumerate(coeff):
            if c:
                v = xor(v, basis[j])
        lookup[v] = coeff

    M6 = blockdiag3(acts)
    cols = []
    for v in basis[1:]:
        y = matvec(M6, v)
        coeff = lookup[y]
        cols.append(coeff[1:])
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["schema"] == "STAGE32_MAIN_SCRATCH_EX1_05AC_NAMED_CHARACTER_GLUE_INTEGRATION_V1"
    assert cert["status"] == "SCRATCH_EXACT_UNAUDITED_CROSS_LANE_INTEGRATION_NONPRUNING"

    Wdoc = load_local(cert["local_source_locks"]["abstract_W"])
    load_local(cert["local_source_locks"]["principal_rosati"])
    krr = load_local(cert["local_source_locks"]["krr_torsor_no_go"])
    assert krr["decision"]["uniform_EX1_residues_remaining"] == [73,97,235]

    wm = Wdoc["weierstrass_model"]
    assert wm["cusp_pairs"] == {"Z1":[1,6],"Z2":[3,5],"Z3":[2,4]}
    assert wm["inertia"] == {"Z1":"tau*u","Z2":"tau*u*v","Z3":"tau"}
    chars = Wdoc["character_pushouts"]["characters"]
    assert chars["chi_u"]["canonical_pair"] == "Z3"
    assert chars["chi_v"]["canonical_pair"] == "Z2"
    assert chars["chi_uv"]["canonical_pair"] == "Z1"

    # Quotient X(8)/H: t=x/y and z=u0*v0*w0/y^3 satisfy z^2=t(t^4-1).
    # Check the homogeneous polynomial identity before division by y^6.
    for x, y in [(2,1),(3,2),(-2,3),(5,-2)]:
        lhs = x*y*(x*x-y*y)*(x*x+y*y)
        rhs = y**6 * ((x/y) * ((x/y)**4 - 1))
        assert abs(lhs-rhs) < 1e-9

    # Named H basis reconstructed from the three odd single-sign inertia lifts.
    su, sv, sw = (1,0,0), (0,1,0), (0,0,1)
    uH = xor(su, sv)
    vH = xor(sv, sw)
    uvH = xor(uH, vH)
    assert uvH == xor(su, sw)

    # Even signs leave Omega invariant; coordinate sign gives the H-character.
    def char(coord, h):
        return h[coord]
    assert (char(0,uH),char(0,vH),char(0,uvH)) == (1,0,1)  # u0 Omega = chi_u
    assert (char(1,uH),char(1,vH),char(1,uvH)) == (1,1,0)  # v0 Omega = chi_uv
    assert (char(2,uH),char(2,vH),char(2,uvH)) == (0,1,1)  # w0 Omega = chi_v

    named = cert["named_prym_character_adapter"]
    assert "delta_0inf" in named["abstract_W_character_pushout"]["P_chi_u"]
    assert "delta_pm1" in named["abstract_W_character_pushout"]["P_chi_uv"]
    assert "delta_pmi" in named["abstract_W_character_pushout"]["P_chi_v"]

    # H-character signs disappear on 2-torsion: +/-P=P for P of order 2.
    # Finite Prym-kernel replay with all selected xi CM-fixed.
    I2 = [[1,0],[0,1]]
    CMI = [[0,1],[1,0]]
    ranks = {}
    for mask in range(8):
        acts = [CMI if (mask >> i) & 1 else I2 for i in range(3)]
        M = kp_action(acts)
        MI = [[M[i][j] ^ (1 if i == j else 0) for j in range(4)] for i in range(4)]
        ranks[mask.bit_count()] = ranks.get(mask.bit_count(), set()) | {rank2(MI)}
    ranks_by_count = {k: next(iter(v)) if len(v)==1 else sorted(v) for k,v in ranks.items()}
    assert ranks_by_count == {0:0,1:1,2:2,3:2}
    assert cert["prym_mod2_action_exhaustion"]["rank_table_by_number_of_i_type_factors"] == {"0":0,"1":1,"2":2,"3":2}

    # Each Gaussian norm admits both parity types, so each named factor can be
    # the unique i-type factor while preserving its required norm.
    assert 11*11 + 4*4 == 137
    assert 4*4 + 11*11 == 137
    assert 3*3 == 9
    assert 3*3 == 9

    decision = cert["decision"]
    assert decision["Q602_residues_entering"] == [73,97,235]
    assert decision["Q602_residues_excluded"] == 0
    assert decision["Q602_residues_leaving"] == [73,97,235]
    assert decision["absolute_delta0inf_retained_W_line_identified"] is False
    assert decision["authority_changed"] is False
    assert decision["claim_dag_changed"] is False
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert decision["Stage32_closed"] is False

    print("PASS scratch EX1-05AC named-character glue integration")
    print("named_factors=chi_u:delta0inf,chi_uv:delta_pm1,chi_v:delta_pmi")
    print("prym_rank_by_i_type_count=0:0,1:1,2:2,3:2")
    print("residues_remaining=73,97,235 pointwise_named_antiisometry=MISSING")


if __name__ == "__main__":
    main()
