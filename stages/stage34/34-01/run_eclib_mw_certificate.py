#!/usr/bin/env python3
import json
import pathlib
import re
import subprocess
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parent
OUT_JSON = ROOT / "mw-eclib-certificate.json"
OUT_TXT = ROOT / "mw-eclib-stdout.txt"

# Residual rank-one fibers not completed by the public Magma saturation route.
FIBERS = [
    {"q": "80/39", "P": ["-160/39", "1760/1521"]},
    {"q": "84/13", "P": ["17787/169", "216678/169"]},
    {"q": "48/55", "P": ["-24/25", "24/275"]},
    {"q": "20/99", "P": ["-20/27", "980/2673"]},
]

FULL_BASIS_SUCCESS = "The rank and full Mordell-Weil basis have been determined unconditionally."


def F(s):
    return Fraction(s)


def neg(P):
    if P is None:
        return None
    x, y = P
    return (x, -y)


def add(P, Q, a2, a4):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 == -y2:
        return None
    if P == Q:
        if y1 == 0:
            return None
        m = (3*x1*x1 + 2*a2*x1 + a4) / (2*y1)
    else:
        m = (y2-y1)/(x2-x1)
    x3 = m*m - a2 - x1 - x2
    y3 = -y1 + m*(x1-x3)
    return (x3, y3)


def mul(P, n, a2, a4):
    if n < 0:
        return mul(neg(P), -n, a2, a4)
    R = None
    Q = P
    while n:
        if n & 1:
            R = add(R, Q, a2, a4)
        Q = add(Q, Q, a2, a4)
        n >>= 1
    return R


def on_curve(P, a2, a4):
    if P is None:
        return True
    x, y = P
    return y*y == x*x*x + a2*x*x + a4*x


def parse_o_generator(stdout):
    # mwrank -o emits a PARI-style line, e.g. [[1],[[3,11]]].
    lines = [ln.strip() for ln in stdout.splitlines() if ln.strip()]
    candidates = [ln.replace(" ", "") for ln in lines if ln.strip().startswith("[[")]
    for ln in reversed(candidates):
        m = re.fullmatch(r"\[\[1\],\[\[([^\]]+)\]\]\]", ln)
        if not m:
            continue
        parts = m.group(1).split(",")
        if len(parts) == 2:
            return (F(parts[0]), F(parts[1])), ln
        if len(parts) == 3:
            X, Y, Z = map(F, parts)
            if Z == 0:
                raise RuntimeError("mwrank returned infinity as free generator")
            # eclib projective convention is [X:Y:Z] with affine x=X/Z^2,y=Y/Z^3.
            return (X/(Z*Z), Y/(Z*Z*Z)), ln
    raise RuntimeError("could not parse rank-one -o generator line")


def package_version():
    p = subprocess.run(
        ["dpkg-query", "-W", "-f=${Version}", "eclib-tools"],
        text=True, capture_output=True, check=True,
    )
    return p.stdout.strip()


records = []
raw_sections = []
for item in FIBERS:
    q = F(item["q"])
    a2 = 1 + q*q
    a4 = q*q
    P = (F(item["P"][0]), F(item["P"][1]))
    assert on_curve(P, a2, a4)

    curve = f"[0,{a2},0,{a4},0]\n"
    cmd = ["mwrank", "-q", "-v", "1", "-o"]
    proc = subprocess.run(cmd, input=curve, text=True, capture_output=True, timeout=240)
    stdout = proc.stdout + ("\nSTDERR:\n" + proc.stderr if proc.stderr else "")
    raw_sections.append(f"===== q={item['q']} =====\n{stdout}")
    if proc.returncode != 0:
        raise SystemExit(f"mwrank failed for q={item['q']} rc={proc.returncode}")

    low = stdout.lower()
    bad_markers = [
        "unable to saturate",
        "saturation failed",
        "not saturated",
        "warning: saturation",
        "conditional rank",
    ]
    bad = [s for s in bad_markers if s in low]
    if bad:
        raise SystemExit(f"mwrank saturation/rank warning for q={item['q']}: {bad}")
    if FULL_BASIS_SUCCESS not in stdout:
        raise SystemExit(
            f"mwrank did not positively certify the full Mordell-Weil basis for q={item['q']}"
        )

    G, o_line = parse_o_generator(stdout)
    if not on_curve(G, a2, a4):
        raise SystemExit(f"parsed mwrank generator is off curve for q={item['q']}")

    dminus = add(P, neg(G), a2, a4)
    dplus = add(P, G, a2, a4)
    minus_torsion4 = mul(dminus, 4, a2, a4) is None
    plus_torsion4 = mul(dplus, 4, a2, a4) is None
    same_free_generator = minus_torsion4 or plus_torsion4
    if not same_free_generator:
        raise SystemExit(f"Paper-C source point is not +/- the mwrank basis modulo 4-torsion for q={item['q']}")

    records.append({
        "q": item["q"],
        "curve": f"y^2=x^3+({a2})*x^2+({a4})*x",
        "paper_c_source_point": [str(P[0]), str(P[1])],
        "mwrank_generator": [str(G[0]), str(G[1])],
        "mwrank_o_line": o_line,
        "full_mw_basis_success_sentence_seen": True,
        "paper_minus_generator_is_4_torsion": minus_torsion4,
        "paper_plus_generator_is_4_torsion": plus_torsion4,
        "source_spans_full_free_part": same_free_generator,
    })

payload = {
    "schema": "STAGE34_01_ECLIB_MWRANK_RESIDUAL_MW_CERTIFICATE_V2_POSITIVE_FULL_BASIS_MARKER",
    "status": "PASS_ECLIB_MWRANK_FULL_BASIS_MOD_TORSION_REPLAY",
    "software": {
        "package": "eclib-tools",
        "package_version": package_version(),
        "routine": "mwrank",
        "command": "mwrank -q -v 1 -o",
        "semantics": "with -o, mwrank performs its default saturation and outputs generators; warnings fail closed and the explicit unconditional full-MW-basis success sentence is required",
    },
    "paper_c_rank_source": "Paper C verify_ranks.gp tight rank locks remain the independent rank authority",
    "torsion_exponent": 4,
    "method": "For each residual rank-one fiber, require mwrank's explicit unconditional full Mordell-Weil basis certificate, obtain its saturated free generator G on the original rational model, and exact-replay 4*(P-G)=O or 4*(P+G)=O. Since E_q(Q)_tors has exponent 4, this proves P and +/-G have the same free class.",
    "fibers": records,
    "all_residual_source_points_span_full_free_part": all(r["source_spans_full_free_part"] for r in records),
    "credit_firewall": {
        "mw_population_repair_is_primitive_divisor_theorem": False,
        "mw_population_repair_is_receiver_closure": False,
        "mw_population_repair_is_endpoint_closure": False,
    },
}
OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
OUT_TXT.write_text("\n".join(raw_sections), encoding="utf-8")
print(json.dumps({
    "status": payload["status"],
    "package_version": payload["software"]["package_version"],
    "fibers": len(records),
    "all_residual_source_points_span_full_free_part": payload["all_residual_source_points_span_full_free_part"],
}, sort_keys=True))
