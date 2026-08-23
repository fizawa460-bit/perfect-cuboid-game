// Stage32-01 exact pilot: replace raw rank-63 norm-ball enumeration by the
// cone of Picard classes having nonnegative intersection with every frozen
// known irreducible curve and exceptional divisor.  The caller reconstructs
// PicL, HinPicL and gensinPicL from the source-locked Picard-core artifact.

printf "STAGE32_POLYHEDRAL_PILOT_BEGIN\n";
assert Dimension(PicL) eq 64;
assert #gensinPicL eq 140;
assert (HinPicL, HinPicL) eq 16;

TL := ToricLattice(64);
TM := Dual(TL);

// If x is a Picard coordinate row, then x.G_j is the intersection with the
// j-th frozen known class.  A genuinely new integral irreducible curve is
// distinct from every known curve and therefore has nonnegative intersection
// with all 140 of them.
known_forms := [
    TM![Integers()!(PicL.j, gensinPicL[k]) : j in [1..64]]
    : k in [1..140]
];
KnownDualCone := ConeWithInequalities({f : f in known_forms});
hform := TM![Integers()!(PicL.j, HinPicL) : j in [1..64]];

P2 := Polyhedron(KnownDualCone, hform, 2);
compact := IsPolytope(P2);
printf "STAGE32_POLY|KNOWN_FILTER_COUNT|%o\n", #known_forms;
printf "STAGE32_POLY|LEVEL2_COMPACT|%o\n", compact;
printf "STAGE32_POLY|CONE_DIMENSION|%o\n", Dimension(KnownDualCone);
printf "STAGE32_POLY|LEVEL2_DIMENSION|%o\n", Dimension(P2);
if compact then
  printf "STAGE32_POLY|LEVEL2_VERTEX_COUNT|%o\n", NumberOfVertices(P2);
end if;

// No raw rank-63 CloseVectors process is started by this pilot.
printf "STAGE32_POLY|RAW_63D_CVP_STARTED|false\n";
printf "STAGE32_POLYHEDRAL_PILOT_END\n";
