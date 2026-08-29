#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

block = json.loads((HERE / "j2-direct-bfield-cycle-evaluation-interface-block.json").read_text(encoding="utf-8"))
tcert = json.loads((HERE / "j2-kc-transcendental-lattice-isometry.json").read_text(encoding="utf-8"))
bcert = json.loads((HERE / "j2-kc-bfield-halfdual-target.json").read_text(encoding="utf-8"))
descent = (ROOT / "stages" / "stage33" / "33-05" / "j2_arithmetic_descent.py").read_text(encoding="utf-8")

assert tcert["canonical_sha256"] == block["source_locks"]["transcendental_lattice_certificate_canonical_sha256"]
assert bcert["canonical_sha256"] == block["source_locks"]["halfdual_target_certificate_canonical_sha256"]
assert tcert["transcendental_lattice_isometry_gram"] == [[4, 0], [0, 8]]
assert tcert["transcendental_marking_materialized"] is False
assert bcert["marked_transcendental_lattice"]["basis"] == ["t1", "t2"]
assert bcert["exact_consequence"]["named_j2_brauer_coordinate_materialized"] is False
assert "Q_defined_CSA" in descent and "Creutz--Viray" in descent

ri = block["retained_interfaces"]
assert ri["named_j2_q_defined_csa_materialized"] is True
assert ri["transcendental_lattice_isometry_class_materialized"] is True
assert ri["transcendental_marking_materialized"] is False
assert ri["explicit_h2_cycle_representatives_for_t1_t2_materialized"] is False
assert ri["csa_or_bfield_pairing_adapter_to_explicit_t_cycles_materialized"] is False
assert block["exact_block"]["route_status"] == "BLOCKED_BY_MISSING_TRANSCENDENTAL_CYCLE_REALIZATION_INTERFACE"
assert block["exact_block"]["candidate_count_before"] == 3
assert block["exact_block"]["candidate_count_after"] == 3
assert block["firewalls"]["stage33_12_closed_exact"] is False
assert block["firewalls"]["stage33_13_released"] is False

payload = dict(block)
claimed = payload.pop("canonical_sha256")
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
assert hashlib.sha256(canonical).hexdigest() == claimed

print("PASS_STAGE33_12_J2_DIRECT_BFIELD_CYCLE_EVALUATION_INTERFACE_BLOCK")
