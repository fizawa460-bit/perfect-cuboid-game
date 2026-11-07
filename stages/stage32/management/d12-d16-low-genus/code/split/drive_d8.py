"""32R-60 driver: write msearch input for the d = 8 filtered y-candidates, run, reconstruct x, compare with known."""
import sys, json, time, pickle, subprocess
import numpy as np
sys.path.insert(0, "../scripts")
args = sys.argv[1:]
sys.argv = ["x"]
exec(open("../scripts/32R-59_split_enum.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0])
Z, Y2, MT, BQ = pickle.load(open("../scripts/32R-59_d8_filtered.pkl", "rb"))
c2min = -10
# D in RREF with pivot (information) positions
rows = [[int(v) % 2 for v in s] for s in satm]
R = []
for r in rows:
    r = r[:]
    for (piv, rr) in R:
        if r[piv]: r = [a ^ b for a, b in zip(r, rr)]
    if any(r):
        piv = r.index(1)
        R = [(p, [a ^ b for a, b in zip(q, r)] if q[piv] else q) for p, q in R]
        R.append((piv, r))
assert len(R) == 10
Ipos = [p for p, _ in R]
lines = [f"{MU.shape[0]} {len(R)}"]
lines += [" ".join(map(str, MU[q])) for q in range(MU.shape[0])]
lines.append(" ".join(map(str, Ipos)))
lines += [" ".join(map(str, r)) for _, r in R]
for i in range(len(Z)):
    s2max = int(np.floor(2 * (Y2[i] - c2min) + 1e-9))
    lines.append(f"{i} {s2max}")
    lines.append(" ".join(map(str, MT[i])))
    lines.append(" ".join(map(str, BQ[i])))
open("d8_in.txt", "w", newline="\n").write("\n".join(lines) + "\n")
t0 = time.time()
p = subprocess.run(["wsl.exe", "-d", "Ubuntu", "-u", "root", "--", "bash", "-c", "/root/msearch < /mnt/c/Users/fizaw/claudework/stage32_research/split/d8_in.txt > /mnt/c/Users/fizaw/claudework/stage32_research/split/d8_out.txt"], capture_output=True, text=True)
print(p.stderr.strip(), f"{time.time()-t0:.1f}s", flush=True)
pre64 = np.array(pre, dtype=np.int64)
S = np.array([[int(v) for v in s] for s in sat], dtype=np.int64)
SM = S.dot(Pm.T)
SMinv = fmpq_mat([[fmpq(int(v)) for v in r] for r in SM.tolist()]).inv()
SMinv_np = np.array([[float(SMinv[i, j]) for j in range(48)] for i in range(48)])
found = set(); bad = 0
for line in open("d8_out.txt"):
    a = list(map(int, line.split()))
    i, m = a[0], np.array(a[1:], dtype=np.int64)
    dm = m - MT[i]
    coef = dm.dot(SMinv_np)
    ci = np.rint(coef).astype(np.int64)
    if np.abs(coef - ci).max() > 1e-6: bad += 1; continue
    x = Z[i].dot(pre64) + ci.dot(S)
    found.add(tuple(int(v) for v in x))
print("solutions -> distinct x:", len(found), " non-integral:", bad)
REPO = "C:/Users/fizaw/claudework/perfect-cuboid-game"
known = set()
for line in open(REPO + "/stages/stage32/management/d8-low-genus/enumeration/certified_results.jsonl"):
    for c in json.loads(line)["classes"]:
        known.add(tuple(c["x"]))
Gn64 = np.array(L.D["Gn"], dtype=np.int64)
F1 = np.array([int(v) for v in L.D["F1row"]], dtype=np.int64)
exc = np.array([int(v) for v in L.D["exc"]], dtype=np.int64)
P140 = np.array([[int(v) for v in L.D["Pn"][k]] for k in range(140)], dtype=np.int64)
degv = np.array([int(v) for v in L.D["deg"]], dtype=np.int64)
def in_inventory(x, d=8):
    x = np.array(x, dtype=np.int64)
    if int(degv.dot(x)) != d or (P140.dot(x) < 0).any(): return False
    n1, e, c2 = int(F1.dot(x)), int(exc.dot(x)), int(x.dot(Gn64).dot(x))
    n2 = d - n1; M = max(n1, n2); mm = min(n1, n2)
    if n1 < 1 or n2 < 1: return False
    if 2 * M + 4 <= e <= 6 * mm: return c2 >= -2 - d
    if 2 * M <= e <= min(6 * mm, 2 * M + 3): return c2 >= -d
    return False
inv = {x for x in found if in_inventory(x)}
print("in inventory:", len(inv), " known:", len(known), " common:", len(inv & known), " new:", len(inv - known), " missing:", len(known - inv))
