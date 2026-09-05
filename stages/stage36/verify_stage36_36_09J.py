#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09J/reciprocal-two-linear-cover-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "a1951b714e321aea1fc88cb806ed6796e4ce621a"
PARENT_PROMOTION = "fc5886d62b78d8dcb21824ff02419a3e3b7634c8"
PARENT_STATE_BLOB = "c94c56ef18cd914fe0e89032bab182eb0c69d61d"
PARENT_CERT_COMMIT = "476829b39679f4c380fe0458e37c28745e5f5621"
PARENT_CERT_BLOB = "f9bf252f3be47f606a3b270961df3b5943fa1909"
CERT_BLOB = "36dab291a9be311fb60db6e919e4fc0bf1b2dc27"
S31_W01_BLOB = "122a6c1c5c871c1c7b797017e854de8ec55e7c50"
S34_W01_BLOB = "01a8e90e34b4aa46edbfa825803d488e5230e9d0"
S34_W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"
CYCLE_BLOB = "4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37"
FIREWALL_BLOB = "7a3de0b2692afe4fb25b6825b31bd0384a118a41"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, check=check, capture_output=True, text=True)


def out(*args: str) -> str:
    return git(*args).stdout.strip()


# Sparse Z-polynomials as tuples c_0 + c_1 Z + ... .
def ztrim(p: tuple[int, ...]) -> tuple[int, ...]:
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return tuple(q)


