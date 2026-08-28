#!/usr/bin/env python3
"""Source-lock cc/ct on the 140 known divisor classes, geometry only.

This deliberately stops before the Picard pairing/quotient construction.  The
Stage32 retained H-perp marking already reconstructs the integral Picard lattice
from these same 140 classes, so the two exact 140-class Galois permutations are
all Stage33 needs to recover cc/ct in the INDLIST basis locally.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path

from stoll_cuboid_source import load_pinned_source, run_magma, SKIP_START

HERE = Path(__file__).resolve().parent
OUT = HERE / "galois-known-class-permutations.json"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
KNOWN = 140


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


text, _, blob, source_attempt = load_pinned_source()
if blob != SOURCE_BLOB:
    raise SystemExit("pinned upstream blob moved")
try:
    cut = text.index(SKIP_START)
except ValueError as exc:
    raise SystemExit(f"pinned geometry marker missing: {exc}")

# Everything needed for S, the 92 known curves and the 48 singular points is
# constructed before the unused degree-8 block.  Avoid all Picard arithmetic.
geometry = text[:cut]
extra = r'''
ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
permcc := [Position(C1s, actcc(C)) : C in C1s]
            cat [#C1s+Position(C2s, actcc(C)) : C in C2s]
            cat [#C1s+#C2s+Position(C3s, actcc(C)) : C in C3s]
            cat [#Cs+Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];

ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permct := [Position(C1s, actct(C)) : C in C1s]
            cat [#C1s+Position(C2s, actct(C)) : C in C2s]
            cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
            cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];

assert #Cs eq 92 and #pts eq 48;
assert #permcc eq 140 and #permct eq 140;
assert Seqset(permcc) eq {1..140} and Seqset(permct) eq {1..140};
assert [permcc[permcc[j]] : j in [1..140]] eq [1..140];
assert [permct[permct[j]] : j in [1..140]] eq [1..140];
assert [permcc[permct[j]] : j in [1..140]] eq
       [permct[permcc[j]] : j in [1..140]];
printf "STAGE33_07_GALPERM_CC=%o\n", permcc;
printf "STAGE33_07_GALPERM_CT=%o\n", permct;
printf "STAGE33_07_GALPERM_DONE\n";
'''
code = "SetColumns(0);\nquick := true;\n" + geometry + "\n" + extra
stdout, magma_attempt = run_magma(
    code, 120, "Stage33-07 geometry-only cc/ct 140-class permutations",
    user_agent="perfect-cuboid-stage33/3.0",
)
if "STAGE33_07_GALPERM_DONE" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")
):
    print(stdout)
    raise SystemExit("geometry-only Galois permutation extraction failed")


def seq(name: str) -> list[int]:
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    value = ast.literal_eval(m.group(1))
    if not isinstance(value, list):
        raise SystemExit(f"{name} is not a list")
    return [int(x) for x in value]


cc = seq("STAGE33_07_GALPERM_CC")
ct = seq("STAGE33_07_GALPERM_CT")
identity = list(range(1, KNOWN + 1))
if sorted(cc) != identity or sorted(ct) != identity:
    raise SystemExit("Galois known-class output is not a permutation")
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
        "geometry_prefix_sha256": hashlib.sha256(geometry.encode()).hexdigest(),
        "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    },
    "known_curve_count": 92,
    "exceptional_count": 48,
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
        "magma_request_attempt": magma_attempt,
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
    "certificate_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
