#!/usr/bin/env python3
"""Network-free replay of the post-Smith proper-Br2 adapter blocker."""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-semantic-u1-at2-to-proper-br2-dual-adapter-blocker.json"
before = CERT.read_bytes()
subprocess.run([sys.executable, str(HERE / "certify_j2_semantic_u1_at2_to_proper_br2_dual_adapter_blocker.py")], check=True)
assert CERT.read_bytes() == before
obj = json.loads(before)
assert obj["exact_new_progress"]["prior_missing_rows_and_Smith_V_blocker_resolved"] is True
assert obj["exact_shortcut_rejection"]["copied_vector_is_joint_V4_invariant"] is False
assert obj["exact_missing_interface"]["proper_Br2_14D_coordinate_materialized"] is False
assert obj["promotion_firewall"]["finite_v4_kummer_columns_materialized"] == 0
print("STAGE33_12_J2_U1_AT2_TO_PROPER_BR2_ADAPTER_BLOCKER=PASS_EXACT")
