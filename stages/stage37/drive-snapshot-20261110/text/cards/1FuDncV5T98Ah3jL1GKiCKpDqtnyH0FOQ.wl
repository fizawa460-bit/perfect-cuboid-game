Clear[a,b,mm,tt]; psi=b^2-12*a*b^2*tt+4*a^2*mm^2*tt^2; fr=a^2*mm^6*tt^4-3*a*b^2*mm^4*tt^3-(11*a^2-b^2)*mm^2*b^2*tt^2/4+a*b^4*tt-b^4/16; ph0=b^4-16*a*b^4*tt+(44*a^2-4*b^2)*mm^2*b^2*tt^2+48*a*mm^4*b^2*tt^3-16*a^2*mm^6*tt^4; Factor[16*fr+ph0]
(* Exact output:0. *)

