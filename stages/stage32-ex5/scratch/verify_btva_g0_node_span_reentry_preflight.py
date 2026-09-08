#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ART = HERE / "btva-g0-node-span-reentry-preflight.json"
NODES = ROOT / "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json"
S29 = ROOT / "stages/stage29/29-02c-LG2/finite-search-contract.md"
G1 = ROOT / "stages/stage32/residual-32-01-production/post1648ad-genus1-node-span-preflight.json"
FULL178 = ROOT / "stages/stage32/residual-32-01-production/audit_stage32_post21bl_full178_node_support_preflight.py"

EXPECTED_ART_CANON = "6cc432791560d575963f5e544fa3ec051bdbbbe8f3a68fcdf8b69a261af166eb"
EXPECTED_NODE_BLOB = "f4a591bfac5e4e6e79b13309bdc006973d7c5b4e"
EXPECTED_NODE_CANON = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
P = 5
I_MOD_P = 2


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def canonical_without_field(obj: dict, field: str) -> str:
    cp = dict(obj)
    cp.pop(field, None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def q_i_mod5(coord: list[int]) -> int:
    rn, rd, inn, ind = map(int, coord)
    req(rd % P != 0 and ind % P != 0, "coordinate denominator divisible by 5")
    real = (rn % P) * pow(rd % P, -1, P) % P
    imag = (inn % P) * pow(ind % P, -1, P) % P
    return (real + I_MOD_P * imag) % P


def canonical_projective(v: tuple[int, ...]) -> tuple[int, ...]:
    first = next((x for x in v if x % P), None)
    req(first is not None, "zero projective node after reduction")
    inv = pow(first, -1, P)
    return tuple((x * inv) % P for x in v)


def load_reduced_nodes() -> list[tuple[int, ...]]:
    raw = json.loads(NODES.read_text())
    req(git_blob_sha1(NODES) == EXPECTED_NODE_BLOB, "node-coordinate blob drift")
    req(raw.get("canonical_sha256") == EXPECTED_NODE_CANON, "node-coordinate canonical marker drift")
    models = raw.get("exceptional_models", [])
    req(len(models) == 48, "expected 48 exceptional/node models")
    pts = []
    for model in models:
        coords = model.get("node_point_ambient_P6_L_basis")
        req(isinstance(coords, list) and len(coords) == 7, "node P6 coordinate length drift")
        v = tuple(q_i_mod5(c) for c in coords)
        pts.append(canonical_projective(v))
    req(len(set(pts)) == 48, "48 nodes cease to be distinct modulo (2-i)")
    return pts


def enumerate_hyperplanes(points: list[tuple[int, ...]]) -> tuple[int, int, int]:
    # Every projective hyperplane over F5 has a unique representative whose
    # first nonzero coefficient is 1. There are (5^7-1)/(5-1)=19531.
    total = 0
    max_incidence = -1
    max_count = 0
    for first in range(7):
        for tail in itertools.product(range(P), repeat=6-first):
            h = [0] * 7
            h[first] = 1
            h[first + 1 :] = tail
            total += 1
            inc = sum(sum(a * b for a, b in zip(h, pt)) % P == 0 for pt in points)
            if inc > max_incidence:
                max_incidence = inc
                max_count = 1
            elif inc == max_incidence:
                max_count += 1
    return total, max_incidence, max_count


def main() -> None:
    art = json.loads(ART.read_text())
    req(art["schema"] == "STAGE32EX5_SCRATCH_BTVA_G0_NODE_SPAN_REENTRY_PREFLIGHT_V1", "schema drift")
    req(canonical_without_field(art, "canonical_sha256_without_this_field") == EXPECTED_ART_CANON, "artifact canonical replay drift")
    req(art["canonical_sha256_without_this_field"] == EXPECTED_ART_CANON, "artifact stored canonical drift")
    req(art["authority"] == "SCRATCH_NONAUTHORITATIVE", "scratch firewall lost")

    s29 = S29.read_text()
    req("exceptional-divisor incidence lower bounds from Testa--Stoll Lemma 21" in s29, "Stage29 prior incidence filter lock missing")
    req("known degree-<=6 classification subtraction" in s29, "Stage29 low-degree subtraction lock missing")

    g1 = json.loads(G1.read_text())
    req(g1["source_locks"]["external_theorem"]["doi"] == "10.2140/ant.2022.16.1377", "existing BTVA source lock drift")
    req(g1["decision"]["genus1_node_span_lane_exhausted_as_direct_obstruction"] is True, "existing genus-1 node-span anti-loop lost")
    req(g1["decision"]["Q602_excluded"] is False and g1["decision"]["O210_excluded"] is False, "existing genus-1 firewall drift")

    full178 = FULL178.read_text()
    req('"strong_support_not_reconstructed":True' in full178, "FULL178 strong-support gap marker missing")
    req('"rows":85' in full178, "FULL178 genus-0 residual row-count lock missing")
    req("required=math.ceil((d-16*g+16)/4)" in full178, "FSM node-support formula lock missing")

    points = load_reduced_nodes()
    total_h, max_h, max_h_count = enumerate_hyperplanes(points)
    req((total_h, max_h, max_h_count) == (19531, 24, 28), "F5 hyperplane census drift")

    active_degrees = list(range(8, 81, 2))
    automatic_degrees = list(range(82, 177, 2))
    req(len(active_degrees) == 37 and len(automatic_degrees) == 48, "genus-0 row partition drift")
    for d in automatic_degrees:
        required_support = math.ceil((d + 16) / 4)
        req(required_support >= 25, f"automatic span threshold failed at d={d}")
    req(math.ceil((80 + 16) / 4) == 24, "d=80 boundary drift")
    req(math.ceil((82 + 16) / 4) == 25, "d=82 boundary drift")

    geom = art["exact_node_geometry"]
    req(geom["projective_hyperplanes_F5_enumerated"] == total_h, "artifact hyperplane count drift")
    req(geom["maximum_nodes_on_one_F5_hyperplane"] == max_h, "artifact max-hyperplane incidence drift")
    req(geom["number_of_F5_hyperplanes_attaining_maximum"] == max_h_count, "artifact max-hyperplane multiplicity drift")

    ri = art["receiver_interaction"]
    req(ri["btva_span_potentially_active_degrees_even"] == active_degrees, "active degree block drift")
    req(ri["btva_span_potentially_active_row_count"] == 37, "active row count drift")
    req(ri["btva_span_automatic_rows"] == 48 and ri["btva_span_automatic_degree_min"] == 82, "automatic block drift")
    req(ri["strong_48bit_support_reconstructed_for_these_rows"] is False, "unsupported strong-support reconstruction asserted")

    rd = art["reentry_decision"]
    req(rd["strict_receiver_effect_obtained"] is False, "strict effect invented")
    req(rd["breadth_cycle_2_admitted"] is False and rd["main_state_change_authorized"] is False, "scratch preflight self-promoted")
    for key, value in art["firewalls"].items():
        req(value is False, f"firewall must remain false: {key}")

    print("PASS: BTVA genus-0 node-span scratch preflight; exact new predicate localized to 37 rows, but no strict receiver effect / EX5 re-entry yet")


if __name__ == "__main__":
    main()
