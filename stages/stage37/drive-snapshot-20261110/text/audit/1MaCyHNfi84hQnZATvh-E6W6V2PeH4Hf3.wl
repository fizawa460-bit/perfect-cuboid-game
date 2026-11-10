Clear[u,s,x,h];
aa=1+u^2;
ee=4*u*s/aa-4*u^2/aa;
pp=4*u^2*s/aa;
ff=x^3-s*x^2+ee*x-pp;
{Factor[(ff/.x->u)-u^2*(u*(aa-4)/aa-s)],
 Factor[(ff/.x->u+h)-(ff/.x->u)-h*(D[ff,x]/.x->u)-(3*u-s)*h^2-h^3]}
(* Expected and obtained: {0,0}. No quartic root is identified with x or u. *)
