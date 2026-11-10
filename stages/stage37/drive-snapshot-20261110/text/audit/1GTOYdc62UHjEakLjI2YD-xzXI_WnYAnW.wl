Clear[a,b,x];
f[x_]:=(a^2+b^2)*x^4-8*a*b*x^3+(11*a^2-b^2)*x^2+6*a*b*x-a^2;
{Factor[Discriminant[f[x],x]],Factor[f[a/b]],Factor[D[f[x],x]/.x->a/b],Expand[(f[x]/.x->-x)-(f[x]/.a->-a)]}
(* Verified output: {-16*a^2*(25*a^2-2*b^2)^3*(a^2+b^2)^2,
 a^2*(a^2+2*b^2)^2/b^4,2*a*(2*a^4+a^2*b^2+2*b^4)/b^3,0} *)
