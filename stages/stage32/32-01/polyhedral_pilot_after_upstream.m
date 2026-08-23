// Stage32-01 exact pilot: replace raw rank-63 norm-ball enumeration by the
// cone of Picard classes having nonnegative intersection with every frozen
// known irreducible curve and exceptional divisor.  This file is evaluated
// only after the pinned Testa--Stoll Picard setup.

printf "STAGE32_POLYHEDRAL_PILOT_BEGIN\n";
assert Dimension(PicL) eq 64;
assert bdim eq #gensinPicL;
assert bdim eq #Cs + #pts;
assert #pts eq 48;

TL := ToricLattice(64);
TM := Dual(TL);

// In Picard basis coordinates v=(v_j), the form v |-> v.G has these
// coefficients.  Every new integral irreducible curve distinct from all
// frozen known curves must satisfy all 140 inequalities v.G >= 0.
known_forms := [
    TM![Integers()!(PicL.j, gensinPicL[k]) : j in [1..64]]
    : k in [1..bdim]
];
KnownDualCone := ConeWithInequalities({f : f in known_forms});
hform := TM![Integers()!(PicL.j, HinPicL) : j in [1..64]];

P2 := Polyhedron(KnownDualCone, hform, 2);
compact := IsPolytope(P2);
printf "STAGE32_POLY|KNOWN_FILTER_COUNT|%o\n", #known_forms;
printf "STAGE32_POLY|LEVEL2_COMPACT|%o\n", compact;
assert compact;
printf "STAGE32_POLY|CONE_DIMENSION|%o\n", Dimension(KnownDualCone);
printf "STAGE32_POLY|LEVEL2_DIMENSION|%o\n", Dimension(P2);
printf "STAGE32_POLY|LEVEL2_VERTEX_COUNT|%o\n", NumberOfVertices(P2);

// Exact low-degree regression against the published numerical exclusions.
// Known negative-self-intersection curves themselves are intentionally not
// points of this cone because they fail their own nonnegative intersection
// inequality; this cone is the search space for genuinely new curves.
time pts2 := Points(KnownDualCone, hform, 2);
cands2m4 := [
    PicL!Eltseq(p) : p in pts2
    | (v,v) eq -4 where v := PicL!Eltseq(p)
];
printf "STAGE32_POLY|LEVEL2_LATTICE_POINTS|%o\n", #pts2;
printf "STAGE32_POLY|LEVEL2_SELFINT_M4|%o\n", #cands2m4;
assert IsEmpty(cands2m4);

time pts4 := Points(KnownDualCone, hform, 4);
cands4m4 := [
    PicL!Eltseq(p) : p in pts4
    | (v,v) eq -4 where v := PicL!Eltseq(p)
];
printf "STAGE32_POLY|LEVEL4_LATTICE_POINTS|%o\n", #pts4;
printf "STAGE32_POLY|LEVEL4_SELFINT_M4|%o\n", #cands4m4;
assert IsEmpty(cands4m4);

printf "STAGE32_POLYHEDRAL_PILOT_END\n";
