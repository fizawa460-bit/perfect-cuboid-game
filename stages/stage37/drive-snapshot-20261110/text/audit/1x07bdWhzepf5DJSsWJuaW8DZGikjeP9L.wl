Clear[u,s,x];
aa=1+u^2;
ff=x^3-s*x^2+(4*u*s/aa-4*u^2/aa)*x-4*u^2*s/aa;
qq=aa*s^4-16*u*s^3+(44*u^2-4)*s^2+48*u*s-16*u^2;
{Factor[(ff/.x->(-u))-u^2*(u*(4-aa)-s*(aa+8))/aa],
 Factor[(ff/.x->u)-u^2*(u*(aa-4)/aa-s)],
 Factor[(qq/.s->u/2)-u^2*(112+145*u^2+u^4)/16]}
(* Independently evaluated identities; expected result {0,0,0}. *)
