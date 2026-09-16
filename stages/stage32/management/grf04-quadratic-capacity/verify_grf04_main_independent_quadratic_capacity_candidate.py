#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIDATE = HERE / "GRF04-MAIN-INDEPENDENT-QUADRATIC-CAPACITY-LP-CANDIDATE.json"

LOCKS = {
    "candidate_blob": "1d669114e930951b9d5f9f82a6abb2b59cd43884",
    "candidate_canonical": "3fca63c0d678eb2de2147848a1aa29839618cfd9cb65bdd27d671b28c6e44b01",
    "v34_state_blob": "ec0243cb998c5c58340100d8151559516c474193",
    "v34_state_canonical": "25e68a40148ce1ca4bb893ef47d23a0e213898aca8be3a76f497252cb2adc2eb",
    "td01_packet_blob": "51271c11078459ad9171138c4fb6121d7a665c39",
    "td01_packet_canonical": "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d",
    "td01_contract_blob": "ca1b195a3ee8e786707e1ef50b404ee8c19f1429",
    "td01_contract_canonical": "02a350a4c4c9b5c999767386be499edfa4e635189ff8f0e37db0bece7a00f660",
    "grf04_kernel_blob": "f7c1073edbf895f498fd9923e59eedf5a4e981c8",
    "grf04_kernel_canonical": "70e6ecdf4c79ee51e843aea043a34e3deb4ad913822537e973be82d2c961114c",
    "hpadj08_worker_blob": "c5fc340ea734dfc54436f124bb302c1ec6c5677c",
    "compressed_family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "td02_bounded_blob": "8dc7b6255b31a79aa7f51141f1ac5a5b8137efc0",
}

