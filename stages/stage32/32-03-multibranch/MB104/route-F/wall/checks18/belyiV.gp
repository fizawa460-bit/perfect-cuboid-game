/* checks18 / belyiV.gp -- fields of the Belyi maps written by belyiV.py.
   Usage: gp -q belyiV.gp < /dev/null   with the environment variable BELYI = name of the .gpdata file */
default(realprecision, 115);
read(getenv("BELYI"));
rat(z) = { my(r = bestappr(real(z), 10^40)); if(abs(z - r) > 1e-50, error("not rational: ", z)); r };
pol(k) = { my(P = prod(j = 1, #S, 'X - S[j][k])); Pol(apply(rat, Vec(P)), 'X) };
{ print(getenv("BELYI"), ": ", #S, " maps, ", #S[1], " coordinates");
  for(k = 1, #S[1],
  my(Q = pol(k), fa = factor(Q), fn = nffactor(nfinit(t^2 + 1), Q));
  print(" coordinate ", k, ": degrees over Q ", apply(poldegree, fa[, 1]~), " exponents ", fa[, 2]~, ";  over Q(i) ", apply(poldegree, fn[, 1]~), " exponents ", fn[, 2]~);
  if(k == 1, for(j = 1, matsize(fa)[1], my(g = fa[j, 1]);
    if(poldegree(g) == 1, print("   rational c = ", -polcoeff(g, 0)/polcoeff(g, 1)),
      my(K = nfinit(g)); if(type(K) == "t_VEC" && #K == 2, K = K[1]); print("   factor of degree ", poldegree(g), ": field ", polredbest(K.pol), ", disc ", factor(K.disc)))))) }
quit
