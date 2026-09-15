#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CHECKPOINT = HERE / 'bc2-36-fresh-unknown52-replay-checkpoint.json'
RUNKEY = ROOT / 'runkeys/bc2-36-fresh-unknown52-replay.json'
SOURCE = HERE / 'bc2_36_replay_explicit_fresh_unknown52.py'
PREFLIGHT = HERE / 'bc2-36-fresh-unknown52-replay-preflight.json'
B32 = HERE / 'bc2_32_replay_explicit_fresh_unknown170.py'
B19 = HERE / 'bc2_19_n354_survivor_normal_positivity_mass_replay.py'
B18 = HERE / 'bc2_18_n354_survivor_exceptional_mod8_decomposition.py'
STATE = ROOT / 'MAIN-STATE.json'
WORKFLOW = HERE.parents[2] / '.github/workflows/stage32-ex5-main.yml'

CP_BLOB = '09ac58349e388c479ac77e04724bef2fd9b49b7e'
CP_CANON = 'e92cd6d07299b833a79fe20b81e9de032d61790cf1b7a6fb81ec6adccdb49fdf'
RUNKEY_BLOB = '78d9c847863232b10d149b651c32c668887e4b23'
SOURCE_BLOB = '18f9c2146d5dc97400c4af1a8691560523cc03cf'
PREFLIGHT_BLOB = 'aa9bf40cf3550cae33cdfe8669aa51a80acddcec'
PREFLIGHT_CANON = 'b2cc1cd97fe8da4504da980aa1c470f1aa419f9417b3eea8b1533305382155b0'
B32_BLOB = '7cfe8450cb9b9ab7f04da797d487655505598b93'
B19_BLOB = 'b2899aa228e7a3ee97526e3787ffbefa483530b4'
B18_BLOB = '1e2ed93cae3c5b446c8d90c1ae2250be83289c79'
TARGET_SHA = '95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818'
UNKNOWN_SHA = '570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9'
STATUS_SHA = '59c8f444d235a7b3223d2ef4df5c2da65636f66edc3f69ebd2572c2d3354dff8'
AUDIT_HEAD = '9c63ccb48dd0e5bdeedda7739dd05e2404698465'
AUDIT_REVIEW = 5188625406
V35 = 'STAGE32EX5_MAIN_COMPACT_STATE_V35_BC2_40_AUDIT_PASS_CONSUMED'


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit('FAIL: ' + message)


