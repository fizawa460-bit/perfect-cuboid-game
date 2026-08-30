#!/usr/bin/env python3
"""Network-free verifier for the naive Shioda-Mitani factor-transport rejection."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-naive-shioda-mitani-factor-transport-rejection.json"
J2_CERT = HERE / "j2-normalization-2isogeny-rational-torsion.json"
T_CERT = HERE / "j2-kc-transcendental-lattice-isometry.json"

cert = json.loads(CERT.read_text(encoding="utf-8"))
stored = cert.pop("canonical_sha256")
canonical = hashlib.sha256(
    json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert canonical == stored == "1713ce4b2a88250e0110fc5b3863836f3b108e752e0911939b3687fc0540ab2b"

j2 = json.loads(J2_CERT.read_text(encoding="utf-8"))
tc = json.loads(T_CERT.read_text(encoding="utf-8"))
assert j2["canonical_sha256"] == cert["source_locks"]["j2_normalization_certificate_sha256"]
assert tc["canonical_sha256"] == cert["source_locks"]["kc_transcendental_lattice_certificate_sha256"]
assert j2["binary_quartic_invariants"]["jacobian_j"] == 1728
assert cert["j2_side"]["cm_field"] == "Q(i)"
assert cert["j2_side"]["quotient_isogenous_to_normalization"] is True

G = cert["kc_side"]["transcendental_gram"]
assert G == [[4, 0], [0, 8]]
a, b, c = G[0][0] // 2, G[0][1], G[1][1] // 2
D = b*b - 4*a*c
assert (a, b, c, D) == (2, 0, 4, -32)
assert cert["kc_side"]["binary_quadratic_form"] == [2, 0, 4]
assert cert["kc_side"]["discriminant"] == -32
assert cert["kc_side"]["shioda_mitani_tau"] == "i*sqrt(2)"
assert cert["kc_side"]["shioda_mitani_second_parameter"] == "2*i*sqrt(2)"
assert cert["kc_side"]["cm_field"] == "Q(sqrt(-2))"
assert cert["exact_obstruction"]["fields_equal"] is False
assert cert["exact_obstruction"]["elliptic_isogeny_from_j2_normalization_or_quotient_to_shioda_mitani_factor_possible"] is False
assert cert["route_status"] == "NAIVE_SHIODA_MITANI_ELLIPTIC_FACTOR_TRANSPORT_REJECTED_EXACTLY"

print(json.dumps({
    "status": "PASS_EXACT",
    "canonical_sha256": stored,
    "j2_cm_field": "Q(i)",
    "kc_shioda_mitani_cm_field": "Q(sqrt(-2))",
    "naive_factor_transport": "REJECTED_EXACTLY",
}, sort_keys=True))
