#!/usr/bin/env python3
"""Stage32 D10-LOW-GENUS: run every Singular script in sing/ (832 representatives x 2 projections) in parallel and
collect the RESULT lines into results.txt, with provenance. Fails loudly on any Singular error marker.

results.txt format: one header line
  "# singular <first line of `Singular --version`> | command: Singular -q sing/<script>"
then one line per script, sorted:  "<script> <sha256 of the script bytes> RESULT ..."
(the verifier recomputes every script with make_residuals.py and compares the sha256).
usage: python run_residuals.py --shell "wsl.exe -d Ubuntu -u root --" --dir-in-shell DIR [--workers 11]
"""
import argparse
import hashlib
import shlex
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--shell", default=""); ap.add_argument("--dir-in-shell", required=True)
ap.add_argument("--workers", type=int, default=11)
a = ap.parse_args()
sh = shlex.split(a.shell)
scripts = sorted(p.name for p in (HERE / "sing").glob("*.sing"))
ver = subprocess.run(sh + ["bash", "-c", "Singular --version 2>&1 | head -1"], capture_output=True, text=True).stdout.strip()
if not ver:
    sys.exit("Singular not found")


def run(name):
    sha = hashlib.sha256((HERE / "sing" / name).read_bytes()).hexdigest()
    p = subprocess.run(sh + ["bash", "-c", f"cd {shlex.quote(a.dir_in_shell)} && timeout 3600 Singular -q sing/{name}"],
                       capture_output=True, text=True)
    lines = [l for l in p.stdout.splitlines() if "redefining" not in l and not l.strip().startswith("//")]
    err = [l for l in lines if l.strip().startswith("?") or "error occurred" in l]
    res = [l for l in lines if l.startswith("RESULT")]
    if p.returncode != 0 or err or len(res) != 1:
        return name, sha, "ERROR " + " | ".join((err or lines)[-3:])
    return name, sha, res[0]


out = []
with ThreadPoolExecutor(a.workers) as ex:
    for k, fut in enumerate(as_completed([ex.submit(run, s) for s in scripts]), 1):
        name, sha, r = fut.result()
        out.append(f"{name} {sha} {r}")
        if k % 100 == 0 or r.startswith("ERROR"):
            print(k, name, r[:120], flush=True)
header = f"# singular {ver} | command: Singular -q sing/<script>"
(HERE / "results.txt").write_bytes((header + "\n" + "\n".join(sorted(out)) + "\n").encode())
print("done", len(out), "errors", sum("ERROR" in l for l in out))
sys.exit(1 if any("ERROR" in l for l in out) else 0)
