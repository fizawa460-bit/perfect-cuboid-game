# 32R-75 §3.5 (lighter check): for one extension-field factor h(s) of a family, work over F_p(a), h(a) = 0, and
# test directly whether the member Y_a (moving part) is smooth: off the nodes by the Jacobian criterion on S,
# on the exceptional curves E_P in the blow-up charts (strict transform, local complete intersection of the chart).
# Usage: python mksx.py SRC.sing FACTORINDEX OUT.sing   (SRC = an e1_/e2_/xe1_/xe2_ job; FACTORINDEX 1-based in HF)
import re, sys
src, fi, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
T = open(src, encoding='utf-8').read().replace('\r', '')
pre = T.split('ring RS = 10009, (a1,a2,a3,b1,b2,b3,c,s), dp;')[0]
hf = re.search(r'list HF = (.*?); int k;', T).group(1)
facs = [f.strip() for f in hf.split(',')]
mp = facs[fi - 1].replace('s', 'a')
tail = r'''
list NPL = minAssGTZ(NODES); int nnp = size(NPL);
ring RA = (10009,a),(a1,a2,a3,b1,b2,b3,c),dp; minpoly = MPOLY;
"FACTOR", minpoly;
ideal S = imap(R, S); ideal Dc = imap(R, Dc); ideal FX = imap(R, FIXI); poly F0 = imap(R, F0); poly F1 = imap(R, F1);
ideal NODES = imap(R, NODES); list NPL = imap(R, NPL); ideal MX = maxideal(1);
proc sA(ideal I, ideal Q) { def T = sat(I, Q); ideal R2; if (typeof(T) == "list") { R2 = T[1]; } else { R2 = T; } return(std(R2)); }
ideal IY = sA(std(S + ideal(F0 - a * F1)), Dc); IY = sA(IY, FX); IY = sA(IY, MX);
"YDIM", dim(IY), " YDEG", mult(IY);
ideal GY = minbase(IY); "YGENS", ncols(GY);
matrix JS = jacob(S); int ig; int ir; int jv; ideal SG;
for (ig = 1; ig <= ncols(GY); ig++) { matrix M[5][7]; for (ir = 1; ir <= 4; ir++) { for (jv = 1; jv <= 7; jv++) { M[ir, jv] = JS[ir, jv]; } }
  for (jv = 1; jv <= 7; jv++) { M[5, jv] = diff(GY[ig], var(jv)); } SG = SG + minor(M, 5); kill M; }
ideal ZS = sA(sA(std(S + IY + SG), NODES), MX);
"SINGOFF dim", dim(ZS), " deg", mult(ZS);
int jn; int kk2; int jc; int jj2; int nthru = 0;
for (jn = 1; jn <= nnp; jn++) {
  ideal NP = std(NPL[jn]);
  if (size(reduce(IY, NP)) == 0) { nthru++;
    jc = 0; for (kk2 = 1; kk2 <= 7; kk2++) { if (jc == 0) { if (dim(std(NP + ideal(var(kk2) - 1))) == 0) { jc = kk2; } } }
    ideal PT = std(NP + ideal(var(jc) - 1)); list pc; for (kk2 = 1; kk2 <= 7; kk2++) { poly rv = reduce(var(kk2), PT); if (rv == 0) { pc[kk2] = number(0); } else { pc[kk2] = leadcoef(rv); } kill rv; }
    for (jj2 = 1; jj2 <= 7; jj2++) { if (jj2 != jc) {
      ring RB = (10009,a),(w1,w2,w3,w4,w5,w6,w7,l),dp; minpoly = MPOLY;
      list pcB = imap(RA, pc); int jcB = jc; int jjB = jj2;
      ideal img; int kv; for (kv = 1; kv <= 7; kv++) { if (kv == jcB) { img[kv] = 1; } else { if (kv == jjB) { img[kv] = number(pcB[kv]) + l; } else { img[kv] = number(pcB[kv]) + l * var(kv); } } }
      map sbm = RA, img;
      ideal SB = sbm(S); ideal XT; ideal LT; int i4;
      for (i4 = 1; i4 <= 4; i4++) { XT[i4] = SB[i4] / l; if (XT[i4] * l != SB[i4]) { "CHART-DIVISION-ERROR"; } LT[i4] = subst(XT[i4], l, 0); }
      module SZL = syz(LT); int i0 = 0; vector cv; int js;
      for (js = 1; js <= size(SZL); js++) { if (i0 == 0 && deg(SZL[js]) == 0) { cv = SZL[js]; for (i4 = 1; i4 <= 4; i4++) { if (i0 == 0 && cv[i4] != 0) { i0 = i4; } } } }
      if (i0 == 0) { "CHART-NO-RELATION", jn, jjB; }
      poly T4 = 0; for (i4 = 1; i4 <= 4; i4++) { T4 = T4 + cv[i4] * XT[i4]; }
      poly T4b = T4 / l; if (T4b * l != T4) { "CHART-T4-ERROR"; }
      ideal XS4; int t4 = 0; for (i4 = 1; i4 <= 4; i4++) { if (i4 != i0) { t4++; XS4[t4] = XT[i4]; } } XS4[4] = T4b;
      XS4 = XS4 + ideal(var(jcB), var(jjB));
      def LY = sat(std(sbm(IY) + XS4), ideal(l)); ideal YB; if (typeof(LY) == "list") { YB = std(LY[1]); } else { YB = std(LY); } kill LY;
      ideal YE = std(YB + ideal(l));
      if (dim(YE) >= 0) {
        list fv; for (kv = 1; kv <= 8; kv++) { if (kv != jcB && kv != jjB) { fv = insert(fv, var(kv), size(fv)); } }
        ideal SGB; int a3; int b3; int g3;
        for (g3 = 1; g3 <= ncols(YB); g3++) { if (YB[g3] != 0) { matrix MB[5][6];
          for (a3 = 1; a3 <= 4; a3++) { for (b3 = 1; b3 <= 6; b3++) { MB[a3, b3] = diff(XS4[a3], fv[b3]); } }
          for (b3 = 1; b3 <= 6; b3++) { MB[5, b3] = diff(YB[g3], fv[b3]); } SGB = SGB + minor(MB, 5); kill MB; } }
        ideal ZE = std(YB + XS4 + SGB + ideal(l));
        "SINGE node", jn, " chart", jjB, " Y.E-pts length", vdim(YE), " sing dim", dim(ZE), " sing length", vdim(ZE);
        kill fv; kill SGB; kill a3; kill b3; kill g3; kill ZE; }
      setring RA; kill RB; } }
    kill PT; kill pc; }
  kill NP; }
"NODES-THROUGH", nthru;
"DONE";
quit;
'''.replace('MPOLY', mp)
open(out, 'w', encoding='utf-8', newline='\n').write(pre + tail)
print(out, mp)
