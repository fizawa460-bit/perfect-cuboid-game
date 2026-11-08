\\ Exact arithmetic in R=(Z/163^k Z)[t]/T, with x the Mumford variable.
\\ The even-degree curve is moved to an odd model using a Hensel branch root.
setring(p,k,tl)={RP=p;RK=k;RM=p^k;RT=Polrev(tl,t)*Mod(1,RM);RTP=Polrev(tl,t)*Mod(1,RP);RC=Mod(t*Mod(1,RM),RT);RCP=Mod(t*Mod(1,RP),RTP);};
top(a)={subst(liftall(a),t,RCP)*Mod(1,RP);};
tom(a)={subst(liftall(a),t,RC)*Mod(1,RM);};
cinv(a)={if(top(a)==0,error("CINV_NONUNIT"));my(b=tom(1/top(a)));for(i=1,logint(RK,2)+2,b=b*(2-a*b));if(a*b!=1,error("coefficient Hensel inverse"));b;};
pinv(a,u)={my(ap=top(a),up=top(u),b);if(poldegree(gcd(ap,up))>0,error("PINV_NONCOPRIME"));b=tom(lift(1/Mod(ap,up)));for(i=1,logint(RK,2)+2,b=(b*(2-a*b))%u);if((a*b)%u!=1,error("polynomial Hensel inverse"));b;};
setcurve(f,g)={FF=f;GG=g;COUNTER=0;};
pexact(a,b)={my(v=divrem(a,b));if(v[2]!=0,error("non-exact polynomial division"));v[1];};
monic(a)={a*cinv(pollead(a));};
mcheck(d)={if(d[1]==0,error("zero Mumford u"));if((d[2]^2-FF)%d[1]!=0,error("Mumford identity failed"));1;};
mred(d)={my(u=d[1],v=d[2]);while(poldegree(u)>GG,u=monic(pexact(FF-v^2,u));v=(-v)%u;);u=monic(u);v=v%u;my(r=[u,v]);mcheck(r);COUNTER++;r;};
mneg(d)={[d[1],(-d[2])%d[1]];};
mdbl(d)={if(d[1]==1,return(d));my(u=d[1],v=d[2],q=pexact(FF-v^2,u));my(s=(q*pinv(2*v,u))%u);mred([u^2,v+u*s]);};
madd(a,b)={if(a[1]==1,return(b));if(b[1]==1,return(a));my(u=a[1],v=a[2],w=b[1],z=b[2]);my(s=((z-v)*pinv(u,w))%w);mred([u*w,(v+u*s)%(u*w)]);};
moffset(d,n,e)={my(bits=binary(n),r=madd(e,d),ne=mneg(e));for(i=2,#bits,DBGSTEP=i;DBGOP="double";r=mdbl(r);DBGOP="subtractE";r=madd(r,ne);if(bits[i],DBGOP="addD";r=madd(r,d)););r;};
mtinyoffset(a,b,n,e)={my(bits=binary(n),r=madd(madd(e,a),b),ne=mneg(e));for(i=2,#bits,r=madd(mdbl(r),ne);if(bits[i],r=madd(madd(r,a),b)););r;};
crtpoly(v,u,z,w)={my(s=((z-v)*pinv(u,w))%w);(v+u*s)%(u*w);};
