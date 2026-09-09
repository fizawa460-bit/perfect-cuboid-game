SetColumns(0);

// Minimal exact reconstruction of the singular-point runtime used by
// Michael Stoll's Cuboids/cuboids.magma at commit
// 51233ed5ef2bf228fac9416c66db9adc0ebcaadd.
L<i,s> := ext<Rationals() | Polynomial([1,0,1]), Polynomial([-2,0,1])>;
Pr6<a1,a2,a3,b1,b2,b3,c> := ProjectiveSpace(L, 6);
eqns := [
    a1^2 + a2^2 - b3^2,
    a2^2 + a3^2 - b1^2,
    a1^2 + a3^2 - b2^2,
    a1^2 + a2^2 + a3^2 - c^2
];
S := Scheme(Pr6, eqns);
pts := Points(SingularSubscheme(S));
assert #pts eq 48;

normpts := [];
for k in [1..#pts] do
    v := Eltseq(pts[k]);
    j0 := 1;
    while v[j0] eq 0 do
        j0 +:= 1;
    end while;
    nv := [x/v[j0] : x in v];
    Append(~normpts, nv);
    printf "NODE|%o|%o\n", k-1, nv;
end for;

assert #normpts eq 48;
assert forall{normpts[j] ne normpts[k] : j,k in [1..48] | j lt k};
printf "COUNT|%o\n", #pts;
printf "UNIQUE|%o\n", #normpts;
print "STAGE32EX5_B_RUNTIME_POINTS_END";
