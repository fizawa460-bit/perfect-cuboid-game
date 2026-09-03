from __future__ import annotations

import ast
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_SHA = "ed5940413c11d8b4f315bed167702a0d5f23104f"
BRANCH = "research-os-retire-evidence-locator"


def run(*args: str, capture: bool = False) -> str:
    proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=capture, check=True)
    return proc.stdout if capture else ""


def commit(message: str) -> None:
    run("git", "commit", "-m", message)


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text)


def main() -> None:
    temp_head = run("git", "rev-parse", "HEAD", capture=True).strip()
    run("git", "config", "user.name", "github-actions[bot]")
    run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")

    # 1. Retire the locator implementation and its dedicated CI.
    run("git", "rm", "-r", "docs/evidence-locator")
    run("git", "rm", ".github/workflows/evidence-locator-stage32-post1498.yml")
    commit("chore: remove evidence locator infrastructure")

    # 2. Replace Research OS discovery policy with final-artifact-first routing.
    write("AGENTS.md", """# Repository Guidelines

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
""")
    write("docs/research-os/README.md", """# Research OS (Compact)

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
""")
    write("docs/research-os/policies/repository-asset-discovery.md", """# Repository Asset Discovery Policy

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
""")
    run("git", "add", "AGENTS.md", "docs/research-os/README.md", "docs/research-os/policies/repository-asset-discovery.md")
    commit("docs: make final artifacts the primary discovery surface")

    # 3. Stage32: only replace the old lookup routing sentence.
    p32 = ROOT / "stages/stage32/controller.json"
    d32 = json.loads(p32.read_text())
    d32["anti_loop"]["asset_lookup_rule"] = (
        "Use prior-Stage final artifacts as the primary existing-result/evidence surface: Stage16+ FINAL.md and "
        "Stages12-15 final HTML. Absence there is not proof of repo-wide mathematical nonexistence; use bounded "
        "targeted repository search only when concretely justified. Arsenal remains the separate cross-Stage reusable-weapon surface."
    )
    p32.write_text(json.dumps(d32, indent=2, ensure_ascii=False) + "\n")
    run("python", "-m", "json.tool", "stages/stage32/controller.json", capture=True)
    run("git", "add", "stages/stage32/controller.json")
    commit("refactor(stage32): remove evidence locator routing")

    # 4. Stage33: preserve mathematical results, retire locator-only routing/attestations.
    p33 = ROOT / "stages/stage33/controller.json"
    d33 = json.loads(p33.read_text())
    d33["research_os"]["asset_lookup_rule"] = (
        "prior-Stage final artifacts first (Stage16+ FINAL.md; Stages12-15 final HTML), Arsenal second, bounded "
        "current-state/targeted repository search third; absence from final artifacts is not repo-wide nonexistence proof"
    )
    for key in ("v36_handoff", "v38_locator_queue_exhaustion", "v39_locator_first_new_search"):
        d33.get("attestation", {}).pop(key, None)
    guard = d33["guard"]
    guard["post_v35_rule"] = (
        "use prior-Stage final artifacts as the primary evidence route (Stage16+ FINAL.md; Stages12-15 final HTML); "
        "Arsenal stays separate; do not rediscover old payload ad hoc"
    )
    guard["post_v37_rule"] = (
        "prior existing-asset check found no lift; preserve stop; resume from a concrete final-artifact lead or "
        "bounded targeted repository search when justified"
    )
    guard["post_v38_rule"] = (
        "prior ranked asset queue is exhausted with no lift; do not restart old origins by default; resume from a "
        "concrete final-artifact/targeted-search lead or genuinely new asset"
    )
    guard["post_v39_rule"] = (
        "newly-created/search-materialized asset search returned empty; preserve stop; resume on a new repository "
        "asset, concrete final-artifact/targeted-search lead, or explicit rerun trigger"
    )
    p33.write_text(json.dumps(d33, ensure_ascii=False, separators=(",", ":")) + "\n")

    sync = ROOT / "stages/stage33/sync_main_state.py"
    source = sync.read_text()
    removed_keys = ("v36_handoff", "v38_locator_queue_exhaustion", "v39_locator_first_new_search")
    source = "\n".join(
        line for line in source.splitlines()
        if not any(key in line for key in removed_keys)
    ) + "\n"
    ast.parse(source)
    sync.write_text(source)

    candidate_locator_files = [
        "stages/stage33/33-12/J2-POST-V35-EVIDENCE-LOCATOR-HANDOFF-V36.json",
        "stages/stage33/33-12/J2-LOCATOR-QUEUE-EXHAUSTION-V38.json",
        "stages/stage33/33-12/J2-LOCATOR-FIRST-NEW-SEARCH-V39.json",
        "stages/stage33/j2-post-v35-evidence-locator-handoff-v36.json",
        "stages/stage33/batch_postv37_locator_queue_exhaustion_v38.json",
        "stages/stage33/j2-post-v38-locator-first-construction-policy-v39.json",
    ]
    run("git", "rm", "-f", "--ignore-unmatch", *candidate_locator_files)
    run("python", "-m", "py_compile", "stages/stage33/sync_main_state.py")
    run("python", "stages/stage33/sync_main_state.py", "--write")
    run("python", "stages/stage33/sync_main_state.py")
    run("git", "add", "stages/stage33/controller.json", "stages/stage33/sync_main_state.py", "stages/stage33/MAIN-STATE.json", "stages/stage33/MAIN-START-HERE.md")
    run("git", "add", "-u", "stages/stage33")
    commit("refactor(stage33): retire locator routing and sync references")

    # Drop all temporary migration setup commits, leaving only the four reviewable changes above.
    run("git", "rebase", "--onto", BASE_SHA, temp_head)

    # Final branch checks before force-with-lease push.
    if (ROOT / "docs/evidence-locator").exists():
        raise RuntimeError("docs/evidence-locator still exists")
    if (ROOT / ".github/workflows/evidence-locator-stage32-post1498.yml").exists():
        raise RuntimeError("dedicated evidence-locator workflow still exists")
    residual = subprocess.run(
        ["git", "grep", "-n", "-i", "-E", "evidence[-_ ]locator|query_evidence|locator[-_ ]first|locator[-_ ]queue", "--", "."],
        cwd=ROOT, text=True, capture_output=True,
    )
    if residual.returncode == 0:
        raise RuntimeError("Residual evidence-locator references:\n" + residual.stdout)
    if residual.returncode != 1:
        raise RuntimeError(residual.stderr)

    readme = (ROOT / "docs/research-os/README.md").read_text()
    policy = (ROOT / "docs/research-os/policies/repository-asset-discovery.md").read_text()
    for text in (readme, policy):
        for needle in ("Stage 16", "Stages 12–15", "FINAL.md", "final HTML"):
            if needle not in text:
                raise RuntimeError(f"Research OS rule missing: {needle}")
    if "not a proof-completeness index" not in readme or "does **not** establish" not in policy:
        raise RuntimeError("absence-is-not-nonexistence rule missing")
    if not (ROOT / "arsenal").is_dir() or not (ROOT / "arsenal/search_arsenal.py").is_file():
        raise RuntimeError("Arsenal was not preserved")
    run("python", "arsenal/search_arsenal.py", "--help", capture=True)
    run("python", "-m", "json.tool", "stages/stage32/controller.json", capture=True)
    run("python", "-m", "json.tool", "stages/stage33/controller.json", capture=True)
    run("python", "-m", "py_compile", "stages/stage33/sync_main_state.py")
    run("python", "stages/stage33/sync_main_state.py")
    if run("git", "status", "--porcelain", capture=True).strip():
        raise RuntimeError("Final working tree is dirty")

    run("git", "push", "--force-with-lease", "origin", f"HEAD:{BRANCH}")


if __name__ == "__main__":
    main()
