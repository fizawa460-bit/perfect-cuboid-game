#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import inspect
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
RESULT = HERE / "GATE-A-INTEGRAL-COMPLETION.json"
INTERFACE = ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
FAMILY = RESIDUAL / "compressed_terminal_family.py"
PREFIX = RESIDUAL / "pairing_prefix_engine.py"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"

EXPECTED_RESULT_CANON = "588ab6769610c3f93afcd5540db7e1c4404d2c6d1cf83caf5616c1fb6e21a3fe"
EXPECTED_INTERFACE_BLOB = "8a30e3aa30777460f344eb19836dc725dd442329"
EXPECTED_INTERFACE_CANON = "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6"
EXPECTED_FAMILY_BLOB = "90ff82ed312dcc0cb32cf207935945f550e29170"
EXPECTED_PREFIX_BLOB = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"
EXPECTED_BUNDLE_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
EXPECTED_BUNDLE_CANON = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
PARITY_SUPPORT = [1, 8, 9, 10]

sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(BUNDLE_DIR))
from compressed_terminal_family import terminal_predicate  # noqa: E402
from pairing_prefix_engine import PrefixMembershipOracle, RetainedBasisPairingTransform  # noqa: E402
import picard_base_rows_retained as retained_bundle  # noqa: E402


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def basis_vector(j: int, value: int = 1) -> list[int]:
    out = [0] * 11
    out[j] = value
    return out


def parity_kernel_basis() -> list[list[int]]:
    pivot = PARITY_SUPPORT[0]
    support = set(PARITY_SUPPORT)
    basis: list[list[int]] = []
    for j in range(11):
        if j not in support:
            basis.append(basis_vector(j))
    for j in PARITY_SUPPORT[1:]:
        v = basis_vector(j)
        v[pivot] = -1
        basis.append(v)
    basis.append(basis_vector(pivot, 2))
    req(len(basis) == 11, "parity-kernel basis rank")
    return basis


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    req(result.get("canonical_sha256_without_this_field") == EXPECTED_RESULT_CANON, "result stored canonical")
    req(canonical(result) == EXPECTED_RESULT_CANON, "result canonical")
    req(result.get("status") == "CANDIDATE_CLOSED_EXACT_PREFIX_LATTICE_EXTENSION_PENDING_CHAIN_AUDIT", "result status")

    req(git_blob(INTERFACE) == EXPECTED_INTERFACE_BLOB, "EX5 interface blob drift")
    req(git_blob(FAMILY) == EXPECTED_FAMILY_BLOB, "compressed terminal family blob drift")
    req(git_blob(PREFIX) == EXPECTED_PREFIX_BLOB, "pairing prefix engine blob drift")
    req(git_blob(BUNDLE_SOURCE) == EXPECTED_BUNDLE_BLOB, "Picard bundle loader blob drift")

    interface = json.loads(INTERFACE.read_text(encoding="utf-8"))
    req(interface.get("canonical_sha256_without_this_field") == EXPECTED_INTERFACE_CANON, "EX5 interface stored canonical")
    req(canonical(interface) == EXPECTED_INTERFACE_CANON, "EX5 interface canonical")
    req(interface["terminal_to_picard64_map"]["terminal_assignment_labels_1based"] == ASSIGNMENT_LABELS,
        "terminal assignment label drift")
    req(interface["reconstructed_picard64_coordinate_identity"]["selected64_inverse_denominator"] == 8,
        "selected64 denominator drift")
    req(interface["terminal_identity_or_exact_rank_unrank_contract"]["hpadj_membership_predicate"].startswith("terminal_predicate AND"),
        "HPADJ population must be a terminal_predicate subset")

    bundle = retained_bundle.load()
    req(bundle.get("canonical_sha256") == EXPECTED_BUNDLE_CANON, "Picard bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    req(transform.den == 8, "retained pairing transform denominator")
    selected_labels = list(transform.certificate["selected_known_indices_1based"])
    positions = [selected_labels.index(label) for label in ASSIGNMENT_LABELS]
    req(positions == interface["terminal_to_picard64_map"]["terminal_fixed_selected_positions_0based"],
        "terminal fixed selected-position identity")

    oracle = PrefixMembershipOracle(transform, positions)
    check = oracle.checks[10]
    req(check.depth == 11, "depth-11 oracle")
    req(check.modulus == 8, "depth-11 oracle modulus")
    req(len(check.coefficients) > 0, "depth-11 oracle must be nontrivial")

    # K = ker(x1+x8+x9+x10 mod 2) has index two in Z^11.  The listed
    # 11 vectors are a Z-basis for K.  If every basis vector is accepted by
    # the exact HNF extension oracle, then K is contained in the oracle
    # kernel.  Rejecting one odd-parity vector proves the oracle kernel is not
    # all of Z^11.  Since there is no subgroup strictly between an index-two
    # subgroup and Z^11, the two kernels are equal.
    k_basis = parity_kernel_basis()
    req(all(check.feasible(v) for v in k_basis), "parity kernel must lie in exact HNF extension kernel")
    odd = basis_vector(PARITY_SUPPORT[0])
    req(sum(odd[j] for j in PARITY_SUPPORT) % 2 == 1, "odd witness parity")
    req(not check.feasible(odd), "odd parity coset must be rejected by exact HNF oracle")

    predicate_src = "".join(inspect.getsource(terminal_predicate).split())
    req("if(x[1]+x[8]+x[9]+x[10])%2:" in predicate_src,
        "terminal_predicate parity source contract")

    proof = result["exact_proof"]
    req(proof["terminal_parity_condition"] == "x1+x8+x9+x10 == 0 (mod 2)", "recorded parity condition")
    req(proof["oracle_kernel_identification"].startswith("the depth-11 HNF oracle kernel equals"),
        "recorded oracle-kernel theorem")
    req(result["chain_handoff"]["gate_a_closed_for_research"] is True, "Gate A research closure")
    req(result["chain_handoff"]["next_gate"] == "B_EFFECTIVE_DIVISOR_EXISTENCE", "Gate A next gate")
    req(result["chain_handoff"]["full_chain_hostile_audit_required_before_main_consumption"] is True,
        "full-chain audit firewall")
    for key, value in result["firewalls"].items():
        req(value is False, f"unexpected Gate A credit/firewall true: {key}")

    print("PASS HPADJ07 Gate A: exact depth-11 Picard extension kernel equals terminal parity kernel; all charged terminals admit integral Picard64 completion; provisional chain evidence only")


if __name__ == "__main__":
    main()
