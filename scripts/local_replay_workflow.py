#!/usr/bin/env python3
"""Replay a GitHub Actions workflow locally (local-first execution, docs/research-os/policies/local-first-execution.md).

Runs every `run:` step of the selected workflow jobs from the repository root with bash, in order, and writes an
exact-head local replay record (JSON) that can stand in for exact-head CI evidence (policy section 5).

Emulation (deliberately small):
  * `actions/checkout` with `path:` -> detached `git worktree` of the requested `ref` at that path (removed afterwards);
    `actions/checkout` without `path:` -> the current working tree (the replay targets the current HEAD).
  * other `uses:` steps (setup-python, upload-artifact, ...) are skipped and listed in the record.
  * `${{ github.sha }}`, `${{ github.event.pull_request.head.sha }}` -> HEAD; `github.event_name` -> 'pull_request';
    `github.event.pull_request.base.sha` -> merge-base(HEAD, origin/main); `github.event.action` -> 'synchronize';
    `github.event.pull_request.number` -> '0'; `github.ref` -> 'refs/heads/<branch>'.
  * `if:` supports `github.*` context values, `steps.<id>.outputs.<key>` (read from the step's $GITHUB_OUTPUT),
    `==`, `!=`, `&&`, `||`, `!`, `always()`, `success()`, `failure()`; anything else is reported as UNSUPPORTED_IF
    and the step is NOT run (fail closed: heavy steps are normally behind gate outputs).
Matrix jobs and `needs:` ordering are not emulated; such jobs are reported as SKIPPED_MATRIX.

usage: python scripts/local_replay_workflow.py .github/workflows/<file>.yml [--job JOB] [--out RECORD.json] [--allow-dirty]
"""
from __future__ import annotations

