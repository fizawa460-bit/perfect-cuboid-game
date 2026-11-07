"""Family pencils: singular points of the strict transforms on the exceptional curves E_P, and members containing E_P.
For each node P: (a) members with ord_P >= oG + 1 (contain E_P beyond the family's generic order);
(b) critical points of the pencil on the blow-up charts, restricted to E_P (l = 0), base points removed."""
import glob, os
jobs = []
for f in sorted(glob.glob('famg/c_*.sing')):
    n = os.path.basename(f)[2:-5]
    src = open(f).read()
    head = src[:src.index('ideal BL = std(S + ideal(F0, F1));')]
    t = head + r'''
proc satl(ideal I) { def T = sat(I, ideal(var(8))); ideal R2; if (typeof(T) == "list") { R2 = T[1]; } else { R2 = T; } return(std(R2)); }
ideal NODES = std(S + minor(jacob(S), 4)); list NPL = minAssGTZ(NODES); int jn; int kk2; int jc; int jj2;
proc ordP2(poly F, ideal P) { int k = 0; int mm2; for (mm2 = 1; mm2 <= 8; mm2++) { if (size(reduce(F, satur(std(S + P^mm2), MX))) == 0) { k = mm2; } else { break; } } return(k); }
for (jn = 1; jn <= size(NPL); jn++) {
  ideal NP = std(NPL[jn]); int o0 = ordP2(F0, NP); int o1 = ordP2(F1, NP); int oG = o0; if (o1 < oG) { oG = o1; }
  // (a) members containing E_P beyond the generic order
  ideal JE = satur(std(S + NP^(oG + 1)), MX); poly r0 = reduce(F0, JE); poly r1 = reduce(F1, JE); string ra = "NONE";
  if (r0 == 0 && r1 == 0) { ra = "ALL"; } else { if (r1 == 0) { ra = "inf"; } else { if (r0 == 0) { ra = "0"; } else { number kq = leadcoef(r0) / leadcoef(r1); if (r0 - kq * r1 == 0) { ra = string(kq); } kill kq; } } }
  "NODEEXC", jn, " oG", oG, " member F0 - u F1 with u =", ra;
  // (b) chart: var(jc) = 1 at P
  jc = 0; for (kk2 = 1; kk2 <= 7; kk2++) { if (jc == 0) { if (dim(std(NP + ideal(var(kk2) - 1))) == 0) { jc = kk2; } } }
  ideal PT = std(NP + ideal(var(jc) - 1)); list pc; for (kk2 = 1; kk2 <= 7; kk2++) { poly rv = reduce(var(kk2), PT); if (rv == 0) { pc[kk2] = number(0); } else { pc[kk2] = leadcoef(rv); } kill rv; }
  for (jj2 = 1; jj2 <= 7; jj2++) { if (jj2 != jc) {
    ring RB = 10009, (w1,w2,w3,w4,w5,w6,w7,l), dp;
    list pcB = imap(R, pc); int jcB = jc; int jjB = jj2; int oGB = oG;
    ideal img; int kv; for (kv = 1; kv <= 7; kv++) { if (kv == jcB) { img[kv] = 1; } else { if (kv == jjB) { img[kv] = number(pcB[kv]) + l; } else { img[kv] = number(pcB[kv]) + l * var(kv); } } }
    map sbm = R, img;
    ideal XS = satl(sbm(S) + ideal(var(jcB), var(jjB))); int q3;
    poly G0; poly G1; if (oGB == 0) { G0 = sbm(F0); G1 = sbm(F1); } else {
      ideal I2 = XS; I2[size(XS) + 1] = l^oGB; int ig = size(XS) + 1;
      list dv0 = division(sbm(F0), I2); list dv1 = division(sbm(F1), I2);
      if (dv0[2][1] != 0 || dv1[2][1] != 0) { "DIVISION-REMAINDER-NONZERO"; }
      G0 = dv0[1][ig, 1]; G1 = dv1[1][ig, 1]; kill I2; kill ig; kill dv0; kill dv1; }
    list fv; for (kv = 1; kv <= 8; kv++) { if (kv != jcB && kv != jjB) { fv = insert(fv, var(kv), size(fv)); } }
    int ng = size(XS); matrix JM[ng + 2][6]; int a3; int b3;
    for (a3 = 1; a3 <= ng; a3++) { for (b3 = 1; b3 <= 6; b3++) { JM[a3, b3] = diff(XS[a3], fv[b3]); } }
    for (b3 = 1; b3 <= 6; b3++) { JM[ng + 1, b3] = diff(G0, fv[b3]); JM[ng + 2, b3] = diff(G1, fv[b3]); }
    ideal ZC = std(XS + minor(JM, 6) + ideal(l, G0 * G1) );
    ZC = std(XS + minor(JM, 6) + ideal(l));
    ideal BPt = std(XS + ideal(l, G0, G1));
    def LZ = sat(ZC, BPt); ideal ZC2; if (typeof(LZ) == "list") { ZC2 = std(LZ[1]); } else { ZC2 = std(LZ); } kill LZ;
    int dz = dim(ZC2);
    if (dz >= 0) {
      ring RS = 10009, (w1,w2,w3,w4,w5,w6,w7,l,s), dp; ideal Zs = imap(RB, ZC2) + ideal(imap(RB, G0) - s * imap(RB, G1));
      def LS = sat(std(Zs), ideal(imap(RB, G1))); ideal Zs2; if (typeof(LS) == "list") { Zs2 = std(LS[1]); } else { Zs2 = std(LS); } kill LS;
      ideal ELS = eliminate(Zs2, w1*w2*w3*w4*w5*w6*w7*l);
      "NODECRIT", jn, " chart", jjB, " dim", dz, " s-values (member F0 - s F1):"; ELS;
      if (dz == 0 && ELS[1] != 0) { list FA = factorize(ELS[1]); int f4; for (f4 = 2; f4 <= size(FA[1]); f4++) { ideal ZK = std(Zs2 + ideal(FA[1][f4]^(FA[2][f4] + 6))); "NODELEN", jn, " chart", jjB, " factor", FA[1][f4], " deg", deg(FA[1][f4]), " length", vdim(ZK); kill ZK; } kill FA; kill f4; }
      setring RB; kill RS; }
    kill ZC; kill BPt; kill ZC2; kill JM; kill fv; kill G0; kill G1; kill XS; kill sbm; kill img; kill kv; kill pcB; kill jcB; kill jjB; kill oGB; kill q3; kill a3; kill b3; kill ng; kill dz;
    setring R; kill RB; } }
  kill NP; kill o0; kill o1; kill oG; kill JE; kill r0; kill r1; kill ra; kill PT; kill pc; }
quit;
'''
    nm = f'n_{n}'
    open(f'famg/{nm}.sing', 'w', newline='\n').write(t)
    jobs.append(nm)
open('famg/njobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n')
print(len(jobs))
