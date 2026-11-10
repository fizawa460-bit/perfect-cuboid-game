Clear[a,b,c,z]; aa={a,b,c}; q=aa^2(2z-aa^2); dd=Expand[z^4+Total[q^2]-2z^2 Total[q]-2(q[[1]]q[[2]]+q[[1]]q[[3]]+q[[2]]q[[3]])]; pp=Expand[dd^2-64z^2 Times@@q]; forms={a^2+b^2+c^2,-a^2+b^2+c^2,a^2-b^2+c^2,a^2+b^2-c^2}; {Exponent[pp,z],Coefficient[pp,z,8],Expand[(dd/.z->0)+Times@@forms],Expand[(pp/.z->0)-(Times@@forms)^2]}
(* Expected {8,1,0,0}; within-session verification. *)
