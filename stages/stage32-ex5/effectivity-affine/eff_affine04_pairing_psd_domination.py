#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
RES = ROOT / "stages/stage32/residual-32-01-production"
RET = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARK = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
HPA = RES / "hperp_integral_adapter.py"
DPS = RES / "direct_picard_slice_bridge.py"

LOCK = {
    HPA: "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    DPS: "be48bd94304d0217727c5c3368761d347cb22eaa",
    RET: "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    MARK: "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
}


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    b = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_module(p: Path, name: str):
    s = importlib.util.spec_from_file_location(name, p)
    req(s is not None and s.loader is not None, "module spec " + name)
    m = importlib.util.module_from_spec(s)
    sys.modules[name] = m
    s.loader.exec_module(m)
    return m


def positive_definite(m: Matrix) -> bool:
    if m != m.T:
        return False
    try:
        l, d = m.LDLdecomposition(hermitian=False)
    except Exception:
        return False
    return m == l * d * l.T and all(d[i, i] > 0 for i in range(d.rows))


def min_coord(good, fixed: int, upper: int, which: str) -> int:
    lo, hi = -1, upper
    req((good(hi, fixed) if which == "normal" else good(fixed, hi)), "upper coordinate lost PSD")
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        ok = good(mid, fixed) if which == "normal" else good(fixed, mid)
        if ok:
            hi = mid
        else:
            lo = mid
    return hi


def main() -> None:
    # Lock before executing any mutable producer/retained source.
    for p, h in LOCK.items():
        req(p.is_file() and blob(p) == h, "source lock " + str(p))

    sys.path.insert(0, str(RES))
    hpa = load_module(HPA, "eff04_hpa")
    dps = load_module(DPS, "eff04_dps")
    bundle = load_module(RET, "eff04_ret").load()
    mark = load_module(MARK, "eff04_mark").load()

    adapter = hpa.HperpIntegralPairingAdapter.from_retained(mark, bundle)
    bridge = dps.DirectPicardSliceBridge.from_retained(mark, bundle)

    P = Matrix(adapter.pairing_matrix)
    G = Matrix(bundle["picard_gram_64x64"])
    H = Matrix(1, 64, bridge.degree_functional)
    E = Matrix(1, 64, bridge.exceptional_mass_functional)

    req(P.shape == (140, 64), "pairing matrix shape")
    req(G.shape == (64, 64) and G == G.T, "Gram matrix")
    req(adapter.certificate["selected64_change_of_basis_unimodular"] is True,
        "selected64 pairing injectivity certificate")

    normal_sum = sum((P.row(i) for i in range(92)), Matrix.zeros(1, 64))
    exceptional_sum = sum((P.row(i) for i in range(92, 140)), Matrix.zeros(1, 64))
    req(exceptional_sum == E, "exceptional mass identity")
    req(normal_sum + 5 * exceptional_sum == 19 * H, "normal mass identity")

    PN = P[:92, :]
    PE = P[92:, :]
    FN = PN.T * PN
    FE = PE.T * PE

    # Q(C) = d^2/16 - C^2.  Work with 16Q to keep the certificate integral.
    Q16 = H.T * H - 16 * G

    def good(wn: int, we: int) -> bool:
        if wn < 0 or we < 0:
            return False
        return positive_definite(16 * (wn * FN + we * FE) - Q16)

    scalar = 1
    while not good(scalar, scalar):
        scalar *= 2
        req(scalar <= (1 << 20), "scalar PSD search exceeded cap")
    lo, hi = 0, scalar
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if good(mid, mid):
            hi = mid
        else:
            lo = mid
    scalar = hi

    wn = min_coord(good, scalar, scalar, "normal")
    we = min_coord(good, wn, scalar, "exceptional")
    # Monotone coordinate descent to a stable exact integer certificate.
    for _ in range(8):
        n2 = min_coord(good, we, wn, "normal")
        e2 = min_coord(good, n2, we, "exceptional")
        if (n2, e2) == (wn, we):
            break
        wn, we = n2, e2
    req(good(wn, we), "final PSD domination")

    cert = 16 * (wn * FN + we * FE) - Q16
    _, dcert = cert.LDLdecomposition(hermitian=False)
    diag = [str(dcert[i, i]) for i in range(dcert.rows)]

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE04_PAIRING_PSD_DOMINATION_V1",
        "status": "PASS_EXACT_GLOBAL_HPERP_NORM_ENVELOPE",
        "pairing_blocks": {"normal": 92, "exceptional": 48},
        "weights": {
            "scalar_integer_upper_bound": scalar,
            "normal_integer_weight": wn,
            "exceptional_integer_weight": we,
        },
        "exact_domination": {
            "matrix_statement": "16*(wN*PN^T*PN+wE*PE^T*PE)-(H^T*H-16G) is positive definite",
            "ldl_positive": True,
            "ldl_diagonal_sha256": hashlib.sha256(json.dumps(diag, separators=(",", ":")).encode()).hexdigest(),
        },
        "mass_identities": {
            "exceptional_sum": "sum(E_48)=e",
            "normal_sum": "sum(N_92)=19*d-5*e",
        },
        "population_envelope": {
            "hypothesis": "all140 pairings nonnegative at fixed d,e",
            "Q": "d^2/16-C^2",
            "bound": f"Q <= {wn}*(19*d-5*e)^2 + {we}*e^2",
            "reason": "sum of nonnegative squares in each block is at most the square of that block sum",
        },
        "interpretation": {
            "what_is_proved": "A source-locked exact population-level quadratic radius exists for every all140-nonnegative fixed-(d,e) fiber.",
            "next_exact_unit": "Push this certified radius through the 58D Gram-LLL coordinates and test whether it yields a practical complete Fincke-Pohst radius before any heavy shard is armed.",
            "what_is_not_proved": "No bad-shell UNSAT, effectivity, MAIN pruning, receiver, theorem, endpoint, or merge credit.",
        },
        "credit": {"effectivity": False, "main": False, "theorem": False, "endpoint": False, "merge": False},
    }
    print("EFF_AFFINE04_PSD_DOMINATION=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
