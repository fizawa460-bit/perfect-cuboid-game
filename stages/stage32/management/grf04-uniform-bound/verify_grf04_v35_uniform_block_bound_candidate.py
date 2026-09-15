#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CANDIDATE = HERE / "GRF04-V35-INDEPENDENT-UNIFORM-BLOCK-BOUND-CANDIDATE.json"

LOCKS = {
    "candidate_canonical": "aa60c5710f86891628420389b0aa5a7f12675264287bd18742e7e9255b2841e6",
    "v34_state_blob": "ec0243cb998c5c58340100d8151559516c474193",
    "v34_state_canonical": "25e68a40148ce1ca4bb893ef47d23a0e213898aca8be3a76f497252cb2adc2eb",
    "td01_packet_blob": "51271c11078459ad9171138c4fb6121d7a665c39",
    "td01_packet_canonical": "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d",
    "td01_contract_blob": "ca1b195a3ee8e786707e1ef50b404ee8c19f1429",
    "td01_contract_canonical": "02a350a4c4c9b5c999767386be499edfa4e635189ff8f0e37db0bece7a00f660",
    "grf04_kernel_blob": "f7c1073edbf895f498fd9923e59eedf5a4e981c8",
    "grf04_kernel_canonical": "70e6ecdf4c79ee51e843aea043a34e3deb4ad913822537e973be82d2c961114c",
    "grf04_verifier_blob": "af883bd66600c626350f9e6ef4bc12c00e239f45",
    "td02_probe_blob": "ed96731709b7425a2a1a4c8f1fcbc79c52bd22b2",
    "td02_bounded_blob": "8dc7b6255b31a79aa7f51141f1ac5a5b8137efc0",
}

