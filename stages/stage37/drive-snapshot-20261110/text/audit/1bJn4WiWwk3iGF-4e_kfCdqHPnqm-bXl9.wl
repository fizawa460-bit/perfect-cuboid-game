Clear[a,b,c]; ff={a^2+b^2+c^2,-a^2+b^2+c^2,a^2-b^2+c^2,a^2+b^2-c^2}; {Expand[ff[[1]]-ff[[2]]-2a^2],Expand[ff[[3]]+ff[[4]]-2a^2],Expand[ff[[2]]+ff[[3]]-2c^2],Expand[ff[[2]]+ff[[4]]-2b^2]}
(* Expected {0,0,0,0}; within-session replay. *)
