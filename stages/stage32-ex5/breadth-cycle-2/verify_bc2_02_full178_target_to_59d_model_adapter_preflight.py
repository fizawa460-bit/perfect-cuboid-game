#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "bc2-02-full178-target-to-59d-model-adapter-preflight.json"


def csha_without_field(obj: dict) -> str:
    x = dict(obj)
    expected = x.pop("canonical_sha256_without_this_field")
    actual = hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if actual != expected:
        raise AssertionError((actual, expected))
    return actual


def source(path: str) -> str:
    return (ROOT / path).read_text()


def require(text: str, *needles: str) -> None:
    for needle in needles:
        if needle not in text:
            raise AssertionError(f"missing source contract: {needle!r}")


def main() -> None:
    x = json.loads(ARTIFACT.read_text())
    assert x["schema"] == "STAGE32EX5_BC2_02_FULL178_TARGET_TO_59D_MODEL_ADAPTER_PREFLIGHT_V1"
    assert x["status"] == "PASS_PREFLIGHT_ARCHITECTURE_LOCALIZED_COMPLETION_BOUNDARY_EXPLICIT"
    csha_without_field(x)

    indexed = x["source_contracts"]["full178_indexed_terminal_family"]
    checkpoint = json.loads(source(indexed["checkpoint"]))
    assert checkpoint["indexed_reparameterization"]["random_access_unrank"] is True
    assert checkpoint["indexed_reparameterization"]["full_terminal_materialization_required"] is False
    assert checkpoint["symbolic_full178_prefix_census"]["row_count"] == 178
    assert checkpoint["symbolic_full178_prefix_census"]["terminal_count_total"] == indexed["terminal_count_total"]
    assert checkpoint["exact_terminal_family"]["assignment_order_known_labels_1based"] == indexed["assignment_order_known_labels_1based"]

    indexer = source(indexed["indexer"])
    require(
        indexer,
        "class CompressedTerminalIndexer:",
        "def unrank(self, rank: int)",
        "def rank(self, x: Sequence[int])",
        "terminal_predicate",
    )

    pic = x["source_contracts"]["picard64_integral_pairing_interface"]
    pairing = source(pic["pairing_prefix_engine"])
    require(
        pairing,
        "assert len(INDLIST) == 64",
        "def full_membership(self, selected_pairings: Sequence[int])",
        "def reconstruct_picard_basis(self, selected_pairings: Sequence[int])",
        "class PrefixMembershipOracle:",
    )
    hperp = source(pic["hperp_adapter"])
    require(
        hperp,
        "KNOWN_CURVE_COUNT = 140",
        "PICARD_RANK = 64",
        "class HperpIntegralPairingAdapter:",
        "all140 class coordinates are not integral in retained Picard basis",
    )

    direct = x["source_contracts"]["direct_slice_interface"]
    direct_src = source(direct["path"])
    require(
        direct_src,
        "slice_coordinates",
        '"degree", "exceptional_total", "first_normal_half_total"',
        "if rank != 3:",
        "historical_magma_gate_equivalent",
    )

    reynolds = x["source_contracts"]["reynolds_projection_interface"]
    reynolds_src = source(reynolds["path"])
    require(
        reynolds_src,
        "EXPECTED_FIXED_RANK = 5",
        "anti_rank = PICARD_RANK - fixed_rank",
        "GROUP_ORDER = 64",
    )

    affine = x["source_contracts"]["affine_59d_interface"]
    affine_src = source(affine["path"])
    require(
        affine_src,
        "EXPECTED_ANTI_RANK",
        '"all_integral_classes_with_projection_z": "x0(z)+K*t, t in Z^59"',
        '"pairing_x0_map"',
        '"K": K',
    )

    legacy = x["source_contracts"]["legacy_integer_solver_kernel"]
    legacy_src = source(legacy["path"])
    require(
        legacy_src,
        "def integerize_linear_ast",
        'SolverFor("QF_LIA")',
        '"witness_r_reduced"',
    )

    f = x["preflight_findings"]
    assert f["indexed_terminal_is_not_yet_a_full_picard_target"] is True
    assert f["direct_index_to_z_shortcut_authorized"] is False
    assert f["new_solver_from_scratch_required"] is False

    contract = x["minimal_adapter_contract"]
    assert "Picard64 completion" in contract["step_2_picard_completion"]
    assert "Reynolds projection" in contract["step_3_projection"]
    assert "x0(z)+K*t" in contract["step_4_59d_model"]
    assert "21az" in contract["step_4_59d_model"]

    assert x["next_exact_unit"]["id"] == "BC2_02_ONE_INDEXED_FULL178_TERMINAL_TO_PICARD64_COMPLETION_PROTOTYPE"
    assert x["next_exact_unit"]["heavy_compute_authorized"] is False
    assert x["merge_authorized"] is False
    assert all(v is False for v in x["credit_firewall"].values())

    print(json.dumps({
        "verdict": "PASS_BC2_02_FULL178_TARGET_TO_59D_MODEL_ADAPTER_PREFLIGHT",
        "canonical_sha256": x["canonical_sha256_without_this_field"],
        "next_exact_unit": x["next_exact_unit"]["id"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
