#!/usr/bin/env python3
"""Compute H^1(V4,UPic) from the same exact total complex used for H^2.

For U_D=Z^14 with trivial finite V4 action, H^1(V4,U_D)=0, so the
hypercohomology edge sequence gives H^1(V4,UPic)=ker(d2^{0,1}).  Since
Pic(Ubar)^V4=(Z/2)^2, this determines rank(d2_01) exactly.  The already
certified H^1(V4,PicU)=(Z/2)^9 and H^2(V4,UPic)=(Z/2)^33 then determine
rank(d2_11) exactly as well.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
src=(ROOT/"compute_v4_hypercohomology.py").read_text(encoding="utf-8")
needle='printf "STAGE33_03_V4_HYPER_BEGIN\\\\n";'
if src.count(needle)!=1:
    raise SystemExit("could not locate finite-V4 output marker")
inject=r'''
// Also compute H^1 = ker(D1)/im(D0) from the same integral total complex.
S1, _, V1 := SmithForm(Transpose(D1));
r1h := Rank(D1);
n1h := Nrows(D1);
kdim1 := n1h-r1h;
V1inv := V1^-1;
Coords1 := D0*Transpose(V1inv);
for rr0 in [1..Nrows(Coords1)] do
  for cc0 in [1..r1h] do
    assert Coords1[rr0,cc0] eq 0;
  end for;
end for;
Brel1 := Submatrix(Coords1,1,r1h+1,Nrows(Coords1),kdim1);
SB1 := SmithForm(Brel1);
rr1h := Rank(Brel1);
diag1 := [Abs(Z!SB1[j,j]) : j in [1..rr1h]];
tors1 := [d : d in diag1 | d ne 1];
free1 := kdim1-rr1h;
assert forall{d : d in tors1 | d in [2,4]};
printf "H1_FREE_RANK=%o\n", free1;
printf "H1_TORSION=%o\n", tors1;
'''
src=src.replace(needle, inject+"\n"+needle)
# Run the source-locked calculator.  It writes the common stdout/certificate.
exec(compile(src,str(ROOT/"compute_v4_hypercohomology.py")+"[H1-ranks]","exec"),{"__name__":"__main__","__file__":str(ROOT/"compute_v4_hypercohomology.py")})

stdout=(ROOT/"v4-hyper-magma-stdout.txt").read_text(encoding="utf-8")
def scalar(name):
    m=re.search(rf"^{name}=(.+)$",stdout,re.M)
    if not m: raise SystemExit(f"missing injected {name}")
    return m.group(1).strip()
def intlist(s):
    s=s.strip()
    if s=="[]": return []
    return [int(x.strip()) for x in s[1:-1].split(",") if x.strip()]
free=int(scalar("H1_FREE_RANK")); tors=intlist(scalar("H1_TORSION"))
if free!=0 or any(x!=2 for x in tors) or len(tors)>2:
    raise SystemExit(f"unexpected H1(V4,UPic): free={free}, tors={tors}")
h1dim=len(tors)
r01=2-h1dim
r11=4-r01
if (r01,r11) not in ((0,4),(1,3),(2,2)):
    raise SystemExit("transgression rank pair escaped certified envelope")

env=json.loads((ROOT/"finite-transgression-envelope.json").read_text())
finite=json.loads((ROOT/"finite-v4-hypercohomology.json").read_text())
cert={
  "schema":"STAGE33_03_FINITE_V4_TRANSGRESSION_RANKS_V1",
  "source_locks":{
    "finite_transgression_envelope_sha256":env["canonical_sha256"],
    "finite_v4_hypercohomology_sha256":finite["canonical_sha256"],
    "calculator":"same exact integral total complex [Div_D -> Pic] as finite H2 certificate",
  },
  "H1_V4_UPic":{"free_rank":0,"torsion_invariants":tors,"f2_dimension":h1dim},
  "H1_V4_unit_lattice":0,
  "PicU_V4_invariant_dimension_f2":2,
  "rank_d2_01":r01,
  "rank_d2_11":r11,
  "finite_transgression_rank_pair_exact":True,
  "absolute_kernel_character_terms_still_open":True,
  "next_exact_leaf":"L33-03-ABSOLUTE-N-CHARACTER-INFLATION-RESTRICTION-AND-d2_11",
  "br0b_all_primary_classes_accounted":False,
  "theorem_credit":False,
  "endpoint_credit":False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(ROOT/"finite-transgression-ranks.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
  "success":True,
  "H1_V4_UPic":f"(Z/2)^{h1dim}",
  "rank_d2_01":r01,
  "rank_d2_11":r11,
  "next_exact_leaf":cert["next_exact_leaf"],
  "certificate_sha256":cert["canonical_sha256"],
},indent=2,sort_keys=True))
