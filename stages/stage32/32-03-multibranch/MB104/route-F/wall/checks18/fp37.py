#!/usr/bin/env python3
"""checks18 / fp37.py -- GPU count N_p (checks15/fpcount2.py, unchanged) for the four exceptional degree-6 data at p = 37.
tower18.gp predicts N_37 = 0 for all four (and N_13 = 4, N_17 = N_29 = 2, which checks15 already found).
Usage: python fp37.py [p]      (output: fp37.jsonl in this directory; checks15/fpcount2.jsonl is not touched)"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "checks15"))
import cupy as cp
import fpcount as F1, fpcount2 as F2
p = int(sys.argv[1]) if len(sys.argv) > 1 else 37
kern = cp.RawKernel(F1.KERNEL, "count")
for d in ["021133", "201133", "110233", "112033"]:
    r = F2.run(6, p, d, cp, kern)
    print(json.dumps(r), flush=True)
    with open(os.path.join(HERE, "fp37.jsonl"), "a") as f: f.write(json.dumps(r) + "\n")
