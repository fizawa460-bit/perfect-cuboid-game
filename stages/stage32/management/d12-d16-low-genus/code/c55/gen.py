"""32R-74: e = 3 node analysis in the bad direction of a configuration Z (generalises c28 / c55).
usage: python c55/gen.py MEMBER(m16 name) OUTDIR "zcomps" "znodes" target
  zcomps: QL indices of the curve components of Z ; znodes: NPL indices of the E's of Z (target included)
Writes OUTDIR/a.sing (char p: W, W2, B*, chart limits, r = 3 discriminant + genera)."""
import sys, os, re
mem, out, zc, zn, tg = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split()], [int(x) for x in sys.argv[4].split()], int(sys.argv[5])
os.makedirs(out, exist_ok=True)
s = open(f'm16/{mem}.sing').read()
head = s[:s.index('// find the member(s) in J')]
zcs = ', '.join(str(x) for x in zc)
zns = ', '.join(str(x) for x in zn)
body = r'''
ideal RR; for (kk = 1; kk <= HH; kk++) { RR[kk] = reduce(FL[kk], J); } matrix CM = coeffs(RR, maxideal(mm)); module SZ = syz(CM); vector vv; int js;
for (js = 1; js <= size(SZ); js++) { if (deg(SZ[js]) == 0) { vv = SZ[js]; } }
poly NN = 0; for (kk = 1; kk <= HH; kk++) { NN = NN + number(vv[kk]) * FL[kk]; }
proc gpow(ideal G, int c) { if (c == 0) { return(ideal(1)); } return(satur(satur(std(S + G^c), NODES), MX)); }
ideal B = std(S + ideal(NN)); ideal Bp = satur(B, Dc); list QL; intvec QM; intvec DM; int nq = 0; int ia; int jj;
list MA = minAssGTZ(Bp); for (ia = 1; ia <= size(MA); ia++) { ideal QA = std(MA[ia]); if (dim(QA) == 2) { nq++; QL[nq] = QA; ideal RZq = satur(Bp, QA); QM[nq] = (mult(Bp) - mult(RZq)) div mult(QA); DM[nq] = 0; kill RZq; } kill QA; }
ideal BBg2 = std(S + ideal(FL[1]));
for (js = 1; js <= size(DLc); js++) { int exn = (mult(B) - mult(satur(B, DL[js]))) div mult(DL[js]); int exg = (mult(BBg2) - mult(satur(BBg2, DL[js]))) div mult(DL[js]); if (exn > exg) { nq++; QL[nq] = std(DL[js]); QM[nq] = exn - exg; DM[nq] = exg; } kill exn; kill exg; }
"COMPS", nq; for (ia = 1; ia <= nq; ia++) { "COMP", ia, mult(QL[ia]), QM[ia], DM[ia]; }
list NPL = minAssGTZ(NODES); intvec oGv;
for (jj = 1; jj <= size(NPL); jj++) { ideal NP = std(NPL[jj]); int oG = 99; for (kk = 1; kk <= HH; kk++) { int o3 = ordP(FL[kk], NP); if (o3 < oG) { oG = o3; } kill o3; } oGv[jj] = oG; kill NP; kill oG; }
intvec zc = ZCS; intvec zn = ZNS; int tg = TG; int q2;
ideal JW = ideal(1); for (q2 = 1; q2 <= size(zc); q2++) { JW = intersect(JW, gpow(QL[zc[q2]], DM[zc[q2]] + 1)); }
for (q2 = 1; q2 <= size(zn); q2++) { JW = intersect(JW, satur(std(S + std(NPL[zn[q2]])^(oGv[zn[q2]] + 1)), MX)); }
JW = std(JW); ideal JW2 = std(intersect(JW, satur(std(S + std(NPL[tg])^(oGv[tg] + 2)), MX)));
ideal R1; ideal R2; for (kk = 1; kk <= HH; kk++) { R1[kk] = reduce(FL[kk], JW); R2[kk] = reduce(FL[kk], JW2); }
int dW = HH - rank(coeffs(R1, maxideal(mm))); int dW2 = HH - rank(coeffs(R2, maxideal(mm)));
"dimW", dW, " dimW2", dW2, " (with NN; nets need dimW = dimW2 = 2)";
module S2 = syz(coeffs(R2, maxideal(mm))); poly BS = 0; for (js = 1; js <= size(S2); js++) { if (deg(S2[js]) == 0) { vector w2 = S2[js]; poly cand = 0; for (kk = 1; kk <= HH; kk++) { cand = cand + number(w2[kk]) * FL[kk]; } if (rank(coeffs(ideal(cand, NN), maxideal(mm))) == 2) { BS = cand; } kill w2; kill cand; } }
if (BS == 0) { "NO-BSTAR"; quit; }
poly B3 = 0; for (kk = 1; kk <= HH; kk++) { if (reduce(FL[kk], JW) != 0 && B3 == 0) { B3 = FL[kk]; } }
"ord at target: NN", ordP(NN, std(NPL[tg])), " B*", ordP(BS, std(NPL[tg])), " B3", ordP(B3, std(NPL[tg])), " oG", oGv[tg];
// chart at the target node
ideal NPt = std(NPL[tg]); int jc = 0; for (kk = 1; kk <= 7; kk++) { if (jc == 0) { if (dim(std(NPt + ideal(var(kk) - 1))) == 0) { jc = kk; } } }
ideal PT = std(NPt + ideal(var(jc) - 1)); list pc; for (kk = 1; kk <= 7; kk++) { poly rv = reduce(var(kk), PT); if (rv == 0) { pc[kk] = number(0); } else { pc[kk] = leadcoef(rv); } kill rv; }
"chart var", jc;
ring RL = 10009, (u1,u2,u3,u4,u5,u6,u7,l,n), dp;
list pcL = imap(R, pc); int jcL = jc;
ideal img1; ideal img3; int kv; for (kv = 1; kv <= 7; kv++) { if (kv == jcL) { img1[kv] = 1; img3[kv] = 1; } else { img1[kv] = number(pcL[kv]) + l * var(kv); img3[kv] = number(pcL[kv]) + l^3 * var(kv); } }
map sb = R, img1; map sb3 = R, img3;
ideal UJ = var(jcL);
proc satl(ideal I) { def T = sat(I, ideal(l)); ideal R2; if (typeof(T) == "list") { R2 = T[1]; } else { R2 = T; } return(std(R2)); }
ideal SL = satl(sb(S) + UJ); ideal SL3 = satl(sb3(S) + UJ);
proc limitc(ideal SLx, poly G) { ideal Jx = satl(SLx + ideal(G)); return(std(Jx + ideal(l))); }
ideal L3 = limitc(SL, sb(NN) + l * sb(BS) + n * l^3 * sb(B3));
ideal La = limitc(SL, sb(NN) + l^2 * sb(BS) + n * l^3 * sb(B3));
ideal Lb = limitc(SL3, sb3(NN) + l^2 * sb3(BS) + n * l^8 * sb3(B3));
proc genuine(ideal L) { list MP = minAssGTZ(L); ideal G = ideal(1); int i; int ng = 0; for (i = 1; i <= size(MP); i++) { ideal Q = std(MP[i]);
    // drop components that are linear in the u's (rulings of the tangent cone, from fixed D-curves through the node)
    ideal Qn = std(subst(Q, n, 7)); int lin = 1; int k; for (k = 1; k <= size(Qn); k++) { if (deg(Qn[k]) > 1) { lin = 0; } } kill k; kill Qn;
    if (!lin) { G = intersect(G, Q); ng++; } kill Q; kill lin; }
  "   genuine components", ng; return(std(G)); }
"r<3:"; ideal Ga = genuine(La); "r=3:"; ideal G3 = genuine(L3); "r>3:"; ideal Gb = genuine(Lb);
ideal Ga7 = subst(Ga, n, 7); ideal Gb7 = subst(Gb, n, 7); ideal G37 = subst(G3, n, 7); ideal G3s = G3;
ring RC = 10009, (u1,u2,u3,u4,u5,u6,u7), dp;
ideal CA = std(imap(RL, Ga7)); ideal CB = std(imap(RL, Gb7)); ideal C3 = std(imap(RL, G37));
"RES r<3 genus", genus(CA), " comps", size(minAssGTZ(CA));
"RES r>3 genus", genus(CB), " comps", size(minAssGTZ(CB));
"RES r=3 generic genus", genus(C3), " comps", size(minAssGTZ(C3));
setring RL;
// singular fibres of the r = 3 family: Jacobian w.r.t. u1..u7
matrix JJ[size(G3s)][7]; int a2; int b2; for (a2 = 1; a2 <= size(G3s); a2++) { for (b2 = 1; b2 <= 7; b2++) { JJ[a2, b2] = diff(G3s[a2], var(b2)); } }
ideal SGF = std(G3s + minor(JJ, 6)); ideal EL = eliminate(SGF, u1*u2*u3*u4*u5*u6*u7); "r=3 discriminant", string(EL);
poly ELn = 0; for (a2 = 1; a2 <= size(EL); a2++) { if (EL[a2] != l && EL[a2] != 0) { ELn = EL[a2]; } }
if (ELn != 0) { list FA = factorize(ELn); int f2; for (f2 = 1; f2 <= size(FA[1]); f2++) { poly ff = FA[1][f2];
   if (deg(ff) == 1 && ff != n) { number n0 = -leadcoef(subst(ff, n, 0)) / leadcoef(ff); ideal Gs = subst(G3s, n, n0); ring RD = 10009, (u1,u2,u3,u4,u5,u6,u7), dp; ideal CD = std(imap(RL, Gs)); "RES r=3 special nu", imap(RL, n0), " genus", genus(CD), " comps", size(minAssGTZ(CD)); setring RL; kill RD; kill n0; kill Gs; }
   if (deg(ff) > 1) { "RES r=3 special factor of degree", deg(ff), " (needs an extension field):", string(ff); } kill ff; } }
quit;
'''
body = body.replace('ZCS', zcs).replace('ZNS', zns).replace('TG', str(tg))
open(f'{out}/a.sing', 'w', newline='\n').write(head + body)
print('written', out)
