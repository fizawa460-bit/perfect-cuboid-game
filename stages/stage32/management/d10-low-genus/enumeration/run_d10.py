#!/usr/bin/env python3
"""Stage32 D10-LOW-GENUS: symmetry-reduced certified enumeration of the d = 10 numerical classes (CONTRACT.md §2).

Inventory (generated): d = 10, n1 = 1..9, n2 = 10 - n1, M = max(n1, n2), m = min(n1, n2):
  (c2min = -12, e = 2M+4 .. 6m)            [genus 0: e >= 2M + 4]
  (c2min = -10, e = 2M .. min(6m, 2M+3))   [genus 1 only; genus-1 classes with e >= 2M + 4 lie in C^2 >= -12]
For each slice: all boundary vectors b (slice_lib.bvectors), orbit representatives under the symmetry group
(full group if n1 = n2, else the subgroup preserving the V side), and for each representative the certified
enumeration with the 12 boundary values fixed.
Provenance: the runner builds certified_enum.c itself (CFLAGS) inside --shell, and every record carries
producer_info = {sources_sha256, cflags, compiler, binary_sha256} and producer = sha256(producer_info).
usage: python run_d10.py --repo REPO --shell "wsl.exe -d Ubuntu -u root --" --src-dir DIR_IN_SHELL --bin PATH
                         [--workers 11] [--out results.jsonl]
"""
import argparse
import hashlib
import json
import os
import shlex
import subprocess
import sys
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import slice_lib as L  # noqa: E402

CFLAGS = "-O2 -std=c11 -Wall -Wextra -ffp-contract=off -fno-fast-math"
SOURCES = ("slice_lib.py", "run_d10.py", "certified_enum.c", "symmetry_generators.json")
D_DEG = 10


def inventory():
    out = []
    for n1 in range(1, D_DEG):
        n2 = D_DEG - n1; M = max(n1, n2); m = min(n1, n2)
        out += [(n1, e, -12) for e in range(2 * M + 4, 6 * m + 1)]
        out += [(n1, e, -10) for e in range(2 * M, min(6 * m, 2 * M + 3) + 1)]
    return out


def sources_sha256():
    h = hashlib.sha256()
    for name in SOURCES:
        h.update(name.encode() + b"|" + (HERE / name).read_bytes() + b"|")
    return h.hexdigest()


def producer_of(info):
    return hashlib.sha256(json.dumps(info, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def slice_use(grp, n1):
    if n1 == D_DEG - n1:
        return grp
    return [g for g in grp if all(g[l - 1] + 1 in L.D["V"] for l in L.D["V"])]


_W = {}


def winit(repo, enum_cmd):
    L.load(repo); _W["enum"] = enum_cmd


def run_job(job):
    key, n1, e, c2, fixes = job
    st, payload = L.slice_data(D_DEG, n1, e, c2, fixes)
    rec = {"job": key, "d": D_DEG, "n1": n1, "e": e, "c2min": c2, "fixes": fixes}
    if st != "OK":
        rec.update(status=st, classes=[], witness=payload)
        return rec
    inp, x0, Nr = payload
    p = subprocess.run(shlex.split(_W["enum"]), input=inp, capture_output=True, text=True)
    status = p.stderr.strip().split("\n")[-1] if p.stderr.strip() else "?"
    if p.returncode != 0 or not status.startswith("COMPLETE"):
        rec.update(status="ERROR " + status, classes=[])
        return rec
    cls, leaves = L.leaf_classes(p.stdout, x0, Nr, c2)
    rec.update(status=status, classes=cls, leaves=leaves)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True); ap.add_argument("--shell", default="")
    ap.add_argument("--src-dir", required=True); ap.add_argument("--bin", required=True)
    ap.add_argument("--cc", default="gcc"); ap.add_argument("--workers", type=int, default=11)
    ap.add_argument("--out", default=str(HERE / "results.jsonl"))
    a = ap.parse_args()
    sh = shlex.split(a.shell)

    def in_shell(cmd):
        return subprocess.run(sh + ["bash", "-c", cmd], capture_output=True, text=True)
    b = in_shell(f"cd {shlex.quote(a.src_dir)} && {a.cc} {CFLAGS} -o {shlex.quote(a.bin)} certified_enum.c -lm")
    if b.returncode != 0 or b.stderr.strip():
        sys.exit(f"build failed or warned:\n{b.stdout}\n{b.stderr}")
    if in_shell(f"sha256sum {shlex.quote(a.src_dir)}/certified_enum.c").stdout.split()[0] != \
            hashlib.sha256((HERE / "certified_enum.c").read_bytes()).hexdigest():
        sys.exit("the shell sees a different certified_enum.c")
    info = {"sources_sha256": sources_sha256(), "cflags": CFLAGS,
            "compiler": in_shell(f"{a.cc} --version | head -1").stdout.strip(),
            "binary_sha256": in_shell(f"sha256sum {shlex.quote(a.bin)}").stdout.split()[0]}
    pid = producer_of(info)
    enum_cmd = shlex.join(sh + [a.bin]) if sh else a.bin
    L.load(a.repo)
    grp = L.group(json.loads((HERE / "symmetry_generators.json").read_text())["generators"])
    jobs = []
    for (n1, e, c2) in inventory():
        use = slice_use(grp, n1)
        reps = L.orbit_reps(L.bvectors(n1, D_DEG - n1, e), use)
        for r, p_ in enumerate(reps):
            jobs.append((f"{n1}|{e}|{c2}|{r}", n1, e, c2, [list(t) for t in p_]))
        if not reps:
            jobs.append((f"{n1}|{e}|{c2}|NOB", n1, e, c2, None))
    out = Path(a.out)
    kept = {}
    if out.exists():
        for line in out.read_text().splitlines():
            r = json.loads(line)
            if r.get("producer") == pid and r["status"].split()[0] in ("COMPLETE", "EMPTY", "CONGRUENCE_EMPTY", "NO_BVECTOR"):
                kept[r["job"]] = r
    out.write_text("".join(json.dumps(r, separators=(",", ":")) + "\n" for r in kept.values()))
    todo = [j for j in jobs if j[0] not in kept]
    print(f"producer {pid} {info}; group order {len(grp)}; jobs {len(jobs)}, to run {len(todo)}", flush=True)
    todo_real = [j for j in todo if j[4] is not None]
    with out.open("a") as fh:
        for j in todo:
            if j[4] is None:
                rec = {"job": j[0], "d": D_DEG, "n1": j[1], "e": j[2], "c2min": j[3], "fixes": None,
                       "status": "NO_BVECTOR", "classes": [], "producer": pid, "producer_info": info}
                fh.write(json.dumps(rec, separators=(",", ":")) + "\n")
        fh.flush()
        with Pool(a.workers, initializer=winit, initargs=(a.repo, enum_cmd)) as pool:
            for k, rec in enumerate(pool.imap_unordered(run_job, todo_real, chunksize=1), 1):
                rec["producer"] = pid; rec["producer_info"] = info
                fh.write(json.dumps(rec, separators=(",", ":")) + "\n"); fh.flush()
                if k % 50 == 0 or rec["classes"]:
                    print(f"[{k}/{len(todo_real)}] {rec['job']} {rec['status'][:50]} classes={len(rec['classes'])}", flush=True)
    if in_shell(f"sha256sum {shlex.quote(a.bin)}").stdout.split()[0] != info["binary_sha256"]:
        sys.exit("binary changed during the run")


if __name__ == "__main__":
    main()
