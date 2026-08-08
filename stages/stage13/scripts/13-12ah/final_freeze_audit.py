#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

OUT = Path('stages/stage13/data/13-12ah/final_freeze_audit_report.json')
RESULT = Path('stages/stage13/13-12ah/result.md')
R03 = Path('review/STAGE13-FINAL-SELF-CONTAINED-20260809-R03.html')
R03_MANIFEST = Path('stages/stage13/data/13-12af/review_bundle_manifest.json')
AG = Path('stages/stage13/13-12ag/result.md')

MATH_COMMIT = 'c843e039306b40bd3693f89d6199da78c2fb4657'
R03_CONTENT_SHA = '0cf573e546d8e952f36ee5ed8f1f899b3718f0d29751cf4ee64640328ad37b93'
R03_LEDGER_SHA = '06e06c68ced77eb52ab937878f638243e9c43cb4dc4b02be9cba474a94bad2b2'
R03_SOURCE_SNAPSHOT = 'a6830e80f752fca327470ae3a79e2c88e038ae4e'
R03_BLOB = '6cf9b696cc02f2d556d8f67c30fb85ad77b57373'
R03_SOURCE_COUNT = 105
R03_HTML_BYTES = 1026122


def git_blob(path: Path) -> str:
    return subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise SystemExit(f'missing freeze lock: {needle}')


def build_report() -> dict:
    manifest = json.loads(R03_MANIFEST.read_text())
    result = RESULT.read_text()
    ag = AG.read_text()

    r03_ok = (
        manifest['bundle_id'] == 'STAGE13-FINAL-SELF-CONTAINED-20260809-R03'
        and manifest['content_sha256'] == R03_CONTENT_SHA
        and manifest['source_ledger_sha256'] == R03_LEDGER_SHA
        and manifest['source_snapshot_commit'] == R03_SOURCE_SNAPSHOT
        and manifest['source_count'] == R03_SOURCE_COUNT
        and manifest['html_bytes'] == R03_HTML_BYTES
        and R03.stat().st_size == R03_HTML_BYTES
        and git_blob(R03) == R03_BLOB
    )

    for needle in (
        'STAGE13_DOWNSTREAM_MATHEMATICAL_CONTENT=FROZEN',
        'R03_GROK_VERDICT=CLOSED',
        'R03_QWEN_VERDICT=CLOSED',
        'R03_CLAUDE_VERDICT=NOT_RECORDED',
        'R03_COPILOT_VERDICT=PENDING_FINAL_REVIEW',
        'UNANIMOUS_THREE_REVIEWER_CLOSED_RECORD=false',
        'STAGE13_THEOREM_CONSTANTS_CHANGED=false',
        'STAGE13_COUNTING_CONVENTION_CHANGED=false',
        'R03_ARTIFACT_MUTATED=false',
        'N_q(B)\\sim\\frac{\\kappa I_q}{3\\pi^3}B(\\log B)^3',
        'N_1(B)\\sim\\frac{\\kappa}{24\\pi}B(\\log B)^3',
        'J_q=\\frac{2I_q}{\\pi}',
        '\\lambda_p=\\frac{p+5}{2(p+1)}',
        'NEXT_STAGE13_ACTION=RECORD_COPILOT_VERDICT_OR_REOPEN_ONLY_ON_NEW_MAJOR',
    ):
        require(result, needle)

    for needle in (
        'w_q\\,d\\omega=d\\theta\\,d\\alpha',
        'N_{\\rm acc}',
        '\\frac{(p+1)^2}{2}',
        'Selberg--Delange / Tauberian hypothesis crosswalk',
    ):
        require(ag, needle)

    report = {
        'metadata': {
            'stage': '13-12ah',
            'scope': 'downstream mathematical freeze bookkeeping; no new theorem content',
        },
        'frozen_math': {
            'commit': MATH_COMMIT,
            'contract': 'R03_PLUS_13_12AG',
            'directional_asymptotic': 'N_q(B) ~ kappa I_q/(3 pi^3) B(log B)^3',
            'exactly_one_total': 'N_1(B) ~ kappa/(24 pi) B(log B)^3',
            'normalized_vector': [
                0.5347369332313988,
                0.24535917783225203,
                0.21990388893634913,
            ],
            'counting_convention_changed': False,
            'theorem_constants_changed': False,
        },
        'review_record': {
            'r03_grok': 'CLOSED',
            'r03_qwen': 'CLOSED',
            'r03_claude': 'NOT_RECORDED',
            'r03_copilot': 'PENDING_FINAL_REVIEW',
            'unanimous_three_reviewer_closed_record': False,
        },
        'r03_identity': {
            'bundle_id': 'STAGE13-FINAL-SELF-CONTAINED-20260809-R03',
            'content_sha256': R03_CONTENT_SHA,
            'source_ledger_sha256': R03_LEDGER_SHA,
            'source_snapshot_commit': R03_SOURCE_SNAPSHOT,
            'source_count': R03_SOURCE_COUNT,
            'html_bytes': R03_HTML_BYTES,
            'git_blob': R03_BLOB,
            'physically_frozen': r03_ok,
        },
        'post_r03_explicitness': {
            'coarea_bridge_written': True,
            'inert_character_sum_written': True,
            'selberg_delange_crosswalk_written': True,
        },
        'downstream_rule': {
            'stage14_may_use_frozen_contract': True,
            'reopen_on_copilot_fatal_or_major': True,
            'copilot_closed_requires_math_change': False,
            'new_review_bundle_if_reopened': 'R04_OR_LATER',
        },
        'scope_locks': {
            'perfect_cuboid_existence_claim': False,
            'perfect_cuboid_nonexistence_claim': False,
            'explicit_convergence_rate_claim': False,
            'monotonicity_claim': False,
            'publication_grade_peer_review_claim': False,
        },
    }
    report['pass'] = bool(r03_ok)
    return report


def main() -> None:
    report = build_report()
    if not report['pass']:
        raise SystemExit('Stage13-12ah freeze audit failed')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'status': 'PASS',
        'frozen_math_commit': MATH_COMMIT,
        'r03_grok': report['review_record']['r03_grok'],
        'r03_qwen': report['review_record']['r03_qwen'],
        'r03_copilot': report['review_record']['r03_copilot'],
    }, indent=2))


if __name__ == '__main__':
    main()
