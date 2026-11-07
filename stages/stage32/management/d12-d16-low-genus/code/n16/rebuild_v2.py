import re
tail = open("net_tail_c.sing", encoding="utf-8").read()
j2 = open("jobs.txt").read().split(); j3 = open("jobs3.txt").read().split()
three = {j.split("_")[1] for j in j3}
for j in j2 + j3:
    s = open(j + ".sing", encoding="utf-8").read()
    k = s.index("int HH = "); e = s.index("\n", k)
    hdr = s[k:e]
    if j.split("_")[1] in three: hdr = re.sub(r"int THR = \d+;", "int THR = 4;", hdr)
    open(j + ".sing", "w", newline="\n", encoding="utf-8").write(s[:k] + hdr + "\n" + tail)
    print(j, hdr)
# 3-dec jobs first so that each net is complete early; longest-known jobs early too
open("jobs_v2.txt", "w", newline="\n").write("\n".join(j3 + j2) + "\n")
