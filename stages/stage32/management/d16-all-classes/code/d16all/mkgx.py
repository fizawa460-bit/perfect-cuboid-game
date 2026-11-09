"""Exact geometric genus of the plane model for the h0 = 1 jobs whose fast bound was <= 1 (t_1967, t_2090, t_2091):
same member and projections as gfast/tail_fast_v2.sing up to the birational plane image Fp; check irreducibility over
F_p; move the line at infinity off the singular locus; g = (d-1)(d-2)/2 - sum of deltaLoc over ALL singular points.
(Variable names chosen not to clash with normal.lib.)  usage (from stoll/): python d16all/mkgx.py t_1967 ..."""
import sys
T = open('gfast/tail_fast_v2.sing').read()
k = T.index("if (size(Fq) != 1"); k = T.index("\n", k) + 1
ADD = '''// exact genus of the (birational) plane image: g = (d-1)(d-2)/2 - sum of delta over ALL singular points
list FF = factorize(Fp[1]); if (size(FF[1]) - 1 >= 2 || FF[2][size(FF[1])] >= 2) { "PLANE-IMAGE-REDUCIBLE"; quit; }
poly fh = Fp[1]; int dd = deg(fh);
int tries; int okc = 0; ideal SJ = std(ideal(fh, diff(fh,w0), diff(fh,w1), diff(fh,w2)));
for (tries = 1; tries <= 10; tries++) { poly lz = random(1,9999)*w0 + random(1,9999)*w1 + random(1,9999)*w2; if (dim(std(SJ + ideal(lz))) <= 0) { okc = 1; break; } kill lz; }
if (okc == 0) { "NO-GOOD-CHART"; quit; }
ring A9 = 10009,(x,y),dp;
setring P2; number c0 = leadcoef(subst(subst(lz,w1,0),w2,0)); number c1 = leadcoef(subst(subst(lz,w0,0),w2,0)); number c2 = leadcoef(subst(subst(lz,w0,0),w1,0));
string sub = "(1 - (" + string(c1) + ")*x - (" + string(c2) + ")*y)/(" + string(c0) + ")";
setring A9; execute("map ph9 = P2, " + sub + ", x, y;");
poly fa = ph9(fh); ideal Ja = std(ideal(fa, diff(fa,x), diff(fa,y)));
"plane degree", dd, " affine sing: dim", dim(Ja), " vdim", vdim(Ja);
list PR = minAssGTZ(Ja); int dsumxq = 0; int kqx; list DLqx;
for (kqx = 1; kqx <= size(PR); kqx++) { DLqx = deltaLoc(fa, PR[kqx]); dsumxq = dsumxq + DLqx[1]; }
"singular point groups", size(PR), " delta sum (exact)", dsumxq;
"EXACT GENUS (plane model, over F_p-bar)", (dd-1)*(dd-2) div 2 - dsumxq;
quit;
'''
for j in sys.argv[1:]:
    s = open(f'd16all/h1/{j}.sing').read(); assert T in s
    open(f'd16all/h1/gx_{j}.sing', 'w', newline='\n').write(s.replace(T, T[:k] + ADD))
    print('gx', j)
