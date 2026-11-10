Clear[v1,v2,v3,z1,z2,z3,uu,ss,xx,aa,ee,pp,ff];
s0=v1+v2+v3;e0=v1 v2+v1 v3+v2 v3;p0=v1 v2 v3;
dd={(v2+v3)/2,(v1+v3)/2,(v1+v2)/2};
pol=Expand[Times@@Flatten[Table[1+e1 z1+e2 z2+e3 z3,{e1,{-1,1}},{e2,{-1,1}},{e3,{-1,1}}]]];
red=PolynomialRemainder[PolynomialRemainder[PolynomialRemainder[pol,z1^2-(1-dd[[1]]^2),z1],z2^2-(1-dd[[2]]^2),z2],z3^2-(1-dd[[3]]^2),z3];
surface=(s0 e0+p0)^2-s0^2 p0(4s0-p0);
aa=1+uu^2;ee=4uu(ss-uu)/aa;pp=4uu^2 ss/aa;ff=xx^3-ss xx^2+ee xx-pp;
{Factor[red-surface],Factor[(ff/.xx->ss+2)/8-(2+ss+ss uu)^2/(4aa)],Factor[-(ff/.xx->ss-2)/8-(2-ss+ss uu)^2/(4aa)]}
