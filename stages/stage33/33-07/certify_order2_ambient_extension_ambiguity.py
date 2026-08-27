#!/usr/bin/env python3
"""Certify that endpoint module data alone leave the finite delta_loc arbitrary.

For the exact Stage33-07 finite diagnostic we have a trivial V4 source
Q=F2^26 and kernel K=Br(Sbar)[2]=F2^14.  Equivalence classes of V4-module
extensions

    0 -> K -> M -> Q -> 0

with the endpoint modules fixed are

    Ext^1_{F2[V4]}(Q,K) ~= H^1(V4,K)^26 ~= F2^(16*26).

The connecting map Q=H^0(V4,Q) -> H^1(V4,K) is precisely the extension
class, column by column.  This script does not merely record that abstract
identity: it constructs all 416 elementary nonsplit extensions using the
locked H1 quotient representatives and feeds every one through the independent
ambient-extension adapter.  Each elementary 16x26 matrix must be recovered
exactly.

This is a negative-but-sharp exact leaf.  It proves that dimensions, endpoint
V4 actions, and exactness cannot determine even one bit of the project
localization matrix.  Geometric lift/action data (or an equivalent real
ambient Gersten/Kummer module) are genuinely necessary.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ADAPTER_PATH = HERE / "materialize_order2_localization_extension_from_ambient.py"
RECEIVER_PATH = HERE / "order2-localization-receiver.json"
BR2_PATH = HERE / "proper-brauer2-from-discriminant.json"
OUTPUT = HERE / "order2-ambient-extension-ambiguity.json"

KDIM, QDIM, H1DIM, MDIM = 14, 26, 16, 40


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def normalized_text_sha256(path):
    """Hash source semantics, independent of Windows CRLF checkout policy."""
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_locked(path):
    x = json.loads(path.read_text(encoding="utf-8"))
    claimed = x.get("canonical_sha256")
    body = dict(x)
    body.pop("canonical_sha256", None)
    actual = canonical_sha256(body)
    if not claimed or claimed != actual:
        raise SystemExit(f"canonical source lock failed for {path.name}")
    return x


def load_adapter():
    spec = importlib.util.spec_from_file_location("stage33_order2_ambient_adapter", ADAPTER_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load ambient adapter")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def build_ambient(adapter, br2, receiver, target16x26):
    """Build the block extension whose connecting matrix is target16x26."""
    h1 = [[int(x) & 1 for x in row]
          for row in receiver["finite_receiver_H1_quotient_representatives_f2_28"]]
    if len(h1) != H1DIM or any(len(row) != 2 * KDIM for row in h1):
        raise SystemExit("receiver H1 representative shape regression")

    ecc = [[0] * KDIM for _ in range(QDIM)]
    ect = [[0] * KDIM for _ in range(QDIM)]
    for source in range(QDIM):
        pair = [0] * (2 * KDIM)
        for h in range(H1DIM):
            if target16x26[h][source]:
                pair = xor(pair, h1[h])
        ecc[source] = pair[:KDIM]
        ect[source] = pair[KDIM:]

    kcc = [[int(x) & 1 for x in row] for row in br2["proper_Br2_cc_action_f2"]]
    kct = [[int(x) & 1 for x in row] for row in br2["proper_Br2_ct_action_f2"]]
    inc = [eye(KDIM)[i] + [0] * QDIM for i in range(KDIM)]
    proj = [[0] * QDIM for _ in range(KDIM)] + eye(QDIM)

    def block_action(k, defects):
        # Row-vector convention on basis [K,Q].  A quotient basis row has
        # action q |-> q + defect(q), so the lower-left block is defects.
        return (
            [row + [0] * QDIM for row in k]
            + [defects[i] + eye(QDIM)[i] for i in range(QDIM)]
        )

    ambient = {
        "schema": "STAGE33_07_ORDER2_AMBIENT_V4_EXTENSION_V1",
        "kernel_dimension_f2": KDIM,
        "quotient_dimension_f2": QDIM,
        "ambient_dimension_f2": MDIM,
        "quotient_V4_action": "TRIVIAL",
        "kernel_inclusion_f2": inc,
        "quotient_projection_f2": proj,
        "ambient_cc_action_f2": block_action(kcc, ecc),
        "ambient_ct_action_f2": block_action(kct, ect),
    }
    return ambient


def zero_target():
    return [[0] * QDIM for _ in range(H1DIM)]


def main():
    receiver = load_locked(RECEIVER_PATH)
    br2 = load_locked(BR2_PATH)
    adapter = load_adapter()

    if receiver.get("finite_source_order2_dimension_f2") != QDIM:
        raise SystemExit("source dimension regression")
    if receiver.get("finite_receiver_module_dimension_f2") != KDIM:
        raise SystemExit("kernel dimension regression")
    if receiver.get("finite_receiver_H1_dimension_f2") != H1DIM:
        raise SystemExit("H1 dimension regression")
    if br2.get("proper_geometric_Br2_dimension_f2") != KDIM:
        raise SystemExit("proper Br2 dimension regression")

    # Recheck the 16 chosen quotient representatives are independent modulo B1.
    b1 = [[int(x) & 1 for x in row]
          for row in receiver["finite_receiver_B1_basis_f2_28"]]
    h1 = [[int(x) & 1 for x in row]
          for row in receiver["finite_receiver_H1_quotient_representatives_f2_28"]]
    if adapter.rank2(b1, 2 * KDIM) != 4:
        raise SystemExit("B1 rank regression")
    if adapter.rank2(b1 + h1, 2 * KDIM) != 20:
        raise SystemExit("H1 quotient representative rank regression")

    checked = 0
    aggregate = hashlib.sha256()
    first_nonzero_examples = []
    for h in range(H1DIM):
        for source in range(QDIM):
            target = zero_target()
            target[h][source] = 1
            ambient = build_ambient(adapter, br2, receiver, target)
            got = adapter.compute(ambient, receiver, br2)
            if got["connecting_map_delta_loc_f2_16x26"] != target:
                raise SystemExit(
                    f"elementary extension recovery failed H1={h+1} source={source+1}"
                )
            if got["connecting_map_rank_f2"] != 1:
                raise SystemExit("elementary extension unexpectedly has rank != 1")
            if got["nonzero_source_columns_1based"] != [source + 1]:
                raise SystemExit("elementary extension support regression")
            aggregate.update(bytes([h, source]))
            aggregate.update(bytes(sum(target, [])))
            checked += 1
            if len(first_nonzero_examples) < 4:
                first_nonzero_examples.append({
                    "receiver_coordinate_1based": h + 1,
                    "source_coordinate_1based": source + 1,
                    "recovered_rank_f2": 1,
                })

    if checked != H1DIM * QDIM:
        raise SystemExit("elementary extension census incomplete")

    ambiguity_dim = H1DIM * QDIM
    cert = {
        "schema": "STAGE33_07_ORDER2_AMBIENT_EXTENSION_AMBIGUITY_V1",
        "source_locks": {
            "receiver_canonical_sha256": receiver["canonical_sha256"],
            "proper_br2_canonical_sha256": br2["canonical_sha256"],
            "ambient_adapter_file_sha256": normalized_text_sha256(ADAPTER_PATH),
        },
        "endpoint_module_statement": {
            "kernel": "proper Br(Sbar)[2]",
            "kernel_dimension_f2": KDIM,
            "quotient": "A[2] finite diagnostic residue quotient",
            "quotient_dimension_f2": QDIM,
            "quotient_v4_action": "TRIVIAL",
            "finite_h1_dimension_f2": H1DIM,
        },
        "extension_classification": {
            "identity": "Ext^1_F2[V4](F2^26,K) ~= H^1(V4,K)^26 ~= Hom_F2(F2^26,H^1(V4,K))",
            "extension_equivalence_space_dimension_f2": ambiguity_dim,
            "extension_equivalence_class_count": "2^416",
            "connecting_matrix_space_dimension_f2": ambiguity_dim,
            "connecting_matrix_shape": [H1DIM, QDIM],
            "connecting_map_is_extension_class_columnwise": True,
        },
        "exhaustive_basis_adapter_check": {
            "elementary_extensions_checked": checked,
            "expected_elementary_extensions": ambiguity_dim,
            "all_416_elementary_16x26_matrices_recovered_exactly": True,
            "elementary_test_aggregate_sha256": aggregate.hexdigest(),
            "sample_elementary_extensions": first_nonzero_examples,
        },
        "exact_consequence": {
            "all_2pow416_connecting_matrices_occur_for_some_abstract_endpoint_compatible_extension": True,
            "endpoint_dimensions_and_v4_actions_determine_any_delta_loc_entry": False,
            "endpoint_dimensions_and_v4_actions_bound_project_delta_loc_rank_below_16": False,
            "real_geometric_extension_data_is_logically_necessary": True,
        },
        "project_status": {
            "project_ambient_gersten_v4_extension_materialized": False,
            "project_finite_v4_delta_loc_matrix_computed": False,
            "project_absolute_delta_loc_computed": False,
            "absolute_h1_identified_with_finite_v4_h1": False,
            "arithmetic_hs_closed": False,
            "stage33_progress": "6/11",
            "stage33_08_released": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "new_smallest_exact_kernel": "R33-BR2A-REAL-GEOMETRIC-GERSTEN-V4-EXTENSION-DATA",
        "next_exact_leaf": "L33-07-MATERIALIZE-REAL-GEOMETRIC-RESIDUE-LIFT-V4-EXTENSION-OR-26-CHOOSEN-LIFT-COCYCLES",
    }
    cert["canonical_sha256"] = canonical_sha256(cert)
    OUTPUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "ambiguity_dimension_f2": ambiguity_dim,
        "elementary_extensions_checked": checked,
        "all_connecting_matrices_abstractly_possible": True,
        "project_delta_loc_computed": False,
        "new_smallest_exact_kernel": cert["new_smallest_exact_kernel"],
        "certificate_sha256": cert["canonical_sha256"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
