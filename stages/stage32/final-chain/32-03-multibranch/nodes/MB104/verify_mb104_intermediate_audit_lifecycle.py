#!/usr/bin/env python3
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
INV = ROOT / "docs/research-os/policies/repo-workflow-trigger-inventory-20260911.json"
STATE = ROOT / "stages/stage32/final-chain/32-03-multibranch/STATE.json"
HERE = Path(__file__).resolve().parent
FREEZE = HERE / "MB104-INTERMEDIATE-HOSTILE-REAUDIT-FREEZE.json"
WF_DIR = ROOT / ".github/workflows"
AUDIT_WF = ".github/workflows/stage32-mb-intermediate-audit-checkpoint.yml"
RETIRED_Z40 = {
    ".github/workflows/stage32-mb-z40-p-null-picard64.yml",
    ".github/workflows/stage32-mb-z40-picard64.yml",
}

def req(ok, msg):
    if not ok:
        raise SystemExit("FAIL: " + msg)

def git_blob(rel):
    return subprocess.check_output(["git", "hash-object", str(ROOT / rel)], text=True).strip()

def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()

def event_names(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^on:\s*", line):
            tail = line.split(":", 1)[1].strip()
            if tail:
                if tail.startswith("[") and tail.endswith("]"):
                    return {x.strip().strip("'\"") for x in tail[1:-1].split(",") if x.strip()}
                return {tail.strip("'\"")}
            out = set()
            for line2 in lines[i+1:]:
                if not line2.strip() or line2.lstrip().startswith("#"):
                    continue
                if not line2.startswith((" ", "\t")):
                    break
                m = re.match(r"^\s{2}([A-Za-z0-9_-]+)\s*:", line2)
                if m:
                    out.add(m.group(1))
            return out
    return set()

def main():
    freeze = json.loads(FREEZE.read_text())
    req(freeze["schema"] == "STAGE32_MB104_INTERMEDIATE_HOSTILE_REAUDIT_FREEZE_V1", "freeze schema")
    boundary = freeze["retained_boundary_sha"]
    req(re.fullmatch(r"[0-9a-f]{40}", boundary) is not None, "freeze sha")
    subprocess.run(["git", "merge-base", "--is-ancestor", boundary, "HEAD"], check=True)

    allowed = set(freeze["allowed_post_boundary_repair_paths"])
    changed = set(filter(None, git("diff", "--name-only", f"{boundary}..HEAD").splitlines()))
    unauthorized = changed - allowed
    req(not unauthorized, f"post-freeze substantive/unapproved paths: {sorted(unauthorized)}")

    # Explicitly include and freeze the isotropic-shell preflight that was appended before d13.
    base = "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/"
    for rel, expected in freeze["isotropic_shell_assets"].items():
        req(git_blob(base + rel) == expected, f"isotropic-shell frozen blob {rel}")
    req(freeze["scope"]["isotropic_shell_preflight_included"] is True, "isotropic preflight in scope")
    req(freeze["scope"]["isotropic_shell_execution_result_included"] is False, "no isotropic execution result")
    req(freeze["scope"]["isotropic_shell_credit"] is False, "no isotropic credit")
    req(freeze["scope"]["substantive_research_after_boundary_authorized"] is False, "freeze authority")
    req(all(v is False for v in freeze["firewalls"].values()), "freeze credit firewalls")

    inv = json.loads(INV.read_text())
    cls = {k: set(v) for k, v in inv["classifications"].items()}
    req(set(cls) == {"ACTIVE_AUTO", "MANUAL", "RETIRED"}, "classification keys")
    req(not (cls["ACTIVE_AUTO"] & cls["MANUAL"]), "ACTIVE/MANUAL disjoint")
    req(not (cls["ACTIVE_AUTO"] & cls["RETIRED"]), "ACTIVE/RETIRED disjoint")
    req(not (cls["MANUAL"] & cls["RETIRED"]), "MANUAL/RETIRED disjoint")

    actual = {
        str(p.relative_to(ROOT)).replace("\\", "/")
        for p in WF_DIR.iterdir()
        if p.is_file() and p.suffix in {".yml", ".yaml"}
    }
    classified = cls["ACTIVE_AUTO"] | cls["MANUAL"] | cls["RETIRED"]
    req(actual == classified, f"workflow inventory mismatch missing={sorted(actual-classified)} stale={sorted(classified-actual)}")
    req(AUDIT_WF in cls["ACTIVE_AUTO"], "audit workflow must be ACTIVE_AUTO")
    req(RETIRED_Z40 <= cls["RETIRED"], "Z40 workflows must be RETIRED")

    counts = inv["counts"]
    req(counts["ACTIVE_AUTO"] == len(cls["ACTIVE_AUTO"]), "ACTIVE_AUTO count")
    req(counts["MANUAL"] == len(cls["MANUAL"]), "MANUAL count")
    req(counts["RETIRED"] == len(cls["RETIRED"]), "RETIRED count")
    req(counts["TOTAL"] == len(actual), "TOTAL count")

    for rel in sorted(cls["MANUAL"] | cls["RETIRED"]):
        ev = event_names((ROOT / rel).read_text())
        req(ev <= {"workflow_dispatch"}, f"nonautomatic lifecycle violated by {rel}: {sorted(ev)}")

    for rel in RETIRED_Z40:
        txt = (ROOT / rel).read_text()
        req("Lifecycle: RETIRED" in txt, f"retired prose mismatch {rel}")
        req(event_names(txt) == {"workflow_dispatch"}, f"Z40 dispatch-only {rel}")

    # STATE remains the controller selecting the audit leaf. The immutable exact retained
    # boundary is deliberately kept in the small freeze manifest because STATE is >64 KiB.
    st = json.loads(STATE.read_text())
    req(st["status"] == "FROZEN_FOR_INTERMEDIATE_HOSTILE_REAUDIT_NO_CREDIT", "STATE freeze")
    req(st["next_obligation"]["active_leaf"] == "MB104-INTERMEDIATE-HOSTILE-REAUDIT-REPAIR-CHECKPOINT", "STATE audit leaf")
    req(st["routing"]["intermediate_audit_freeze"] is True, "audit freeze routing")
    req(st["routing"]["substantive_research_append_blocked_until_reaudit_pass"] is True, "append firewall")

    pm = st["retained_frontier"]["pair_map_audit_repair"]
    req(pm["status"] == "PRE_AUDIT_CORRECTED_ZERO_EXCLUSION_CREDIT_FROZEN_FOR_REAUDIT", "pair-map state status")
    for field in ("restriction_certificate", "restriction_note", "discriminant_certificate", "discriminant_note", "verifier"):
        req(git_blob(pm[field + "_path"]) == pm[field + "_blob"], f"pair-map blob lock {field}")

    r4 = st["retained_frontier"]["shallow_fresh_weapon_portfolio_r4"]
    req(r4["status"] == "POST_FAIL_RETAINED_BUT_FROZEN_PRE_AUDIT_NO_CREDIT", "R4 frozen status")
    for field in ("note", "certificate", "verifier"):
        req(git_blob(r4[field + "_path"]) == r4[field + "_blob"], f"R4 blob lock {field}")

    req(all(v is False for v in st["credit_firewall"].values()), "STATE credit firewall")

    print("PASS: MB104 intermediate audit lifecycle/controller boundary")
    print("retained freeze boundary", boundary)
    print("post-boundary changed paths", sorted(changed))
    print("all post-boundary paths are bounded audit repairs")
    print(f"workflow inventory total={len(actual)} active={len(cls['ACTIVE_AUTO'])} manual={len(cls['MANUAL'])} retired={len(cls['RETIRED'])}")
    print("MANUAL/RETIRED definitions are dispatch-only")
    print("isotropic-shell preflight included at frozen boundary with zero execution/credit")
    print("STATE remains frozen; pair-map/R4 source locks exact")

if __name__ == "__main__":
    main()
