/* checks18 / tower18.gp -- exact checks for ANSWER-18 (request 18).
   (a) the degree-10 and degree-25 towers over Q(i) that are not of elliptic type (counterexamples to the strict claim Q);
   (b) degree 6, type 2 o 3: the 3-isogenies of the curves E_S for every Galois-stable branch set S, and the predicted
       F_p counts N_p for the four data 021133, 201133, 110233, 112033;
   (c) the curve with j = 128 (non-square 4-subsets of B) has no isogeny of odd prime degree l <= 13 over Q(i).
   Usage: gp -q tower18.gp < /dev/null > tower18.out */
default(parisizemax, 2000000000);
ii = Mod(t, t^2 + 1);
nfi = nfinit(t^2 + 1);

/* ---------- (a) ---------- */
f1 = ((3 - 4*ii)*x^5 + (10 + 20*ii)*x^3 - 25*x)/(25*x^4 - (10 + 20*ii)*x^2 - (3 - 4*ii));     /* x((2+i)P) on y^2 = x^3 - x, checks14/cm14.gp */
f2 = ii*subst(f1, x, -ii*x);                                                                   /* the same for the square {0, oo, i, -i} */
g2 = ii*(x^2 - 1)/(x^2 + 1);                                                                   /* degree 2, critical values -i (x = 0) and i (x = oo) */
/* ramification of p over b: returns [number of double points, number of simple points, largest multiplicity] */
ram(p, b) = { my(n = max(poldegree(numerator(p)), poldegree(denominator(p))), N, fa, dd = 0, ss = 0, mx = 0);
  N = if(b === oo, denominator(p), numerator(p - b));
  fa = nffactor(nfi, lift(N));
  for(j = 1, matsize(fa)[1], my(e = fa[j, 2], d = poldegree(fa[j, 1])); mx = max(mx, e); if(e == 2, dd += d); if(e == 1, ss += d));
  my(m = n - poldegree(N)); if(m == 1, ss++); if(m == 2, dd++); mx = max(mx, m);
  [dd, ss, mx] };
report(nm, p) = { my(n = max(poldegree(numerator(p)), poldegree(denominator(p))), B = [ii, -ii, 1, -1, 0, oo], v = vector(6, k, ram(p, B[k])), a, o, mx, ncv);
  a = vector(6, k, v[k][1]); o = vecsum(vector(6, k, v[k][2])); mx = vecmax(vector(6, k, v[k][3])); ncv = #select(z -> z > 0, a);
  print(nm, ": degree ", n, ", data (i,-i,1,-1,0,oo) = ", a, ", sum = ", vecsum(a), " (2n-2 = ", 2*n - 2, "), |O| = ", o, " (2n+4 = ", 2*n + 4, "), largest multiplicity ", mx,
        ", critical values ", ncv, if(vecsum(a) == 2*n - 2 && o == 2*n + 4 && mx <= 2, "  -> slack 0", "  -> NOT slack 0"), if(ncv <= 4, ", elliptic type", ", not of elliptic type")) };
print("(a) towers over Q(i)");
print("  f1(i) = ", lift(subst(f1, x, ii)), ", f1(-i) = ", lift(subst(f1, x, -ii)), ", f1(1) = ", lift(subst(f1, x, 1)), ", f1(-1) = ", lift(subst(f1, x, -1)));
report("  f1 = x((2+i)P)", f1);
report("  f2 = i f1(-i x)", f2);
report("  p10 = f1 o g2", subst(f1, x, g2));
report("  p25 = f1 o f2", subst(f1, x, f2));
report("  f1 o f1 (same square)", subst(f1, x, f1));
print("    the same over Q:");
{ my(E = ellinit([-1, 0]), v = ellxn(E, 3)); f3 = v[1]/v[2] };                 /* x([3]P) on y^2 = x^3 - x */
f3b = I*0 + ii*subst(f3, x, -ii*x);                                             /* x([3]P) for the square {0, oo, i, -i}: y^2 = x^3 + x */
gq = (x^2 - 1)/(2*x);                                                           /* degree 2 over Q, critical values i (x = i) and -i (x = -i) */
print("  f3b has rational coefficients: ", poldegree(lift(numerator(f3b)), t) <= 0 && poldegree(lift(denominator(f3b)), t) <= 0, ";  f3(i) = ", lift(subst(f3*Mod(1, t^2+1), x, ii)));
report("  f3 = x([3]P)", f3*Mod(1, t^2 + 1));
report("  p18 = f3 o gq", subst(f3, x, gq)*Mod(1, t^2 + 1));
report("  p81 = f3 o f3b", subst(f3, x, f3b));

/* ---------- (b) ---------- */
/* quartic q(x) = a x^4 + b x^3 + c x^2 + d x + e  ->  Jacobian y^2 = x^3 - 27 I x - 27 J */
jac(q) = { my(a = polcoeff(q, 4), b = polcoeff(q, 3), c = polcoeff(q, 2), d = polcoeff(q, 1), e = polcoeff(q, 0), I4, J4);
  I4 = 12*a*e - 3*b*d + c^2; J4 = 72*a*c*e + 9*b*c*d - 27*a*d^2 - 27*e*b^2 - 2*c^3; [-27*I4, -27*J4] };