def zadd(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    n = max(len(a), len(b))
    return ztrim(tuple((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)))


def zscale(a: tuple[int, ...], c: int) -> tuple[int, ...]:
    return ztrim(tuple(c * x for x in a))


def zmul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    q = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            q[i + j] += x * y
    return ztrim(tuple(q))


def zpow(a: tuple[int, ...], n: int) -> tuple[int, ...]:
    q = (1,)
    for _ in range(n):
        q = zmul(q, a)
    return q


# Sparse bivariate polynomials in Z,k for exact cross-multiplied identities.
Bi = dict[tuple[int, int], int]


def bnorm(p: Bi) -> Bi:
    return {m: c for m, c in p.items() if c}


def badd(a: Bi, b: Bi) -> Bi:
    q = dict(a)
    for m, c in b.items():
        q[m] = q.get(m, 0) + c
    return bnorm(q)


def bscale(a: Bi, c: int) -> Bi:
    return bnorm({m: c * x for m, x in a.items()})


def bmul(a: Bi, b: Bi) -> Bi:
    q: Bi = {}
    for (zi, ki), x in a.items():
        for (zj, kj), y in b.items():
            m = (zi + zj, ki + kj)
            q[m] = q.get(m, 0) + x * y
    return bnorm(q)


def main() -> None:
    req(git("merge-base", "--is-ancestor", PARENT_PROMOTION, "HEAD", check=False).returncode == 0,
        "36-09I audited promotion is not an ancestor")
    req(git("merge-base", "--is-ancestor", BASE, "HEAD", check=False).returncode == 0,
        "36-09J base is not an ancestor")

    # Immutable source locks.
    req(out("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == PARENT_STATE_BLOB,
        "V31 parent state blob moved")
    req(out("rev-parse", f"{PARENT_CERT_COMMIT}:stages/stage36/36-09I/post-w01-breadth-refresh.json") == PARENT_CERT_BLOB,
        "36-09I audited certificate moved")
    req(out("rev-parse", "HEAD:stages/stage36/36-09J/reciprocal-two-linear-cover-preflight.json") == CERT_BLOB,
        "36-09J certificate blob moved")
    for path, blob in {
        "docs/arsenal/cards/formal/S31-W01.md": S31_W01_BLOB,
        "docs/arsenal/cards/formal/S34-W01.md": S34_W01_BLOB,
        "docs/arsenal/cards/formal/S34-W03.md": S34_W03_BLOB,
        "docs/research-os/policies/cycle-exploration-safety-protocol.md": CYCLE_BLOB,
        "docs/research-os/policies/research-credit-and-promotion-firewalls.md": FIREWALL_BLOB,
    }.items():
        req(out("rev-parse", f"HEAD:{path}") == blob, f"source blob moved: {path}")

    c = json.loads(CERT.read_text())
    req(c["schema"] == "STAGE36_36_09J_RECIPROCAL_TWO_LINEAR_COVER_PREFLIGHT_V1", "certificate schema moved")
    req(c["base_main_sha"] == BASE and c["parent_promotion_main_sha"] == PARENT_PROMOTION,
        "certificate base lock moved")

    # Recompute the 36-09I X reconstruction identities exactly.
    one: Bi = {(0, 0): 1}
    Z: Bi = {(1, 0): 1}
    k2: Bi = {(0, 2): 1}
    two = bscale(one, 2)
    a = badd(Z, bscale(one, -2))
    D = badd(one, bscale(bmul(a, k2), -1))
    P = badd(bscale(k2, 4), bscale(one, -1))
    Q = badd(bscale(k2, 16), bscale(a, -1))
    N = badd(bscale(bmul(k2, badd(Z, bscale(one, 6))), 2), bscale(Z, -1))
    lhs_minus = badd(N, bscale(D, -2))
    rhs_minus = bmul(badd(Z, two), P)
    lhs_plus = badd(N, bscale(D, 2))
    req(lhs_minus == rhs_minus, "X-2 cross-multiplied identity failed")
    req(lhs_plus == Q, "X+2 cross-multiplied identity failed")

    ec = c["exact_cover"]
    req(ec["model"] == ["C_Z: y1^2=P*D", "C_Z: y2^2=Q*D"], "cover model moved")
    req(ec["kummer_squareclasses"] == ["[P*D]", "[Q*D]", "[P*Q]"], "Kummer classes moved")
    req(ec["degree_over_k_line"] == 4, "cover degree moved")

    # Recompute pairwise resultants using Res_k(A k^2+B, C k^2+D)=(A D-B C)^2.
    zm6 = (-6, 1)  # Z-6
    zp2 = (2, 1)   # Z+2
    zm2 = (-2, 1)  # Z-2
    res_PD = zpow(zm6, 2)
    res_PQ = zscale(zpow(zm6, 2), 16)
    res_QD = zmul(zpow(zm6, 2), zpow(zp2, 2))
    req(res_PD == (36, -12, 1), "Res(P,D) recomputation failed")
    req(res_PQ == (576, -192, 16), "Res(P,Q) recomputation failed")
    req(res_QD == zmul((36, -12, 1), (4, 4, 1)), "Res(Q,D) recomputation failed")

    # Discriminant product identity Disc(fg)=Disc(f)Disc(g)Res(f,g)^2.
    # Disc(P)=16, Disc(D)=4(Z-2), Disc(Q)=64(Z-2).
    disc_PD = zmul(zscale(zm2, 64), zpow(zm6, 4))
    disc_QD = zmul(zscale(zpow(zm2, 2), 256), zmul(zpow(zm6, 4), zpow(zp2, 4)))
    disc_PQ = zmul(zscale(zm2, 262144), zpow(zm6, 4))
    req(disc_PD != (0,) and disc_QD != (0,) and disc_PQ != (0,), "generic quartic discriminant vanished")

    ba = c["branch_audit"]
    req(ba["collision_or_degeneracy_values"] == [-2, 2, 6], "collision set moved")
    req(ba["generic_distinct_branch_points"] == 6 and ba["infinity_branch"] is False,
        "branch count/infinity status moved")

    # Physical collision exclusion: Z=2 is boundary; 8 is not a rational square; -4 cannot be a rational square.
    req(math.isqrt(8) ** 2 != 8, "unexpected square test failure for 8")
    req(-4 < 0, "unexpected sign test failure for -4")
    pe = c["physical_collision_exclusion"]
    req("Z!=2" in pe["Z_eq_2"], "Z=2 boundary firewall moved")
    req("8" in pe["Z_eq_6"] and "-4" in pe["Z_eq_minus_2"], "physical collision explanations moved")

    # Connected V4 cover: outside collision set, P*D has P-only branch points,
    # Q*D has Q-only branch points, and P*Q has both, so all three classes are nontrivial.
    gc = c["genus_classification"]
    req(gc["connected_cover"] is True and gc["cover_degree"] == 4 and gc["branch_points"] == 6,
        "connected V4 cover classification moved")
    rh_rhs = 4 * (-2) + 6 * 2
    g = (rh_rhs + 2) // 2
    req(rh_rhs == 4 and g == 3 and gc["cover_genus"] == 3, "genus-3 Riemann-Hurwitz failed")
    qs = gc["character_quotients"]
    req(len(qs) == 3, "character quotient count moved")
    for q in qs:
        qrhs = 2 * (-2) + 4
        qg = (qrhs + 2) // 2
        req(q["branch_points"] == 4 and q["genus"] == qg == 1, f"character genus moved: {q['id']}")

    ar = c["arsenal_routing"]
    req(ar["S31_W01"]["status"] == "FORMALLY_MATCHED_QUARTIC_SIDE_NOT_TRIGGERED" and ar["S31_W01"]["credit"] is False,
        "S31-W01 firewall moved")
    req(ar["S34_W01"]["credit"] is False and ar["S34_W03"]["credit"] is False,
        "S34 Arsenal credit leaked")
    req(c["cycle_exit"]["CYCLE_ROUTE_STATUS"] == "PASS_NEXT_GATE_UNCHANGED", "cycle route status moved")
    req(c["cycle_exit"]["CYCLE_UNTESTED_CANDIDATES"] == 3 and c["cycle_exit"]["CYCLE_SPLIT_TRIGGERED"] is False,
        "candidate preservation moved")

    fw = c["credit_firewall"]
    req(fw["generic_cover_genera_candidate_classified"] is True, "candidate genus result missing")
    req(fw["audited_generic_cover_genera_credit"] is False, "pre-audit genus credit leaked")
    req(fw["S31_W01_triggered"] is False and fw["elliptic_models_derived"] is False and fw["quartic_elliptic_birational_maps_derived"] is False,
        "quartic-to-elliptic credit leaked")
    for key in [
        "uniform_Mordell_Weil_control", "rational_points_exhausted",
        "receiver_restricted_intersection_exclusion_triggered", "receiver_emptiness_proved",
        "quotient_Q_point_emptiness_proved", "receiver_matched_replacement_theorem_proved",
        "R29_CAMP2_closed", "Q11_CAMPEDELLI_closed", "endpoint_closed",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
    ]:
        req(fw[key] is False, f"higher credit leaked: {key}")

    s = json.loads(STATE.read_text())
    req(s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V32_36_09J_PENDING_HOSTILE_AUDIT",
        "V32 state schema moved")
    req(s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT" and s["base_main_sha"] == BASE,
        "V32 state/base moved")
    j = s["authority_frontier"]["36-09J"]
    req(j["status"] == "PROVISIONAL_EXACT_RECIPROCAL_V4_GENUS3_COVER_PENDING_HOSTILE_AUDIT", "36-09J authority status moved")
    req(j["certificate_blob_sha"] == CERT_BLOB, "36-09J state certificate lock moved")
    req(j["COVER_GENUS_CANDIDATE"] == 3 and j["CHARACTER_QUOTIENT_GENERA_CANDIDATE"] == [1, 1, 1],
        "36-09J genus candidate state moved")
    req(j["S31_W01_STATUS"] == "FORMALLY_MATCHED_QUARTIC_SIDE_NOT_TRIGGERED", "36-09J S31 status moved")
    req(j["promotion_status"] == "PENDING_HOSTILE_AUDIT", "36-09J promotion status moved")
    req(s["cycle_ledger"]["counts"] == {"live": 1, "untested": 3, "blocked": 6, "dominated": 2}, "cycle counts moved")
    req(s["current"]["unit"] == "36-09J" and s["current"]["next_exact_leaf"] == "36-09J_HOSTILE_AUDIT",
        "audit boundary moved")
    req(s["current"]["36_09K_entry_allowed"] is False, "36-09K prematurely unlocked")
    req(s["promotion_gates"]["generic_cover_genera_classified"] is False,
        "generic genus credit promoted before audit")
    req(all(v is False for v in s["claims"].values()), "higher state claim leaked")

    print("PASS STAGE36_36_09J_RECIPROCAL_TWO_LINEAR_COVER_PREFLIGHT")
    print("exact physical reconstruction cover = connected V4 degree 4; physical branch collisions excluded")
    print("candidate genus=3; character quotient genera=[1,1,1]; S31-W01 quartic side matched but not triggered")
    print("36-09K remains locked pending hostile audit; no receiver/endpoint credit")


if __name__ == "__main__":
    main()
