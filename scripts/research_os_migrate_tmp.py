from __future__ import annotations

import ast
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str, capture: bool = False) -> str:
    proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=capture, check=True)
    return proc.stdout if capture else ""


def commit(message: str) -> None:
    run("git", "commit", "-m", message)


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text)


def main() -> None:
    run("git", "config", "user.name", "github-actions[bot]")
    run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")

    # Commit 1: delete locator infrastructure.
    run("git", "rm", "-r", "docs/evidence-locator")
    run("git", "rm", ".github/workflows/evidence-locator-stage32-post1498.yml")
    commit("chore: remove evidence locator infrastructure")

    # Commit 2: make final artifacts the primary Research OS discovery surface.
    write(
        "AGENTS.md",
        """# Repository Guidelines

## Research OS

Follow `docs/research-os/README.md`.

Required behavior:
1. For existing results/evidence from prior Stages, start from the Stage's final artifact:
   - Stage 16 and later: `stages/stageNN/FINAL.md`.
   - Stages 12–15: the Stage's final HTML artifact; these Stages predate `FINAL.md` as the canonical final output.
2. Absence from a final artifact is not proof that the mathematics is absent from the repository. Do not recursively mine old Stage internals by default, but allow bounded, targeted repository search when a concrete research need justifies it.
3. Search `arsenal/` for reusable cross-Stage weapons; Arsenal is independent of prior-Stage evidence discovery and remains in use.
4. Read only small slices of the current Stage handoff/state/controller needed for decisions.
5. Do not recursively enumerate the whole repository unless a verifier/release script requires it or a concrete research question has opened a bounded targeted search.
6. During active development, keep these Research OS discovery rules and Arsenal maintenance instructions aligned with the repo's current canonical workflow.
""",
    )
    write(
        "docs/research-os/README.md",
        """# Research OS (Compact)

## Default execution path

1. For prior-Stage existing results/evidence, open the Stage's final artifact first:
   - Stage 16 and later: `stages/stageNN/FINAL.md`.
   - Stages 12–15: the Stage's final HTML artifact; these Stages use HTML rather than `FINAL.md` as their final output.
2. Treat the final artifact as the primary discovery surface, not a proof-completeness index. If the needed item is absent there, do not claim that it is mathematically absent from the repository. A bounded, targeted repository search is allowed when a concrete research need justifies it.
3. Search Arsenal for reusable cross-Stage weapons:
   - `python arsenal/search_arsenal.py "<need>" --top 10`
4. Read the **minimum** current-Stage state slice needed to act:
   - Stage `< 33`: `CURRENT.md` + `controller.json`
   - Stage `>= 33`: `MAIN-START-HERE.md` + `MAIN-STATE.json`
5. If the bounded discovery path yields no usable mechanism, emit a concrete stop state rather than recursively mining old payloads.

## Anti-sprawl contract

- Prior-Stage final artifact first: Stage 16+ uses `FINAL.md`; Stages 12–15 use the final HTML artifact.
- Arsenal remains the separate cross-Stage reusable-weapon surface.
- Small current-state slice next.
- No recursive `find`/`grep -R` over old Stage payloads during ordinary exploration.
- A concrete need may open a bounded targeted repository search; this exception must not become default historical re-mining.
- Verifiers may enumerate the exact generated/result sets they are responsible for.
""",
    )
    write(
        "docs/research-os/policies/repository-asset-discovery.md",
        """# Repository Asset Discovery Policy

This policy applies to Codex/agent repository exploration.

1. **Prior-Stage final artifact first**
   - Stage 16 and later: use each Stage's `FINAL.md` as the first discovery surface for existing results and evidence.
   - Stages 12–15: use each Stage's final HTML artifact; these Stages predate `FINAL.md` as the canonical final output.
   - A final artifact is a primary discovery surface, not a proof-completeness index.

2. **Bounded escalation when needed**
   - Failure to find an item in `FINAL.md` or the final HTML does **not** establish that the mathematics is absent from the repository.
   - Ordinary research should not recursively enumerate or repeatedly re-mine old Stage internals.
   - When a concrete research need identifies a plausible missing lemma, provenance edge, verifier input, generated asset, or other specific target, a bounded targeted repository search is allowed. Stop when that target is resolved or the bounded route is exhausted.

3. **Arsenal stays separate**
   - Query `arsenal/index.yaml` or `python arsenal/search_arsenal.py` for reusable general tools/methods.
   - Arsenal is the cross-Stage weapon surface and is intentionally retained; it is not a replacement for a Stage's final result/evidence artifact.

4. **Current state only**
   - Read only the minimum current-Stage handoff/state/controller slice required to decide the next action.
   - Do not turn ordinary discovery into whole-repository recursive exploration.

5. **Verifier boundaries**
   - Verifiers may enumerate their own exact generated/result directories. Exploration agents should not do so by default.
""",
    )
    run("git", "add", "AGENTS.md", "docs/research-os/README.md", "docs/research-os/policies/repository-asset-discovery.md")
    commit("docs: make final artifacts the primary discovery surface")

    # Commit 3: Stage32 only changes the discovery routing sentence.
    stage32 = ROOT / "stages/stage32/controller.json"
    data32 = json.loads(stage32.read_text())
    data32["anti_loop"]["asset_lookup_rule"] = (
        "Use prior-Stage final artifacts as the primary existing-result/evidence surface: "
        "Stage16+ FINAL.md and Stages12-15 final HTML. Absence there is not proof of repo-wide "
        "mathematical nonexistence; use bounded targeted repository search only when concretely justified. "
        "Arsenal remains the separate cross-Stage reusable-weapon surface."
    )
    stage32.write_text(json.dumps(data32, indent=2, ensure_ascii=False) + "\n")
    run("python", "-m", "json.tool", "stages/stage32/controller.json", capture=True)
    run("git", "add", "stages/stage32/controller.json")
    commit("refactor(stage32): remove evidence locator routing")

    # Commit 4: Stage33 retains mathematical state/results while replacing locator routing and guards.
    controller = ROOT / "stages/stage33/controller.json"
    data33 = json.loads(controller.read_text())
    data33["anti_loop"]["asset_lookup_rule"] = (
        "Use prior-Stage final artifacts as the primary existing-result/evidence surface: "
        "Stage16+ FINAL.md and Stages12-15 final HTML. Absence there is not proof of repo-wide "
        "mathematical nonexistence; use bounded targeted repository search only when concretely justified. "
        "Arsenal remains the separate cross-Stage reusable-weapon surface."
    )
    data33["post_v36_routing"] = {
        "status": "FINAL_ARTIFACT_FIRST_INTERNAL_EVIDENCE_ROUTE",
        "policy": "prior_stage_final_artifacts_first_arsenal_second_bounded_current_state_third",
        "primary_stage16_plus_surface": "FINAL.md",
        "primary_stage12_15_surface": "final HTML artifact",
        "stop_condition": (
            "Absence from the primary final artifacts is not a repo-wide nonexistence proof. Do not blindly "
            "re-mine old payloads; use a bounded targeted repository search only when a concrete research need "
            "justifies it."
        ),
    }
    data33["post_v37_routing"] = {
        "status": "FIRST_ASSET_TRIED_NO_LIFT_CERTIFIED",
        "first_asset": "stages/stage33/batch_postv36_existing_fullsurface_asset_check_v37.json",
        "first_asset_origin_stage": "stage32",
        "first_asset_h2_mu2_lift": "none",
        "next_queue": (
            "Continue only from a concretely justified final-artifact lead or bounded targeted-repository lead; "
            "otherwise stay at STOP. Absence from primary final artifacts is not a repo-wide nonexistence proof."
        ),
    }
    data33["post_v38_routing"] = {
        "status": "PRIOR_ASSET_QUEUE_EXHAUSTED_NO_LIFT",
        "all_prior_ranked_assets_checked": True,
        "all_full_surface_h2_mu2_lifts": "none",
        "all_col2_positive_bundles": "none",
        "anti_loop_stop": (
            "Do not replay the exhausted prior asset queue or blindly re-mine old Stage32 payloads, e3, or "
            "repeated row2/col2 scans. Stay at STOP unless a concrete final-artifact or bounded targeted-search "
            "lead opens a new route."
        ),
    }
    data33["post_v39_routing"] = {
        "status": "FINAL_ARTIFACT_FIRST_ROUTING_POLICY_RELEASED_ON_PRIOR_STOP",
        "policy_artifact": "docs/research-os/policies/repository-asset-discovery.md",
        "primary_stage16_plus_surface": "FINAL.md",
        "primary_stage12_15_surface": "final HTML artifact",
        "mandatory_next_step": "Inspect the relevant prior Stage final artifact first before attempting new construction.",
        "bounded_new_construction_gate": (
            "Absence from final artifacts does not prove repo-wide nonexistence. Use a bounded targeted repository "
            "search when concretely justified; otherwise preserve the prior STOP before speculative new construction."
        ),
        "fresh_evidence_reset": (
            "If final-artifact discovery or a justified targeted search yields usable evidence, verify that evidence "
            "before speculative construction."
        ),
        "forbidden_by_default": [
            "speculative one-parameter family hunting",
            "brute-force e3 search",
            "old Stage32 payload re-mining",
            "unbounded symbolic/numerical sweeps",
        ],
        "anti_loop_stop": "The prior asset queue remains certified exhausted; do not replay it blindly.",
    }
    locator_only = {
        "stages/stage33/j2-post-v35-evidence-locator-handoff-v36.json",
        "stages/stage33/batch_postv37_locator_queue_exhaustion_v38.json",
        "stages/stage33/j2-post-v38-locator-first-construction-policy-v39.json",
    }
    for field in ("artifact_requirements", "pull_request_needs_to_release"):
        if isinstance(data33.get(field), list):
            data33[field] = [x for x in data33[field] if x not in locator_only]
    controller.write_text(json.dumps(data33, ensure_ascii=False, separators=(",", ":")) + "\n")

    sync_path = ROOT / "stages/stage33/sync_main_state.py"
    source = sync_path.read_text()
    tree = ast.parse(source)
    remove_names = {"_guard_stage33_evidence_policy", "_validate_evidence_locator_head_binding"}
    remove_ranges = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in remove_names:
            remove_ranges.append((node.lineno, node.end_lineno))
    lines = []
    for lineno, line in enumerate(source.splitlines(), start=1):
        if any(start <= lineno <= end for start, end in remove_ranges):
            continue
        if "evidence_locator_" in line or "evidence_stage33" in line:
            continue
        if "_guard_stage33_evidence_policy(" in line or "_validate_evidence_locator_head_binding(" in line:
            continue
        lines.append(line)
    source = "\n".join(lines) + "\n"
    marker = '    ("post_v39_routing", "policy_artifact"),\n'
    if marker not in source:
        raise RuntimeError("post_v39 policy lock marker missing")
    source = source.replace(
        marker,
        marker
        + '    ("post_v39_routing", "primary_stage16_plus_surface"),\n'
        + '    ("post_v39_routing", "primary_stage12_15_surface"),\n',
        1,
    )
    ast.parse(source)
    sync_path.write_text(source)

    for path in sorted(locator_only):
        full = ROOT / path
        if full.exists():
            run("git", "rm", path)

    run("python", "-m", "py_compile", "stages/stage33/sync_main_state.py")
    run("python", "stages/stage33/sync_main_state.py", "--write")
    run("python", "stages/stage33/sync_main_state.py")
    run("git", "add", "stages/stage33/controller.json", "stages/stage33/sync_main_state.py", "stages/stage33/MAIN-STATE.json", "stages/stage33/MAIN-START-HERE.md")
    run("git", "add", "-u", "stages/stage33")
    commit("refactor(stage33): retire locator routing and sync guards")

    # Remove temporary migration machinery from the final tree before validating/pushing.
    run("git", "rm", ".github/workflows/research-os-retire-evidence-locator-migration.yml", "scripts/research_os_migrate_tmp.py")
    commit("chore: remove one-shot migration machinery")

    # Final head checks.
    if (ROOT / "docs/evidence-locator").exists():
        raise RuntimeError("docs/evidence-locator still exists")
    grep = subprocess.run(
        ["git", "grep", "-n", "-i", "-E", "evidence[-_ ]locator|docs/evidence-locator|query_evidence|locator[-_ ]first|locator queue", "--", "."],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if grep.returncode == 0:
        raise RuntimeError("Residual evidence-locator references:\n" + grep.stdout)
    if grep.returncode not in (0, 1):
        raise RuntimeError(grep.stderr)

    readme = (ROOT / "docs/research-os/README.md").read_text()
    for needle in ("Stage 16 and later", "Stages 12–15", "FINAL.md", "final HTML", "not a proof-completeness index"):
        if needle not in readme:
            raise RuntimeError(f"Research OS rule missing: {needle}")
    if not (ROOT / "arsenal").is_dir() or not (ROOT / "arsenal/search_arsenal.py").is_file():
        raise RuntimeError("Arsenal was not preserved")
    run("python", "arsenal/search_arsenal.py", "--help", capture=True)
    run("python", "-m", "json.tool", "stages/stage32/controller.json", capture=True)
    run("python", "-m", "json.tool", "stages/stage33/controller.json", capture=True)
    run("python", "-m", "py_compile", "stages/stage33/sync_main_state.py")
    run("python", "stages/stage33/sync_main_state.py")
    if run("git", "status", "--porcelain", capture=True).strip():
        raise RuntimeError("Final working tree is dirty")

    run("git", "push", "origin", "HEAD:research-os-retire-evidence-locator")


if __name__ == "__main__":
    main()
