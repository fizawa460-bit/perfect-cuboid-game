Clear[u,s,x];
aa=1+u^2;
ff=x^3-s*x^2+4*u*(s-u)/aa*x-4*u^2*s/aa;
Factor[4*(2*s-u)+aa*(s+u)+aa*(ff/.x->(-u))/u^2]
(* Evaluated result 0. Since f(-u)=-product_i(u+v_i), this is the exact root-product pullback. *)
