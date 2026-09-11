#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import z3
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
N260_STATE = HERE.parent / "N260/STATE.json"
N230_DIR = HERE.parent / "N230"
EX5_CONSUMER = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_02_exact_witness_to_node_support.py"
NODE_BRIDGE = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-01b-runtime-node-coordinate-bridge.json"

sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(N230_DIR))

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import RetainedBasisPairingTransform
from n220_filtered_terminal_indexer import N220FilteredTerminalIndexer

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_N341_RUN = 34424019499
EXPECTED_N341_JOB = 102705288033
EXPECTED_N341_CANONICAL = "672ca52e1b71e7bde2b14de6320ae57dddcbf6f0d3817f3244f27eec20cce315"
EXPECTED_N341_VERIFIER_BLOB = "70d17967f7a965de4994dce1bc70a398468ef42e"
EXPECTED_EX5_AUDITED_HEAD = "a5e59bab3f7fe5a31e356c5a78edcbd741b093a6"
EXPECTED_EX5_CONSUMER_BLOB = "5941a6270def08a614797be84b3242aaa83def72"
EXPECTED_NODE_BRIDGE_BLOB = "2a14a683e8ec38ec993eb711841c466f2be6eb06"
EXCEPTIONAL_LABELS = list(range(93, 141))
NORMAL_LABELS = list(range(1, 93))
X4_LABEL = 49

TARGETS = [
    {
        "row_id": "g0-d176",
        "genus": 0,
        "degree": 176,
        "e": 48,
        "normal_mass": 3104,
        "x4_max": 84,
        "sat": {
            3: "af14c80005effea74980d1726f8318d6a6dd574833787fdbb47b1bf9701e238f",
            7: "a0496f7430a2f07fc4de6651796c6d0c4cc523c9c9485e572eebabaae693c3d7",
            11: "9c4379ff98f036b324c7095e8e99f4f897741ef2ff0837275386ceef746370b5",
            15: "3cafb39656a9297e39c25ee7ab5cc93ea5efb5cbdb017fa2c4d3b4f8d683c2c9",
            19: "8d8d95f3230cd1cdae2b8bb581c686246ae4a729120083548eb57059db4b2674",
            23: "8420fc0c5f1460a24e54320daca22274db26f08777c5b8f54940091445a8d00e",
            27: "89ddc8521c0f38298a61608f702823dad94ab16db0d9ac00851abeb77ecc0c2a",
            31: "2a548e9dd7e188fec948c08ef529a2242ad71e516d19ea593aad40147f2bc8f5",
            35: "e767cd2c4dd5081cdedfbe9f52df2b8a719b6184e8b556648bc771ddac03abec",
            39: "0cfe683d39b76551ea4cdbd63509783029850a650939c2cea95e0f726764058e",
        },
    },
    {
        "row_id": "g1-d192",
        "genus": 1,
        "degree": 192,
        "e": 48,
        "normal_mass": 3408,
        "x4_max": 92,
        "sat": {
            3: "057f9a915df413cf38b14309a807b5857674d3931addbeaa0f523b55ed339f85",
            7: "8aa788124bee0488136bfe88fc1cb7facae183e625577a8d7bfe492740177ae2",
            11: "826292a5668d1515a082d901ffef612419a5952e30600a93895be5e84d3eee53",
            15: "596c2b8374de6e4e7a467a7d675e34d624eac38d4c8b7d55f6387839a55fecc0",
            19: "2c037bc2e12f15a11cbb3c7633c2d183984121e823882898c730e1182e74876c",
            23: "5f6870d69e12386831c9e5e08381cd354bed157684f68100128709ad0e0ef34d",
            27: "36f9e538dc75cb24a613658104ad78c894ca5e4bf17c2fdf09b3f9436dee1291",
            31: "f8746b708725aad0cb1f8e3c279912e07f98db6d7aad98ae515f6c75ddcd3766",
            35: "30c3b0bcd5a50e4a9ad4d946035f31892b27a20af83bdf6658bb48dec2f7cea3",
            39: "b1e3e148fe0e91119d288d6941604663bc32d9d2f693a3d3aa5493198af5504f",
            43: "d85cf1bf2bccd7d4c0133bae8a5d8715469cab4b43cb2a85e9edc2fb290762ef",
        },
    },
]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def sha256_json(value: object) -> str:
    return csha(value)


