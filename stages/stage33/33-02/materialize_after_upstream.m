// Stage33-02 exact BR0A materialization after the pinned Testa--Stoll core.
// Emits the complete 72 -> Pic(Sbar) map, integral kernel, boundary pairing,
// quotient data, and the two frozen Galois permutations.

assert assigned Pic;
assert assigned Big;
assert assigned Cs;
assert assigned C1s;
assert assigned pts;
assert assigned qPic;
assert assigned ccPic;
assert assigned ctPic;
assert assigned permcc;
assert assigned permct;
assert assigned pairingmat;

side_inds := [1..24];
exc_inds := [#Cs + j : j in [1..48]];
boundary_inds := side_inds cat exc_inds;
assert #boundary_inds eq 72;

boundary_gens := [qPic(Big.j) : j in boundary_inds];
DivD := RSpace(Integers(), 72);
phiD := hom<DivD -> Pic | boundary_gens>;
UnitDivRelations := Kernel(phiD);
BoundaryImage := Image(phiD);
PicU, qPicU := quo<Pic | BoundaryImage>;

bpermcc := [Position(boundary_inds, permcc[j]) : j in boundary_inds];
bpermct := [Position(boundary_inds, permct[j]) : j in boundary_inds];
assert 0 notin bpermcc;
assert 0 notin bpermct;

actPic := func<v, M | Pic!(Vector(Integers(), Eltseq(v))*M)>;
assert forall{v : v in Basis(BoundaryImage) | actPic(v, ccPic) in BoundaryImage};
assert forall{v : v in Basis(BoundaryImage) | actPic(v, ctPic) in BoundaryImage};

printf "STAGE33_02_BEGIN\n";
printf "BOUNDARY_COMPONENT_COUNT=%o\n", #boundary_inds;
printf "PIC_RANK=%o\n", #Basis(Pic);
printf "BOUNDARY_IMAGE_RANK=%o\n", #Basis(BoundaryImage);
printf "UNIT_KERNEL_RANK=%o\n", #Basis(UnitDivRelations);
printf "PICU_INVARIANTS=%o\n", Invariants(PicU);
printf "BOUNDARY_INDICES=%o\n", boundary_inds;
printf "BOUNDARY_PERM_CC=%o\n", bpermcc;
printf "BOUNDARY_PERM_CT=%o\n", bpermct;

for j in [1..72] do
  printf "PHI_ROW_%o=%o\n", j, Eltseq(boundary_gens[j]);
end for;
for j in [1..#Basis(UnitDivRelations)] do
  printf "KER_ROW_%o=%o\n", j, Eltseq(Basis(UnitDivRelations)[j]);
end for;
for j in [1..72] do
  printf "PAIR_ROW_%o=%o\n", j,
    [pairingmat[boundary_inds[j], boundary_inds[k]] : k in [1..72]];
end for;
for j in [1..#Basis(Pic)] do
  printf "PICU_GEN_%o=%o\n", j, Eltseq(qPicU(Pic.j));
end for;

printf "GALOIS_BOUNDARY_STABLE=true\n";
printf "STAGE33_02_END\n";
