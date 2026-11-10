Clear[a,b,c]; v={a,b,c}; ss=Total[v]; ee=a b+a c+b c; pp=a b c; tt=Expand[(ss ee+pp)^2-ss^2 pp(4ss-pp)]; {Expand[(tt/.c->-a-b)-(a b(-a-b))^2],Expand[(tt/.a->0)-((b+c)b c)^2]}
(* Expected {0,0}; within-session replay. *)
