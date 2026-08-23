// Stage32-01 Picard preflight. This file is concatenated after an exact
// source-locked subset of the pinned Cuboids/cuboids.magma computation.

printf "STAGE32_PREFLIGHT_BEGIN\n";

assert Dimension(PicL) eq 64;
assert (HinPicL, HinPicL) eq 16;
assert Dimension(LHp) eq 63;
assert #pts eq 48;
assert Rank(pmPic) eq 64;
assert bdim eq #gensinPicL;

printf "STAGE32_INVARIANT|PICARD_RANK|%o\n", Dimension(PicL);
printf "STAGE32_INVARIANT|H2|%o\n", (HinPicL, HinPicL);
printf "STAGE32_INVARIANT|HPERP_RANK|%o\n", Dimension(LHp);
printf "STAGE32_INVARIANT|NODE_COUNT|%o\n", #pts;
printf "STAGE32_INVARIANT|KNOWN_FILTER_COUNT|%o\n", bdim;
printf "STAGE32_INVARIANT|HPERP_DETERMINANT|%o\n", Determinant(LHp);

function Stage32Data(d, genus)
  assert IsEven(d);
  assert genus in [0,1];
  r := GCD(d, 16);
  m := 16 div r;
  n := d div r;
  C0 := qPic((d div 2)*Big.1);
  y0 := m*C0 - n*HinPic;
  assert (PicL!y0, HinPicL) eq 0;
  base := LHp!Eltseq(y0 @@ HperptoPic);
  delta := genus eq 0 select 2 else 0;
  BQ := m^2 * (Rationals()!(d^2)/16 + d + delta);
  assert Denominator(BQ) eq 1;
  B := Integers()!BQ;
  return r, m, n, base, B;
end function;

r2,m2,n2,b2,B2 := Stage32Data(2,0);
r4,m4,n4,b4,B4 := Stage32Data(4,1);
assert r2 eq 2 and m2 eq 8 and n2 eq 1;
assert r4 eq 4 and m4 eq 4 and n4 eq 1;
assert b2 eq b4;
assert B2 eq 272;
assert B4 eq 80;
printf "STAGE32_REGRESSION|D2_BASE_D4_BASE_EQUAL|true\n";
printf "STAGE32_REGRESSION|G0_D2_BOUND|%o\n", B2;
printf "STAGE32_REGRESSION|G1_D4_BOUND|%o\n", B4;

row_count := 0;
for genus in [0,1] do
  dmin := genus eq 0 select 2 else 4;
  dmax := genus eq 0 select 176 else 192;
  for d in [dmin..dmax by 2] do
    r,m,n,base,B := Stage32Data(d,genus);
    row_count +:= 1;
    printf "STAGE32_ROW|%o|%o|%o|%o|%o|%o|%o\n",
           genus, d, r, m, n, B, Norm(base);
  end for;
end for;
assert row_count eq 183;
printf "STAGE32_INVARIANT|WINDOW_ROW_COUNT|%o\n", row_count;

// Export an exact machine-readable core so later Stage32 search experiments do
// not have to spend the online-Magma gateway budget recomputing intersections.
printf "STAGE32_CORE_H|%o\n", Eltseq(HinPicL);
for j in [1..64] do
  printf "STAGE32_CORE_PMPIC|%o|%o\n", j, Eltseq(pmPic[j]);
end for;
for j in [1..bdim] do
  printf "STAGE32_CORE_KNOWN|%o|%o\n", j, Eltseq(gensinPicL[j]);
end for;
printf "STAGE32_CORE_EXPORT_COMPLETE|true\n";

printf "STAGE32_AUT_PHASE_EXECUTED|false\n";
printf "STAGE32_RAW_63D_CVP_STARTED|false\n";
printf "STAGE32_PREFLIGHT_END\n";
