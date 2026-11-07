import sys
A_OLD = 'execute("ring RN = 10009,(a1,a2,a3,b1,b2,b3,c," + PARS + "),dp;");'
A_NEW = '''// 32R-91 net v3: Z1 = sat(Z, base) is replaced by sat(Z, h), h = one random member of the net (3x faster).
// sat(Z, h) differs from sat(Z, base) only by associated primes of Z1 containing h.  Z1 has no embedded points
// (assumption already made in v2), so these are components of V(Z) off the base: (i) graphs over a component of the
// jacobian curve SIG -> checked: h is a nonzerodivisor mod SIG; (ii) {p} x (line or plane) with p off the base: then
// grad S has rank < 4 (p a node) or rank J7 <= 5 -> checked: h does not vanish at the nodes off the base nor at the
// rank <= 5 points off the base.
// If a check fails, the old three-saturation step is used.
intvec HC = 4931, 7717, 2269, 6113; poly HB = 0; for (kk = 1; kk <= HH; kk++) { HB = HB + HC[kk] * FL[kk]; }  // fixed coefficients keep the random stream of v2
int okh = 1; int t3 = timer;
if (size(reduce(sat1(SIG, HB), SIG)) != 0) { okh = 0; "V3-CHECK-FAIL jacobian curve component in h = 0"; }
ideal RD0 = std(SIG + minor(J7, 6)); ideal RD = sat1(RD0, FI[1]); for (kk = 2; kk <= HH; kk++) { RD = intersect(RD, sat1(RD0, FI[kk])); } RD = std(RD); kill RD0;
if (dim(std(RD + ideal(HB))) > 0) { okh = 0; "V3-CHECK-FAIL rank-drop point in h = 0"; }
ideal NOB = sat1(NODES, FI[1]); for (kk = 2; kk <= HH; kk++) { NOB = intersect(NOB, sat1(NODES, FI[kk])); } NOB = std(NOB);
if (dim(std(NOB + ideal(HB))) > 0) { okh = 0; "V3-CHECK-FAIL node off base in h = 0"; }
"v3 checks: ok", okh, " rank-drop points dim", dim(RD), " time", timer - t3;
''' + A_OLD
B_OLD = '''ideal Z1 = sat1(Z, FIN[1]);
for (kk = 2; kk <= HH; kk++) { Z1 = intersect(Z1, sat1(Z, FIN[kk])); }
Z1 = std(Z1);'''
B_NEW = '''ideal Z1;
if (okh == 1) { Z1 = sat1(Z, imap(R, HB)); "v3: single saturation by a random member"; }
else { Z1 = sat1(Z, FIN[1]); for (kk = 2; kk <= HH; kk++) { Z1 = intersect(Z1, sat1(Z, FIN[kk])); } }
Z1 = std(Z1);'''
for f in sys.argv[1:]:
    s = open(f).read()
    if 'net v3' in s: continue
    assert s.count(A_OLD) == 1 and s.count(B_OLD) == 1, f
    open(f, 'w').write(s.replace(A_OLD, A_NEW).replace(B_OLD, B_NEW))
    print('patched', f)