def blob(path: Path) -> str:
    return subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop('canonical_sha256_without_this_field', None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def main() -> None:
    req(blob(CHECKPOINT) == CP_BLOB, 'checkpoint blob')
    cp = json.loads(CHECKPOINT.read_text())
    req(cp['schema'] == 'STAGE32EX5_BC2_36_FRESH_UNKNOWN52_REPLAY_V1', 'checkpoint schema')
    req(cp['canonical_sha256_without_this_field'] == CP_CANON and canon(cp) == CP_CANON, 'checkpoint canonical')
    replay = cp['replay']
    req((replay['parents_checked'], replay['unsat_count'], replay['unknown_count'], replay['sat_count']) == (52, 11, 41, 0), 'partition counts')
    req(replay['per_parent_timeout_ms'] == 100000, 'timeout contract')
    req(replay['unknown_parent_indices_sha256'] == UNKNOWN_SHA and replay['status_stream_sha256'] == STATUS_SHA, 'partition hashes')
    req(len(replay['unknown_parent_indices']) == 41 and len(replay['unsat_parent_indices']) == 11, 'partition identities')
    req(set(replay['unsat_parent_indices']).isdisjoint(replay['unknown_parent_indices']), 'partition disjointness')
    target = cp['target']
    req(target['audited_bc2_35_unknown_count'] == 52 and target['parent_indices_sha256'] == TARGET_SHA, 'target identity')
    req(target['prior_audited_unsat_count'] == 7284, 'prior audited lower bound')
    req(sorted(target['parent_indices']) == sorted(replay['unsat_parent_indices'] + replay['unknown_parent_indices'] + replay['sat_parent_indices']), 'target partition')
    req(cp['credit']['known_parent_unsat_count_lower_bound'] == 7295 and cp['credit']['new_exact_parent_unsat_count'] == 11, 'checkpoint credit')
    req(cp['credit']['stage32_main_credit'] is False and cp['credit']['full178_complete'] is False, 'checkpoint credit firewall')
    req(cp['firewalls']['timeout_unknown_relabelled_unsat'] is False and cp['firewalls']['unknown_dropped'] is False, 'UNKNOWN firewall')

    req(blob(SOURCE) == SOURCE_BLOB and blob(PREFLIGHT) == PREFLIGHT_BLOB, 'BC2-36 source identity')
    req(blob(B32) == B32_BLOB and blob(B19) == B19_BLOB and blob(B18) == B18_BLOB, 'transitive source identity')
    pf = json.loads(PREFLIGHT.read_text())
    req(pf['canonical_sha256_without_this_field'] == PREFLIGHT_CANON and canon(pf) == PREFLIGHT_CANON, 'preflight canonical')

    req(blob(RUNKEY) == RUNKEY_BLOB, 'consumed runkey blob')
    rk = json.loads(RUNKEY.read_text())
    req(rk['generation'] == 1 and rk['armed'] is False, 'runkey consumed')
    receipt = rk['consumed_run']
    req(receipt['accepted_for_hostile_audit'] is True, 'run accepted for hostile audit')
    req(receipt['exact_head'] == '63986c900a34cbbfa00c96a0d2dcc38d3ffc92d5', 'execution head')
    req(receipt['workflow_run_id'] == 34718999232 and receipt['authorize_job_id'] == 103621253008 and receipt['compute_job_id'] == 103621306508, 'workflow provenance')
    req(receipt['artifact_id'] == 10306816385, 'artifact provenance')
    req(receipt['checkpoint_git_blob_sha'] == CP_BLOB and receipt['checkpoint_canonical'] == CP_CANON, 'checkpoint receipt binding')
    req((receipt['new_unsat_count'], receipt['remaining_unknown_count'], receipt['sat_count'], receipt['known_parent_unsat_count_lower_bound']) == (11, 41, 0, 7295), 'run counts')
    req(receipt['remaining_unknown_parent_indices_sha256'] == UNKNOWN_SHA and receipt['status_stream_sha256'] == STATUS_SHA, 'run identity hashes')

    state = json.loads(STATE.read_text())
    req(state['schema'] == V35, 'BC2-36 live state schema drift')
    prior = state['prior_audited_authority']['bc2_36_pr_1776']
    req(prior['hostile_audit_status'] == 'PASS', 'BC2-36 retained hostile audit status')
    req(prior['audit_checkpoint_exact_head'] == AUDIT_HEAD and prior['hostile_audit_review_id'] == AUDIT_REVIEW, 'BC2-36 retained hostile audit provenance')
    frontier = state['frontier']
    req(frontier['e8_bc2_36_audited'] is True, 'BC2-36 retained audited flag')
    req(frontier['e8_bc2_36_known_parent_unsat_count_lower_bound'] == 7295, 'BC2-36 retained lower bound')
    req(frontier['e8_known_parent_unsat_count_lower_bound'] == 7336, 'current EX5 audited lower bound')
    req(frontier['e8_bc2_40_audited'] is True and frontier['e8_bc2_40_remaining_unknown_count'] == 0 and frontier['e8_bc2_40_sat_count'] == 0, 'newer authority retention')
    req(frontier['e8_whole_first_block_unsat'] is True, 'first e8 block retained closure')
    req(frontier['population_wide_main_consumable_result_complete'] is False, 'MAIN adapter firewall')
    req(state['credit']['stage32_main_credit'] is False and state['credit']['FULL178_complete'] is False, 'current credit firewall')
    req(state['firewalls']['merge_authorized'] is False, 'merge firewall')

    wf = WORKFLOW.read_text()
    req('verify_bc2_36_targeted_replay_checkpoint.py' in wf, 'BC2-36 verifier absent from workflow')
    req('authorize-bc2-36-fresh-unknown52:' not in wf and '\n  bc2-36-fresh-unknown52:' not in wf, 'retired BC2-36 runtime job restored')

    print('PASS: Stage32EX5 BC2-36 retained checkpoint is V35-aware and fail-closed')
    print('bc2_36=11_NEW_UNSAT_41_RETAINED_UNKNOWN_0_SAT; audited_lower_bound=7295; current_EX5_lower_bound=7336')
    print('execution_head=63986c900a34cbbfa00c96a0d2dcc38d3ffc92d5; workflow=34718999232; artifact=10306816385')


if __name__ == '__main__':
    main()
