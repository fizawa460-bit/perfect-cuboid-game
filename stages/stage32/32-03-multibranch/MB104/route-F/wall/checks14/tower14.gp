/* checks14 / tower14.gp -- request 14: search for an odd "isogeny piece" over Q on top of a 2-tower.
   A slack-0 map f over Q (critical values in B = {0, oo, 1, -1, i, -i}, simple critical points) is extended by
     (a) a degree-2 piece g branched at a Galois-stable pair of O(f)  (all Q-forms w^2 = d q(x), d in TW, with a
         rational point), giving f o g of twice the degree;
     (b) an odd isogeny piece: a Galois-stable 4-subset S of O(f) such that the elliptic curve y^2 = s(x)
         (s = the quartic with roots S) has a rational isogeny of odd prime degree l; this would give a slack-0 map
         f o g over Q of degree l * deg f.
   The script lists every (f, S) of type (b) up to tower depth DEPTH.  Usage: gp -q tower14.gp > tower14.out */
default(parisize, 800000000);
TW = [1, -1, 2, -2, 3, -3, 6, -6];
DEPTH = 3;
/* simple-root part of f^{-1}(B): list of irreducible factors over Q (f is first moved so that oo is generic) */
generic(f) = { my(k = 0, h, v);
  while(1, k++; h = subst(f, x, (k*x + 1)/(x - k - 1));
    if(poldegree(numerator(h)) == poldegree(denominator(h)) && poldegree(numerator(h)'*denominator(h) - numerator(h)*denominator(h)') == 2*poldegree(numerator(h)) - 2,
      my(c = pollead(numerator(h))/pollead(denominator(h))); if(c != 0 && c != 1 && c != -1 && c^2 != -1, return(h)))) };
ofac(f) = { my(L = List(), pols, F);
  pols = [numerator(f), denominator(f), numerator(f - 1), numerator(f + 1), numerator(f^2 + 1)];
  for(i = 1, #pols, F = factor(pols[i]);
    for(j = 1, matsize(F)[1], if(F[j, 2] == 1, listput(L, F[j, 1]), if(F[j, 2] != 2, error("not slack 0")))));
  Vec(L) };
check0(f) = { my(n = poldegree(numerator(f)), O = ofac(f)); if(vecsum(apply(poldegree, O)) != 2*n + 4, error("slack ", f)); O };
/* degree-2 piece with critical values the roots of the quadratic q, Q-form w^2 = d q(x) */
piece2(q, d) = { my(c = polcoef(q, 0), b = polcoef(q, 1), a = polcoef(q, 2), G, s, P);
  G = [d*a, d*b/2, 0; d*b/2, d*c, 0; 0, 0, -1];      /* d(aX^2 + bXZ + cZ^2) - W^2 */
  s = qfsolve(G); if(type(s) != "t_COL", return(0));
  P = qfparam(G, s) * [x^2, x, 1]~;                   /* [X, Z, W] as quadratic polynomials in x */
  if(P[2] == 0, return(0)); P[1]/P[2] };
subsets4(O) = { my(L = List(), m = #O, dg = apply(poldegree, O));
  forsubset(m, s, my(v = Vec(s)); if(#v > 0 && vecsum(vector(#v, k, dg[v[k]])) == 4, listput(L, vecprod(vector(#v, k, O[v[k]])))));
  Vec(L) };
oddisog(s) = { my(E, M, r = 1);
  E = ellinit(ellfromeqn(y^2 - s)); if(#E == 0, return(0));
  M = ellisomat(E, , 1)[2];
  for(i = 1, #M~, for(j = 1, #M, my(dd = M[i, j], o = dd/2^valuation(dd, 2)); r = max(r, o)));
  r };
level = [x]; hits = 0; tested = 0;
{ for(dep = 0, DEPTH,
    my(nxt = List());
    for(k = 1, #level, if(k % 10 == 0, printf("  .. depth %d map %d/%d  t=%d ms
", dep, k, #level, gettime())); my(f = generic(level[k]), O = check0(f), n = poldegree(numerator(f)), S4 = subsets4(O));
      for(t = 1, #S4, my(r = oddisog(S4[t])); tested++;
        if(r > 1, hits++; print("HIT depth ", dep, " degree ", n, " odd isogeny degree ", r, "  f = ", f, "  s = ", S4[t])));
      if(dep < DEPTH,
        my(m = #O, dg = apply(poldegree, O));
        forsubset(m, s, my(v = Vec(s)); if(#v > 0 && vecsum(vector(#v, kk, dg[v[kk]])) == 2,
          my(q = vecprod(vector(#v, kk, O[v[kk]])));
          for(tt = 1, #TW, my(g = piece2(q, TW[tt])); if(g != 0, listput(nxt, subst(f, x, g))))))));
    print("depth ", dep, ": maps ", #level, " (degree ", 2^dep, "), stable 4-sets tested so far ", tested, ", hits so far ", hits);
    level = Set(Vec(nxt))) }
print("total hits: ", hits);
quit
