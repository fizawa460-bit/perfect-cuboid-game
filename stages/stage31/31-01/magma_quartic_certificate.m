SetSeed(20260823);
SetQuitOnError(true);

v1, v2, v3 := GetVersion();
print "STAGE31_MAGMA_QUARTIC_CERTIFICATE_BEGIN";
print "MAGMA_VERSION:", v1, v2, v3;

Q := [ Integers() | 5, 40, 90, -40, 5 ];
P := [ Integers() | 1, 10 ];
print "MODEL: U^2 = 5*Y^4 + 40*Y^3 + 90*Y^2 - 40*Y + 5";
print "BASE_POINT:", P;

// IntegralQuarticPoints supplies a complete set of integral x-values with one
// representative for the hyperelliptic sign U -> -U.  We restore both signs below.
pts := IntegralQuarticPoints(Q, P);
Sort(~pts);
print "INTEGRAL_QUARTIC_REPRESENTATIVE_COUNT:", #pts;
print "INTEGRAL_QUARTIC_REPRESENTATIVES:", pts;

signed := [];
target := [];
for R in pts do
    yy := Integers() ! R[1];
    uu := Integers() ! R[2];
    Append(~signed, [ yy, uu ]);
    if uu ne 0 then
        Append(~signed, [ yy, -uu ]);
    end if;
    assert uu mod 10 eq 0;
    Append(~target, [ yy, uu div 10 ]);
    if uu ne 0 then
        Append(~target, [ yy, -(uu div 10) ]);
    end if;
end for;
Sort(~signed);
Sort(~target);
print "ALL_SIGNED_INTEGRAL_QUARTIC_U_POINTS_COUNT:", #signed;
print "ALL_SIGNED_INTEGRAL_QUARTIC_U_POINTS:", signed;
print "C_ANOM_INTEGRAL_POINTS_COUNT:", #target;
print "C_ANOM_INTEGRAL_POINTS:", target;

E := EllipticCurve([ 0, 0, 0, -275, 1750 ]);
G, mwmap, rank_proved, full_group_proved := MordellWeilGroup(E);
print "MW_ABSTRACT_GROUP:", G;
print "MW_RANK_PROVED:", rank_proved;
print "MW_FULL_GROUP_PROVED:", full_group_proved;
print "MW_GENERATORS:", Generators(E);
T, tmap := TorsionSubgroup(E);
print "TORSION_GROUP:", T;

// Magma returns one representative of each +/- pair here; restore signs independently.
epts := IntegralPoints(E);
print "E_ANOM_INTEGRAL_POINT_REPRESENTATIVE_COUNT:", #epts;
print "E_ANOM_INTEGRAL_POINT_REPRESENTATIVES:", epts;

print "STAGE31_MAGMA_QUARTIC_CERTIFICATE_END";
