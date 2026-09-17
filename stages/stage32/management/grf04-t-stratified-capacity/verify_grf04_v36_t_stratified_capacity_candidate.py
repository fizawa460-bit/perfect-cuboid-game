#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
V36 = HERE / "GRF04-V36-T-STRATIFIED-CAPACITY-LP-CANDIDATE.json"
V35_DIR = HERE.parent / "grf04-uniform-bound"
V35 = V35_DIR / "GRF04-V35-INDEPENDENT-UNIFORM-BLOCK-BOUND-CANDIDATE.json"
V35_VERIFY = V35_DIR / "verify_grf04_v35_uniform_block_bound_candidate.py"

LOCKS = {
    "v36_canonical": "d777ecd239a26dc4436bedd1e1438146139fc74b751defeffc77210e6f39a1bf",
    "v35_blob": "a203df7b15a9cc655b78aa70b849933b98404a2d",
    "v35_canonical": "221f7bc44989130de39b639d4a0a0af85a056ea0ab9461e61a1cb24be907d5b5",
    "v35_verifier_blob": "10979e2e7fb49405606c646f2f02d54cf91513b1",
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

V34 = 3360778813767800658369
V35_BOUND = 511195899564352597589
ENVELOPE = 6703403803993209250491
TOTAL_CAPACITY = 97368698704158830018099
REFINED_TYPES = 4264678
UNIQUE_RATIOS = 50827
MAX_RATIO = Fraction(5, 33)
LAMBDA = Fraction(46, 903)
CAP_GT = 6701544661867342326214
CAP_GE = 6704500123334151445174
N_GT = 7594
N_EQ = 1
DUAL = Fraction(361903153489481765536400, 903)
V36_BOUND = 400778686034863527725
IMPROVE_V35 = 110417213529489069864
IMPROVE_V34 = 2960000127732937130644


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
    data = json.loads(path.read_text())
    req(data.get("canonical_sha256_without_this_field") == canonical, f"{label} stored canonical")
    req(canon(data) == canonical, f"{label} canonical")
    return data


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def parity_count_upto(L: int, parity: int) -> int:
    if L < parity:
        return 0
    return (L - parity) // 2 + 1


def build_t_parity_prefix_caps(H: int = 96) -> dict[int, dict[tuple[int, int], int]]:
    # Refine the exact relaxed V35 canonical-prefix capacity by
    # t=2*x0+x6+x9 and the required x4 parity. No later support/square/
    # total-mass restriction is introduced here.
    pair_sum_parity = [[0, 0] for _ in range(H + 1)]
    for L in range(H + 1):
        for s in range(L + 1):
            pair_sum_parity[L][s & 1] += s + 1

    # Equal x0=x1 case, stored relative to R=h-x0 and x0 parity.
    equal = [[None, None] for _ in range(H + 1)]
    for R in range(H + 1):
        for x0par in (0, 1):
            dist: dict[tuple[int, int], int] = defaultdict(int)

            # (x5,x6) <lex (x8,x9) because x5<x8.
            for x8 in range(1, R + 1):
                L = R - x8
                for x9 in range(R + 1):
                    n_x5 = min(x8, R - x9 + 1)
                    if n_x5 <= 0:
                        continue
                    x10par = x0par ^ ((x8 + x9) & 1)
                    p4 = x9 & 1
                    for x6 in range(L + 1):
                        n_x10 = parity_count_upto(L - x6, x10par)
                        if n_x10:
                            dist[(x6 + x9, p4)] += n_x5 * n_x10

            # x5=x8=u and x6<=x9.
            for u in range(R + 1):
                for x9 in range(R - u + 1):
                    x10par = x0par ^ ((u + x9) & 1)
                    p4 = x9 & 1
                    for x6 in range(min(x9, R - u) + 1):
                        n_x10 = parity_count_upto(R - u - x6, x10par)
                        if n_x10:
                            dist[(x6 + x9, p4)] += n_x10
            equal[R][x0par] = dist

    out: dict[int, dict[tuple[int, int], int]] = {}
    for h in range(4, H + 1):
        dist: dict[tuple[int, int], int] = defaultdict(int)

        # x0<x1: canonical lex condition is automatic.
        for x0 in range(h + 1):
            for x1 in range(x0 + 1, h + 1):
                rb = h - x1
                rc = h - x0
                for x9 in range(rb + 1):
                    n_x5 = rb - x9 + 1
                    sumpar = (x1 + x9) & 1
                    p4 = (x0 + x1 + x9) & 1
                    for x6 in range(rc + 1):
                        n_x8x10 = pair_sum_parity[rc - x6][sumpar]
                        if n_x8x10:
                            dist[(2 * x0 + x9 + x6, p4)] += n_x5 * n_x8x10

        # x0=x1.
        for x0 in range(h + 1):
            R = h - x0
            for (s, p4), n in equal[R][x0 & 1].items():
                dist[(2 * x0 + s, p4)] += n

        # x2,x3,x7 are parity/t-free in the relaxed V35 capacity.
        free = math.comb(h + 3, 3)
        out[h] = {k: v * free for k, v in dist.items()}
    return out


def coarse_v35_prefix_caps(H: int = 96) -> dict[int, int]:
    # Independent aggregate replay of V35's relaxed capacity for a
    # refinement-conservation check.
    B2 = []
    C3 = []
    D2 = []
    for R in range(H + 1):
        b = [0, 0]
        for x9 in range(R + 1):
            b[x9 & 1] += R - x9 + 1
        B2.append(b)
        c = [0, 0]
        for x8 in range(R + 1):
            for x10 in range(R - x8 + 1):
                c[(x8 + x10) & 1] += R - x8 - x10 + 1
        C3.append(c)
        d = [0, 0]
        for x10 in range(R + 1):
            d[x10 & 1] += R - x10 + 1
        D2.append(d)

    eq = [[0, 0] for _ in range(H + 1)]
    for R in range(H + 1):
        first = [0, 0]
        for x5 in range(R + 1):
            for x8 in range(x5 + 1, R + 1):
                L = R - x8
                for x9 in range(R - x5 + 1):
                    p = (x8 + x9) & 1
                    first[0] += D2[L][p]
                    first[1] += D2[L][p ^ 1]
        second = [0, 0]
        for u in range(R + 1):
            for x9 in range(R - u + 1):
                p0 = (u + x9) & 1
                for x6 in range(min(x9, R - u) + 1):
                    L = R - u - x6
                    second[0] += parity_count_upto(L, p0)
                    second[1] += parity_count_upto(L, p0 ^ 1)
        eq[R][0] = first[0] + second[0]
        eq[R][1] = first[1] + second[1]

    out = {}
    for h in range(4, H + 1):
        unequal = 0
        for x0 in range(h + 1):
            for x1 in range(x0 + 1, h + 1):
                rb = h - x1
                rc = h - x0
                p = x1 & 1
                unequal += B2[rb][0] * C3[rc][p]
                unequal += B2[rb][1] * C3[rc][p ^ 1]
        equal_count = sum(eq[h - x0][x0 & 1] for x0 in range(h + 1))
        out[h] = math.comb(h + 3, 3) * (unequal + equal_count)
    return out


def coarse_block_cap(g: int, d: int) -> int:
    R = 3 * d * d + 48 * d + 96 - 96 * g
    req(R >= 0 and R % 4 == 0, f"R divisibility {(g,d)}")
    r = math.isqrt(R // 4)
    U = (d // 2 + r) // 2
    return U // 2 + 1


def refined_block_cap(g: int, d: int, t: int, p4: int, B: int) -> int:
    R = 3 * d * d + 48 * d + 96 - 96 * g
    r = math.isqrt(R // 4)
    D = d // 2 - t
    lo = max(0, ceil_div(D - r, 2))
    hi = min(B - 1, (D + r) // 2)
    if lo > hi:
        return 0
    first = lo if (lo & 1) == p4 else lo + 1
    if first > hi:
        return 0
    return (hi - first) // 2 + 1


def build_ratio_capacity(prefix: dict[int, dict[tuple[int, int], int]]):
    ratios: dict[Fraction, int] = defaultdict(int)
    total = 0
    refined_types = 0
    max_ratio = Fraction(0, 1)
    coarse_bins = 0
    for g, max_d in ((0, 176), (1, 192)):
        for d in range(8, max_d + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16 * g + 16, 4)
            lower = max(legacy, K, d - 4 * g + 4)
            if lower & 1:
                lower += 1
            cv35 = coarse_block_cap(g, d)
            for e in range(lower, 3 * d + 1, 2):
                if g == 1 and d == 8 and e == 8:
                    continue
                coarse_bins += 1
                B = 19 * d - 5 * e + 1
                req(B > 0 and B % 2 == 1, f"block size {(g,d,e)}")
                for (t, p4), nblocks in prefix[h].items():
                    refined_types += 1
                    c = refined_block_cap(g, d, t, p4, B)
                    req(c <= cv35, f"pointwise refinement exceeds V35 {(g,d,e,t,p4)}")
                    cap = nblocks * B
                    total += cap
                    if c:
                        ratio = Fraction(c, B)
                        ratios[ratio] += cap
                        if ratio > max_ratio:
                            max_ratio = ratio
    return ratios, total, coarse_bins, refined_types, max_ratio


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--td01-root", required=True)
    ap.add_argument("--grf04-root", required=True)
    ap.add_argument("--hpadj08-root", required=True)
    ap.add_argument("--td02-root", required=True)
    ns = ap.parse_args()

    req(V36.is_file(), "missing V36 candidate")
    v36 = json.loads(V36.read_text())
    req(v36.get("canonical_sha256_without_this_field") == LOCKS["v36_canonical"], "V36 stored canonical")
    req(canon(v36) == LOCKS["v36_canonical"], "V36 canonical")

    v35 = locked_json(V35, LOCKS["v35_blob"], LOCKS["v35_canonical"], "V35 candidate")
    req(git_blob(V35_VERIFY) == LOCKS["v35_verifier_blob"], "V35 verifier blob")
    req(v35["candidate_bound"]["candidate_upper_bound"] == V35_BOUND, "V35 benchmark")
    req(v35["exact_input_envelope"]["hpadj08_survivor_x4_complete_envelope_terminals"] == ENVELOPE, "V35 envelope")

    td01 = locked_json(
        Path(ns.td01_root) / "stages/stage32/32-01-178/topdown-01/EXACT-X4-ENVELOPE-BOUND.json",
        LOCKS["td01_packet_blob"], LOCKS["td01_packet_canonical"], "TD01 packet"
    )
    contract = locked_json(
        Path(ns.td01_root) / "stages/stage32/32-01-178/topdown-01/FULL178-SCALEOUT-CONTRACT.json",
        LOCKS["td01_contract_blob"], LOCKS["td01_contract_canonical"], "TD01 contract"
    )
    req(td01["exact_envelope_derivation"]["x4_complete_after_hpadj08"] is True, "TD01 x4 completeness")
    req(td01["exact_envelope_derivation"]["hpadj08_exact_square_survivor_envelope"] == ENVELOPE, "TD01 envelope total")
    req(td01["parity_bound"]["required_character"] == "x4 == x0+x8+x10 (mod 2)", "TD01 parity")
    req(contract["coverage"]["rows_total"] == 178, "TD01 FULL178 rows")

    grf04 = locked_json(
        Path(ns.grf04_root) / "stages/stage32/management/global-residual-feasibility/GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json",
        LOCKS["grf04_kernel_blob"], LOCKS["grf04_kernel_canonical"], "GRF04 kernel"
    )
    req(grf04["mathematical_kernel"]["minimum"] == "rho=b0^T*S^{-1}*b0", "GRF04 symbolic kernel")

    hp_root = Path(ns.hpadj08_root)
    worker = hp_root / "stages/stage32-ex5/hpadj-08_ex5/hpadj08_ex5_full178_b_shard.py"
    family = hp_root / "stages/stage32/residual-32-01-production/compressed_terminal_family.py"
    req(git_blob(worker) == LOCKS["hpadj08_worker_blob"], "HPADJ08 worker blob")
    req(git_blob(family) == LOCKS["compressed_family_blob"], "compressed family blob")
    wt = worker.read_text()
    ft = family.read_text()
    for snippet in (
        "for g,dmax in ((0,176),(1,192))",
        "lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))",
        "upper=min((19*d)//5,3*d,3*d-(b-c))",
        "if g==1 and d==8: excluded.add(8)",
    ):
        req(snippet in wt, "HPADJ08 domain source drift: " + snippet)
    for snippet in (
        "x0 <= x1",
        "(x5,x6) <=lex (x8,x9)",
        "x1 + x8 + x9 + x10 == 0 (mod 2)",
        "The sole normal variable x4 is independent and lies in 0..19*d-5*e.",
    ):
        req(snippet in ft, "compressed-family source drift: " + snippet)

    td02 = Path(ns.td02_root) / "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bounded.py"
    req(git_blob(td02) == LOCKS["td02_bounded_blob"], "TD02 source blob")
    tdt = td02.read_text()
    req("24*q + 4*(d/2 - t - 2*x4)^2 <= 3*d^2+48*d+96-96*g." in tdt, "TD02 GRF04 formula")
    req("t = 2*x0 + x6 + x9" in tdt, "TD02 t formula")

    prefix = build_t_parity_prefix_caps()
    coarse = coarse_v35_prefix_caps()
    req(coarse[4] == 24010 and coarse[96] == 27398914615401945, "V35 prefix fixtures")
    for h in range(4, 97):
        req(sum(prefix[h].values()) == coarse[h], f"t/parity partition conservation h={h}")

    ratios, total, coarse_bins, refined_types, max_ratio = build_ratio_capacity(prefix)
    req(coarse_bins == 17127, "coarse bin coverage")
    req(refined_types == REFINED_TYPES, "refined type count")
    req(total == TOTAL_CAPACITY, "total relaxed capacity")
    req(len(ratios) == UNIQUE_RATIOS, "unique ratio count")
    req(max_ratio == MAX_RATIO, "maximum refined ratio")

    cap_gt = sum(cap for r, cap in ratios.items() if r > LAMBDA)
    cap_ge = sum(cap for r, cap in ratios.items() if r >= LAMBDA)
    n_gt = sum(1 for r in ratios if r > LAMBDA)
    n_eq = sum(1 for r in ratios if r == LAMBDA)
    req(cap_gt == CAP_GT and cap_ge == CAP_GE, "threshold capacities")
    req(n_gt == N_GT and n_eq == N_EQ, "threshold ratio-group counts")
    req(cap_gt < ENVELOPE <= cap_ge, "threshold brackets envelope")

    correction = sum((r - LAMBDA) * cap for r, cap in ratios.items() if r > LAMBDA)
    dual = LAMBDA * ENVELOPE + correction
    req(dual == DUAL, "exact dual")
    upper = dual.numerator // dual.denominator
    req(upper == V36_BOUND and dual.numerator % dual.denominator == 725, "V36 floor")
    req(V35_BOUND - upper == IMPROVE_V35, "V35 improvement")
    req(V34 - upper == IMPROVE_V34, "V34 improvement")

    cb = v36["candidate_bound"]
    cert = v36["capacity_lp_certificate"]
    ref = v36["refinement"]
    req(cb["v36_candidate_upper_bound"] == V36_BOUND, "candidate bound JSON")
    req(cb["improvement_vs_v35_candidate"] == IMPROVE_V35, "candidate V35 improvement JSON")
    req(cb["improvement_vs_current_audited_v34"] == IMPROVE_V34, "candidate V34 improvement JSON")
    req(cert["dual_threshold"] == "46/903", "candidate threshold JSON")
    req(cert["capacity_strictly_above_threshold"] == CAP_GT, "candidate cap gt JSON")
    req(cert["capacity_at_or_above_threshold"] == CAP_GE, "candidate cap ge JSON")
    req(ref["refined_gde_t_parity_types"] == REFINED_TYPES, "candidate refined count JSON")
    req(ref["maximum_refined_block_ratio"] == "5/33", "candidate max ratio JSON")
    req(v36["authority"]["authority_mutated"] is False and v36["authority"]["main_credit_granted"] is False, "authority firewall")
    req(v36["semantics"]["statistical_independence_assumed"] is False, "independence firewall")
    req(v36["firewalls"]["full178_complete"] is False and v36["firewalls"]["merge_authorized"] is False, "closure firewall")

    print("PASS: V36 t/parity-stratified GRF04 capacity refines V35 without capacity loss")
    print(f"PASS: refined_types={refined_types} total_capacity={total} max_ratio={max_ratio}")
    print(f"PASS: lambda={LAMBDA} cap_gt={cap_gt} cap_ge={cap_ge}")
    print(f"PASS: candidate={upper} improvement_vs_V35={IMPROVE_V35}")
    print("PASS: V34 authority unchanged; hostile audit required before any promotion")


if __name__ == "__main__":
    main()
