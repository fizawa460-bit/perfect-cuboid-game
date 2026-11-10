Clear[a,b,s,t]; n=a^2+b^2; q=n*s^2-12*a*b*s*t+4*a^2*t^2; j=n*s^2-16*a*b*s*t+48*a^2*t^2; phi=n*s^4-16*a*b*s^3*t+(44*a^2-4*b^2)*s^2*t^2+48*a*b*s*t^3-16*a^2*t^4; {Expand[phi+4*t^2*q-s^2*j],PolynomialRemainder[(phi/.b->0)+176*a^2*t^4,s^2+4*t^2,s],Factor[Resultant[q,phi,t]]}
(* Exact output: {0, 0, 256*a^8*(121*a^2-7*b^2)*(a^2+b^2)*s^8}. *)
