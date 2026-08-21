// Stage29-02f boundary-module probe.
//
// Usage: run/load the immutable Testa--Stoll verification file first:
//   MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd
//   Cuboids/cuboids.magma
// Then load this file in the same Magma session.
//
// This probe does not compute Brauer groups.  It extracts the exact physical
// boundary lattice and checks Galois stability so R29-BR0A/B can be executed
// on certified matrices.

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

// First 24 C1s = eight conics in each of a1=0,a2=0,a3=0.
side_inds := [1..24];
// All exceptional curves are represented by the 48 singular-point generators.
exc_inds := [#Cs + j : j in [1..48]];
boundary_inds := side_inds cat exc_inds;
assert #boundary_inds eq 72;

boundary_gens := [qPic(Big.j) : j in boundary_inds];
BoundaryPic := sub<Pic | boundary_gens>;

// Full divisor lattice on geometric boundary components.
DivD := RSpace(Integers(), 72);
phiD := hom<DivD -> Pic | boundary_gens>;
UnitDivRelations := Kernel(phiD);
BoundaryImage := Image(phiD);
PicU, qPicU := quo<Pic | BoundaryImage>;

printf "Boundary geometric components: %o\n", #boundary_inds;
printf "Boundary image basis size: %o\n", #Basis(BoundaryImage);
printf "Principal boundary-relation basis size: %o\n", #Basis(UnitDivRelations);
printf "Pic(Ubar) invariants: %o\n", Invariants(PicU);

// The full known Galois permutations preserve the physical boundary set.
bpermcc := [Position(boundary_inds, permcc[j]) : j in boundary_inds];
bpermct := [Position(boundary_inds, permct[j]) : j in boundary_inds];
assert 0 notin bpermcc;
assert 0 notin bpermct;

// Check the image sublattice is stable under the Picard Galois matrices.
actPic := func<v, M | Pic!(Vector(Integers(), Eltseq(v))*M)>;
assert forall{v : v in Basis(BoundaryImage) | actPic(v, ccPic) in BoundaryImage};
assert forall{v : v in Basis(BoundaryImage) | actPic(v, ctPic) in BoundaryImage};

printf "Boundary is stable under complex conjugation and sqrt(2)-conjugation.\n";
printf "R29-BR0A extraction preflight PASS.\n";
