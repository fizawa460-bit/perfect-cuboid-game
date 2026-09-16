#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-GAMMAQ-ORIENTATION-NUMERICAL-WALL-CERTIFICATE.json"


def req(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


cert = json.loads(CERT.read_text())
req(cert["schema"] == "STAGE32_MB104_000707_E2_GAMMAQ_ORIENTATION_NUMERICAL_WALL_V1", "schema")
rr = root()

for lock in cert["source_locks"]:
    p = rr / lock["path"]
    if not p.is_file():
        raise SystemExit(f"SOURCE_LOCK_FAIL: missing {lock['id']}: {lock['path']}")
    got = blob_sha1(p)
    if got != lock["blob_sha1"]:
        raise SystemExit(f"SOURCE_LOCK_FAIL: {lock['id']}: expected {lock['blob_sha1']}, got {got}")

locks = {x["id"]: x for x in cert["source_locks"]}
gamma = json.loads((rr / locks["GAMMAQ_CERT"]["path"]).read_text())
node = json.loads((rr / locks["NODE_ORBIT_CERT"]["path"]).read_text())
pic = json.loads((rr / locks["PICARD_PARITY_CERT"]["path"]).read_text())
tors = (rr / locks["ZERO_QUARTIC_TORSION_NOTE"]["path"]).read_text()
energy = (rr / locks["A1_ENERGY_NOTE"]["path"]).read_text()

req(gamma["routing_consequence"]["ambient_generator_materialized"] is True, "gamma_Q generator source")
req(gamma["lifted_graph"]["gamma_Q_alpha_abs"] == 1, "gamma_Q nonzero source")
req(node["exact_residual_orbits"]["q1_supported_nodes"] == [8,9,10,11,32,33,34], "Q1 node block")
req(node["saturation_constraints"]["q1"] == "x8+x9+x10+x11+x32+x33+x34=28*l", "Q1 saturation source")
req(pic["exact_result"]["canonical_conditions"] == "x_j = 0 mod 2 for every supported node j", "all-even Picard source")
req("x8+x9+x10+x11 == 0 mod 4" in tors, "Q1 first mod4 source")
req("x32+x33+x34 == 0 mod 4" in tors, "Q1 last mod4 source")
req("y/2\n =84l^2+(1/8)sum_j d_j^2" in energy, "energy source")

# Exact affine algebra.  Represent the Q1 block by arbitrary integers x_j and integer l.
# Flip is x'_j=8l-x_j, so sum flip = 56l-sum x and centered d'_j=-d_j.
q1 = cert["q1_block"]
req(q1["nodes"] == [8,9,10,11,32,33,34], "cert Q1 block")
req(q1["orientation_flip"] == "x_j -> 8*l-x_j", "cert flip")
req(q1["centered_flip"] == "d_j -> -d_j", "cert centered flip")

# If original saturation sum is 28l, flipped sum is 56l-28l=28l.
req(56 - 28 == 28, "saturation invariant coefficient")
# all-even is preserved because 8*l is even for every integer l.
req(8 % 2 == 0, "all-even invariant")
# mod-4 constants for the 4- and 3-node subblocks.
req(4 * 8 % 4 == 0, "32l mod4 invariant")
req(3 * 8 % 4 == 0, "24l mod4 invariant")
# d -> -d preserves each square exactly.
for d in range(-25, 26):
    req((-d) * (-d) == d * d, "square energy invariant")

inv = cert["invariance"]
req(inv["all_even_picard64"] is True, "cert even invariant")
req(inv["q0_constraints_untouched"] is True, "Q0 untouched")
req(inv["square_energy"] == "sum_j d_j^2 preserved", "energy invariant cert")

w = cert["wolfram_crosscheck"]
req(w["sat_flip"] == "-sat", "Wolfram sat")
req(w["d_flip_plus_d"] == "zero_vector", "Wolfram d")
req(w["energy_flip_minus_energy"] == 0, "Wolfram energy")
req(w["mod4_first_flip_plus_original"] == "32*l", "Wolfram mod4 first")
req(w["mod4_last_flip_plus_original"] == "24*l", "Wolfram mod4 last")

route = cert["routing_consequence"]
req(route["gamma_Q_is_genuine_geometric_generator"] is True, "gamma_Q retained")
req(route["gamma_Q_orientation_alone_reduces_formal_allocation_set"] is False, "no allocation reduction")
req(route["current_numerical_package_distinguishes_q1_global_orientation"] is False, "orientation invisible")
req(route["conductor_loop_comparison_still_required"] is True, "conductor comparison required")

for key, value in cert["credit_firewall"].items():
    if key.endswith("_authorized") or key.endswith("_credit") or key.endswith("_closed") or key.endswith("_complete") or key.endswith("_computed") or key.endswith("_proved") or key.endswith("_claim"):
        req(value is False, f"firewall {key}")

print("PASS STAGE32_MB104_000707_E2_GAMMAQ_ORIENTATION_NUMERICAL_WALL_V1")
print("Q1_global_flip preserves saturation+even+mod4+energy; gamma_Q orientation alone adds no allocation equation; conductor_comparison=REQUIRED")
