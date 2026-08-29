#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

audit = json.loads((HERE / "j2-good-reduction-etale-specialization-route-audit.json").read_text(encoding="utf-8"))
tcert = json.loads((HERE / "j2-kc-transcendental-lattice-isometry.json").read_text(encoding="utf-8"))
bcert = json.loads((HERE / "j2-kc-bfield-halfdual-target.json").read_text(encoding="utf-8"))
direct = json.loads((HERE / "j2-direct-bfield-cycle-evaluation-interface-block.json").read_text(encoding="utf-8"))
norm = json.loads((HERE / "j2-normalization-2isogeny-rational-torsion.json").read_text(encoding="utf-8"))

locks = audit["source_locks"]
assert tcert["canonical_sha256"] == locks["transcendental_lattice_certificate_canonical_sha256"]
assert bcert["canonical_sha256"] == locks["halfdual_target_certificate_canonical_sha256"]
assert direct["canonical_sha256"] == locks["direct_cycle_block_certificate_canonical_sha256"]
assert norm["canonical_sha256"] == locks["normalization_2torsion_certificate_canonical_sha256"]

assert tcert["transcendental_lattice_isometry_gram"] == [[4, 0], [0, 8]]
assert tcert["transcendental_marking_materialized"] is False
assert bcert["exact_consequence"]["named_j2_brauer_coordinate_materialized"] is False
assert audit["retained_exact_inputs"]["j2_independent_elliptic_2torsion_image"] == [0, 0]
assert audit["route_audit"]["candidate_count_before"] == 3
assert audit["route_audit"]["candidate_count_after"] == 3
assert audit["route_audit"]["named_j2_independent_observation_added"] is False
assert audit["route_audit"]["route_status"] == "EQUIVALENT_BLOCKED_BY_SAME_MARKING_INTERFACE"
assert audit["cycle_guard"]["exhaustive_view_audit_required_now"] is True
assert audit["cycle_guard"]["blind_rediscovery_required_now"] is True
assert audit["firewalls"]["stage33_12_closed_exact"] is False
assert audit["firewalls"]["stage33_13_released"] is False

payload = dict(audit)
claimed = payload.pop("canonical_sha256")
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
assert hashlib.sha256(canonical).hexdigest() == claimed

print("PASS_STAGE33_12_J2_GOOD_REDUCTION_ETALE_SPECIALIZATION_ROUTE_AUDIT")
