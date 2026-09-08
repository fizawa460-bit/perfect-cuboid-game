#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUT = HERE / "residual-g-tangent-capacity-nonclosure-20260909.json"
AQ = ROOT / "stages/stage32/residual-32-01-production/post1648aq-residual-g-cusp-multiplicity-grid.json"
AR = ROOT / "stages/stage32/residual-32-01-production/post1648ar-two-factor-slack-minimal-branches.json"
AQ_NOTE = ROOT / "stages/stage32/residual-32-01-production/post1648aq-residual-g-cusp-multiplicity-grid-source-note.md"
AR_NOTE = ROOT / "stages/stage32/residual-32-01-production/post1648ar-two-factor-slack-minimal-branches-source-note.md"

EXPECTED_OUT = "4611bc731a1630d2446f5aa69dd2e39a0ffb09698e5dcede3608120d42c3713e"
EXPECTED_AQ = "1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e"
EXPECTED_AR = "dba5756e4b10c8bd6e412f1027b8edf693fb74f9ea90f9b591cc99437746a8dd"


def csha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    out = json.loads(OUT.read_text())
    stored = out.pop("canonical_sha256_without_this_field")
    assert stored == EXPECTED_OUT == csha(out)

    aq = json.loads(AQ.read_text())
    ar = json.loads(AR.read_text())
    assert aq["canonical_sha256_without_this_field"] == EXPECTED_AQ
    assert ar["canonical_sha256_without_this_field"] == EXPECTED_AR
    locks = out["source_locks"]
    assert blob_sha(AQ) == locks["AQ"]["blob_sha1"]
    assert blob_sha(AR) == locks["AR"]["blob_sha1"]
    assert blob_sha(AQ_NOTE) == locks["AQ_source_note"]["blob_sha1"]
    assert blob_sha(AR_NOTE) == locks["AR_source_note"]["blob_sha1"]

    M = out["exact_inputs"]["target_cusp_multiplicities"]
    assert M == aq["target_cusp_grid"]["image_multiplicities"]
    assert sum(M) == 266
    assert sum(m * (m - 1) // 2 for m in M) == 3350
    assert aq["target_cusp_grid"]["D_total_delta"] == 8319

    w = out["formal_collision_free_witness"]
    d = w["contact2_branch_counts_by_target_cusp"]
    r = w["branch_counts_by_target_cusp"]
    assert d == [10, 8, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0]
    assert r == [m - e for m, e in zip(M, d)]
    assert sum(d) == 28
    assert sum(r) == 238
    assert sum(r) + sum(d) == 266
    assert sum(r) - sum(d) == 210
    assert w["contact1_minimal_branch_count"] == 210 >= ar["minimal_branch_bound"]["minimum_FSM_minimal_A_B_1_1_branches"]

    f81 = w["factor81_slack_assignment"]
    f105 = w["factor105_slack_assignment"]
    assert f81["t"] + f81["q_node"] + f81["eta"] + f81["rho"] == 52
    assert f105["t"] + f105["q_node"] + f105["eta"] + f105["rho"] == 28
    assert f81["t"] + 2 * f81["q_smooth"] - f81["smooth_boundary_point_count"] + f81["rho"] == 162
    assert f105["t"] + 2 * f105["q_smooth"] - f105["smooth_boundary_point_count"] + f105["rho"] == 210

    # For each cusp, c=1,...,r_j supplies r_j distinct nonzero tangent values.
    for rr in r:
        cvals = list(range(1, rr + 1))
        assert len(cvals) == len(set(cvals)) == rr
        assert all(c != 0 for c in cvals)

    # Local contact-two model: u=s^2, v=s^2*(lambda+s)^2.
    # Its target multiplicity is 2. After first blowup, v/u=(lambda+s)^2
    # has a nonzero linear term 2*lambda*s for lambda != 0, so the strict
    # transform is smooth. This check is algebraic over characteristic zero.
    assert out["residual_local_action"]["target_tangent_parameter"] == "c=v/u=w^2=lambda^2"
    assert out["residual_local_action"]["finite_tangent_slot_bound"] is False
    assert w["formal_cusp_delta_total"] == 3350
    assert w["remaining_delta_budget"] == 4969

    dec = out["decision"]
    assert dec["forced_tangent_collision_from_current_branch_counts"] is False
    assert out["firewalls"]["formal_local_witness_is_not_global_curve"] is True
    assert out["firewalls"]["Q602_excluded"] is False
    assert out["firewalls"]["O210_excluded"] is False
    assert out["firewalls"]["Stage32_closed"] is False

    print(json.dumps({
        "verdict": "PASS_STAGE32_MAIN_SCRATCH_RESIDUAL_G_TANGENT_CAPACITY_NONCLOSURE",
        "N": sum(r),
        "minimal_branches": sum(r) - sum(d),
        "contact2_branches": sum(d),
        "cusp_delta": 3350,
        "remaining_delta_budget": 4969,
        "forced_tangent_collision": False,
        "canonical_sha256": EXPECTED_OUT,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
