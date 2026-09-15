#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIDATE = HERE / "GRF04-V35-INDEPENDENT-UNIFORM-BLOCK-BOUND-CANDIDATE.json"

LOCKS = {
    "candidate_blob": "a203df7b15a9cc655b78aa70b849933b98404a2d",
    "candidate_canonical": "221f7bc44989130de39b639d4a0a0af85a056ea0ab9461e61a1cb24be907d5b5",
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

V34_BOUND = 3360778813767800658369
ENVELOPE = 6703403803993209250491
EXPECTED_CANDIDATE = 511195899564352597589
EXPECTED_TIGHTENING = 2849582914203448060780
EXPECTED_CAP_GT = 6701827613531965854955
EXPECTED_CAP_GE = 6721545322878350699380
EXPECTED_DUAL = Fraction(7667938493465288963846, 15)
LAMBDA = Fraction(1, 15)

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

def canonical_prefix_caps(H: int = 96) -> dict[int, int]:
    # Count only the source-locked h-caps + canonical ordering + terminal parity.
    # Omitting all further support, total-sum, N358 and HPADJ08-square restrictions
    # makes this an upper envelope, never an undercount.
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

    equal = [[0, 0] for _ in range(H + 1)]
    for R in range(H + 1):
        lex_first = [0, 0]
        for x5 in range(R + 1):
            for x8 in range(x5 + 1, R + 1):
                L = R - x8
                for x9 in range(R - x5 + 1):
                    p = (x8 + x9) & 1
                    lex_first[0] += D2[L][p]
                    lex_first[1] += D2[L][p ^ 1]

        lex_second = [0, 0]
        for u in range(R + 1):
            for x9 in range(R - u + 1):
                max_x6 = min(x9, R - u)
                p0 = (u + x9) & 1
                for x6 in range(max_x6 + 1):
                    L = R - u - x6
                    n0 = (L - p0) // 2 + 1 if L >= p0 else 0
                    p1 = p0 ^ 1
                    n1 = (L - p1) // 2 + 1 if L >= p1 else 0
                    lex_second[0] += n0
                    lex_second[1] += n1

        equal[R][0] = lex_first[0] + lex_second[0]
        equal[R][1] = lex_first[1] + lex_second[1]

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
        eq = sum(equal[h - t][t & 1] for t in range(h + 1))
        a_count = math.comb(h + 3, 3)
        out[h] = a_count * (unequal + eq)

    req(out[4] == 24010, "h=4 canonical-prefix fixture")
    req(out[96] == 27398914615401945, "h=96 canonical-prefix fixture")
    return out

def block_survivor_count(g: int, d: int) -> int:
    R = 3*d*d + 48*d + 96 - 96*g
    req(R >= 0 and R % 4 == 0, f"R divisibility {(g,d)}")
    r = math.isqrt(R // 4)
    U = (d // 2 + r) // 2
    return U // 2 + 1

def build_bins(caps: dict[int, int]):
    bins = []
    for g, max_d in ((0, 176), (1, 192)):
        for d in range(8, max_d + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16*g + 16, 4)
            lower = max(legacy, K, d - 4*g + 4)
            if lower & 1:
                lower += 1
            c = block_survivor_count(g, d)
            for e in range(lower, 3*d + 1, 2):
                if g == 1 and d == 8 and e == 8:
                    continue
                B = 19*d - 5*e + 1
                req(B > 0, f"normal block {(g,d,e)}")
                capacity = caps[h] * B
                ratio = Fraction(c, B)
                bins.append((ratio, capacity, g, d, e, c, B))
    req(len(bins) == 17127, "coarse (g,d,e) bin coverage")
    return bins

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

    v34 = locked_json(
        Path(ns.v34_root) / "stages/stage32/MAIN-STATE.json",
        LOCKS["v34_state_blob"], LOCKS["v34_state_canonical"], "V34 state"
    )
    req(v34["current_exact_frontier"]["authoritative_remaining_terminals"] == V34_BOUND, "V34 authority")
    req(v34["current_exact_frontier"]["authoritative_remaining_strata"] == 17128, "V34 strata")

    td01 = locked_json(
        Path(ns.td01_root) / "stages/stage32/32-01-178/topdown-01/EXACT-X4-ENVELOPE-BOUND.json",
        LOCKS["td01_packet_blob"], LOCKS["td01_packet_canonical"], "TD01 envelope"
    )
    contract = locked_json(
        Path(ns.td01_root) / "stages/stage32/32-01-178/topdown-01/FULL178-SCALEOUT-CONTRACT.json",
        LOCKS["td01_contract_blob"], LOCKS["td01_contract_canonical"], "TD01 contract"
    )
    req(td01["exact_envelope_derivation"]["x4_complete_after_hpadj08"] is True, "x4 complete")
    req(td01["exact_envelope_derivation"]["hpadj08_exact_square_survivor_envelope"] == ENVELOPE, "envelope total")
    req(td01["parity_bound"]["required_character"] == "x4 == x0+x8+x10 (mod 2)", "completion parity")
    req(contract["coverage"]["rows_total"] == 178, "FULL178 rows")

    grf04 = locked_json(
        Path(ns.grf04_root) / "stages/stage32/management/global-residual-feasibility/GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json",
        LOCKS["grf04_kernel_blob"], LOCKS["grf04_kernel_canonical"], "GRF04 kernel"
    )
    req(grf04["mathematical_kernel"]["minimum"] == "rho=b0^T*S^{-1}*b0", "GRF04 kernel formula")

    hp_root = Path(ns.hpadj08_root)
    hp_worker = hp_root / "stages/stage32-ex5/hpadj-08_ex5/hpadj08_ex5_full178_b_shard.py"
    compressed = hp_root / "stages/stage32/residual-32-01-production/compressed_terminal_family.py"
    req(git_blob(hp_worker) == LOCKS["hpadj08_worker_blob"], "HPADJ08 worker blob")
    req(git_blob(compressed) == LOCKS["compressed_family_blob"], "compressed family blob")
    wt = hp_worker.read_text()
    ct = compressed.read_text()
    for snippet in (
        "for g,dmax in ((0,176),(1,192))",
        "h=d//2; legacy=8 if g==0 else 4; K=ceil_div(d-16*g+16,4)",
        "lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))",
        "upper=min((19*d)//5,3*d,3*d-(b-c))",
        "if g==1 and d==8: excluded.add(8)",
    ):
        req(snippet in wt, "HPADJ08 domain source drift: " + snippet)
    for snippet in (
        "x0 <= x1",
        "(x5,x6) <=lex (x8,x9)",
        "x1 + x8 + x9 + x10 == 0 (mod 2)",
        "x1 + x5 + x9",
        "x0 + x8 + x6 + x10",
    ):
        req(snippet in ct, "compressed canonical source drift: " + snippet)

    td02 = Path(ns.td02_root) / "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bounded.py"
    req(git_blob(td02) == LOCKS["td02_bounded_blob"], "TD02 source blob")
    text = td02.read_text()
    req("24*q + 4*(d/2 - t - 2*x4)^2 <= 3*d^2+48*d+96-96*g." in text, "concrete GRF04 formula")
    req("t = 2*x0 + x6 + x9" in text, "nonnegative t source")

    caps = canonical_prefix_caps()
    bins = build_bins(caps)
    cap_gt = sum(cap for ratio, cap, *_ in bins if ratio > LAMBDA)
    cap_ge = sum(cap for ratio, cap, *_ in bins if ratio >= LAMBDA)
    n_gt = sum(1 for ratio, *_ in bins if ratio > LAMBDA)
    n_eq = sum(1 for ratio, *_ in bins if ratio == LAMBDA)
    req(cap_gt == EXPECTED_CAP_GT and cap_ge == EXPECTED_CAP_GE, "threshold capacities")
    req(n_gt == 2566 and n_eq == 17, "threshold bin counts")
    req(cap_gt < ENVELOPE <= cap_ge, "threshold brackets envelope")

    correction = sum(
        (ratio - LAMBDA) * cap
        for ratio, cap, *_ in bins
        if ratio > LAMBDA
    )
    dual = LAMBDA * ENVELOPE + correction
    req(dual == EXPECTED_DUAL, "exact LP dual value")
    upper = dual.numerator // dual.denominator
    req(upper == EXPECTED_CANDIDATE, "integer LP bound")
    req(V34_BOUND - upper == EXPECTED_TIGHTENING, "tightening arithmetic")

    cb = candidate["candidate_bound"]
    cert = candidate["capacity_lp_certificate"]
    req(cb["candidate_upper_bound"] == EXPECTED_CANDIDATE, "candidate JSON bound")
    req(cb["candidate_tightening_vs_v34"] == EXPECTED_TIGHTENING, "candidate JSON tightening")
    req(cert["capacity_strictly_above_threshold"] == EXPECTED_CAP_GT, "candidate cap gt")
    req(cert["capacity_at_or_above_threshold"] == EXPECTED_CAP_GE, "candidate cap ge")
    req(cert["exact_dual_value_numerator"] == EXPECTED_DUAL.numerator and cert["exact_dual_value_denominator"] == EXPECTED_DUAL.denominator, "candidate dual")
    pg = candidate["promotion_gate"]
    req(pg["hostile_audit_required"] is True and pg["main_authority_mutated"] is False and pg["main_credit_granted"] is False, "promotion firewall")
    req(pg["additive_subtraction_authorized"] is False and pg["exact_incremental_rejected_identity_set_claimed"] is False, "no additive credit")
    req(candidate["firewalls"]["full178_complete"] is False and candidate["firewalls"]["merge_authorized"] is False, "closure firewall")

    print("PASS: exact nonheavy canonical-capacity LP certificate")
    print(f"PASS: envelope={ENVELOPE} lambda=1/15 cap_gt={cap_gt} cap_ge={cap_ge}")
    print(f"PASS: candidate={upper} tightening_vs_V34={EXPECTED_TIGHTENING}")
    print("PASS: V34 authority unchanged; hostile audit required before promotion")

if __name__ == "__main__":
    main()
