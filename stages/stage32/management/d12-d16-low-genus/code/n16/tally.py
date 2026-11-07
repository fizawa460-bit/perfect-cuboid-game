import re, collections, sys
jobs = open(sys.argv[1]).read().split(); C = collections.Counter(); inc = []
for j in jobs:
    try: t = open(j + ".out").read()
    except FileNotFoundError: C["missing"] += 1; inc.append((j, "missing")); continue
    if "time" not in t: C["unfinished"] += 1; inc.append((j, "unfinished")); continue
    if "MEMBER-REDUCIBLE" in t: C["reducible"] += 1; continue
    m = re.search(r"FASTGENUS (lower bound )?(-?\d+)", t)
    if m:
        g = int(m.group(2))
        if g >= 2: C["genus>=2"] += 1
        else: C["bound<=1"] += 1; inc.append((j, f"bound {g}"))
        continue
    m = re.search(r"(FAST: [a-z ]+|MEMBER-NOT-CURVE|error[^\n]*)", t); C["other"] += 1; inc.append((j, m.group(1) if m else "no result"))
print(len(jobs), dict(C))
open(sys.argv[2], "w", newline="\n").write("\n".join(f"{a}\t{b}" for a, b in inc) + "\n")
print(collections.Counter(b if not b.startswith("bound") else "bound<=1" for a, b in inc))
