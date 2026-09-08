#!/usr/bin/env python3
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex4-05b-fsm-theta-level-homology-marking-preflight-scratch.json"

def canonical_sha256_without_field(obj):
    x = dict(obj)
    expected = x.pop("canonical_sha256_without_this_field")
    payload = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    actual = hashlib.sha256(payload).hexdigest()
    assert actual == expected, (actual, expected)

def det_mod(M, n):
    return (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % n

def reduce2(M):
    return tuple(v % 2 for row in M for v in row)

def act2(M, v):
    return (
        (M[0][0] * v[0] + M[0][1] * v[1]) % 2,
        (M[1][0] * v[0] + M[1][1] * v[1]) % 2,
    )

def main():
    obj = json.loads(ART.read_text())
    canonical_sha256_without_field(obj)

    assert obj["schema"] == "STAGE32EX4_EX4_05B_FSM_THETA_LEVEL_HOMOLOGY_MARKING_PREFLIGHT_SCRATCH_V1"
    assert obj["status"].startswith("SCRATCH_REPLAYABLE_")
    assert obj["claim_ceiling"]["absolute_W_line_identified"] is False
    assert obj["claim_ceiling"]["absolute_Q602_residue_identified"] is False
    assert obj["firewalls"]["elliptic_level_structure_promoted_to_genus2_homology_marking"] is False
    assert obj["firewalls"]["pairing_preserving_beta_promoted_to_frey_kani_anti_isometry"] is False

    mats = []
    for a, b, c, d in itertools.product(range(8), repeat=4):
        M = ((a, b), (c, d))
        if det_mod(M, 8) == 7:
            mats.append(M)
    assert len(mats) == 384

    red = Counter(reduce2(M) for M in mats)
    assert len(red) == 6
    assert set(red.values()) == {64}

    nonzero = {(1, 0), (0, 1), (1, 1)}
    assert set(red.keys()) == {
        (1, 0, 0, 1),
        (0, 1, 1, 0),
        (1, 0, 1, 1),
        (1, 1, 0, 1),
        (0, 1, 1, 1),
        (1, 1, 1, 0),
    }

    images = Counter(act2(M, (1, 0)) for M in mats)
    assert set(images) == nonzero
    assert sorted(images.values()) == [128, 128, 128]

    p = obj["optional_frey_kani_anti_isometry_preflight"]
    assert p["det_minus_one_matrix_count"] == 384
    assert p["reduction_mod2_distinct_matrices"] == 6
    assert p["lifts_per_mod2_matrix"] == 64
    assert p["fixed_nonzero_mod2_direction_image_counts"] == [128, 128, 128]

    d = obj["decision"]
    assert d["result"] == "EX4_05B_FSM_LEVEL_STRUCTURE_DOES_NOT_SUPPLY_BRANCH_LABELLED_BOLZA_HOMOLOGY_MARKING"
    assert d["absolute_W_line_identified"] is False
    assert d["absolute_Q602_residue_identified"] is False
    assert d["Q602_excluded"] is False
    assert d["O210_excluded"] is False
    assert d["stage32_main_credit"] is False

    print("PASS EX4-05B FSM theta-level homology marking preflight")
    print("det=-1 mod8 matrices: 384")
    print("mod2 image: GL2(F2), 6 matrices, 64 lifts each")
    print("fixed nonzero direction images: 128/128/128")

if __name__ == "__main__":
    main()
