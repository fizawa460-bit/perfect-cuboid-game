"""32R-65: finish split_reps.py from the shard outputs (r{d}_out_*.txt + log) with the C orbit-size tool.
usage: python split_reps_finish.py d nshards"""
import sys, json, re, subprocess
import numpy as np
from collections import Counter
d, NSH = int(sys.argv[1]), int(sys.argv[2])
sys.path.insert(0, "C:/Users/fizaw/claudework/stage32_research/d12_run")
import slice_lib as L
L.load("C:/Users/fizaw/claudework/perfect-cuboid-game")
P140 = [[int(v) for v in L.D["Pn"][k]] for k in range(140)]
Gn = [[int(v) for v in r] for r in L.D["Gn"]]
gens = [tuple(p) for p in json.load(open("../stoll/geo_perms.json"))["perms"]]
G = {tuple(range(140))}; fr = list(G)
while fr:
    nf = []
    for a in fr:
        for g in gens:
            c = tuple(a[g[k]] for k in range(140))
            if c not in G: G.add(c); nf.append(c)
    fr = nf
G = sorted(G); assert len(G) == 1536
hdr = [str(len(G))] + [" ".join(map(str, p)) for p in G] + [" ".join(map(str, r)) for r in P140] + [" ".join(map(str, r)) for r in Gn]
open(f"orb{d}_hdr.txt", "w", newline=chr(10)).write(chr(10).join(hdr) + chr(10))
log = open(f"reps_d{d}.log").read()
inv = [int(v) for v in re.findall(r"inventory (\d+) reps", log)]; nrep_log = [int(v) for v in re.findall(r"reps (\d+)", log)]
assert len(inv) == NSH, f"log has {len(inv)} shard lines"
W = "/mnt/c/Users/fizaw/claudework/stage32_research/split"
files = " ".join(f"{W}/r{d}_out_{s}.txt" for s in range(NSH))
cmd = f"cat {W}/orb{d}_hdr.txt {files} | /root/orbsize > {W}/orb{d}_out.txt"
subprocess.run(["wsl.exe", "-d", "Ubuntu", "-u", "root", "--", "bash", "-c", cmd], check=True)
O = np.loadtxt(f"orb{d}_out.txt", dtype=np.int64, ndmin=2)
print(f"d={d}: reps {len(O)} (log {sum(nrep_log)}), sum of orbit sizes {O[:, 0].sum()}, inventory {sum(inv)}")
assert len(O) == sum(nrep_log) and O[:, 0].sum() == sum(inv), "MISMATCH"
print("geometric reps by C^2:", sorted(Counter(O[:, 1].tolist()).items()))
np.save(f"reps_d{d}_orbC2.npy", O)
