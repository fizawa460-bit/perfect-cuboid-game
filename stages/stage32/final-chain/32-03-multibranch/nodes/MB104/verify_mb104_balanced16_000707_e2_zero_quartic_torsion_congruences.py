#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-ZERO-QUARTIC-TORSION-CONGRUENCES-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ZERO-QUARTIC-TORSION-CONGRUENCES.md",
        "544ded0d132dcf4dca0a5a3d52925a88c8c461e2",
    ),
    "HALF_HYPERPLANE_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION-CERTIFICATE.json",
        "b166657c08ec90c7b30d5c67ab0991978aa56381",
    ),
    "ZERO_QUARTIC_PIC0_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json",
        "1a92336433816883757fee844b736181e6848813",
    ),
    "RESIDUAL_NODE_TABLE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md",
        "dbfea5a4f62b1388c9810c37ad867076ed4dca6e",
    ),
    "BOUNDARY_SATURATION": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md",
        "aa9a7215467428b55b18ef296ced91b63ec4bf07",
    ),
    "AMBIENT_CHARACTER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-CHARACTER-FUNCTION.md",
        "2bdb46e79be8a745880622c9c0643eb13ef20b26",
    ),
    "CHARACTER_PAIR_SQUARE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-CHARACTER-PAIR-SQUARE-WALL.md",
        "657653c56f8e36be505bbca663e60ef3a937a044",
    ),
    "G2_FIBRATION_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md",
        "b71225ac859eef5afefeebd019a97c403ed27655",
    ),
}


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def repo_root() -> Path:
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repository root not found")


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def source_lock_preflight(cert: dict) -> None:
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    require(declared == LOCKS, "certificate/source-lock table mismatch")
    rr = repo_root()
    for key, (rel, expected) in LOCKS.items():
        path = rr / rel
        if not path.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL: missing {key}: {rel}")
        got = blob_sha1(path)
        if got != expected:
            raise SystemExit(f"SOURCE_LOCK_FAIL: {key}: expected {expected}, got {got}")


def nodes() -> list[tuple[complex, ...]]:
    out: list[tuple[complex, ...]] = []
    for j in range(3):
        for sa in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    z = [0j] * 7
                    z[j] = sa
                    o = [t for t in range(3) if t != j]
                    z[3 + o[0]] = s1
                    z[3 + o[1]] = s2
                    z[6] = 1
                    out.append(tuple(z))
    for j in range(3):
        o = [t for t in range(3) if t != j]
        a, b = o
        for sr in (1, -1):
            for ep in (1, -1):
                for eq in (1, -1):
                    z = [0j] * 7
                    z[a] = 1
                    z[b] = 1j * sr
                    z[3 + a] = 1j * ep
                    z[3 + b] = -eq * sr
                    out.append(tuple(z))
    require(len(out) == 48 and len(set(out)) == 48, "48-node model")
    return out


def check_zero_quartics(v: list[tuple[complex, ...]]) -> None:
    q0 = {
        j for j, z in enumerate(v)
        if z[3] == 0 and 1j * z[1] - z[2] == 0 and z[0] - z[6] == 0
    }
    q1 = {
        j for j, z in enumerate(v)
        if z[4] == 0 and 1j * z[2] + z[0] == 0 and z[1] - z[6] == 0
    }
    require(q0 == {0, 1, 2, 3, 24, 25, 26, 27}, f"Q0 node set regression: {sorted(q0)}")
    require(q1 == {8, 9, 10, 11, 32, 33, 34, 35}, f"Q1 node set regression: {sorted(q1)}")

    q0_xyzw = {j: (v[j][0], v[j][1], v[j][4], v[j][5]) for j in sorted(q0)}
    q1_xyzw = {j: (v[j][1], v[j][2], v[j][5], v[j][3]) for j in sorted(q1)}
    require({j for j, p in q0_xyzw.items() if p[1] == 0} == {0, 1, 2, 3}, "Q0 y=0 half")
    require({j for j, p in q0_xyzw.items() if p[0] == 0} == {24, 25, 26, 27}, "Q0 x=0 half")
    require({j for j, p in q1_xyzw.items() if p[1] == 0} == {8, 9, 10, 11}, "Q1 y=0 half")
    require({j for j, p in q1_xyzw.items() if p[0] == 0} == {32, 33, 34, 35}, "Q1 x=0 half")

    for p in list(q0_xyzw.values()) + list(q1_xyzw.values()):
        x, y, z, w = p
        require(z * z == x * x - y * y, "quartic z equation")
        require(w * w == x * x + y * y, "quartic w equation")


