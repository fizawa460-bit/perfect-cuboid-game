/* checks18 / tower18b.gp -- the Q-rational 2-towers of checks14/tower14.gp (same construction, same twists), degree <= 8:
   how many are NOT of elliptic type (critical values in 5 or 6 points of B)?   (DRAFT-TOWER-17, C4; ANSWER-18, 2.1)
   Usage: gp -q tower18b.gp < /dev/null > tower18b.out */
default(parisizemax, 2000000000);
TW = [1, -1, 2, -2, 3, -3, 6, -6];
DEPTH = 3;
generic(f) = { my(k = 0, h);
  while(1, k++; h = subst(f, x, (k*x + 1)/(x - k - 1));
    if(poldegree(numerator(h)) == poldegree(denominator(h)) && poldegree(numerator(h)'*denominator(h) - numerator(h)*denominator(h)') == 2*poldegree(numerator(h)) - 2,
      my(c = pollead(numerator(h))/pollead(denominator(h))); if(c != 0 && c != 1 && c != -1 && c^2 != -1, return(h)))) };
/* returns [simple factors, data (a_0, a_oo, a_1, a_-1, a_i + a_-i)] */
ofac(f) = { my(L = List(), pols, F, a = vector(5));
  pols = [numerator(f), denominator(f), numerator(f - 1), numerator(f + 1), numerator(f^2 + 1)];
  for(i = 1, #pols, F = factor(pols[i]);
    for(j = 1, matsize(F)[1], if(F[j, 2] == 1, listput(L, F[j, 1]), if(F[j, 2] != 2, error("not slack 0"), a[i] += poldegree(F[j, 1])))));
  [Vec(L), a] };
piece2(q, d) = { my(c = polcoef(q, 0), b = polcoef(q, 1), a = polcoef(q, 2), G, s, P);
  G = [d*a, d*b/2, 0; d*b/2, d*c, 0; 0, 0, -1];
  s = qfsolve(G); if(type(s) != "t_COL", return(0));
  P = qfparam(G, s) * [x^2, x, 1]~;
  if(P[2] == 0, return(0)); P[1]/P[2] };
level = [x];
{ for(dep = 0, DEPTH,
    my(nxt = List(), hist = vector(6), ex = 0, exa);
    for(k = 1, #level, my(f = generic(level[k]), R = ofac(f), O = R[1], a = R[2], n = poldegree(numerator(f)), ncv);
      if(vecsum(apply(poldegree, O)) != 2*n + 4 || vecsum(a) != 2*n - 2, error("slack"));
      ncv = #select(z -> z > 0, a[1..4]) + if(a[5] > 0, 2, 0); if(ncv > 0, hist[ncv]++);
      if(ncv >= 5 && ex == 0, ex = level[k]; exa = a);
      if(dep < DEPTH,
        my(m = #O, dg = apply(poldegree, O));
        forsubset(m, s, my(v = Vec(s)); if(#v > 0 && vecsum(vector(#v, kk, dg[v[kk]])) == 2,
          my(q = vecprod(vector(#v, kk, O[v[kk]])));
          for(tt = 1, #TW, my(g = piece2(q, TW[tt])); if(g != 0, listput(nxt, subst(f, x, g))))))));
    print("depth ", dep, " (degree ", 2^dep, "): maps ", #level, ";  number of maps by number of critical values (1..6; +-i counted as 2): ", hist);
    if(ex != 0, print("   example with >= 5 critical values: data (a_0, a_oo, a_1, a_-1, a_i + a_-i) = ", exa, "   p = ", ex));
    level = Set(Vec(nxt))) }
quit
