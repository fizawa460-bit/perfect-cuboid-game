Clear[uu,ss,zz,aa,ww,kk,ee,pp]; aa=1+uu^2; ss=-2uu/aa; ee=4uu(ss-uu)/aa; pp=4uu^2 ss/aa; {Together[zz^3-ss zz^2+ee zz-pp-((aa zz-2uu)(aa zz^2+4uu zz-4uu^2)/aa^2)],Simplify[Expand[(ww+uu)^2+(ww-uu)^2-4kk^2]/.{ww^2->uu^2+2,kk^2->uu^2+1}],Simplify[Expand[(ww+uu)(ww-uu)/2]/.{ww^2->uu^2+2}]}
(* Observed symbolic replay: {0,0,1}. Corrected safe symbol names. *)
