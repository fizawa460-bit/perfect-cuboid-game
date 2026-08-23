#!/usr/bin/env python3
import hashlib
import json
import pathlib

import PyNormaliz
from PyNormaliz import Cone

ROOT = pathlib.Path(__file__).resolve().parent
CORE_PATH = ROOT / "picard-core.json"
OUT_PATH = ROOT / "normaliz-polyhedral-pilot.json"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_SCHEMA = "STAGE32_PICARD_CORE_INDLIST_V1"

core = json.loads(CORE_PATH.read_text(encoding="utf-8"))
if core.get("schema") != EXPECTED_SCHEMA:
    raise SystemExit("wrong Picard-core schema")
if core.get("source", {}).get("git_blob_sha1") != EXPECTED_BLOB:
    raise SystemExit("Picard core is not bound to the pinned upstream blob")
if core.get("rank") != 64 or core.get("known_class_count") != 140 or core.get("h2") != 16:
    raise SystemExit("Picard-core invariant mismatch")

# Verify the artifact's canonical digest before using it as the numerical base.
claimed_digest = core.get("canonical_sha256_without_this_field")
unsigned = dict(core)
unsigned.pop("canonical_sha256_without_this_field", None)
actual_digest = hashlib.sha256(
    json.dumps(unsigned, separators=(",", ":"), sort_keys=True).encode("utf-8")
).hexdigest()
if claimed_digest != actual_digest:
    raise SystemExit("Picard-core canonical digest mismatch")

gram = core["basis_gram"]
h = core["hyperplane"]
ineq = core["raw_cross_pairings_with_basis"]
if len(gram) != 64 or any(len(r) != 64 for r in gram):
    raise SystemExit("bad 64x64 Gram matrix")
if len(h) != 64 or len(ineq) != 140 or any(len(r) != 64 for r in ineq):
    raise SystemExit("bad Picard-core vectors")
if int(core["basis_gram_determinant"]) == 0:
    raise SystemExit("singular Picard basis")

# Functional x -> H.x in the chosen integral Picard basis.
hform = [sum(h[i] * gram[i][j] for i in range(64)) for j in range(64)]
h2 = sum(h[i] * hform[i] for i in range(64))
if h2 != 16:
    raise SystemExit(f"reconstructed H^2 mismatch: {h2}")

# Every genuinely new irreducible curve is distinct from each of the frozen
# 140 irreducible curves/exceptional divisors, hence has nonnegative
# intersection with all of them.  The recession cone of a fixed-degree slice
# is exactly C cap ker(H), where C is this 140-halfspace cone.  The 64 basis
# rows among these inequalities have nonsingular Gram matrix, so C has no
# lineality.  Therefore the degree slices are bounded iff C cap ker(H)={0}.
# Normaliz checks that homogeneous tail cone exactly, with integer arithmetic.
tail = Cone(inequalities=ineq, equations=[hform])
tail_rays = tail.ExtremeRays()
tail_subspace = tail.MaximalSubspace()
compact = len(tail_rays) == 0 and len(tail_subspace) == 0

# If compact, also inspect the full cone's extreme rays and verify H is
# strictly positive on every one. This is a redundant exact certificate and
# is useful for later graded enumeration design.
full_ray_count = None
min_h_on_ray = None
max_h_on_ray = None
nonpositive_ray_count = None
if compact:
    cone = Cone(inequalities=ineq)
    rays = cone.ExtremeRays()
    heights = [sum(hform[i] * r[i] for i in range(64)) for r in rays]
    full_ray_count = len(rays)
    min_h_on_ray = min(heights) if heights else None
    max_h_on_ray = max(heights) if heights else None
    nonpositive_ray_count = sum(1 for x in heights if x <= 0)
    if nonpositive_ray_count != 0:
        compact = False

version = None
for attr in ("__version__", "version"):
    value = getattr(PyNormaliz, attr, None)
    if value is not None:
        version = str(value)
        break
if version is None:
    try:
        version = str(PyNormaliz.NmzVersion())
    except Exception:
        version = "unknown"

payload = {
    "schema": "STAGE32_NORMALIZ_POLYHEDRAL_PILOT_V1",
    "success": True,
    "pynormaliz_version": version,
    "upstream_blob": EXPECTED_BLOB,
    "picard_core_sha256": actual_digest,
    "ambient_rank": 64,
    "known_halfspace_count": 140,
    "basis_gram_determinant": int(core["basis_gram_determinant"]),
    "h2": h2,
    "tail_equation": "H.x=0",
    "tail_extreme_ray_count": len(tail_rays),
    "tail_maximal_subspace_count": len(tail_subspace),
    "fixed_positive_degree_slices_compact": compact,
    "full_cone_extreme_ray_count": full_ray_count,
    "min_h_on_extreme_ray": min_h_on_ray,
    "max_h_on_extreme_ray": max_h_on_ray,
    "nonpositive_h_extreme_ray_count": nonpositive_ray_count,
    "raw_rank63_cvp_started": False,
}
OUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))

# A noncompact result is mathematically informative rather than a tool error,
# so the script exits successfully either way. Workflow failure is reserved for
# invalid source locks, corrupt artifacts, or Normaliz/runtime failures.
