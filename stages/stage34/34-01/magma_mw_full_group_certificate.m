SetSeed(20260901);
SetQuitOnError(true);

v1, v2, v3 := GetVersion();
QQ := Rationals();
print "STAGE34_01_MAGMA_MW_CERTIFICATE_BEGIN";
print "MAGMA_VERSION:", v1, v2, v3;
print "SEMANTICS: MordellWeilGroup rank_proved/full_group_proved are the documented proof-status booleans";

procedure CheckFiber(label, qnum, qden, expected_rank, srcxy)
    qq := QQ!qnum / qden;
    E := EllipticCurve([ QQ | 0, 1 + qq^2, 0, qq^2, 0 ]);
    source_pts := [ E![ pair[1], pair[2], 1 ] : pair in srcxy ];

    print "FIBER_BEGIN:", label;
    print "Q:", qq;
    print "EXPECTED_RANK:", expected_rank;
    print "SOURCE_POINTS:", source_pts;

    G, mwmap, rank_proved, full_group_proved := MordellWeilGroup(E : Effort := 2, HeightBound := 100);
    inv := Invariants(G);
    free_positions := [ i : i in [1..#inv] | inv[i] eq 0 ];
    free_rank := #free_positions;
    T, tmap := TorsionSubgroup(E);

    print "MW_INVARIANTS:", inv;
    print "MW_RANK:", free_rank;
    print "MW_RANK_PROVED:", rank_proved;
    print "MW_FULL_GROUP_PROVED:", full_group_proved;
    print "MW_GENERATORS:", [ mwmap(G.i) : i in [1..Ngens(G)] ];
    print "TORSION_INVARIANTS:", Invariants(T);
    assert rank_proved;
    assert free_rank eq expected_rank;

    if full_group_proved then
        source_coords := [];
        source_free_coords := [];
        for j in [1..#source_pts] do
            a := source_pts[j] @@ mwmap;
            assert mwmap(a) eq source_pts[j];
            seq := Eltseq(a);
            fseq := [ seq[i] : i in free_positions ];
            Append(~source_coords, seq);
            Append(~source_free_coords, fseq);
        end for;
        print "SOURCE_MW_COORDS:", source_coords;
        print "SOURCE_FREE_COORDS:", source_free_coords;
        assert #source_free_coords eq expected_rank;
        flat := &cat source_free_coords;
        M := Matrix(Integers(), expected_rank, expected_rank, flat);
        idx := Abs(Determinant(M));
        print "SOURCE_FREE_COORD_MATRIX:", M;
        print "SOURCE_FREE_INDEX:", idx;
        print "SOURCE_SPANS_FULL_FREE_PART:", idx eq 1;
    else
        print "SOURCE_MW_COORDS: UNAVAILABLE_FULL_GROUP_NOT_PROVED";
        print "SOURCE_FREE_INDEX: UNAVAILABLE_FULL_GROUP_NOT_PROVED";
        print "SOURCE_SPANS_FULL_FREE_PART: false";
    end if;

    print "FIBER_END:", label;
end procedure;

CheckFiber("20/21", 20, 21, 1, [ [ QQ | -45/49, 10/343 ] ]);
CheckFiber("80/39", 80, 39, 1, [ [ QQ | -160/39, 1760/1521 ] ]);
CheckFiber("24/7", 24, 7, 1, [ [ QQ | -75/7, 510/49 ] ]);
CheckFiber("84/13", 84, 13, 1, [ [ QQ | 17787/169, 216678/169 ] ]);
CheckFiber("48/55", 48, 55, 1, [ [ QQ | -24/25, 24/275 ] ]);
CheckFiber("20/99", 20, 99, 1, [ [ QQ | -20/27, 980/2673 ] ]);
CheckFiber("60/11", 60, 11, 2, [
    [ QQ | -180/11, 7020/121 ],
    [ QQ | -300/11, 5100/121 ]
]);

print "STAGE34_01_MAGMA_MW_CERTIFICATE_END";
