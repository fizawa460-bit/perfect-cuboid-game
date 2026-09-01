SetSeed(20260901);
SetQuitOnError(true);

v1, v2, v3 := GetVersion();
QQ := Rationals();
print "STAGE34_01_MAGMA_MW_SATURATION_BEGIN";
print "MAGMA_VERSION:", v1, v2, v3;
print "SEMANTICS: Saturation(points) returns generators of the saturation of the given points in the Mordell-Weil group";
print "LOGIC: Paper-C exact rank + full saturation of an equal-rank source subgroup gives the full free Mordell-Weil lattice";

procedure CheckFiber(label, qnum, qden, expected_rank, srcxy)
    qq := QQ!qnum / qden;
    E := EllipticCurve([ QQ | 0, 1 + qq^2, 0, qq^2, 0 ]);
    source_pts := [ E![ pair[1], pair[2], 1 ] : pair in srcxy ];
    T, tmap := TorsionSubgroup(E);

    print "FIBER_BEGIN:", label;
    print "Q:", qq;
    print "EXPECTED_SOURCE_LOCKED_RANK:", expected_rank;
    print "SOURCE_POINTS:", source_pts;
    print "TORSION_INVARIANTS:", Invariants(T);

    src_independent, src_rel := IsLinearlyIndependent(source_pts);
    print "SOURCE_INDEPENDENT_MOD_TORSION:", src_independent;
    assert src_independent;

    sat := Saturation(source_pts : TorsionFree := true);
    print "SATURATED_SOURCE_BASIS:", sat;
    assert #sat eq expected_rank;

    sat_independent, sat_rel := IsLinearlyIndependent(sat);
    print "SATURATED_BASIS_INDEPENDENT_MOD_TORSION:", sat_independent;
    assert sat_independent;

    source_free_coords := [];
    for j in [1..#source_pts] do
        independent, rel := IsLinearlyIndependent([ source_pts[j] ] cat sat);
        assert not independent;
        v := [ Integers()!z : z in Eltseq(rel) ];
        g := 0;
        for z in v do
            g := Gcd(g, Abs(z));
        end for;
        assert g ne 0;
        v := [ z div g : z in v ];
        assert Abs(v[1]) eq 1;
        fseq := [ -(v[k+1] div v[1]) : k in [1..expected_rank] ];
        Append(~source_free_coords, fseq);
        print "SOURCE_RELATION:", j, v;
        print "SOURCE_FREE_COORD:", j, fseq;
    end for;

    flat := &cat source_free_coords;
    M := Matrix(Integers(), expected_rank, expected_rank, flat);
    idx := Abs(Determinant(M));
    print "SOURCE_FREE_COORD_MATRIX:", M;
    print "SOURCE_FREE_INDEX_IN_SATURATION:", idx;
    print "SOURCE_SPANS_SATURATED_FREE_PART:", idx eq 1;
    print "FIBER_END:", label;
end procedure;

if target eq "20/21" then
    CheckFiber("20/21", 20, 21, 1, [ [ QQ | -45/49, 10/343 ] ]);
elif target eq "80/39" then
    CheckFiber("80/39", 80, 39, 1, [ [ QQ | -160/39, 1760/1521 ] ]);
elif target eq "24/7" then
    CheckFiber("24/7", 24, 7, 1, [ [ QQ | -75/7, 510/49 ] ]);
elif target eq "84/13" then
    CheckFiber("84/13", 84, 13, 1, [ [ QQ | 17787/169, 216678/169 ] ]);
elif target eq "48/55" then
    CheckFiber("48/55", 48, 55, 1, [ [ QQ | -24/25, 24/275 ] ]);
elif target eq "20/99" then
    CheckFiber("20/99", 20, 99, 1, [ [ QQ | -20/27, 980/2673 ] ]);
elif target eq "60/11" then
    CheckFiber("60/11", 60, 11, 2, [
        [ QQ | -180/11, 7020/121 ],
        [ QQ | -300/11, 5100/121 ]
    ]);
else
    error "unknown target fiber";
end if;

print "STAGE34_01_MAGMA_MW_SATURATION_END";