def load_module(path: Path, name: str):
    if not path.exists():
        raise FileNotFoundError(
            f"required retained EX5 consumer missing at {path}; run on the PR merge/current-main integration surface"
        )
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import module: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_retained(path: Path, name: str) -> dict:
    mod = load_module(path, name)
    payload = mod.load()
    if not isinstance(payload, dict):
        raise ValueError(f"retained payload is not dict: {path}")
    return payload


def zsum(coeffs, vars_):
    return z3.Sum([int(a) * v for a, v in zip(coeffs, vars_)])


def ints(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
    out = []
    for i in range(v.rows):
        q = Rational(v[i, 0])
        if q.q != 1:
            raise ValueError(f"nonintegral coordinate at {i}: {q}")
        out.append(int(q))
    return out


def derive_reduced_witness(*, x: Matrix, data: dict, U: Matrix, kernel_reduced: Matrix) -> tuple[list[int], list[int]]:
    z = data["C"] * x
    x0 = data["x0_map"] * z
    q = x - x0
    if data["C"] * q != Matrix.zeros(5, 1):
        raise ValueError("derived correction is not in affine kernel")
    _, pivot_rows = kernel_reduced.T.rref()
    pivot_rows = list(pivot_rows)
    if len(pivot_rows) != 59:
        raise ValueError(f"reduced kernel row-rank regression: {len(pivot_rows)}")
    square = kernel_reduced.extract(pivot_rows, list(range(59)))
    qsel = q.extract(pivot_rows, [0])
    r = square.inv() * qsel
    if kernel_reduced * r != q:
        raise ValueError("59D witness reconstruction regression")
    return ints(z), ints(r)


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260" or n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 [1]^48 authority regression")

    bundle = load_retained(RETAINED, "s32_n342_bundle")
    marking = load_retained(MARKING, "s32_n342_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    if transform.den != 8:
        raise ValueError("selected64 denominator regression")
    selected_labels = list(transform.certificate["selected_known_indices_1based"])
    if len(selected_labels) != 64 or sum(1 for v in selected_labels if v > 92) != 29:
        raise ValueError("selected64 partition regression")

    data = reconstruct_translation_data(marking, bundle)
    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    selected_M = M.extract(list(pivots), list(range(59)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform reconstruction regression")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("59D reduced-coordinate transform is not unimodular")
    kernel_reduced = data["K"] * U
    Mred = M * U

    ex5 = load_module(EX5_CONSUMER, "s32_n342_ex5_consumer")
    bridge_rows, bridge_canonical = ex5.load_node_bridge(NODE_BRIDGE)
    bridge_raw = json.loads(NODE_BRIDGE.read_text())
    bridge_claimed = bridge_raw.get("canonical_sha256_without_this_field")
    if bridge_claimed is not None:
        bridge_body = dict(bridge_raw)
        bridge_body.pop("canonical_sha256_without_this_field", None)
        if csha(bridge_body) != bridge_claimed:
            raise ValueError("node bridge canonical regression")
    if bridge_canonical != bridge_claimed:
        raise ValueError("EX5 consumer node-bridge canonical disagreement")

    yn = [z3.Int(f"yn_{j}") for j in range(35)]
    yexpr = [z3.IntVal(1) for _ in range(29)] + yn
    B = transform.inverse_integer
    P = adapter.pairing_matrix
    num_expr = [zsum([B[i, j] for j in range(64)], yexpr) for i in range(64)]
    pairing_num = [zsum([P[r, i] for i in range(64)], num_expr) for r in range(140)]

    base = z3.SolverFor("QF_LIA")
    for expr in num_expr:
        base.add(expr % 8 == 0)
    for label in EXCEPTIONAL_LABELS:
        base.add(pairing_num[label - 1] == 8)
    for label in NORMAL_LABELS:
        base.add(pairing_num[label - 1] >= 0)
    normal_total_num = z3.Sum([pairing_num[label - 1] for label in NORMAL_LABELS])
    x4_num = pairing_num[X4_LABEL - 1]

    gram = Matrix(bundle["picard_gram_64x64"])
    phi = Matrix([
        list(data["bridge"].degree_functional),
        list(data["bridge"].exceptional_mass_functional),
        list(data["bridge"].first_normal_half_functional),
    ])

    rows = []
    sat_total = unsat_total = unknown_total = 0
    self_square_pass_total = 0
    support48_total = 0
    spans_p6_total = 0

    for target in TARGETS:
        row_id = str(target["row_id"])
        genus = int(target["genus"])
        degree = int(target["degree"])
        e = int(target["e"])
        mass = int(target["normal_mass"])
        expected_sat = {int(k): v for k, v in target["sat"].items()}
        indexer = N220FilteredTerminalIndexer(genus, degree, e)
        if indexer.accepted_exceptional_count != 1:
            raise ValueError(f"N260 one-exceptional-block regression for {row_id}")

        base.push()
        for v in yn:
            base.add(v >= 0, v <= mass)
        base.add(normal_total_num == 8 * mass)

        observed_sat = []
        for x4 in range(int(target["x4_max"]) + 1):
            base.push()
            base.add(x4_num == 8 * x4)
            result = base.check()
            if result == z3.sat:
                sat_total += 1
                observed_sat.append(x4)
                model = base.model()
                yvals = [1] * 29 + [int(model.eval(v, model_completion=True).as_long()) for v in yn]
                if not transform.full_membership(yvals):
                    raise ValueError("SAT selected64 membership replay regression")
                xvals = transform.reconstruct_picard_basis(yvals)
                pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
                if pairings[92:] != [1] * 48:
                    raise ValueError("SAT exceptional replay regression")
                if min(pairings[:92]) < 0 or sum(pairings[:92]) != mass or pairings[X4_LABEL - 1] != x4:
                    raise ValueError("SAT normal/x4 replay regression")
                n341_witness_sha = csha({
                    "selected64_pairings": yvals,
                    "picard_coordinates": xvals,
                    "all140_pairings": pairings,
                })
                if x4 not in expected_sat:
                    raise ValueError(f"unexpected N341 SAT at {row_id}/x4={x4}")
                if n341_witness_sha != expected_sat[x4]:
                    raise ValueError(
                        f"N341 SAT witness hash drift at {row_id}/x4={x4}: {n341_witness_sha} != {expected_sat[x4]}"
                    )

                x = Matrix(xvals)
                zvals, rvals = derive_reduced_witness(x=x, data=data, U=U, kernel_reduced=kernel_reduced)
                z = Matrix(zvals)
                r = Matrix(rvals)
                if data["N"] * x != data["B"] * z:
                    raise ValueError("Reynolds numerator replay regression")
                y0 = data["pairing_x0_map"] * z
                if y0 + Mred * r != Matrix(pairings):
                    raise ValueError("59D pairing replay regression")

                slice_values = ints(phi * x)
                if slice_values[0] != degree or slice_values[1] != e:
                    raise ValueError(f"slice d/e regression at {row_id}/x4={x4}: {slice_values}")
                a = int(slice_values[2])

                terminal_pairings = list(indexer.unrank(x4))
                if terminal_pairings[4] != x4:
                    raise ValueError("filtered rank / x4 identity regression")
                old_rank = int(indexer.old_rank_of_filtered(x4))
                disposition = indexer.disposition_of_old(old_rank)
                if disposition.get("disposition") != "N220_SURVIVOR" or int(disposition["filtered_rank"]) != x4:
                    raise ValueError("old-rank locator replay regression")

                evidence = {
                    "target": {
                        "row_id": row_id,
                        "e": e,
                        "a": a,
                        "z": zvals,
                    },
                    "result": {
                        "status": "SAT",
                        "witness_r_reduced": rvals,
                    },
                }
                support = ex5.reconstruct(evidence, bundle, marking, bridge_rows)
                if support.get("status") != "PASS_EXACT_WITNESS_TO_NODE_SUPPORT":
                    raise ValueError(f"EX5 consumer failed at {row_id}/x4={x4}")
                if support["reconstruction"]["picard_coordinates_sha256"] != sha256_json(xvals):
                    raise ValueError("EX5 consumer Picard witness hash mismatch")
                exceptional = support["exceptional_support"]
                if exceptional["pairings_last48"] != [1] * 48:
                    raise ValueError("EX5 exact replay lost [1]^48 exceptional vector")
                if int(exceptional["support_count"]) != 48:
                    raise ValueError("EX5 exact replay support-count regression")
                support48_total += 1
                if bool(exceptional["spans_p6"]):
                    spans_p6_total += 1

                self_square = int((x.T * gram * x)[0])
                required_lower = -degree - 2 + 2 * genus
                self_square_pass = self_square >= required_lower
                if self_square_pass:
                    self_square_pass_total += 1

                rows.append({
                    "row_id": row_id,
                    "g": genus,
                    "d": degree,
                    "e": e,
                    "filtered_rank": x4,
                    "old_terminal_rank": old_rank,
                    "terminal_pairings": terminal_pairings,
                    "x4": x4,
                    "n341_witness_sha256": n341_witness_sha,
                    "picard_coordinates_sha256": sha256_json(xvals),
                    "z": zvals,
                    "a": a,
                    "witness_r_reduced": rvals,
                    "witness_r_reduced_sha256": sha256_json(rvals),
                    "all140_pairings_sha256": sha256_json(pairings),
                    "self_square": self_square,
                    "required_self_square_lower": required_lower,
                    "chosen_picard_model_self_square_pass": self_square_pass,
                    "node_support": {
                        "consumer_status": support["status"],
                        "pairings_last48_sha256": exceptional["pairings_last48_sha256"],
                        "support_count": int(exceptional["support_count"]),
                        "zero_indices_0based": exceptional["zero_indices_0based"],
                        "canonical_node_vector_rank": int(exceptional["canonical_node_vector_rank"]),
                        "projective_span_dimension": int(exceptional["projective_span_dimension"]),
                        "spans_p6": bool(exceptional["spans_p6"]),
                    },
                })
            elif result == z3.unsat:
                unsat_total += 1
                if x4 in expected_sat:
                    raise ValueError(f"expected N341 SAT became UNSAT at {row_id}/x4={x4}")
            else:
                unknown_total += 1
            base.pop()
        base.pop()

        if observed_sat != sorted(expected_sat):
            raise ValueError(f"N341 SAT x4 ledger drift for {row_id}: {observed_sat} != {sorted(expected_sat)}")

    if (sat_total, unsat_total, unknown_total) != (21, 157, 0):
        raise ValueError(f"N341 aggregate drift: {(sat_total, unsat_total, unknown_total)}")
    if len(rows) != 21 or support48_total != 21 or spans_p6_total != 21:
        raise ValueError("N342 exact support aggregate regression")

    body = {
        "schema": "STAGE32_32_01_178_N342_N341_SAT_TO_59D_NODE_SUPPORT_V1",
        "source_scope": "exact 21 N341 integral-Picard SAT terminals only",
        "source_locks": {
            "n341_run_id": EXPECTED_N341_RUN,
            "n341_job_id": EXPECTED_N341_JOB,
            "n341_canonical_sha256": EXPECTED_N341_CANONICAL,
            "n341_verifier_blob_sha1": EXPECTED_N341_VERIFIER_BLOB,
            "retained_bundle_canonical_sha256": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical_sha256": EXPECTED_MARKING_CANONICAL,
            "ex5_audited_head": EXPECTED_EX5_AUDITED_HEAD,
            "ex5_exact_witness_consumer_blob_sha1": EXPECTED_EX5_CONSUMER_BLOB,
            "node_bridge_blob_sha1": EXPECTED_NODE_BRIDGE_BLOB,
            "node_bridge_canonical_sha256": bridge_canonical,
        },
        "n341_replay": {
            "candidate_count": sat_total + unsat_total + unknown_total,
            "sat_count": sat_total,
            "unsat_count": unsat_total,
            "unknown_count": unknown_total,
            "all_21_logged_sat_witness_hashes_replayed_exactly": True,
        },
        "handoff": {
            "count": len(rows),
            "all_have_exact_old_rank_locator": True,
            "all_have_exact_terminal_pairings_11": True,
            "all_have_z5": all(len(row["z"]) == 5 for row in rows),
            "all_have_integral_r59": all(len(row["witness_r_reduced"]) == 59 for row in rows),
            "all_replay_reynolds_numerator": True,
            "all_replay_all140_from_r59": True,
            "all_replay_through_retained_ex5_consumer": True,
            "all_have_exact_full48_labelled_support": support48_total == 21,
            "all_full48_support_spans_p6": spans_p6_total == 21,
            "chosen_picard_models_meeting_self_square_threshold": self_square_pass_total,
            "rows": rows,
        },
        "interpretation": {
            "n341_unsat_157_are_exact_integral_picard_noncompletions_at_n341_scope": True,
            "n341_sat_21_are_now_materialized_as_exact_picard64_plus_reynolds59d_witnesses": True,
            "labelled_node_support_is_replayed_not_inferred_from_scalar_e": True,
            "full48_support_does_not_supply_a_genus0_btva_rejection": True,
            "full48_support_does_not_supply_a_genus1_btva_rejection": True,
            "chosen_model_self_square_failure_if_any_is_not_terminal_unsat": True,
            "picard_numerical_class_is_not_effective_curve_existence": True,
            "n260_n310_n341_hostile_audits_still_required_before_main_credit": True,
            "production_leaf_contract_not_registered_by_this_node": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    canonical = csha(body)
    print(json.dumps({**body, "canonical_sha256_without_this_field": canonical}, sort_keys=True))


if __name__ == "__main__":
    main()
