/* checks14 / cm14.gp -- request 14: the two degree-5 slack-0 maps with moduli field Q(i) are the x-coordinates of the
   complex multiplications 2 + i and 2 - i on E: y^2 = x^3 - x  (branch set S = {0, oo, 1, -1}; the other two points
   of B are x = +-i, the x-coordinates of the points with 2P = (0,0)).   Usage: gp -q cm14.gp > cm14.out */
I2 = Mod(t, t^2 + 1);                     /* i */
lam2 = (3*x^2 - 1)/2;                     /* slope of the tangent, times y */
x2 = lam2^2/(x^3 - x) - 2*x;              /* x([2]P) */
R = lam2*(x - x2)/(x^3 - x) - 1;          /* y([2]P) / y */
F(e) = { my(l2 = (x^3 - x)*(R - e*I2)^2/(x2 + x)^2); l2 - x2 + x };   /* x([2]P + [e i]P), [i](x,y) = (-x, i y) */
chk(e) = { my(f = F(e), N = numerator(f), D = denominator(f), ok = 1, fa);
  print("e = ", e, ":  x((2 + e i)P) = ", lift(f));
  print("  degree ", max(poldegree(N), poldegree(D)));
  my(pl = [N, D, numerator(f - 1), numerator(f + 1)], nm = ["0", "oo", "1", "-1"]);
  for(k = 1, 4, fa = factor(pl[k]);
    my(e2 = vecsum(vector(matsize(fa)[1], j, if(fa[j, 2] == 2, poldegree(fa[j, 1]), 0))),
       e1 = vecsum(vector(matsize(fa)[1], j, if(fa[j, 2] == 1, poldegree(fa[j, 1]), 0))));
    if(k == 2, e1 += 5 - poldegree(D) + 0; );
    print("  over ", nm[k], ": double points ", e2, ", simple points ", e1 + if(k != 2 && poldegree(pl[k]) < 5, 5 - poldegree(pl[k]), 0)));
  fa = factor(numerator(f^2 + 1));
  print("  over +-i: exponents ", fa[, 2]~, " degrees ", apply(poldegree, fa[, 1]~));
  print("  commutes with x -> -x: ", subst(f, x, -x) == -f, ";  with x -> -1/x: ", subst(f, x, -1/x) == -1/f || subst(f, x, -1/x) == 1/f || subst(f,x,-1/x) == f || subst(f,x,-1/x) == -f) };
chk(1); chk(-1);
/* a slack-0 map over Q(i) that uses all six points of B: f o g, f = x((2+i)P), g of degree 2 branched at the two
   Q(i)-rational points of f^{-1}(i), f^{-1}(-i) */
{ my(f = F(1), fa, r1, r2, g, h, tot = 0, typ = List());
  fa = factor(numerator(f - I2)); r1 = -polcoef(fa[1, 1], 0)/polcoef(fa[1, 1], 1);
  fa = factor(numerator(f + I2)); r2 = -polcoef(fa[1, 1], 0)/polcoef(fa[1, 1], 1);
  print("rational points over i, -i: ", lift(r1), ", ", lift(r2));
  g = (r1 - r2*x^2)/(1 - x^2);                       /* critical points 0, oo -> values r1, r2 */
  h = subst(f, x, g);
  my(pl = [numerator(h - I2), numerator(h + I2), numerator(h - 1), numerator(h + 1), numerator(h), denominator(h)]);
  for(k = 1, 6, fa = factor(pl[k]);
    my(e2 = vecsum(vector(matsize(fa)[1], j, if(fa[j, 2] == 2, poldegree(fa[j, 1]), 0))) + if(k == 2, 0, 0),
       bad = vecsum(vector(matsize(fa)[1], j, fa[j, 2] > 2)), dd = 10 - poldegree(pl[k]));
    if(dd == 2, e2++); if(dd == 1 || dd > 2, bad++);
    listput(typ, e2); tot += e2; if(bad, print("NOT slack 0")));
  print("degree-10 map f o g: double points over (i, -i, 1, -1, 0, oo) = ", Vec(typ), ", total ", tot, " (2n - 2 = 18)");
  print("automorphism x -> -x: ", subst(h, x, -x) == h) }
quit
