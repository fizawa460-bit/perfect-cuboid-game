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

for k in [1..#pts] do
    v := Eltseq(pts[k]);
    j0 := 1;
    while v[j0] eq 0 do
        j0 +:= 1;
    end while;
    nv := [x/v[j0] : x in v];
    printf "NODE|%o|", k-1;
    for j in [1..7] do
        printf "%o", nv[j];
        if j lt 7 then
            printf ",";
        end if;
    end for;
    printf "\n";
end for;

printf "COUNT|%o\n", #pts;
print "STAGE32EX5_B_RUNTIME_POINTS_END";
