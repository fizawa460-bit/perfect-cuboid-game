/* checks18 / belyi7.gp -- fields of the 16 Belyi maps of degree 7 with passport (4 2 1)^3 (ANSWER-18, 2.4).
   Usage: gp -q belyi7.gp < /dev/null > belyi7.out   (reads belyi7data.gp, written from belyi7.json) */
default(realprecision, 105);
read("belyi7data.gp");
nm = ["c", "b", "c1", "d", "e", "g", "h"];
rat(z) = { my(r = bestappr(real(z), 10^30)); if(abs(z - r) > 1e-60, error("not rational: ", z)); r };
pol(k) = { my(P = prod(j = 1, #S, 'X - S[j][k])); Pol(apply(rat, Vec(P)), 'X) };
{ for(k = 1, 7,
  my(Q = pol(k), fa = factor(Q), fn = nffactor(nfinit(t^2 + 1), Q));
  print(nm[k], ": degrees over Q ", apply(poldegree, fa[, 1]~), " exponents ", fa[, 2]~, ";  degrees over Q(i) ", apply(poldegree, fn[, 1]~))) }
{ my(Q = pol(1), fa = factor(Q));
  for(j = 1, matsize(fa)[1], my(g = fa[j, 1]);
    if(poldegree(g) == 1, print("rational c: ", -polcoeff(g, 0)/polcoeff(g, 1)),
      my(K = nfinit(g), gg = polredbest(g)); print("factor of degree ", poldegree(g), ": polredbest ", gg, ", disc ", factor(K.disc), if(poldegree(g) <= 11, Str(", Galois group ", polgalois(g)), "")))) }
quit
