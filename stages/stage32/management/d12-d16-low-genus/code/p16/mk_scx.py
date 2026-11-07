import json,os
NL=chr(10); r=json.load(open("sx_tally.json")); jobs=[]
for k,v in r.items():
    if not v.startswith("OPEN"): continue
    nm="scx"+k[2:]
    if os.path.exists(nm+".out"): continue
    L=open(k+".sing").read().split(NL)
    i=[j for j,l in enumerate(L) if "MEMBER-NOT-CURVE" in l][0]
    body=NL.join(L[:i+1])+NL
    body+='ideal RB = std(radical(Bp)); "radical degree", mult(RB), " scheme degree", mult(Bp);'+NL
    body+='list MA = minAssGTZ(Bp); int ia; int n2 = 0; for (ia = 1; ia <= size(MA); ia++) { ideal QA = std(MA[ia]); "component", ia, " dim", dim(QA), " degree", mult(QA); if (dim(QA) == 2) { n2++; } kill QA; }'+NL
    body+='if (mult(RB) < mult(Bp)) { "MEMBER-NONREDUCED"; } if (n2 >= 2) { "MEMBER-REDUCIBLE-FP"; } if (n2 == 1 && mult(RB) == mult(Bp)) { "MEMBER-IRREDUCIBLE-FP"; }'+NL+"quit;"+NL
    open(nm+".sing","w",newline=NL).write(body); jobs.append(nm)
open("scxjobs.txt","w",newline=NL).write(NL.join(jobs)+NL); print(len(jobs))
