#!/usr/bin/env python3
"""Goal4AJ gen24: Stage32-style parallel prime checkpoint/materialization.

Run the already source-locked degree-31 strict-kernel computation independently
at four good split primes, then aggregate the four unique projective lines by
CRT/rational reconstruction.  This deliberately avoids gen21->gen22->gen23
nested replay.  The aggregate is accepted only if it reproduces the exact Q
candidate hash/size/height already obtained and first-strict checked by gen23.

Diagnostic/materialization transport only.  It does not grant literal numerator,
F_B, local, Brauer-Manin, E1, Stage35, theorem, receiver, or endpoint credit.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
GEN17 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17.py"
GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"
STRICT_PACKET_OLD = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"
PRIMES = {
    1: (32009, 10754, 8047),
    2: (32057, 8059, 14662),
    3: (32089, 9893, 9854),
    4: (32233, 3354, 12944),
}
DEGREE = 31
SUPPORT_COUNT = 5924
SUPPORT_SHA256 = "75d30dd90779604b46e34d0e7210f9e403ef3481af1196c55ac46051ea17a372"
NORMALIZATION_MONOMIAL = "a1*a2*a3*b1*b2*b3*c^25"
BALANCED_BOUND = 700_000_000
EXPECTED_Q_SHA256 = "358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb"
EXPECTED_Q_BYTES = 208802
EXPECTED_MAX_NUM = 39155899
EXPECTED_MAX_DEN = 174336
GEN23_RUN = 34195787266
GEN23_JOB = 101963128070
GEN23_CANONICAL = "0fe84fb94968d4283392383056e321ba1f430f8929897f0bab07d90d55dd76df"
GEN23_ROUTE = "FOUR_PRIME_SUPPORT_MATCHED_BALANCED_RECONSTRUCTION_FIRST_STRICT_EXACT_PASS_ALL_STRICT_REPLAY_READY"


def csha(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def parse_candidate(candidate: str, p: int) -> dict[str, int]:
    out = {}
    for m in re.finditer(r"([+-]?)([^+-]+)", candidate):
        sign_s, body = m.groups()
        sign = -1 if sign_s == "-" else 1
        factors = body.split("*")
        if factors[0].isdigit():
            coeff = sign * int(factors[0]); mon = "*".join(factors[1:])
        else:
            coeff = sign; mon = body
        if not mon or mon in out:
            raise SystemExit("unexpected candidate encoding")
        out[mon] = coeff % p
    return out


def patched_gen17(slot: int) -> dict:
    p, ir, sr = PRIMES[slot]
    assert git_blob(GEN17) == GEN17_BLOB
    assert p % 8 == 1 and pow(ir, 2, p) == p - 1 and pow(sr, 2, p) == 2
    src = GEN17.read_text(encoding="utf-8")
    replacements = [
        ('DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"', f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"'),
        (f'STRICT_PACKET_SHA256 = "{STRICT_PACKET_OLD}"', f'STRICT_PACKET_SHA256 = "{STRICT_PACKET}"'),
    ]
    if slot != 1:
        replacements += [
            ("FIELD_PRIME = 32009", f"FIELD_PRIME = {p}"),
            ("I_ROOT = 10754", f"I_ROOT = {ir}"),
            ("SQRT2_ROOT = 8047", f"SQRT2_ROOT = {sr}"),
            ("ring r=32009,(a1,a2,a3,b1,b2,b3,c),dp;", f"ring r={p},(a1,a2,a3,b1,b2,b3,c),dp;"),
            ("number ii=10754;", f"number ii={ir};"),
            ("number ss=8047;", f"number ss={sr};"),
        ]
    for old, new in replacements:
        if src.count(old) != 1:
            raise SystemExit(f"gen24 patch cardinality mismatch: {old!r}")
        src = src.replace(old, new, 1)
    ns = {"__name__": "__main__", "__file__": str(GEN17)}
    buf = io.StringIO()
    with redirect_stdout(buf):
        exec(compile(src, str(GEN17) + f"[gen24-p{p}]", "exec"), ns)
    g = ns["out"]; cands = ns["candidates"]
    if not (g["numerator_strict_kernel_completed"] is True and g["strict_condition_section_space_degree31_dimension"] == 1 and len(cands) == 1):
        raise SystemExit("prime strict-kernel did not reproduce unique line")
    cand = cands[0]
    mp = parse_candidate(cand, p)
    support = sorted(mp)
    ssha = hashlib.sha256("\n".join(support).encode()).hexdigest()
    if len(support) != SUPPORT_COUNT or ssha != SUPPORT_SHA256:
        raise SystemExit("prime support regression")
    return {"prime": p, "i_root": ir, "sqrt2_root": sr, "candidate": cand,
            "candidate_sha256": hashlib.sha256(cand.encode()).hexdigest(),
            "candidate_bytes": len(cand.encode()), "support_sha256": ssha}


def prime_mode(slot: int, outdir: Path):
    r = patched_gen17(slot)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "candidate.txt").write_text(r.pop("candidate"), encoding="utf-8")
    meta = {"schema": "STAGE35_EX_GOAL4AJ_GEN24_PRIME_CHECKPOINT_V1", "slot": slot,
            "gen17_blob_sha1": GEN17_BLOB, "degree": DEGREE, "support_count": SUPPORT_COUNT,
            **r, "literal_q_numerator_materialized": False, "theorem_credit": False}
    meta["canonical_sha256"] = csha(meta)
    (outdir / "prime.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("GOAL4AJ_GEN24_PRIME_JSON=" + json.dumps(meta, sort_keys=True, separators=(",", ":")), flush=True)


def crt_pair(a: int, p: int, b: int, q: int) -> int:
    return (a + p * (((b - a) * pow(p, -1, q)) % q)) % (p * q)


def ratrec(v: int, modulus: int, A: int, B: int):
    assert 2 * A * B < modulus
    v %= modulus
    if v == 0: return Fraction(0, 1)
    r0, r1 = modulus, v; s0, s1 = 0, 1
    while r1 and abs(r1) > A:
        q = r0 // r1; r0, r1 = r1, r0 - q * r1; s0, s1 = s1, s0 - q * s1
    if r1 == 0 or s1 == 0: return None
    a, b = r1, s1
    if b < 0: a, b = -a, -b
    g = math.gcd(abs(a), b); a //= g; b //= g
    if abs(a) > A or not (1 <= b <= B) or (a - v * b) % modulus: return None
    return Fraction(a, b)


def aggregate_mode(indir: Path, outdir: Path):
    metas = {}
    for pth in indir.rglob("prime.json"):
        m = json.loads(pth.read_text(encoding="utf-8")); slot = int(m["slot"])
        if slot in metas: raise SystemExit("duplicate prime slot")
        cand = (pth.parent / "candidate.txt").read_text(encoding="utf-8")
        if hashlib.sha256(cand.encode()).hexdigest() != m["candidate_sha256"]: raise SystemExit("candidate hash mismatch")
        metas[slot] = (m, cand)
    if set(metas) != set(PRIMES): raise SystemExit(f"missing prime checkpoints: {sorted(metas)}")
    maps = {}; support = None
    for slot in sorted(metas):
        m, cand = metas[slot]; p = int(m["prime"]); mp = parse_candidate(cand, p); s = sorted(mp)
        if support is None: support = s
        if s != support: raise SystemExit("four-prime support mismatch")
        lead = mp[NORMALIZATION_MONOMIAL]
        if lead == 0: raise SystemExit("normalization coefficient zero")
        maps[slot] = {mon: v * pow(lead, -1, p) % p for mon, v in mp.items()}
    assert support is not None and len(support) == SUPPORT_COUNT
    modulus = 1; crt = {mon: 0 for mon in support}
    first = True
    for slot in sorted(PRIMES):
        p = PRIMES[slot][0]
        if first:
            crt = dict(maps[slot]); modulus = p; first = False
        else:
            crt = {mon: crt_pair(crt[mon], modulus, maps[slot][mon], p) for mon in support}; modulus *= p
    recon = {mon: ratrec(crt[mon], modulus, BALANCED_BOUND, BALANCED_BOUND) for mon in support}
    if any(q is None for q in recon.values()): raise SystemExit("four-prime balanced reconstruction incomplete")
    def fstr(q): return str(q.numerator) if q.denominator == 1 else f"({q.numerator}/{q.denominator})"
    def term(q, mon, first_term):
        sign = "-" if q < 0 else "+"; a = abs(q); body = mon if a == 1 else f"({fstr(a)})*{mon}"
        return (("-" if q < 0 else "") if first_term else sign) + body
    exact = [(mon, recon[mon]) for mon in support]
    qrat = "".join(term(q, mon, k == 0) for k, (mon, q) in enumerate(exact))
    qsha = hashlib.sha256(qrat.encode()).hexdigest(); qbytes = len(qrat.encode())
    maxnum = max(abs(q.numerator) for _, q in exact); maxden = max(q.denominator for _, q in exact)
    if (qsha, qbytes, maxnum, maxden) != (EXPECTED_Q_SHA256, EXPECTED_Q_BYTES, EXPECTED_MAX_NUM, EXPECTED_MAX_DEN):
        raise SystemExit(f"gen23 Q candidate reproduction mismatch: {(qsha,qbytes,maxnum,maxden)}")
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "qcandidate.txt").write_text(qrat, encoding="utf-8")
    report = {
        "schema": "STAGE35_EX_GOAL4AJ_GEN24_PARALLEL_FOUR_PRIME_MATERIALIZATION_V1",
        "source_locks": {"gen17_blob_sha1": GEN17_BLOB, "gen23_run": GEN23_RUN, "gen23_job": GEN23_JOB,
                         "gen23_canonical_sha256": GEN23_CANONICAL, "gen23_route": GEN23_ROUTE},
        "primes": [PRIMES[i][0] for i in sorted(PRIMES)], "four_prime_modulus": modulus,
        "support_count": len(support), "support_sha256": SUPPORT_SHA256,
        "projective_normalization_monomial": NORMALIZATION_MONOMIAL,
        "reconstructed_count": len(exact), "q_candidate_sha256": qsha, "q_candidate_text_bytes": qbytes,
        "q_candidate_max_abs_numerator": maxnum, "q_candidate_max_denominator": maxden,
        "reproduces_gen23_first_strict_pass_candidate_exactly": True,
        "route_result": "PARALLEL_FOUR_PRIME_CHECKPOINT_REPRODUCED_GEN23_Q_CANDIDATE_MATERIALIZATION_TRANSPORT_READY",
        "literal_q_numerator_materialized": False, "literal_F_B_materialized": False,
        "local_evaluations_computed": False, "brauer_manin_obstruction_obtained": False,
        "E1_proved": False, "stage35_closed": False, "theorem_credit": False, "endpoint_credit": False,
    }
    report["canonical_sha256"] = csha(report)
    (outdir / "certificate.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("GOAL4AJ_GEN24_AGGREGATE_JSON=" + json.dumps(report, sort_keys=True, separators=(",", ":")), flush=True)


def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="mode", required=True)
    p = sub.add_parser("prime"); p.add_argument("--slot", type=int, choices=sorted(PRIMES), required=True); p.add_argument("--output-dir", type=Path, required=True)
    a = sub.add_parser("aggregate"); a.add_argument("--input-dir", type=Path, required=True); a.add_argument("--output-dir", type=Path, required=True)
    x = ap.parse_args()
    if x.mode == "prime": prime_mode(x.slot, x.output_dir)
    else: aggregate_mode(x.input_dir, x.output_dir)

if __name__ == "__main__": main()