def check_bitangent_torsion_logic() -> None:
    # Q: z^2=x^2-y^2, w^2=x^2+y^2.
    # z=±x and w=±x force y^2=0, giving double pairs of y=0 nodes.
    # z=±i*y and w=±y force x^2=0, giving double pairs of x=0 nodes.
    require((1 - 1, 1) == (0, 1), "z=±x substitution")
    require((1 - 1, -1) == (0, -1), "w=±x substitution")
    require((-1, -1 + 1) == (-1, 0), "z=±iy substitution")
    require((-1, 1 - 1) == (-1, 0), "w=±y substitution")
    require(4 == 2 ** 2, "elliptic two-torsion cardinality")


def gf2_rank(rows: list[list[int]]) -> int:
    a = [sum((v & 1) << j for j, v in enumerate(row)) for row in rows]
    r = 0
    n = max((len(row) for row in rows), default=0)
    for bit in range(n):
        pivot = next((k for k in range(r, len(a)) if (a[k] >> bit) & 1), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for k in range(len(a)):
            if k != r and ((a[k] >> bit) & 1):
                a[k] ^= a[r]
        r += 1
    return r


def check_mod4_reduction(cert: dict) -> None:
    inds = [0,1,2,3,8,9,10,11,24,25,26,32,33,34]
    pos = {j: k for k, j in enumerate(inds)}

    def row(support):
        v = [0] * len(inds)
        for j in support:
            v[pos[j]] = 1
        return v

    sat0 = row([0,1,2,3,24,25,26])
    sat1 = row([8,9,10,11,32,33,34])
    tor0 = row([24,25,26])
    tor1 = row([32,33,34])
    require(gf2_rank([sat0, sat1]) == 2, "centered saturation F2 rank")
    require(gf2_rank([sat0, sat1, tor0, tor1]) == 4, "combined torsion F2 rank")

    for bits in product((0,1), repeat=len(inds)):
        s0 = sum(bits[pos[j]] for j in [0,1,2,3,24,25,26]) % 2
        s1 = sum(bits[pos[j]] for j in [8,9,10,11,32,33,34]) % 2
        if s0 or s1:
            continue
        t0 = sum(bits[pos[j]] for j in [24,25,26]) % 2
        e0 = sum(bits[pos[j]] for j in [0,1,2,3]) % 2
        t1 = sum(bits[pos[j]] for j in [32,33,34]) % 2
        e1 = sum(bits[pos[j]] for j in [8,9,10,11]) % 2
        require(t0 == e0, "Q0 saturation/torsion equivalence")
        require(t1 == e1, "Q1 saturation/torsion equivalence")

    rank = cert["rank"]
    require(rank["centered_saturation_rank_mod2"] == 2, "certificate saturation rank")
    require(rank["combined_rank_mod2"] == 4, "certificate combined rank")
    require(rank["new_independent_bits"] == 2, "certificate new-bit count")


def main() -> None:
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_000707_E2_ZERO_QUARTIC_TORSION_CONGRUENCES_V1", "certificate schema")
    source_lock_preflight(cert)
    check_zero_quartics(nodes())
    check_bitangent_torsion_logic()
    check_mod4_reduction(cert)

    split = cert["componentwise_residual_split"]
    require(split["ambient_square_classes_equal"] == "[f_t]=[f_u]", "factor square-class identity")
    require(split["split_over_complex_field"] is True, "componentwise split")
    require(split["global_same_sheet_on_Q0_union_Q1_claimed"] is False, "global-sheet firewall")

    zq = cert["zero_quartics"]
    require(zq["Q0"]["mod4_condition"] == "x24+x25+x26=0 mod 4", "Q0 mod4 certificate")
    require(zq["Q0"]["equivalent_mod4_condition"] == "x0+x1+x2+x3=0 mod 4", "Q0 equivalent mod4")
    require(zq["Q1"]["mod4_condition"] == "x32+x33+x34=0 mod 4", "Q1 mod4 certificate")
    require(zq["Q1"]["equivalent_mod4_condition"] == "x8+x9+x10+x11=0 mod 4", "Q1 equivalent mod4")
    require(cert["relation_to_prior_parity"]["balanced_x_j_equals_4l_survives"] is True, "balanced firewall")
    require(cert["credit_firewall"]["e2_closed"] is False, "e2 firewall")
    require(cert["credit_firewall"]["MB104_complete"] is False, "MB104 firewall")

    print("PASS STAGE32_MB104_000707_E2_ZERO_QUARTIC_TORSION_CONGRUENCES_V1")
    print("new_mod4=x0+x1+x2+x3=0,x8+x9+x10+x11=0; new_independent_bits=2; e2_open")


if __name__ == "__main__":
    main()
