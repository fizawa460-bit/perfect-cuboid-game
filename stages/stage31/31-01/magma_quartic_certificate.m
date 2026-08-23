SetSeed(20260823);

Q := [ Integers() | 5, 40, 90, -40, 5 ];
P := [ Integers() | 1, 10 ];

print "STAGE31_MAGMA_QUARTIC_CERTIFICATE_BEGIN";
print "MODEL: U^2 = 5*Y^4 + 40*Y^3 + 90*Y^2 - 40*Y + 5";
print "BASE_POINT:", P;

pts := IntegralQuarticPoints(Q, P);
Sort(~pts);
print "ALL_INTEGRAL_QUARTIC_U_POINTS_COUNT:", #pts;
print "ALL_INTEGRAL_QUARTIC_U_POINTS:", pts;

target := [];
for R in pts do
    if R[2] mod 10 eq 0 then
        Append(~target, [ R[1], R[2] div 10 ]);
    end if;
end for;
Sort(~target);
print "C_ANOM_INTEGRAL_POINTS_COUNT:", #target;
print "C_ANOM_INTEGRAL_POINTS:", target;

E := EllipticCurve([ 0, 0, 0, -275, 1750 ]);
epts := IntegralPoints(E);
print "E_ANOM_INTEGRAL_POINTS_COUNT:", #epts;
print "E_ANOM_INTEGRAL_POINTS:", epts;

print "STAGE31_MAGMA_QUARTIC_CERTIFICATE_END";
