"""32R-77: mu = sum_p x.E_p (48 exceptional curves) for the 23 d = 16 net classes (h0 = 3, 4; n16/plan.json).
Exact integer arithmetic; independent of mu_d16.json.  Prints one row per net and the E05.1 verdict."""
import json, sys
REPO = "C:/Users/fizaw/claudework/perfect-cuboid-game"
sys.path.insert(0, REPO + "/stages/stage32/management/d10-low-genus/enumeration")
import slice_lib as L
L.load(REPO)
Gn = [[int(v) for v in r] for r in L.D["Gn"].tolist()]; n = len(Gn)
Cn = [[int(v) for v in L.D["Cn"][i]] for i in range(140)]; deg = [int(v) for v in L.D["deg"]]
dot = lambda a, b: sum(a[i] * Gn[i][j] * b[j] for i in range(n) for j in range(n) if a[i] and b[j])
EXC = [c for c in Cn if dot(c, c) == -2 and sum(c[i] * deg[i] for i in range(n)) == 0]
if len(EXC) != 48: raise SystemExit("FAIL: %d exceptional curves" % len(EXC))
reps = json.load(open("d16_reps_full.json"))["reps"]; plan = json.load(open("n16/plan.json"))
if len(plan) != 23: raise SystemExit("FAIL: plan has %d nets" % len(plan))
bad = 0; low = []
for k, v in plan.items():
    x = reps[int(k)]["x"]
    d = sum(x[i] * deg[i] for i in range(n)); c2 = dot(x, x); pr = [dot(x, e) for e in EXC]; mu = sum(pr)
    if d != 16 or c2 != v["C2"] or min(pr) < 0: bad += 1
    verdict = "no g<=1 curve (mu < 18)" if mu < 18 else ("g = 1 only" if mu < 22 else "g <= 1 possible")
    print(f"{k:>6}  h0 {v['h0']}  C2 {c2:>2}  mu {mu:>2}  min x.E {min(pr)}  {verdict}")
    if mu < 18: low.append(k)
print("mu < 18:", len(low), low)
print("PASS" if bad == 0 and len(low) == 13 else "FAIL")