V34_BOUND = 3_360_778_813_767_800_658_369
ENVELOPE = 6_703_403_803_993_209_250_491
LAMBDA_NUM = 29
LAMBDA_DEN = 1357
EXPECTED_CAP_GT = 6_703_020_190_175_287_654_201
EXPECTED_CAP_GE = 6_704_031_906_137_426_835_471
EXPECTED_GT_BINS = 427_750
EXPECTED_EQ_BINS = 17
EXPECTED_DUAL_NUM = 265_434_151_794_158_295_629_351
EXPECTED_DUAL_DEN = 1357
EXPECTED_UPPER = 195_603_649_074_545_538_415
EXPECTED_REMAINDER = 196
EXPECTED_TIGHTENING = 3_165_175_164_693_255_119_954
HMAX = 96


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def locked_json(path: Path, blob: str, canonical: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(git_blob(path) == blob, f"{label} blob drift")
    value = json.loads(path.read_text())
    req(value.get("canonical_sha256_without_this_field") == canonical, f"{label} stored canonical drift")
    req(canon(value) == canonical, f"{label} canonical drift")
    return value


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def count_parity_upto(limit: int, parity: int) -> int:
    if limit < parity:
        return 0
    return (limit - parity) // 2 + 1


def build_bc_counts() -> list[list[int]]:
    """Exact relaxed canonical/parity prefix counts keyed by (b,c)."""
    B = [[0, 0] for _ in range(HMAX + 1)]
    C = [[0, 0] for _ in range(HMAX + 1)]
    for m in range(HMAX + 1):
        for x9 in range(m + 1):
            B[m][x9 & 1] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                C[m][(x8 + x10) & 1] += 1

    pb = [[0] * (HMAX + 1) for _ in range(2)]
    for p in (0, 1):
        total = 0
        for m in range(HMAX + 1):
            total += B[m][p]
            pb[p][m] = total

    def sum_b(p: int, lo: int, hi: int) -> int:
        if lo > hi:
            return 0
        return pb[p][hi] - (pb[p][lo - 1] if lo else 0)

    eq_first = [[[0] * (HMAX + 1) for _ in range(HMAX + 1)] for __ in range(2)]
    eq_second = [[[0] * (HMAX + 1) for _ in range(HMAX + 1)] for __ in range(2)]
    for tp in (0, 1):
        for rb in range(HMAX + 1):
            for rc in range(HMAX + 1):
                total = 0
                for delta in range(1, rc + 1):
                    last_x5 = min(rb, rc - delta)
                    p = (tp + rb + delta) & 1
                    top = rc - delta
                    total += sum_b(p, top - last_x5, top)
                eq_first[tp][rb][rc] = total

                need_x10 = (tp + rb) & 1
                total = 0
                for u in range(min(rb, rc) + 1):
                    x9 = rb - u
                    rem = rc - u
                    limit_x6 = min(x9, rem)
                    need_x6 = (rem - need_x10) & 1
                    total += count_parity_upto(limit_x6, need_x6)
                eq_second[tp][rb][rc] = total

    bc = [[0] * (HMAX + 1) for _ in range(HMAX + 1)]
    for x0 in range(HMAX + 1):
        for x1 in range(x0 + 1, HMAX + 1):
            px1 = x1 & 1
            for b in range(x1, HMAX + 1):
                g2 = b - x1
                b0, b1 = B[g2]
                for c in range(x0, HMAX + 1):
                    c0, c1 = C[c - x0]
                    bc[b][c] += b0 * (c1 if px1 else c0) + b1 * (c0 if px1 else c1)

    for t in range(HMAX + 1):
        tp = t & 1
        for b in range(t, HMAX + 1):
            rb = b - t
            for c in range(t, HMAX + 1):
                rc = c - t
                bc[b][c] += eq_first[tp][rb][rc] + eq_second[tp][rb][rc]
    return bc


def f0(h: int, g: int, b: int, c: int, x4: int) -> int:
    D = h - 2 * x4
    d = 2 * h
    r4 = (3 * d * d + 48 * d + 96 - 96 * g) // 4
    return 3 * (
        6 * D * D - 8 * D * b - 6 * D * c + 18 * b * b + 4 * b * c + 13 * c * c
    ) - 23 * r4


def a0_interval(h: int, g: int, b: int, c: int) -> tuple[int, int] | None:
    n_min = 8 * h
    linear = -72 * h + 48 * b + 36 * c
    vertex = max(0, min(n_min, (-linear) // 144))
    best = vertex
    for z in (vertex - 1, vertex + 1):
        if 0 <= z <= n_min and f0(h, g, b, c, z) < f0(h, g, b, c, best):
            best = z
    if f0(h, g, b, c, best) > 0:
        return None

    if f0(h, g, b, c, 0) <= 0:
        left = 0
    else:
        lo, hi = 0, best
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if f0(h, g, b, c, mid) <= 0:
                hi = mid
            else:
                lo = mid
        left = hi

    req(f0(h, g, b, c, n_min) > 0, f"quadratic interval reaches N_min {(g,2*h,b,c)}")
    lo, hi = best, n_min
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if f0(h, g, b, c, mid) <= 0:
            lo = mid
        else:
            hi = mid
    return left, lo


def replay_capacity_lp() -> dict[str, int]:
    bc = build_bc_counts()

    def prefix_total(h: int) -> int:
        acount = sum((a + 1) * (a + 2) // 2 for a in range(h + 1))
        bccount = sum(bc[b][c] for b in range(h + 1) for c in range(h + 1))
        return acount * bccount

    req(prefix_total(4) == 24_010, "h=4 canonical-prefix fixture")
    req(prefix_total(96) == 27_398_914_615_401_945, "h=96 canonical-prefix fixture")

    cap_gt = cap_ge = correction_num = bins_gt = bins_eq = 0
    for g, hmax in ((0, 88), (1, 96)):
        for h in range(4, hmax + 1):
            d = 2 * h
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16 * g + 16, 4)
            e_lower = max(legacy, K, d - 4 * g + 4)
            if e_lower & 1:
                e_lower += 1
            e_upper = 3 * d

            hist = [[0] * (3 * h + 1) for _ in range(h + 2)]
            for b in range(h + 1):
                for c in range(h + 1):
                    bc_count = bc[b][c]
                    if not bc_count:
                        continue
                    interval = a0_interval(h, g, b, c)
                    if interval is None:
                        continue
                    left, right = interval
                    diff = [0] * (h + 2)
                    for x4 in range(left, right + 1):
                        room = -f0(h, g, b, c, x4)
                        req(room >= 0, "interval construction regression")
                        amax = min(h, math.isqrt(room // 46))
                        diff[0] += 1
                        diff[amax + 1] -= 1

                    raw = 0
                    for a in range(h + 1):
                        raw += diff[a]
                        if raw <= 0:
                            break
                        survivor_cap = (raw + 1) // 2
                        req(survivor_cap < len(hist), "survivor histogram overflow")
                        a_count = (a + 1) * (a + 2) // 2
                        hist[survivor_cap][a + b + c] += a_count * bc_count

            for s in range(1, len(hist)):
                row = hist[s]
                if not any(row):
                    continue
                prefix = []
                acc = 0
                for value in row:
                    acc += value
                    prefix.append(acc)
                for e in range(e_lower, e_upper + 1, 2):
                    if g == 1 and d == 8 and e == 8:
                        continue
                    weight = prefix[min(e, 3 * h)]
                    if not weight:
                        continue
                    B = 19 * d - 5 * e + 1
                    req(B > 0, f"normal block {(g,d,e)}")
                    cmp = LAMBDA_DEN * s - LAMBDA_NUM * B
                    capacity = weight * B
                    if cmp > 0:
                        bins_gt += 1
                        cap_gt += capacity
                        cap_ge += capacity
                        correction_num += weight * cmp
                    elif cmp == 0:
                        bins_eq += 1
                        cap_ge += capacity

    dual_num = LAMBDA_NUM * ENVELOPE + correction_num
    return {
        "bins_gt": bins_gt,
        "bins_eq": bins_eq,
        "cap_gt": cap_gt,
        "cap_ge": cap_ge,
        "dual_num": dual_num,
        "dual_den": LAMBDA_DEN,
        "upper": dual_num // LAMBDA_DEN,
        "remainder": dual_num % LAMBDA_DEN,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v34-root", required=True)
    ap.add_argument("--td01-root", required=True)
    ap.add_argument("--grf04-root", required=True)
    ap.add_argument("--hpadj08-root", required=True)
    ap.add_argument("--td02-root", required=True)
    ns = ap.parse_args()

    req(git_blob(CANDIDATE) == LOCKS["candidate_blob"], "candidate blob")
    candidate = json.loads(CANDIDATE.read_text())
    req(candidate.get("canonical_sha256_without_this_field") == LOCKS["candidate_canonical"], "candidate stored canonical")
    req(canon(candidate) == LOCKS["candidate_canonical"], "candidate canonical")

    v34 = locked_json(Path(ns.v34_root) / "stages/stage32/MAIN-STATE.json", LOCKS["v34_state_blob"], LOCKS["v34_state_canonical"], "V34 state")
    req(v34["current_exact_frontier"]["authoritative_remaining_terminals"] == V34_BOUND, "V34 authority")
    req(v34["current_exact_frontier"]["authoritative_remaining_strata"] == 17_128, "V34 strata")

    td01 = locked_json(Path(ns.td01_root) / "stages/stage32/32-01-178/topdown-01/EXACT-X4-ENVELOPE-BOUND.json", LOCKS["td01_packet_blob"], LOCKS["td01_packet_canonical"], "TD01 envelope")
    contract = locked_json(Path(ns.td01_root) / "stages/stage32/32-01-178/topdown-01/FULL178-SCALEOUT-CONTRACT.json", LOCKS["td01_contract_blob"], LOCKS["td01_contract_canonical"], "TD01 contract")
    deriv = td01["exact_envelope_derivation"]
    req(deriv["x4_complete_after_hpadj08"] is True, "x4-complete envelope")
    req(deriv["hpadj08_exact_square_survivor_envelope"] == ENVELOPE, "envelope total")
    req("whole exceptional-prefix x4 blocks" in deriv["reason"], "x4 block semantics")
    req(td01["parity_bound"]["required_character"] == "x4 == x0+x8+x10 (mod 2)", "completion parity")
    req(contract["coverage"]["rows_total"] == 178, "FULL178 rows")

    grf04 = locked_json(Path(ns.grf04_root) / "stages/stage32/management/global-residual-feasibility/GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json", LOCKS["grf04_kernel_blob"], LOCKS["grf04_kernel_canonical"], "GRF04 kernel")
    req(grf04["mathematical_kernel"]["minimum"] == "rho=b0^T*S^{-1}*b0", "GRF04 symbolic kernel")

    hp_root = Path(ns.hpadj08_root)
    hp_worker = hp_root / "stages/stage32-ex5/hpadj-08_ex5/hpadj08_ex5_full178_b_shard.py"
    compressed = hp_root / "stages/stage32/residual-32-01-production/compressed_terminal_family.py"
    req(git_blob(hp_worker) == LOCKS["hpadj08_worker_blob"], "HPADJ08 worker blob")
    req(git_blob(compressed) == LOCKS["compressed_family_blob"], "compressed family blob")
    wt = hp_worker.read_text()
    ct = compressed.read_text()
    for snippet in ("for g,dmax in ((0,176),(1,192))", "h=d//2; legacy=8 if g==0 else 4; K=ceil_div(d-16*g+16,4)", "lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))", "upper=min((19*d)//5,3*d,3*d-(b-c))", "if g==1 and d==8: excluded.add(8)", "g2=b-x1", "g3=c-x0", "b=t+x5+x9", "c=t+x8+m", "b=t+u+x9", "c=t+u+x6+x10"):
        req(snippet in wt, "HPADJ08 source drift: " + snippet)
    for snippet in ("x0 <= x1", "(x5,x6) <=lex (x8,x9)", "x1 + x8 + x9 + x10 == 0 (mod 2)"):
        req(snippet in ct, "compressed canonical source drift: " + snippet)

    td02 = Path(ns.td02_root) / "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bounded.py"
    req(git_blob(td02) == LOCKS["td02_bounded_blob"], "TD02 source blob")
    td02_text = td02.read_text()
    req("24*q + 4*(d/2 - t - 2*x4)^2 <= 3*d^2+48*d+96-96*g." in td02_text, "concrete GRF04 formula")
    req("t = 2*x0 + x6 + x9" in td02_text, "TD02 t identity")

    ql = candidate["quadratic_lower_bound"]
    req(ql["qA_bound"] == "x2^2+x3^2+x7^2 >= a^2/3", "qA bound metadata")
    req(ql["difference_form_spd"] == "leading_minor=15>0, determinant=69>0", "quadratic SPD certificate")
    req("46*a^2" in ql["necessary_integer_inequality"], "quadratic inequality metadata")
    req("can only lower the left side" in ql["relaxation_direction"], "relaxation direction metadata")

    replay = replay_capacity_lp()
    req(replay["bins_gt"] == EXPECTED_GT_BINS, "strict-threshold aggregate bin count")
    req(replay["bins_eq"] == EXPECTED_EQ_BINS, "equal-threshold aggregate bin count")
    req(replay["cap_gt"] == EXPECTED_CAP_GT, "capacity strictly above threshold")
    req(replay["cap_ge"] == EXPECTED_CAP_GE, "capacity at/above threshold")
    req(EXPECTED_CAP_GT < ENVELOPE <= EXPECTED_CAP_GE, "threshold brackets exact envelope")
    req(replay["dual_num"] == EXPECTED_DUAL_NUM and replay["dual_den"] == EXPECTED_DUAL_DEN, "exact LP dual")
    req(replay["upper"] == EXPECTED_UPPER, "integer survivor upper bound")
    req(replay["remainder"] == EXPECTED_REMAINDER, "dual floor remainder")
    req(V34_BOUND - EXPECTED_UPPER == EXPECTED_TIGHTENING, "V34 tightening arithmetic")

    cert = candidate["capacity_lp_certificate"]
    req(cert["strictly_above_threshold_bin_count"] == EXPECTED_GT_BINS, "candidate >threshold bins")
    req(cert["equal_threshold_bin_count"] == EXPECTED_EQ_BINS, "candidate =threshold bins")
    req(cert["capacity_strictly_above_threshold"] == EXPECTED_CAP_GT, "candidate cap_gt")
    req(cert["capacity_at_or_above_threshold"] == EXPECTED_CAP_GE, "candidate cap_ge")
    req(cert["exact_dual_value_numerator"] == EXPECTED_DUAL_NUM, "candidate dual numerator")
    req(cert["exact_dual_value_denominator"] == EXPECTED_DUAL_DEN, "candidate dual denominator")
    cb = candidate["candidate_bound"]
    req(cb["candidate_upper_bound"] == EXPECTED_UPPER, "candidate upper bound")
    req(cb["candidate_tightening_vs_v34"] == EXPECTED_TIGHTENING, "candidate tightening")
    req(cb["composition_if_audited"] == "MIN_OF_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "composition firewall")

    pg = candidate["promotion_gate"]
    req(pg["candidate_is_current_authority"] is False, "candidate must remain non-authority")
    req(pg["main_authority_mutated"] is False and pg["main_credit_granted"] is False, "MAIN credit firewall")
    req(pg["hostile_audit_required"] is True, "hostile audit gate")
    fw = candidate["firewalls"]
    req(not any(fw.values()), "all candidate firewalls must remain false")

    print(json.dumps({"status":"SUCCESS","candidate_upper_bound":EXPECTED_UPPER,"tightening_vs_v34":EXPECTED_TIGHTENING,"threshold":f"{LAMBDA_NUM}/{LAMBDA_DEN}","capacity_strictly_above_threshold":replay["cap_gt"],"capacity_at_or_above_threshold":replay["cap_ge"],"strictly_above_threshold_bin_count":replay["bins_gt"],"equal_threshold_bin_count":replay["bins_eq"],"dual_numerator":replay["dual_num"],"dual_denominator":replay["dual_den"],"dual_floor_remainder":replay["remainder"],"main_authority_changed":False,"hostile_audit_required":True}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
