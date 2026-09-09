SetColumns(0);

// Exact reconstruction of the singular-point runtime and the 92 known-curve
// incidence fingerprints used by Michael Stoll's Cuboids/cuboids.magma at
// commit 51233ed5ef2bf228fac9416c66db9adc0ebcaadd.
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

C1s :=    [Curve(S, [a1, a2+e1*b3, a3+e2*b2, b1+e3*c]) : e1,e2,e3 in [1,-1]]
      cat [Curve(S, [a2, a3+e1*b1, a1+e2*b3, b2+e3*c]) : e1,e2,e3 in [1,-1]]
      cat [Curve(S, [a3, a1+e1*b2, a2+e2*b1, b3+e3*c]) : e1,e2,e3 in [1,-1]]
      cat [Curve(S, [c, i*a1+e1*b1, i*a2+e2*b2, i*a3+e3*b3]) : e3,e2,e1 in [1,-1]];
C2s :=    [Curve(S, [b1, i*a2+e1*a3, a1+e2*c]) : e1,e2 in [1,-1]]
      cat [Curve(S, [b2, i*a3+e1*a1, a2+e2*c]) : e1,e2 in [1,-1]]
      cat [Curve(S, [b3, i*a1+e1*a2, a3+e2*c]) : e1,e2 in [1,-1]];
C3s :=    [Curve(S, [a1+e1*a2, s*a1+e2*b3, b1+e3*b2]) : e1,e2,e3 in [1,-1]]
      cat [Curve(S, [a2+e1*a3, s*a2+e2*b1, b2+e3*b3]) : e1,e2,e3 in [1,-1]]
      cat [Curve(S, [a3+e1*a1, s*a3+e2*b2, b3+e3*b1]) : e1,e2,e3 in [1,-1]]
      cat [Curve(S, [i*a1+e1*c, i*b2+e2*b3, i*s*a1+e3*b1]) : e3,e2,e1 in [1,-1]]
      cat [Curve(S, [i*a2+e1*c, i*b3+e2*b1, i*s*a2+e3*b2]) : e3,e2,e1 in [1,-1]]
      cat [Curve(S, [i*a3+e1*c, i*b1+e2*b2, i*s*a3+e3*b3]) : e3,e2,e1 in [1,-1]];
Cs := C1s cat C2s cat C3s;
assert #Cs eq 92;
Cpts := [{pt : pt in pts | pt in C} : C in Cs];

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
    printf "|";
    for j in [1..#Cs] do
        printf "%o", pts[k] in Cpts[j] select 1 else 0;
    end for;
    printf "\n";
end for;

printf "COUNT|%o\n", #pts;
printf "CURVES|%o\n", #Cs;
print "STAGE32EX5_B_RUNTIME_POINTS_END";
