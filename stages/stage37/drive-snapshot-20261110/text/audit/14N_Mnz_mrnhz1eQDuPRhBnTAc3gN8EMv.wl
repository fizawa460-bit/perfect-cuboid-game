Clear[r,x]; a=2*r;b=r^2-1;n=(r^2+1)^2;
f=n*x^4-8*a*b*x^3+(11*a^2-b^2)*x^2+6*a*b*x-a^2;
{Factor[2*b^2-25*a^2],Factor[f/.r->8],Factor[(f/.r->8),Modulus->3],
 Factor[(f/.r->8),Modulus->11],Table[Mod[x^3+8*x^2+8*x+4,11],{x,0,10}]}
(* Verified output: {2*(1-52*r^2+r^4),-256+6048*x-1153*x^2-8064*x^3+4225*x^4,
 2+2*x^2+x^4,(2+x)*(4+8*x+8*x^2+x^3),{4,10,5,6,8,6,6,3,3,1,3}} *)
