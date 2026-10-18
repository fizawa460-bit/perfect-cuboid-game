#!/usr/bin/env python3
"""Stage32 D8-LOW-GENUS: generate the exhaustive job inventory and run the certified enumeration (CONTRACT.md §2).

Inventory (generated, not hand-listed): d = 8, n1 in 1..7, and
  (c2min = -10, e in 12..24)  [genus 0 needs e >= 12 by §1; g = 1 classes with e >= 12 are inside C^2 >= -10]
  (c2min =  -8, e in 8..11)   [genus 1 only, e >= 8 by §1]
For every slice: one BOUND job (exact certificate Gamma49.x <= 10 on the unsplit slice) and 11 split jobs v = 0..10.
Results are appended to RESULTS (one JSON per line, resumable).
usage: python run_certified.py --repo REPO --enum "CMD" [--workers 11] [--out certified_results.jsonl]
"""
import argparse
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent


def inventory():
    slices = [(n1, e, -10) for n1 in range(1, 8) for e in range(12, 25)] + \
             [(n1, e, -8) for n1 in range(1, 8) for e in range(8, 12)]
    jobs = []
    for (n1, e, c2) in slices:
        jobs.append((n1, e, c2, None))
        jobs += [(n1, e, c2, v) for v in range(0, 11)]
    return jobs


def producer_id():
    """sha256 over the exact bytes of the three producer files; every record carries it, and resumption only
    reuses records with the CURRENT producer id (stale results from other code are never accepted)."""
    h = hashlib.sha256()
    for name in ("certified_driver.py", "certified_enum.c", "run_certified.py"):
        h.update(name.encode() + b"|" + (HERE / name).read_bytes() + b"|")
    return h.hexdigest()


def key(j):
    return f"{j[0]}|{j[1]}|{j[2]}|{'BOUND' if j[3] is None else j[3]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--enum", required=True)
    ap.add_argument("--workers", type=int, default=11)
    ap.add_argument("--out", default=str(HERE / "certified_results.jsonl"))
    a = ap.parse_args()
    out = Path(a.out)
    pid = producer_id()
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            r = json.loads(line)
            if r.get("producer") == pid and not r["status"].startswith("ERROR"):
                done.add(r["job"])
    todo = [j for j in inventory() if key(j) not in done]
    todo.sort(key=lambda j: (j[0] != 4, j[1], j[3] is not None))     # big n1 = 4 slices first
    print(f"producer {pid}; inventory {len(inventory())}, to run {len(todo)}", flush=True)

    def run(j):
        n1, e, c2, v = j
        cmd = [sys.executable, str(HERE / "certified_driver.py"), a.repo, "8", str(n1), str(e), str(c2), "--enum", a.enum]
        cmd += ["--bound-only"] if v is None else ["--fix", f"49={v}"]
        p = subprocess.run(cmd, capture_output=True, text=True, env={**__import__("os").environ, "PYTHONUTF8": "1"})
        try:
            r = json.loads(p.stdout.strip().splitlines()[-1])
        except Exception:
            r = {"status": f"ERROR driver rc={p.returncode} {p.stderr[-300:]}"}
        r["job"] = key(j)
        r["producer"] = pid
        return r

    with ThreadPoolExecutor(a.workers) as ex, out.open("a") as fh:
        futs = [ex.submit(run, j) for j in todo]
        for k, f in enumerate(as_completed(futs), 1):
            r = f.result()
            fh.write(json.dumps(r, separators=(",", ":")) + "\n"); fh.flush()
            print(f"[{k}/{len(todo)}] {r['job']} {r['status'][:60]} classes={len(r.get('classes', []))}", flush=True)


if __name__ == "__main__":
    main()