jinv(AB) = 1728*4*AB[1]^3/(4*AB[1]^3 + 27*AB[2]^2);
psi3(AB) = 3*x^4 + 6*AB[1]*x^2 + 12*AB[2]*x - AB[1]^2;       /* 3-division polynomial of y^2 = x^3 + A x + B: its roots <-> subgroups of order 3 */
pat(q) = { my(AB = jac(q), fa = nffactor(nfi, lift(psi3(AB)))); [lift(jinv(AB)), apply(poldegree, fa[, 1]~)] };
print(); print("(b) degree 6, type 2 o 3: branch sets S of the cubic g, stable under Gal(Qbar/Q(i)) (after scaling);");
print("    [j(E_S), degrees over Q(i) of the factors of the 3-division polynomial]; a factor of degree 1 = a 3-isogeny over Q(i)");
print("  f = x^2 (critical values 0, oo), S = union of two +- pairs:");
{ my(pr = [x^2 - 1, x^2 + 1, x^2 - ii, x^2 + ii], nm = ["+-1", "+-i", "+-zeta", "+-zeta^3"]);
  for(u = 1, 4, for(v = u + 1, 4, print("    ", nm[u], ", ", nm[v], ": ", pat(pr[u]*pr[v])))) }
print("  f = x^2/(x^2-1) (critical values 0, 1), S = union of two +- pairs:");
{ my(pr = [x^2 - 1, x^2 - 1/2, x^2 - (1 - ii)/2, x^2 - (1 + ii)/2], nm = ["over oo", "over -1", "over i", "over -i"]);
  for(u = 1, 4, for(v = u + 1, 4, print("    ", nm[u], ", ", nm[v], ": ", pat(pr[u]*pr[v])))) }
print("  f = x^2, the four exceptional data:");
QA = (x^2 + ii)*(x - 1)*(x - ii); QB = (x^2 + ii)*(x - 1)*(x + ii);            /* 021133: S = {+-sqrt(-i), 1, i}, {+-sqrt(-i), 1, -i} */
QA2 = (x^2 - ii)*(x - 1)*(x - ii); QB2 = (x^2 - ii)*(x - 1)*(x + ii);          /* 201133 */
QC = (x^2 - 1/2)*(x^2 - x + 1/2); QD = (x^2 + 1/2)*(x^2 - x + 1/2);            /* 110233 and 112033 (after scaling by zeta +- zeta^3) */
print("    021133 A: ", pat(QA)); print("    021133 B: ", pat(QB)); print("    201133 A: ", pat(QA2)); print("    201133 B: ", pat(QB2));
print("    110233/112033 C: ", pat(QC)); print("    110233/112033 D: ", pat(QD));
/* Galois groups of the quartics over Q (C, D are defined over Q) and over Q(i) by the norm polynomial */
print("    C: 3-division quartic over Q factors as ", apply(poldegree, factor(lift(psi3(jac(QC))))[, 1]~), ", D: ", apply(poldegree, factor(lift(psi3(jac(QD))))[, 1]~));
{ print("    C: Galois group of the quartic over Q ", polgalois(lift(psi3(jac(QC)))), ";  D: the two quadratic factors over Q have discriminants (squarefree part) ",
      apply(g -> core(poldisc(g)), factor(lift(psi3(jac(QD))))[, 1]~)) }
print("    C: field of one root ", polredbest(lift(psi3(jac(QC)))), ", subfields ", apply(v -> v[1], nfsubfields(polredbest(lift(psi3(jac(QC)))))));
{ my(fa = nffactor(nfi, lift(psi3(jac(QA))))); print("    021133 A: discriminants of the two quadratic factors over Q(i): ", apply(g -> lift(poldisc(g)), fa[, 1]~)) }
/* predicted N_p: number of roots of the 3-division quartics mod the two primes above p */
cnt(q, p, r) = { my(P0 = subst(lift(psi3(jac(q))), t, r), P = P0 * Mod(1, p)); if(poldegree(P) < 4 || poldegree(gcd(P, deriv(P))) > 0, return(-1)); #polrootsmod(P0, p) };
print("  predicted N_p (r = the root of -1 used for i; two columns = the two choices):");
print("    p : 021133 (A+B) | 201133 (A+B) | 110233 = 112033 (C+D)");
{ forprime(p = 13, 200, if(p % 4 == 1, my(r = lift(sqrt(Mod(-1, p))), s = "");
  s = Str("    ", p, " (mod 8 = ", p % 8, ", mod 3 = ", p % 3, "): ");
  s = Str(s, cnt(QA, p, r) + cnt(QB, p, r), ",", cnt(QA, p, p - r) + cnt(QB, p, p - r), " | ", cnt(QA2, p, r) + cnt(QB2, p, r), ",", cnt(QA2, p, p - r) + cnt(QB2, p, p - r), " | ", cnt(QC, p, r) + cnt(QD, p, r));
  s = Str(s, "    [A: ", cnt(QA, p, r), ",", cnt(QA, p, p - r), "  B: ", cnt(QB, p, r), ",", cnt(QB, p, p - r), "  C: ", cnt(QC, p, r), "  D: ", cnt(QD, p, r), "]");
  print(s))) }

/* ---------- (c) ---------- */
print(); print("(c) j = 128 (non-square 4-subsets of B): roots of the modular polynomial Phi_l(128, Y) in Q(i)");
{ forprime(l = 3, 13, my(P = subst(polmodular(l), x, 128), fa = nffactor(nfi, P)); print("  l = ", l, ": degrees of the factors over Q(i) ", apply(poldegree, fa[, 1]~))) }
quit
