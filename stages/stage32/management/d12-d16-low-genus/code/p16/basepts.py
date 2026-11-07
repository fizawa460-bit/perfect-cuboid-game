"""32R-69j base points: for a pencil, i_q = length at q of (g0, g1) is the local intersection of ANY two distinct
members; a member singular at q forces i_q >= 2.  So if R1 ∩ R2 (two random members, D-curves removed) is reduced
off the 48 nodes, no member is singular at a base point off the nodes."""
import json, sys
sys.path.insert(0, "fasth0")
plan = json.load(open("p16/plan.json")); jobs = []
for i, p in plan.items():
    src = open(f"p16/c_{i}_0.sing").read()
    pre = src[:src.index('system("random", 2718);')] + src[src.index('system("random", 2718);'):].split("\n", 1)[0] + "\n"
    m, D, hid = p["decs"][0]
    cids = sorted(int(k) for k in D if int(k) <= 92)
    dc = ("intersect(" + ",".join(f"G{k}" for k in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
    s = pre + f"ideal Dc = std({dc}); ideal NODES = std(S + minor(jacob(S), 4));\n"
    s += "proc satQ(ideal I, ideal Q) { def T = sat(I, Q); ideal R2; if (typeof(T) == \"list\") { R2 = T[1]; } else { R2 = T; } return(std(R2)); }\n"
    s += "ideal R1 = satQ(std(S + ideal(F0 + 3171*F1)), Dc); ideal R2 = satQ(std(S + ideal(F0 - 5521*F1)), Dc);\n"
    s += '"members: degree", mult(R1), mult(R2), " dims", dim(R1), dim(R2);\n'
    s += "ideal BP = satQ(std(R1 + R2), NODES); ideal BPr = std(radical(BP));\n"
    s += '"base points off nodes: length", mult(BP), " distinct", mult(BPr), " dim", dim(BP);\n'
    s += 'if (dim(BP) <= 0) { "BASE-OK (none)"; } else { if (mult(BP) == mult(BPr)) { "BASE-OK (all simple)"; } else { "BASE-NONSIMPLE"; } }\nquit;\n'
    open(f"p16/bp_{i}.sing", "w", newline="\n").write(s); jobs.append(f"bp_{i}")
open("p16/bpjobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n"); print(len(jobs))
