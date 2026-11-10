Clear[a1,a2,a3,cc,ss,tt,z,uu,xx,aa,ee,pp,ff,r];
cc=a2 a3;ss=a1/a2;tt=a1/a3;
z[c_,s_,t_]:=1+(1+c^2+c^2 s^2)t/(c s);
phaseChecks={Factor[z[cc,ss,tt]-(1+a1^2+a2^2+a3^-2)],Factor[z[cc,tt,ss]-(1+a1^2+a2^-2+a3^2)],Factor[z[cc ss,tt/ss,1/ss]-(1+a1^-2+a2^2+a3^2)]};
Clear[ss];aa=1+uu^2;ee=4uu(ss-uu)/aa;pp=4uu^2 ss/aa;ff=xx^3-ss xx^2+ee xx-pp;
productChecks={Factor[(ff/.xx->ss+2)/8-(2+ss+ss uu)^2/(4aa)],Factor[-(ff/.xx->ss-2)/8-(2-ss+ss uu)^2/(4aa)]};
rhoChecks={Factor[(3+r)^2-8(1+3r/4)-(1+r^2)],Factor[(3-r)^2-8(1-3r/4)-(1+r^2)]};
{phaseChecks,productChecks,rhoChecks}