import argparse, datetime, json, os, platform, re, shutil, subprocess, sys, time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def sh(cmd, **kw):
    return subprocess.run(cmd, cwd=kw.pop("cwd", ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


def git(*args):
    r = sh(["git", *args])
    if r.returncode:
        raise SystemExit(f"git {' '.join(args)} failed: {r.stderr}")
    return r.stdout.strip()


def find_bash() -> str:
    if os.name != "nt":
        return "bash"
    for cand in (r"C:\Program Files\Git\bin\bash.exe", r"C:\Program Files\Git\usr\bin\bash.exe"):
        if Path(cand).is_file():
            return cand
    return shutil.which("bash") or "bash"


def subst(text: str, ctx: dict) -> str:
    def rep(m):
        expr = m.group(1).strip()
        for part in [p.strip() for p in expr.split("||")]:
            if part in ctx and ctx[part]:
                return ctx[part]
            if part.startswith("'") and part.endswith("'"):
                return part[1:-1]
        return ctx.get(expr, "")
    return re.sub(r"\$\{\{\s*(.*?)\s*\}\}", rep, text)


def eval_if(cond, ctx, failed, outputs):
    """Evaluate a step `if:`. Unsupported expressions return (False, 'UNSUPPORTED_IF'): fail closed = do NOT run
    (heavy steps are typically guarded by gate outputs, so running them by default would be unsafe)."""
    if cond is None:
        return (not failed), None
    c = str(cond).strip()
    c = re.sub(r"^\$\{\{\s*(.*?)\s*\}\}$", r"\1", c, flags=re.S)
    c = re.sub(r"\bsteps\.([A-Za-z0-9_-]+)\.outputs\.([A-Za-z0-9_-]+)",
               lambda m: repr(outputs.get(m.group(1), {}).get(m.group(2), "")), c)
    for k, v in ctx.items():
        c = re.sub(r"\b" + re.escape(k) + r"\b", repr(v), c)
    c = c.replace("always()", "True").replace("success()", repr(not failed)).replace("failure()", repr(failed))
    c = c.replace("cancelled()", "False").replace("&&", " and ").replace("||", " or ")
    c = re.sub(r"!(?!=)", " not ", c)
    try:
        val = bool(eval(c, {"__builtins__": {}}, {"true": True, "false": False}))
    except Exception:
        return False, "UNSUPPORTED_IF"
    uses_status = any(x in str(cond) for x in ("always()", "failure()", "cancelled()"))
    return (val if uses_status else (val and not failed)), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workflow")
    ap.add_argument("--job", action="append")
    ap.add_argument("--out")
    ap.add_argument("--allow-dirty", action="store_true")
    a = ap.parse_args()

    wf_path = (ROOT / a.workflow).resolve()
    wf = yaml.safe_load(wf_path.read_text(encoding="utf-8"))
    head = git("rev-parse", "HEAD")
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    dirty = git("status", "--porcelain")
    if dirty and not a.allow_dirty:
        raise SystemExit("working tree is not clean; commit first or pass --allow-dirty (the record will say so)")
    base = sh(["git", "merge-base", "HEAD", "origin/main"]).stdout.strip() or head
    ctx = {"github.sha": head, "github.event.pull_request.head.sha": head, "github.event_name": "pull_request",
           "github.event.pull_request.base.sha": base, "github.event.action": "synchronize",
           "github.event.pull_request.number": "0", "github.ref": f"refs/heads/{branch}", "github.workspace": str(ROOT),
           "runner.temp": str(ROOT / ".git" / "local-replay-tmp")}
    bash = find_bash()
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", GITHUB_WORKSPACE=str(ROOT), CI="true")
    env.update({k: str(v) for k, v in (wf.get("env") or {}).items()})
    record = {"schema": "LOCAL_REPLAY_RECORD_V1", "policy": "docs/research-os/policies/local-first-execution.md",
              "workflow": wf_path.relative_to(ROOT).as_posix(), "exact_head": head, "emulated_pr_base": base, "branch": branch,
              "working_tree_clean": not dirty, "dirty_paths": dirty.splitlines() if dirty else [],
              "started_utc": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
              "environment": {"os": platform.platform(), "python": sys.version.split()[0], "bash": bash,
                              "git": git("--version")}, "jobs": []}
    worktrees = []
    overall_ok = True
    try:
        for job_id, job in (wf.get("jobs") or {}).items():
            if a.job and job_id not in a.job:
                continue
            jrec = {"job": job_id, "steps": []}
            record["jobs"].append(jrec)
            if (job.get("strategy") or {}).get("matrix"):
                jrec["status"] = "SKIPPED_MATRIX"; continue
            jenv = dict(env); jenv.update({k: subst(str(v), ctx) for k, v in (job.get("env") or {}).items()})
            failed = False
            outputs: dict = {}
            for i, st in enumerate(job.get("steps") or []):
                name = st.get("name") or st.get("uses") or f"step{i}"
                srec = {"name": name}
                jrec["steps"].append(srec)
                run_it, note = eval_if(st.get("if"), ctx, failed, outputs)
                if note: srec["note"] = note
                if not run_it:
                    srec["status"] = "SKIPPED_IF"; continue
                if "uses" in st:
                    uses = st["uses"]; w = st.get("with") or {}
                    if uses.startswith("actions/checkout") and w.get("path"):
                        ref = subst(str(w.get("ref") or "HEAD"), ctx) or "HEAD"
                        dest = ROOT / w["path"]
                        if dest.exists():
                            sh(["git", "worktree", "remove", "--force", str(dest)])
                        r = sh(["git", "worktree", "add", "--detach", str(dest), ref])
                        if r.returncode:  # ref not present locally (e.g. a commit only reachable from a PR branch)
                            f = sh(["git", "fetch", "--quiet", "origin", ref])
                            srec["fetched_from_origin"] = f.returncode == 0
                            r = sh(["git", "worktree", "add", "--detach", str(dest), ref])
                        if r.returncode:
                            srec["status"] = "FAIL"; srec["stderr"] = r.stderr[-2000:]; failed = True; continue
                        worktrees.append(dest); srec["status"] = "EMULATED_WORKTREE"; srec["ref"] = ref
                    elif uses.startswith("actions/checkout"):
                        srec["status"] = "EMULATED_CURRENT_TREE"
                    else:
                        srec["status"] = "SKIPPED_USES"; srec["uses"] = uses
                    continue
                if "run" not in st:
                    srec["status"] = "SKIPPED_EMPTY"; continue
                script = subst(st["run"], ctx)
                senv = dict(jenv); senv.update({k: subst(str(v), ctx) for k, v in (st.get("env") or {}).items()})
                cwd = ROOT / st["working-directory"] if st.get("working-directory") else ROOT
                t0 = time.time()
                # pass the script through a file: Windows command-line quoting can corrupt long multi-line `-c` scripts
                tmpdir = ROOT / ".git" / "local-replay-tmp"; tmpdir.mkdir(exist_ok=True)
                sfile = tmpdir / f"{job_id}-{i}.sh"
                sfile.write_text(script, encoding="utf-8", newline="\n")
                senv.setdefault("GITHUB_OUTPUT", str(tmpdir / f"{job_id}-{i}.github_output"))
                senv.setdefault("GITHUB_ENV", str(tmpdir / f"{job_id}-{i}.github_env"))
                senv.setdefault("GITHUB_STEP_SUMMARY", str(tmpdir / f"{job_id}-{i}.summary"))
                senv.setdefault("RUNNER_TEMP", str(tmpdir))
                Path(senv["GITHUB_OUTPUT"]).write_text("", encoding="utf-8")
                r = subprocess.run([bash, "--noprofile", "--norc", "-eo", "pipefail", sfile.as_posix()], cwd=cwd, env=senv,
                                   capture_output=True, text=True, encoding="utf-8", errors="replace")
                srec["seconds"] = round(time.time() - t0, 1)
                srec["exit"] = r.returncode
                srec["stdout_tail"] = r.stdout[-1500:]
                if r.returncode:
                    srec["stderr_tail"] = r.stderr[-1500:]
                    srec["status"] = "FAIL"; failed = True
                else:
                    srec["status"] = "PASS"
                if st.get("id"):
                    kv = {}
                    for line in Path(senv["GITHUB_OUTPUT"]).read_text(encoding="utf-8", errors="replace").splitlines():
                        if "=" in line:
                            k, v = line.split("=", 1); kv[k.strip()] = v.strip()
                    outputs[st["id"]] = kv
                    srec["outputs"] = kv
                print(f"[{srec['status']}] {job_id} :: {name} ({srec['seconds']}s)", flush=True)
            jrec["status"] = "FAIL" if failed else "PASS"
            overall_ok &= not failed
    finally:
        for d in worktrees:
            sh(["git", "worktree", "remove", "--force", str(d)])
        sh(["git", "worktree", "prune"])
    record["finished_utc"] = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    record["verdict"] = "PASS" if overall_ok else "FAIL"
    record["skipped_uses"] = sorted({s.get("uses") for j in record["jobs"] for s in j["steps"] if s.get("status") == "SKIPPED_USES"})
    out = Path(a.out) if a.out else None
    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": record["verdict"], "exact_head": head, "working_tree_clean": not dirty,
                      "jobs": {j["job"]: j.get("status") for j in record["jobs"]}}, ensure_ascii=False))
    sys.exit(0 if overall_ok else 1)


if __name__ == "__main__":
    main()
