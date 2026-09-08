#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
AR=ROOT/"stages/stage32/residual-32-01-production/post1648ar-two-factor-slack-minimal-branches.json"
V6=ROOT/"stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
OUT=Path(__file__).with_name("ar-fsm-uniform-v6-integration-20260909.json")
EXPECTED_AR="dba5756e4b10c8bd6e412f1027b8edf693fb74f9ea90f9b591cc99437746a8dd"
EXPECTED_V6="d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_OUT="91e01ca6df31cf8de9b8e2790ab329e8c760abc3a5d52de1ebaf166f5e77158e"

def csha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

ar=json.loads(AR.read_text())
v6=json.loads(V6.read_text())
out=json.loads(OUT.read_text())
assert ar["canonical_sha256_without_this_field"]==EXPECTED_AR
assert v6["canonical_sha256_without_this_field"]==EXPECTED_V6
assert ar["slack_identity"]["minimum_node_branches"]==238
assert ar["minimal_branch_bound"]["minimum_FSM_minimal_A_B_1_1_branches"]==186
m=[int(x) for x in v6["witness"]["all140_pairings"][92:]]
assert len(m)==48 and sum(m)==266 and sum(x>0 for x in m)==47
assert sum(min(x,10) for x in m)==232
labels=[i+1 for i,x in enumerate(m) if x>=11]
assert labels==[18,23,27,28,38,39,42,48]
excess=sorted((x-1 for x in m if x>0), reverse=True)
assert sum(excess[:23])==190
assert sum(excess[:24])==194

# AR: qsum = 80 - 2t - E; N = 266 - t.
# FSM: D_node/(8k)=sum(a+b-2)=266+qsum-2N.
# The t terms cancel exactly.
for t in range(29):
    qsum=80-2*t
    N=266-t
    assert 266+qsum-2*N==-186
assert 8*186==1488
assert 1488-2*186==1116

core=dict(out)
stored=core.pop("canonical_sha256_without_this_field")
assert stored==EXPECTED_OUT
assert csha(core)==EXPECTED_OUT
print(json.dumps({
    "verdict":"PASS_STAGE32_MAIN_SCRATCH_AR_FSM_UNIFORM_V6_INTEGRATION",
    "minimum_node_branches":238,
    "minimum_multibranch_nodes":24,
    "high_branch_threshold":11,
    "high_branch_candidate_labels":labels,
    "D_node":"-(1488+8E)k",
    "D_res_nonnode":"(1116+8E)k",
    "canonical_sha256":EXPECTED_OUT
},sort_keys=True))
