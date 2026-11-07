import os,sys
T=r'''list MA = minAssGTZ(Bp); int ia; int ib; int ic; int jj;
ideal NODES = std(S + minor(jacob(S), 4));
proc ordP(poly F, ideal P) { int k = 0; int mm2; for (mm2 = 1; mm2 <= 5; mm2++) { if (size(reduce(F, satur(std(S + P^mm2), MX))) == 0) { k = mm2; } else { break; } } return(k); }
proc satx(ideal I, ideal J) { def T2 = sat(I, J); ideal R3; if (typeof(T2) == "list") { R3 = T2[1]; } else { R3 = T2; } return(std(R3)); }
list QL; intvec QM; int nq = 0;
for (ia = 1; ia <= size(MA); ia++) { ideal QA = std(MA[ia]); if (dim(QA) == 2) { nq++; QL[nq] = QA; ideal RZq = satx(Bp, QA); QM[nq] = (mult(Bp) - mult(RZq)) div mult(QA); kill RZq; } kill QA; }
"COMPS", nq, " degrees/mults:"; for (ia = 1; ia <= nq; ia++) { "  comp", ia, " deg", mult(QL[ia]), " mult", QM[ia]; }
int bad = 0;
// off-node pairwise transversality and triple points
for (ia = 1; ia < nq; ia++) { for (ib = ia + 1; ib <= nq; ib++) { ideal W = satx(std(QL[ia] + QL[ib]), NODES);
  if (dim(W) > 0) { int lw = mult(W); int rw = mult(std(radical(W))); if (lw != rw) { "  OFFNODE non-transverse", ia, ib, lw, rw; bad++; }
    for (ic = ib + 1; ic <= nq; ic++) { ideal W3 = std(W + QL[ic]); if (dim(W3) > 0) { "  OFFNODE triple point", ia, ib, ic; bad++; } kill W3; } kill lw; kill rw; }
  kill W; } }
// off-node: b nonvanishing at off-node singular points of M (pairwise intersections) and on multiple comps
poly GB = F0; if (rank(coeffs(ideal(NN, F0), maxideal(mm))) < 2) { GB = F1; }
ideal IB = satx(std(S + ideal(GB)), Dc);
for (ia = 1; ia <= nq; ia++) { if (QM[ia] >= 2) { ideal WB = satx(std(QL[ia] + IB), NODES); if (dim(WB) > 0) { "  OFFNODE base point on multiple comp", ia; bad++; } kill WB; }
  for (ib = ia + 1; ib <= nq; ib++) { ideal WB2 = satx(std(QL[ia] + QL[ib] + IB), NODES); if (dim(WB2) > 0) { "  OFFNODE base point at crossing", ia, ib; bad++; } kill WB2; } }
// nodes
list NPL = minAssGTZ(NODES);
for (jj = 1; jj <= size(NPL); jj++) { ideal NP = std(NPL[jj]);
  string th = ""; int sm = 0; intvec thr; int nt = 0;
  for (ia = 1; ia <= nq; ia++) { if (size(reduce(QL[ia], NP)) == 0) { nt++; thr[nt] = ia; sm = sm + QM[ia]; th = th + " " + string(ia) + "x" + string(QM[ia]); } }
  int oN = ordP(NN, NP); int oG = ordP(F0 + 7*F1, NP); int e = oN - oG;
  if (nt > 0 || e > 0) {
    int xE = -2*e + sm; string tg = "";
    for (ia = 1; ia < nt; ia++) { for (ib = ia + 1; ib <= nt; ib++) { ideal W = std(QL[thr[ia]] + QL[thr[ib]]); ideal Wo = satx(W, NP); int ll = mult(W) - mult(Wo); if (dim(Wo) <= 0) { ll = mult(W); } tg = tg + " L(" + string(thr[ia]) + "," + string(thr[ib]) + ")=" + string(ll); if (ll != 1) { bad++; } kill W; kill Wo; kill ll; } }
    "  NODE", jj, " pdeg", mult(NP), " e", e, " comps", th, " x.E", xE, tg;
    if (xE < 0) { "  NEGATIVE x.E ??"; bad++; }
    if (xE > 0 && e >= 2) { "  base points on multiple E"; bad++; }
    if (xE > 0) { string lb = ""; int need = 0;
      for (ia = 1; ia <= nt; ia++) { ideal WB = std(QL[thr[ia]] + IB); ideal WBo = satx(WB, NP); int l2 = mult(WB) - mult(WBo); if (dim(WBo) <= 0) { l2 = mult(WB); } if (dim(WB) <= 0) { l2 = 0; }
        lb = lb + " LB(" + string(thr[ia]) + ")=" + string(l2);
        if ((QM[thr[ia]] >= 2 || e >= 1) && l2 >= 2) { need++; } kill WB; kill WBo; kill l2; }
      "    b-contact:", lb; if (need > 0) { "    B-THROUGH-SPECIAL-POINT"; bad++; } kill lb; kill need; }
    kill xE; kill tg; }
  kill NP; kill th; kill sm; kill thr; kill nt; kill oN; kill oG; kill e; }
if (bad == 0) { "NC-OK"; } else { "NC-BAD", bad; }
quit;
'''
names=[]
for f in sys.argv[1:]:
    s=open(f).read(); key='list MA = minAssGTZ(Bp);'
    n='nc_'+os.path.basename(f)[:-5]
    open('cnc/'+n+'.sing','w',newline='\n').write(s[:s.index(key)]+T); names.append(n)
open('cnc/jobs.txt','w',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
