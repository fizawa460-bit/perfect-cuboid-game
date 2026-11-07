"""D-point check for a net job e_<i>_<t>.sing: members G_q (q = (s0:u:v)) whose residual R_q = G_q - D is singular at a
smooth point p of S lying on one D-curve Gamma (mult m in D) and on no other D-curve: mult_p(G_q) >= m + 2.
Tested with words of length <= m+1 in three random tangent fields (5x5 cross products of the quadric gradients); two
independent random triples, union of results.  Output: finitely many q (or a positive-dim family) per curve.
usage: python mkdchk.py <i> <t>  -> d_<i>_<t>.sing"""
import re, sys
i, t = sys.argv[1], sys.argv[2]; NL = chr(10)
src = open(f"e_{i}_{t}.sing").read()
k = src.index("ideal Iall = "); pre = src[:src.index(NL, src.index("int HH = "))] + NL
names = re.findall(r"\b(G\d+p?)\b", src[k:src.index(NL, k)])
curves = [(n[:-1], 2) if n.endswith("p") else (n, 1) for n in names]
sd = re.search(r'system\("random", (\d+)\)', src).group(1)
body = f'''
ideal SS = std(S); ideal NFL = simplify(reduce(Lsys, SS), 2);
system("random", {sd});
int ii; int jj; int kk;
list FL; for (kk = 1; kk <= HH; kk++) {{ poly Ft = 0; for (ii = 1; ii <= ncols(NFL); ii++) {{ Ft = Ft + random(1,9999)*NFL[ii]; }} FL[kk] = Ft; kill Ft; }}
if (HH != 3) {{ "ONLY-HH3"; quit; }}
ideal NOD = std(S + minor(jacob(S), 4));
matrix JS[4][7] = jacob(S);
// cofactor fields: for 5-subset J, D_J(f) = det(rows JS, grad f | cols J)
list FIELDS; int nf = 0; intvec JJ; int a; int b; int c2; int d; int e;
for (a = 1; a <= 7; a++) {{ for (b = a+1; b <= 7; b++) {{ for (c2 = b+1; c2 <= 7; c2++) {{ for (d = c2+1; d <= 7; d++) {{ for (e = d+1; e <= 7; e++) {{
  JJ = a,b,c2,d,e; matrix V[1][7]; int s;
  for (s = 1; s <= 5; s++) {{ matrix Mm[4][4]; int r2; int cc; int col = 0;
    for (cc = 1; cc <= 5; cc++) {{ if (cc != s) {{ col++; for (r2 = 1; r2 <= 4; r2++) {{ Mm[r2, col] = JS[r2, JJ[cc]]; }} }} }}
    V[1, JJ[s]] = (-1)^(5 + s) * det(Mm); kill Mm; kill r2; kill cc; kill col; }}
  nf++; FIELDS[nf] = V; kill V; kill s; }} }} }} }} }}
"tangent fields", nf;
proc applyF(matrix V, poly f) {{ poly g = 0; int j; for (j = 1; j <= 7; j++) {{ g = g + V[1, j] * diff(f, var(j)); }} return(g); }}
list OUT;
'''
for cname, m in curves:
    body += f'''
"== curve {cname} mult {m}";
ideal OTH = {"intersect(" + ",".join(c for c, _ in curves if c != cname) + ")" if len(curves) > 1 else "ideal(1)"};
ideal ALLQ;
for (int tr = 1; tr <= 2; tr++) {{
  system("random", 500 + tr);
  list TF; for (kk = 1; kk <= 3; kk++) {{ matrix W[1][7]; for (ii = 1; ii <= nf; ii++) {{ W = W + random(1,99) * FIELDS[ii]; }} TF[kk] = W; kill W; }}
  // words of length <= {m+1} applied to each basis section: rows of the 3-column matrix
  list LV; for (kk = 1; kk <= 3; kk++) {{ LV[kk] = list(FL[kk]); }}
  list CUR = LV; int lv;
  for (lv = 1; lv <= {m+1}; lv++) {{
    list NXT; for (kk = 1; kk <= 3; kk++) {{ list Lk; int w; int x;
      for (w = 1; w <= size(CUR[kk]); w++) {{ for (x = 1; x <= 3; x++) {{ Lk = insert(Lk, applyF(TF[x], CUR[kk][w]), size(Lk)); }} }}
      NXT[kk] = Lk; LV[kk] = LV[kk] + Lk; kill Lk; kill w; kill x; }}
    CUR = NXT; kill NXT; }}
  kill lv;
  "  operators", size(LV[1]);
  ring RQ = 10009,(a1,a2,a3,b1,b2,b3,c,s0,u,v),dp;
  ideal Z = imap(R, {cname}) + imap(R, S);
  list LVQ = imap(R, LV);
  for (ii = 1; ii <= size(LVQ[1]); ii++) {{ Z = Z + ideal(s0 * LVQ[1][ii] + u * LVQ[2][ii] + v * LVQ[3][ii]); }}
  int t0 = timer; Z = std(Z);
  Z = satur(Z, imap(R, NOD)); Z = satur(Z, imap(R, OTH)); Z = satur(Z, ideal(a1,a2,a3,b1,b2,b3,c)); Z = satur(Z, ideal(s0,u,v));
  matrix TM[3][7]; for (kk = 1; kk <= 3; kk++) {{ for (jj = 1; jj <= 7; jj++) {{ TM[kk, jj] = imap(R, TF)[kk][1, jj]; }} }}
  Z = satur(Z, minor(TM, 3));
  "  incidence on curve: dim", dim(Z), " time", timer - t0;
  ideal EQ = eliminate(Z, a1*a2*a3*b1*b2*b3*c);
  setring R; ring PQ = 10009,(s0,u,v),dp; ideal Q = std(imap(RQ, EQ));
  "  bad members: projective dim", dim(Q) - 1, " degree", mult(Q);
  if (dim(Q) == 1) {{ list PQL = minAssGTZ(Q); for (kk = 1; kk <= size(PQL); kk++) {{ "   bad", kk, " deg", mult(std(PQL[kk])), ":", PQL[kk]; }} kill PQL; }}
  if (dim(Q) >= 2) {{ "  POSITIVE-DIM-BAD-FAMILY", Q; }}
  setring R; kill PQ; kill RQ; kill TF; kill LV; kill CUR;
}}
kill tr; kill OTH; kill ALLQ;
'''
body = body.replace("satur(", "satur(")
open(f"d_{i}_{t}.sing", "w", newline=NL).write(pre + body + "quit;" + NL)
print("curves", curves)
