P=t^6-5*t^5-8*t^4-5*t^3-8*t^2-5*t-1;
b=bnfinit(P,1);print("PARI_VERSION=",version());print("BNFCERTIFY=",bnfcertify(b));print("DISC=",b.disc," SIGNATURE=",b.sign," CLASS=",b.no," INDEX=",b.index);print("BASIS=",b.zk);B=[1,t,(1+t+t^2)/2,(1+t^3)/2,(1+t^2+t^4)/4,(t+t^3+t^5)/4];Z=matrix(6,6,i,j,nfalgtobasis(b,B[j])[i]);print("SUPPLIED_BASIS_DET=",matdet(Z)," ROOTS_OF_UNITY=",b.tu);if(abs(matdet(Z))!=1,error("basis mismatch"));
U=[(-1-17*t-5*t^2-13*t^3-17*t^4+3*t^5)/4,(13+40*t+11*t^2+32*t^3+33*t^4-6*t^5)/4,(-8-35*t-12*t^2-23*t^3-28*t^4+5*t^5)/4];
E=matrix(3,3);for(j=1,3,v=bnfisunit(b,U[j]);print("UNIT",j,"=",v);for(i=1,3,E[i,j]=v[i]));print("UNIT_TRANSITION_DET=",matdet(E));
print("DECOMP2=",idealprimedec(b,2));print("DECOMP3461=",idealprimedec(b,3461));
pi=-2-t+(1+t+t^2)/2+2*(1+t^3)/2+(1+t^2+t^4)/4;
ga=10-2*t-11*(1+t+t^2)/2-8*(1+t^3)/2-10*(1+t^2+t^4)/4+2*(t+t^3+t^5)/4;
gb=3461/Mod(ga,P)^2;print("PRINCIPAL_PI=",idealfactor(b,pi));print("PRINCIPAL_GA=",idealfactor(b,ga));print("PRINCIPAL_GB=",idealfactor(b,gb));print("DISC_F=",poldisc(t*subst(P,t,-t)));quit;
