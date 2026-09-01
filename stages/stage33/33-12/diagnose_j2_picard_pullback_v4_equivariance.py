#!/usr/bin/env python3
"""Exact diagnostic for V4-equivariance of the Kc-to-full-surface Picard pullback.

The current J2 raw ct defect was transported from six Kc divisor classes to the
full-surface Picard lattice. That transport was exact as a lattice map, but its
producer deliberately did not compute Galois action. Rebuild the same pinned
Stoll model and check, integrally, that for g=cc,ct

    K_g * MatKtoS = MatKtoS * S_g

in the row-action convention used by the repository.

This is diagnostic only. It does not promote a Kummer relation or column.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"

sys.path.insert(0, str(LEGACY))
from stoll_cuboid_source import load_pinned_source, run_magma  # noqa: E402

text, core, blob, source_attempt = load_pinned_source()
if blob != SOURCE_BLOB:
    raise SystemExit("pinned Stoll source blob moved")

start = "// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6."
end = "// action of sign change of c"
kcore = text[text.index(start):text.index(end, text.index(start))]

extra = r'''
// Reconstruct the two Galois actions on Pic(S) omitted by the compact core.
ccL33 := hom<L -> L | -i>;
ctL33 := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
RS33 := CoordinateRing(Pr6);
ccPS33 := hom<RS33 -> RS33 | ccL33*Bang(L,RS33), [RS33.j : j in [1..7]]>;
ctPS33 := hom<RS33 -> RS33 | ctL33*Bang(L,RS33), [RS33.j : j in [1..7]]>;
actccS33 := func<C | Curve(Pr6, [ccPS33(e) : e in DefiningEquations(C)])>;
actctS33 := func<C | Curve(Pr6, [ctPS33(e) : e in DefiningEquations(C)])>;
permccS33 := [Position(C1s, actccS33(C)) : C in C1s]
  cat [#C1s+Position(C2s, actccS33(C)) : C in C2s]
  cat [#C1s+#C2s+Position(C3s, actccS33(C)) : C in C3s]
  cat [#Cs+Position(pts, Pr6![ccL33(a) : a in Eltseq(pt)]) : pt in pts];
permctS33 := [Position(C1s, actctS33(C)) : C in C1s]
  cat [#C1s+Position(C2s, actctS33(C)) : C in C2s]
  cat [#C1s+#C2s+Position(C3s, actctS33(C)) : C in C3s]
  cat [#Cs+Position(pts, Pr6![ctL33(a) : a in Eltseq(pt)]) : pt in pts];
assert &and[j gt 0 : j in permccS33] and &and[j gt 0 : j in permctS33];
actpermS33 := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;
ccPicS33 := Matrix(Integers(), [Eltseq(actpermS33(Pic.j, permccS33)) : j in [1..64]]);
ctPicS33 := Matrix(Integers(), [Eltseq(actpermS33(Pic.j, permctS33)) : j in [1..64]]);
assert ccPicS33*pmPic*Transpose(ccPicS33) eq pmPic;
assert ctPicS33*pmPic*Transpose(ctPicS33) eq pmPic;
assert ccPicS33^2 eq IdentityMatrix(Integers(),64);
assert ctPicS33^2 eq IdentityMatrix(Integers(),64);
assert ccPicS33*ctPicS33 eq ctPicS33*ccPicS33;

// Reconstruct the same two Galois actions on Pic(K).
RK33 := CoordinateRing(Pr5);
ccPK33 := hom<RK33 -> RK33 | ccL33*Bang(L,RK33), [RK33.j : j in [1..6]]>;
ctPK33 := hom<RK33 -> RK33 | ctL33*Bang(L,RK33), [RK33.j : j in [1..6]]>;
actccK33 := func<C | Curve(Pr5, [ccPK33(e) : e in DefiningEquations(C)])>;
actctK33 := func<C | Curve(Pr5, [ctPK33(e) : e in DefiningEquations(C)])>;
permccK33 := [Position(C1sK, actccK33(C)) : C in C1sK]
  cat [#C1sK+Position(C2sK, actccK33(C)) : C in C2sK]
  cat [#C1sK+#C2sK+Position(C3sK, actccK33(C)) : C in C3sK]
  cat [#CsK+Position(ptsK, Pr5![ccL33(a) : a in Eltseq(pt)]) : pt in ptsK];
permctK33 := [Position(C1sK, actctK33(C)) : C in C1sK]
  cat [#C1sK+Position(C2sK, actctK33(C)) : C in C2sK]
  cat [#C1sK+#C2sK+Position(C3sK, actctK33(C)) : C in C3sK]
  cat [#CsK+Position(ptsK, Pr5![ctL33(a) : a in Eltseq(pt)]) : pt in ptsK];
assert &and[j gt 0 : j in permccK33] and &and[j gt 0 : j in permctK33];
actpermK33 := func<g, perm | qPicK(BigK![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPicK)>;
ccPicK33 := Matrix(Integers(), [Eltseq(actpermK33(PicK.j, permccK33)) : j in [1..20]]);
ctPicK33 := Matrix(Integers(), [Eltseq(actpermK33(PicK.j, permctK33)) : j in [1..20]]);
assert ccPicK33*pmPicK*Transpose(ccPicK33) eq pmPicK;
assert ctPicK33*pmPicK*Transpose(ctPicK33) eq pmPicK;
assert ccPicK33^2 eq IdentityMatrix(Integers(),20);
assert ctPicK33^2 eq IdentityMatrix(Integers(),20);
assert ccPicK33*ctPicK33 eq ctPicK33*ccPicK33;

// Naturality of the degree-two Picard pullback, exactly over Z.
assert ccPicK33*MatKtoS eq MatKtoS*ccPicS33;
assert ctPicK33*MatKtoS eq MatKtoS*ctPicS33;
printf "STAGE33_12_PICARD_PULLBACK_V4_EQUIVARIANCE=PASS_EXACT\n";
printf "CC_EQUIVARIANT=true\n";
printf "CT_EQUIVARIANT=true\n";
printf "MAT_K_TO_S_ROWS=%o\n", Nrows(MatKtoS);
printf "MAT_K_TO_S_COLS=%o\n", Ncols(MatKtoS);
'''

code = "SetColumns(0);\nquick := true;\n" + core + "\n" + kcore + "\n" + extra
stdout, magma_attempt = run_magma(
    code,
    360,
    "Stage33-12 Kc-to-S Picard V4 equivariance",
    user_agent="perfect-cuboid-stage33/4.6-j2-picard-v4-equivariance",
)
if any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
    print(stdout)
    raise SystemExit("Picard pullback V4-equivariance diagnostic failed")
if "STAGE33_12_PICARD_PULLBACK_V4_EQUIVARIANCE=PASS_EXACT" not in stdout:
    print(stdout)
    raise SystemExit("missing V4-equivariance PASS marker")
for key in ("CC_EQUIVARIANT", "CT_EQUIVARIANT"):
    m = re.search(rf"^{key}=(.+)$", stdout, re.M)
    if not m or m.group(1).strip() != "true":
        raise SystemExit(f"missing {key} exact true marker")
print({
    "success": True,
    "cc_equivariant": True,
    "ct_equivariant": True,
    "picard_pullback_shape": [20, 64],
    "stoll_blob_sha1": blob,
    "submitted_magma_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    "source_fetch_attempt": source_attempt,
    "magma_request_attempt": magma_attempt,
    "promotion": "DIAGNOSTIC_ONLY_NO_KUMMER_RELATION_OR_COLUMN",
})