V34_BOUND = 3360778813767800658369
ENVELOPE = 6703403803993209250491
EXPECTED_CANDIDATE = 2640734831876112735041
EXPECTED_TIGHTENING = 720043981891687923328


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
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == blob, f"{label} blob drift")
    value = json.loads(path.read_text())
    req(value.get("canonical_sha256_without_this_field") == canonical, f"{label} stored canonical drift")
    req(canon(value) == canonical, f"{label} canonical drift")
    return value


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v34-root", required=True)
    ap.add_argument("--td01-root", required=True)
    ap.add_argument("--grf04-root", required=True)
    ap.add_argument("--td02-root", required=True)
    args = ap.parse_args()

    v34_root = Path(args.v34_root)
    td01_root = Path(args.td01_root)
    grf04_root = Path(args.grf04_root)
    td02_root = Path(args.td02_root)

    candidate = json.loads(CANDIDATE.read_text())
    req(candidate.get("canonical_sha256_without_this_field") == LOCKS["candidate_canonical"], "candidate stored canonical")
    req(canon(candidate) == LOCKS["candidate_canonical"], "candidate canonical")

    v34 = locked_json(
        v34_root / "stages/stage32/MAIN-STATE.json",
        LOCKS["v34_state_blob"], LOCKS["v34_state_canonical"], "V34 MAIN state"
    )
    req(v34["current_exact_frontier"]["authoritative_remaining_strata"] == 17128, "V34 strata")
    req(v34["current_exact_frontier"]["authoritative_remaining_terminals"] == V34_BOUND, "V34 bound")
    req(v34["firewalls"]["full178_complete"] is False and v34["firewalls"]["merge_authorized"] is False, "V34 firewalls")

    packet = locked_json(
        td01_root / "stages/stage32/32-01-178/topdown-01/EXACT-X4-ENVELOPE-BOUND.json",
        LOCKS["td01_packet_blob"], LOCKS["td01_packet_canonical"], "audited TD01 envelope"
    )
    contract = locked_json(
        td01_root / "stages/stage32/32-01-178/topdown-01/FULL178-SCALEOUT-CONTRACT.json",
        LOCKS["td01_contract_blob"], LOCKS["td01_contract_canonical"], "TD01 FULL178 contract"
    )
    deriv = packet["exact_envelope_derivation"]
    pbound = packet["parity_bound"]
    req(deriv["x4_complete_after_hpadj08"] is True, "TD01 x4-complete envelope")
    req(deriv["hpadj08_exact_square_survivor_envelope"] == ENVELOPE, "TD01 envelope total")
    req(pbound["domain_facts"] == ["d,e even", "d>=8", "e<=3*d"], "TD01 domain facts")
    req(pbound["normal_budget"] == "N=19*d-5*e", "normal budget")
    cov = contract["coverage"]
    req(cov["rows_total"] == 178 and cov["g0_d_even"] == [8, 176] and cov["g1_d_even"] == [8, 192], "FULL178 coverage")

    grf04_kernel = locked_json(
        grf04_root / "stages/stage32/management/global-residual-feasibility/GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json",
        LOCKS["grf04_kernel_blob"], LOCKS["grf04_kernel_canonical"], "audited MAIN GRF04 kernel"
    )
    grf04_verifier = grf04_root / "stages/stage32/management/global-residual-feasibility/verify_grf04_rational_quadratic_lower_bound_kernel.py"
    req(grf04_verifier.is_file() and git_blob(grf04_verifier) == LOCKS["grf04_verifier_blob"], "GRF04 symbolic verifier")
    mk = grf04_kernel["mathematical_kernel"]
    req("rho=b0^T*S^{-1}*b0" == mk["minimum"], "GRF04 minimum formula")
    req(mk["emptiness_rule"].startswith("If rho>B_g(d)"), "GRF04 strict lower-bound rule")

    td02_probe = td02_root / "stages/stage32/32-01-178/topdown-02/probe_td02_grf04_hperp.py"
    td02_bounded = td02_root / "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bounded.py"
    req(td02_probe.is_file() and git_blob(td02_probe) == LOCKS["td02_probe_blob"], "TD02 probe source identity")
    req(td02_bounded.is_file() and git_blob(td02_bounded) == LOCKS["td02_bounded_blob"], "TD02 bounded source identity")
    text = td02_bounded.read_text()
    req("24*q + 4*(d/2 - t - 2*x4)^2 <= 3*d^2+48*d+96-96*g." in text, "concrete GRF04 formula source")
    req("upper = min((19*d)//5, 3*d, 3*d - (b-c))" in text, "e<=3d source")
    req("req(grf_bad >= hp_bad" in text, "TD02 encodes GRF04 as strengthening of HPADJ08 on its diagnostic domain")

    worst_num = 0
    worst_den = 1
    worst = None
    for g, max_d in ((0, 176), (1, 192)):
        for d in range(8, max_d + 1, 2):
            R = 3*d*d + 48*d + 96 - 96*g
            req(R >= 0 and R % 4 == 0, f"R divisibility {(g,d)}")
            r = math.isqrt(R // 4)
            num = r + 1
            den = 4*d + 1
            req(num * 33 <= 13 * den, f"13/33 bound failed {(g,d,num,den)}")
            if num * worst_den > worst_num * den:
                worst_num, worst_den, worst = num, den, (g, d, r)
    req(worst == (0, 8, 12) and worst_num == 13 and worst_den == 33, f"unexpected worst block {worst}")

    P10 = 7549*10*10 - 60592*10 - 102944
    req(P10 == 46036 and P10 > 0, "P(10)")
    req(30196*10 - 90988 == 210972 and 210972 > 0, "P even-step monotonicity")
    for d in range(10, 194, 2):
        P = 7549*d*d - 60592*d - 102944
        req(P >= P10, f"P monotonic sanity d={d}")
        R0 = 3*d*d + 48*d + 96
        req(1089*R0 <= (104*d - 40)**2, f"squared 13/33 inequality d={d}")

    expected = (13 * ENVELOPE) // 33
    req(expected == EXPECTED_CANDIDATE, "candidate arithmetic")
    req(V34_BOUND - expected == EXPECTED_TIGHTENING, "tightening arithmetic")
    cb = candidate["candidate_bound"]
    req(cb["candidate_upper_bound"] == EXPECTED_CANDIDATE, "candidate JSON bound")
    req(cb["candidate_tightening_vs_v34"] == EXPECTED_TIGHTENING, "candidate JSON tightening")
    req(candidate["uniform_block_proof"]["uniform_retained_fraction"] == "13/33", "candidate fraction")
    pg = candidate["promotion_gate"]
    req(pg["hostile_audit_required"] is True and pg["main_authority_mutated"] is False and pg["main_credit_granted"] is False, "promotion firewall")
    req(pg["exact_incremental_rejected_identity_set_claimed"] is False and pg["additive_subtraction_authorized"] is False, "no additive credit")
    req(candidate["firewalls"]["full178_complete"] is False and candidate["firewalls"]["merge_authorized"] is False, "closure firewalls")

    print("PASS: independent MAIN GRF04 uniform all-FULL178 x4-block theorem <= 13/33")
    print(f"PASS: candidate upper bound={EXPECTED_CANDIDATE} tightening_vs_V34={EXPECTED_TIGHTENING}")
    print("PASS: authority unchanged; hostile audit required before any MAIN promotion")


if __name__ == "__main__":
    main()
