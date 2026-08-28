#!/usr/bin/env python3
"""Source-lock cc/ct on the 140 known divisor classes, geometry only.

The public Magma calculator times out if all 92 known curves and 48 singular
points are materialized in one request. Split the same pinned upstream
geometry into two bounded requests:
  (1) the 92 curve permutations;
  (2) the 48 exceptional-point permutations.
No Picard pairing, quotient or Smith computation is performed remotely.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path

from stoll_cuboid_source import load_pinned_source, run_magma

HERE = Path(__file__).resolve().parent
OUT = HERE / "galois-known-class-permutations.json"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
KNOWN = 140
CURVES = 92
POINTS = 48

POINT_MARKER = "// The 48 singular points"
CURVE_MARKER = "// See Definition 6 for C1s, C2s, C3s."
CPTS_MARKER = "// ...and the singular points on them"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def parse_seq(stdout: str, name: str) -> list[int]:
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    value = ast.literal_eval(m.group(1))
    if not isinstance(value, list):
        raise SystemExit(f"{name} is not a list")
    return [int(x) for x in value]


text, _, blob, source_attempt = load_pinned_source()
if blob != SOURCE_BLOB:
    raise SystemExit("pinned upstream blob moved")
try:
    point_start = text.index(POINT_MARKER)
    curve_start = text.index(CURVE_MARKER, point_start)
    curve_end = text.index(CPTS_MARKER, curve_start)
except ValueError as exc:
    raise SystemExit(f"pinned geometry marker missing: {exc}")

surface_prefix = text[:point_start]
curve_geometry = surface_prefix + text[curve_start:curve_end]
point_geometry = text[:curve_start]

curve_extra = r"""
ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
cccurves := [Position(C1s, actcc(C)) : C in C1s]
             cat [#C1s+Position(C2s, actcc(C)) : C in C2s]
             cat [#C1s+#C2s+Position(C3s, actcc(C)) : C in C3s];

ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
ctcurves := [Position(C1s, actct(C)) : C in C1s]
             cat [#C1s+Position(C2s, actct(C)) : C in C2s]
             cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s];

assert #Cs eq 92;
assert #cccurves eq 92 and #ctcurves eq 92;
assert Seqset(cccurves) eq {1..92} and Seqset(ctcurves) eq {1..92};
printf "STAGE33_07_GALCURVE_CC=%o\n", cccurves;
printf "STAGE33_07_GALCURVE_CT=%o\n", ctcurves;
printf "STAGE33_07_GALCURVE_DONE\n";
"""

point_extra = r"""
ccL := hom<L -> L | -i>;
ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ccpts := [Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];
ctpts := [Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];

assert #pts eq 48;
assert #ccpts eq 48 and #ctpts eq 48;
assert Seqset(ccpts) eq {1..48} and Seqset(ctpts) eq {1..48};
printf "STAGE33_07_GALPOINT_CC=%o\n", ccpts;
printf "STAGE33_07_GALPOINT_CT=%o\n", ctpts;
printf "STAGE33_07_GALPOINT_DONE\n";
"""

curve_code = "SetColumns(0);\nquick := true;\n" + curve_geometry + "\n" + curve_extra
point_code = "SetColumns(0);\nquick := true;\n" + point_geometry + "\n" + point_extra

curve_stdout, curve_attempt = run_magma(
    curve_code, 120, "Stage33-07 cc/ct 92-curve permutations",
    user_agent="perfect-cuboid-stage33/3.1-curves",
)
if "STAGE33_07_GALCURVE_DONE" not in curve_stdout or any(
    x in curve_stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")
):
    print(curve_stdout)
    raise SystemExit("curve-only Galois permutation extraction failed")

point_stdout, point_attempt = run_magma(
    point_code, 120, "Stage33-07 cc/ct 48-point permutations",
    user_agent="perfect-cuboid-stage33/3.1-points",
)
if "STAGE33_07_GALPOINT_DONE" not in point_stdout or any(
    x in point_stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")
):
    print(point_stdout)
    raise SystemExit("point-only Galois permutation extraction failed")

cc_curves = parse_seq(curve_stdout, "STAGE33_07_GALCURVE_CC")
ct_curves = parse_seq(curve_stdout, "STAGE33_07_GALCURVE_CT")
cc_points = parse_seq(point_stdout, "STAGE33_07_GALPOINT_CC")
ct_points = parse_seq(point_stdout, "STAGE33_07_GALPOINT_CT")

if sorted(cc_curves) != list(range(1, CURVES + 1)):
    raise SystemExit("cc curve output is not a permutation")
if sorted(ct_curves) != list(range(1, CURVES + 1)):
    raise SystemExit("ct curve output is not a permutation")
if sorted(cc_points) != list(range(1, POINTS + 1)):
    raise SystemExit("cc point output is not a permutation")
if sorted(ct_points) != list(range(1, POINTS + 1)):
    raise SystemExit("ct point output is not a permutation")

cc = cc_curves + [CURVES + x for x in cc_points]
ct = ct_curves + [CURVES + x for x in ct_points]
identity = list(range(1, KNOWN + 1))
if sorted(cc) != identity or sorted(ct) != identity:
    raise SystemExit("combined Galois known-class output is not a permutation")
if [cc[cc[j] - 1] for j in range(KNOWN)] != identity:
    raise SystemExit("cc known-class permutation is not involutive")
if [ct[ct[j] - 1] for j in range(KNOWN)] != identity:
    raise SystemExit("ct known-class permutation is not involutive")
if [cc[ct[j] - 1] for j in range(KNOWN)] != [ct[cc[j] - 1] for j in range(KNOWN)]:
    raise SystemExit("cc/ct known-class permutations do not commute")

out = {
    "schema": "STAGE33_07_GALOIS_KNOWN_CLASS_PERMUTATIONS_V1",
    "source": {
        "repository": "MichaelStollBayreuth/Verification",
        "commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "path": "Cuboids/cuboids.magma",
        "git_blob_sha1": blob,
        "geometry_prefix_sha256": hashlib.sha256((curve_geometry + "\0" + point_geometry).encode()).hexdigest(),
        "submitted_code_sha256": hashlib.sha256((curve_code + "\0" + point_code).encode()).hexdigest(),
    },
    "known_curve_count": CURVES,
    "exceptional_count": POINTS,
    "known_class_count": KNOWN,
    "cc_permutation_1based": cc,
    "ct_permutation_1based": ct,
    "relations": {
        "cc_involution": True,
        "ct_involution": True,
        "cc_ct_commute": True,
    },
    "execution": {
        "source_fetch_attempt": source_attempt,
        "magma_request_attempt": max(curve_attempt, point_attempt),
        "split_magma_requests": 2,
        "curve_request_attempt": curve_attempt,
        "point_request_attempt": point_attempt,
        "picard_pairing_constructed": False,
        "picard_quotient_constructed": False,
        "smith_form_constructed": False,
    },
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "known_class_count": KNOWN,
    "geometry_only": True,
    "split_magma_requests": 2,
    "certificate_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
